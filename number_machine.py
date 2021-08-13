def reverse_number(num):
    sum = 0
    rvs = 0
    while num>0:
        lastnum = num%10
        rvs = (rvs*10) + lastnum
        num = num//10
        sum = lastnum + sum
    return rvs,sum

def main():
    try:
        num = int(input("Enter your five-digit number \n"))
        rvs, sum = reverse_number(num)
        added = num + 11111
        print("The number in reverse is", rvs)
        print("The sum equals to", sum)
        print("The number after adding 1 to each digit is" ,added)
    except ValueError:
	    print('Given input is not a number.')
main()