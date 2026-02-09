class Worker:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"Worker {self.name} is working")

class Developer(Worker):
    def work(self):
        super().work()
        print(f"Developer {self.name} writes code")

class Designer(Worker):
    def work(self):
        super().work()
        print(f"Designer {self.name} creates design")

workers = [ Developer("Alex"), Designer("Kate"), Worker("Sam") ]

for worker in workers:
    worker.work()
