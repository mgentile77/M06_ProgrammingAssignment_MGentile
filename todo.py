import multiprocessing
import time
import random

def process_task(queue, process_number):
    # Wait a random number of seconds between 0 and 1
    time.sleep(random.random())

    # Get the current time
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    # Put the process number and current time in the queue
    queue.put((process_number, current_time))

if __name__ == "__main__":
    # Create a multiprocessing Queue
    output_queue = multiprocessing.Queue()

    # Creating and starting three separate processes
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=process_task, args=(output_queue, i))
        processes.append(p)
        p.start()

    # Waiting for all processes to complete
    for p in processes:
        p.join()

    # Collecting and displaying the output
    while not output_queue.empty():
        process_number, time_output = output_queue.get()
        print(f"Process {process_number} current time: {time_output}")

