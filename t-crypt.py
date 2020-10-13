from cryptography.fernet import Fernet
from colorama import init, Fore
import time
import os
import sys
import base64
def imprimir_texto(texto, n, i = 1):
    for _ in range(n):
        print(texto)
        time.sleep(i)
init(autoreset=True)
imprimir_texto(Fore.CYAN+"[VERSION]:   [2.0] \n", 1)
imprimir_texto(Fore.CYAN+"[CREADOR]:   [ALEJANDRO ESPINOSA] \n", 1)
imprimir_texto(Fore.CYAN+"[INSTAGRAM]: https://www.instagram.com/alejandrogit9/ \n", 1)
imprimir_texto(Fore.CYAN+"[GITHUB]:    https://github.com/AlejandroCode9 \n", 1)
imprimir_texto(Fore.CYAN+"[FACEBOOK]:  https://www.facebook.com/profile.php?id=100028037019091 \n", 1)

print(Fore.CYAN+"Presione [ENTER]")
input("")
os.system("cls")




init(autoreset=True)

while True:
        print(Fore.WHITE+'''+========================================================+
||       Traductor de codificacion o criptografia       ||
+========================================================+
||                          ||                          ||
|| [1] BlackCode            ||  [4] ROT                 ||
||                          ||                          ||
|| [2] Base64               ||  [5] Fernet              ||
||                          ||                          ||
|| [3] Binario              ||  [6] Exit                ||
||                          ||                          ||
+===================================================V2.0=+
+====================[T-CRYPTOGRAPHY]====================+ \n''')

        y = input(Fore.WHITE+"[Opcion]: ")
        os.system("cls")

        if y== '1':
                print("")
                print("+-----------------------------+")
                print("|     ≋B≋l≋a≋c≋k≋C≋o≋d≋e≋     |")
                print("+-----------------------------+")
                print("|[1] Codifica  | Decodifica   |")
                print("|[0] Salir                    |")
                print("+-----------------------------+")
                b = int(input("> "))
                os.system('cls')
                

                while b !=0:
                        if b == 1:
                           print("")
                           print("+--------------------+")
                           print("|introduzca el texto |")
                           print("+--------------------+")
                           def encriptar(y):
                             x1=y.replace('A', '-')
                             x2=x1.replace('B', 'b')
                             x3=x2.replace('C', '|')
                             x4=x3.replace('D', ',')
                             x5=x4.replace('E', '<')
                             x6=x5.replace('F', '°')
                             x7=x6.replace('G', '&')
                             x8=x7.replace('H', '4')
                             x9=x8.replace('I', '.')
                             x10=x9.replace('J', '2')
                             x11=x10.replace('K', '$')
                             x12=x11.replace('L', '+')
                             x13=x12.replace('M', '3')
                             x14=x13.replace('N', '%')
                             x15=x14.replace('O', '*')
                             x16=x15.replace('P', '¬')
                             x17=x16.replace('Q', '=')
                             x18=x17.replace('R', '~')
                             x19=x18.replace('S', '/')
                             x20=x19.replace('T', '¿')
                             x21=x20.replace('U', '1')
                             x22=x21.replace('V', '(')
                             x23=x22.replace('W', '5')
                             x24=x23.replace('X', ')')
                             x25=x24.replace('Y', '9')
                             x0=x25.replace('Z', '7')
                             return x0
                           def desencriptar(p):
                             x1=p.replace('-', 'A')
                             x2=x1.replace('b', 'B')
                             x3=x2.replace('|', 'C')
                             x4=x3.replace(',', 'D')
                             x5=x4.replace('<', 'E')
                             x6=x5.replace('°', 'F')
                             x7=x6.replace('&', 'G')
                             x8=x7.replace('4', 'H')
                             x9=x8.replace('.', 'I')
                             x10=x9.replace('2', 'J')
                             x11=x10.replace('$', 'K')
                             x12=x11.replace('+', 'L')
                             x13=x12.replace('3', 'M')
                             x14=x13.replace('%', 'N')
                             x15=x14.replace('*', 'O')
                             x16=x15.replace('¬', 'P')
                             x17=x16.replace('=', 'Q')
                             x18=x17.replace('~', 'R')
                             x19=x18.replace('/', 'S')
                             x20=x19.replace('¿', 'T')
                             x21=x20.replace('1', 'U')
                             x22=x21.replace('(', 'V')
                             x23=x22.replace('5', 'W')
                             x24=x23.replace(')', 'X')
                             x25=x24.replace('9', 'Y')
                             x0=x25.replace('7', 'Z')
                             return x0
                           y= input(">  ").upper()
                           z=encriptar(y)
                           print(Fore.YELLOW+"[Codificado]: ", z)
                           print(Fore.YELLOW+"[Decodificado]: ", desencriptar(z))
                                

                        else:
                                print(Fore.RED+"opcion no valida")
                        print("")       
                        print("+-----------------------------+")
                        print("|     ≋B≋l≋a≋c≋k≋C≋o≋d≋e≋     |")
                        print("+-----------------------------+")
                        print("|[1] Codifica  | Decodifica   |")
                        print("|[0] Salir                    |")
                        print("+-----------------------------+")

                        b = int(input(Fore.WHITE+"[Opcion]: "))
                        os.system('cls')

        elif y =='2':
                print("")
                print("+-------------------------+")
                print("| ▌│█║▌║▌║ Base64 ║▌║▌║█│▌|")
                print("+-------------------------+")
                print("|[1] Codifica tu texto    |")
                print("|[2] Decodifica tu texto  |")
                print("|[0] Salir                |")       
                print("+-------------------------+")
                bs = int(input("> "))
                os.system('cls')
                
                while bs !=0:
                        if bs ==1:
                            print("")
                            print("[Ingrese lo que desea codificar]")
                            s = input("> ")
                            b = s.encode("UTF-8")
                            e = base64.b64encode(b)
                            s1 = e.decode("UTF-8")
                            print(Fore.YELLOW+"[Base64]: " , s1)
                        elif bs ==2:
                            print("")
                            print("[Ingrese lo que desea decodificar]")
                            x = input("> ")
                            b1 = x.encode("UTF-8")
                            d = base64.b64decode(b1)
                            s2 = d.decode("UTF-8")
                            print(Fore.YELLOW+"[Decodificado]: ",s2)
                        else:
                            print(Fore.RED+"[opcion no valida]")

                        print("")
                        print("+-------------------------+")
                        print("| ▌│█║▌║▌║ Base64 ║▌║▌║█│▌|")
                        print("+-------------------------+")
                        print("|[1] Codifica tu texto    |")
                        print("|[2] Decodifica tu texto  |")
                        print("|[0] Salir                |")       
                        print("+-------------------------+")    
                        bs = int(input(Fore.WHITE+"[Opcion]: "))
                        os.system('cls')


        elif y =='3':
             class Encriptartxt():
                 def encriptar(self,txt):
                     mensaje = ''
                     for letra in txt:
                         x = self.convertirDB(ord(letra))
                         mensaje = mensaje + str(x) + " "

                     return mensaje

                 def convertirDB(self,decimal):
                     DE = ''
                     dec1 = decimal
                     dec = 0
                     i = 0
                     while i < 8:
                         dec = dec1 % 2
                         DE = DE + str(dec)
                         if dec1==decimal :
                             dec1 = decimal//2
                         else:
                             dec1 = dec1//2

                         i = i + 1
                     return (self.invertir(DE))
                 def invertir(self,var):
                     return var[::-1]    
             class Desencriptaciontxt():

                 def Desencriptar(self,binario):
                     x = binario.split()
                     texto = ''
                     for i in range(len(x)):
                         texto = texto + chr(self.convertirBD(int(x[i])))

                     return texto
                 def convertirBD(self,binario):
                     decimal = 0
                     i=0    
                     for iteractor in self.invertir(str(binario)):
                         if(int(iteractor) ==1):
                             decimal = decimal + 2 ** i

                         i = i + 1
                           
                     return decimal
                 def invertir(self,var):
                     return var[::-1]
                
             n = Encriptartxt();
             x = Desencriptaciontxt();
             print("")
             print("+----------------------------+")
             print("|      ░B░I░N░A░R░I░O░       |")
             print("+----------------------------+")
             print("|[1] Codifica tu texto       |")
             print("|[2] Decodifica tu texto     |")
             print("|[0] Salir                   |")       
             print("+----------------------------+")
             b = int(input("> "))
             os.system('cls')

             while b !=0:
                  if b == 1:
                      print("")
                      print("+---------------------------------+")
                      print("| introduzca el texto a codificar |")
                      print("+---------------------------------+")
                      print(Fore.YELLOW+"[mensaje]")
                      print(n.encriptar(input(">")))
                  elif b == 2:
                      print("")
                      print("+-----------------------------------+")
                      print("| Introduzca el texto a decodificar |")
                      print("+-----------------------------------+")
                      print(Fore.YELLOW+"[mensaje]")
                      print(x.Desencriptar(input(">" )))
                  else:
                      print(Fore.RED+"[Opcion no valida]")

                  print("")
                  print("+----------------------------+")
                  print("|      ░B░I░N░A░R░I░O░       |")
                  print("+----------------------------+")
                  print("|[1] Codifica tu texto       |")
                  print("|[2] Decodifica tu texto     |")
                  print("|[0] Salir                   |")       
                  print("+----------------------------+")
                  b = int(input(Fore.WHITE+"[Opcion]: "))
                  os.system('cls')
 

        elif y =='4':
            print("")
            print("+-------------------------+")
            print("|         ≋R≋O≋T≋         |")  
            print("+-------------------------+")
            print("|[1] Codifica tu texto    |")
            print("|[2] Decodifica tu texto  |")
            print("|[0] Salir                |")       
            print("+-------------------------+")
            r = int(input("> "))
            os.system('cls')

            while r !=0:
                    
                if r ==1:
                    print("")
                    print("[Ingrese el texto a [codificar]")
                    print(Fore.YELLOW+"[Mensaje]")
                    t = input("> ")

                    if t == t.upper ():
                        abc=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                    else:
                        abc=("abcdefghijklmnopqrstuvwxyz")

                    print("¿Que ROT necesita?")
                    b = int(input("> "))
                    cifrado = ""

                    for c in t:
                        if c in abc:
                            cifrado += abc[(abc.index(c)+b)%(len(abc))] 
                        else:
                            cifrado += c
                    print("")        
                    print("+==================+")        
                    print("| TEXTO CODIFICADO |")
                    print("+==================+")
                    print(Fore.YELLOW+"[Codificado]: ", cifrado)

                elif r ==2:
                    print("")
                    print("[Ingrese el texto a [decodificar]")
                    print(Fore.YELLOW+"[Mensaje]")
                    t1 = input("> ")

                    if t1 == t1.upper ():
                        abc=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                    else:
                        abc=("abcdefghijklmnopqrstuvwxyz")

                    print("¿Que ROT necesita?")
                    b1 = int(input("> "))
                    cifrado = " "

                    for c in t1:
                        if c in abc:
                            cifrado += abc[(abc.index(c)-b1)%(len(abc))]
                        else:
                            cifrado += c
                    print("")        
                    print("+====================+")        
                    print("| TEXTO DECODIFICADO |")
                    print("+====================+")
                    print(Fore.YELLOW+"[Decodificado]: ", cifrado)

                else:
                    print(Fore.RED+"[Opcion no valida]")

                print("")   
                print("+-------------------------+")
                print("|         ≋R≋O≋T≋         |") 
                print("+-------------------------+")
                print("|[1] Codifica tu texto    |")
                print("|[2] Decodifica tu texto  |")
                print("|[0] Salir                |")       
                print("+-------------------------+")
                r = int(input(Fore.WHITE+"[Opcion]: "))
                os.system('cls')

        elif y =='5':
             print("")
             print("+-------------------------+")
             print("|      ░F░E░R░N░E░T░      |")
             print("+-------------------------+")
             print("|[1] Encripta tu texto    |")
             print("|[2] Desencripta tu texto |")
             print("|[0] Salir                |")       
             print("+-------------------------+")
             fe = int(input("> "))
             os.system("cls")


             while fe !=0:

                 if fe ==1:
                     clave = Fernet.generate_key()
                     print("Esta es tu key")
                     print(Fore.YELLOW+"[Key]:" , clave)
                     print("+--------------------+")
                     print("| Ingresa tu mensaje |")
                     print("+--------------------+")
                     b = input(Fore.YELLOW+"[Mensaje]: ")
                     mensaje = b.encode()

                     f = Fernet(clave)

                     encriptado = f.encrypt(mensaje)
                     print("")
                     print("+--------------------+")
                     print("|  Texto encriptado  |")
                     print("+--------------------+")
                     print(Fore.YELLOW+"[Mensaje]:" , encriptado)
                     print("")
                 elif fe ==2:
                     print("")
                     print("+----------------+")
                     print("| Ingresa la key |")
                     print("+----------------+")
                     key = input(Fore.YELLOW+"[Key]: ");
                     print("")
                     print("+==================+")      
                     print("| Texto encriptado |")
                     print("+==================+")
                     text= input(Fore.YELLOW+"[Mensaje]: ");

                     key = bytes(key,encoding="utf-8")
                     text = bytes(text,encoding="utf-8")

                     f2 = Fernet(key)

                     f = f2.decrypt(text)
                     print("")
                     print("+=====================+")
                     print("| Texto desencriptado |")
                     print("+=====================+")
                     print(Fore.YELLOW+"[Mensaje]: " , f)
                     #muchas gracias a Jesus David Clavijo por ayudarme en esta parte:)

                 else:
                     print(Fore.RED+"[Opcion no valida]")
                    
                 print("+-------------------------+")
                 print("|      ░F░E░R░N░E░T░      |")
                 print("+-------------------------+")
                 print("|[1] Encripta tu texto    |")
                 print("|[2] Desencripta tu texto |")
                 print("|[0] Salir                |")       
                 print("+-------------------------+")
                 fe = int(input(Fore.WHITE+"[Opcion]: "))
 
                 
        elif y =='6':
            print("")   
            input(Fore.RED+"[Presione E̳N̳T̳E̳R̳]")
            os.system("cls")
            sys.exit(101)     
                       

                             
                                    
                                
                                
                            
                                

                        
                
                            
                                
                            
                
                                
                                
                
                
                        
                        
                
        
