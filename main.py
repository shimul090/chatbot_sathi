import re
from trainer import bot_response


def bot_digest(message):
    message = re.sub('\W+', ' ', message).strip()
    texts = re.split("\s", message.lower())
    return bot_response(texts)


print('Enter 0 to end the chat')
while True:
    inputs = input('You: ')
    if inputs == '0':
        print('Bye Bye')
        break
    print(bot_digest(inputs))
