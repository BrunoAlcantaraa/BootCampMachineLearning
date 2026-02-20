cond1 = True
cond2 = False
cond3 = True

print(cond1 and cond2 and cond3)
print(cond1 or cond2 or cond3)
print(cond1 != cond2) # xor ^
print(not cond1)
print(not cond2)

print(cond1 and not cond2)

x = 3
y = 4

print(cond1 and not cond2 and x < y)