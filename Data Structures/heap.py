class Heap:
    def __init__(self, items_to_be_added=None, verbose=True):
        if(items_to_be_added is None):
            items_to_be_added = []
        self.items = items_to_be_added
        self.num_items = len(self.items)
        self.verbose = verbose
        
    
    def percolate_down(self, i):
        if(self.verbose):
            self.display()
        if(i < self.num_items // 2):
            maxChild = 2*i + int(self.items[2*i+1] > self.items[2*i])
            if(self.items[i] < self.items[maxChild]):
                self.items[i], self.items[maxChild] = self.items[maxChild], self.items[i]
                self.percolate_down(maxChild)  
            
    def percolate_up(self, i):
        if(self.verbose):
            self.display()
        while(i>0 and self.items[i] > self.items[i//2]): # while larger than parent
            self.items[i//2], self.items[i] = self.items[i], self.items[i//2]
            i = i // 2
            
    def insert(self, x):
        self.items.append(x)
        self.num_items += 1
        self.percolate_up(self.num_items - 1)
    
    def peek_max(self):
        # O(1)
        return(self.items[0])

    def extract_max(self):
        res = self.peek_max()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.num_items -= 1
        self.percolate_down(0)
        return(res)
    
    def display(self):
        print()
        i = 0
        curr_level = 1
        while(i < self.num_items):
            if(i == 2**curr_level - 1):
                print()
                curr_level += 1
            print(self.items[i],end="  ")
            i += 1
        print()
