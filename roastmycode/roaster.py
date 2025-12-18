
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

from pathlib import Path

def get_config_path():
    return Path.home() / ".roastmycode.env"

def load_global_config():
    config_path = get_config_path()
    if config_path.exists():
        load_dotenv(config_path)

def get_api_key():
    load_global_config()
    # Check env var (loaded from global config or shell)
    api_key = os.getenv("GEMINI_API_KEY")
    return api_key

def read_file_content(file_path: str) -> str:
    """Reads the content of a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        raise IOError(f"Error reading file {file_path}: {e}")

def roast_code(code_content: str, model_name: str = "gemini-flash-latest") -> str:
    """Sends the code to Gemini API and returns the roast."""
    api_key = get_api_key()
    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel(model_name)
    
    prompt = f"""
    You are a cynical, sarcastic, and extremely critical senior software engineer. 
    You have seen it all, and you are unimpressed.
    
    Your task is to ROAST the following code. 
    - Be mean, but funny. 
    - Critique the code quality, variable names, logic, and structure.
    - Make references to pop culture or programming stereotypes if appropriate.
    - Keep it short and punchy (under 200 words).
    - If the code is actually good, find something petty to complain about.
    
    Here is the code:
    ```
    {code_content}
    ```
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error contacting Gemini API: {e}"
