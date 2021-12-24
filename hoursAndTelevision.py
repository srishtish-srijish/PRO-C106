
import csv
import numpy as np 

def get_data_src(data_path):
    Size_of_TV=[]
    Average_TimeSpent=[]
    with open(data_path) as csv_file:
             csv_Reader= csv.DictReader(csv_file)
             for row in csv_Reader:
                Size_of_TV.append(float(row["Size of TV"]))
                Average_TimeSpent.append(float(row["\tAverage time spent watching TV in a week"]))

    return{"x":Size_of_TV,"y":Average_TimeSpent}

def find_correlation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"]) 
    print ("correlation between size of tv and average time spent watching the tv\n",correlation[0,1])


def setup():
    data_path="data2.csv"
    datasource=get_data_src(data_path)
    find_correlation(datasource)
setup()
