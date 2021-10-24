def palindrome(a):
    if a == a[::-1]:
        return 1
    return 0


user_input,lst = input("enter a string: "), []
for i in range(len(user_input)):
    if palindrome(user_input[i:user_input.rfind(user_input[i])+1]):
        lst.append(user_input[i:user_input.rfind(user_input[i])+1])

max_len = ''
for i in lst:
    if len(i) > len(max_len):
        max_len = i

print(max_len)
