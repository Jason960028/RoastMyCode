# 🔥 RoastMyCode-CLI

Use AI to absolutely destroy your code's self-esteem.

**RoastMyCode-CLI** is a terminal tool that reads your code, sends it to a cynical AI (Gemini), and prints a brutal, hilarious, and technically accurate roast of your programming skills.

## 📦 Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/RoastMyCode-CLI.git
    cd RoastMyCode-CLI
    ```

2.  Create a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  Set up your API Key:
    -   Get a key from [Google AI Studio](https://aistudio.google.com/).
    -   Create a `.env` file:
        ```bash
        echo "GEMINI_API_KEY=your_api_key_here" > .env
        ```

## 🚀 Usage

Run the tool on any file you dare:

```bash
python main.py <file_path>
```

### Example

**Input:** (`test_spaghetti.py`)
```python
def do_stuff(x, y):
    temp = x + y
    if temp > 10:
        print("ok")
```

**Output:**

> ... "do_stuff." That’s the most descriptive function name since I named my 2008 startup "The Thing That Does Stuff." ... And what is this indentation pyramid? This isn't Python; it's an archeological dig. ...

## 🛠️ Tech Stack
-   **Python 3.9+**
-   **Typer** (CLI)
-   **Rich** (Terminal UI)
-   **Google Gemini API** (The Roaster)

## 📄 License
MIT. Do whatever you want, your code probably leaks memory anyway.
