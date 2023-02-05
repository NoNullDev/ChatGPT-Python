import openai
import os

# Autenticando e carregando o modelo GPT-3
openai.api_key = ""

conversation_history = ""

def generate_response(prompt):
    completions = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=500,
        top_p=0.9,
        frequency_penalty=0.2,
        presence_penalty=0.5,
)

    message = completions.choices[0].text
    return message.strip()


os.system("clear")
while True:
    user_input = input("-> ")
    if user_input == "exit":
        break
    
    conversation_history += user_input + '\n\n'
    try:
        response = generate_response(conversation_history)
        conversation_history += response + '\n\n'
        print(response)
    except: 
        print("An error has occurred!")
        print("Please, restart to continue (ctrl-c)")
    print("____________________________________")