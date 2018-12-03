plaintext=input("Input text:")
alphabet="abcdefghijklmnopqrstuvwxyz"
G=1            
cipher=''
choice=''
if use =='1':
     for k in plaintext:
         if kin alphabet:
             cipher += alphabet [(alphabet.index(k)+key)%len(alphabet)]
             print("your encrypted message is:"+cipher)
elif use =='2':
     for k in plaintext:
          if k in alphabet:
             cipher += alphabet [(alphabet.index(k)-key)%len(alphabet)]
             print("your encrypted message is:"+cipher)
else:
     print("you have entered an invalid input")
