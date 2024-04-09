from PIL import Image, ImageDraw, ImageFont

def generate_meme(image_path, text, output_path):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    font_path = "D:\Mini Project\Combine\Anton-Regular.ttf"  # Change the font path to your preferred font
    font_size = 50
    font = ImageFont.truetype(font_path, font_size)

    text_width, text_height = draw.textsize(text, font=font)
    x = (img.width - text_width) / 2
    y = img.height - text_height - 20

    draw.rectangle([(0, img.height - text_height - 30), (img.width, img.height)], fill="black")
    draw.text((x, y), text, fill="white", font=font)
    img.save(output_path)

# Example usage
image_path = "D:\Mini Project\Combine\image.jpg"
text = "MI trying to win their first IPL cup \nbe like"
output_path = "D:\Mini Project\Combine\output_meme.jpg"

generate_meme(image_path, text, output_path)
