test = "abcde"

# test = ''.join(format(ord(x), 'b') for x in test)
print (test[::2] + "\n" + test[1::2])


