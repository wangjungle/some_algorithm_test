def bsearch(nums,target,length=-1):
    if length == -1:
        length = len(nums)
    l,r = 0,length-1
    while l <= r:
        mid = (l+r) // 2
        if nums[mid] >= target:
            r = mid-1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
    return -1

