from abc import ABC, abstractmethod

class Stationery(ABC):
    def __init__(self, title):
        self.title = title
    
    @abstractmethod
    def draw(self):
        pass

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
        print ("Drawing horse with a pen")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
        print("Solving sudoku with a pencil")
    
class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
        print("Highlight quotes with a handle")
