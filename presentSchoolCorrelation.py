
import csv
import numpy as np 

def get_data_src(data_path):
    Days_Present=[]
    MarksInPercentage=[]
    with open(data_path) as csv_file:
             csv_Reader= csv.DictReader(csv_file)
             for row in csv_Reader:
                Days_Present.append(float(row["Days Present"]))
                MarksInPercentage.append(float(row["Marks In Percentage"]))

    return{"x":Days_Present,"y":MarksInPercentage}

def find_correlation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"]) 
    print ("correlation between Days Present and Marks in Percentage\n",correlation[0,1])


def setup():
    data_path="data3.csv"
    datasource=get_data_src(data_path)
    find_correlation(datasource)
setup()
