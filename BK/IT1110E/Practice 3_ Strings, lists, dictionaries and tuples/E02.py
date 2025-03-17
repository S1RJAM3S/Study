s = input()
print(''.join(list(map(lambda x: x.capitalize(), s.split('_')))))