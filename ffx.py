from Crypto.Cipher import AES
import math
import random

class FFX:
    def __init__(self, tweaks, plaintext):
        self.radix = 2
        self.validChars = ["0","1"]
        self.minLength = 8
        self.maxLength = 128
        self.key = self.strToHexString("0010001011000001") #16 byte -> 8*16 = 256 bit

        #Plaintext check
        if((self.minLength > len(plaintext)) or (len(plaintext) > self.maxLength)):
            raise ValueError("Invalid length of plaintext.")
        elif(self.checkContaindedChars(plaintext)):
            raise ValueError("Plaintext contains invalid characters.")
        else:
            self.plaintext = self.strToHexString(plaintext)

        self.tweaks = self.strToHexString(tweaks)
        self.addition = 0 #characterwise xor
        self.method = 2 # alternating Feistel
        self.lengthOfPlaintext = len(plaintext)
        self.split = math.floor(self.lengthOfPlaintext/2)
        self.rnds = self.rndsFunc(self.lengthOfPlaintext)

        self.ciphertext = b''
        self.resultEnc = b''
        self.resultDec = ""
        self.nonce = []
        self.initNonce()


    def checkContaindedChars(self, plaintext):
        for i in range(len(plaintext)):
            if (plaintext[i] not in self.validChars):
                return True
        return False


    def strToHexString(self, text): #"10" -> b'\x01\x00'
        c = b''
        for i in text:
            c +=bytes([int(i)])
        return c


    def initNonce(self):#preaparing a list containing the nonces; 36 elements, because the rnds function defines max 36 rounds
        for i in range(36):
            c =''
            for j in range(11):# AES CBC-MAC: https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html#ccm-mode
                c += str(random.randint(0,1))
            self.nonce.append(self.strToHexString(c))


    def rndsFunc(self, lengthOfPlaintext):
        if (8<=lengthOfPlaintext and lengthOfPlaintext<=9):
            return 36
        elif (10<=lengthOfPlaintext and lengthOfPlaintext<=13):
            return 30
        elif (14<=lengthOfPlaintext and lengthOfPlaintext<=19):
            return 24
        elif (20<=lengthOfPlaintext and lengthOfPlaintext<=31):
            return 18
        elif (32<=lengthOfPlaintext and lengthOfPlaintext<=128):
            return 12


    def encrypt(self):
        A = self.plaintext[:self.split]
        B = self.plaintext[self.split:]

        for i in range(self.rnds):
            F = self.fkFunc(i,B)
            C = self.xorFunc(A, F)
            A = B
            B = C

        print("Encrypted message:")
        self.resultEnc = A + B
        #print("Hex form:")
        #print(self.resultEnc.hex())
        #print(self.resultEnc)
        strFormEnc = self.hexToStr(self.resultEnc.hex())
        print(strFormEnc)


    def hexToStr(self, textToConvert): #"0100" -> "10"
        resultText = ""
        for i in range(0, len(textToConvert), 2):
            resultText += str(textToConvert[i+1])
        return resultText


    def xorFunc(self, A, F):
        C = b""
        if (len(A) != len(F)):
            print("Error: lengths are different.")
        C=bytes(a ^ b for a, b in zip(A, F))
        return C


    def fkFunc(self, i, B):
        t = len(self.tweaks)
        P = self.pFunc(t)
        Q = self.qFunc(i, t, B)

        PQ = P+Q
        Y = self.AESEncAndSplit(PQ, i)

        return self.strToHexString(Y)


    def pFunc(self, t):
        vers = 1
        P = (
        self.strToHexString(self.toStringBinaryPadded(vers, 2)) + 
        self.strToHexString(self.toStringBinaryPadded(self.method, 1)) + 
        self.strToHexString(self.toStringBinaryPadded(self.addition, 1)) +
        self.strToHexString(self.toStringBinaryPadded(self.radix, 1)) +
        self.strToHexString(self.toStringBinaryPadded(self.lengthOfPlaintext, 1)) +
        self.strToHexString(self.toStringBinaryPadded(self.split, 1)) +
        self.strToHexString(self.toStringBinaryPadded(self.rnds, 1)) +
        self.strToHexString(self.toStringBinaryPadded(t, 8)))

        return P


    def qFunc(self, i, t, B):
        exponentQ1 = (-t - 9) % 16
        exponentQ2 = 64 - len(B)
        Q = (self.tweaks + 
        self.strToHexString(self.toStringBinaryPadded(0, exponentQ1)) +
        self.strToHexString(self.toStringBinaryPadded(i, 1)) +
        self.strToHexString(self.toStringBinaryPadded(0, exponentQ2)) + 
        B)

        return Q


    def toStringBinaryPadded(sef, decNumber, lengthOct): #preparing the appropriate sized string conaining only 0s and 1s
        binNum = format(decNumber, 'b')
        padZeros=""
        for i in range(lengthOct*8-len(binNum)):
            padZeros+="0"
        resultString = padZeros + binNum

        return resultString


    def AESEncAndSplit(self, PQ, index):
        cipher = AES.new(self.key, AES.MODE_CCM, self.nonce[index])
        #print(PQ)
        ciphertext, tag = cipher.encrypt_and_digest(PQ)
        #print(tag)

        tagShorter = bin(int.from_bytes(tag))[2:]
        while(len(tagShorter)<128):
            tagShorter = '0' + tagShorter
        #f'{int.from_bytes(tag):0128b}' # simplier form

        m = 0
        if ((index % 2) ==0):
            m = self.split
        else:
            m = self.lengthOfPlaintext-self.split
        Y = tagShorter[129-m-1:]

        return Y


    def decrypt(self):
        A = self.resultEnc[:self.split]
        B = self.resultEnc[self.split:]

        for i in reversed(range(self.rnds)):
            C = B
            B = A
            F = self.fkFunc(i,B)
            A = self.xorFunc(C,F)

        self.resultDec = A + B
        #print(self.resultDec)
        print("Decrypted message:")

        strFormDec = self.hexToStr(self.resultDec.hex())
        print(strFormDec)
        return strFormDec




