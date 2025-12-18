
import typer
import time
import warnings
import os
import sys
from rich.prompt import Prompt
from rich.console import Console

# Suppress annoying warnings for clean CLI output
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# Monkeypatch for Python < 3.10 compatibility with google-api-core
# MUST BE DONE BEFORE IMPORTING GOOGLE LIBRARIES
# Monkeypatch for Python < 3.10 compatibility with google-api-core
if sys.version_info < (3, 10):
    try:
        import importlib.metadata
        if not hasattr(importlib.metadata, "packages_distributions"):
            import importlib_metadata
            importlib.metadata.packages_distributions = importlib_metadata.packages_distributions
    except ImportError:
        pass 
 

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

# Import local modules AFTER patching
from .roaster import read_file_content, roast_code, get_api_key, get_config_path
from .ui import print_welcome, print_roast, print_error

app = typer.Typer()
console = Console()

def ensure_api_key():
    """Checks for API key and runs onboarding if missing."""
    key = get_api_key()
    if key:
        return True
    
    # Onboarding Flow
    print_welcome()
    console.print("[bold yellow]Wait! You need a Gemini API Key to roast your code.[/bold yellow]")
    console.print("Get one for free here: [link]https://aistudio.google.com/app/apikey[/link]\n")
    
    key_input = Prompt.ask("[bold green]Enter your Gemini API Key[/bold green]", password=True)
    
    if key_input:
        config_path = get_config_path()
        try:
            with open(config_path, "w") as f:
                f.write(f"GEMINI_API_KEY={key_input}\n")
            console.print(f"[green]Saved API key to {config_path}[/green]\n")
            # Reload env
            os.environ["GEMINI_API_KEY"] = key_input
            return True
        except Exception as e:
            print_error(f"Failed to save config: {e}")
            return False
    return False

@app.command()
def main(file_path: str):
    """
    Roast the code in the specified file.
    """
    if not ensure_api_key():
        print_error("API Key is required to proceed.")
        raise typer.Exit(code=1)

    # Note: We print welcome inside ensure_api_key if onboarding, 
    # but if key exists, we might want to print it here.
    # To avoid double printing, let's just print it here if we didn't just onboard.
    # Simplified: Just print it.
    # print_welcome() 
    
    try:
        # Step 1: Read File
        code_content = read_file_content(file_path)
        
        # Step 2: Roast it (with spinner)
        from rich.progress import Progress, SpinnerColumn, TextColumn
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            progress.add_task(description="[red]Analyzing spaghetti code...[/red]", total=None)
            roast_result = roast_code(code_content)
            
        # Step 3: Display Result
        print_roast(roast_result)
        
    except Exception as e:
        print_error(str(e))

if __name__ == "__main__":
    app()
