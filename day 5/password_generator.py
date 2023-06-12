import random
print("Welcome to password generator!")
letters=int(input("how many letter like to be in your password?"))
symbols=int(input("how many symbol like to be in your password?"))
numbers=int(input("how many number like to be in your password?"))
pass1=[]
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number=['1','2','3','4','5','6','7','8','9','0']
symbol=['!','@','#',"$","^","&","*",")","("]

for i in range(0,letters):
  pass1.append(random.choice(letter))
for i in range(0,symbols):
  pass1.append(random.choice(symbol))
for i in range(0,numbers):
  pass1.append(random.choice(number))
hard_pass =[]
for i in range(0,len(pass1)):
  hard_pass.append(random.choice(pass1))
pass_str=""
for i in range(0,len(pass1)):
  pass_str +=hard_pass[i]
  
print(f"here is your password {pass_str}")