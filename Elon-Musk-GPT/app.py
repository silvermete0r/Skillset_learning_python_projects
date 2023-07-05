import openai

# Настройка ключа OpenAI API
openai.api_key = 'YOUR_API_KEY'

# Функция Elon Musk GPT
def elon_musk_gpt(message):
    user_message = "User: " + message

    chatbot_message = """
    - Elon Musk GPT is a language model trained to chat like Elon Musk.
    - Act as Elon Musk, CEO of Tesla and SpaceX.
    """

    chat_history = chatbot_message + user_message

    # Вызываем функция для получения ответа от GPT
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=chat_history,
        max_tokens=50,
        temperature=0.8,
        top_p=1.0,
        n=1,
        stop=None,
        temperature_decay_rate=0.9
    )

    chatbot_reply = response.choices[0].text.strip().split("Elon Musk GPT: ")[1]

    return chatbot_reply

# Основная программа
while True:
    user_input = input("User: ")
    chatbot_response = elon_musk_gpt(user_input)
    print("Elon Musk GPT:", chatbot_response)