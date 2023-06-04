##this file will count how many users, who prefer a certain genre, enjoy a certain show
##mainly used for computational data collection
import pandas as pd
import numpy as np
LISTOFGENRES = ['comedy', 'action', 'adventure', 'fantasy', 'scifi', 'drama', 'shounen', 'kids', 'romance', 'school']
OUTPUTANIMEID = ['9253', '5114', '4224', '19815', '2167']
#loads data from self-generated CSV file
def dataLoader():
    return pd.read_csv(f"{'newAnime.csv'}")

#generates a probability vector in format [P(X=x|Y=1), P(X=x|Y=2)....]
def prob_GenreX_given_ScoreY_Helper(genre, df, outcomeAnimeID):
    probabilityVec = []
    for i in range(10):
        score = i + 1
        countGenre_givenScore = df[(df['genre'] == genre) & (df[outcomeAnimeID] == score)].shape[0]
        countScore = df[df[outcomeAnimeID] == score].shape[0]
        #print(genre + " " + outcomeAnimeID)
        #print(str(score) + ": " + str(countGenre_givenScore) + " / " + str(countScore))
        laplaceProbability = (countGenre_givenScore + 1) / (countScore + 2)
        probabilityVec.append(laplaceProbability)
    return probabilityVec


#generates probability table in the form:
#[P(X=x1|Y=1), P(X=x1|Y=2)....]
#[P(X=x2|Y=1), P(X=x2|Y=2)....]
#To access probabilites for a given genre, find genre number and probTableForAnimeX[1] (for genre 1)
def prob_GenreX_given_ScoreY(trainingData, outcomeAnimeID):
    probabilityListGenresMatrix = np.zeros((10, 10))
    genreNumber = 0
    for genre in LISTOFGENRES:
        listOfProbabilitiesGenreGivenScore = prob_GenreX_given_ScoreY_Helper(genre, trainingData, outcomeAnimeID)
        #TABLE ASSEMBLY LOGIC
        for i in range(len(listOfProbabilitiesGenreGivenScore)):
            probabilityListGenresMatrix[genreNumber][i] = listOfProbabilitiesGenreGivenScore[i]
        genreNumber += 1
    return probabilityListGenresMatrix


#generates a dict, matching the probability table (P(Genre=x|Anime=y)) to its key AnimeID
def genreProbabilityTableGeneration(trainingData):
    listOfProbTablesForAnimeX = {}
    for anime in OUTPUTANIMEID:
        probTableForAnimeX = prob_GenreX_given_ScoreY(trainingData, anime)
        listOfProbTablesForAnimeX[anime] = probTableForAnimeX
    return listOfProbTablesForAnimeX








if __name__ == '__main__':
    allData = dataLoader()
    #trainingData = allData.iloc[:10000]
    trainingData = allData
    genreProbabilityTableGeneration(trainingData)
    ##TODO:
        #collect list of shows watched by given user from userstatistics
        #cross reference to count probability that a likes show "X" given their favorite genre is "Y"
        #"X" selected by preference

