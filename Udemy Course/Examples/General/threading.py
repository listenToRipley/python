import threading
import time

# def func(): 
#   print("ran")
#   time.sleep(1)
#   print("done")
#   time.sleep(0.85)
#   print("now done")

# # thread object - one thread
#   # to provide agr to the function that was targeted include a tuple :  args=(value,) 
# x = threading.Thread(target=func)
# # how to we run
# x.start()

# # see the threading as it goes. 
# print(threading.activeCount()) # main thread and x
# time.sleep(1.2)
# print("finally done")

# a thread that counts up to ten

ls = []

def count(n):
  for i in range(1,n+1):
    # print(i)
    ls.append(i)
    time.sleep(0.5)

def countTwo(n):
  for i in range(1,n+1):
    # print(i)
    ls.append(i)
    time.sleep(0.5)

# the _ is an alias
for _ in range(2):
  x = threading.Thread(target=count, args=(5,))
  x.start() # runs twice as fast

  x.join()
  
  y = threading.Thread(target=countTwo, args=(5,))
  y.start()


  y.join() # don't move on until thread is "completed" = stopped running. 
  
print(ls)
print("DONE") # the pause allows to finsih the main thread first. 