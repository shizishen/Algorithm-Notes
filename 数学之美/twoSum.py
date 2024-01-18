# 解法一 排序+双指针（不符合）
def twoSum(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    nums.sort()
    l = 0
    r = len(nums) - 1
    while l < r:
        if nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] > target:
            r -= 1

        else:
            return [l, r]
    return []


# 解法二 空间换时间
def twoSum2(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    mapper = {}
    for i in range(n):
        if target-nums[i] in mapper:
            return [mapper[target-nums[i]],i]
        else:
            mapper[nums[i]] = i
    return []

def main():
    nums = [1, 23, 34, 45, 8, 7, 8]
    target = 8
    #index = twoSum(nums, target)
    index = twoSum2(nums, target)
    print(index)


if __name__ == '__main__':
    main()
