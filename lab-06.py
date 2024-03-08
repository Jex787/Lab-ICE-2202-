class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")
            return None


# Example usage:
q = Queue()

# Enqueue items
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

# Peek at the front element
print("Front element:", q.peek())

# Dequeue items
print("Dequeued item:", q.dequeue())
print("Dequeued item:", q.dequeue())

# Size of the queue
print("Size of the queue:", q.size())

# Check if the queue is empty
print("Is queue empty?", q.is_empty())
