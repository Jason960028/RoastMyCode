# 🔥 RoastMyCode: The AI That Hates Your Code

**Turn your terminal into a comedy club where YOU are the punchline.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Roast Level: Critical](https://img.shields.io/badge/Roast%20Level-Critical-red)](https://github.com/yourusername/RoastMyCode-CLI)

Are you tired of polite code reviews like *"Maybe consider a slight refactor here :)"*?
Do you secretly crave the validation of a grumpy Senior Engineer who has seen too much spaghetti?

**RoastMyCode-CLI** is here to hurt your feelings. Powered by Google's Gemini AI, it reads your code and delivers a **brutal, hilarious, and technically accurate** roast that will make you rethink your career choices.

---

## 🚀 Get Roasted in 30 Seconds

Stop debugging and start crying. Install via pip directly from GitHub:

```bash
pip install git+https://github.com/yourusername/RoastMyCode-CLI.git
```

## 🎮 How to Play

### 1. The "I'm Brave" Mode
Run it on your messiest file. We dare you.

```bash
roast my_spaghetti.py
```

### 2. The "What does this button do?" Mode
Just type `roast` to see our beautiful help screen (and delay the inevitable).

```bash
roast
```

### 🔑 First Time Set Up
The first time you run it, we'll ask for a **Gemini API Key**.
> "Ugh, effort?"
>
> Don't worry, it's free. [Get one here](https://aistudio.google.com/app/apikey). We store it locally in `~/.roastmycode.env` so we don't have to ask you again (we know you'd forget it).

---

## 📸 Hall of Fame (Screenshots)

**Input:**
```python
def do_stuff(x, y):
    temp = x + y
    if temp > 10:
        print("ok")
```

**RoastMyCode Output:**
> "Oh look, a function named `do_stuff`. How descriptive. Did `function_that_does_things` consist of too many characters for your fingers? And `temp`? **TEMP**? What is this, 1998?
>
> That indentation level is deeper than your understanding of asynchronous programming. Honestly, reading this code makes me want to `sudo rm -rf /` my own existence."

---

## 🛠️ Tech Stack (The Boring Part)

-   **Python 3.9+**: Because we have standards (unlike your code).
-   **Rich**: To make the abuse look pretty in your terminal.
-   **Typer**: Because `argparse` is for cavemen.
-   **Google Gemini**: The silicon brain that judges you.

## 📄 License

**MIT License**.
Copy it. Fork it. Sell it. do whatever you want. Just don't blame us when you cry.

---

Made with 💔 by a developer who procrastinated on their actual work to build this.
