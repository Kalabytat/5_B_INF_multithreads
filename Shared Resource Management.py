import threading

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1

num_threads = 10
threads = []

for _ in range(num_threads):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")
print("done")
