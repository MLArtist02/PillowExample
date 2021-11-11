from PIL import Image, ImageDraw, ImageFont

# Pillow
# https://pillow.readthedocs.io/en/stable/installation.html

if __name__ == "__main__":
    # square image 640x640 pixels
    width = 640
    height = 640

    image = Image.new('RGB', (width, height), "black")
    draw = ImageDraw.Draw(image)

    # 1st arg = [x0, y0, x1, y1]
    draw.rectangle((20,20,width-20,height-20), fill="blue")

    # draw hello world!
    font = ImageFont.truetype("arial.ttf", 60)
    draw.multiline_text((250,250), "Hello\nWorld!", font=font, fill="white", )

    image.save("hello_world_pillow_img.png")   