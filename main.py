from ffx import FFX

print("1. example")
plaintext = "11110000"
tweaks = ""
ffx_1 = FFX(tweaks, plaintext)
ffx_1.encrypt()
print("1. result")
print(plaintext == ffx_1.decrypt())
print("\n")


print("2. example")
plaintext = "111100000101010101010101111100000"
tweaks = "01"
ffx_2 = FFX(tweaks, plaintext)
ffx_2.encrypt()
print("2. result")
print(plaintext == ffx_2.decrypt())
print("\n")


print("3. example")
plaintext = "10100101100110001011001100001000011110111011111011000001111100000010100110101010101101000011111000100000110101101111111110001110"
tweaks = "0110100101111100"
ffx_3 = FFX(tweaks, plaintext)
ffx_3.encrypt()
print("3. result")
print(plaintext == ffx_3.decrypt())
print("\n")