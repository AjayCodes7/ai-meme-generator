# function definitions 
def insert_newlines(text, max_chars=45):
    words = text.split()
    lines = []
    current_line = ''
    for word in words:
        if len(current_line) + len(word) <= max_chars:
            current_line += ' ' + word
        else:
            lines.append(current_line.strip())
            current_line = word
    lines.append(current_line.strip())  # Add the remaining part
    return '\n'.join(lines)

#<================================ Image Generation ======================================>

import requests
from authtoken import auth_token
import io
from PIL import Image

# API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {auth_token}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

#Generates and saves the image in image.jpg file
def generateImage(userInput):
    image_bytes = query({
        "inputs": userInput,
    })
    image = Image.open(io.BytesIO(image_bytes))
    image.save("D:\Mini Project\Flask Framework\static\images\image.jpg")
    print("Image Generated!!!")
    return 1

#<================================ Image Generation ======================================>


#<=================================== Combination ========================================>
from PIL import Image, ImageDraw, ImageFont

def generate_meme(image_path, text, output_path):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    font_path = "D:\Mini Project\Flask Framework\Anton-Regular.ttf"  # Change the font path to your preferred font
    font_size = 50
    font = ImageFont.truetype(font_path, font_size)

    text_width, text_height = draw.textsize(text, font=font)

    x = (img.width - text_width) / 2
    y = img.height - text_height - 20
    draw.rectangle([(0, img.height - text_height - 30), (img.width, img.height)], fill="black")
    draw.text((x, y), text, fill="white", font=font)
    img.save(output_path)
    return


#<=================================== Combination ========================================>

#<============================== Meme Text Generation ====================================>
import json
from authtoken import OPEN_AI_KEY

# Not WOrking Here
# from dotenv import load_dotenv
# load_dotenv()
from openai import OpenAI
client = OpenAI(api_key=OPEN_AI_KEY)

def generateMeme(GPTInput):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are a creative meme generater.You create funny memes and generate output in JSON. The json includes 'image_description','meme_text'"},
        {"role": "user", "content": GPTInput}
    ]
    )
    output = response.choices[0].message.content
    json_output = json.loads(output)
    json_output['meme_text'] = insert_newlines(json_output['meme_text'], max_chars=45)
    print("Image :",json_output['image_description'])
    print("Text :",json_output['meme_text'])
    success = 0
    print("Calling Image Generation Function!!")
    success = generateImage(json_output['image_description'])
    print("Returned from Image Generation Function!!")
    if success:
        print("GPTWork Done!!!")
        generate_meme("D:\Mini Project\Flask Framework\static\images\image.jpg",json_output['meme_text'],"D:\Mini Project\Flask Framework\static\images\output.jpg")
        return 1

#<============================== Meme Text Generation ====================================>

# main program 

from flask import Flask, render_template, url_for, request

app = Flask(__name__)
default_image = 'default.jpg'
@app.route('/')
def index():
    return render_template("index.html",image_path='output.jpg')

@app.route('/submit', methods=['POST'])
def submit():
    try:    
        user_input = request.form['user_input']
        success = generateMeme(user_input)
        if success:
            return render_template('index.html', image_path='output.jpg')
    except:
        return render_template('index.html', error_message='something went wrong!')



if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception:
        render_template('index.html', image_path='output.jpg')