import csv
from userstatistics import userToFavGenreDict
from userstatistics import dictOfUserAnime



def writeCSV():
    userStats = userToFavGenreDict()
    userAnimeRating = dictOfUserAnime()
    #userStats = {'73510': ('harem', 0.12618296529968454), '73511': ('shoujo', 0.009950248756218905), '73512': ('shoujoai', 0.01818181818181818), '73513': ('psychological', 0.013100436681222707), '73514': ('magic', 0.0012853470437017994), '73515': ('thriller', 0.19540229885057472), '73516': ('psychological', 0.004366812227074236)}
    #print(userStats)
    filename = 'newAnime.csv'
    with open(filename, mode='w', newline='', encoding='UTF-8') as file:
        file.truncate()
        writer = csv.writer(file)
        bigData = [['user','genre']]

        for user in userStats.keys():
            data = []
            data.append(user)
            data.append(userStats[user][0])
            ##sifts through data for specific animes
            scoreListUserSpecific = userAnimeRating[user]
            #control anime
            deathNote = '-1'
            attackOnTitan = '-1'
            swordArtOnline = '-1'
            angelBeats = '-1'
            miraiNikki = '-1'
            #variable anime
            steinsGate = '-1'
            fullmetalAlchemist = '-1'
            toradora = '-1'
            noGameNoLife = '-1'
            clannad = '-1'
            for scoreTuple in scoreListUserSpecific:
                #control
                if scoreTuple[1] == '1535': deathNote = scoreTuple[0]
                if scoreTuple[1] == '16498': attackOnTitan = scoreTuple[0]
                if scoreTuple[1] == '11757': swordArtOnline = scoreTuple[0]
                if scoreTuple[1] == '6547': angelBeats = scoreTuple[0]
                if scoreTuple[1] == '10620': miraiNikki = scoreTuple[0]
                #variable
                if scoreTuple[1] == '9253': steinsGate = scoreTuple[0]
                if scoreTuple[1] == '5114': fullmetalAlchemist = scoreTuple[0]
                if scoreTuple[1] == '4224': toradora = scoreTuple[0]
                if scoreTuple[1] == '19815': noGameNoLife = scoreTuple[0]
                if scoreTuple[1] == '2167': clannad = scoreTuple[0]
            #append all to data
            data.append(deathNote)
            data.append(attackOnTitan)
            data.append(swordArtOnline)
            data.append(angelBeats)
            data.append(miraiNikki)
            data.append(steinsGate)
            data.append(fullmetalAlchemist)
            data.append(toradora)
            data.append(noGameNoLife)
            data.append(clannad)

            bigData.append(data)
        writer.writerows(bigData)


def testCSV():
    reader = csv.DictReader(open('newAnime.csv', encoding="utf8"))
    deathNote = False
    attackOnTitan = False
    swordArtOnline = False
    angelBeats = False
    miraiNikki = False
    # variable anime
    steinsGate = False
    fullmetalAlchemist = False
    toradora = False
    noGameNoLife = False
    clannad = False

    for row in reader:
        # control
        if row['1535'] != '-1': deathNote = True
        if row['16498'] != '-1': attackOnTitan = True
        if row['11757'] != '-1': swordArtOnline = True
        if row['6547'] != '-1': angelBeats = True
        if row['10620'] != '-1': miraiNikki = True
        # variable
        if row['9253'] != '-1': steinsGate = True
        if row['5114'] != '-1': fullmetalAlchemist = True
        if row['4224'] != '-1': toradora = True
        if row['19815'] != '-1': noGameNoLife = True
        if row['2167'] != '-1': clannad = True

    print(deathNote and attackOnTitan and swordArtOnline and angelBeats and miraiNikki and steinsGate and fullmetalAlchemist and toradora and noGameNoLife and clannad)
    return deathNote


if __name__ == '__main__':
    testCSV()