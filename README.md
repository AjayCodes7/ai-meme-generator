# **Project Description**
The AI Meme Generation project leverages Natural Language Processing (NLP) and computer vision
to automatically generate humorous memes. Users can input a prompt or context, and the system
uses GPT-based models for caption generation and image models (like Stable Diffusion or DALL-E) to
generate or select suitable images. The goal is to automate meme creation using advanced AI,
targeting content creation efficiency and creativity.

## How to run this thing?
Follow the below steps
1. Clone the respository
2. Install the required packages
   ```
      Flask==3.0.2
      requests==2.31.0
      Pillow==10.3.0
      openai==1.23.2
   ```
   > Any suitable versions at the time you installation
3. Create a python file called ```authtoken.py```
   Place your openAI key and Hugging face Access Token here.
   **Example**:
     ```
     auth_token = "Your-hugging-face-access-token"
     OPEN_AI_KEY = "Your-open-ai-key-here"
     ```
4. Here we go! Your setup is done. Run ```app.py```.
