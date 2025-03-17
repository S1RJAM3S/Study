def mirror(s):
  s = s[-1::-1]
  result = ""
  for char in s:
      if (char == 'b'): result += 'd'
      elif (char == 'd'): result += 'b'
      elif (char == 'p'): result += 'q'
      elif (char == 'q'): result += 'p'
      elif (char in ['i', 'o', 'v', 'w', 'x']): result += char
      else: return "NOT POSSIBLE"
  return result