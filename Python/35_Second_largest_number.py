# Second Largest Number
nums = list(map(int, input("Enter numbers: ").split()))
if len(nums) < 2:
    print("No second largest")
else:
    largest = second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    if second == float('-inf'):
        print("No second largest")
    else:
        print("Second largest:", second)
