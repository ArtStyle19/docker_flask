import requests
import csv
import time

while True:
    try:
        response = requests.get('http://localhost:5000/data')
        response.raise_for_status()  # Asegurar que no haya errores HTTP
        
        data = response.json()

        with open('data.csv', mode='a', newline='') as file:  # Usar 'a' para append
            writer = csv.writer(file)
            
            # Escribir solo si hay datos nuevos (evitar encabezados repetidos)
            if len(data) > 0:
                writer.writerows(data)  # Escribir todas las filas a la vez

        print(f'Data written to data.csv at {time.strftime("%Y-%m-%d %H:%M:%S")}')
    
    except requests.exceptions.RequestException as e:
        print(f'Error during request: {e}')

    time.sleep(3)  # Esperar una hora antes de la siguiente ejecución

