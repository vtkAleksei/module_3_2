def send_email (message, recipient, *, sender = "university.help@gmail.com"):
    signs_of_mail = ['.com', '.net', '.ru']
    is_availability_recipient = False
    is_availability_sender = False
    for symbol in signs_of_mail:
        if symbol in recipient:
            is_availability_recipient = True
        if symbol in sender:
            is_availability_sender = True
    if '@' not in recipient or '@' not in sender:
        print('Невозможно отправить письмо с адреса <', sender, '> на адрес <', recipient ,'>')
    elif not is_availability_recipient or not is_availability_sender:
        print('Невозможно отправить письмо с адреса <', sender, '> на адрес <', recipient, '>')
    elif recipient == sender:
        print('Невозможно отправить письмо самому себе')
    elif sender == "university.help@gmail.com":
        print('Письмо с адреса', sender, 'отправлено на адрес', recipient, 'СООБЩЕНИЕ: ', message)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо с адреса', sender, 'отправлено на адрес', recipient, 'СООБЩЕНИЕ: ', message)

send_email('Привет, проверка связи.', 'user@mail.com')
send_email('Привет, проверка связи.', 'user@mail.com', sender = 'new_user@gmail.ru')
send_email('Привет, проверка связи.', 'user@mail.com', sender = 'user@mail.com')
send_email('Привет, проверка связи.', 'user@mail')