class DynamicArray:
    
    def __init__(self, capacity: int):
        self.length = 0
        self.capacity = capacity
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        
        
        self.arr[self.length] = n
        self.length += 1 

    def popback(self) -> int:
        self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        new_capacity = 2 * self.capacity
        new_arr = [0] * new_capacity
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr 
        self.capacity = new_capacity
    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
