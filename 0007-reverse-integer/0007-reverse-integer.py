class Solution:
    def reverse(self, x: int) -> int:
        
        # 1st solution
        
        # IF REVERSEING X CAUSES VALUE TO GO OUTSIDE THIS RANGE (-2^31, 2^31 - 1) RETURN 0
        # 123
        # GETTING 3 INTO THE FRONT: var = x % 10 => x /= 10, reverse = reverse * 10 + var

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = -1 if x < 0 else 1

        reversed_x = sign * int(str(abs(x))[::-1]) # -123 apply abs = 123, apply str = "123", use ::-1 = "321", apply int = 321, apply sign = -321

        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x

        # 2nd solution

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x) # 123

        while x!= 0:
            # get last digit from 1 = gets 1
            pop = x % 10
            # remove the last digit from 123 = 0
            x //= 10
            # x = x // 10

            # push the digit onto the reversed number = 1
            rev = rev * 10 + pop

            rev *= sign

            if rev < INT_MIN or rev > INT_MAX:
                return 0

            return rev

            # x = 0
            # rev = 321 * sign = 321 * 1 = 321
            
            


