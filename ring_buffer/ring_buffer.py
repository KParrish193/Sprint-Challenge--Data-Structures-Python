class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.current = 0
    
    def append(self, item):

        # if queue is full/at capacity
        if len(self.data) == self.capacity:
            self.data.pop(self.current)
            self.data.insert(self.current, item)
            self.current = (self.current + 1) % self.capacity
        else:
            self.data.append(item)
        
    def get(self): 
        return self.data


buf = RingBuffer(5)
for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']:
    buf.append(i)
    print(buf.get())