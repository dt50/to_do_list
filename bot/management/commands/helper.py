def parse_message(message):
    text = str(message.text).split(' ')
    user_info = {
        'email': text[0],
        'password': text[1]
    }
    return user_info
