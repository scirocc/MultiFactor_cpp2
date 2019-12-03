//
// Created by Administrator on 2019/12/2.
//

#ifndef MULTIFACTOR_IOSTUFF_H
#define MULTIFACTOR_IOSTUFF_H
#include <windows.h>
#include <vector>
#include <iostream>
bool CheckFolderExist(const std::string &strPath);
std::vector<std::string> split_to_folder_and_file(const std::string& path);


//打印相关
template <typename T>
void myPrint(const std::vector<T>& v);

template <typename T>
void myPrint(const std::vector<std::vector<T>>& v);

template <typename T>
void myPrint(const T& object);

void myPrint();

template <typename T,typename... Types>
void myPrint(const T& firstPara,const Types&... args);


#endif //MULTIFACTOR_IOSTUFF_H
