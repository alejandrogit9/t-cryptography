from cryptography.fernet import Fernet
import base64


print("+=========================================================+")
print("||         Traductor de cifrados o criptografia          ||")
print("+=========================================================+")
print("|| [1] BlackCode            ||  [4] ROT                  ||")
print("||                          ||                           ||")
print("|| [2] Base64               ||  [5] Fernet               ||")
print("||                          ||                           ||")
print("|| [3] Binario              ||  [6] Exit                 ||")
print("||                          ||                           ||")
print("+=========================================================+")
print("+=================[Hecho por Alejandro]===================+ \n")

y = int(input("Qué opcion desea: "))

if y ==1:
    print("+-------------------------+")
    print("|       [Opciones]        |")
    print("+-------------------------+")
    print("|[1] Encripta tu texto    |")
    print("|[2] Desencripta tu texto |")
    print("|[0] Salir                |")       
    print("+-------------------------+")
    b = int(input("> "))

    while b !=0:
        if b == 1:            
            print("+-------------------------------+")
            print("|introduzca el texto a encriptar|")
            print("+-------------------------------+")
        
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
            y= input("Ingrese el texto a encriptar: ").upper()
            z=encriptar(y)
            print(z)
            print(desencriptar(z))
        elif b ==2:
            print("+----------------------------------+")
            print("|introduzca el texto a desencriptar|")
            print("+----------------------------------+")            
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
            y= input("Ingrese el texto a desencriptar: ").upper()
            z=encriptar(y)
            print(z)
            print(desencriptar(z))
        else:
            print("[Opcion no valida]")

        b = int(input("[Opcion]:"))

elif y==2:   
    print("+-------------------------+")
    print("|       [Opciones]        |")
    print("+-------------------------+")
    print("|[1] Encripta tu texto    |")
    print("|[2] Desencripta tu texto |")
    print("|[0] Salir                |")       
    print("+-------------------------+")
    bs = int(input("> "))

    while bs !=0:
        if bs ==1:
            print("[Ingrese lo que desea codificar]")
            s = input("> ")
            b = s.encode("UTF-8")
            e = base64.b64encode(b)
            s1 = e.decode("UTF-8")
            print("Base64: " , s1)

        elif bs ==2:
            print("[Ingrese lo que desea decodificar]")
            x = input("> ")
            b1 = x.encode("UTF-8")
            d = base64.b64decode(b1)
            s2 = d.decode("UTF-8")
            print("> ",s2)
        else:
            print("[Opcion no valida]")
        bs = int(input("[Opcion]: "))

elif y ==3:
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
    print("+-------------------------+")
    print("|       [Opciones]        |")
    print("+-------------------------+")
    print("|[1] Encripta tu texto    |")
    print("|[2] Desencripta tu texto |")
    print("|[0] Salir                |")       
    print("+-------------------------+")
    b = int(input("> "))

    while b !=0:
        if b == 1:
            print("+-------------------------------+")
            print("|introduzca el texto a encriptar|")
            print("+-------------------------------+")
            print(n.encriptar(input(">")))
        elif b == 2:
            print("+----------------------------------+")
            print("|Introduzca el texto a desencriptar|")
            print("+----------------------------------+")
            print(x.Desencriptar(input(">" )))
        else:
            print("[Opcion no valida]")

        b = int(input("[Opcion]: "))

elif y ==4:
    print("+-------------------------+")
    print("|       [Opciones]        |")
    print("+-------------------------+")
    print("|[1] Encripta tu texto    |")
    print("|[2] Desencripta tu texto |")
    print("|[0] Salir                |")       
    print("+-------------------------+")
    r = int(input("> "))

    while r !=0:

        if r ==1:
            print("[Ingrese el texto a codificar]")
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

            print(">", cifrado)

        elif r == 2:
            print("[Ingrese el texto a decodificar]")
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

            print("> ", cifrado)

        else:
            print("[Opcion no valida]")

        r = int(input("[Opcion]: "))

elif y ==5:
    print("+-------------------------+")
    print("|       [Opciones]        |")
    print("+-------------------------+")
    print("|[1] Encripta tu texto    |")
    print("|[2] Desencripta tu texto |")
    print("|[0] Salir                |")       
    print("+-------------------------+")
    fe = int(input("> "))

    while fe !=0:
        
        if fe ==1:
            clave = Fernet.generate_key()
            print("Esta es tu key")
            print(clave)
            print("+--------------------+")
            print("|Ingresa tu mensaje  |")
            print("+--------------------+")
            b = input("")
            mensaje = b.encode()

            f = Fernet(clave)

            encriptado = f.encrypt(mensaje)
            print("+-------------------+")
            print("|Texto encriptado   |")
            print("+-------------------+")
            print(encriptado)
        elif fe ==2:
            print("+----------------+")
            print("|Ingresa la key  |")
            print("+----------------+")
            key = input(">");
            print("+----------------+")      
            print("|Texto encriptado|")
            print("+----------------+")
            text= input(">");

            key = bytes(key,encoding="utf-8")
            text = bytes(text,encoding="utf-8")

            f2 = Fernet(key)

            f = f2.decrypt(text)
            print("+====================+")
            print("+ Texto desencriptado+")
            print("+====================+")
            print(f)
            #muchas gracias a Jesus David Clavijo por ayudarme en esta parte:)

        else:
            print("[Opcion no valida]")

        fe = int(input("[Opcion]: "))

elif y ==6:
    input("Preciona [Enter] para finalizar.")
        

                

    
        


    

