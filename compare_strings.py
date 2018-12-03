def compare_str(first_str, second_str):
	if not (type(first_str) == str and type(second_str) == str):
		return 0
	elif first_str == second_str:
		return 1
	elif len(first_str) > len(second_str):
		return 2
	elif second_str == 'learn':
			return 3
	else:
		return 4

result_dict = {0:'это не строки', 1:'одинаковые строки', 2:'первая строка длиннее',
				 3:'вторая строка - learn', 4:'незаданные параметры задачи'}

result = compare_str(123, True)
print('{}: {}'.format(result, result_dict[result]))

result = compare_str('Тук', 'Тук')
print('{}: {}'.format(result, result_dict[result]))

result = compare_str('Туки,', 'Тук')
print('{}: {}'.format(result, result_dict[result]))

result = compare_str('Питон', 'learn')
print('{}: {}'.format(result, result_dict[result]))

result = compare_str('Ну ка,', 'попробуем')
print('{}: {}'.format(result, result_dict[result]))
