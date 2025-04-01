#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import random
import time
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from core.menu import display_menu, generate_server_message, show_main_menu, display_dark_message

# Force UTF-8 encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    os.environ['PYTHONIOENCODING'] = 'utf-8'

# Essential imports only
load_dotenv()
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
console = Console(force_terminal=True)

def display_startup_sequence():
    """Display a fun startup sequence"""
    generate_server_message()  # Only call this once during startup
    display_dark_message()  # Add dark message to startup
    console.print("[bold green]TextApp Lite Terminal v1.0[/bold green]")
    time.sleep(0.01)
    console.print("[bold blue]Initializing systems...[/bold blue]")
    time.sleep(0.01)
    console.print("[bold yellow]Loading modules...[/bold yellow]")
    time.sleep(0.01)
    console.print("[bold cyan]All systems nominal[/bold cyan]")
    time.sleep(0.01)

def main():
    """Main application entry point"""
    display_startup_sequence()
    
    while True:
        try:
            # Display menu
            menu_panel = display_menu()
            console.print(menu_panel)
            
            choice = input("\nEnter your choice: ")
            
            # Handle menu options
            if choice == "99":
                console.print("[yellow]Exiting application...[/yellow]")
                sys.exit(0)
            else:
                console.print("[red]Invalid choice! Please try again.[/red]")
                
        except KeyboardInterrupt:
            console.print("\n[yellow]Program interrupted by user. Goodbye![/yellow]")
            sys.exit(0)
        except Exception as e:
            console.print(f"\n[red]Unexpected error: {str(e)}[/red]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Program interrupted by user. Goodbye![/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[red]Unexpected error: {str(e)}[/red]")
