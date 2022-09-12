import random


def unknown():
    response = ["Could you please re-phrase that?", "I don't know.", "What does that mean?"][
        random.randrange(4)]
    return response


def message_probability(user_message, recognized_words, required_words=[]):
    word_found = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            word_found += 1
    percentage = float(word_found) / float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False

    if has_required_words:
        return int(percentage * 100)
    else:
        return 0


def bot_response(message_list):
    max_probability = {}

    def response(output, recognized_words, required_words=[]):
        nonlocal max_probability
        max_probability[output] = message_probability(message_list, recognized_words,
                                                      required_words)

    response('Hello!', ['hello', 'hi', 'hey', 'heyo'])
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('I am Sathi. How can I help you?', ['what', 'your', 'name', 'who', 'are', 'you'])
    response('I eat nothing. I am just a bot.', ['what', 'you', 'eat'], required_words=['what', 'eat'])
    response('Welcome!', ['thank', 'you'])

    best_match = max(max_probability, key=max_probability.get)

    return unknown() if max_probability[best_match] < 1 else best_match
