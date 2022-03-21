# Debugging
# 3-21-22
# CTI-110 P3HW1 - Debugging
# Zachary Reichel

# This program takes a number grade and outputs a letter grade.

def main():
    
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    
    Score = int(input('Enter grade: '))
    if Score >= A_score:
        print('Your grade is: A')
    elif Score >= B_score:
        print('Your grade is: B')
    elif Score >= C_score:
        print('Your grade is: C')
    elif Score >= D_score:
        print('Your grade is: D')  
    else:
        print('Your grade is: F')

main()
