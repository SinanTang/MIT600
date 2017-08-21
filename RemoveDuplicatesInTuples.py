## remove duplicates in tuple

all = (5, 15, 5, 15, 5, 15, 0, 5, 15)

# 1.
new = []
for i in all:
    if i not in new: new.append(i)

print tuple(new)

# 2. use function enumerate
print tuple([item for index, item in enumerate(all) if item not in all[:index]])

    # equals to this for loop
for i, t in enumerate(all):
    if t not in all[:i]:
        print t

# print all[:2], all[2:], all[:5] # tuple slicing gives tuples

# 3. using lambda anonymous function with reduce() function
print reduce(lambda a, b: a if b in a else a+(b,), all, ())