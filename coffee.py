import plotly.express as px
import csv

with open("data4.csv") as csv_file:
 df = csv.DictReader(csv_file)

#Using px.scatter() method we plotted the scatter graph
 fig = px.scatter(df, x="Coffee in ml", y="sleep in hours", color="week")

#Then using the show method we show the scatter graph
fig.show()