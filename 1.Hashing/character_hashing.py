s = "azyxyyzaaaa"
q = ["d", "a", "z", "x", "y"]

hash_dict = {}


# Method 1 - solution
"""
hash_list = [0] * 27

for ch in s:
    ascii_val = ord(ch)
    index = ascii_val - 97
    hash_list[index] += 1

for ch in q:
    ascii_val = ord(ch)
    index = ascii_val-97
    print(f"{ch} : {hash_list[index]}")
"""
# Method -2
for i in range(0, len(s)):
    hash_dict[s[i]] = hash_dict.get(s[i], 0) + 1
for i in range(0, len(q)):
    print(f"{q[i]} appears {hash_dict.get(q[i],0)}")
