from datetime import datetime
import csv
import re

myData = list()


with open('DataEntrenamiento.csv') as csvfile:
    with open('DataEntrenamiento1.csv', 'w') as csvfile1:
        fieldnames = ["DateTime","Carvajal - Sevillana","Centro de Alto Rendimiento","Fontibon","Guaymaral","Kennedy","Las Ferias",\
        "Puente Aranda","San Cristobal","Suba","Usaquen","MinAmbiente","Movil 7ma","Tunal"]

        writer = csv.DictWriter(csvfile1, fieldnames=fieldnames, quoting=csv.QUOTE_ALL,delimiter=',')
        writer.writeheader()
        reader = csv.DictReader(csvfile)
        i= 0
        for row in reader:
            #if i==5:break
            Datet = row['DateTime']
            datatest = Datet.split(" ")[-1]
            valor = row['Carvajal - Sevillana']
            print(i)
            if ("24" not in datatest):
                data1 = datetime.strptime(Datet,"%d-%m-%Y %H:%M")  
                myData.append({'DateTime':data1, 'Carvajal - Sevillana':int( float(row['Carvajal - Sevillana'])),\
                'Centro de Alto Rendimiento':int( float(row['Centro de Alto Rendimiento'])),\
                'Fontibon':int( float(row['Fontibon'])),'Guaymaral':int( float(row['Guaymaral'])),\
                'Kennedy':int( float(row['Kennedy'])),'Las Ferias':int( float(row['Las Ferias'])),\
                'Puente Aranda':int( float(row['Puente Aranda'])),'San Cristobal':int( float(row['San Cristobal'])),\
                'Suba':int( float(row['Suba'])),'Usaquen':int( float(row['Usaquen'])),'MinAmbiente':int( float(row['MinAmbiente'])),\
                'Movil 7ma':int( float(row['Movil 7ma'])),'Tunal':int( float(row['Tunal']))})
                writer.writerows(myData)
                myData.pop()    
            i+=1 
                    
print("Tamaño real de la data: {}".format(i))
print("ReWriting Complete")