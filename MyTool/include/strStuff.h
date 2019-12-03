//
// Created by Administrator on 2019/12/2.
//

#ifndef MULTIFACTOR_STRSTUFF_H
#define MULTIFACTOR_STRSTUFF_H
#include<vector>
#include <iostream>

bool  CheckFolderExist(const std::string &strPath);

std::vector<std::string> split_to_folder_and_file(const std::string& path);

#endif //MULTIFACTOR_STRSTUFF_H
