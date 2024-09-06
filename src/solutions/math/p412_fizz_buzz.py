from typing import List
from ...utils.helper import ProblemInfo

number = 412
name = "Fizz Buzz"
variant = "Easy"
takeaway = ""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
            pass

        return result

def run():
    info = ProblemInfo(number=number, name=name, variant=variant, takeaway=takeaway)
    info.display()

    # run code here
    res = Solution().fizzBuzz(n=15)
    print(f'New integer {res}')

    info.end()
    pass
