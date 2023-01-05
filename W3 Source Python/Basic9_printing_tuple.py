exam_st_date = (11, 12, 2014)
print("Date of the exam is: ", end='')
for i in range(len(exam_st_date)):
    print(exam_st_date[i], "/" if i != (len(exam_st_date) - 1) else "", end="")