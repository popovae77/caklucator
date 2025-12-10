class Mem():
    def __init__(self):
        self.saved = None

    def mem_save(self, num):
        self.saved = float(num) if str(num).isdigit() else 0
        return None

    def mem_read(self, num=None):
        return self.saved
    
    def mem_add(self, num):
        return float(num) + (self.saved if self.saved else 0)
    
    def mem_sub(self, num):
        return float(num) - (self.saved if self.saved else 0)
    
    def mem_clear(self, num=None):
        self.saved = None
        return None