import threading
from structured_logging.command_queue.command import Command
import queue
import time


class Queue:
    # TODO: we also need to inject the async delay time into the constructor
    def __init__(self, async_delay_seconds: int): #set the async delay and start backround processes.
        self.__thread = threading.Thread(target=self.__process)
        self.__thread.daemon = True
        self.__thread.start()
        self.__async_delay_seconds = async_delay_seconds
        self.__queue = queue.Queue()
        self.__running = True



    def add(self, command: Command):
        self.__queue.put(command)

    def __process(self):
        while self.__running:
            try:
                #keep on processing commands
                command = self.__queue.get(timeout=self.__async_delay_seconds)
                command.execute()
            except queue.Empty:
                  #if its empty it waits then retries
                  time.sleep(self.__async_delay_seconds)
