from numpy import tile, array
import operator

def classify0(inX, dataSet, labels, k):

    dataSetSize = dataSet.shape[0]  # 数组第一维的长度
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet  # 重复某个数组
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()  # 数组值从小到大的索引值

    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1  # 指定键的值,如果值不在字典中返回default值
    # operator.itemgetter(1)根据iterable的第二个值域排序
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=False)
    return sortedClassCount[0][0]

if __name__ == '__main__':
    # 定义训练集
    group = array(
        [[1.0, 1.1], 
        [1.0, 1.0], 
        [0, 0], 
        [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']

    print(classify0([0.6, 0.6], group, labels, 3))
