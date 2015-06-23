class Staircase:
  def __init__(self, steps):
    self.ways = 0
    self.staircase(steps)
    print self.ways
    
  def staircase(self, steps):
    if steps > 0:
      self.staircase(steps-1)
      self.staircase(steps-2)
      self.staircase(steps-3)
    elif steps == 0: self.ways += 1

compute = Staircase(3)