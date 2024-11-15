import threading
import time


def increment():
   for increment in range(1, 11):
       print(f"increment_thread: {increment}")
       time.sleep(1)
def decrease():
   for decrease in range(10, 0, -1):
       print(f"decrease_thread: {decrease}")
       time.sleep(1)


increment_thread = threading.Thread(target=increment)
decrease_thread = threading.Thread(target=decrease)


increment_thread.start()
decrease_thread.start()


increment_thread.join()
decrease_thread.join()


print("Done")