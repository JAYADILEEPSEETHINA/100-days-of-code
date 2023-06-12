from replit import clear
print("""___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\"""")
bid_dic={}
is_true=True
print("welcome to the secret auction program")
while is_true:
  name=input("What is your name?")
  price=int(input("What is your bid? $"))
  is_there=input("Are there any other bidders? Type 'yes or 'no'.").lower()
  if(is_there=="yes"):
    clear()
    bid_dic[name]=price
  else:
    max=0
    is_true=False
    for things in bid_dic:
      if(max<bid_dic[things]):
        max_name=things
        max=bid_dic[things]
      
    print(f"The winner is {max_name} with a bid of ${max}")
      
  
                    