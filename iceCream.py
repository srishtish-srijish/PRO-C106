import plotly.express as px
import csv

with open("data1.csv") as csv_file:
 df = csv.DictReader(csv_file)

#Using px.scatter() method we plotted the scatter graph
 fig = px.scatter(df, x="Temperature", y="Ice-cream Sales",color="Cold drink sales")

#Then using the show method we show the scatter graph
fig.show()