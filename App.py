import json
from difflib import get_close_matches
data=json.load(open("data.json"))

word=input("Enter a word:")


def dictionary(word):
    if word.lower() in data:
        return data[word.lower()]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        check= input("did you mean: "+get_close_matches(word,data.keys())[0]+" (y/n)")
        check=check.upper()
        if check=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif check=="N":
            return "please check your input"
        else:
            return "I am not able to understand you"
    
    else:
        return "please check your input"

output= dictionary(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)