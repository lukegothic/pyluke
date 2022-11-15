#TODO: distribucion venn para *sets
# def distribute(*sets):
#   pass

class VennSet:
  pass

class VennIntersection:
  pass

class VennDistribution:
  def __init__(self):
    self.sets = VennSet()
    self.intersections = VennIntersection()
    self.union = {}

# in: a, b, c : set
class VennSet3:
  def __init__(self, a, b, c):
    self.a = a - b - c
    self.b = b - c - a
    self.c = c - a - b

# in: a, b, c : set
class VennIntersection3:
  def __init__(self, a, b, c):
    self.ab = a & b - c
    self.bc = b & c - a
    self.ac = a & c - b

# in: a, b, c : set
class VennDistribution3(VennDistribution):
  def __init__(self, a, b, c):
    self.sets = VennSet3(a, b, c)
    self.intersections = VennIntersection3(a, b, c)
    self.union = a & b & c

# in: a, b, c, d : set
class VennSet4:
  def __init__(self, a, b, c, d):
    self.a = a - b - c - d
    self.b = b - c - d - a
    self.c = c - d - a - b
    self.d = d - a - b - c

# in: a, b, c, d : set
class VennIntersection4:
  def __init__(self, a, b, c, d):
    self.ab = a & b - c - d
    self.cd = c & d - a - b
    self.ac = a & c - b - d
    self.bd = b & d - a - c
    self.ad = a & d - c - b
    self.bc = b & c - a - d
    self.abc = a & b & c - d
    self.abd = a & b & d - c
    self.acd = a & c & d - b
    self.bcd = b & c & d - a

# in: a, b, c, d : set
class VennDistribution4(VennDistribution):
  def __init__(self, a, b, c, d):
    self.sets = VennSet4(a, b, c, d)
    self.intersections = VennIntersection4(a, b, c, d)
    self.union = a & b & c & d
