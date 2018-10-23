#codong:utf_8
import numpy as np
from numpy import linalg
import pandas as pd
inputfile='c:/用户/hp/文档/Tencent File/908637854/FileRecv/xigua.xls'
data_original = pd.read_excel(inputfile,'xigua')
x=np.array([list(data_original[u'密度']),list(data_original[u'含糖率']),[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])

y=np.array([是,是,是,是,是,是,是,是,否,否,否,否,否,否,否,否,否])
beta = np.array([[0],[0],[1]])
old_l = 0 
n=0
while 1:
    beta_T_x = np.dot(beta.T[0], x)  
    cur_l = 0   
    for i in range(17):
        cur_l = cur_l + ( -y[i]*beta_T_x[i]+np.log(1+np.exp(beta_T_x[i])) )
    if np.abs(cur_l - old_l) <= 0.000001:  
        break               
    n=n+1
    old_l = cur_l
    dbeta = 0
    d2beta = 0
    for i in range(17):
        dbeta = dbeta - np.dot(np.array([x[:,i]]).T,( y[i]-(  np.exp(beta_T_x[i])/(1+np.exp(beta_T_x[i])) ) )) #一阶导数
        d2beta =d2beta + np.dot(np.array([x[:,i]]).T,np.array([x[:,i]]).T.T) * (  np.exp(beta_T_x[i])/(1+np.exp(beta_T_x[i])) ) * (1-(  np.exp(beta_T_x[i])/(1+np.exp(beta_T_x[i])) ))
    beta = beta - np.dot(linalg.inv(d2beta),dbeta)

print('模型参数是：'),beta
print ('迭代次数：'),n
