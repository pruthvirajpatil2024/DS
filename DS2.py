class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow! Cannot insert", value)
        elif self.front == -1:  # first element
            self.front = self.rear = 0
            self.queue[self.rear] = value
            print(value, "enqueued")
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            print(value, "enqueued")

    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow! No element to delete")
        elif self.front == self.rear:  # single element
            print("Dequeued:", self.queue[self.front])
            self.front = self.rear = -1
        else:
            print("Dequeued:", self.queue[self.front])
            self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Queue elements are:", end=" ")
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()


# Driver code
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.display()

cq.dequeue()
cq.display()

cq.enqueue(50)
cq.enqueue(60)  # shows overflow
cq.display()
