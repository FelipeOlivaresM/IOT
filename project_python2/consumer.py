from matplotlib import cm
from pykafka import KafkaClient
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation


y_range=[0,30]
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.grid()
xs = []
ys = []
ax.set_ylim(y_range)





client = KafkaClient(hosts="127.0.0.1:9092")
print ("Listado de Topics actuales")
print(client.topics)
topic = client.topics['Hello-Kafka']
contador=0
consumer = topic.get_simple_consumer()
print ("Recibiendo Mensajes")
for message in consumer:
    if message is not None:
        print("---------------------") 
    #    print("Mensaje proveniente del productor")
        
        
        def animate(i, xs, ys):
            
            xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
            ys.append(float(message.value))
            xs = xs[-20:]
            ys = ys[-20:]
            ab= float(message.value)
            ax.clear()
            if ab>18:
                ax.plot(xs, ys, marker='x', color='r',label="Temperatura Actual")
            else:
                ax.plot(xs, ys, marker='o', color='b',label="Temperatura Actual")
            plt.legend(loc="upper left")
            plt.ylim(0,30)
            plt.xticks(rotation=45, ha='right')
            plt.subplots_adjust(bottom=0.30)
            plt.title('Control de Temperatura avicola')
            plt.ylabel('Temperature Node') 
            plt.xlabel('Time') 
            

        ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=20000)
        print message.value
        print message.offset 
        

        if message.offset==100000:
            plt.show()

        plt.pause(1)
        
      
        
