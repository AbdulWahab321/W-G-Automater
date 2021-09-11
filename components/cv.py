from msgboxpy import *
from PIL import Image
import os

def get_id_from_invite_link(invite_link=""):
    if "https://chat.whatsapp.com/" not in invite_link:
        alert("Incorrect Invite Link",Styles.Icons.ICON_ERROR," IILx255")
    else:    
        invite_link = invite_link.replace("https://chat.whatsapp.com/","")
        return invite_link



def image_to_ascii_art(img_path: str,output_file: str = "pywhatkit_asciiart") -> str:
    """Converts the given image to ascii art and save it to output_file"""

    # pass the image as command line argument
    img = Image.open(img_path)

    # resize the image
    width, height = img.size
    aspect_ratio = height / width
    new_width = 80
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((500,500))
    # new size of image
    # print(img.size)

    # convert image to greyscale format
    img = img.convert('L')

    pixels = img.getdata()

    # replace each pixel with a character from array
    chars = ["*", "?", ".", "#", "!", "@", "$", "&", "%", "~", "`"]
    new_pixels = [chars[pixel // 25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    # split string of chars into multiple strings of length equal to the new width and create a list
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width]
                   for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)


    with open(f"{output_file}", "w") as f:
        f.write(ascii_image)                                   
    return ascii_image