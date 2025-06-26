# Time Complexity :
- O(n + k), where n is the length of nums and k is the max value in nums

# Space Complexity :
- O(k), where k is the range of values in nums used for points array

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_num = max(nums)
        points = [0] * (max_num + 1)

        for num in nums:
            points[num] += num

        take, skip = 0, 0

        for i in range(len(points)):
            take_i = skip + points[i]
            skip_i = max(skip, take)
            take, skip = take_i, skip_i

        return max(take, skip)

