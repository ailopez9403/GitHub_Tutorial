print("Hello, world 2 (edit from VS)")

def median(input):
  length = len(input)

  if length % 2 == 1:
    median = input[math.floor(length / 2)]
  else:
    middle1 = input[math.floor(length / 2)]
    middle2 = input[(math.floor(length / 2)) - 1]
    median = (middle1 + middle2) / 2
  return median