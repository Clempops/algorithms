import random

def simulation(total_time_sec):
  printer = Printer()
  queue = PrinterQueue()

  for second in range(total_time_sec):
    
    if queue.new_task():
      queue.add_task()
      
    if queue.waiting_time == 0:
      queue.current_task = None
      printer.busy = False
      
    if not printer.is_busy() and len(queue.body) > 0:
      queue.send_task()
      printer.busy = True
    
    if printer.is_busy():
      queue.waiting_time -= 1
      
    if queue.waiting_time == 1: 
      print "At %s seconds: Printings in queue: %s | Total printing time: %s" % (second, len(queue.body), sum(queue.body))

# classes

class PrinterQueue:
  def __init__(self):
    self.body = []
    self.waiting_time = 0
    self.current_task = None
    
  def new_task(self):
    if random.randrange(8) == 1:
      return True
    else:
      return False
      
  def add_task(self):
    self.body.append(random.randrange(60))
    
  def remove_task(self):
    self.body.pop(0)
    
  def send_task(self):
    self.current_task = self.body[0]
    self.body.pop(0) 
    self.waiting_time = self.current_task

class Printer:
  def __init__(self):
    self.busy = False
    
  def is_busy(self):
    if self.busy == True:
      return True
    else:
      return False

print simulation(1800)

