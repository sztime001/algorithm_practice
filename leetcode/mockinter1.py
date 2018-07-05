class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        _INT_MAX32 = 2**31-1
        _INT_MIN32 = -2**31
        
        str = str.strip().split(".")
        if not str:
            return 0
        try:
            i = int(str[0])
            if i > _INT_MAX32:
                return _INT_MAX32
            elif i < _INT_MIN32:
                return _INT_MIN32
            else:
                return i
        except ValueError:
            return 0