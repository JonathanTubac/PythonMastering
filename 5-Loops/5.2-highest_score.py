student_scores = [150, 230, 120, 24, 23, 12, 20, 420, 1, 2, 230, 20, 120, 320, 123, 321, 542, 100, 230, 200, 125, 321]
#1-get the total score
#option 1
#total_exam_score = sum(student_scores)

#option 2
sum = 0
for score in student_scores:
    sum += score
print(sum)

#2-Max score in list
#option 1
#max = max(student_scores)

#option 2
max = 0
for score in student_scores:
    if score > max:
        max = score
    else:
        pass
print(max)