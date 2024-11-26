class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = -1 if x < 0 else 1

        x_reversed = int(str(abs(x))[::-1])
        x_reversed *= sign

        if x_reversed < -2**31 or x_reversed > 2**31 - 1:
            return 0

        return x_reversed
        