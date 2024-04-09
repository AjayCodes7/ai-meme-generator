import requests
from authtoken import auth_token

API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
headers = {"Authorization": f"Bearer {auth_token}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content


image_bytes = query({
	"inputs": "BMW car",
})

# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))
image.save("D:\Mini Project\Flask Framework\static\images\image.jpg")
