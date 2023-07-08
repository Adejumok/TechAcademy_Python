def search(sentence, word):
    if word in sentence:
        return True
    else:
        return False


def check_output(sentence_, word_):
    if search(sentence_, word_):
        print('Found')
    else:
        print('Not Found')


sentence = input('Enter a sentence: ')
word = input('Enter a word: ')
check_output(sentence, word)
