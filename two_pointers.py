from debug_decorator import debug

@debug("A man, a plan, a canal: Panama","race a car","0p")
def is_palindrome(s):
    s = s.lower()
    lp,rp = 0,len(s)-1

    while lp <= rp:
        if not (ord("a") <= ord(s[lp]) <= ord("z") or ord("0") <= ord(s[lp]) <= ord("9")):
            lp += 1
            continue
        if not (ord("a") <= ord(s[rp]) <= ord("z") or ord("0") <= ord(s[rp]) <= ord("9")):
            rp -= 1
            continue
        if s[lp] != s[rp]:
            return False
        else:
            lp += 1
            rp -= 1
    return True

@debug(("abc","aaaaahjbnc"),("ac","xyz"))
def is_subsequence(s,t):
    # time O(n)
    # 如果用python 迭代器的特性，那么只需要2行
    # it = iter(t)
    # return all(c in it for c in s)
    sp,tp = 0,0
    while sp <= len(s) - 1 and tp <= len(t) - 1:
        print(sp,tp)
        if s[sp] == t[tp]:
            sp += 1
        tp += 1
    if sp == len(s):
        return True
    return False

@debug(([2,7,11,15],9),([2,3,4],6),([-1,0],-1))
def two_sum(numbers,target):
    lp,rp = 0,len(numbers) - 1
    while lp < rp:
        if numbers[lp] + numbers[rp] > target:
            rp -= 1
        elif numbers[lp] + numbers[rp] < target:
            lp += 1
        else:
            return [lp+1,rp+1]


@debug([1,8,6,2,5,4,8,3,7],[1,1],[1],[8,7,2,1])
def max_area(height):
    lp, rp = 0, len(height) - 1
    maximum = 0

    while lp < rp:
        h_left, h_right = height[lp], height[rp]
        current_height = min(h_left,h_right)
        maximum = max(maximum, current_height * (rp - lp))

        if h_left < h_right:
            while lp < rp and height[lp] <= h_left:
                lp += 1
        else:
            while lp < rp and height[rp] <= h_right:
                rp -= 1

    return maximum

@debug([-1,-1,0,1,2],[-1,0,1,2,-1,-4],exec=True)
def three_num(nums):
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n - 2):
        if nums[i] > 0:
            break

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        lp, rp = i + 1, n - 1
        while lp < rp:
            total = nums[i] + nums[lp] + nums[rp]
            if total < 0:
                lp += 1
            elif total > 0:
                rp -= 1
            else:
                res.append([nums[i], nums[lp], nums[rp]])
                while lp < rp and nums[lp] == nums[lp + 1]:
                    lp += 1
                while lp < rp and nums[rp] == nums[rp - 1]:
                    rp -= 1
                lp += 1
                rp -= 1

    return res





