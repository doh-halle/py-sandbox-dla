def animal_cracker(text):
    wordlist = text.split()
    
    print(wordlist)
    return wordlist[0][0] == wordlist[1][0]