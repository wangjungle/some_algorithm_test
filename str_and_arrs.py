from debug_decorator import debug

@debug(([1,2,3,3,0,0,0], 4, [2,5,6], 3), exec=True)
def merge_list(nums1, m, nums2, n):
	p1,p2,pAll = m-1,n-1,m+n-1
	while p1 >= 0 and p2 >= 0:
		if nums1[p1] > nums2[p2]:
			nums1[pAll] = nums1[p1]
			p1 -= 1
		else:
			nums1[pAll] = nums2[p2]
			p2 -= 1
		pAll -= 1
	while p1 >= 0:
		nums1[pAll] = nums1[p1]
		p1 -= 1
		pAll -= 1
	while p2 >= 0:
		nums1[pAll] = nums2[p2]
		p2 -= 1
		pAll -= 1
	return nums1


@debug(([0,1,2,2,3,0,4,2], 2), exec=True)
def remove_element(example,val):
	count = 0
	length = len(example)
	index = length - 1
	while index >= 0:
		if example[index] == val:
			example[index],example[length - 1 - count] = example[length - 1 - count],example[index]
			count += 1
		index -= 1
	return length - count


@debug([0,1,1,1,3,4,5], exec=True)
def remove_repeat(nums):
	length = len(nums)
	unique_element_count = 1
	unique_element_p = 0
	index = 1
	temp = nums[0]
	while index < length:
		if nums[index] != temp:
			unique_element_count += 1
			unique_element_p += 1
			temp = nums[index]
			nums[unique_element_p] = nums[index]
		index += 1
	return unique_element_count


@debug([1,1,1,2,2,2,3,3], exec=True)
def remove_repeatk(nums):
    k = 2
    if len(nums) <= k:
        return len(nums)
    
    write_p = k
    
    for read_p in range(k, len(nums)):
        if nums[read_p] != nums[write_p - k]:
            nums[write_p] = nums[read_p]
            write_p += 1
    
    return write_p


@debug([3,2,3], exec=True)
def major_element(nums):
	res = {}
	maximum = 0
	major_ele = None
	for ele in nums:
		if res.get(ele):
			res[ele] += 1
		else:
			res[ele] = 1
		if res[ele] > maximum:
			maximum = res[ele]
			major_ele = ele
	return major_ele

@debug([1,1,1,2,2,2,2], exec=True)
def genius_major_element(nums):
	candidate = None
	count = 0
	for num in nums:
		if count == 0:
			candidate = num
		else:
			count += (1 if num == candidate else -1)
	return candidate


def roll_sequence(nums,k):
	if not nums:
		return
	length = len(nums)


@debug([7,1,5,3,6,4], exec=True)
def max_profit(prices):
	if not prices:
		return 0
	min_price = float('inf')
	max_pro = - min_price
	for price in prices:
		if price < min_price:
			min_price = price
		elif price - min_price > max_pro:
			max_pro = price - min_price
	return max_pro

@debug([7,1,5,3,6,4], exec=True)
def max_profit2(prices):
	if not prices:
		return 0
	profit = 0
	for i in range(1, len(prices)):
		if prices[i] > prices[i-1]:
			profit += prices[i] - prices[i-1]
	return profit

@debug([0], exec=True)
def can_jump(nums):
	max_reach = 0
	for index,leap in enumerate(nums):
		if index > max_reach:
			return False
	
		max_reach = max(max_reach,index + leap)
	
	if max_reach >= len(nums)-1:
		return True
	
	return False

@debug([2,3,1,1,4], exec=True)
def jump(nums):
    if len(nums) <= 1:
        return 0
    
    steps = 0      
    end = 0       
    max_reach = 0  

    for i in range(len(nums) - 1):
        max_reach = max(max_reach, i + nums[i])

        if i == end:
            steps += 1   
            end = max_reach
            
            if end >= len(nums) - 1:
                break
                
    return steps


@debug([2,2,2,2,2,2,2,2,2], exec=True)
def h_index(citations):
	length = len(citations)
	buckets = [0 for _ in range(length+1)]

	for c in citations:
		if c >= length:
			buckets[length] += 1
		else:
			buckets[c] += 1
	
	total_papers = 0
	for h in range(length,-1,-1):
		total_papers += buckets[h]
		if total_papers >= h:
			return h


class RandomizedSet:
	def __init__(self):
		self.data = {}
	
	def insert(self,val):
		if not self.data.get(val):
			self.data[val] = 1
			return True
		return False
	
	def remove(self,val):
		if self.data.get(val):
			del self.data[val]
			return True
		return False
	
	def getRandom(self):
		import random
		return random.choice(list(self.data.keys()))


@debug([1,2,3,4], exec=True)
def product_except_self(nums):
    length = len(nums)
    res = [1] * length
    
    for i in range(1, length):
        res[i] = res[i-1] * nums[i-1]
        
    right = 1
    for i in range(length - 1, -1, -1):
        res[i] = res[i] * right
        right *= nums[i]
        
    return res


@debug(([1,2,3,4,5], [3,4,5,1,2]), exec=True)
def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    
    total_tank = 0
    start_station = 0
    
    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        
        if total_tank < 0:
            start_station = i + 1
            total_tank = 0
            
    return start_station

@debug([1,3,2,2,1], exec=True)
def candy(ratings):
    n = len(ratings)
    candies = [1] * n
    
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
            
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
            
    return sum(candies)

@debug([0,1,0,2,1,0,1,3,2,1,2,1], exec=True)
def trap(height):
	l_max,r_max = 0,0
	l,r = 0,len(height) - 1
	res = 0
	
	while l < r:
		if height[l] < height[r]:
			if height[l] >= l_max:
				l_max = height[l]
			else:
				res += l_max - height[l]
			l += 1
		else:
			if height[r] > r_max:
				r_max = height[r]
			else:
				res += r_max - height[r]
			r -= 1
	return res

@debug("MCMXCIV", exec=True)
def roman_to_int_optimized(s):
    tables = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    n = len(s)
    
    for i in range(n):
        value = tables[s[i]]
        if i < n - 1 and value < tables[s[i+1]]:
            res -= value
        else:
            res += value
    return res

@debug(10, exec=True)
def int_to_roman_optimized(num):
    value_symbols = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    res = []
    for value, symbol in value_symbols:
        while num >= value:
            num -= value
            res.append(symbol)
            
    return "".join(res)

@debug("Hello World","fly me to the moon    ")
def length_of_last_word(s):
	count = 0
	start_flag = False
	for i in range(len(s)-1,-1,-1):
		if not (((ord(s[i])) <= 122 and ord(s[i]) >= 97) or (ord(s[i]) >= 65 and ord(s[i]) <= 90)):
			if start_flag:
				break
			else:
				continue
			
		start_flag = True
		count += 1
	return count

@debug(["flower","flow","flight"],["dog","racecar","car"],["a"])
def max_common_prefix(strs):
	if not strs: return ""
	res = ""
	for chars in zip(*strs):
		if len(set(chars)) == 1:
			res += chars[0]
		else:
			break
	return res

@debug("Hello World","   the sky is blue   ","a good   example")
def reverse_words(s):
	s = s.lstrip(" ")
	s = s.rstrip(" ")
	l = s.split()
	l.reverse()
	return " ".join(l)

@debug(
		("PAYPALISHIRING",3),
		("PAYPALISHIRING",4),
		("A",1),
		("ABC",1),
		("ABCDEF",2),

)
def convert(s,numRows):
	if numRows == 1:
		return s
	rows = ["" for _ in range(numRows)]
	curr_row = 0
	going_down = False
	for c in s:
		rows[curr_row] += c
		if curr_row == numRows - 1 or curr_row == 0:
			going_down = not going_down
		
		curr_row += 1 if going_down else -1

	return "".join(rows)



@debug(("sadbutsad", "sad"), ("leetcode", "leeto"))
def strStr_kmp(haystack: str, needle: str) -> int:
    if not needle: return 0
    n, m = len(haystack), len(needle)
    
    nxt = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and needle[i] != needle[j]:
            j = nxt[j - 1]
        if needle[i] == needle[j]:
            j += 1
        nxt[i] = j
        
    j = 0
    for i in range(n):
        while j > 0 and haystack[i] != needle[j]:
            j = nxt[j - 1]
        if haystack[i] == needle[j]:
            j += 1
        if j == m:
            return i - m + 1
            
    return -1

@debug(
    (["This", "is", "an", "example", "of", "text", "justification."], 16),
    (["What","must","be","acknowledgment","shall","be"], 16),
    (["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20),
    exec=True
)
def full_justify(words, maxWidth):
    res = []
    cur_line = []
    cur_len = 0 

    for w in words:
        if cur_len + len(w) + len(cur_line) > maxWidth:
            for i in range(maxWidth - cur_len):
                cur_line[i % (len(cur_line) - 1 or 1)] += ' '
            res.append("".join(cur_line))
            cur_line, cur_len = [], 0
        
        cur_line.append(w)
        cur_len += len(w)

    last_line = " ".join(cur_line).ljust(maxWidth)
    res.append(last_line)
    
    return res


