
# \\ those value which gives same output when we read wither front or backward\\
s= input("enter the value: ")

reverse= s[:: -1]

if(s==reverse):
    print("Palindrome")
else:
    print("Non-palindrome")



