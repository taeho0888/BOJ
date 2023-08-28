line = input()
nums = []
operator_idx = [-1]
operators = []

for i in range(len(line)):
    if not line[i].isdigit():
        operator_idx.append(i)
        operators.append(line[i])

operator_idx.append(len(line)+1)
for i in range(len(operator_idx)-1):
    nums.append(int(line[operator_idx[i]+1:operator_idx[i+1]]))

while "+" in operators:
    for i in range(len(operators)):
        if operators[i] == "+":
            nums[i] += nums[i+1]
            operators.pop(i)
            nums.pop(i+1)
            break
    
result = nums.pop(0)
for n in nums:
    result -= n
print(result)