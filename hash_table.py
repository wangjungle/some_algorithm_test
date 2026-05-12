from debug_decorator import debug
from collections import Counter

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

@debug(["eat", "tea", "tan", "ate", "nat", "bat"],exec=True)
def group_anagrams(strs):
    ans = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return list(ans.values())
