class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        # Brute Force
        ans = []

        for i in range(1,n+1):
            is_div_3 = i % 3 == 0
            is_div_5 = i % 5 == 0
            
            if is_div_3 and is_div_5: ans.append("FizzBuzz")
            elif is_div_3: ans.append("Fizz")
            elif is_div_5: ans.append("Buzz")
            else: ans.append(f"{i}")
        
        return ans