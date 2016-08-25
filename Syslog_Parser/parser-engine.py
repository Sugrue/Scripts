from config import *
from parsers.log_parser import *

import threading
import time


class parser():
    def __init__(self, parser_threads, comm_threads):
        self.parser_threads = parser_threads
        self.comm_threads = comm_threads
        self.queue = []
        self.parsed_logs = []
        self.main_loop()

    def main_loop(self):
        threads = []
        logs = []


        for log_file in LOG_FILES:
            logs.append(open(log_file, mode='r'))

        for i in range(self.parser_threads):
            threads.append(threading.Thread(target=self.parser, args=[]))
            threads[-1].start()

        for i in range(self.comm_threads):
            threads.append(threading.Thread(target=self.communicate_stats, args=[]))
            threads[-1].start()

        while True:
            for log_file in logs:
                line = log_file.readline()
                if line:
                    self.queue.append(line)



    def parser(self):
        while True:
            if len(self.queue) > 0:
                self.parsed_logs.append(log_parser(self.queue.pop(), VENDOR_MERAKI).get_parsed())

    def communicate_stats(self, facility=None):
        while True:
            if len(self.parsed_logs) > 0:
                item = self.parsed_logs.pop()
                if item['type'] == 'events':
                    print(item)


parser(4, 2)


