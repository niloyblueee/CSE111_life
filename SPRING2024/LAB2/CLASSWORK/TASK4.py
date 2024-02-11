#task4
def check_palindrome(any):
  y=''
  for i in any:
    if i!=' ':
      y+=i
  x=y[::-1]
  if y==x:
    print('Palindrome')
  else:
    print("Not a palindrome")
check_palindrome("madam")
check_palindrome("hello")
check_palindrome("nurses run")
check_palindrome("")