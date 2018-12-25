#solusi ini tidak maksimal, masih ada test case yang tidak tercover

# def climbingLeaderboard(scores, alice):
#     scores.sort(reverse = True)
#     # membuat setiap elemen di list menjadi unik
#     newScores = newScores = sorted(set(scores), reverse = True)


#     for score in alice:
#         if score in newScores:
#             print(newScores.index(score)+1)
#         else:
#             score = [score]
#             newScores.extend(score)
#             newScores.sort(reverse = True)
#             score = score[0]
#             print(newScores)
#             print(newScores.index(score)+1)

# ini solusi yang menurut saya sangat bagus
# Saya selalu terkesima denganm program yang ditulis oleh [para master]
def climbingLeaderboard(scores, alice):
    scores.sort(reverse = True)
    # membuat setiap elemen di list menjadi unik
    newScores = sorted(set(scores), reverse = True)
    ranking = []
    l = len(newScores)
    for score in alice:
        while l > 0 and score >= newScores[l-1]:
            l -= 1
            print(l)
            print(newScores[l-1])
        ranking.append(l+1)

    print(ranking)

climbingLeaderboard([100, 100, 50, 40, 20, 10], [5, 25, 50, 102])