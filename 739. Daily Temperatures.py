class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if not len(stack) or temperatures[i] <= stack[-1][0]:
                stack.append([temperatures[i], i])
            else:
                for el, j in stack[::-1]:
                    if el < temperatures[i]:
                        result[j] = i - j
                        stack.pop()
                    else:
                        break
                stack.append([temperatures[i], i])
        return result