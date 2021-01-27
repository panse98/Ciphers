f = open("C:\\Users\hp\Desktop\caesar\caesar_plain.txt", "r")
#print(f.read())
p= open("C:\\Users\hp\Desktop\caesar\caesar_enc.txt", "w")
plain=f.read()

def caesar(plain,key):
        result=""
        
        
        #plain=f.read()

        for i in range(len(plain)): 
            char = plain[i] 
            
            if (char.isupper()): 
                result += chr((ord(char) + key-65) % 26 + 65) 
    
            
            else: 
                result += chr((ord(char) + key - 97) % 26 + 97) 
            #p= open("C:\\Users\hp\Desktop\caesar\caesar_enc.txt", "a")
        print(result)
        p.write(result)
            
        p.close()

   
#return result 

if __name__=="__main__":
    caesar(plain,3)
    #print(caesar(f,3))
    
