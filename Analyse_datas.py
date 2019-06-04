#!/usr/bin/python
# Based on the knn.py in the same root, combined with matplotlib,numpy packages
# to analyse datas to find the connections behind the datas.

import knn
import matplotlib.pyplot as plt
# import matplotlib  # 不需要使用?
import numpy as np

# 利用knn中的函数从文本文件中解析数据
datingDataMat, datingLabels = knn.file2matrix('datingTestSet2.txt')

# 利用plt对解析数据进行可视化分析
fig = plt.figure()
ax = fig.add_subplot(111)


# ax.scatter(datingDataMat[:,1],datingDataMat[:,2])

# ax.scatter(datingDataMat[:,1],datingDataMat[:,2],
#   15.0*np.array(datingLabels), 15.0*array(datingLabels))

##ax.scatter(datingDataMat[:,0],datingDataMat[:,1],
##   15.0*np.array(datingLabels), 15.0*np.array(datingLabels))

ax.scatter(datingDataMat[:,0],datingDataMat[:,1],
   15.0*np.array(datingLabels), 15.0*np.array(datingLabels))

plt.xlabel('X')
plt.ylabel('Y')
plt.legend('buxihuan')

plt.show()



