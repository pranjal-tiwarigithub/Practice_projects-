from string import  ascii_uppercase

def substition(plainText,key):
    def PTmodification(pt):
        for x in pt:
            if ord(x)<65 or ord(x)>90:
                pt=pt.replace(x,'')
        return pt

    plainText=PTmodification(plainText)

    def keyModification(pt,key):
        pad=len(pt)%len(key)
        padding=""
        for i in range(0,pad):
            padding+=chr(65+i)


        blocks=len(pt)//len(key)
        newkey=key*blocks

        midindx=len(newkey)//2
        newkey=newkey[:midindx]+padding+newkey[midindx:]
        return newkey


    key=keyModification(plainText,key)        

    cipherText1=''
    for (pt,k) in zip(plainText,key):
        cipherIndex=(ascii_uppercase.index(pt) + ascii_uppercase.index(k)) % 26
        cipherText1+=ascii_uppercase[cipherIndex]

    return cipherText1

def permutaion(cipherText1, key):
    pad=len(cipherText1)%len(key)
    colSize=pad

    matrix=[]

    for i in range(colSize):
        matrix.append([])

    rowNum=0
    for x in cipherText1:
        matrix[rowNum].append(x)
        rowNum+=1
        if rowNum == pad:
            rowNum=0

    fixLen=len(matrix[0])
    for col in matrix:
        if len(col)!=fixLen:
            col.append("#")

    temp =[]
    temp= matrix[0]
    matrix[0]=matrix[-1]
    matrix[-1]=temp

    cipherText2=""
    for col in matrix:
        for x in col:
            cipherText2+=x

    return cipherText2


