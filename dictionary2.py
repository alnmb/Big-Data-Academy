word = input('Hi,\nPlease give me a word and I will count each letter occurrence in it: ')

wordDict = {}

for c in word.lower():
    count = word.count(c)
    wordDict[c] = count

print(wordDict)
