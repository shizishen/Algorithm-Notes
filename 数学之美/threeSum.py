def threeSum(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    nums.sort()
    res = []
    # 要找到3个数字，因此只需要找到 倒数n-3个数即可
    for i in range(n - 2):
        # 去重, 如果当前元素与前一个元素相同，则跳过
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # 初始化左右指针，l 从 i 的下一个开始，r 从数组末尾开始
        l = i + 1
        r = n - 1
        while l < r:
            # 三数之和小于零，需要增大总和，因此将左指针向右移动（l += 1）
            if (nums[i] + nums[l] + nums[r] < 0):
                l += 1
            elif (nums[i] + nums[l] + nums[r] > 0):
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                # 去重 在左指针右侧，如果存在连续相同的数字，左指针继续向右移动，以避免重复的三元组。
                while (l < r and nums[l] == nums[l + 1]):
                    l += 1
                # 在右指针左侧，如果存在连续相同的数字，右指针继续向左移动，同样是为了避免重复的三元组。
                while (l < r and nums[r] == nums[r - 1]):
                    r -= 1
                l += 1
                r -= 1
    return res


def main():
    nums = [1, 2, 34, 0, -2, -1, 8]
    num = threeSum(nums)
    print(num)


if __name__ == '__main__':
    main()
