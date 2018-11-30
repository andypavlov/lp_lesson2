def get_summ(num_one, num_two):
    try:
        result = int(num_one) + int(num_two)
        return result    
    except ValueError:
        return

var_one = input('Введите первый аргумент:')
var_two = input('Введите второй аргумент:')
summ = get_summ(var_one, var_two)
if not summ == None:
    print('Сумма аргументнтов равна:',summ)
else:
    print('Агрументы не целого типа')