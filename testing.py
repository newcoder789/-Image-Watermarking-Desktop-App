# from PIL import Image
#
# im = Image.open('stock-photo.jpg')
#
# print(im.format, im.size, im.mode)
# im.show()
import os, sys
from PIL import Image

# size = (128, 128)


# def convert_to_thumbnail(infile):
#     outfile = os.path.splitext(infile)[0] + ".thumbnail"
#     if infile != outfile:
#         try:
#             with Image.open(infile) as im:
#                 im.thumbnail(size)
#                 im.save(outfile, "JPEG")
#         except OSError:
#             print("cannot create thumbnail for", infile)


from PIL import Image, ImageFilter

im = Image.open('stock-photo.jpg')
im2 = Image.open('dogo.jpg')
print(im.size)


''' upper left corner is 0,0 
also coordinate are like (left, upper, right, lower)
so image shown will be like right-left
'''

# box = (100, 100, 2000, 2000)
# region = im.crop(box)
# region.show()


'''
rolling an image right is like 
I M A G E -----  M A G E I
'''


# def roll(im, delta):
#     """Roll an image sideways."""
#     xsize, ysize = im.size
#
#     delta = delta % xsize
#     if delta == 0:
#         return im
#
#     part1 = im.crop((0, 0, delta, ysize))
#     part2 = im.crop((delta, 0, xsize, ysize))
#     im.paste(part1, (xsize - delta, 0, xsize, ysize))
#     im.paste(part2, (0, 0, xsize - delta, ysize))
#
#     return im
#
#
# j = roll(im, 100)
# j.show()



'''
how to merge image 
'''
#
# def merge(im1, im_2):
#     nw_2 = im_2.resize((700, 400))
#     w = im1.size[0] + nw_2.size[0]
#     h = max(im1.size[1], nw_2.size[1])
#     im = Image.new("RGBA", (w, h))
#
#     im.paste(im1)
#     im.paste(nw_2, (3450, 1110))
#
#     return im
#
#
# j = merge(im, im2)
# j.show()



'''
how to blur and all 
'''
# im1 = im.filter(ImageFilter.BLUR)
# im1.show()
# im_2 = im.filter(ImageFilter.BoxBlur(11))
# im_2.show()

'''
imagedraw 
useful as fuckkk
'''

# import sys
# from PIL import Image, ImageDraw
#
# with Image.open("dogo.jpg") as im:
#
#     draw = ImageDraw.Draw(im)
#     draw.line((0, 0) + im.size, fill=128)
#     draw.line((0, im.size[1], im.size[0], 0), fill=128)
#
#     # write to stdout
#     im.save("editedfile", "JPEG")

# import os
# from PIL import Image, ImageDraw
#
# # Print the current working directory
# print("Current working directory:", os.getcwd())
# def hello(i):
#     try:
#         draw = ImageDraw.Draw(i)
#         draw.line((0, 0) + i.size, fill=128)
#         draw.line((0, i.size[1], i.size[0], 0), fill=128)
#         i.save("output.jpg", "JPEG")
#         print("Image saved successfully!")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# from PIL import Image, ImageDraw, ImageFont
#
# # get an image
# with Image.open("dogo.jpg").convert("RGBA") as base:
#     x, y = base.size
#
#     # make a blank image for the text, initialized to transparent text color
#     txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
#
#     # get a font
#     fnt = ImageFont.truetype("Libre_Baskerville,Martel_Sans,Pacifico/Pacifico/Pacifico-Regular.ttf", 200)
#     # get a drawing context
#     d = ImageDraw.Draw(txt)
#
#     # draw text, half opacity
#     d.text((x/4, y/2), "Hello", font=fnt, fill=(255, 255, 255, 255))
#     # draw text, full opacity
#     d.text((x/2, y/2), "World", font=fnt, fill=(255, 255, 255, 255))
#
#     out = Image.alpha_composite(base, txt)
#
#     out.show()


# from PIL import Image, ImageDraw, ImageFont
im = Image.open('stock-photo.jpg').convert("RGBA")
x,y = im.size
# blank_im = Image.new("RGBA", im.size, (255, 255, 255, 0))
# d = ImageDraw.Draw(blank_im)                                                        
# num_lines = 10
# spacing = min(x, y) // (num_lines - 1)
# # for i in range(0,x):
# # Draw the lines
# for i in range(num_lines):
#     offset = i * spacing
#     # Draw diagonal lines
#     d.line((offset, 0, 0, offset), fill=(128, 128, 128, 255), width=2)  # From top-left to bottom-right
#     d.line((x, offset, x - offset, 0), fill=(128, 128, 128, 255), width=2)# Diagonal line from bottom-left to top-right

#     # i += x/2
# out = Image.alpha_composite(im, blank_im)
# out.show()

imgg = Image.open('stock-photo2.jpg').convert("RGBA")
watermark_img = Image.open("dogo.jpg").convert("RGBA")
watermark = watermark_img.resize((x // 4, y // 4), Image.LANCZOS)
position = (x - watermark.width - 10, y - watermark.height - 10)  # Bottom right corner
imgg.paste(watermark, position, watermark)
imgg.show()
if __name__ == '__main__':
    pass

