import numpy as np

def hill(key):
    key=np.array(key)
    if key.shape==(2,2):
        f = open("E:\\4th CSE\Hill\hill_plain_2x2.txt", "r")
        plain=f.read()
        plain=plain.split("\n")
       
    else:
        f = open("E:\\4th CSE\Hill\hill_plain_3x3.txt", "r")
        plain=f.read()
        plain=plain.split("\n")
   
    
    
    for line in plain:
        result=""
        #print(len(line))
        if (len(line)) % np.shape(key)[0] > 0:
          line= line + 'x'
          #print(len(line))
        line_vec=np.zeros((len(line),1))
         # convert letters to numbers
        for i in range(len(line)):
             line_vec[i]=(ord(line[i])-65)
        #print(line_vec)
        #reshape the line vector
        line_vec=np.reshape(line_vec,(-1,(np.shape(key)[0])))
        #print (line_vec)
        A=np.dot(key,line_vec.T)
        #print(A)
        # convert numbers to letters
        
        A=np.reshape(A,(-1,1))
        #print(A)
        for i in range( len(A)):
            A[i]=A[i]
            print(A[i])
            result+=chr((A[i]%26)+65)
        print(result)
        if key.shape==(2,2):
             p= open("E:\\4th CSE\Hill\hill_enc_2x2.txt", "a")
             p.write(result)
             p.write("\n")
        else:
            k= open("E:\\4th CSE\Hill\hill_enc_3x3.txt", "a")
            k.write(result)
            k.write("\n")

            
        

        

      

    




    #for debugginggg###
    #a=np.array([[2,2,3],[1,1,3]])
    #print(np.shape(a)[0])
    #print(np.shape(a)[1])
    #print(np.multiply([[1,1],[2,2]],[1,1]))
        






if __name__=="__main__":
    hill(np.array([[5, 17], [8, 3]]))

    hill( np.array([[2, 4, 12], [9, 1, 6], [7, 5, 3]]))
   
