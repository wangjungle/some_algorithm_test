def bsearch(nums, target, condition=lambda val, tgt: val >= tgt):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if condition(nums[mid], target):
            r = mid - 1
        else:
            l = mid + 1

    return l
