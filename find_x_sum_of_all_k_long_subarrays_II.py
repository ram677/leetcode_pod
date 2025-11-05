#3321. Find X-Sum of All K-Long Subarrays II

from sortedcontainers import SortedList


class Solution:
  def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
    ans = []
    windowSum = 0
    count = collections.Counter()
    top = SortedList()
    bot = SortedList()

    def update(num: int, freq: int) -> None:
      nonlocal windowSum
      if count[num] > 0:  # Clean up old values.
        if [count[num], num] in bot:
          bot.remove([count[num], num])
        else:
          top.remove([count[num], num])
          windowSum -= num * count[num]
      count[num] += freq
      if count[num] > 0:
        bot.add([count[num], num])

    for i, num in enumerate(nums):
      update(num, 1)
      if i >= k:
        update(nums[i - k], -1)
      # Move the bottom element to the top if needed.
      while bot and len(top) < x:
        countB, b = bot.pop()
        top.add([countB, b])
        windowSum += b * countB
      # Swap the bottom and top elements if needed.
      while bot and bot[-1] > top[0]:
        countB, b = bot.pop()
        countT, t = top.pop(0)
        bot.add([countT, t])
        windowSum -= t * countT
        top.add([countB, b])
        windowSum += b * countB
      if i >= k - 1:
        ans.append(windowSum)

    return ans
  
# Time Complexity: O(n log k), where n is the length of nums and k is the subarray length.
# Space Complexity: O(k), for storing the frequency counts and the two sorted lists.