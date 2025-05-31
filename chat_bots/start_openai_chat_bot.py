import asyncio
from openai import AsyncOpenAI
from utils.utils import get_api_key


async def ask_llm(question, client):
    try:
        response = await client.with_options(max_retries=5).chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"


async def chat_loop(client):
    print("Ask a question (type 'exit' to quit):")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        answer = await ask_llm(user_input, client)
        print(f"AI: {answer}\n")


if __name__ == "__main__":
    asyncio.run(chat_loop(client=AsyncOpenAI(api_key=get_api_key("OPENAI_API_KEY"))))
