from numpy import tile, zeros, array
import operator


def classify0(inX, dataSet, labels, k):

    dataSetSize = dataSet.shape[0]  # 数组行数
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()

    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # operator.itemgetter(1)根据iterable的第二个值域排序
    sortedClassCount = sorted(
        classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    arrayOfLines = fr.readlines()
    numberOfLines = len(arrayOfLines)
    # 用0填充的数组(numberOfLines行，3列)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOfLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(listFromLine[-1])
        index += 1
    return returnMat, classLabelVector


def autoNorm(dataSet):
    minVals = dataSet.min(0)  # 每列的最小值
    maxVals = dataSet.max(0)  # 每列的最大值
    ranges = maxVals - minVals
    m = dataSet.shape[0]  # 数组第一维的长度
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet/tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


def classifyPerson():
    percentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))

    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')

    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify0(
        (inArr-minVals)/ranges, normMat, datingLabels, 3)
    print(classifierResult)


def datingClassTest():
    hoRatio = 0.10  # 用于测试的比例
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    result_autoNorm  = autoNorm(datingDataMat)
    normMat = result_autoNorm[0]
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(
            normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print(str(i) + ': the classifier came back with: %s, the real answer is: %s' % (
            classifierResult, datingLabels[i]))
        if classifierResult != datingLabels[i]:
            errorCount += 1.0
    print("the total error rate is: %f" % (errorCount / float(numTestVecs)))
    print(errorCount)


if __name__ == '__main__':

    #　测试
    # datingClassTest()

    # 预测函数调用
    classifyPerson()
