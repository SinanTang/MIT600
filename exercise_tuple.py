# # tuple packing
# t = 123, 456, "sinan!"
# # sequence unpacking
# x, y, z = t
# print t, z

# #tuples may be nested
# u = t, (7,8,9)
# print u


# empty = ()
# singleton = "Hello",
# len(empty)
# len(singleton)
# print singleton, empty
# print singleton[0]

# tuples: immutable, contain a heterogeneous sequence of elements, accessed via unpacking & indexing
# lists: mutable, homogeneous elements, accessed via iterating

t2 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print t2[2:9:2] # slice of t2 from 2 to 9 with step 2
print t2.index(4)
print t2[1:9].index(4)

l = ["a","b","c","d","e","f","g","h","i","j","k"]
print l[2:9:2]
print l.index("f")
print l.index("f"[,2[,8]]) # not working