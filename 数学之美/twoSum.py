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
    mapper = {}  # 创建一个空字典，用于存储每个数字及其索引
    '''
    字典用法
    mapper = {}
    mapper['key1'] = 'value1'  # 添加键值对
    '''

    for i in range(n):
        if target - nums[i] in mapper:
            # 如果目标值减去当前数字的差在字典中存在，说明找到了两个数之和等于目标值
            # 返回这两个数的索引
            return [mapper[target - nums[i]], i]
        else:
            # 否则将当前数字及其索引添加到字典中
            mapper[nums[i]] = i
    # 如果无法找到满足条件的两个数，返回一个空列表
    return []

def main():
    nums = [1, 23, 34, 45, 8, 7, 8]
    target = 8
    #index = twoSum(nums, target)
    index = twoSum2(nums, target)
    print(index)


if __name__ == '__main__':
    main()
