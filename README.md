# TextApp - Multi-Service Research and Development Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Active-green)
![Security](https://img.shields.io/badge/Security-Hardened-blue)
[![CrewAI](https://img.shields.io/badge/CrewAI-Enabled-orange)](https://github.com/joaomdmoura/crewAI)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP8-brightgreen)](https://www.python.org/dev/peps/pep-0008/)
[![Documentation](https://img.shields.io/badge/Documentation-Comprehensive-blue)](https://github.com/strikerdlm/textapp/wiki)

TextApp is a comprehensive platform that integrates various services for research, development, and data analysis. It combines medical services, AI capabilities, research tools, and system utilities into a unified interface.

## 🔄 Recent Updates

### March 2024
- Added NASA HRP Countermeasures Review and Project Generator in the Research & Academic Tools
- Updated to use `langchain_community` imports for better compatibility
- Enhanced HTTP client implementation with proper timeout handling
- Improved error logging and exception handling
- Fixed OpenAI client integration with custom HTTP client
- Optimized network request handling
- Added Conda environment setup support

## 🚀 Key Features

### 🏥 Medical Services
- Medical Voice Recording
- Medical Diagnosis
- Audio Transcription
- Medical Agenda Management (Streamlit)

### 🔬 Research & Academic Tools
- NASA HRP Countermeasures Review and Project Generator
- PyPaperBot Integration
- PubMed Search
- Semantic Scholar Integration
- CrossRef Search
- CORE Search
- Document Processing

### 🤖 AI & LLM Services
- Multiple LLM Integrations (GPT-4, Claude, PPLX)
- Training Data Creation
- Flow Agents
- Book Writing Assistant
- Multi-Agent Testing

### 📊 Data Operations
- Flowise API Management
- Pinecone Vector Operations
- LlamaIndex Integration
- GraphRAG Operations
- Mendeley Integration
- Batch Processing (PDF/MD/JSONL)

### 🌐 Network & System Tools
- Network Monitoring
- Speed Testing
- Weather Services
- Google Maps Integration
- PC Temperature Monitoring

### 🔍 OSINT Tools
- Intelligence X Operations
- SkyTrack Aircraft OSINT

## 📋 Requirements

- Python 3.8 or higher
- See `requirements.txt` for complete dependencies

## 🛠️ Installation

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
   # Use your preferred text editor
   ```

## 🚦 Usage

Run the main application:
```bash
python main.py
```

The application provides an interactive menu interface with the following main categories:
- Medical Services
- ROBD2 Services
- AI Services
- Data Operations
- Research Tools
- Document Tools
- OSINT Tools
- Network Tools
- Weather Services
- Location Services
- Communication Tools
- Hardware Monitoring

### NASA HRP Project

To run the NASA HRP Countermeasures Review and Project Generator:

**Unix/Linux/macOS:**
```bash
./services/nasa_hrp/run.sh
```

**Windows:**
```powershell
.\services\nasa_hrp\run.ps1
```

Or you can run the Python script directly:
```bash
python services/nasa_hrp/run.py
```

See the [NASA HRP Project README](services/nasa_hrp/README.md) for more details.

## 🔐 Security

- All API keys and sensitive data are managed through environment variables
- Implements secure error handling and logging
- Regular security updates and dependency management
- Hardened against common vulnerabilities
- Enhanced HTTP client security with proper timeout handling

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

Diego Malpica

## 📞 Support

For support, please open an issue in the GitHub repository or contact the maintainers directly.

## 🙏 Acknowledgments

- All the open-source projects that made this possible
- Contributors and users of the platform
- Research and academic partners