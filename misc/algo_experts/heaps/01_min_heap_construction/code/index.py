r"""TODO: port to Python.

Original JavaScript (misc/algo-experts/heaps/01-min-heap-construction/code/index.js):

class MinHeap {
    constructor() {
        this.heap = this.buildHeap(array);
    }

    buildHeap(array) {
        const firstParentIdx = Math.floor((array.length - 2) / 2);

        for (let currentIdx = firstParentIdx; currentIdx >= 0; currentIdx--) {
            this.siftDown(currentIdx, array.length - 1, array);
        }
    }

    siftDown(currentIdx, endIdx, heap) {
        let childOneIdx = currentIdx * 2 + 1;

        while (childOneIdx <= endIdx) {}
    }

    siftUp() {}

    peek() {
        return this.heap[0];
    }

    remove() {}

    insert(value) {
        this.heap.push(value);
        this.siftUp(this.heap.length - 1, this.heap);
    }

    swap(i, j, heap) {
        const temp = heap[j];

        heap[j] = heap[i];
        heap[j] = temp;
    }
}

exports.MinHeap = MinHeap;

"""
