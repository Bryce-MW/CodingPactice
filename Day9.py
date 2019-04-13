"""
Prompt:
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

For this one, I will not use Python's built in scheduling but my own based around a queue that is sorted by how long
until calling should occur.
"""
__author__ = "Bryce Wilson"
#  Copyright (c) Bryce Wilson 2019.
#  This program is probably useless so no warranty is given, even the implied warranty of being
#  suitable for any specific use as no specific use is suggested.
#  This program is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike
#   4.0 International (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/


from typing import List, Tuple, Callable
from datetime import datetime, timedelta
import threading
from threading import Thread
from time import sleep

jobs: List[Tuple[datetime, Callable[[], None]]] = []
schedule_lock: threading.Condition = threading.Condition()


def schedule(function: Callable[[], None], offset: timedelta) -> None:
    """
    Schedule a function to be run in the future.
    :param function: The function to schedule
    :param offset: the tim until the function should be run
    :return: None
    """
    with schedule_lock:
        true_time = datetime.now() + offset
        if jobs:
            for i, job in enumerate(jobs):
                if job[0] <= true_time:
                    jobs.insert(i, (true_time, function))
                    schedule_lock.notify()
                    break
        else:
            jobs.append((true_time, function))
            schedule_lock.notify()


def do_jobs() -> None:
    """
    Function to be run  by the scheduler thread to do jobs
    :return: None
    """
    while threading.main_thread().is_alive():
        if jobs:
            if jobs[0][0] <= datetime.now():
                jobs.pop(0)[1]()
            else:
                sleep((jobs[0][0]-datetime.now()).seconds)
        else:
            with schedule_lock:
                schedule_lock.wait()


scheduler = Thread(target=do_jobs)
scheduler.daemon = True
scheduler.start()
if __name__ == "__main__":
    schedule(lambda: print("Hello, World!"), timedelta(seconds=5))
    sleep(10)
