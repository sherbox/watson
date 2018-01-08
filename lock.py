f = open('/path/to/file')
text = f.read()
f.close()
lines = text.split("\n")
def rc(row,col):
  r=lines[row-1]
  c=r[col-1]
  print(c)
