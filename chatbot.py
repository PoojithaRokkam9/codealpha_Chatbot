import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    (r"hi|hello|hey", ["Hello! How can I help you?", "Hi there!", "Hey!"]),
    (r"what is your name?", ["I'm a chatbot. What's yours?"]),
    (r"how are you?", ["I'm just a program, so I'm always fine! How about you?"]),
    (r"tell me about (.*)", ["Sure! What do you want to know about %1?"]),
    (r"quit", ["Goodbye! Have a great day!"])
]
chatbot=Chat(pairs,reflections)
def start_chat():
  print("Hi!I'm your chatbot.Type 'quit' to end the chat.")
  while True:
    user_input=input("You: ").lower()
    if user_input=="quit":
      print("Chatbot:Goodbye!have a great day")
      break
    else:
      response=chatbot.respond(user_input)
      print("Chatbot:",response)
start_chat()