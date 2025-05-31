import os


def get_api_key(env_var_name):
    api_key = os.getenv(env_var_name)
    if not api_key:
        api_key = input("Enter your OpenAI API key: ")
    return api_key
