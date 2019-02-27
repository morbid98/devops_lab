def reverse(s):
    s = s.split()
    revs = " h".join([word[::-1] for word in s])
    return revs
