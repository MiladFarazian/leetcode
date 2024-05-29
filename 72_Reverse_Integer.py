class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        print(x)
        x_str = str(x)
        reverse = ""
        if x_str[0] == '-':
            reverse += '-'
            x_str = x_str[1:]

        for i in range(len(x_str)):
            j = len(x_str) - i - 1
            reverse += x_str[j]

        rev_int = int(reverse)
        if rev_int < -2**31 or rev_int > 2**31 -1:
            return 0
        
        return rev_int