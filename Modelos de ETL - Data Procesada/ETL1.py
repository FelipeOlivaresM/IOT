from datetime import datetime
import csv
import re

myData = list()


with open('DataEntrenamiento2.csv') as csvfile:
    with open('DataEntrenamiento3.csv', 'w') as csvfile1:
        fieldnames = ["DateTime","Centro de Alto Rendimiento"]

        writer = csv.DictWriter(csvfile1, fieldnames=fieldnames, quoting=csv.QUOTE_ALL,delimiter=',')
        writer.writeheader()
        reader = csv.DictReader(csvfile)
        i= 0

        for row in reader:

            val1 = row['Centro de Alto Rendimiento']
            if val1!="0":
                myData.append({'DateTime':row['DateTime'],'Centro de Alto Rendimiento':row['Centro de Alto Rendimiento']})
                writer.writerows(myData)
                myData.pop()                
                i+=1 
                    
print("Tamaño real de la data: {}".format(i))
print("ReWriting Complete")