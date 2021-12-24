import plotly.express as px
import csv

with open("data3.csv") as csv_file:
 df = csv.DictReader(csv_file)

#Using px.scatter() method we plotted the scatter graph
 fig = px.scatter(df, x="Days Present", y="Marks In Percentage",color="Roll No")

#Then using the show method we show the scatter graph
fig.show()