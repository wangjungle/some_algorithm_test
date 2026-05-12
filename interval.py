from debug_decorator import debug
from collections import deque
from tools import *

@debug([0,1,2,4,5,7],[0,2,3,4,6,8,9],[])
def summary_ranges(nums):
    if not nums:
        return []
    res = []
    length = len(nums)
    nums.append(nums[-1])
    index = 0
    while index < length:
        start_index = index
        while index < length and nums[index + 1] - nums[index] <= 1:
            index += 1
        if nums[index] == nums[start_index]:
            res.append(str(nums[index]))
        else:
            res.append(f"{nums[start_index]}->{nums[index]}")
        index += 1
    return res

@debug([[1,3],[2,6],[8,10],[15,18]],[[1,4],[4,5]],[[4,7],[1,4]],[[1,4],[2,3]])
def merge(intervals):
    if not intervals: return []

    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


@debug()
def insert(intervals, newInterval):
    res = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    res.append(newInterval)

    while i < n:
        res.append(intervals[i])
        i += 1

    return res

@debug([[10,16],[2,8],[1,6],[7,12]], [[1,2],[3,4]], exec=True)
def find_min_arrow_shots(points):
    if not points: return 0

    # 1. 核心关键：按右边界排序
    points.sort(key=lambda x: x[1])

    arrows = 1
    current_arrow_pos = points[0][1] # 第一支箭射在第一个气球的右端点

    for i in range(1, len(points)):
        # 2. 如果下一个气球的左端点大于当前箭的位置，说明射不到
        if points[i][0] > current_arrow_pos:
            arrows += 1
            current_arrow_pos = points[i][1] # 更新箭的位置到新气球的右端点

    return arrows




