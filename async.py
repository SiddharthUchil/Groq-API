import asyncio
from groq import AsyncGroq

async def main():
    client = AsyncGroq()

    stream = await client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Explain the importance of low latency LLMs",
            }
        ],
        model="mixtral-8x7b-32768",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stop=None,
        stream=True,
    )

    async for chunk in stream:
        print(chunk.choices[0].delta.content, end="")

asyncio.run(main())