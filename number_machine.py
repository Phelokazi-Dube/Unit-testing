def reverse_number(num):
    sum = 0
    rvs = 0
    while num>0:
        lastnum = num%10
        rvs = (rvs*10) + lastnum
        num = num//10
    return rvs

def add_nums(num):
    nums = 0
    rvs = 0
    while num > 0:
        lastnum = num % 10
        rvs = (rvs * 10) + lastnum
        num = num // 10
        nums = lastnum + nums
    return nums

def add_one(num):
    added = num + 11111
    return added

def main():
    try:
        num = int(input("Enter your five-digit number \n"))
        rvs = reverse_number(num)
        nums = add_nums(num)
        added = add_one(num)
        print("The number in reverse is", rvs)
        print("The sum equals to", nums)
        print("The number after adding 1 to each digit is" ,added)
    except ValueError:
	    print('Given input is not a number.')

if __name__=='__main__':
    main()