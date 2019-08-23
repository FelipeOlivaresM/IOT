from sense_hat import SenseHat
import time
import requests
import math
import random

TOKEN = "A1E-uAVvp0zikgBUkb0Ck0hz6aspFO1aNh"
DEVICE_LABEL = "1234" 
VARIABLE_LABEL_1 = "temp"

# Funcion temperatura

sense = SenseHat()
T  = round(sense.temperature,2)


# Funcion para guardar el dato que se va a enviar

def build_payload(variable_1):

    value_1 = T  # Insertar el dato
    payload = {variable_1: value_1}
    return payload

def post_request(payload):

    # Parametros para realizar el request

    url = "http://things.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Realiza el request

    status = 400
    attempts = 0

    while status >= 400 and attempts <= 5:

        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Resultados del proceso

    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
        random.randint(-10, 50)    your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True

# Funcion principal

def main():

    payload = build_payload(VARIABLE_LABEL_1)
    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")

if __name__ == '__main__':
    while (True):
        main()
	sense.show_message(str(T))
        time.sleep(60) # = Delay
