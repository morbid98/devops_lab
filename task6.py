s = input("Input something cool!")
s = s.split()
revs = " ".join([word[::-1] for word in s])
print(revs)
