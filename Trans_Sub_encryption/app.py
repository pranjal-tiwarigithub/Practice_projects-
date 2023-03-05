from encryption import permutaion, substition
import os
import streamlit as st


st.title("K076 K077 cryptographic system")
plainText = st.text_input('Please enter text here ')



clear = lambda: os.system('cls')


if plainText:
    #plainText=input("Enter plain text: ")
    plainText=plainText.upper()
    key="NMIMS"
    key=key.upper()

    cipherText1=substition(plainText,key)
    cipherText2=permutaion(cipherText1,key)

    print(cipherText2)

    st.error(cipherText2)

    password = st.text_input('Please enter Password here ' ,)

    #password=input("Enter password to start decrytion:  ")
    pass_="security"

    if password.upper() == pass_.upper():
        clear()
        from decryption import permutaionInverse, substitutionInverse
        #cipherText2_decrypt=input("Enter cipherText: ")

        cipherText2_decrypt = st.text_input('Please enter Ciphertext here ')

        if cipherText2_decrypt:
            cipherText1_decrypt=permutaionInverse(cipherText2_decrypt,key)
            plainText_decrypt=substitutionInverse(cipherText1_decrypt,key)

            st.success(plainText_decrypt)


            print(plainText_decrypt)




