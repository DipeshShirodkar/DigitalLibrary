import os
import pyttsx3

def acadamics():
          print("==========================================")
          b ="list of books"
          print(b.center(40).upper())
          print("==========================================")
          print("ID \t book_name")
          print("122\t 1stYEAR")
          print("123\t 2stYEAR")
          print("124\t 3stYEAR")
          print("125\t 4stYEAR")
          acadamics_id = int(input("BOOK  ID==>"))
          match acadamics_id:
                case 122: 
                  print("WHAT YOU WANT \nPRESS:- \n 1.READ \n 2.LISTEN")
                  option = int(input(" ====> "))
     
                       #chooise()
                  if option == 1:                            
                          f = open("LibraryManagement/1styear" , "r")
                          w = f.read()
                          print(w)
                      # f.close()
                  elif option == 2 :
                           robo = pyttsx3.init()
                           print("I am starting reading ==>")
                           q = open("LibraryManagement/1styear","r" )
                           w = q.read()
                           robo.say(w)
                           robo.runAndWait()
                  else :
                        print("invalid")

                case 123:
                  print("WHAT YOU WANT \nPRESS:- \n 1.READ \n 2.LISTEN")
                  option = int(input(" ====> "))
                  if option == 1:                                                 
                          f =open("LibraryManagement/2ndyear" ,"r")
                          p = f.read()
                          print(p)
                  elif option == 2 :
                           robo = pyttsx3.init()
                           print("I am starting reading ==> \n")
                           q = open("LibraryManagement/2ndyear","r" )
                           w = q.read()
                           robo.say(w)
                           robo.runAndWait()
                  else :
                            print("invalid")

                case 124:
                  print("WHAT YOU WANT \nPRESS:- \n 1.READ \n 2.LISTEN")
                  option = int(input(" ====> "))
                      
                      #chooise()
                  if option == 1:                                                                        
                       f =open("LibraryManagement/3rdyear" , "r")
                       z = f.read()
                       print(z)
                      # o.close()
                  elif option == 2  :
                           robo = pyttsx3.init()
                           print("I am starting reading ==> \n")
                           q = open("LibraryManagement/3rdyear","r" )
                           w = q.read()
                           robo.say(w)
                           robo.runAndWait()
                  else :
                       print("invalid")
                       
                case 125:
                  print("WHAT YOU WANT \nPRESS:- \n 1.READ \n 2.LISTEN")
                  option = int(input(" ====> "))
                  if option == 1:                                                  
                       o =open("LibraryManagement/4thyear" , "r")
                       c = o.read()
                       print(c)
                     # o.close()
                  elif option == 2 :
                           robo = pyttsx3.init()
                           print("I am starting reading ==> \n")
                           q = open("LibraryManagement/4thyear","r" )
                           w = q.read()
                           robo.say(w)
                           robo.runAndWait()
                  else :
                       print("invalid")
                        
                case _:
                      print("invalid")                 

def novel():
      print("==========================================")
      b ="list of books"
      print(b.center(40).upper())
      print("==========================================")
      print("ID \t book_name")
      print("134\t Jane Eyre")
      print("135\t The Great Gatsby")
      print("136\t wuthering  Height")
      print("137\t Me Before You")
      novel_id = int(input("BOOK  ID==>"))
      match novel_id:

            case 134:
              print("WHAT YOU WANT \nPRESS:- \n 1.READ \n 2.LISTEN")
              option = int(input(" ====> "))

              #chooise()
              if option == 1:                                                       
               f = open("LibraryManagement/jane_Eyre.ovel" , "r") 
               q = f.read()
               print(q)
              elif option == 2 :
                           robo = pyttsx3.init()
                           print("I am starting reading ==> \n")
                           q = open("LibraryManagement/jane_Eyre.ovel","r" )
                           w = q.read()
                           robo.say(w)
                           robo.runAndWait()
              else :
                   print("invalid")

            case 135: 
              print("WHAT YOU WANT \nPRESS:- \n 1.READ \n 2.LISTEN")
              option = int(input(" ====> "))
              
              #chooise()
              if option == 1:                           
               f = open("LibraryManagement/The_Great_Gtsby" , "r")
               q = f.read()
               print(q)
              elif option == 2 :
                           robo = pyttsx3.init()
                           print("I am starting reading ==> \n")
                           q = open("LibraryManagement/The_Great_Gtsby","r" )
                           w = q.read()
                           robo.say(w)
                           robo.runAndWait()
              else :
                   print("invalid")

            case 136:
              print("WHAT YOU WANT \nPRESS:- \n 1.READ \n 2.LISTEN")
              option = int(input(" ====> "))
  
              #chooise()
              if option == 1:                
                f = open("LibraryManagement/Wuthering_Height" , "r")  
                q = f.read()
                print(q)
              elif option == 2 :
                           robo = pyttsx3.init()
                           print("I am starting reading ==> \n")
                           q = open("LibraryManagement/Wuthering_Height","r" )
                           w = q.read()
                           robo.say(w)
                           robo.runAndWait()
              else :
                   print("invalid")

            case 137:
              print("WHAT YOU WANT \nPRESS:- \n 1.READ \n 2.LISTEN")
              option = int(input(" ====> "))
              if option == 1:
                f = open("LibraryManagement/me.text" , "r")
                q = f.read()
                print(q)
              elif option == 2 :
                           robo = pyttsx3.init()
                           print("I am starting reading ==> \n")
                           q = open("LibraryManagement/me.text","r" )
                           w = q.read()
                           robo.say(w)
                           robo.runAndWait()
              else :
                   print("invalid")

            case _:
                      print("invalid")                 

def story():
      print("==========================================")
      b ="list of books"
      print(b.center(40).upper())
      print("==========================================")
      print("ID \t book_name")
      print("11\t Chota Bheam ")
      print("22\t Lela Majnu")
      story_id = int(input("BOOK  ID==>"))
      match story_id:
            case 11:
              print("WHAT YOU WANT \nPRESS:- \n 1.READ \n 2.LISTEN")
              option = int(input(" ====> "))
              
             # chooise()
              if option == 1:                              
                 e = open("LibraryManagement/Chota_bheam" , "r")
                 t = e.read()
                 print(t)
              elif option == 2 :
                           robo = pyttsx3.init()
                           print("I am starting reading ==> \n ")
                           q = open("LibraryManagement/Chota_bheam","r" )
                           w = q.read()
                           robo.say(w)
                           robo.runAndWait()
              else :
                   print("invalid")

         
            case 22: 
              print("WHAT YOU WANT \nPRESS:- \n 1.READ \n 2.LISTEN")
              option = int(input(" ====> "))
              
            #   chooise()
              if option == 1:                           
               e = open("LibraryManagement/Lela_Majnu" , "r")
               t = e.read()
               print(t)
              elif option == 2 :
                           robo = pyttsx3.init()
                           print("I am starting reading ==> \n")
                           q = open("LibraryManagement/Lela_Majnu","r" )
                           w = q.read()
                           robo.say(w)
                           robo.runAndWait()
              else :
                   print("invalid")

                             
            case _:             
               print("invalid")

      
def newspaper():
       print("==========================================")
       b ="list of books"
       print(b.center(40).upper())
       print("==========================================")
       print("ID \t book_name")
       print("222\t MARATHI")
       print("333\t ENGLISH")
       print("444\t HINDI")
       newspaper_id = int(input("BOOK  ID==>"))
       match newspaper_id :
             case 222:
              print("WHAT YOU WANT \nPRESS:- \n 1.READ \n 2.LISTEN")
              option = int(input(" ====> "))

              # chooise()
              if option == 1:                            
               s = open("LibraryManagement/MARATHI" , "r")
               j = s.read()
               print(j)
              elif option == 2 :
                           robo = pyttsx3.init()
                           print("I am starting reading ==> \n")
                           q = open("LibraryManagement/MARATHI","r" )
                           w = q.read()
                           robo.say(w)
                           robo.runAndWait()
              else :
                   print("invalid")

             case 333:
              print("WHAT YOU WANT \nPRESS:- \n 1.READ \n 2.LISTEN")
              option = int(input(" ====> "))
              if option == 1:                             
                s = open("LibraryManagement/ENGLISH" , "r")
                j = s.read()
                print(j)
              elif option == 2 :
                           robo = pyttsx3.init()
                           print("I am starting reading ==> \n")
                           q = open("LibraryManagement/ENGLISH","r" )
                           w = q.read()
                           robo.say(w)
                           robo.runAndWait()
              else :
                   print("invalid")

             
             case 444:
              print("WHAT YOU WANT \nPRESS:- \n 1.READ \n 2.LISTEN")
              option = int(input(" ====> "))
              if option == 1:                  
                  s = open("LibraryManagement/hindi.text" , "r")
                  j = s.read()
                  print(j)
              elif option == 2 :
                           robo = pyttsx3.init()
                           print("I am starting reading ==> \n")
                           q = open("LibraryManagement/hindi.text","r" )
                           w = q.read()
                           robo.say(w)
                           robo.runAndWait()
              else :
                   print("invalid")
             
             case _:             
               print("invalid")

def intro():   
 print("okay!! \nWhich Type Of Book You Are Looking For ")
 print(" 1.ACADAMICS \n 2.NOVEL \n 3.STORY \n 4.NEWSPAPER ")
 book_type = int(input("====> "))
 match book_type :
      case 1:
            acadamics()
      case 2:
            novel()
      case 3:
            story()
      case 4:
            newspaper()
      case _:
           print("check again :-  ")           
           intro()

print("==========================================")
W = "welcome to digital library"
print(W.center(40).upper())
print("==========================================")

print("PLEASE ENTER YOUR ID")
id =int(input("====> E122"))

if id in range(4000 , 5000):
      intro()
              
else :
   print("PLEASE ENTER YOUR VALID ID")
   id = int(input("====>E122"))
   if id in range(4000 , 5000):
     intro()
   else :
     print("PLEASE ENTER YOUR VALID ID")
     id = int(input("====>E122"))
     if id in range(4000 , 5000):
      intro()
     else :
      print("SORRY NOT ELIGIBLE")