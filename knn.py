from numpy import *
from os import listdir
import operator

# k-近邻算法
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
##    voteILabel = ''
    for i in range(k):
        voteILabel = labels[sortedDistIndicies[i]]
        classCount[voteILabel] = classCount.get(voteILabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
                              key = operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels
# Summary: 创建一个knn01函数，记录数据group和labels，在根目录下的cmd命令中打开
# python开发环境，我们就可以import knn01来调用knn01中的函数，获取数据group和labels


# 将文本记录转换为NumPy的解析程序
def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines,3))
    classLabelVector = [] # 预处理给classLabelVector分配一个list的空间
    index = 0
    for line in arrayOLines:
        line = line.strip() # strip()函数去除首尾空格,strip('0')去除首尾字符0.    
        listFromLine = line.split('\t') # 按照制表符进行分割
        returnMat[index,:] = listFromLine[0:3]
##        classLabelVector.append(int(listFromLine[-1]))
        classLabelVector.append(listFromLine[-1])
        index += 1
    return returnMat,classLabelVector


def autoNorm(dataSet):
    minVals = dataSet.min(0) # min(0)返回列的最小值;min(1)返回行的最小值
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1)) # element wise divide
    return normDataSet, ranges, minVals



## 暂时未通过对datingClass的测试，函数存在bug
def datingClassTest():
    hoRatio = 0.10   # hold out 10%
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt') # load data setform file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m* hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:], normMat[numTestVecs:m,:],\
                                     datingLabels[numTestVecs:m],3)
        print('the classifier came back with : %d, the real answer is: %d')\
                   %(classifierResult, datingLabels[i])
        if(classifierResult != datingLabels[i]): errorCount += 1.0
    print('the total error rate is: %f' %(errorCount/float(numTestVecs)))



def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(input(\
        'percentage of time spent playing veido games?'))
    ffMiles = float(input('frequent flier miles earned per year'))
    iceCream = float(input('liters of ice cream consumed per year?'))
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr-\
                                  minVals)/ranges, normMat, datingLabels, 3)
    print('You will probabaly like this person: ',\
          resultList[int(classifierResult) - 1])

def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])
    return returnVect


def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest,\
                                     trainingMat, hwLabels, 3)
        print('the classifier came back with: %d, the real answer is: %d'\
              %(classifierResult, classNumStr))
        if(classifierResult != classNumStr): errorCount += 1.0
    print('\nthe total number of errors is: %d'% errorCount)
    print('\nthe total error rate is: %d' % (errorCount/float(mTest)))
