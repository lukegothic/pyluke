# in: multiple arrags
# out: last item from last array or None if no items in any lists
def pop_AnyOrNone(*args):
  for a in reversed(args):
    if len(a) > 0:
      return a.pop()
  return None