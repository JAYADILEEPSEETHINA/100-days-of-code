import random
words=["apple","mango","monkey","bear","camel","parrot","carrot"]
random_word=random.choice(words)
print("""_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/""")
emojis=["""" +---+
  |   |
  O   |
      |
      |
      |
=========""",   """+---+
  |   |
  O   |
  |   |
      |
      |
=========""","""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""","""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""","""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""","""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

life=5
win=False
lenght=len(random_word)
len1=0
str=""
for i in range(0,len(random_word)):
  str+="_"

my_list=list(str)

while life>0 and not win:
  found=False
  guessing_letter=input("guess a letter ").lower()
  
  for i in range(0,len(random_word) ):
    if(random_word[i]==guessing_letter and my_list[i]!=guessing_letter):
      my_list[i]=guessing_letter
      
      len1+=1
      found=True
  str=''.join(my_list)
  print(str)
  
  
  if(len1==lenght):
    win=True
  
      
  if found==False:
    print(f"You guessed {guessing_letter}, that's not in the word. You lose a life.")
    print(emojis[5-life])
    life-=1
  
if(win):
  print("you win the game")
else:
  print("you loss the game")
  print(emojis[5])