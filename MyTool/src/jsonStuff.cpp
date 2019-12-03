//
// Created by Administrator on 2019/12/2.
//
#include <iostream>
#include <fstream>
#include <istream>
#include "json.hpp"
#include <direct.h> //_mkdir函数的头文件
#include <io.h>
#include "ioStuff.h"
//template <typename T>//写
//void jsonDump(T cpp_object,std::string path){
//    //看路径存不存在，不存在则创建
//
//
//
//    if(opendir(path)== nullptr){
//
//    }
//
//    nlohmann::j(cpp_object);
//    std::ofstream myfile(path);
//    myfile << j;
//}
//
//template <typename T>//读
//void jsonLoad(T cpp_object,std::string path){
//    std::ifstream io;
//    io.open(path);
//
//    nlohmann::j(cpp_object);
//    std::ofstream myfile(path);
//    myfile << j;
//}