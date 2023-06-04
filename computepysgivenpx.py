import pandas as pd
from countingGenreProbabilities import genreProbabilityTableGeneration
from countingAnimeSpecificProbabilities import animeProbabilityTableGeneration
from probabilityFinalAnimeRatingY import generateProbabilityTable
import math
from calcprobabilities import IDtoanime


LISTOFGENRES = ['comedy', 'action', 'adventure', 'fantasy', 'scifi', 'drama', 'shounen', 'kids', 'romance', 'school']
OUTPUTANIMEID = ['9253', '5114', '4224', '19815', '2167']
INPUTANIMEID = ['1535', '16498', '11757', '6547', '10620']

# vector ratings for control anime
#score input/used differs
#int 9 = 10/10
#int 0 = 1/10
#etc etc
#Death Note, AOT, SAO, Angel Beats, Mirai Nikki
#x_set = ['comedy', 5, 5, 5, 5, 5]
#x_set = ['action', 6, 9, 9, 3, 3]
x_set = ['romance', 0, 9, 9, 0, 0]

def dataLoader():
    return pd.read_csv(f"{'newAnime.csv'}")

#xset[0] = genre string
# xset[1-5] follows indexing of inputanimeID
#for a specfific output, calculates the probability of every score (vector)
def compute_specific_y_givenxset(x_set, genreProbabilityTable, animeProbabilityTables, likelihoodTable, outputAnime):
    scoreVector = []
    for y in range(10):
        initialProb = 1
        #computing p_y's
        score_y = y + 1
        probScoreY = likelihoodTable[outputAnime][y]
        initialProb *= probScoreY

        #computing p(x | y) = p(x1|y)*p(x2|y)...
        #GENRE FIRST
        genre = LISTOFGENRES.index(x_set[0])
        if genre == -1:
            print("DOES NOT CONTAIN GENRE")
            return
        p_genre = genreProbabilityTable[outputAnime][genre][y]
        initialProb *= p_genre

        #INDIVIDUAL ANIME SCORES
        for i in range(len(x_set) - 1):
            currentScore = x_set[i + 1]
            curIDNum = INPUTANIMEID[i]
            p_x_feature = animeProbabilityTables[outputAnime][curIDNum][currentScore][y]
            initialProb *= math.log(p_x_feature, 10)
        scoreVector.append(abs(initialProb))

    maxVal = max(scoreVector)
    scoreOfMax = scoreVector.index(maxVal) + 1
    percentScoreNameTuple = (maxVal, scoreOfMax, outputAnime)
    return percentScoreNameTuple






#computes once for every output anime
def compute(x_set, genreProbabilityTable, animeProbabilityTables, likelihoodTable):
    tupleList = []
    for outputAnime in OUTPUTANIMEID:
        scoreTuple = compute_specific_y_givenxset(x_set, genreProbabilityTable, animeProbabilityTables, likelihoodTable, outputAnime)
        tupleList.append(scoreTuple)

    #finding all score tuples that have the maximum rating of the set
    max_value = float('-inf')
    max_tuples = []
    for item in tupleList:
        if item[1] > max_value:
            max_value = item[1]
            max_tuples = [item]
        elif item[1] == max_value:
            max_tuples.append(item)

    #going to return score tuple with highest percentage
    max_tuple = max(max_tuples, key=lambda item: item[0])

    return max_tuple

def resultStage(scoreTuple, x_set):
    IDtoAnimeDict = IDtoanime()
    animeName = IDtoAnimeDict[scoreTuple[2]]
    print("Hi, I am am Anime Recommender Machine Learning Model v0!")
    print("Here is your Data:")
    print("Favorite Genre: " + x_set[0])
    print("Death Note Rating: " + str(x_set[1]) + " out of 10")
    print("Attack On Titan Rating: " + str(x_set[2]) + " out of 10")
    print("Sword Art Online Rating: " + str(x_set[3]) + " out of 10")
    print("Angel Beats Rating: " + str(x_set[4]) + " out of 10")
    print("Mirai Nikki Rating: " + str(x_set[5]) + " out of 10")
    print("Based on your Data, I recommend you watch: " + str(animeName) + " !")
    print("Hope You Enjoy!")
    return



def main():
    trainingData = dataLoader()

    #dict mapping outcomeAnime 10x10 prob matrix
    #matrix syntax: probabilityListGenresMatrix[genreNumber][y_rating = index + 1]
    genreProbabilityTable = genreProbabilityTableGeneration(trainingData)

    #takes in trainingData, and a single outputAnime ID \\ form of a dict mapping to a dict mapping to a table
    #dict1 = outputAnime dict2 inputAnime -> probability Table
    # income anime same scores in same row
    # down the rows iterate by outcome anime score
    # next row is one greater than the prev row old anime score
    # probabilityListGenres[scoreNumber][i]
    animeProbabilityTables = {}
    for outputAnime in OUTPUTANIMEID:
        animeProbabilityTableSingle = animeProbabilityTableGeneration(trainingData, outputAnimeID=outputAnime)
        animeProbabilityTables[outputAnime] = animeProbabilityTableSingle

    #p_y calculation
    #returns a dict, mapping a given output anime to its probability vector
    #index 0 = score 1, index 1 = score 2...
    likelihoodTable = {}
    generateProbabilityTable(trainingData, likelihoodTable)


    scoreTuple = compute(x_set, genreProbabilityTable, animeProbabilityTables, likelihoodTable)
    resultStage(scoreTuple, x_set)

if __name__ == '__main__':
    main()