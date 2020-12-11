
# string longestPalindrome(string s) {
#     string res;
#     for (int i = 0; i < s.size(); i++) {
#         // 寻找长度为基数的回文子串
#         string s1 = palindrome(s, i, i);
#         // 寻找长度为偶数的回文子串
#         string s2 = palindrome(s, i, i + 1);
#         // res = longest(res, s1, s2)
#         res = res.size() > s1.size() ? res : s1;
#         res = res.size() > s2.size() ? res : s2;
#     }
#     return res;
# }

# // 从 s[l] 和 s[r] 开始向两端扩散
# // 返回以 s[l] 和 s[r] 为中心的最长回文串
# string palindrome(string& s, int l, int r) {
#     // 防止索引越界
#     while (l >= 0 && r < s.size() && s[l] == s[r]) {
#         l--; r++;
#     }
#     return s.substr(l + 1, r - l - 1);
# }

def longestPalindrome(s:str):
    res = str()
    for i  in range(len(s)):
        # // 寻找长度为基数的回文子串
        s1 = palindrome(s, i, i)
        # // 寻找长度为偶数的回文子串
        s2 = palindrome(s, i, i + 1)
        res =  res if len(res) >= len(s1) else s1
        res = res if len(res) >= len(s2)  else s2
    
    return res

def palindrome(s:str, l:int, r:int):
    # // 防止索引越界
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l-=1
        r+=1
    return s[l + 1: r]



# "babad" --> "bab","aba"
# "cbbd" --> "bb"

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))