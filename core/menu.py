from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.box import MINIMAL
from rich.panel import Panel
import random
import time

console = Console()

def display_dark_message():
    """Display a random dark humor message"""
    messages = [
        "Warning: This program may contain traces of bad code and terrible decisions.",
        "Caution: Side effects may include loss of sanity and excessive caffeine consumption.",
        "Disclaimer: No developers were harmed in the making of this software... much.",
        "Notice: This program is powered by dark magic and questionable life choices.",
        "Alert: Your computer may judge you for the commands you're about to enter."
    ]
    console.print(f"[bold red]{random.choice(messages)}[/bold red]")

def generate_server_message():
    """Generate a random server connection message with IP and space-related organization."""
    # Generate random IP
    ip_parts = [str(random.randint(1, 255)) for _ in range(4)]
    ip = ".".join(ip_parts)
    
    # Connection sequence with faster timing
    console.print(f"[yellow]Connecting to {ip}[/yellow]")
    time.sleep(0.01)
    console.print("[cyan]Establishing secured network tunnel[/cyan]")
    time.sleep(0.01)

def display_menu():
    """Display the main menu interface with horizontal layout"""
    
    # System Tools
    system_tools = {
        "98": "Settings",
        "99": "Exit"
    }

    # Create main table with columns and add header panels
    main_table = Table(
        box=None,
        show_header=False,
        show_edge=False,
        expand=True,
        padding=(0, 1)
    )
    
    # Add three columns for the menu sections
    main_table.add_column("Column1", justify="left", ratio=1)

    # Add title
    main_table.add_row()
    main_table.add_row(
        Panel("[bold yellow]TextApp Lite[/bold yellow]", 
              border_style="yellow", 
              expand=True)
    )
    
    # Create a section for menu items
    table = Table(
        box=None, 
        show_header=False, 
        show_edge=False, 
        pad_edge=False, 
        width=40
    )
    
    table.add_column("Key", justify="right", style="cyan", width=4)
    table.add_column("Value", style="white")
    
    # Add title row with clean separator
    table.add_row("", f"[bold magenta]System[/bold magenta]")
    table.add_row("", "─" * 30)
    
    # Add menu items
    for key, value in system_tools.items():
        table.add_row(f"{key}", value)
    
    # Add the table to the main table
    main_table.add_row(table)

    return main_table

def show_main_menu():
    """Display the main menu options"""
    console.print("\n[bold blue]Main Menu[/bold blue]")
    console.print("1. Exit")
    return input("Select an option: ")
