def binarySearch(num, last, start, n):
    if start >= last:
        mid = last + (start - last)/2
        if num[mid] == n:
            print("Number is present")
        elif num[mid] > n:
            return binarySearch(num, last, mid-1, n)
        else:
            return binarySearch(num, mid+1, start, n)
    else:
        print("Number not found")


if __name__ == "__main__":
    num1 = input("Enter an ordered list of numbers e.g. 34 45 67 78.. etc : ")
    num1 = list(num1.split(" "))
    num1 = sorted(num1, key=int)
    n1 = int(input("Enter another number : "))
    binarySearch(num1, len(num1), 0, n1)
