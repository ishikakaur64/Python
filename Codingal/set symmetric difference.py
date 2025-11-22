set_a = {10, 20, 30, 40, 50}
set_b = {40, 50, 60, 70, 80}

print("Set A:", set_a)
print("Set B:", set_b)

symmetric_diff_method = set_a.symmetric_difference(set_b)
print("\nSymmetric Difference using method:", symmetric_diff_method)

symmetric_diff_operator = set_a ^ set_b
print("Symmetric Difference using ^ operator:", symmetric_diff_operator)