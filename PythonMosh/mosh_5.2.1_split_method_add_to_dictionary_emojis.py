
message = input(">")
words = message.split(" ")
emojis = {
    ":)": "[smily face]",
    ":(": "[sad face]"
}
emojis[":D"] = "[giggle face]"          # přidá do slovníku value "[giggle face]" pod keyword ":D"
output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)