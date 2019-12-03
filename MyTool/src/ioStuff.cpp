//
// Created by Administrator on 2019/12/2.
//
#include <ioStuff.h>

template <typename T>
void myPrint(const std::vector<T>& v){
    std::cout<<'[';
    int len=v.size();
    int counter=0;
    for(const auto& element:v){
        counter++;
        if (counter!=len){std::cout<<element<<',';}
        else{std::cout<<element;}
    }
    std::cout<<"],";
}



template <typename T>
void myPrint(const std::vector<std::vector<T>>& v){
    std::cout<<'[';
    int len=v.size();
    int counter=0;
    for(const auto& subV:v){
        myPrint(subV);
    }
    std::cout<<"\b], ";
}



template <typename T>
void myPrint(const T& object) {
    std::cout<<object<< ", ";
}



void myPrint() {
    std::cout<<"\b\b "<<std::endl;
}



template <typename T,typename... Types>
void myPrint(const T& firstPara,const Types&... args){
    if (sizeof...(args)>1){
        myPrint(firstPara);
        myPrint(args...);
    }
    else{
        myPrint(firstPara);
        myPrint(args...);
        myPrint();
    }
}







bool CheckFolderExist(const std::string &strPath)
{
    auto last2Char=strPath.substr(strPath.length()-2,2);
    std::string temp;
    if(last2Char=="//" or last2Char=="\\\\"){//要去掉
        temp=strPath.substr(0,strPath.length()-2);
    }
    else{
        auto lastChar=strPath.substr(strPath.length()-1,1);
        if (lastChar=="/" or last2Char=="\\"){//要去掉
            temp=strPath.substr(0,strPath.length()-1);
        }
        else{
            temp=strPath;
        }
    }
    WIN32_FIND_DATA  wfd;
    bool rValue = false;
    HANDLE hFind = FindFirstFile(temp.c_str(), &wfd);
    if ((hFind != INVALID_HANDLE_VALUE) && (wfd.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY))
    {
        rValue = true;
    }
    FindClose(hFind);
    return rValue;
}


std::vector<std::string> split_to_folder_and_file(const std::string& path) {
    std::vector<std::string> result(2, "");
    char drive[_MAX_DRIVE];
    char dir[_MAX_DIR];
    char fname[_MAX_FNAME];
    char ext[_MAX_EXT];
    _splitpath(path.c_str(), drive, dir, fname, ext);
    if (strlen(ext) == 0) {//说明没有类型，那么就是个folder，而不是文件
        result[0]=path;
    }
    else {
        result[0]=std::string(drive) + std::string(dir);
        result[1]=std::string(fname) + std::string(ext);
    }
    return result;
}
