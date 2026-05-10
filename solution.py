def merge_list():
	# time:O(m+n) space:O(1)
	nums1 = [1,2,3,3,0,0,0]
	m = 4
	nums2 = [2,5,6]
	n = 3
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
	print(nums1)

		
# merge_list()

def remove_element(example,val):
	# time O(n) space O(1)
	count = 0
	length = len(example)
	index = length - 1
	while index >= 0:
		if example[index] == val:
			example[index],example[length - 1 - count] = example[length - 1 - count],example[index]
			count += 1
		index -= 1
	print(example,length - count)
	return length - count
	
	
# remove_element([0,1,2,2,3,0,4,2],2)

def remove_repeat(nums):
	# time O(n) space O(1)
	length = len(nums)
	unique_element_count = 1 # index为0 的总是独特的
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
		
	# print(nums,unique_element_count)
	return unique_element_count
	
# remove_repeat([0,1,1,1,3,4,5])

def remove_repeatk(nums):
	# time:O(n) space O(1) 
    # k 是允许重复的次数，这题是 2
    k = 2
    if len(nums) <= k:
        return len(nums)
    
    write_p = k
    
    for read_p in range(k, len(nums)):
        if nums[read_p] != nums[write_p - k]:
            nums[write_p] = nums[read_p]
            write_p += 1
    
    # print(nums)
    return write_p
	
# remove_repeatk([1,1,1,2,2,2,3,3])

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
	
def genius_major_element(nums):
	# 只适用于能确定众数大于 floor(len(nums))
	# time O(n) space O(1)
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
	
		
	
# print(major_element([3,2,3]))
# print(genius_major_element([1,1,1,2,2,2,2]))

	
# 7,1,5,3,6,4
# 0,-6,4,-2,3,-2
def max_profit(prices):
	# time O(n) space O(1)
	if not prices:
		return 0
	length = len(prices)
	min_price = float('inf')
	max_pro = - min_price
	for price in prices:
		if price < min_price:
			min_price = price
		elif price - min_price > max_pro:
			max_pro = price - min_price
	return max_pro

# print(max_profit([7,1,5,3,6,4]))

def max_profit2(prices):
	# time O(n) space O(1) 
	if not prices:
		return 0
	length = len(prices)
	profit = 0
	for i in range(1,length):
		if prices[i] > prices[i-1]:
			profit += prices[i] - prices[i-1]
	return profit

# print(max_profit2([7,1,5,3,6,4]))

def can_jump(nums):
	# time O(n) space O(1)
	max_reach = 0
	for index,leap in enumerate(nums):
		if index > max_reach:
			return False
	
		max_reach = max(max_reach,index + leap)
	
	if max_reach >= len(nums)-1:
		return True
	
	return False
	
# print(can_jump([0]))

def jump(nums):
	# time O(n) SPACE O(n)
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
	
	
# print(jump_to([2,3,1,1,4]))

def h_index(citations):
	# time O(n) space O(n)
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

# print(h_index([2,2,2,2,2,2,2,2,2]))

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
		
# r = RandomizedSet()
# r.insert(5)
# print(r.getRandom())

def product_except_self(nums):
    length = len(nums)
    res = [1] * length
    
    # 1. 顺着扫：res[i] 存储 i 左边所有数的积
    # res[0] 默认就是 1（左边没东西）
    for i in range(1, length):
        res[i] = res[i-1] * nums[i-1]
        
    # 2. 倒着扫：用一个变量 right 动态维护右边的积
    right = 1
    for i in range(length - 1, -1, -1):
        # 现在的 res[i] 是左积，乘上此时的右积就是答案
        res[i] = res[i] * right
        # 更新右积，给左边那个位置用
        right *= nums[i]
        
    return res
# 	
# print(product_except_self([1,2,3,4]))

# gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# minus = [-2,-2,-2,3,3]

# gas = [2,3,4], cost = [3,4,3]
# minus = [-1,-1,1]

# minus = [-1,7,-1,8,-9,3]
def can_complete_circuit(gas, cost):
    # 如果总油量还没总消耗多，直接放弃，不可能跑完
    if sum(gas) < sum(cost):
        return -1
    
    total_tank = 0  # 当前油箱里的油
    start_station = 0
    
    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        
        # 如果油箱见底了
        if total_tank < 0:
            # 贪心：前面的站都不行，从下一站重新开始
            start_station = i + 1
            total_tank = 0
            
    return start_station

# print(can_complete_circuit([1,2,3,4,5],[3,4,5,1,2]))

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
			
	
# print(candy([1,3,2,2,1]))
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
			
	
		
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
			
	
	
			
		
	

