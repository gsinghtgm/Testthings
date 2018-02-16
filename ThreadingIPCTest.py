import multiprocessing
import time

def calc_square(numbers,q):
    for n in numbers:
        q.put(n*n)

if __name__ == "__main__":
    numbers = [2,4,8,16,32,64,128]
    t1 = time.time()
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square,args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())

    print("This took:",time.time()-t1,"seconds")