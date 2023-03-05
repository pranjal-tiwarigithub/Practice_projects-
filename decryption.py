from string import  ascii_uppercase

def CTmodification(ct):
        cleanCT=ct
        for x in ct:
            if ord(x)<65 or ord(x)>90:
                cleanCT=ct.replace(x,'')
        return cleanCT

def permutaionInverse(cipherText2,key):
       
    cleanCT=CTmodification(cipherText2)

    pad=len(cleanCT)%len(key)
    colSize=pad

    matrix=[]

    for i in range(colSize):
        matrix.append([])

    sizeOfCol=len(cipherText2)/pad
    
    i=0
    j=0
    for x in cipherText2:
        matrix[i].append(x)
        j+=1
        if j==sizeOfCol:
            j=0
            i+=1

    temp =[]
    temp= matrix[0]
    matrix[0]=matrix[-1]
    matrix[-1]=temp
    

    cipherText1=""
    for i in range(int(sizeOfCol)):  
        for j in range(colSize):   
            cipherText1+=matrix[j][i]

    return cipherText1

def substitutionInverse(cipherText1, key):

    cipherText1=CTmodification(cipherText1)

    def keyModification(ct,key):
            pad=len(ct)%len(key)
            padding=""
            for i in range(0,pad):
                padding+=chr(65+i)


            blocks=len(ct)//len(key)
            newkey=key*blocks

            midindx=len(newkey)//2
            newkey=newkey[:midindx]+padding+newkey[midindx:]
            return newkey

    key=keyModification(cipherText1,key)

    plainText=''
    for (ct,k) in zip(cipherText1,key):
        if ct == '#':
            continue
        cipherIndex=(ascii_uppercase.index(ct) - ascii_uppercase.index(k)) % 26
        plainText+=ascii_uppercase[cipherIndex]

    return plainText    



