rownumber = int(input("write row quantity: "))
wordlist = []
word = {}
for i in range(1, rownumber + 1):
    words = input("write words and synonims: ")
    words = words.split()
    print(words)
    wordlist.append(words)
