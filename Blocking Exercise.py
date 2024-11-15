import threading
import time

counter = 0

def complex_calculation():
    global counter
    counter = sum(range(1, 1000001))

def status_message(calc_thread):
    while calc_thread.is_alive():
        print("Status: Calculation in progress...")
        time.sleep(0.5)
    print("Calculation completed!")

def exercise():
    calc_thread = threading.Thread(target=complex_calculation)
    status_thread = threading.Thread(target=status_message, args=(calc_thread,))
    
    calc_thread.start()
    status_thread.start()
    
    calc_thread.join()  
    status_thread.join()  
    
    print(f"Final Counter Value: {counter}")
    print("Done")

exercise()