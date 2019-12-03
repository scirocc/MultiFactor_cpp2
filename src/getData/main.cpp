#include <iostream>
#include <fstream>
#include <istream>
#include "getTradebleShare.h"
#include "json.hpp"
#include <map>
#include <vector>
#include<ctime>
//#include <fstream>
#include <direct.h> //_mkdir函数的头文件
#include <vector>
#include <windows.h>

#include "ioStuff.h"







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


//
//template <typename T>//写
//void jsonDump(T cpp_object,std::string path){
//    //看路径存不存在，不存在则创建
//    if(opendir(path)== nullptr){
//
//    }
//
//    nlohmann::j(cpp_object);
//    std::ofstream myfile(path);
//    myfile << j;
//}
// vector::emplace
#include <iostream>
#include <vector>

//int main () {
//    std::vector<int> myvector = {10, 20, 30};
//
//    auto it = myvector.emplace(myvector.begin() + 1, 100);
//    myvector.emplace(it, 200);
//    myvector.emplace(myvector.end(), 300);
//
//    std::cout << "myvector contains:";
//    for (auto &x: myvector)
//        std::cout << ' ' << x;
//    std::cout << '\n';
//
//    return 0;
//}
int x=3;
void asd(){
    x=4;
}
int main() {
    std::vector<int> v1{1,2,3};
    std::vector<std::vector<int>>v{v1,v1,v1};
//    for(const auto& element:v1){
//        std::cout<<element<<std::endl;}
//    myPrintVec(v);
    myPrint(1,v,"asd");
}
////    std::map<int,std::map<int,int> > h;
////    std::map<int,std::map<int,int> > h={{1,{{1,1}}}};
////    std::cout<<h[1][1]<<std::endl;
////    std::vector<std::string> s={"asd","dsa"};
////    nlohmann::json j1(h);
////    nlohmann::json j2(s);
////    std::fstream _file;
////    _file.open("C:/Users/Administrator/Desktop/asd/js1",std::ios::in);
////    if(!_file)
////    {
////        std::cout<< "Cannot find file:"<<std::endl;
////        exit(-1);
////        }
////    std::ofstream myfile1("C:/Users/Administrator/Desktop/asd/js1");
////    std::ofstream myfile2("C:/Users/Administrator/Desktop/js2");
////    myfile1 << j1 << std::endl;
////    myfile2 << j2 << std::endl;
////    auto path="C:/Users/Administrator/Desktop/";
////    auto path="C:/Users/Administrator/Desktop\\\\";
////    auto path="C:/Users/Administrator/Desktop\\";
////    auto path="C:/Users/Administrator/Desktop/";
////    auto path="C:/Users/Administrator/Desktop//";
//    auto path="C:/Users/Administrator/Desktop";
////    auto x=CheckFolderExist(path);
//    std::string y="";
//    std::string x="";
//    auto v=split_to_folder_and_file(path);
//    std::cout<< v[0]<<std::endl;
////            std::cout<< v[1]<<std::endl;
////    NULL
//
//    //    split_to_vec(path,"/");
//
////    auto result=replace(path,"s","asd");
////    std::cout<<x;
////    std::cout<<path[strlen(path)-1];
////    std::ifstream io;
////    io.open("C:/Users/Administrator/Desktop/js8");
////    nlohmann::json j;
////    io >> j;
////    auto b=j.get<std::map<int,std::map<int,int> >>();
////    std::cout<<b[2][2];
////    std::cout<<b[1][1];
//
////    auto j3 = nlohmann::json::parse(j);
////    auto j3 = nlohmann::json::parse(j.dump());
////    auto j3 = j._js;
////    std::cout<<j3<<std::endl;
////    std::cout<<j3[1][1];
//    return 0;
//}

//auto fun1(){
//    std::vector<int>x(300000000, 2);
//
//    return x;
//}
//auto fun2(){
//    std::vector<int>x(300000000, 2);
//    auto p=std::make_unique<std::vector<int>>(x);
//    return p;
//}
//
//int main(){
//    auto time_start=std::clock();
//    auto x=fun1();
//    auto time_end=std::clock();
//    auto p=fun2();
//    auto time_end2=std::clock();
//
//    std::cout<<time_end-time_start<<std::endl;
//    std::cout<<time_end2-time_end<<std::endl;
//
//
//    return 0;
//}