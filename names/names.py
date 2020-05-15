import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# initialize BST value as an empty string
tree = BSTNode('')

# iterate over names to build tree from list
for name in names_1:
    tree.insert(name)
# search names_2 for matches to tree(names_1) and append to duplicates list
for name_match in names_2:
    if tree.contains(name_match):
        duplicates.append(name_match)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
start_time_stretch = time.time()

duplicatesStretch = [duplicate for duplicate in(set(names_1).intersection(names_2))]
end_time_stretch = time.time()

print (f"Stretch:  {len(duplicatesStretch)} duplicates:\n\n{', '.join(duplicatesStretch)}\n\n")
print (f"Stretch runtime: {end_time_stretch - start_time_stretch} seconds")