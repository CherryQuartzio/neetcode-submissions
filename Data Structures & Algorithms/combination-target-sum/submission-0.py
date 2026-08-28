class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, current, total):
            ''' There are two options we can take for each layer, we can either:
            - Add another count of the current candidate into the combination
            - Move on to the next candidate
            '''
            if total == target: # sum of the current combination matches
                result.append(current.copy())
                return

            # terminate branch if we are out of base candidate or if the sum already went over target
            if i >= len(nums) or total > target:
                return
            
            # either add current candidate or try out next candidate
            current.append(nums[i])
            dfs(i, current, total + nums[i])

            current.pop()
            dfs(i + 1, current, total)

        dfs(0, [], 0) # we start with the first base candidate, an empty combination, and no total
        return result

        