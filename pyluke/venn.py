#TODO: distribucion venn para *sets
# def distribute(*sets):
#   pass

def distribute(a, b, c, d):
  a = set(a)
  b = set(b)
  c = set(c)
  d = set(d)
  return {
    "a": list(a - b - c - d),
    "b": list(b - a - c - d),
    "c": list(c - a - b - d),
    "d": list(d - a - b - c),
    "ab": list(a & b - c - d),
    "ac": list(a & c - b - d),
    "ad": list(a & d - b - c),
    "bc": list(b & c - a - d),
    "bd": list(b & d - a - c),
    "cd": list(c & d - a - b),
    "abc": list(a & b & c - d),
    "abd": list(a & b & d - c),
    "bcd": list(b & c & d - a),
    "abcd": list(a & b & c & d)
  }

def distribute(a, b, c):
  a = set(a)
  b = set(b)
  c = set(c)
  return {
    "a": list(a - b - c),
    "b": list(b - a - c),
    "c": list(c - a - b),
    "ab": list(a & b - c),
    "ac": list(a & c - b),
    "bc": list(b & c - a),
    "abc": list(a & b & c)
  }