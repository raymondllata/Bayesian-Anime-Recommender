from calcprobabilities import generateGenreStatistics, cleanKey
import csv
##for a given user, calculates the following statistics
##favorite genre given their top 100 animes (or less)
##quantify data??

##create a dict binding userid to a list of shows watched (marked by id)
def dictOfUserAnime():
    reader = csv.DictReader(open('rating.csv', encoding="utf8"))
    userToTopShow = {}
    for row in reader:
        if row['user_id'] not in userToTopShow.keys():
            userToTopShow[row['user_id']] = []
        scoreRatingTuple = (int(row['rating']), row['anime_id'])
        if (scoreRatingTuple[0] != -1):
            userToTopShow[row['user_id']].append(scoreRatingTuple)
    return userToTopShow

##finds a list of show swatched by specfic user
def singleUserAnime(user_id):
    reader = csv.DictReader(open('rating.csv', encoding="utf8"))
    listShows = []
    for row in reader:
        if row['user_id'] == user_id:
            scoreRatingTuple = (int(row['rating']), row['anime_id'])
            if (scoreRatingTuple[0] != -1):
                listShows.append(scoreRatingTuple)
    return listShows

#make dict counting a users genre watch count
def findFavGenre(IDtoGenre, pastShows, genreCount):
    dictGenreCount = {}
    for show in pastShows:
        if show[1] in IDtoGenre:
            listGenre = IDtoGenre[show[1]]
            for genre in listGenre:
                if genre not in dictGenreCount.keys():
                    dictGenreCount[genre] = 0
                dictGenreCount[genre] += 1
    favGenre = ('', 0)

    for genre in dictGenreCount.keys():
        if (genre == 'comedy' or genre == 'action' or genre == 'adventure' or genre == 'fantasy' or genre == 'scifi'or genre == 'drama' or genre == 'shounen' or genre == 'kids' or genre == 'romance' or genre == 'school'):
            dictGenreCount[genre] = (dictGenreCount[genre] / genreCount[genre])
            if dictGenreCount[genre] > favGenre[1]:
                favGenre = (genre, dictGenreCount[genre])
    return favGenre

##main caller function
def userToFavGenreDict():
    resultsVec = generateGenreStatistics()
    animeDictIdToGenre = resultsVec[0]
    animeGenreCount = resultsVec[1]
    dictOfUserToAnime = dictOfUserAnime()
    userToFavGenreDict = {}
    for userID in dictOfUserToAnime.keys():
        user_id = userID
        listOfAnime = dictOfUserToAnime[user_id]
        favGenreStat = findFavGenre(animeDictIdToGenre, listOfAnime, animeGenreCount)
        if favGenreStat[0] != '':
            userToFavGenreDict[user_id] = favGenreStat
    return userToFavGenreDict
















# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print(userToFavGenreDict())
    print(dictOfUserAnime()





























          )
    # resultsVec = generateGenreStatistics()
    # animeDictIdToGenre = resultsVec[0]
    # animeGenreCount = resultsVec[1]
    # #dictOfUserToAnime = dictOfUserAnime()
    # user_id = '3'
    # #listOfAnime = singleUserAnime(user_id)
    # ##delete later
    # listOfAnime = [(8, '20'), (6, '154'), (9, '170'), (10, '199'), (9, '225'), (6, '341'), (7, '430'), (7, '527'), (7, '552'), (10, '813'), (7, '1119'), (7, '1121'), (7, '1122'), (8, '1132'), (6, '1292'), (8, '1313'), (7, '1526'), (10, '1535'), (7, '1564'), (8, '1689'), (6, '1764'), (8, '1943'), (7, '2201'), (7, '2404'), (7, '2847'), (8, '3588'), (7, '4026'), (10, '5114'), (8, '5231'), (7, '6178'), (8, '6702'), (6, '6880'), (7, '7695'), (6, '8074'), (6, '9107'), (7, '9135'), (9, '9760'), (8, '9917'), (8, '9919'), (10, '9989'), (7, '10408'), (8, '10507'), (8, '11111'), (6, '11703'), (7, '11737'), (9, '11757'), (7, '11759'), (10, '11771'), (3, '12671'), (8, '14075'), (7, '14093'), (8, '14345'), (10, '14513'), (10, '16498'), (5, '16512'), (7, '16782'), (10, '16894'), (8, '16918'), (7, '17265'), (7, '18097'), (10, '18115'), (7, '18393'), (3, '19315'), (9, '19815'), (5, '20021'), (10, '20159'), (8, '20507'), (9, '20583'), (6, '21507'), (7, '21881'), (8, '22199'), (8, '22297'), (6, '22319'), (6, '22547'), (7, '22729'), (8, '23301'), (6, '23321'), (4, '23333'), (8, '23755'), (10, '24415'), (6, '26243'), (8, '27631'), (8, '27899'), (9, '28121'), (10, '28171'), (6, '28223'), (7, '28497'), (9, '28701'), (9, '28891'), (6, '29854'), (10, '31043'), (7, '31859')]
    # ##delete later
    # favGenreStat = findFavGenre(animeDictIdToGenre, listOfAnime, animeGenreCount)
    # print('User ID: ' + user_id + ' | Favorite Genre: ' + str(favGenreStat))

