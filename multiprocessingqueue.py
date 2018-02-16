import multiprocessing

def calc_sqaure(numbers, q):
    for n in numbers:
        q.put(n*n)

if __name__ == "__main__":
    numbers = [2,3,4]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_sqaure,args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
       print(q.get())