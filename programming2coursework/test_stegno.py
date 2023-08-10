import unittest
from PIL import Image
from stegno import Stegno  # Assuming the main code file is named stegno.py

class TestStegno(unittest.TestCase):
    def setUp(self):
        self.stegno = Stegno()

    def test_genData(self):
        data = "Hello, World!"
        expected_output = [
            '01001000', '01100101', '01101100', '01101100',
            '01101111', '00101100', '00100000', '01010111',
            '01101111', '01110010', '01101100', '01100100',
            '00100001'
        ]
        self.assertEqual(self.stegno.genData(data), expected_output)

    def test_modPix(self):
        image = Image.new("RGB", (100, 100), color=(255, 255, 255))
        data = "Hello, World!"
        pixels = list(self.stegno.modPix(image.getdata(), data))
        self.assertEqual(len(pixels), len(data) * 3)

    def test_encode_enc(self):
    # Create a sample image to be used in the test
        image = Image.new("RGB", (100, 100), color=(255, 255, 255))
        data = "Hey!! there"
        self.stegno.encode_enc(image, data)
        image.save("output_image.png")
    
    # Generate the expected output image
        expected_output_image = Image.new("RGB", (100, 100), color=(255, 255, 255))
        expected_output_data = "Hey!! there"
        self.stegno.encode_enc(expected_output_image, expected_output_data)
    
    # Compare the generated image with the expected output image
        self.assertEqual(image, expected_output_image)


if __name__ == '__main__':
    unittest.main()
