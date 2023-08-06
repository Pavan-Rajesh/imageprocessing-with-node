
# import sys
# import pandas as pd

# # Takes first name and last name via command
# # line arguments and then display them
# print("Output from Python")

# x = []


# for i in range(100):
#     x.append(i)
# print(x)

# # save the script as hello.py


# dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
 
# # Creating series of Dictionary type
# sd = pd.Series(dictionary)

# # print(sd)

# from PIL import Image
imagePath = "E:\imagesprac\sponge.png"
# #Open Image
# im = Image.open(imagePath)
# x = im.tobytes()
# print(x)

from PIL import Image
# Open the image file
# with open(imagePath, "rb") as f:
#     image = Image.open(f)
import base64
# # Convert the image to base64 format
# with open(imagePath, "rb") as f:
#     encoded_image = base64.b64encode(f.read())



spongeGray = Image.open(imagePath).rotate(45)
# encoded_image = base64.b64encode(spongeGray.tobytes())

spongeGray.save('grayspong.png')
with open('grayspong.png', "rb") as f:
    encoded_image = base64.b64encode(f.read())


print(encoded_image.decode('utf-8'))