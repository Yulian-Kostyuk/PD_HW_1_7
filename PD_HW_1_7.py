grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print('Список оценок:', grades)
print('Множество учеников:', students)
students_list = list(students)
st_list_s = sorted(students_list)
print('Список учеников:', st_list_s)
av_grade_1 = sum(grades[0][0:])/len(grades[0])
# print(len(grades[0]))
# print(av_grade_1)
av_grade_2 = sum(grades[1][0:])/len(grades[1])
av_grade_3 = sum(grades[2][0:])/len(grades[2])
av_grade_4 = sum(grades[3][0:])/len(grades[3])
av_grade_5 = sum(grades[4][0:])/len(grades[4])
list_av_grades = [av_grade_1, av_grade_2, av_grade_3, av_grade_4, av_grade_5]
# print(list_av_grades)
# print(dictionary_st)
dictionary_st = {st_list_s[0]: av_grade_1,
                 st_list_s[1]: av_grade_2,
                 st_list_s[2]: av_grade_3,
                 st_list_s[3]: av_grade_4,
                 st_list_s[4]: av_grade_5}
print('Словарь учеников:', dictionary_st)
