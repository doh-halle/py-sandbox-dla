def master_yoda(text):
    wordlist = text.split()
    reverse_wordlist = wordlist[::-1]
    return ' '.join(reverse_wordlist)