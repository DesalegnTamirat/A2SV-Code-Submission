for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input()))
    for i in range(n):
        nums[i] -= 1
    
    sum_count = {0: 1}
    accumulator = total = 0
    for num in nums:
        accumulator += num
        if accumulator in sum_count:
            total += sum_count[accumulator]
            sum_count[accumulator] += 1
        else:
            sum_count[accumulator] = 1
    
    print(total)