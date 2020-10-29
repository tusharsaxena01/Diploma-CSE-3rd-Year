#
# Random Cypher Creation
#
import random
import os
import pyfiglet
#
# The logic behind this cypher is to add
# a random number to the ascii value of
# the text and then print out the new
# syntax into a dictionary and print out
# the key to decrypt it
#
s = str('[+]') #  When a normal statement is to be shown
s1 = str('[-]') # When a negative statement is to be shown
valid_char = list(range(32,127))
def encrypt():
  print(pyfiglet.figlet_format("Encryptor"))
  '''
    Enable the next line in case pyfiglet is not installed
  '''
  #print("Encryptor")
  n_text = input("%s Enter Text: "%s)
  #
  # this would add or subtract a number which would only
  # give us valid character input so there is total of
  # 94 valid character then it means only 47 should be
  # added or subtracted to get a valid character input
  #
  key = random.randint(1,48)
  #
  # This statement is neccessary because if the key
  # is 32 then there is no mean to create this cypher
  # because it would spell out the exact same statement
  # changing the case
  #
  while key == 32:
    key = random.randint(1,48)
  print("%s Save the encrypted text to a file?(Y/N): "%s,end="")
  save = input()
  if save in 'Yy':
    f_name = input("%s Enter the file name: "%s)
    files = os.listdir()
  else:
    if save in 'nN':
      print("%s OK"%s,end=f"\n{s} ")
    else:
      print("%s Invalid Input!"%s1,end=f"\n{s1} ")
    print("File would not be saved!")
    #
    # Block to check if the file is already in the directory
    #
  if save in 'Yy':
    while True:
      num = 1
      if f_name+'.txt' in files:
        print("%s File Already Exists!"%s1)
        f_name = f"{f_name}-{num}"
        print("%s Checking File Name %s"%(s,f_name))
        continue
      else:
        break
  #
  # After renaming the input file using a number  
  #
    fi_name = f_name+'.txt'
    file = open(fi_name,'a')
  #
  #
  # Some spacing to make the code look less confusing ;-)
  #
  #
  encrypted_text=""
  for a in range(0,len(n_text)):
    n_a = n_text[a]
    if ord(n_a) == 32:
        continue
    #
    # This logic is neccassary to get a character which
    # could be simply typed on a regular keyboard
    #
    if ord(n_a) in range(47,127):
      enc = ord(n_a)-key
    elif ord(n_a) in range(0,47):
      enc = ord(n_a)+key
    enc_a = chr(enc)
    encrypted_text  = encrypted_text+enc_a
  if save in 'Yy':
    file.write(encrypted_text)
    key_statement = f"\nKey = {key}"
    file.write(key_statement)
    print("%s The Encryption is saved in %s\\%s"%(s,os.getcwd(),fi_name))
    file.close()
  print("\n%s Your Encrypted Text: %s\n%s Key: %i"%(s,encrypted_text,s,key))

def decrypt():
  # in this block e stands for encrypted for eg e_text means encrypted_text
  print(pyfiglet.figlet_format("Decryptor"))
  '''
    Enable the next line in case pyfiglet is not installed
  '''
  #print("Decryptor")

  #
  # Adding the read from file feature later
  #
  e_text = input("%s Enter Text: "%s)
  key = int(input("%s Key: "%s))
  while key not in range(1,48) and key == 32:
    key= int(input("%s Key: "%s))
  decrypted_text = ""
  for a in range(0,len(e_text)):
    e_a = e_text[a]
      #
      # This logic is neccassary to get a character which
      # could be simply typed on a regular keyboard
      #
    if ord(e_a) in range(47,128):
      nor = ord(e_a)+key
    elif ord(e_a) in range(0,47):
      nor = ord(e_a)-key
    nor_a = chr(nor)
    decrypted_text  = decrypted_text+nor_a
  print("\n%s Your Decrypted Text: %s"%(s,decrypted_text))
  print("%s Key Entered: %i"%(s,key))
#encrypt()
# Starting of the code
def choice():
  print(pyfiglet.figlet_format("Encryptor / Decryptor"))
  '''
    Enable the next line in case pyfiglet is not installed
  '''
  #print("Encryptor/Decryptor")
  
  print("%s Choose:\n%s 1. Encryptor\n%s 2. Decryptor\n%s 3. Exit"%(s,s,s,s))
  ch = int(input("%s > "%s))
  if ch == 1:
    encrypt()
  elif ch == 2:
    decrypt()
  elif ch == 3:
    quit()
  else:
    print("%s Error! Wrong Input!"%s1)
    print("%s Exiting..."%s1)

choice()