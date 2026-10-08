class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #      return False
        # s_list = list(s)
        # t_list = list(t)
        # result = []
        # for s_val in s_list:
        #     count_s_val = s_list.count(s_val)

        #     if s_val not in t_list:
        #         return False

        #     count_t_val = t_list.count(s_val)

        #     if count_s_val != count_t_val:
        #         return False
            
        #     result.append(True)
        
        # if len(result) == len(s_list) == len(t_list):
        #     return True
        
        # return False
        if len(s) != len(t):
            return False
        if ''.join(sorted(s)) == ''.join(sorted(t)):
            return True
        return False


