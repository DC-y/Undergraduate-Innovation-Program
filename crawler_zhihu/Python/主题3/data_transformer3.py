import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from pylab import *



cx = sqlite3.connect("user_info.db")
cu = cx.cursor()
cu.execute("create table user_info (user_id text primary key,followers integer, asks integer, answers integer, goods integer)")





def transform(name):
    line = f.readline()
    while line:
        line = f.readline()
        line.strip()
        data = line.split(',')
        try:
            cx.execute("insert into user_info values (?,?,?,?,?)",data)
            print data
            cx.commit()
        except:
            print "existed.\n"
    
    f.close()

name_list = ['ahdu', 'allenzhang','amuro1230','baiya','billhan','boxun','chen_hao_84','chu_yang_trueyoung','cindysss',
'commando','daxiong','delphi','fenng','gongjun','hecaitou','hi_id','imike','jin_chen_yu','jinpengyuan',
'jixin','junyu','kaifulee','kentzhu','keso','lianghai','linan','mj1997','mochaz','ni_lao','raymond_wang',
'shek','tian_ji_shun','wang_wei_63','wang_xiao_chuan','wangxing','waynezhang','yangbo','yeluoguzhou','yeyi',
'zhangleo','zhou_xiao_nong','zhouyuan']

for name in name_list:
    print name
    f = open(name + ".txt")
    transform(name)


# cu.execute("select COUNT(user_id)from user_info where asks>0")
# result = cu.fetchall()[0][0]



"""
asks = []
for i in range(200):
    cu.execute("select COUNT(user_id) from user_info where asks="+str(i)+"")
    a = cu.fetchall()[0][0]
    asks.append(a)
    print a
    
answers = []
for i in range(200):
    cu.execute("select COUNT(user_id) from user_info where answers="+str(i)+"")
    a = cu.fetchall()[0][0]
    answers.append(a)
    #print a    
    
for i in range(200):
    cu.execute("select COUNT(user_id) from user_info where answers="+str(i)+"")
    a = cu.fetchall()[0][0]
    answers.append(a)
    print a     
    
t = range(200)
plot(t,asks)
loglog(t,asks)

plot(t,answers)
loglog(t,answers)

show()
"""



"""
answers = []
cu.execute("select answers from user_info")
a = cu.fetchall()
for i in range(100000):
    b = a[i][0]
    answers.append(b)
    print b
    
    
asks = []
cu.execute("select asks from user_info")
a = cu.fetchall()
for i in range(100000):
    b = a[i][0]
    asks.append(b)
    
    
followers = []
cu.execute("select followers from user_info")
a = cu.fetchall()
for i in range(100000):
    b = a[i][0]
    followers.append(b)    
    
    
goods = []
cu.execute("select goods from user_info")
a = cu.fetchall()
for i in range(100000):
    b = a[i][0]
    goods.append(b)

plot(asks,answers)
loglog(followers,goods)

show()
"""  
