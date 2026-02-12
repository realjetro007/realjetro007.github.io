from PIL import Image, ImageOps, ImageEnhance

def ascii_art(img, width, bgcolour, brightness, contrast, aspratm):
    img= img.convert('L')
    img = ImageOps.autocontrast(img)

    img = ImageEnhance.Contrast(img).enhance(contrast)
    img = ImageEnhance.Brightness(img).enhance(brightness)

    aspect_ratio = img.height / img.width
    height = int(aspect_ratio * width * aspratm)

    img = img.convert("1")  # 1-bit black & white
    img = img.convert("L")

    img = img.resize((width, height))
    pixels=list(img.getdata())






    if bgcolour == "White":
        shades = " .:-=+*#%@"
    else:
        shades=r'''@%#*+=-:. '''

    chars = [shades[p * (len(shades)-1) // 255] for p in pixels]


    ascii_image = ''''''
    for i in range(0, len(chars), width):
        line = "".join(chars[i:i+width])
        ascii_image += line + "\n"


    return ascii_image

