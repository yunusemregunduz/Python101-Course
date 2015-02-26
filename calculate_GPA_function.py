''' lets start with something real '''
def covertGrade(grade):
    if grade == 'F':
        return 0
    else:
        return 4 - (ord(grade) - ord('A'))

def getGrades():
    semester_info = []
    more_grades = True
    empty_str = ""
    while more_grades:
        course_grade = input("Enter grade:")
        while course_grade not in ("A", "B", "C", "D", "F", empty_str):
            course_grade = input("Enter letter grade received: ")
            if course_grade == empty_str:
                more_grades = False
            else:
                num_credits = int(input("Enter number of credits: "))
                semester_info.append([num_credits, course_grade])

def calculateGPA(sem_grades_info, cumm_gpa_info):
    sem_quality_pts = 0
    sem_credits = 0
    current_cumm_gpa, total_credits = cumm_gpa_info

    for k in range(len(sem_grades_info)):
        num_credits, letter_grade = sem_grades_info[k]

        sem_quality_pts = sem_quality_pts + num_credits * convertGrade(letter_grade)

        sem_credits = sem_credits + num_credits

    sem_gpa = sem_quality_pts / sem_credits
    new_cumm_gpa = (current_cumm_gpa * total_credits + sem_gpa * sem_credits) / (total_credits + sem_credits)
    return (sem_gpa, new_cumm_gpa)

print("This proram calculates new semester and cummulative GPAs\n")

total_credits = int(input("Enter total number of earned credits: "))
cumm_gpa = float(input("Enter your current cummulative GPA: "))
cumm_gpa_info = (cumm_gpa, total_credits)

print()
semester_grades = getGrades()

semester_gpa, cumm_gpa = calculateGPA(semester_grades, cumm_gpa_info)

print("\nYour semester GPA is", format(semester_gpa, ".2f"))
print("Your new cummulative GPA is", format(cumm_gpa, ".2f"))

#I cant understand is it working or not :D 

    
    
