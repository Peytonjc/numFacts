import requests
import json

number = input("Please type a number: ")
fact = requests.get('http://numbersapi.com/' + ''.join(number) + '?json')
print(fact.json()["text"])
