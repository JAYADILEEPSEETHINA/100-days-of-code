print( """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")
alpha_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encrypt(msg,num):
  
  encrypt_str=""
  
  for i in range(0,len(msg)):
    for j in range(0,26):
      if(msg[i]==alpha_list[j]):
        add1=j+num
      
        if(j+num<26):
          add1=j+num
          encrypt_str+=alpha_list[add1]
          
        else:
          
          encrypt_str+=alpha_list[add1-25]
  print(f"here the encoded msg  {encrypt_str}")
def decrypt(msg,num):
  decrypt_str=""
  for i in range(0,len(msg)):
    for j in range(0,26):
      if(msg[i]==alpha_list[j]):
        add1=j-num
        if(add1<0):
          decrypt_str+=alpha_list[25+add1]
        else:
          decrypt_str+=alpha_list[add1]
  print(f"here the decoded msg {decrypt_str}.")
        
          
          
        
        
        
user_ans=input("type 'encode' for encrypt ,type 'decode for decrypt' ").lower()
user_decrypt=""
user_encrypt=""
user_msg=input("type your message ").lower()
shift_num=int(input("type shift number "))
if(user_ans=="encode"):
  encrypt(user_msg,shift_num)
else:
  decrypt(user_msg,shift_num)
        
  
  
