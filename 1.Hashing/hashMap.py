# Find the occurence of elements of m in the list n

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

l = len(n)

hashmap = {}
# for i in range(3, len(n)):
#     if n[i] in hashmap:
#         hashmap[n[i]] += 1
#     else:
#         hashmap[n[i]] = 1

# for keys, values in hashmap.items():
#     print(f"{keys} : {values}")

# for i in range(0, l):
#     hashmap[n[i]] = hashmap.get(n[i],0)+1
# print(hashmap[5])

# for keys, values in hashmap.items():
#     print(f"{keys} : {values}")

for i in range(0, l):
    hashmap[n[i]] = hashmap.get(n[i], 0) + 1

for x in range (0,len(m)):
    print(f"{m[x]} appears {hashmap.get(m[x],0)}")
