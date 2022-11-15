import multiprocessing
import time

def sleep_for_second(s):
    print(f'I am going to sleep {s}',end="\n")
    time.sleep(s)
    print("Done Sleep")
    
# Synchronous
# sleep_for_second(1)
# sleep_for_second(1)
​
# Async 
p1 = multiprocessing.Process(target=sleep_for_second,args=[2])
p2 = multiprocessing.Process(target=sleep_for_second,args=[1])
​
p1.start()
p2.start()
p1.join()
p2.join()
finish = time.perf_counter()
print(f"It is finish in {abs(int(finish))}s")
