import numpy as np 
import time 
 
n = 1_000_000 
lista = list(range(n)) 
array = np.arange(n) 
 
inicio = time.time() 
resultado_lista = [x + 10 for x in lista] 
print("Bucle for:", time.time() - inicio, "segundos") 
 
inicio = time.time() 
resultado_array = array + 10 
print("Vectorizado:", time.time() - inicio, "segundos") 