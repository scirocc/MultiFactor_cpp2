cmake_minimum_required(VERSION 3.14)
project(MultiFactor)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_EXE_LINKER_FLAGS "-static-libgcc -static-libstdc++")
include_directories(include)
include_directories(D:/ProgramData/Anaconda3/include)
include_directories(E:/CLionProjects/MultiFactor/MyTool/include)
include_directories(E:/CLionProjects/MultiFactor/include/getData)
include_directories(E:/frequentlyUsedCPPLibrary/include)
link_directories(bin)
link_directories(D:/ProgramData/Anaconda3/libs)
add_executable(MultiFactor
E:/CLionProjects/MultiFactor/MyTool/src/jsonStuff.cpp
E:/CLionProjects/MultiFactor/MyTool/src/ioStuff.cpp
E:/CLionProjects/MultiFactor/src/getData/main.cpp
E:/CLionProjects/MultiFactor/MyTool/src/strStuff.cpp
E:/CLionProjects/MultiFactor/src/getData/getTradebleShare.cpp
E:/CLionProjects/MultiFactor/include/getData/getTradebleShare.h
E:/frequentlyUsedCPPLibrary/include/json.hpp
E:/CLionProjects/MultiFactor/MyTool/include/ioStuff.h
E:/CLionProjects/MultiFactor/MyTool/include/strStuff.h
D:/ProgramData/Anaconda3/include/Python.h
)
TARGET_LINK_LIBRARIES(MultiFactor 
python36.lib
)
TARGET_LINK_LIBRARIES(MultiFactor 
)
