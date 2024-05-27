nums = list(map(int, input().split()))
res = [n for n in nums if (n != min(nums) and n != max(nums)) or nums.count(n) > 1]
print(res[0])