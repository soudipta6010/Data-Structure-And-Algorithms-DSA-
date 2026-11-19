# LeetCode - 2220. Minimum Bit Flips to Convert Number

def minBitFlips(start: int, goal: int) -> int:
    ans = start ^ goal
    count = 0
    for i in range(0, 32):
        if ans & (1 << i) != 0:
            count += 1
    return count


start = 10
goal = 7

result = minBitFlips(start, goal)
print(f"Min flips required to change {start} to {goal} is: {result}")
