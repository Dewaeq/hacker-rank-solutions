s = input()
full_name = s.split(' ')
print(' '.join((word.capitalize() for word in full_name)))
