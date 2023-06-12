import replit

print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|""")

def add(n1,n2):
  return n1+n2
def mul(n1,n2):
  return n1*n2
def div(n1,n2):
  return n1/n2
def sub(n1,n2):
  return n1-n2
first_num=int(input("What's the first number?: "))
is_continue=True


while is_continue:
  operator=input("""+
  -
  *
  /
  Pick an operation: """)
  operators_list={"+":add,"-":sub,"*":mul,"/":div}
  sec_num=int(input("What's the next number?: "))
  print(f"{first_num} {operator} {sec_num} = {operators_list[operator](first_num,sec_num)}")
  
  con=input(f"Type 'y' to continue calculating with {operators_list[operator](first_num,sec_num)}, or type 'n' to start a new calculation: ").lower()
  if(con=="n"):
    is_continue=False
  else:
    replit.clear()
    first_num=operators_list[operator](first_num,sec_num)
    
  
