# WITHOUT THE DUPLICATES

# class Solution(object):
# def combinationSum(self, candidates, target):
#     result = []
#     def dfs(index,path,remaining):
#         if remaining==0:
#             result.append(list(path))
#             return
#         elif remaining<0 or index==len(candidates):
#             return
#         path.append(candidates[index])
#         dfs(index,path,remaining-candidates[index])
#         path.pop()
#         dfs(index+1,path,remaining)
#     dfs(0,[],target)
#     return result

# WITH DUPLICATES

# class Solution(object):
#     def combinationSum2(self, candidates, target):
#         result = []
#         candidates.sort()
#         def dfs(index,path,remaining):
#             if remaining==0:
#                 result.append(list(path))
#                 return
#             if remaining<0 or index==len(candidates):
#                 return
#             path.append(candidates[index])
#             dfs(index+1,path,remaining-candidates[index])
#             path.pop()
#             next_index=index+1
#             for i in range(index,len(candidates)):
#                 if candidates[i]==candidates[i-1]:
#                     continue
#             dfs(index+1,path,remaining)
#         dfs(0,[],target)
#         return result
