# *
# **
# ***
# ****
# ...
# ********

f = [1, 2, 3]
f2 = {"hello": "world", "HELLO": "WORLD"}

print(f)
print(f2)

print(f[0])
print(f2["hello"])

for e in f:
    print(e)
print("finished")

for e in range(5):
    print(e)

# for e in f:
# print("*")

max_length = 10000

line_data = 0

for count in range(max_length):
    line_data += 1
    print(line_data)
    print((count+1)*(count + 1))
print("finished")
