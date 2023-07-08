def vowel_(word_):
    vowels = 'aeiou'
    vowel_count = 0
    for i in word_:
        if i in vowels:
            vowel_count += 1
    return vowel_count


word = input('Enter a word or a sentence: ')
print(vowel_(word))
