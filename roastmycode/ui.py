
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()

def print_welcome():
    console.print(Panel.fit("[bold red]🔥 RoastMyCode-CLI 🔥[/bold red]\n[yellow]Prepare to get cooked.[/yellow]", border_style="red"))

def print_roast(roast_text: str):
    md = Markdown(roast_text)
    console.print(Panel(md, title="[bold red]🔥 The Verdict 🔥[/bold red]", border_style="red", expand=False))

def print_error(message: str):
    console.print(f"[bold red]Error:[/bold red] {message}")
