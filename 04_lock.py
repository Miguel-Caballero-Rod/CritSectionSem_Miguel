from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value, Array
from multiprocessing import Lock

N = 8

def task(common, tid, lock):
    a = 0
    for i in range(10):
        print(f"{tid}−{i}: Non−critical Section")
        a += 1
        print(f"{tid}−{i}: End of non−critical Section")
        lock.acquire()
        print(f"{tid}−{i}: Critical section")
        v = common.value + 1
        print(f"{tid}−{i}: Inside critical section")
        common.value = v
        print(f"{tid}−{i}: End of critical section")
        lock.release()
def main():
    lp = []
    common = Value("i", 0)
    lock=Lock()
    for tid in range(N):
        lp.append(Process(target=task, args=(common, tid, lock)))
    print (f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()
    for p in lp:
        p.join()
    print (f"Valor final del contador {common.value}")
    print ("fin")
if __name__ == "__main__":
    main()
