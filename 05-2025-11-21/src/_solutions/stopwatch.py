class StopWatch():
    def __init__(self, seconds):
        
        self.time = seconds
        
    def measure_time(self):
        import time
        
        for i in range(self.time + 1):
            print(i)
            time.sleep(1)