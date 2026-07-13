from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = ChatMistralAI(model_name = "mistral-small-2506", temperature= 0.8)

messages = []
messages.append(SystemMessage(content = "Be a friendly, humorous AI. Use emojis in every reply and light sarcasm when it fits."))

print("Welcome😊")
print("To Exit the chat type 0")
while True:
    prompt = input("You :")
    messages.append(HumanMessage(content = prompt))
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content = response.text))
    print(f"AI: {response.text}\n")
    
        


