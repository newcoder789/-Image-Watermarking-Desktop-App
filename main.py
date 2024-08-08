from PIL import Image, ImageFilter, ImageFont, ImageDraw

im = Image.open('stock-photo.jpg')
im2 = Image.open('dogo.jpg')



def watermarked_image(original_path="stock-photo.jpg", blur_density=10, font_size=100, font_text="Made by Aryan Dixit",  task=None, num_lines=10, watermark_img_path="dogo.jpg"):
    original = Image.open(original_path).convert("RGBA")
    x,y = original.size
    
    # blank_im = Image.new("RGBA", im.size, (255, 255, 255, 0))
    blank_im = Image.new('RGBA', original.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(blank_im)
    
    if task=="watermark_blur":
        original = original.filter(ImageFilter.BoxBlur(blur_density))
        # product = original
        # product.show()
        # return

    if task=="watermark_text":
        # get a font
        fnt = ImageFont.truetype("Libre_Baskerville,Martel_Sans,Pacifico/Pacifico/Pacifico-Regular.ttf", font_size)
        d.text((x-(x / 4), y-(y / 8)), font_text, font=fnt, fill=(255, 255, 255, 255))


    if task=="watermark_img":
        watermarking_img = Image.open(watermark_img_path).convert("RGBA")
        watermarkingg_img = watermarking_img.resize((x // 4, y // 4), Image.LANCZOS)
        position = (x - watermarkingg_img.width - 10, y - watermarkingg_img.height - 10)  # Bottom right corner
        blank_im.paste(watermarkingg_img, position, watermarkingg_img)
    
    if task=="watermark_lines":
        num_lines = num_lines
        spacing = min(x, y) // (num_lines - 1)
        for i in range(num_lines):
            offset = i * spacing
            d.line((offset, 0, 0, offset), fill=(128, 128, 128, 255), width=2)  # From top-left to bottom-right
            d.line((x, offset, x - offset, 0), fill=(128, 128, 128, 255), width=2)  # From top-right to bottom-left
    
    product = Image.alpha_composite(original, blank_im)
    
    product.show()
    
    


watermarked_image(task="watermark_lines")
