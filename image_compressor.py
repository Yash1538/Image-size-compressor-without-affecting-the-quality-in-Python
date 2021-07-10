import PIL
from PIL import Image

name = input("Please enter the name of the image: ")
n = int(input("Choose the extension \n press '1' for jpg\n press '2' for jpeg \n press '3' for png\n"))


def myfun(n, b):
    print("For better quality please enter original dimensions of Image")
    width = int(input("Enter the width of the image: "))
    height = int(input("Enter The height of the image: "))
    name_tobe_saved = input("Please enter the name of the image to be saved: ")

    img = Image.open(n)
    img = img.resize((width, height), PIL.Image.ANTIALIAS)
    name_tobe_saved = name_tobe_saved+b
    img.save(name_tobe_saved)
    print("Operation Succesfull")


if n == 1:
    extention = ".jpg"
    name = name+extention
    print(name)
    myfun(name, extention)
elif n == 2:
    extention = ".jpeg"
    name = name+extention
    print(name)
    myfun(name, extention)
elif n == 3:
    extention = ".png"
    name = name+extention
    print(name)
    myfun(name, extention)
else:
    print("Please choose right extension")
