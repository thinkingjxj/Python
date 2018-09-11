import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd
from sklearn import linear_model, svm
from sklearn import preprocessing
from sklearn.cross_validation import KFold
import json
import random


# 本代码用来求不同维度之间的关系
# 首先将原始数据全部变成ln数据，并且将X和Y的n时间前组合
# 其次进行预测
# 实现一个观看图像形状的代码，从而看相关关系


# 返回用电矩阵
def readAllTxt(filename):
    tmp = np.loadtxt(filename, delimiter=",")
    # np.delete(tmp, 0, axis = 0)
    tmp = tmp.T
    # np.delete(tmp, 0, axis = 0)
    # embed()
    np.savetxt('all_begin.csv', tmp, delimiter=",")
    return tmp


# changeCPI('newcpi.csv', 'cpigood.csv')
# changeCPI('newfood.csv', 'foodgood.csv')
# changeCPI('newtraffic.csv', 'trafficgood.csv')
# changeCPI('newlive.csv', 'livegood.csv')

# 直接用上一期的cpi预测本期CPI
def easyPredict(srFile):
    cpiNp = np.loadtxt(srFile, delimiter=',')
    sampleNum = cpiNp.shape[0]
    listNp = np.arange(sampleNum)

    plt.plot(listNp, cpiNp)
    plt.show()

    easyNp = cpiNp.copy()
    for i in range(sampleNum - 1):
        easyNp[i] = easyNp[i + 1] - easyNp[i]
    easyNp[sampleNum - 1] = 0

    meanAbs = np.mean(np.absolute(easyNp))
    meanNp = np.mean(cpiNp)

    print(' abs error is ' + str(meanAbs / meanNp))


# easyPredict('costgood.csv')
# timeStep为多少步以前的时间
def makeXFile(xFile, yFile, timeStep):
    xNumpy = np.loadtxt(xFile, delimiter=',')
    yNumpy = np.loadtxt(yFile, delimiter=',')
    xNumpy = xNumpy[timeStep:, :]
    yNumpy = np.log(yNumpy)
    yNumpy = np.reshape(yNumpy, (1, -1))
    needY = yNumpy[:, :-1 * timeStep]
    yNumpy = yNumpy[:, timeStep:]
    xNumpy = np.log(xNumpy)
    yNumpy = yNumpy.T
    needY = needY.T

    allNumpy = np.column_stack((xNumpy, needY))

    sampleNum = allNumpy.shape[0]
    listNp = np.arange(sampleNum)

    # plt.plot(listNp, yNumpy, color = 'blue', label = 'original')
    plt.plot(listNp, allNumpy[:, 3], color='red', label='city people life')
    plt.plot(listNp, allNumpy[:, 9], color='black', label='internet')
    plt.legend()
    plt.show()

    # embed()

    return allNumpy, yNumpy


def getPearsonX(wantY, oneX, timeStep):
    pearsonList = []
    klList = []

    for i in range(timeStep):
        # embed()
        newY = wantY[i:, :].flatten()
        # newY = np.log(newY)
        if i == 0:
            newX = oneX
        else:
            newX = oneX[:-1 * i]
        # newX = np.log(newX)
        diffY = np.zeros(len(newY) - 1)
        diffX = np.zeros(len(newX) - 1)
        for k in range(len(newX) - 1):
            diffY[k] = newY[k + 1] - newY[k]
            diffX[k] = newX[k + 1] - newX[k]

        # embed()
        pearson = np.corrcoef(diffX, diffY)[0][1]
        # embed()
        pearsonList.append(pearson)
        print('time is ' + str(i) + ' Person is: ' + str(pearson))

        diffX = diffX - diffX.min() + 0.0001
        diffY = diffY - diffY.min() + 0.0001

        oneProbX = diffX / diffX.sum()
        oneProbY = diffY / diffY.sum()

        middleProb = oneProbY * np.log(oneProbY / oneProbX)
        # embed()
        kldivergence = middleProb.sum()
        klList.append(kldivergence)
        print('kl divergence is ' + str(kldivergence))
    return pearsonList, klList


# timeStep用到前一个月的用电数据和CPI
def newmakeXFile(xFile, yFile, timeStep):
    xNumpy = np.loadtxt(xFile, delimiter=',')
    yNumpy = np.loadtxt(yFile, delimiter=',')
    allNumpy = xNumpy[(timeStep - 1):(-1 * timeStep), :]

    for i in range(1, timeStep):
        newX = xNumpy[(timeStep - 1 - i):(-1 * (timeStep + i)), :]
        allNumpy = np.column_stack((allNumpy, newX))

    yNumpy = np.reshape(yNumpy, (-1, 1))

    for i in range(timeStep):
        newY = yNumpy[(timeStep - i - 1):(-1 * (timeStep + i)), :]
        allNumpy = np.column_stack((allNumpy, newY))

    allNumpy = np.log(allNumpy)
    yNumpy = np.log(yNumpy)

    yNumpy = yNumpy[timeStep:, :]

    return allNumpy, yNumpy


def makeYFile(yFile, timeStep):
    yNumpy = np.loadtxt(yFile, delimiter=',')
    yNumpy = np.log(yNumpy)
    yNumpy = np.reshape(yNumpy, (-1, 1))

    allNumpy = yNumpy[:(-1 * timeStep), :]
    yNumpy = yNumpy[timeStep:, :]

    return allNumpy, yNumpy


# lnMinusFile('livecpi.csv', 'lnlivecpi.csv')

def makeOnlyXFile(xFile, yFile, timeStep):
    print(xFile)
    xNumpy = np.loadtxt(xFile, delimiter=',')
    yNumpy = np.loadtxt(yFile, delimiter=',')
    if timeStep == 0:
        allNumpy = xNumpy
    else:
        allNumpy = xNumpy[:(-1 * timeStep), :]

    yNumpy = np.reshape(yNumpy, (-1, 1))

    allNumpy = np.log(allNumpy)
    yNumpy = np.log(yNumpy)

    yNumpy = yNumpy[timeStep:, :]
    return allNumpy, yNumpy


def changeWantX(wantX, delList):
    wantX = np.delete(wantX, delList, 1)
    return wantX


def diffMatrix(wantX, wantY):
    sampleLen, sampleDim = wantX.shape
    ysampleLen, ysampleDim = wantY.shape
    newX = np.zeros((sampleLen - 1, sampleDim))
    newY = np.zeros((ysampleLen - 1, 1))
    for i in range(sampleLen - 1):
        newX[i, :] = wantX[i + 1, :] - wantX[i, :]
    for i in range(ysampleLen - 1):
        newY[i] = wantY[i + 1] - wantY[i]
    return newX, newY


# 拼接上个月和上上个月表现好的
def getTimeXY(xFile, yFile, timeList):
    wantX, wantY = makeOnlyXFile(xFile, yFile, 0)

    # wantX = np.log(wantX)
    # wantY = np.log(wantY)
    # wantX, wantY = diffMatrix(newX, newY)
    twoXList = wantX[:, timeList]
    allNumpy = np.delete(wantX, timeList, 1)

    twoXList = twoXList[:-1, :]
    allNumpy = allNumpy[1:, :]
    wantY = wantY[1:, :]
    allNumpy = np.column_stack((allNumpy, twoXList))

    return allNumpy, wantY


def linearPredict(newX, newY):
    mseAccuracy = []
    absAccuracy = []
    stdNp = []

    wantX, wantY = diffMatrix(newX, newY)

    sampleNum = wantX.shape[0]
    kf = KFold(sampleNum, n_folds=10)

    i = 0

    r2List = []
    aicList = []

    for train_index, test_index in kf:
        i += 1
        # print('fold ' + str(i))

        trainX = wantX[train_index]
        testX = wantX[test_index]
        trainY = wantY[train_index]
        testY = wantY[test_index]

        regr = linear_model.LinearRegression()
        # embed()
        regr.fit(trainX, trainY)

        predictY = regr.predict(testX)

        absError, stdError = returnLogY(newY, predictY, test_index)

        absAccuracy.append(absError)
        stdNp.append(stdError)

        oner2score = regr.score(wantX, wantY)
        r2List.append(oner2score)

        first50X = wantX[:50, :]
        first50Y = wantY[:50, :]
        allPredictY = regr.predict(first50X)
        RSS = rssValue(first50Y, allPredictY)
        xRow, xLine = first50X.shape
        AIC = 2 * 13 + xRow * np.log(RSS / xRow)
        aicList.append(AIC)

    # print('linear result is: ')
    absAverage = sum(absAccuracy) / len(absAccuracy)
    stdAverage = sum(stdNp) / len(stdNp)
    r2Averge = sum(r2List) / len(r2List)
    aicAverage = sum(aicList) / len(aicList)
    # print('absAverage is ' + str(absAverage))
    # print('std is:' + str(stdAverage))
    # if r2Averge > 0.3:
    #     print('r2 is ' + str(r2Averge))
    #     print('aic is ' + str(aicAverage))
    return r2Averge, aicAverage


def linearOneTest(newX, newY):
    mseAccuracy = []
    absAccuracy = []
    stdNp = []

    wantX, wantY = diffMatrix(newX, newY)

    number = len(wantY)
    trainNum = number * 9 / 10
    trainNum = int(trainNum)
    testNum = number - trainNum

    trainX = wantX[:trainNum:, :]
    testX = wantX[trainNum:, :]
    trainY = wantY[:trainNum, :]
    testY = wantY[trainNum:, :]

    regr = linear_model.LinearRegression()

    test_index = range(trainNum, number)
    # embed()
    regr.fit(trainX, trainY)

    predictY = regr.predict(testX)

    xRow, xLine = testX.shape
    listX = [i for i in range(xRow)]
    listX = np.array(listX).reshape(-1, 1)
    # embed()
    plt.plot(listX, testY, label='real', color='red')
    plt.plot(listX, predictY, label='predict', color='blue')
    plt.legend()
    plt.show()

    absError, stdError = returnLogY(newY, predictY, test_index)

    r2score = regr.score(wantX, wantY)

    if r2score > 0.4:
        # print('absError is ' + str(absError))
        # print('stdError is ' + str(stdError))
        print('r2 is ' + str(r2score))


def rssValue(predictY, realY):
    return np.sum((predictY - realY) * (predictY - realY))


def returnLogY(originY, predictY, test_index):
    # sampleNum, sampleDim = predictY.shape
    sampleNum = len(predictY)
    finalPredict = np.zeros(sampleNum)

    partOrigin = originY[test_index]
    finalPredict = np.exp(partOrigin + predictY)
    realIndex = [i + 1 for i in test_index]
    realResult = originY[realIndex]
    realResult = np.exp(realResult)
    # np.savetxt('r11_new_2.csv', realResult, delimiter = ',')
    # np.savetxt('r22_new_2.csv', finalPredict, delimiter = ',')
    meanOriginY = np.mean(realResult)
    npAbsArray = np.absolute(realResult - finalPredict) / realResult
    nabsError = np.mean(npAbsArray)
    # nstdError = np.std(realResult - finalPredict)
    nstdError = np.std(npAbsArray)

    # np.savetxt('originValue.csv', realResult, delimiter = ",")
    # np.savetxt('predictValue.csv', finalPredict, delimiter = ",")
    return nabsError, nstdError


def ridgeOneTest(newX, newY, alpha):
    mseAccuracy = []
    absAccuracy = []
    varNp = []

    wantX, wantY = diffMatrix(newX, newY)

    sampleNum = wantX.shape[0]

    scaler = preprocessing.StandardScaler().fit(wantX)

    wantX = scaler.transform(wantX)

    number = len(wantY)
    trainNum = number * 9 / 10
    trainNum = int(trainNum)
    testNum = number - trainNum

    trainX = wantX[:trainNum:, :]
    testX = wantX[trainNum:, :]
    trainY = wantY[:trainNum, :]
    testY = wantY[trainNum, :]

    regr = linear_model.Ridge(alpha=alpha)
    # embed()
    regr.fit(trainX, trainY)

    # predictY = regr.predict(testX)

    # test_index = range(trainNum, number)

    predictY = regr.predict(wantX)
    test_index = list(range(len(wantY)))

    absError, stdError = returnLogY(newY, predictY, test_index)

    print('absError is ' + str(absError))
    print('stdError is ' + str(stdError))


def ridgePredict(newX, newY, alpha):
    mseAccuracy = []
    absAccuracy = []
    varNp = []

    wantX, wantY = diffMatrix(newX, newY)

    sampleNum = wantX.shape[0]

    scaler = preprocessing.StandardScaler().fit(wantX)

    wantX = scaler.transform(wantX)

    kf = KFold(sampleNum, n_folds=10)

    i = 0

    for train_index, test_index in kf:
        i += 1
        # print('fold ' + str(i))

        trainX = wantX[train_index]
        testX = wantX[test_index]
        trainY = wantY[train_index]
        testY = wantY[test_index]

        regr = linear_model.Ridge(alpha=alpha)
        # embed()
        regr.fit(trainX, trainY)

        predictY = regr.predict(testX)

        nabsError, absVar = returnLogY(newY, predictY, test_index)

        absAccuracy.append(nabsError)
        varNp.append(absVar)

    absAverage = sum(absAccuracy) / len(absAccuracy)
    varAverage = sum(varNp) / len(varNp)
    # print('MSE average is ' + str(mseAverage))
    # print('absAverage is ' + str(absAverage))
    return absAverage, varAverage

    # embed()
    # return regr.predict(wantX)


def finalRidge(newX, newY, alpha):
    wantX, wantY = diffMatrix(newX, newY)
    scaler = preprocessing.StandardScaler().fit(wantX)

    wantX = scaler.transform(wantX)
    regr = linear_model.Ridge(alpha=alpha)

    trainX = wantX[:-12, :]
    trainY = wantY[:-12, :]
    testX = wantX[-12:, :]
    testY = wantY[-12:, :]
    # embed()
    regr.fit(trainX, trainY)

    predictY = regr.predict(testX)
    # embed()
    print('Coefficients: \n', regr.coef_)
    # The mean squared error
    print('ridge Result')

    test_index = list(range(len(wantY) - 12, len(wantY)))

    absError, stdError = returnLogY(newY, predictY, test_index)

    print('abs is ' + str(absError))
    print('std is ' + str(stdError))


def myProcess(lnoriginFile, originFile, predictFile, xFile):
    lnMinusFile(originFile, lnoriginFile)

    allLinearPredict(lnoriginFile, originFile, predictFile, xFile)

    allRidgePredict(lnoriginFile, originFile, predictFile, xFile)
    # allSvmPredict('cpi_all_ln.csv', 'cpi_all.csv', 'cpisvmpredict.csv', 'all_ln.csv')
    plt.legend()
    plt.show()


# myProcess('cpi_all_ln.csv', 'cpi_all.csv', 'cpisvmpredict.csv', 'all_ln.csv')
# myProcess('lnlivecpi.csv', 'livecpi.csv', 'livecpisvmpredict.csv', 'all_ln.csv')
# myProcess('foodln.csv', 'foodcpi.csv', 'cpifoodpredict.csv', 'all_ln.csv')
# myProcess('trafficln.csv', 'trafficcpi.csv', 'cpitrafficpredict.csv', 'all_ln.csv')


# 用来选alpha
def oneridgePredict(wantX, wantY):
    maxAver = 100000000
    wantAlpha = -1
    bestAccuracy = 0

    for t in range(0, 200):
        alpha = t / 100 + 1
        # alpha = t
        absAverage, absAccuracy = ridgePredict(wantX, wantY, alpha)
        if absAverage < maxAver:
            maxAver = absAverage
            wantAlpha = alpha
            bestAccuracy = absAccuracy
    print('Ridge Predict')
    print('alpha is ' + str(wantAlpha))
    print('abs is ' + str(maxAver))
    print('std is ' + str(bestAccuracy))
    return alpha


def allProcess(xFile, yFile, timeStep):
    print('a new process: ' + str(yFile))

    wantX, wantY = makeOnlyXFile(xFile, yFile, timeStep)
    laterList = [2, 3, 0, 1, 1, 0, 3, 0, 2, 0]
    finalX, finalY = changeTimeWantXY(wantX, wantY, laterList)
    # wantX, wantY = mergeTimeX( wantX, wantY, 5, 9)
    # wantX, wantY = getTimeXY(xFile, yFile, twoList)
    # finalX = changeWantX(finalX, diffList1)
    # wantX = changeWantX(wantX, delList3)
    # wantX = changeWantX(wantX, delList7)
    # finalRidge(wantX, wantY, 46.59)

    # linearPredict(wantX, wantY)
    oneridgePredict(finalX, finalY)
    # oneridgePredict(wantX, wantY)
    # onelassoPredict(wantX, wantY)
    print('end\n\n')


# 将changeDim延后lateTime期，看效果
def mergeTimeX(wantX, wantY, changeDim, lateTime):
    oneLater = wantX[:, changeDim].reshape(-1, 1)
    allLater = np.delete(wantX, changeDim, 1)
    finalY = wantY[lateTime:, :]
    oneLater = oneLater[:-1 * lateTime, :]
    allLater = allLater[lateTime:, :]
    allX = np.column_stack((allLater, oneLater))
    return allX, finalY


def myTest(xFile, yFile, timeStep):
    wantX, wantY = makeOnlyXFile(xFile, yFile, timeStep)
    laterList = [2, 3, 0, 1, 1, 0, 3, 0, 2, 0]
    finalX, finalY = changeTimeWantXY(wantX, wantY, laterList)
    # finalX = changeWantX(finalX, diffList1)
    # wantX, wantY = getTimeXY(xFile, yFile, twoList)
    # wantX = changeWantX(wantX, diffList1)
    # wantX = changeWantX(wantX, delList7)
    # finalRidge(finalX, finalY, 0.22)
    # finalRidge(wantX, wantY, 1)
    # ridgeOneTest(wantX, wantY, 1)
    ridgeOneTest(finalX, finalY, 2.17)
    # finalLasso(wantX, wantY, 0.0001)


def oneTest(xFile, yFile, timeStep):
    wantX, wantY = makeOnlyXFile(xFile, yFile, timeStep)
    # wantX, wantY = getTimeXY(xFile, yFile, twoList)
    # wantX = changeWantX(wantX, diffList1)
    # wantX = changeWantX(wantX, delList7)
    linearOneTest(wantX, wantY)
    print('\n')
    ridgeOneTest(wantX, wantY, 18)


def rtestTime(xFile, yFile):
    wantX, wantY = makeOnlyXFile(xFile, yFile, 1)
    xRow, xLine = wantX.shape
    for i in range(3):
        for j in range(13):
            for k in range(12 - i):
                newX = np.zeros((xRow - i, xLine))
                newY = np.zeros((xRow - i, 1))
                if i == 0:
                    newX = wantX
                    newY = wantY
                else:
                    newX = wantX[:-1 * i, :]
                    newY = wantY[i:, :]
                oneLater = newX[:, j].copy().reshape(-1, 1)
                allLater = np.delete(newX, j, 1)

                finalY = newY[k:, :]

                if k != 0:
                    oneLater = oneLater[:-1 * k, :]
                    allLater = allLater[k:, :]
                # embed()
                finalX = np.column_stack((allLater, oneLater))

                print('all late is ' + str(i) + ' dimension is ' + str(j) + ' one later is ' + str(k))
                R2, AIC = linearPredict(finalX, finalY)
                if R2 > 0.2:
                    print('r2 is ' + str(R2))
                    print('AIC is ' + str(AIC))


# 遍历所有延迟组合里面，最优模型拟合
def allRtestTime(xFile, yFile):
    wantX, wantY = makeOnlyXFile(xFile, yFile, 1)
    laterList = [0] * 13
    stopLabel = 0
    finalList = []
    while 1:
        laterList[0] += 1
        for i in range(13):
            if laterList[i] > 11:
                if i == 12:
                    stopLabel = 1
                laterList[i] = laterList[i] - 11
                laterList[i + 1] += 1
        if stopLabel == 1:
            break
        allList = []
        bigLate = max(laterList)

        finalY = wantY[bigLate:, :]

        for i in range(13):
            cutDim = bigLate - laterList[i]
            oneLater = wantX[cutDim:, i].reshape(-1, 1)
            if laterList[i] != 0:
                oneLater = oneLater[:-1 * laterList[i]]
            allList.append(oneLater)

        finalX = np.column_stack(allList)
        # sampleNum, sampleDim = finalX.shape
        # if sampleNum < 20:
        #     embed()
        # print('sameple number is '+ str(sampleNum))
        R2, AIC = linearPredict(finalX, finalY)
        if R2 > 0.45:
            tmpList = []
            for i in range(13):
                print(str(laterList[i]) + ' ', end='')
                tmpList.append(laterList[i])
            tmpList.append(R2)
            tmpList.append(AIC)
            print()
            print(R2)
            print(AIC)
            finalList.append(tmpList)
    jsObj = json.dumps(finalList)
    fileObject = open('myresult.json', 'w')
    fileObject.write(jsObj)
    fileObject.close()


# 锁定模型里面几个数，最优模型拟合
def stableRtestTime(xFile, yFile):
    wantX, wantY = makeOnlyXFile(xFile, yFile, 1)
    laterList = []
    # change
    addList = [0] * 10

    stopLabel = 0
    finalList = []
    while 1:
        addList[0] += 1
        # change
        for i in range(10):
            if addList[i] > 11:
                # change
                if i == 9:
                    stopLabel = 1
                addList[i] = addList[i] - 11
                addList[i + 1] += 1
            else:
                break
        if stopLabel == 1:
            break
        laterList = addList.copy()
        # change
        laterList.insert(0, 9)
        laterList.insert(1, 1)
        laterList.insert(2, 9)
        allList = []
        bigLate = max(laterList)

        finalY = wantY[bigLate:, :]

        for i in range(13):
            cutDim = bigLate - laterList[i]
            oneLater = wantX[cutDim:, i].reshape(-1, 1)
            if laterList[i] != 0:
                oneLater = oneLater[:-1 * laterList[i]]
            allList.append(oneLater)

        finalX = np.column_stack(allList)
        # sampleNum, sampleDim = finalX.shape
        # if sampleNum < 20:
        #     embed()
        # print('sameple number is '+ str(sampleNum))
        R2, AIC = linearPredict(finalX, finalY)
        if R2 > 0.45:
            tmpList = []
            for i in range(13):
                print(str(laterList[i]) + ' ', end='')
                tmpList.append(laterList[i])
            tmpList.append(R2)
            tmpList.append(AIC)
            print()
            print(R2)
            print(AIC)
            finalList.append(tmpList)
    jsObj = json.dumps(finalList)
    fileObject = open('myresult.json', 'w')
    fileObject.write(jsObj)
    fileObject.close()


# 某一个dim寻找最优
def oneDimFind(wantX, wantY, laterList, dimNum):
    smallNum = 0
    aicScore = 0
    r2Score = 0
    for i in range(11):
        laterList[dimNum] = i
        R2, AIC = changeTimeAicR(wantX, wantY, laterList)
        # print(R2)
        # if R2 > r2Score:
        #     smallNum = i
        #     r2Score = R2
        if aicScore > AIC:
            aicScore = AIC
            smallNum = i
    laterList[dimNum] = smallNum
    # embed()
    return laterList


# 一次遍历寻找最优
def oneWayFind(xFile, yFile):
    wantX, wantY = makeOnlyXFile(xFile, yFile, 1)
    # 初始随机赋值
    laterList = []
    for i in range(13):
        randomNum = random.randint(0, 11)
        laterList.append(randomNum)
    # 先试试跑1000次看看是否收敛
    for i in range(50):
        for j in range(13):
            laterList = oneDimFind(wantX, wantY, laterList, j)
        print('loop ' + str(i) + ' finished:')
        for j in range(13):
            print(str(laterList[j]), end=' ')
        R2, AIC = changeTimeAicR(wantX, wantY, laterList)
        print('r2 is ' + str(R2))
        print('AIC is ' + str(AIC))


# 每次将随机5个位置设置为随机值
def oneZeroFind(xFile, yFile):
    wantX, wantY = makeOnlyXFile(xFile, yFile, 1)
    finalR = 0
    finalAic = 0
    finalLaterList = [0] * 13
    # 初始随机赋值
    laterList = []
    for i in range(13):
        randomNum = random.randint(0, 11)
        laterList.append(randomNum)
    # 先试试跑1000次看看是否收敛
    for k in range(100000):
        print('all loop is ' + str(k))
        for i in range(5):
            randLoc = random.randint(0, 12)
            randNum = random.randint(0, 11)
            laterList[randLoc] = randNum
        for i in range(6):
            for j in range(13):
                laterList = oneDimFind(wantX, wantY, laterList, j)
            # print('loop ' + str(i) + ' finished:')
            # for j in range(13):
            #     print(str(laterList[j]), end=' ')
            R2, AIC = changeTimeAicR(wantX, wantY, laterList)

            if AIC < finalAic:
                finalAic = AIC
                finalR = R2
                finalLaterList = laterList.copy()
        for j in range(13):
            print(str(finalLaterList[j]), end=' ')
        print('final r2 is ' + str(finalR))
        print('final aic is ' + str(finalAic))

    np.savetxt('finalList2.csv', finalLaterList, delimiter=',')


# 输入延迟list，输出延迟以后的数据
def changeTimeWantXY(wantX, wantY, laterList):
    allList = []
    bigLate = max(laterList)
    # embed()
    finalY = wantY[bigLate:, :]

    for i in range(10):
        cutDim = bigLate - laterList[i]
        oneLater = wantX[cutDim:, i].reshape(-1, 1)
        if laterList[i] != 0:
            oneLater = oneLater[:-1 * laterList[i]]
        allList.append(oneLater)

    finalX = np.column_stack(allList)
    return finalX, finalY


# 输入延迟list，输出模型拟合效果
def changeTimeAicR(wantX, wantY, laterList):
    finalX, finalY = changeTimeWantXY(wantX, wantY, laterList)
    R2, AIC = linearPredict(finalX, finalY)
    return R2, AIC


# 输入延迟list，返回模型效果
def testTimeList(xFile, yFile):
    wantX, wantY = makeOnlyXFile(xFile, yFile, 1)
    laterList = [2, 3, 0, 1, 1, 0, 3, 0, 2, 0]
    aicArray = np.zeros((11, 11))
    for i in range(11):
        for j in range(11):
            newLaterList = laterList.copy()
            newLaterList[3] = j
            newLaterList[4] = i
            R2, AIC = changeTimeAicR(wantX, wantY, newLaterList)
            aicArray[i][j] = 0 - AIC - 520
    np.savetxt('aicArray_2.csv', aicArray, delimiter=',')
    # print('R2 is ' + str(R2))
    # print('AIC is ' + str(AIC))


# 实现以同一个月为基年的CPI
# srFile为原始文件，dstFile为目标文件
def changeCPI(srFile, dstFile):
    cpiNp = np.loadtxt(srFile, delimiter=',')
    cpiNp[0] = 100
    npLen = cpiNp.shape[0]
    for i in range(1, npLen):
        cpiNp[i] = cpiNp[i - 1] * cpiNp[i] / 100
    np.savetxt(dstFile, cpiNp, delimiter=',')
    return


# 计算AIC
# xFile为行业用电数据，yFile为CPI数据
# laterList为一个数组，laterList[i]表示第i个行业的延时
# 返回该laterList对应的AIC
def calAIC(xFile, yFile, laterList):
    wantX, wantY = makeOnlyXFile(xFile, yFile, 1)
    R2, AIC = changeTimeAicR(wantX, wantY, laterList)
    return AIC


# 计算最优延时，结果保存在delayFile里面，结果为各个行业最优延时
# xFile为行业用电数据，yFile为CPI数据
# 每次将随机5个位置设置为随机值
# 函数可能要训练很多小时，所以前端最好有个loading。。。提示
def findTimeDelay(xFile, yFile, delayFile):
    wantX, wantY = makeOnlyXFile(xFile, yFile, 1)
    finalR = 0
    finalAic = 0
    finalLaterList = [0] * 10
    # 初始随机赋值
    laterList = []
    for i in range(10):
        randomNum = random.randint(0, 11)
        laterList.append(randomNum)
    # 先试试跑1000次看看是否收敛
    for k in range(10):
        print('all loop is ' + str(k))
        for i in range(5):
            randLoc = random.randint(0, 9)
            randNum = random.randint(0, 11)
            laterList[randLoc] = randNum
        for i in range(6):
            for j in range(10):
                laterList = oneDimFind(wantX, wantY, laterList, j)
            # print('loop ' + str(i) + ' finished:')
            # for j in range(13):
            #     print(str(laterList[j]), end=' ')
            R2, AIC = changeTimeAicR(wantX, wantY, laterList)

            if AIC < finalAic:
                finalAic = AIC
                finalR = R2
                finalLaterList = laterList.copy()
        for j in range(10):
            print(str(finalLaterList[j]), end=' ')
        print('final r2 is ' + str(finalR))
        print('final aic is ' + str(finalAic))

    np.savetxt(delayFile, finalLaterList, delimiter=',')
    return


# 求Pearson延时系数和KL-DIVERGENCE
# xFile为用电历史数据，yFile为CPI历史数据
# timeStep为想要算到的延时数，推荐取值11（即一年）
# pearFile为pearson相关系数保存文件， klFile为kl-divergence保存文件
def findPearKl(xFile, yFile, timeStep, pearFile, klFile):
    wantX, wantY = makeOnlyXFile(xFile, yFile, 1)
    scaler = preprocessing.StandardScaler().fit(wantX)
    wantX = scaler.transform(wantX)
    xLine, xRow = wantX.shape

    pearsonMatrix = np.zeros((timeStep, xRow))
    klMatrix = np.zeros((timeStep, xRow))

    pearsonList = []
    klList = []

    for i in range(xRow):
        print('begin Dimenson ' + str(i))
        pearsonList, klList = getPearsonX(wantY, wantX[:, i], timeStep)
        # embed()
        pearsonMatrix[:, i] = pearsonList
        klMatrix[:, i] = klList
        print('\n')
    np.savetxt(pearFile, pearsonMatrix, delimiter=",")
    np.savetxt(klFile, klMatrix, delimiter=',')
    return


# 预测下个月CPI
# newxFile为加了当月用电数据的用电历史数据，yFile为CPI历史数据
# testX为当月用电数据
# delayFile为最优延时文件
def predictResult(newxFile, yFile, delayFile):
    laterList = np.loadtxt(delayFile, delimiter=',')
    laterList = laterList.astype(int)
    laterList = list(laterList)

    tmpX, tmpY = makeOnlyXFile(newxFile, yFile, 1)
    newX, newY = changeTimeWantXY(tmpX, tmpY, laterList)

    wantX, wantY = diffMatrix(newX, newY)

    testX = wantX[-1]
    trainX = wantX[:-1]
    trainY = wantY

    bestAlpha = oneridgePredict(trainX, trainY)

    scaler = preprocessing.StandardScaler().fit(wantX)

    wantX = scaler.transform(wantX)

    testX = wantX[-1]
    trainX = wantX[:-1]
    # embed()

    regr = linear_model.Ridge(alpha=bestAlpha)
    # embed()
    regr.fit(trainX, trainY)

    predictY = regr.predict(testX)
    # embed()
    finalResult = np.exp(predictY[0] + tmpY[-1])

    coff = regr.coef_
    finalCoff = coff / coff[0][0]
    finalResult = finalResult[0]
    print('cpi is ' + str(finalResult))
    return finalCoff, finalResult

# changeCPI('./data/beijingcpi.csv', './data/beijinggoodcpi.csv')
# laterList = [0, 0, 0, 5, 2, 1, 7, 1, 1, 9]
# AIC = calAIC('./data/beijingelec.csv', './data/beijing_cpi_good.csv', laterList)
# findTimeDelay('./data/zhejiangelec2.csv', './data/zhejiang_cpi_good.csv', './data/delayzhejiangFile.csv')
# findTimeDelay('./data/beijingelec.csv', './data/beijing_cpi_good.csv', './data/delaybeijingFile.csv')
# findPearKl('all_10.csv', 'cpigood.csv', 11, 'pearson.csv', 'kl.csv')
# predictResult('./data/zhejiangelec2.csv', './data/zhejiang_cpi_predict.csv', './data/delayzhejiangFile.csv')

# findTimeDelay('./data/zhejiangelec.csv', './data/zhejiang_live_good.csv', './data/delayzhejiangLiveFile.csv')
# findPearKl('./data/zhejiangelec.csv', './data/zhejiang_live_good.csv', 11, 'zhejiang_live_pearson.csv', 'zhejiang_live_kl.csv')
# predictResult('./data/zhejiangelec.csv', './data/zhejianggoodcpi_predict.csv', './data/delayzhejiangLiveFile.csv')
