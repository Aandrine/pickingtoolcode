
s = lambda q: ["".join(ch for ch in q if not ch.isdigit())]

print(s("h5ih5g5"))

mylist = [1,2,3,4,5,6,7]
b = [2,7]

res = list(filter(lambda x: x in mylist, b))

print(res)