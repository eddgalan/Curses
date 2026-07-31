import threading
import time

def process_request(request_id):
    print(f'Procesando la solicitud {request_id}')
    time.sleep(3)
    print(f'Solicitud {request_id} procesada')

threads = []
for i in range(3):
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('Fin del programa')