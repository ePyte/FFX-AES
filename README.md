# About this project
FFX-AES is a format preserving, Feistel based encryption method group which also uses AES (Advanced Encryption Standard).
This project is one implementation of this method using python.
Source: [NIST site](https://csrc.nist.gov/csrc/media/projects/block-cipher-techniques/documents/bcm/proposed-modes/ffx/ffx-spec.pdf)

# Details
Format preserving means that the encrypted message has the same amount of characters, like the plaintext.

Both of these strings - message (plaintext) and encrypted message - contain only '1' and '0' characters. Radix is 2.

The ```ffx.py``` file contains the class of implementation: FFX.

For the AES the Crypto.Cipher library has been used with a constant key. Source: [AES CBC-MAC](https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html#ccm-mode)

(Necessary command: ```pip install pycryptodome```)


# Testing
1. The test_ffx.py file contains the unit test.
    - 3 encryption - decription check
    - 3 exception check
    - 1 subTest of encryption - decription check
    - 1 subTest of exception check

    (The last two functions are the shorter format of the first two.)
    
    Commands:
    ```python -m unittest test_ffx.py``` or 
    ```python test_ffx.py```

2. This program (```main.py```) also contains 3 examples presenting the function of the code.
Please see one code end result example:

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
    Encrypted message:
    01101101
    1. result
    Decrypted message:
    11110000
    True
    ```

Command: ```python main.py```

# Built with
- Programming language: Python version 3.11.9
- Opertaing system: Microsoft Windows 10 (10.0.19045)



