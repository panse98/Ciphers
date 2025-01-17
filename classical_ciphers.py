import numpy as np


def caesar(text,key):
    result=""
            

    for i in range(len(text)): 
        char = text[i] 
                
        if (char.isupper()): 
            char=char.lower()
            result += chr((ord(char) + key - 97) % 26 + 97) 
        
                
        else: 
            result += chr((ord(char) + key - 97) % 26 + 97) 
                #p= open("C:\\Users\hp\Desktop\caesar\caesar_enc.txt", "a")
                #print(result)
    return result
                   



def caesar_files(key):

            f = open("Input Files/Caesar/caesar_plain.txt", "r")
#print(f.read())
            p= open("Output Files/caesar_enc.txt", "a")
            plain=f.read()
            p.write("key="+str(key)+"\n")

            result=""
            

            for i in range(len(plain)): 
                char = plain[i] 
                
                if char=="\n":
                    p.write("\n")
                elif (char.isupper()): 
                    char=char.lower()
                    result = chr((ord(char) + key - 97) % 26 + 97) 
        
                
                else: 
                    result = chr((ord(char) + key - 97) % 26 + 97) 
                #p= open("C:\\Users\hp\Desktop\caesar\caesar_enc.txt", "a")
                #print(result)
                    p.write(result)
            p.write("\n")
                
            p.close()


def hill(text,key):
     key=np.array(key)
     text=text.lower()
     while (len(text)) % np.shape(key)[0] > 0:
          text= text + 'X'
     text_vec=np.zeros((len(text), 1))
     result=""
     for i in range(len(text)):
            text_vec[i]=(ord(text[i])-97)     # because lowercase
     text_vec=np.reshape(text_vec,(-1,(np.shape(key)[0])))
     A=np.dot(key,text_vec.T)
     A=np.mod(A,26)
     A=A.T
        # convert numbers to letters
        
     A=np.reshape(A,(-1,1))
     for i in range( len(A)):
        A[i]=A[i]
            #print(A[i])
        result+=chr((A[i]%26)+65)
     return result





    
        


def hill_files(key):
    key=np.array(key)
    if key.shape==(2,2):
        f = open("Input Files/Hill/hill_plain_2x2.txt", "r")
        plain=f.read()
        plain=plain.split("\n")
       
    else:
        f = open("Input Files/Hill/hill_plain_3x3.txt", "r")
        plain=f.read()
        plain=plain.split("\n")
   
    
    
    for line in plain:
        result=""
        #print(len(line))
        while (len(line)) % np.shape(key)[0] > 0:
          line= line + 'X'
          #print(len(line))
          #print(line)
        line_vec=np.zeros((len(line),1))
         # convert letters to numbers
        for i in range(len(line)):
             line_vec[i]=(ord(line[i])-65)
        #print(line_vec)
        #reshape the line vector
        line_vec=np.reshape(line_vec,(-1,(np.shape(key)[0])))
        #print (line_vec)
        A=np.dot(key,line_vec.T)
        A=np.mod(A,26)
        A=A.T
        # convert numbers to letters
        
        A=np.reshape(A,(-1,1))
        #print(A)
        for i in range( len(A)):
            A[i]=A[i]
            #print(A[i])
            result+=chr((A[i]%26)+65)

        #print(result)
        if key.shape==(2,2):
             p= open("Output Files/hill_enc_2x2.txt", "a")
             p.write(result)
             p.write("\n")
        else:
            k= open("Output Files/hill_enc_3x3.txt", "a")
            k.write(result)
            k.write("\n")

            
        

        

      

    




    #for debugginggg###
    #a=np.array([[2,2,3],[1,1,3]])
    #print(np.shape(a)[0])
    #print(np.shape(a)[1])
    #print(np.multiply([[1,1],[2,2]],[1,1]))
        










def generate_key_matrix(k):
    
    letters = []
    temp = []
    key_matrix = np.zeros([1, 25])
    for i in range(26):
        if(i == 9): #j
            continue
        letters.append(i + 97)
    for i in range(len(k)):
        if(ord(k[i]) not in temp):
            temp.append(ord(k[i]))
    for i in range(25):
        if(letters[i] not in temp):
             temp.append(letters[i])
    for i in range(25):
        key_matrix[0][i] = temp[i]
    key_matrix = key_matrix.reshape([5,5])
    return key_matrix






def playfair(text,key):
     text=text.lower()
     
     key.lower()
     key = generate_key_matrix(key)
     result = ""
     text1= ""
     temp = text

     for i in range(len(temp) - 1):
            if (temp[i] == temp[i + 1] and i%2==0):
                text1 += temp[i] + "x"
            else:
                text1 += temp[i]
     text1 += temp[-1]

     if (len(text1) % 2 != 0):
            text1 += "x"

     for i in range(0, len(text1), 2):
            letter1 = ord(text1[i])
            letter2 = ord(text1[i + 1])
            if (letter1 == 106):
                letter1 -= 1
            if (letter2 == 106):
                letter2 -= 1
            p1,q1 = np.where(key == letter1)
            p2,q2= np.where(key == letter2)
            r1 = int(p1)
            c1 = int(q1)
            r2 = int(p2)
            c2 = int(q2)
            if (r1 == r2):
                result+= chr(int(key[r1][(c1 + 1) % 5])) + chr(int(key[r2][(c2 + 1) % 5]))
            elif (c1 == c2):
                result += chr(int(key[(r1 + 1) % 5][c1])) + chr(int(key[(r2 + 1) % 5][c2]))
            else:
                result += chr(int(key[r1][c2])) + chr(int(key[r2][c1]))
     return result





def playfair_files(key):
    f = open("Input Files/PlayFair/playfair_plain.txt", "r")
    plain=f.read()
    plain=plain.split("\n")
    #print(plain)
    p= open("Output Files/playfair_enc.txt", "a")
    
    key = generate_key_matrix(key)

    for line in plain:
        result = ""
        text= ""
        temp = line

        for i in range(len(temp) - 1):
            if (temp[i] == temp[i + 1] and i%2==0):
                text += temp[i] + "x"
            else:
                text += temp[i]
        text += temp[-1]

        if (len(text) % 2 != 0):
            text += "x"

        for i in range(0, len(text), 2):
            letter1 = ord(text[i])
            letter2 = ord(text[i + 1])
            if (letter1 == 106):
                letter1 -= 1
            if (letter2 == 106):
                letter2 -= 1
            p1,q1 = np.where(key == letter1)
            p2,q2= np.where(key == letter2)
            r1 = int(p1)
            c1 = int(q1)
            r2 = int(p2)
            c2 = int(q2)
            if (r1 == r2):
                result+= chr(int(key[r1][(c1 + 1) % 5])) + chr(int(key[r2][(c2 + 1) % 5]))
            elif (c1 == c2):
                result += chr(int(key[(r1 + 1) % 5][c1])) + chr(int(key[(r2 + 1) % 5][c2]))
            else:
                result += chr(int(key[r1][c2])) + chr(int(key[r2][c1]))

        p.write(result)
        p.write('\n')
    p.close()



def vernam(text,key):
    result=""
    for i in range(len(text)):
        result+= chr((((ord(text[i])-65) + (ord(key[i])-65)) %26)+65)
    return result


def vernam_files(key):
    

            f = open("Input Files/Vernam/vernam_plain.txt", "r")
            plain=f.read()
            plain=plain.split("\n")

            #print(plain)

            p= open("Output Files/vernam_enc.txt", "a")
            p.write("key="+key+"\n")
            
            
            for line in plain:
                result=""
                for i in range(len(line)):
                    result+= chr((((ord(line[i])-65) + (ord(key[i])-65)) %26)+65)
                p.write(result)
                p.write("\n")
            p.close()


def vigenere(text,k,mode):
    text=text.lower()
    k=k.lower()
    result=""
    key=""

                #print(line)
    if mode=="1": #auto
        print(mode)
        for i in range(len(text)-len(key)):
         key=k+text
        print(key)
                     #print(key)
    else: # repeaating
                    #print(len(line))
                    #print(len(key))
        for i in range(len(text)-len(key)):
            key=key+k
    for i in range(len(text)):
        result+=chr((ord(text[i])-97 + ord(key[i]) - 97) % 26 + 97)
    return result
               

                         
               
def vigenere_files(k,mode):
    

            f = open("Input Files/Vigenere/Vigenere_plain.txt", "r")
            plain=f.read().lower()
            plain=plain.split("\n")

            #print(plain)

            p= open("Output Files/Vigenere_enc.txt", "a")
           
            p.write("key="+k+"\n")
            
            
            for line in plain:
                result=""
                key=""

                #print(line)
                if mode==True: #auto
                    #for i in range(len(line)-len(key)):
                     key=k+line
                     #print(key)
                else: # repeaating
                    #print(len(line))
                    #print(len(key))
                    for i in range(len(line)-len(key)):
                        key=key+k
                for i in range(len(line)):
                    result+=chr((ord(line[i])-97 + ord(key[i]) - 97) % 26 + 97)
                p.write(result)
                p.write("\n")
            p.close()
                    
            #print(result) 

    
#return result 

if __name__=="__main__":

    caesar_files(3)
    caesar_files(6)
    caesar_files(12)

    hill_files(np.array([[5, 17], [8, 3]]))
    hill_files( np.array([[2, 4, 12], [9, 1, 6], [7, 5, 3]]))
    
    playfair_files("rats")
    playfair_files("archangel")

    vernam_files("SPARTANS")   

    vigenere_files("pie",False)
    vigenere_files("aether",True)



    while(1):
        plain_text=input("Enter plain text\n")
        caesar_key=int(input("Enter caesar key\n"))
        print(caesar(plain_text,caesar_key))
      
        hill_keysize=int(input("Enter hill cipher key size\n")) # as it's a square matrix
        hill_values=list(map(int, input("Enter matrix values per row in one line separated by space \n").split())) 
        hill_matrix = np.array(hill_values).reshape(hill_keysize, hill_keysize) 
        print(hill_matrix) 
        print(hill(plain_text,hill_matrix))

        playfair_key=(input("Enter playfair key\n"))
        print(playfair(plain_text,playfair_key))
        vernam_key=input("Enter vernam key\n")
        print(vernam(plain_text,vernam_key))
      
        vigenere_mode=(input("Enter vigenere mode 1 for auto and 0 for repeating"))
        vigenere_key=input("Enter vigenere key\n ")
        print(vigenere(plain_text,vigenere_key,vigenere_mode))










                

   
    