from groq import Groq

client = Groq()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Count to 10.  Your response must begin with \"1, \".  example: 1, 2, 3, ...",
        }
    ],
    model="mixtral-8x7b-32768",
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    stop=", 6",
    stream=False,
)

print(chat_completion.choices[0].message.content)