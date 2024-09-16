def dashboard():
    print('==================================')
    mathematics = float(input('Enter Mathematics Grade: '))
    science = float(input('Enter Science Grade: '))
    english = float(input('Enter English Grade: '))
    dsa = float(input('Enter DSA Grade: '))
    computer_programming = float(input('Enter Com_Prog Grade: '))
    print('===================================')

    array_grades = [mathematics, science, english, dsa, computer_programming]
    subjects = ['Mathematics', 'Science', 'English', 'DSA', 'Com_Prog']

    separator = '==================================='


    for i in range(len(array_grades)):   
        if array_grades[i] <= 3.0:
            print(subjects[i],separator , array_grades[i],separator, 'passed')
        else:
           
            print(subjects[i],separator , array_grades[i],separator, 'Failed')






name = input('Enter Name : ')
student_id = int(input('Enter Student ID : '))
section = input('Enter Section : ')

dashboard()



#functions for calculate avg grade
def average():
    print('======================================================')
    print('                   AVERAGE GRADE                      ')

    pre_lim = float(input('Enter PRELIM GRADE : '))
    midterm = float(input('Enter MIDTERM GRADE : '))
    pre_final = float(input('Enter PREFINAL GRADE : '))
    final_grade = float(input('Enter FINAL GRADE '))

    avg_grade = (pre_lim + midterm + pre_final + final_grade) / 4

    print('\n AVERAGE GRADE : ', avg_grade)

average()
