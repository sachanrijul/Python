# ------------------- Python Threading Module (Complete Notes) -------------------

"""
🧵 Threading in Python allows concurrent execution of code using multiple threads.
Each thread runs independently but shares memory with other threads.

Python threads are best for I/O-bound tasks (networking, file I/O).
Due to the Global Interpreter Lock (GIL), threads do not run truly in parallel on multiple cores for CPU-bound tasks.
"""

import threading
import time

# ------------------- 1. Creating a Simple Thread -------------------

def greet():
    print("Hello from thread")
    
# Create thread object
t1 = threading.Thread(target=greet)

# Start thread
t1.start()

# Wait for it to finish
t1.join()

# ------------------- 2. Passing Arguments to Thread -------------------

def greet_with_name(name, delay):
    time.sleep(delay)
    print(f"Hello {name}")

t2 = threading.Thread(target=greet_with_name, args=("Alice", 1))
t2.start()
t2.join()

# ------------------- 3. Subclassing Thread -------------------

class MyThread(threading.Thread):
    def run(self):
        print("Running inside subclassed thread")

t3 = MyThread()
t3.start()
t3.join()

# ------------------- 4. Checking If Thread is Alive -------------------

t4 = threading.Thread(target=time.sleep, args=(2,))
t4.start()
print("Is thread alive?", t4.is_alive())
t4.join()

# ------------------- 5. Daemon Threads -------------------

"""
Daemon threads run in background and die when the main program exits.
Use for background tasks like logging, monitoring, etc.
"""

def background_task():
    while True:
        print("Running background task...")
        time.sleep(1)

daemon_thread = threading.Thread(target=background_task, daemon=True)
daemon_thread.start()

time.sleep(3)
print("Main thread ending. Daemon will stop.")

# ------------------- 6. Using Lock for Synchronization -------------------

"""
Race condition: When two threads access shared data at the same time,
the result is unpredictable.

Lock is used to prevent race conditions.
"""

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:  # safer than lock.acquire()/release()
            counter += 1

t5 = threading.Thread(target=increment)
t6 = threading.Thread(target=increment)

t5.start()
t6.start()

t5.join()
t6.join()

print("Final counter:", counter)

# ------------------- 7. RLock (Reentrant Lock) -------------------

"""
RLock allows the same thread to acquire the lock multiple times.
Useful when functions call each other and use the same lock.
"""

rlock = threading.RLock()

def outer():
    with rlock:
        print("Outer acquired")
        inner()

def inner():
    with rlock:
        print("Inner acquired")

t7 = threading.Thread(target=outer)
t7.start()
t7.join()

# ------------------- 8. Timer Threads -------------------

"""
Thread that runs a function after a delay
"""

def delayed_hello():
    print("Hello after delay")

timer_thread = threading.Timer(2.0, delayed_hello)
timer_thread.start()
timer_thread.join()

# ------------------- 9. Event Objects -------------------

"""
Events are flags that can be set or cleared and used to control threads.
"""

event = threading.Event()

def wait_for_event():
    print("Waiting for event...")
    event.wait()
    print("Event triggered!")

t8 = threading.Thread(target=wait_for_event)
t8.start()

time.sleep(2)
event.set()
t8.join()

# ------------------- 10. Semaphore -------------------

"""
Semaphore allows limited access to a shared resource.
"""

sem = threading.Semaphore(2)

def limited_access(name):
    print(f"{name} waiting to acquire semaphore")
    with sem:
        print(f"{name} acquired semaphore")
        time.sleep(2)
        print(f"{name} released semaphore")

for i in range(4):
    threading.Thread(target=limited_access, args=(f"Thread-{i}",)).start()

# ------------------- 11. Condition Variables -------------------

"""
Used for complex thread communication (producer-consumer problems).
"""

buffer = []
condition = threading.Condition()

def producer():
    with condition:
        buffer.append("data")
        print("Produced data")
        condition.notify()

def consumer():
    with condition:
        condition.wait()
        print("Consumed data:", buffer.pop())

threading.Thread(target=consumer).start()
time.sleep(1)
threading.Thread(target=producer).start()

# ------------------- Summary -------------------

"""
✔ Thread(target=func, args=(), kwargs={}) → create threads
✔ start(), join(), is_alive() → thread control
✔ Daemon threads → background execution
✔ Subclass Thread for OOP usage
✔ Lock, RLock → synchronize access
✔ Semaphore → limit simultaneous access
✔ Event → control flow using flags
✔ Timer → delayed execution
✔ Condition → complex communication
"""

# ------------------- End of Threading Notes -------------------
