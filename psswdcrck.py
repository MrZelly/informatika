from hashlib import sha256

def key_cracking(hashed: str) -> str:
    # 97 az 122
    prve = 97
    druhe = 97
    tretie = 97
    stvrte = 97
    test = chr(prve)+chr(druhe)+chr(tretie)+chr(stvrte)
    for i in range(88529281):
        if(sha256(test.encode()).hexdigest() == hashed):
            return(test)
        else:
            stvrte += 1
            if(stvrte > 122):
                tretie += 1
                stvrte = 97
                if(tretie > 122):
                    druhe += 1
                    tretie = 97
                    if(druhe > 122):
                        prve += 1
                        druhe = 97
                        if(prve > 122):
                            return("failed")
        test = chr(prve)+chr(druhe)+chr(tretie)+chr(stvrte)


# Verejné testy:
print(key_cracking("a746222f09d85605c52d4e636788d6ffdc274698b98b8c5f3244c06958683a69"))  # snow
print(key_cracking("e6ad06ca7b0a33fbb0ea8d52e482eacca927a5735101bd2a0712d2f230233089"))  # iglu