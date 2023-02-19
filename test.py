def real_len(text):
   # iskl = [\n, \f, \r, \t, \v]
    return len(text)

text = 'Alex\nKdfe23\t\f\v.\r'
print(real_len(text))