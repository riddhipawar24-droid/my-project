n = 3
ch = ord('a')

for i in range(n):
    print(" " * i + chr(ch) * (n - i))
    ch += 1