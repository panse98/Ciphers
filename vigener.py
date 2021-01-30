
def vigenere(key,mode):
    

            f = open("e:/4th CSE/Vigenere/Vigenere_plain.txt", "r")
            plain=f.read()
            plain=plain.split("\n")
            #print(plain)

            p= open("e:/4th CSE/Vigenere/Vigenere_enc.txt", "a")
           
            p.write("key="+key+"\n")
            
            
            for line in plain:
                result=""
                #print(line)
                if mode==True: #auto
                    key=key+line
                else: # repeaating
                    #print(len(line))
                    #print(len(key))
                    for i in range(len(line)-len(key)):
                        key=key+key[i]
                for i in range(len(line)):
                    result+=chr((ord(line[i])-97 + ord(key[i]) - 97) % 26 + 97)
                p.write(result)
                p.write("\n")
                    
            print(result) 

        



                    



               
                    

                    
                
if __name__=="__main__":
    vigenere("abc",False)
                 

             



          
            