from PIL import Image, ImageFilter, ImageFont, ImageDraw

im = Image.open('stock-photo.jpg')
im2 = Image.open('dogo.jpg')



def watermarked_image(ima, blur_density=6, font_size=100, font_text="Made by Aryan Dixit", ):
    product1 = ima.filter(ImageFilter.BoxBlur(blur_density))
    base = product1.convert("RGBA")
    x, y = base.size

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

    # get a font
    fnt = ImageFont.truetype("Libre_Baskerville,Martel_Sans,Pacifico/Pacifico/Pacifico-Regular.ttf", font_size)
    # get a drawing context
    d = ImageDraw.Draw(txt)


    d.text((x-(x / 4), y-(y / 8)), font_text, font=fnt, fill=(255, 255, 255, 255))

    product2 = Image.alpha_composite(base, txt)
    product2.show()


watermarked_image(im)
