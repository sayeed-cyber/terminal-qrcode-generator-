# pip install pyqrcode 
# pip install pypng
import pyqrcode 
import png
import os


def main ():
     print ("to kill process enter : ***")
     s= input ("enter the subject  :") 
     global xyz


     if s==("***"):
          os.system('cls||clear')
          exit()

     elif  len (s) !=0: # if the lenth of subject is not equal to 0
           xyz = pyqrcode.create(s) 
           print(xyz.terminal(quiet_zone=1))
           option()
              
     else:
          os.system('cls||clear')
          print ("error!! subject must be given")
          main() 

def option ():
    print("to generate QRCODE one's again enter : 1")
    print("to save this QRCODE as image enter : 2")
    print("to kill process : 3")
    d = input ()
    if d == ("1"):
       os.system('cls||clear')
       main ()
    elif d== ("2"):
       os.system('cls||clear')
       plain ()
    elif d==("3"):
       os.system('cls||clear')
       exit ()
    else :
        print ("error!! select any above option")
        option()
def plain ():
     print ("to kill process enter :000")
     print ("to generate QRCODE one's again enter :001")
     print ("warning!!! file name cannot be 000 & 001")
     p = input ("enter the file name to be saved  :")

     if p == ("000"):
         os.system('cls||clear')
         exit ()
     elif p==("001"):
         os.system('cls||clear')
         main()
     elif len (p) !=0: # if the lenth of file name is not equal to 0
            xyz.png((p)+'.png',scale =6) # save's the image where this file is located     

            os.system('cls||clear')
            print ("QRCODE has been successfully saved where this program file is located")
            option()
     else:
        print ("error!! file name must be given")
        plain ()
main()
option()
plain()

# by sayeedkhan 
# gmail : sayeedpkhan2004@gmail.com
# source code : self 
# credit : python.org / pyqrcode documentation 
#/pypng documentation# instagram : jefreonsyed 