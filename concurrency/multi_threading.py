from typing import List

import threading
import timeit

def process_chunk(chunk: List[int]) -> int:
    mto5 = 0
    for n in chunk:
        if n % 5 == 0:
            mto5 += 1

    return mto5

class MultiThreading():
    def __init__(self, data_set: List[int]):
        self.chunk_size = len(data_set) // 4
        self.chunks = [data_set[i:i + self.chunk_size] for i in range(0, len(data_set), self.chunk_size)]
        
        self.threads: List[threading.Thread] = []
        self.lock = threading.Lock()
        self.mto5 = 0

    def _process_chunk(self, chunk: List[int]):
        for n in chunk:
            if n % 5 != 0:
                continue

            with self.lock:
                self.mto5 += 1

    def count(self) -> int:
        for chunk in self.chunks:
            thread = threading.Thread(target=self._process_chunk, args=(chunk,))
            self.threads.append(thread)
            thread.start()

        for thread in self.threads:
            thread.join()

        mto5 = self.mto5
        self.mto5 = 0
        return mto5

result = None
def count_multiple_of_5(multi_threading: bool, list: List[int]):
    global result

    if multi_threading:
        result = MultiThreading(list).count()
    else:
        result = process_chunk(list)

if __name__ == "__main__":
    list = list(range(1, int(1e6) + 1))

    time_execution_1 = timeit.timeit(lambda: count_multiple_of_5(False, list), number=100)
    average_time_1 = (time_execution_1 / 1000) * 1000
    print(f"mono thread: {average_time_1} ms")
    print(f"There is {result} multiple of 5 in this data set")

    time_execution_2 = timeit.timeit(lambda: count_multiple_of_5(True, list), number=100)
    average_time_2 = (time_execution_2 / 1000) * 1000
    print(f"multi thread: {average_time_2} ms")
    print(f"There is {result} multiple of 5 in this data set")
