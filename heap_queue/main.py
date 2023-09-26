from typing import List
import warnings

class HeapQueue:
    def __init__(self):
        self.heap = []

    def push(self, value: any) -> None:
        self.heap.append(value)
        self._heap_up(len(self.heap) - 1)
    
    def pop(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heap_down(0)
        return root

    def _heap_up(self, index: int) -> None:
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] >= self.heap[parent_index]:
                break

            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index

    def _heap_down(self, index: int) -> None:
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if (left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]):
                smallest = left_child_index

            if (right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]):
                smallest = right_child_index

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

def find_largest_values(list_of_numbers: List[int], size: int) -> List[int]:
    if len(list_of_numbers) < size:
        warnings.warn(f"The list provided has a smaller size than {size}, skipped..", category=UserWarning)
        return []
    
    queue = HeapQueue()

    for n in list_of_numbers:
        if len(queue.heap) < size:
            queue.push(n)
        elif n > queue.heap[0]:
            queue.pop()
            queue.push(n)

    largest_three = []
    while queue.heap:
        largest_three.append(queue.pop())

    return largest_three[::-1]
