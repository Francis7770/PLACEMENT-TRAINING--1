class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []
        res = ''
        num = 0
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            
            elif i == '[':
                st.append((res,num))
                res, num = '', 0

            elif i == ']':
                prev_res, k = st.pop()
                res = prev_res + res * k
            
            else:
                res += i

        return res
