import sys
import os
import win32api
import win32con
import glob
# print(123)
#
sSrcFile=[]
sLIB=[]
sDLL=[]
sInclude=[]
slibFolder=[]
sIncludefolder=[]

def findAllSrcFile(ab_dir):#src目录下的所有文件及其子目录内的文件
    sSrc=glob.glob(ab_dir)
    if not sSrc:
        return 0
    for file in sSrc:
        if os.path.isfile(file) and (('.c' in file)or('.cpp' in file)) and 'pyc' not in file:
            sSrcFile.append(file)
        elif os.path.isdir(file):#这时候需要继续迭代
            path = file + '/*'
            findAllSrcFile(path)

def findALLLibFile(ab_dir):
    sLib = glob.glob(ab_dir)
    if not sLib:
        return 0
    for file in sLib:
        if os.path.isfile(file) and '.lib' in file:
            sLIB.append(file)
            slibFolder.append(os.path.split(file)[0])
        elif os.path.isdir(file):  # 这时候需要继续迭代
            slibFolder.append(file)
            path = file + '/*'
            findALLLibFile(path)

def findALLDllFile(ab_dir):
    sDll = glob.glob(ab_dir)
    if not sDll:
        return 0
    for file in sDll:
        if os.path.isfile(file) and '.dll' in file:
            sDLL.append(file)
        elif os.path.isdir(file):  # 这时候需要继续迭代
            path = file+'/*'
            findALLDllFile(path)

def findALLIncludeFile(ab_dir):
    sinclude_ = glob.glob(ab_dir)
    if not sinclude_ :
        return 0
    for file in sinclude_ :
        if os.path.isfile(file) and (('.h' in file)or('.c' in file)or('.hpp' in file)):
            sInclude.append(file)
            sIncludefolder.append(os.path.split(file)[0])
        elif os.path.isdir(file):  # 这时候需要继续迭代
            sIncludefolder.append(file)
            path = file+'/*'
            findALLIncludeFile(path)


def WriteMake():
    s=sys.argv
    x,projectFiledir,filedir=s
    projectName=projectFiledir[projectFiledir.rfind('\\')+1:]
    #找出项目绝对路径
    ab_dir=s[1]
    print('项目绝对路径:',ab_dir)
    findAllSrcFile(ab_dir+'/src/*')
    findAllSrcFile(ab_dir+'/MyTool/src/*')
    findALLLibFile(ab_dir+'/bin/*')
    findALLDllFile(ab_dir+'/bin/*')
    findALLIncludeFile(ab_dir+'/include/*')
    findALLIncludeFile(ab_dir+'/MyTool/include/*')

    findALLLibFile('E:/frequentlyUsedCPPLibrary/bin/*')
    findALLDllFile('E:/frequentlyUsedCPPLibrary/bin/*')
    findALLIncludeFile('E:/frequentlyUsedCPPLibrary/include/*')
    print('项目源文件集合:',sSrcFile)
    print('项目动态库文件集合:',sDLL)
    print('项目静态库文件集合:',sLIB)
    print('项目头文件夹集合:',sInclude)
    print('项目库文件夹集合:',slibFolder)
    print('项目头文件夹集合:',sIncludefolder)
    str_='add_executable({}\n'.format(projectName)
    for srcFile in set(sSrcFile):
        srcFile=srcFile.replace('\\','/')
        str_+=srcFile+'\n'
    for header in set(sInclude):
        header=header.replace('\\','/')
        str_ += header + '\n'
    str_+='D:/ProgramData/Anaconda3/include/Python.h'+'\n'
    str_+=')\n'
    str_.replace('i','iiiiiiiiiiii')
    with open(ab_dir+'/CMakeLists.txt','w')as f:
        f.write('cmake_minimum_required(VERSION 3.14)\n')
        f.write('project({})\n'.format(projectName))
        f.write('set(CMAKE_CXX_STANDARD 17)\n')
        f.write('set(CMAKE_EXE_LINKER_FLAGS "-static-libgcc -static-libstdc++")\n')
        f.write('include_directories(include)\n')
        f.write('include_directories(D:/ProgramData/Anaconda3/include)\n')#还要把python的inlcude文件夹添加进来，因为有可能和python交互，用到python.h
        for dir in set(sIncludefolder):
            dir=dir.replace('\\','/')
            f.write('include_directories({})\n'.format(dir))
        f.write('link_directories(bin)\n')
        f.write('link_directories(D:/ProgramData/Anaconda3/libs)\n')#还要把python的inlcude文件夹添加进来，因为有可能和python交互，用到python36.lib
        for dir in set(slibFolder):
            dir=dir.replace('\\','/')
            f.write('include_directories({})\n'.format(dir))
        f.write(str_)#add_executable信息
        str1_='TARGET_LINK_LIBRARIES({}'.format(projectName)+' \n'
        for lib in set(sLIB):
            lib=lib.replace('\\','/')
            str1_+=lib+'\n'
        str1_+='python36.lib'+'\n'#添加这个东西
        str1_+=')\n'
        f.write('{}'.format(str1_))
        str1_='TARGET_LINK_LIBRARIES({}'.format(projectName)+' \n'
        for dll in set(sDLL):
            dll=dll.replace('\\','/')
            str1_+=dll+'\n'
        str1_+=')\n'
        f.write('{}'.format(str1_))
# readMake()

def getRidOfTextBetweenSth(str_,sign):
    left_sign_counter = 0
    right_sign_counter = 0
    startloc = 0
    endloc = 0
    if sign=='{' or sign=='}':
        left_sign='{'
        right_sign='}'
        for index,i in enumerate(str_):
            if i == left_sign:
                print(1)
                left_sign_counter += 1
                if left_sign_counter == 1:
                    startloc = index
                    print(22222222)
                    print(startloc)
            elif i == right_sign:
                print(2)
                right_sign_counter += 1
                if left_sign_counter == right_sign_counter:
                    endloc = index
                    print(22222222)
                    print(endloc)
                    break
    elif sign=='\'':
        left_sign='\''
        right_sign='\''
    elif sign=='\"':
        left_sign='\"'
        right_sign='\"'
    print(str_[startloc:endloc])



def gen_str_to_write_in_headerfile(sourceFilePath):
    str_=[]
    attetionMark=False
    with open(sourceFilePath,'r',encoding='utf-8')as f:
        datas=f.readlines()
    sData=[line for line in datas if '#include' not in line]
    str_="".join(sData)
    
    
    
    
    # str_=getRidOfTextBetweenSth(str_,"\"")
    # str_=getRidOfTextBetweenSth(str_,"\'")
    str_=getRidOfTextBetweenSth(str_,"{")



def autoReplenishFile():
    s = sys.argv
    projectDir=s[1]
    projectName=projectDir.split('\\')[-1]
    # sInclude = []
    #检查所有源文件是否有对应的头文件
    for file in sSrcFile:
        if 'main.cpp' not in file:
            corresponding_header=file.replace('src','include').replace('.cpp','.h')
            sfolder=corresponding_header.split('\\')
            s=[]
            for folder in sfolder:
                s.extend(folder.split('/'))
            if not os.path.isfile(corresponding_header):#没有这些文件，应该新建
                fileName=corresponding_header.split('\\')[-1].replace('.h','')
                sFolder = s
                sFolder=sFolder[sFolder.index(projectName):-1]
                print('sFolder:',sFolder)
                with open(corresponding_header,'w')as f:
                    str_='#ifndef '
                    for folder in sFolder:
                        str_+=folder.upper()+'_'
                    str_+=fileName.upper()
                    str_+='_H\n'
                    f.write(str_)

                    str_='#define '
                    for folder in sFolder:
                        str_+=folder.upper()+'_'
                    str_+=fileName.upper()
                    str_+='_H\n'
                    f.write(str_)

                    str_='#endif'
                    f.write(str_)






def main():
    WriteMake()
    autoReplenishFile()
    WriteMake()
# main()
gen_str_to_write_in_headerfile('E:\CLionProjects\MultiFactor_cpp2\src\getData/getTradebleShare.cpp')

