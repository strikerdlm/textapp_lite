# TextApp Lite

A lightweight version of the Text Application with core functionality.

## Features

- Clean UI similar to the original TextApp
- Support for Linux (ARM and x86_64) and Windows
- Modular structure for easy maintenance
- Minimal dependencies

## Installation

1. Clone the repository:
```bash
git clone https://github.com/strikerdlm/textapp_lite.git
cd textapp_lite
```

2. Set up your environment (choose one option):

   ### Option A: Using Conda (Recommended)
   ```bash
   # Create a new Conda environment with the latest Python
   conda create -n textapp python=3.12 -y
   
   # Activate the environment
   conda activate textapp
   
   # Install pip dependencies
   pip install -r requirements.txt
   ```

   ### Option B: Using venv
   ```bash
   # Create a virtual environment
   python -m venv venv
   
   # Activate the environment
   # On Windows:
   venv\Scripts\activate
   # On Unix/macOS:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   # Copy the example environment file
   cp .env.example .env
   # Edit .env with your API keys and configurations
   ```

## Usage

Run the application:
```bash
python main.py
```

## License

MIT