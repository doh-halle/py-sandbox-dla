message = input(">")
sentence = message.split(" ")
emojis = {
    ":)": "😀",
    ":(": "☹️"
}
output = ""
for word in sentence:
    output += emojis.get(word, word) + " "
print(output)