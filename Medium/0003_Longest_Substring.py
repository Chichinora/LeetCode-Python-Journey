#時間複雜度O(n):
class Solution:
     def lengthOfLongestSubstring(self, s: str) -> int:
        left=0 #有效字串起點
        right=0 #目前讀到的字元
        last_seen={} #每個字元上次出現的位置
        temp=0
        count=0

        for right, char in enumerate(s):
            #若讀到重覆
            if char in last_seen and last_seen[char]>=left:
                left = last_seen[char]+1
            # 下一步：更新 char 最新出現的位置
            last_seen[char]=right
            # 下一步：計算目前視窗長度
            temp=right-left+1
            # 下一步：更新 count
            if temp>=count:
                count=temp
        # 最後回傳答案
        return count

#時間複雜度O(n^2):
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         temp = ""
#         count = 0

#         for char in s:
#             if char not in temp:
#                 temp += char
#             else:
#                 # 1. 記錄目前 temp 的長度
#                 if len(temp)>count:
#                     count = len(temp)
#                 # 2. 找出重複字元的位置
#                 position = temp.index(char)
#                 # 3. 使用切片更新 temp
#                 temp=temp[position+1:]
#                 # 4. 加入目前的 char
#                 temp+=char

#         # 5. 回傳count
#         return count
