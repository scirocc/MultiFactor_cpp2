cmake_minimum_required(VERSION 3.14)
project(MultiFactor_cpp2)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_EXE_LINKER_FLAGS "-static-libgcc -static-libstdc++")
include_directories(include)
include_directories(D:/ProgramData/Anaconda3/include)
include_directories(E:/CLionProjects/MultiFactor_cpp2/MyTool/include)
include_directories(E:/CLionProjects/MultiFactor_cpp2/include/getData)
include_directories(E:/frequentlyUsedCPPLibrary/include)
link_directories(bin)
link_directories(D:/ProgramData/Anaconda3/libs)
add_executable(MultiFactor_cpp2
E:/CLionProjects/MultiFactor_cpp2/src/getData/getStockDayLine.cpp
E:/CLionProjects/MultiFactor_cpp2/MyTool/src/strStuff.cpp
E:/CLionProjects/MultiFactor_cpp2/src/getData/main.cpp
E:/CLionProjects/MultiFactor_cpp2/src/getData/getTradebleShare.cpp
E:/CLionProjects/MultiFactor_cpp2/src/getData/56.cpp
E:/CLionProjects/MultiFactor_cpp2/MyTool/src/jsonStuff.cpp
E:/CLionProjects/MultiFactor_cpp2/src/getData/89.cpp
E:/CLionProjects/MultiFactor_cpp2/MyTool/src/ioStuff.cpp
E:/CLionProjects/MultiFactor_cpp2/include/getData/getTradebleShare.h
E:/frequentlyUsedCPPLibrary/include/json.hpp
E:/CLionProjects/MultiFactor_cpp2/MyTool/include/jsonStuff.h
E:/CLionProjects/MultiFactor_cpp2/include/getData/getStockDayLine.h
E:/CLionProjects/MultiFactor_cpp2/MyTool/include/ioStuff.h
E:/CLionProjects/MultiFactor_cpp2/MyTool/include/strStuff.h
E:/CLionProjects/MultiFactor_cpp2/include/getData/56.h
E:/CLionProjects/MultiFactor_cpp2/include/getData/89.h
D:/ProgramData/Anaconda3/include/Python.h
)
TARGET_LINK_LIBRARIES(MultiFactor_cpp2 
python36.lib
)
TARGET_LINK_LIBRARIES(MultiFactor_cpp2 
)
