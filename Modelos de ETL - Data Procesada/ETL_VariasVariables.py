from datetime import datetime
import csv
import re

myData = list()


with open('DataEntrenamientoVariasVariables.csv') as csvfile:
    with open('DataEntrenamientoVariasVariables1.csv', 'w') as csvfile1:
        fieldnames = ["DateTime","Centro de Alto Rendimiento","Vel Viento","Dir Viento","Temperatura"]

        writer = csv.DictWriter(csvfile1, fieldnames=fieldnames, quoting=csv.QUOTE_ALL,delimiter=',')
        writer.writeheader()
        reader = csv.DictReader(csvfile)
        i= 0
        for row in reader:
            #if i==5:break
            Datet = row['DateTime']
            datatest = Datet.split(" ")[-1]
            valor = row['Centro de Alto Rendimiento']
            print(i)
            if ("24" not in datatest):
                data1 = datetime.strptime(Datet,"%d-%m-%Y %H:%M")  
                myData.append({
                'DateTime':data1,\
                'Centro de Alto Rendimiento':int( float(row['Centro de Alto Rendimiento'])),\
                'Vel Viento':int( float(row['Vel Viento'])),\
                'Dir Viento':int( float(row['Dir Viento'])),\
                'Temperatura':int( float(row['Temperatura']))})
                writer.writerows(myData)
                myData.pop()    
            i+=1 
                    
print("Tamaño real de la data: {}".format(i))
print("ReWriting Complete")