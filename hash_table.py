from debug_decorator import debug
from collections import Counter,defaultdict
from tools import *

@debug(("a","b"),("aa","aab"))
def can_construct(ransomNote,magazine):
    rc = Counter(ransomNote)
    mc = Counter(magazine)

    for k in rc:
        if rc[k] > mc.get(k,0):
            return False
    return True

@debug(("egg", "add"), ("foo", "bar"), ("paper", "title"))
def is_isomorphic_optimized(s, t):
    # s2t 记录 s -> t 的映射，t2s 记录 t -> s 的映射
    s2t, t2s = {}, {}

    for char_s, char_t in zip(s, t):
        # 如果 s->t 冲突 或 t->s 冲突，说明不是双射
        if (char_s in s2t and s2t[char_s] != char_t) or \
           (char_t in t2s and t2s[char_t] != char_s):
            return False

        s2t[char_s] = char_t
        t2s[char_t] = char_s

    return True

@debug(("abba","dog cat cat dog"),("aaaa","dog cat cat dog"),("aaa","aa aa aa aa"))
def word_pattern(pattern,s):
    ss = s.split()
    if len(pattern) != len(ss):
        return False
    p2s,s2p = {},{}
    for char_p,word_s in zip(pattern,ss):
        if (char_p in p2s and p2s[char_p] != word_s) or \
            (word_s in s2p and s2p[word_s] != char_p):
                return False
        p2s[char_p] = word_s
        s2p[word_s] = char_p
    return True

@debug(("rat","cat"),("python","typhon"))
def is_anagram(s,t):
    return Counter(s) == Counter(t)

@debug(["eat", "tea", "tan", "ate", "nat", "bat"])
def group_anagrams(strs):
    ans = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return list(ans.values())

@debug(([2,7,11,15],9), ([3,2,4],6), ([3,3],6))
def two_sum_hash(nums, target):
    mapping = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in mapping:
            return [mapping[complement], i]
        mapping[num] = i
    return [-1, -1]

@debug(19,2,100)
def is_happy(n):
    cache = {}
    def next_num(num):
        res = 0
        while num >= 1:
            res += (num % 10)**2
            num = num // 10
        return res
    while True:
        next_n = next_num(n)
        cache[n] = next_n
        if next_n == 1:
            return True
        elif next_n in cache:
            return False

        n = next_n

@debug(([1,2,3,1],3),([1,2,3,1,2,3],2))
def contains_nearby_duplicate(nums, k):
    last_seen = {}

    for i, num in enumerate(nums):
        if num in last_seen and i - last_seen[num] <= k:
            return True
        last_seen[num] = i

    return False

@debug([100, 4, 200, 1, 3, 2], [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], exec=True)
def longest_consecutive_optimized(nums):
    if not nums: return 0

    num_set = set(nums) # 1. 去重并实现 O(1) 查找
    longest_streak = 0

    for num in num_set:
        # 2. 判断是否是序列起点
        # 如果 num-1 在集合里，说明 num 不是起点，直接跳过
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # 3. 只有是起点时，才开始向后数数
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

