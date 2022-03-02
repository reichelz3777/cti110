# CTI-110
# P2HW2 - List and Sets
# Zachary Reichel
# 2/28/22

#Enter 7 scores and store in list
#Determine the lowest score and store in a variable
#Drop lowest score from list
#Calculate Score average after having dropped lowest score

ScoreList = []

score1 = float(input('Enter score #1: '))
ScoreList.append(score1)
score2 = float(input('Enter score #2: '))
ScoreList.append(score2)
score3 = float(input('Enter score #3: '))
ScoreList.append(score3)
score4 = float(input('Enter score #4: '))
ScoreList.append(score4)
score5 = float(input('Enter score #5: '))
ScoreList.append(score5)
score6 = float(input('Enter score #6: '))
ScoreList.append(score6)
score7 = float(input('Enter score #7: '))
ScoreList.append(score7)

print('\n')
print('--------------Results-----------')

print('Lowest Score  : '+str(min(ScoreList)))

ScoreList.remove(min(ScoreList))
      
print('Modified List :', end= ' ')
print(ScoreList)

ScoreAvg = sum(ScoreList)/len(ScoreList)
ScoreAvg = "{:.2f}".format(ScoreAvg)
      
print('Scores Average:', ScoreAvg)

print('----------------------------------')
