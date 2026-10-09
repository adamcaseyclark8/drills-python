class MinHeap:
    def __init__(self, array):
        self.heap = self.build_heap(array)

    def build_heap(self, array):
        first_parent_idx = (len(array) - 2) // 2

        for current_idx in range(first_parent_idx, -1, -1):
            self.sift_down(current_idx, len(array) - 1, array)

    def sift_down(self, current_idx, end_idx, heap):
        child_one_idx = current_idx * 2 + 1

        # unfinished: the original loop had an empty body, which never terminates
        # while child_one_idx <= end_idx:
        #     ...

    def sift_up(self, *args):
        pass

    def peek(self):
        return self.heap[0]

    def remove(self):
        pass

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        temp = heap[j]

        heap[j] = heap[i]
        heap[j] = temp
