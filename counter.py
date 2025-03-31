class Counter:
    
    def __init__(self):
        self.value = 1
        
    def counter_up(self):
        self.value += 1
        
    def counter_down(self):
        self.value -= 1
        
    def __str__(self):
        return f"counter = {self.value}"
    
    def __add__(self,other):
        return self.value + other.value 

count1 = Counter()
count2 = Counter()
count3 = Counter()

count1.counter_up()
count2.counter_up()
count3.counter_up()


print(count1)
print(count2)
print(count1 + count2 + count3)


