import requests
import plotly.graph_objects as go
import json

for i in range(101):
    num = i
    #print(num)
    fact = requests.get('http://numbersapi.com/' + str(i) + '?json')
    print(fact.json()["number"])

fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3], x=['Facts', 'No Facts', 'Extra'])],
    layout_title_text="A Figure Displayed with fig.show()"
)
fig.show()
