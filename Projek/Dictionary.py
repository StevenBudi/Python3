from difflib import get_close_matches
import json
import os
os.chdir("C:\\Users\ASUS\Documents\Python\Projek")
data = json.load(open("data.json", "r"))


def translate(x):
    x = x.lower()
    if x in data:
        return data[x]
    elif len(get_close_matches(x, data.keys())) > 0:
        opt = input("Did you mean %s ? Enter Y if Yes or N if NO : " %
                    get_close_matches(x, data.keys())[0])
        if opt == "Y" or opt == "y":
            return data[get_close_matches(x, data.keys())[0]]
        elif opt == "N" or opt == "n":
            return "The word doesn't exist. Please double check it"
        else:
            "Your entry not valid."
    else:
        return "The word doesn't exist. Please double check it"


word = str(input("Enter a word : "))

output = translate(word)
if type(output) == list:
    for item in output:
        print(item, end=" ")
else:
    print(output)
