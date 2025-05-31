import asyncio
import httpx
from utils.utils import get_api_key


async def ask_llm(messages, client, api_key):
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "meta-llama/Llama-3-70b-chat-hf",
        "messages": messages,
        "temperature": 0.7
    }

    try:
        response = await client.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except httpx.HTTPStatusError as e:
        return f"HTTP error: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"Error: {str(e)}"


async def chat_loop(api_key):
    async with httpx.AsyncClient() as client:
        messages = [{"role": "system", "content": "You are a helpful assistant."}]
        print("Ask a question (type 'exit' to quit):")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            messages.append({"role": "user", "content": user_input})
            answer = await ask_llm(messages, client, api_key)
            messages.append({"role": "assistant", "content": answer})
            print(f"AI: {answer}\n")


if __name__ == "__main__":
    asyncio.run(chat_loop(api_key=get_api_key("TOGETHER_API_KEY")))
