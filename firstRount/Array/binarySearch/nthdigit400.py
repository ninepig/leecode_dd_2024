class Solution:
    '''Check if n is a single digit number, return n if true.
Set the base value for the digit count to 9 and the initial number of digits to 1.
Use a while loop to iterate as long as n is greater than the product of the base and digits.
Inside the loop, subtract the count of digits from n, increase the base value by a factor of 10, and increase the number of digits by 1.
Calculate the number where the nth digit is located by using the formula: num = 10 ** (digits - 1) + (n - 1) // digits.
Calculate the index of the nth digit in the number by using the formula: idx = (n - 1) % digits.
Return the nth digit as an integer by converting the character at the calculated index to an integer.'''
    def findNthDigit(self, n: int) -> int:
        if n <= 9:  # If n is a single digit, return n
            return n

        base = 9  # Set the base value for the digit count
        digits = 1  # Set the initial number of digits to 1
        while n > base * digits:
            n -= base * digits  # Subtract the count of digits from n
            base *= 10  # Increase the base value by a factor of 10
            digits += 1  # Increase the number of digits by 1

        num = 10 ** (digits - 1) + (n - 1) // digits  # Calculate the number where the nth digit is located
        idx = (n - 1) % digits  # Calculate the index of the nth digit in the number

        return int(str(num)[idx])  # Return the nth digit as an integer