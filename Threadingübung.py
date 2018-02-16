import time
import threading

def calc_square(zahlen):
    print("Berechnung der ein gespeicherten Zahlen")
    for n in zahlen:
        time.sleep(0.2)
        print("calc_square:", n*n)

def calc_cube(zahlen):
    print("Berechnung der ein gespeicherten Zahlen")
    for n in zahlen:
        time.sleep(0.2)
        print("calc_cube:",n*n*n)

arr = [4,8,16,32,64,128,256,512,1024]

t = time.time()

t1 = threading.Thread(target=calc_square,args=(arr,))
t2 = threading.Thread(target=calc_cube,args=(arr,))

t1.start() #Thread 1 started und berechnet die jeweiligen Werte die ihm zugestellt wurden

t1.join()  #Es wird gewartet bis Thread 1 mit der Aufgabe fertig wird

t2.start() #Thread 2 started und berechnet die jeweiligen Werte die ihm zugestellt wurden
t2.join()  #Es wird gewartet bis Thread 2 mit der Aufgabe fertig wird

print("Der Vorgang wurde vollendet in: ",time.time()-t)
print("Es sind kein Aufträge mehr verfügbar")

