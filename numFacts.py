import requests
import plotly.graph_objects as go
import time
import json

facts = 0
noFacts = 0
grassNum = 0
waterNum = 0
fireNum = 0


for i in range(250):
    numURL = 'http://numbersapi.com/' + str(i) + '?json'
    pokURL = 'https://pokeapi.co/api/v2/pokemon-species/' + str(1+i)
    pokURL2 = 'https://pokeapi.co/api/v2/pokemon/' + str(1+i)
    num = i
    #print(num)
    while True:
        fact = requests.get(pokURL)
        type = requests.get(pokURL2)
        try:
            #print(fact.json()["number"])
            #print(fact.json()["found"])
            print(fact.json()["name"].capitalize())
            print(type.json()["types"][0]["type"]["name"].capitalize())
            if type.json()["types"][0]["type"]["name"] == "grass":
                grassNum += 1
            if type.json()["types"][0]["type"]["name"] == "fire":
                fireNum += 1
            if type.json()["types"][0]["type"]["name"] == "water":
                waterNum += 1
            if len(type.json()["types"]) == 2:
                print(type.json()["types"][1]["type"]["name"].capitalize())
                if type.json()["types"][1]["type"]["name"] == "grass":
                    grassNum += 1
                if type.json()["types"][1]["type"]["name"] == "fire":
                    fireNum += 1
                if type.json()["types"][1]["type"]["name"] == "water":
                    waterNum += 1
            break
        except:
            pass

fig = go.Figure(
    data=[go.Bar(y=[grassNum, fireNum, waterNum], x=["# Grass", "# Fire", "# Water"])],
    layout_title_text="Number of Pokemon per Type"
)
fig.show()