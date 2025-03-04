import unittest
from ffx import FFX

class TestFFX(unittest.TestCase):

    #Testing encryption - decription
    def test_FFX1(self):
        plaintext = "11110000"
        tweaks = ""
        ffx_1 = FFX(tweaks, plaintext)
        ffx_1.encrypt()
        self.assertEqual(ffx_1.decrypt(), plaintext)

    def test_FFX2(self):
        plaintext = "111100000101010101010101111100000"
        tweaks = "01"
        ffx_2 = FFX(tweaks, plaintext)
        ffx_2.encrypt()
        self.assertEqual(ffx_2.decrypt(), plaintext)

    def test_FFX3(self):
        plaintext = "10100101100110001011001100001000011110111011111011000001111100000010100110101010101101000011111000100000110101101111111110001110"
        tweaks = "0110100101111100"
        ffx_3 = FFX(tweaks, plaintext)
        ffx_3.encrypt()
        self.assertEqual(ffx_3.decrypt(), plaintext)

    # Testing exceptions
    def test_FFX_exception1(self):
        plaintext = "1"
        tweaks = ""
        with self.assertRaises(ValueError):
            FFX(tweaks, plaintext)

    def test_FFX_exception2(self):
        plaintext = "011111111000000001111111100000000111111110000000011111111000000001111111100000000111111110000000011111111000000001111111100000000"
        tweaks = "01010101"
        with self.assertRaises(ValueError):
            FFX(tweaks, plaintext)

    def test_FFX_exception3(self):
        plaintext = "201010101"
        tweaks = "01010101"
        with self.assertRaises(ValueError):
            FFX(tweaks, plaintext)




    #Same tests using subTests
    test_encryption = [("11110000", ""), 
                        ("111100000101010101010101111100000", "01"), 
                        ("10100101100110001011001100001000011110111011111011000001111100000010100110101010101101000011111000100000110101101111111110001110", "0110100101111100")]

    def test_FFX(self):
        for (plaintext, tweaks) in self.test_encryption:
            with self.subTest(plaintext=plaintext, tweaks = tweaks):
                ffx_p = FFX(tweaks, plaintext)
                ffx_p.encrypt()
                self.assertEqual(ffx_p.decrypt(), plaintext)


    test_exceptions = [("1","", ValueError),
                        ("011111111000000001111111100000000111111110000000011111111000000001111111100000000111111110000000011111111000000001111111100000000","01010101", ValueError),
                        ("201010101","01010101", ValueError)]

    def test_FFX_exception(self):
        for (plaintext, tweaks, exception) in self.test_exceptions:
            with self.subTest(plaintext=plaintext, tweaks = tweaks, exception = exception):
                        with self.assertRaises(exception):
                            FFX(tweaks, plaintext)

if __name__ == '__main__':
    unittest.main()
