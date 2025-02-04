# About this project
FFX-AES is a Format preserving, Feistel based encryption method group which also uses AES (Advanced Encryption Standard).
This project is one implementation of this method using python.
Source: [NIST site](https://csrc.nist.gov/csrc/media/projects/block-cipher-techniques/documents/bcm/proposed-modes/ffx/ffx-spec.pdf)

# Details
Format preserving means that the encrypted message has the same amount of characters, like the plaintext.
Both of these strings contains only '1' and '0' characters. Radix is 2.
For the AES the Crypto.Cipher libraray has been used with a constant key. Source: [AES CBC-MAC](https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html#ccm-mode)
This program contains 3 examples presenting the function of the code.

```
print("1. example")
plaintext = "11110000"
tweaks = ""
ffx_1 = FFX(tweaks, plaintext)
ffx_1.encrypt()
print("1. result")
print(plaintext == ffx_1.decrypt())
```

```
1. example
Encryped message:
01101101
1. result
Decryped message:
11110000
True
```

# Built with
- Programming language: Python version 3.11.9
- Opertaing system: Microsoft Windows 10 (10.0.19045)



