answer_dict = {
            'Как дела?':'Отлично!',
            'Тебя как зовут?':'Леха!',
            'Кем ты хочешь стать?':'Космонавтом!',
            'Главный ответ?':'42'
}

def ask_user():
    try:
        while True:
            user_say = input('Спроси меня что-нибудь?\n')
            if user_say == 'Что за ...?' or user_say == 'WTF?':
                print('You are win!')
                break
            elif user_say in answer_dict:
                print('{}\n'.format(answer_dict[user_say]))
            else:
                print('Это конечно интересно, {}, но...\n'.format(user_say))
    except KeyboardInterrupt:
        print('Это запрещенный прием!\nПока!')

ask_user()
