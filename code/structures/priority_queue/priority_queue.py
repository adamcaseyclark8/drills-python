from code.structures.priority_queue.queue import Queue


class PriorityQueue(Queue):
    def enqueue(self, value, priority):
        new_item = {'value': value, 'priority': priority}

        if self.is_empty():
            self.items.append(new_item)
        else:
            inserted = False
            for i in range(len(self.items)):
                if priority < self.items[i]['priority']:
                    self.items.insert(i, new_item)
                    inserted = True
                    break
            if not inserted:
                self.items.append(new_item)

    def dequeue(self):
        item = super().dequeue()
        return item['value'] if item else None

    def peek(self):
        item = super().peek()
        return item['value'] if item else None

    def to_array(self):
        return [item['value'] for item in self.items]
