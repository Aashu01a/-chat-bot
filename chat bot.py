#install with pip install google-generativeai
from urllib import response
import google.generativeai as ai
# API Key
API_KEY = 'AIzaSyAciiJmeNiN4_6OKMxfLXf5bXku990EIDE'

# configure the API
ai.configure(api_key=API_KEY)

#create a new model
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

# start a conversation
while True:
    message = input('You: ')
    if message.lower() == 'bye':
        print('chatbot: bui bui!')
        break
    respone = chat.send_message(message)
    print('chatbot:', response.text)