import plotly.express as px
import csv
import numpy as np 

def get_data_src(data_path):
    Ice_cream_sales=[]
    cold_drink_sales=[]
    with open(data_path) as csv_file:
             csv_Reader= csv.DictReader(csv_file)
             for row in csv_Reader:
                Ice_cream_sales.append(float(row["Temperature"]))
                cold_drink_sales.append(float(row["Ice-cream Sales"]))

    return{"x":Ice_cream_sales,"y":cold_drink_sales}

def find_correlation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"]) 
    print ("correlation between temperature and Ice-Cream sales\n",correlation[0,1])


def setup():
    data_path="data1.csv"
    datasource=get_data_src(data_path)
    find_correlation(datasource)
setup()
