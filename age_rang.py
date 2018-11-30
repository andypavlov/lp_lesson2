your_age = int(input('Сколько-сколько тебе лет?\n'))

def age_interval(age):
    if age < 0:
        age_grade = 'Вот родишься, тогда и поговорим.'
    elif age <= 7:
        age_grade = 'Детский сад, штаны на лямках.'
    elif age <= 18:
        age_grade = 'Школьные годы чудесные.'
    elif age <= 23:
        age_grade = 'От сессии до сессии живут студенты весело!'
    elif age <= 70:
        age_grade = 'Работать негры! Солнце еще высоко.'
    elif age <= 80:
        age_grade = 'Пора на пенсию'
    elif age <= 90:
        age_grade = 'Давно пора на пенсию'    
    elif age <= 123:
        age_grade = 'Давным-давно пора на пенсию'    
    else:
        age_grade = 'Столько не живут.'    
    return age_grade

diagnosis = age_interval(your_age)
print(diagnosis)