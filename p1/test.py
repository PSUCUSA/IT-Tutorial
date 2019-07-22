from Solution import Solution


sol = Solution()

assert sol.sum_list_1([]) == 0
assert sol.sum_list_2([]) == 0
assert sol.sum_list_3([]) == 0
assert sol.sum_list_4([]) == 0

assert sol.sum_list_1([1]) == 1
assert sol.sum_list_2([2]) == 2
assert sol.sum_list_3([1]) == 1
assert sol.sum_list_4(['1']) == 1

assert sol.sum_list_1([1, 2, 3]) == 6
assert sol.sum_list_2([1, 2, 3, 4]) == 6
assert sol.sum_list_3([1, 2, 3]) == 6
assert sol.sum_list_4(['1', '2', '3']) == 6

print("Great!")
