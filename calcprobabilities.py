#Bayesian Network
import csv
import heapq
import re


##cleans a key of so only alphanumeric character remain; uses "re" library
def cleanKey(input):
    input = re.sub(r'\W+', '', input).lower()
    return input

##creates a dictionary containing various stats about anime; used to compute probabilities
##prints 10 most popular anime genres
##animeDict contains counts of the popularity of each genre
##animeDictUsers matches a genre to all the anime_id's with that genre
##animeDictIdToGenre matches an anime to it's genres
def generateGenreStatistics():
    reader = csv.DictReader(open('anime.csv', encoding="utf8"))
    animeDict = {}
    animeDictUsers = {}
    animeDictIdToGenre = {}

    netAnimeCount = 0
    for row in reader:
        netAnimeCount += 1
        genres = row['genre']
        listGenre = genres.split(',')
        animeDictIdToGenre[row['anime_id']] = []
        for genre in listGenre:
            key = cleanKey(genre)
            if (key not in animeDict.keys()):
                animeDict[key] = 0
                animeDictUsers[key] = []
            animeDictIdToGenre[row['anime_id']].append(key)
            animeDict[key] += 1
            animeDictUsers[key].append(row['anime_id'])
    ##sorted anime list represents a comprehensive count of the statistics of every genre
    sortedAnimeList = sorted(animeDict.items(), key=lambda item: item[1], reverse=True)
    for index in range(10):
        print(str(sortedAnimeList[index]) + " Percent of Total: " + str(sortedAnimeList[index][1] / netAnimeCount))
    ##print(sortedAnimeList)
    print("\n")
    return [animeDictIdToGenre, animeDict]

##prints 20 most popular animes
def generatePopularAnime(animeIdDict):
    reader = csv.DictReader(open('anime.csv', encoding="utf8"))
    listOfTopAnime = []
    heapq.heapify(listOfTopAnime)
    for row in reader:
        namePopTuple = (int(row['members']), row['name'])
        if (len(listOfTopAnime) < 20):
            heapq.heappush(listOfTopAnime, namePopTuple)
        elif(listOfTopAnime[0][0] < namePopTuple[0]):
            heapq.heappop(listOfTopAnime)
            heapq.heappush(listOfTopAnime, namePopTuple)
    while (len(listOfTopAnime) != 0):
        var = heapq.heappop(listOfTopAnime)
        print(var)
        print(animeIdDict[cleanKey(var[1])])

##returns a dict matching anime name to id
def animeToID():
    reader = csv.DictReader(open('anime.csv', encoding="utf8"))
    nameIdDict = {}
    for row in reader:
        nameIdDict[cleanKey(row['name'])] = row['anime_id']
    return nameIdDict

#inverse of the above
def IDtoanime():
    reader = csv.DictReader(open('anime.csv', encoding="utf8"))
    nameIdDict = {}
    for row in reader:
        nameIdDict[cleanKey(row['anime_id'])] = row['name']
    return nameIdDict



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    animeDictIdToGenre = generateGenreStatistics()
    userIdDict = animeToID()
    generatePopularAnime(userIdDict)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
