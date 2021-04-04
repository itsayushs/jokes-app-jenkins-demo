# This code will call the jokes api over the internet and then print a joke for you!
import requests
import json

def printJoke():
    apiResponse = requests.get('https://v2.jokeapi.dev/joke/Any')
    response = json.loads(apiResponse.text)
    if response['type'] == "single":
        print(response['joke'])
    else:
        print("It a twopart joke:")
        print("Setup: ",response['setup'],"\n Joke: ",response['delivery'])
    return apiResponse.text
printJoke()