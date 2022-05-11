# Score List to Grade
# 4/20/22
# CTI-110 P5HW1 - Score List
# Zachary Reichel
#

#By using this program, the user enters a score and the program outputs the letter grade.
#10pt grade scale is used in the program.
#A_grade = 90
#B_grade = 80
#C_grade = 70
#D_grade = 60
#F_grade = 50

def Menu():
      scores = []
      while True:
        print('MENU')
        print('-------------------')
        print('1. Create Score List')
        print('2. Display Results')
        print('3. Exit\n')
        choice = input('Please choose one of the menu options: ')
        if choice == '1':
            scores = Score_Input()
        elif choice == '2':
            Display_Results(scores)
        elif choice == '3':
            print('Thank you for playing... \nBye!!')
            break
        else:
            print('Please make a choice from the \'MENU\'.')

def Score_Input():
   scores = []
   num_scores = int(input('How many scores do you want to enter? '))
   print()
   for c in range(num_scores):
      score = (int(input('Enter score #'+ str(c+1) +' : ')))
      while not 0 <= score <= 100 :
         score = int(input('''INVALID Score entered!!!!
Score should be between 0 and 100
Enter score #''' + str(c+1) + ' again: '))
      scores.append(score)
   return(scores)
   
def Display_Results(scores):
   A_grade = 90
   B_grade = 80
   C_grade = 70
   D_grade = 60
   lowest = min(scores)
   scores.remove(min(scores))
   average = sum(scores) / len(scores)
   print()
   print()
   print('---------Results----------')
   print('Lowest Score: ' , lowest)
   print('Modified List: ' , scores)
   print('Scores Average: ', average)
   if average >= A_grade:
      print('Grade : A')
   elif average >= B_grade:
      print('Grade : B')
   elif average >= C_grade:
      print('Grade: C')
   elif average >= D_grade:
      print('Grade : D')
   else:
      print('Grade : F')
   print('--------------------------')


def Main ():
   Menu()


Main()
