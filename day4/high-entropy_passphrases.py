from day4.day4_input import passphrases

result = 0
for phrase in passphrases:
    words = phrase.split(' ')
    result += 1 if len(words) == len(set(words)) else 0

print(result)
