OUTPUTANIMEID = ['9253', '5114', '4224', '19815', '2167']
import pandas as pd

def dataLoader():
    return pd.read_csv(f"{'newAnime.csv'}")

#for a single outputAnime, prob it is rated 1-10
#[rating 1 prob, rating 2 prob...]
def generateProbabilityTableHelper(data, outputAnimeID):
    scoreProb = []
    #creates vector index zero = score 1, index one = score two
    count = data.shape[0]
    for i in range(10):
        score = i + 1
        tempData = data[data[outputAnimeID] == score].shape[0]
        scoreProb.append(tempData / count)
    return scoreProb


def generateProbabilityTable(df, outAnimeIDtoProbabilityRating):
    for outputAnime in OUTPUTANIMEID:
        newDF = df[df[outputAnime] != -1]
        tempVec = generateProbabilityTableHelper(newDF, outputAnime)
        outAnimeIDtoProbabilityRating[outputAnime] = tempVec
    return outAnimeIDtoProbabilityRating



if __name__ == '__main__':
    testDict = {}
    allData = dataLoader()
    trainingData = allData
    generateProbabilityTable(trainingData, testDict)
    print(testDict)
