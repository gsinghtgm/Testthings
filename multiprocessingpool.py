from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum

if __name__ == "__main__":

    array = [1,2,3,4,5]
    t1 = time.time()
    p = Pool()
    result = p.map(f,range(10000))
    p.close()
    p.join()
    print(result)

    print("Pool processing took:", time.time()-t1)

    t2 = time.time()
    result = []
    for x in range(10000):
        result.append(f(x))

    print("Serial processing took:", time.time()-t2)