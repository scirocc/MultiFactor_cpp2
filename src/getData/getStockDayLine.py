# coding=utf-8
import os,datetime
import cx_Oracle as cx
import json

def NestDictTransfer(hKey1Key2Info):
    #hKey1Key2Info-->hKey2Key1Info
    hKey2Key1Info={}
    for key1 in hKey1Key2Info:
        hSub=hKey1Key2Info[key1]
        for key2 in hSub:
            try:
                hKey2Key1Info[key2][key1]=hSub[key2]
            except:
                hKey2Key1Info[key2]={}
                hKey2Key1Info[key2][key1]=hSub[key2]
    return(hKey2Key1Info)

def gen_sCode(beginT,endT):
    conn = cx.connect('market/1@192.168.0.8:1521/orcl')
    cursor=conn.cursor()
    sqlstring='select code from sh_day where(code like \'6%\')and(code<688000)and(mdate>=\'{}\')and(mdate<=\'{}\')group by code'.format(beginT,endT)
    cursor.execute('{}'.format(sqlstring))
    data=cursor.fetchall()
    temp1=[x[0] for x in data]
    sqlstring='select code from sz_day where((code like \'00%\')or(code like \'300%\'))and(mdate>=\'{}\')and(mdate<=\'{}\')group by code'.format(beginT,endT)
    cursor.execute('{}'.format(sqlstring))
    data=cursor.fetchall()
    temp2=[x[0] for x in data]
    sCode=temp1+temp2
    conn.close()
    with open('../Data/sCode.js','w')as f:json.dump(sCode,f)
    return(sCode)

def getStockDayLineFromDb(sCode,startdate,endDate):
    conn = cx.connect('market/1@192.168.0.8:1521/orcl')
    cursor = conn.cursor()
    def dealData(data):
        if data:
            mdate, openprice, highprice, lowprice, closeprice, volume, amount, reweightfactor = data
            averPrice = amount / volume
            try:
                rehabilitationClosePrice = closeprice * reweightfactor
                rehabilitationAverPrice = averPrice * reweightfactor
            except:
                rehabilitationClosePrice = closeprice
                rehabilitationAverPrice = averPrice
            return (mdate, [round(closeprice, 2),
                            round(averPrice, 2),
                            round(volume, 2),
                            round(amount, 2),
                            round(rehabilitationClosePrice, 2),
                            round(rehabilitationAverPrice, 2)])

    hCodeDateInfo = {}
    hCodeInitInfo = {}
    for code in sCode:
        if code[0]=='6':tablename='sh_day'
        else:tablename='sz_day'
        sql='select closeprice,reweightfactor from {} where(code=\'{}\')and(mdate<=\'{}\')order by mdate desc'\
                    .format(tablename,code,startdate)
        cursor.execute(sql)
        closeprice,reweightfactor=cursor.fetchone()
        hCodeInitInfo[code]=[closeprice,closeprice*reweightfactor]
        sqlstring = 'select mdate,openprice,highprice,lowprice,closeprice,volume,amount,reweightfactor' \
                    ' from {} where(code=\'{}\')and(mdate>=\'{}\')and(mdate<=\'{}\')order by mdate'\
                    .format(tablename,code,startdate,endDate)
        cursor.execute(sqlstring)
        datas=cursor.fetchall()
        hDateInfo=dict(map(dealData,datas))
        hCodeDateInfo[code]=hDateInfo
    conn.close()
    return (hCodeDateInfo,hCodeInitInfo)


def genFile(hCodeDateInfo,hCodeInitInfo):
    #把hCodeDateInfo的停牌日的price补上
    with open('../Data/hCodeInitDate.js','r')as f:hCodeInitDate=json.load(f)
    with open('../Data/hCodeDelistingDate.js','r')as f:hCodeDelistingDate=json.load(f)
    h={}
    sDate=sorted(set([date for hDateinfo in hCodeDateInfo.values() for date in hDateinfo]))
    for code,hDateInfo in hCodeDateInfo.items():
        h[code]={}
        initT=hCodeInitDate[code]
        delistT=hCodeDelistingDate[code]
        sDate4code=list(filter(lambda date:initT<=date<=delistT,sDate))
        for i in range(len(sDate4code)):
            date=sDate4code[i]
            if i==0:
                try:
                    info=hDateInfo[date]#c,aver,vol,amount,re_c,re_aver
                except:
                    c,reweightFactor=hCodeInitInfo[code]
                    info=[c,0,0,0,c*reweightFactor,0]
            else:
                try:
                    info=hDateInfo[date]#c,aver,vol,amount,re_c,re_aver
                except:
                    c=oldInfo[0]
                    reweightFactor=oldInfo[-2]
                    info=[c,0,0,0,c*reweightFactor,0]
            h[code][date] = info
            oldInfo = info
    hDateCodeInfo=NestDictTransfer(h)
    sDate=sorted(hDateCodeInfo)
    for date in sDate:
        hCodeInfo=hDateCodeInfo[date]
        with open('../Data/dayline/hCodeInfoOf{}.js'.format(date),'w')as f:json.dump(hCodeInfo,f)
        return 0
    with open('../Data/sDate.js','w')as f:json.dump(sDate,f)
    return 0



def main(startdate,endDate):
    try:os.makedirs('../Data/dayline/')
    except:pass
    now1=datetime.datetime.now()
    sCode=gen_sCode(startdate,endDate)
    now2=datetime.datetime.now()
    hCodeDateInfo,hCodeInitInfo=getStockDayLineFromDb(sCode,startdate,endDate)
    print('下载数据花费时间为：',now2-now1)
    genFile(hCodeDateInfo,hCodeInitInfo)
    now3 = datetime.datetime.now()
    print('二次整理股票数据花费时间为：',now3-now2)
    return 0
