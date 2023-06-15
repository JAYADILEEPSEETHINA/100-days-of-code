import art
import replit
import random
import game_data
choice1=random.choice(game_data.data)
score=0
game_on=True
while game_on:
  
  choice2=random.choice(game_data.data)
  name1=choice1["name"]
  desc1=choice1["description"]
  country1=choice1["country"]
  followers1=choice1["follower_count"]
  name2=choice2["name"]
  desc2=choice2["description"]
  country2=choice2["country"]
  followers2=choice2["follower_count"]
  
  print(art.logo)
  print(f"compare A {name1} , {desc1}, {country1}")
  print(art.vs)
  print(f"compare B {name2} , {desc2}, {country2}")
  user_ans=input("who has more followers A or B ").lower()
  if(user_ans=="a" and followers1>followers2):
    score+=1
    replit.clear()

    
  elif(user_ans=="b" and followers1<followers2):
    score+=1
    choice1=choice2
    replit.clear()
  else:
    print(f"sorry that wrong .final score :{score}")
    game_on=False
  




