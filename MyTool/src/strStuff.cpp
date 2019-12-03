//
// Created by Administrator on 2019/12/2.
//

#include "strStuff.h"


std::string replace(const std::string& str,
        const std::string& oldStrToDelete,
        const std::string& newStrToReplace){
    std::string result(str);
    int loc=0;
    int len=oldStrToDelete.length();
    std::vector<int> vLoc;
    for(;;){
        loc=result.find(oldStrToDelete,loc);
        if (loc!=-1){
            vLoc.emplace_back(loc);
            loc+=len;
        }
        else{
            break;
        }
    }
    //开始替换，从后向前
    for(auto iter_reverse=vLoc.rbegin();iter_reverse!=vLoc.rend();iter_reverse++){
        result.replace(*iter_reverse,len,newStrToReplace);
    }
    return(result);
}




std::vector<std::string> split_to_vec(const std::string& str,const std::string& separator){
    std::vector<std::string> vResult;
    int beginLoc=0;
    int loc;
    for(;;){
        loc=str.find(separator,beginLoc);
        if (loc!=-1){
            vResult.emplace_back(str.substr(beginLoc,loc-beginLoc));
            beginLoc=loc+1;
        }
        else{
            vResult.emplace_back(str.substr(beginLoc,str.length()-beginLoc));
            break;
        }
    }
    return vResult;
}


