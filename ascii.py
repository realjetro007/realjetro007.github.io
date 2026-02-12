from PIL import ImageOps, ImageEnhance

def ascii_art(img, width, bgcolour, brightness, contrast, aspratm):
    img= img.convert('L')
    img = ImageOps.autocontrast(img)

    img = ImageEnhance.Contrast(img).enhance(contrast)
    img = ImageEnhance.Brightness(img).enhance(brightness)

    aspect_ratio = img.height / img.width
    height = int(aspect_ratio * width * aspratm) #0.55 works well for most images but I've had trouble with some images getting stretched

    img = img.convert("1")
    img = img.convert("L")  #This applies Floyd-Steinberg Dithering

    img = img.resize((width, height))
    pixels=list(img.getdata())

    if bgcolour == "White":     #This changes depending on whether colour is inverted
        shades = " .:-=+*#%@"
    else:
        shades=r'''@%#*+=-:. '''

    chars = [shades[p * (len(shades)-1) // 255] for p in pixels]

    ascii_image = ''''''
    for i in range(0, len(chars), width):
        line = "".join(chars[i:i+width])    #This joins each line of art together to make the full image
        ascii_image += line + "\n"


    return ascii_image

