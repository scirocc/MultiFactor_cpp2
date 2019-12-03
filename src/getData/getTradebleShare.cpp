
#include "getTradebleShare.h"
namespace getData {
    bool getTradebleShares(int endT,int threadNums) {
        Py_Initialize();//使用python之前，要调用Py_Initialize();这个函数进行初始化
        if (!Py_IsInitialized()) {
            printf("初始化失败！");
            return false;
        }
        PyRun_SimpleString("import sys");
        PyRun_SimpleString("sys.path.append('E:/CLionProjects/MultiFactor/src/getData/')");
        //这一步很重要，标识出要引入的python文件路径
        PyObject *pModule = nullptr;//声明变量
        pModule = PyImport_ImportModule("getTradebleShare");//这里是要调用的文件名
        if (pModule == nullptr)//注意，除了未找到文件外，若模块没有正常运行结束，也会返回空指针
        {
            std::cout << "something wrong happend" << std::endl;
            return false;
        }
        PyObject *pFunc = nullptr;
        pFunc = PyObject_GetAttrString(pModule, "main");//这里是要调用的函数名
        PyObject* args = PyTuple_New(2);       // 2个参数
        //PyObject* arg1 = PyUnicode_FromString("hello");    // 参数一设为，字符串
        PyObject* arg1 = PyLong_FromLong(endT);    // 20190601参数一设为，一个整数，用long表示
        PyObject* arg2 = PyLong_FromLong(threadNums);    // 24参数二设为，一个整数，用long表示
        PyTuple_SetItem(args, 0, arg1);
        PyTuple_SetItem(args, 1, arg2);
        PyEval_CallObject(pFunc,args);//调用带参数无返回值的python函数
//
//    PyObject* pRet = PyObject_CallObject(pFunc3, args2);//调用函数
//    int res = 0;
//    PyArg_Parse(pRet, "i", &res);//转换返回类型
//
        Py_Finalize(); // 与初始化对应
        return true;
    }
}
