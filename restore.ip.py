class Solution(object):
    def restoreIpAddresses(self, s):
        result = []
        def valid(segment):
            if segment[0]=="0" and len(segment)>1:
                return False
            if int(segment)>255:
                return False
            return True
        def dfs(index,path):
            if len(path)==4 and index==len(s):
                result.append(".".join(path))
            if index==len(s):
                return
            for length in range(1,4):
                if index+length>len(s):
                    break
                segment = s[index:index+length]
                if valid(segment):
                    dfs(index+length,path+[segment])
        dfs(0,[])
        return result