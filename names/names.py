import time
from BST import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Return the list of duplicates in this data structure
duplicates = []
bst = BSTNode("")


def printEach(node):
    print(f"{node},")

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


for name in names_1:
    bst.insert(name)

for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{bst.for_each(printEach)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
start_time_s = time.time()
stretch_names = set()
dupes = set()
for name in names_1:
    stretch_names.add(name)
for names in names_2:
    if name in stretch_names:
        dupes.add(name)

print(f"{len(dupes)} duplicates:\n\n{', '.join(duplicates)}\n\n")
end_time_s = time.time()
print(f"runtime: {end_time_s - start_time_s} seconds")
