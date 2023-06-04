##this file will count how many users, who rate a control anime X, enjoy a certain show level Y
##mainly used for computational data collection
import pandas as pd
import numpy as np
LISTOFSCORES = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
INPUTANIMEID = ['1535', '16498', '11757', '6547', '10620']
OUTPUTANIMEID = ['9253', '5114', '4224', '19815', '2167']
#loads data from self-generated CSV file
def dataLoader():
    return pd.read_csv(f"{'newAnime.csv'}")

#generates a probability vector in format [P(X=x|Y=1), P(X=x|Y=2)....]
#P(income = constant score | outputAnime = scores 1-10)
def prob_AnimeScoreX_given_ScoreY_Helper(animeScore, currentAnimeID, df, incomeAnimeID):
    probabilityVec = []
    for i in range(10):
        score = i + 1
        countGenre_givenScore = df[(df[incomeAnimeID] == animeScore) & (df[currentAnimeID] == score)].shape[0]
        countScore = df[df[currentAnimeID] == score].shape[0]
        laplaceProbability = (countGenre_givenScore + 1) / (countScore + 2)
        probabilityVec.append(laplaceProbability)
    return probabilityVec


#generates probability table in the form:
#[P(X=x1|Y=1), P(X=x1|Y=2)....]
#[P(X=x2|Y=1), P(X=x2|Y=2)....]
#To access probabilites for a anime score rating, find anime score index number and probTableForAnimeX[1] (for curAnime score = index 1)
def prob_AnimeScoreX_given_ScoreY(trainingData, incomeAnimeID, outputAnimeID):
    probabilityListGenres = np.zeros((10, 10))
    scoreNumber = 0
    for score in LISTOFSCORES:
        listOfProbabilitiesGenreGivenScore = prob_AnimeScoreX_given_ScoreY_Helper(int(score), outputAnimeID, trainingData, incomeAnimeID)
        #TABLE ASSEMBLY LOGIC
        for i in range(len(listOfProbabilitiesGenreGivenScore)):
            probabilityListGenres[scoreNumber][i] = listOfProbabilitiesGenreGivenScore[i]
            #income anime same scores in same row
            #down the rows iterate by outcome anime score
            #next row is one greater than the prev row old anime score
        scoreNumber += 1
    return probabilityListGenres


#generates a dict, matching the probability table (P(inputAnime=x|outputAnime=y)) to its key AnimeID
def animeProbabilityTableGeneration(trainingData, outputAnimeID):
    listOfProbTablesForAnimeX = {}
    for inputAnime in INPUTANIMEID:
        probTableForAnimeX = prob_AnimeScoreX_given_ScoreY(trainingData, inputAnime, outputAnimeID)
        listOfProbTablesForAnimeX[inputAnime] = probTableForAnimeX

    return listOfProbTablesForAnimeX








if __name__ == '__main__':
    allData = dataLoader()
    #trainingData = allData.iloc[:10000]
    trainingData = allData
    animeProbabilityTableGeneration(trainingData, OUTPUTANIMEID[0])
    ##TODO:
        #collect list of shows watched by given user from userstatistics
        #cross reference to count probability that a likes show "X" given their favorite genre is "Y"
        #"X" selected by preference