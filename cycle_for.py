test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for list_var in test_list:
    print(list_var + 1)

print('----------------------')

test_string = input('Введите какую-нибудь строку:\n')
for string_char in test_string:
    print(string_char)

print('----------------------')

student_scores = [
                {'scool_class':'9a', 'scores':[4,5,3,4,4,5,5,4]},
                {'scool_class':'9b', 'scores':[3,5,3,5,5,5,5,4,5,3,3]},
                {'scool_class':'10a', 'scores':[5,5,5,4,4,4,3,5,5,4]},
                {'scool_class':'10b', 'scores':[3,3,4,4,4,5,5,5,4]}
                ]

scool_score = 0

for count in student_scores:
    middle_class_score = round(sum(count['scores'])/len(count['scores']),1)
    print('Средняя оценка в {} классе = {}'.format(count['scool_class'],middle_class_score))
    scool_score += middle_class_score 
print ('Средняя оценка по школе = {}'.format(round(scool_score/len(student_scores),1)))
