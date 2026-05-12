
from debug_decorator import debug
from collections import Counter

@debug(
    ("barfoothefoobarman", ["foo", "bar"]),
    ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]),
    ("barfoobarthefoobarman", ["bar", "foo", "the"])
)
def find_substring(s, words):
    if not s or not words:
        return []
    
    word_len = len(words[0])
    word_num = len(words)
    total_len = word_len * word_num
    words_count = Counter(words)
    res = []

    for i in range(word_len):
        left = i
        right = i
        current_count = Counter()
        count = 0
        
        while right + word_len <= len(s):
            w = s[right : right + word_len]
            right += word_len
            
            if w in words_count:
                current_count[w] += 1
                count += 1

                while current_count[w] > words_count[w]:
                    left_w = s[left : left + word_len]
                    current_count[left_w] -= 1
                    count -= 1
                    left += word_len
                
                if count == word_num:
                    res.append(left)
            else:
                current_count.clear()
                count = 0
                left = right
                
    return res

@debug(("ADOBECODEBANC","ABC"),exec=True)
def min_window(s, t):
    if not s or not t:
        return ""

    target_count = Counter(t)
    window_count = {}
    
    lp = 0
    valid_chars = 0
    required_chars = len(target_count)
    
    res_l, res_len = 0, float('inf')

    for rp in range(len(s)):
        char = s[rp]
        if char in target_count:
            window_count[char] = window_count.get(char, 0) + 1
            if window_count[char] == target_count[char]:
                valid_chars += 1
        
        while valid_chars == required_chars:
            if rp - lp + 1 < res_len:
                res_len = rp - lp + 1
                res_l = lp
            
            left_char = s[lp]
            if left_char in target_count:
                if window_count[left_char] == target_count[left_char]:
                    valid_chars -= 1
                window_count[left_char] -= 1
            
            lp += 1
            
    return "" if res_len == float('inf') else s[res_l : res_l + res_len]
            