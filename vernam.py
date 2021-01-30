def vernam(key):
    

            f = open("e:/4th CSE/Vernam/vernam_plain.txt", "r")
            plain=f.read()
            plain=plain.split("\n")

            #print(plain)

            p= open("e:/4th CSE/Vernam/vernam_enc.txt", "a")
            p.write("key="+key+"\n")
            
            
            for line in plain:
                result=""
                for i in range(len(line)):
                    result+= chr((ord(line[i])-65 ^ ord(key[i])-65) %26+65)
                p.write(result)
                p.write("\n")
            p.close()
                         
               

if __name__=="__main__":
    vernam("SPARTANS")               