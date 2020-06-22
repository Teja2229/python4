num = input('Enter any number : ')
try:
    val = int(num)
    if num == str(num)[::-1]:
        print('The given number is palindrome')
    else:
        print('The given number is not a palindrome')
except ValueError:
    print("it is not a valid number")