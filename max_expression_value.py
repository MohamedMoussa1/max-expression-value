class MaxExpValue:
    def max_expression_value(self, nums, ops):
        Max = [[float('-inf')] * range(len(nums) + 1) for _ in range(len(nums) + 1)]
        Min = [[float('inf')] * range(len(nums) + 1) for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            Max[i][i] = nums[i-1]
            Min[i][i] = nums[i-1]
        for diff in range(1, len(nums)):
            for i in range(1, len(nums)-diff + 1):
                j = i + diff
                for k in range(i, j):
                    if ops[k-1] == '+':
                        Max[i][j] = max(Max[i][j], Max[i][k] + Max[k+1][j])
                        Min[i][j] = min(Min[i][j], Min[i][k] + Min[k+1][j])
                    elif ops[k-1] == '-':
                        Max[i][j] = max(Max[i][j], Max[i][k] - Min[k+1][j])
                        Min[i][j] = min(Min[i][j], Min[i][k] - Max[k+1][j])
        return Max[1][len(nums)]
