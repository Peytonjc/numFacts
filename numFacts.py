import requests
import plotly.graph_objects as go
import time
import json

facts = 0
noFacts = 0


for i in range(800):
    numURL = 'http://numbersapi.com/' + str(i) + '?json'
    pokURL = 'https://pokeapi.co/api/v2/pokemon-species/' + str(1+i)
    num = i
    #print(num)
    while True:
        fact = requests.get(pokURL)
        try:
            #print(fact.json()["number"])
            #print(fact.json()["found"])
            print(fact.json()["name"].capitalize())
            break
        except:
            pass

fig = go.Figure(
    data=[go.Bar(y=[fact, noFacts], x=['Facts', 'No Facts'])],
    layout_title_text="A Figure Displayed with fig.show()"
)
fig.show()