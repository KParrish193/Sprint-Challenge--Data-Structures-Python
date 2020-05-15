class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.front = 0
    
    def append(self, item):
        # if queue is empty

        # if queue is full/at capacity
        if len(self.data) == self.capacity:
            self.data.pop(self.front)
            self.data.insert(self.front, item)
            self.front = (self.front + 1) % self.capacity
        else:
            self.data.append(item)
        
    def get(self): 
        return self.data


buf = RingBuffer(3)
for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
    buf.append(i)
    print(buf.get())