# Jarvis 2.0 - AI Voice Assistant

A Python-based intelligent voice assistant inspired by Tony Stark's J.A.R.V.I.S. This personal assistant can perform various tasks through voice commands, making your daily computer interactions more efficient and hands-free.

## 🚀 Features

### Core Functionality
- **Voice Recognition**: Responds to voice commands using speech recognition
- **Text-to-Speech**: Provides audio feedback for all interactions
- **Wake Word Activation**: Responds when you say "Jarvis" or "Friday"
- **Multiple Voice Options**: Choose between Jarvis and Friday voice personalities

### Communication
- **Email Integration**: Send emails through voice commands
- **WhatsApp Messaging**: Send WhatsApp messages via web interface
- **Contact Management**: Store and access frequently used contacts

### Web & Search
- **Google Search**: Perform web searches with voice commands
- **YouTube Integration**: Search and play videos on YouTube
- **Weather Updates**: Get real-time weather information for any city

### System Operations
- **Application Launcher**: Open system applications (Notepad, Calculator, Chrome, etc.)
- **File Management**: Navigate and open documents
- **Screenshot Capture**: Take and save screenshots
- **System Monitoring**: Check CPU usage and battery status

### Productivity Tools
- **Text-to-Speech Reader**: Read clipboard content aloud
- **Password Generator**: Generate secure random passwords
- **Memory Function**: Remember and recall information
- **Time & Date**: Get current time and date information

### Entertainment
- **Joke Telling**: Get random jokes for entertainment
- **Personal Information**: Share pre-programmed personal details

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- Microphone for voice input
- Internet connection for web features

### Required Packages
Install the following dependencies using pip:

```bash
pip install pyttsx3
pip install SpeechRecognition
pip install pyaudio
pip install pyautogui
pip install requests
pip install clipboard
pip install pyjokes
pip install psutil
pip install nltk
```

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/jarvis-2.0.git
   cd jarvis-2.0
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure email settings**
   - Create a file named `email_secrets.py`
   - Add your email credentials:
   ```python
   senderemail = "your_email@gmail.com"
   epwd = "your_app_password"  # Use App Password for Gmail
   to = "recipient@gmail.com"
   ```

4. **Set up API keys**
   - Get a free API key from OpenWeatherMap
   - Replace the API key in the `get_weather()` function

5. **Configure application paths**
   - Update the `app_paths` dictionary in `open_application()` function with correct paths for your system

## 🎯 Usage

### Starting the Assistant
```bash
python "Jarvis 2.0.py"
```

### Voice Commands

| Command | Action |
|---------|--------|
| "Jarvis, what time is it?" | Get current time |
| "Jarvis, what's the date?" | Get current date |
| "Jarvis, send an email" | Send email to contacts |
| "Jarvis, send WhatsApp message" | Send WhatsApp message |
| "Jarvis, search [query]" | Search Google |
| "Jarvis, YouTube [video name]" | Search YouTube |
| "Jarvis, weather in [city]" | Get weather information |
| "Jarvis, open [application]" | Launch applications |
| "Jarvis, take a screenshot" | Capture screenshot |
| "Jarvis, tell me a joke" | Get a random joke |
| "Jarvis, remember [information]" | Store information |
| "Jarvis, recall" | Retrieve stored information |
| "Jarvis, generate password" | Create secure password |
| "Jarvis, system performance" | Check CPU and battery |
| "Jarvis, goodbye" | Exit the assistant |

### Switching Voice
- Say "Jarvis, switch" to change between Jarvis and Friday voices

## 📁 Project Structure

```
jarvis-2.0/
│
├── Jarvis 2.0.py          # Main application file
├── email_secrets.py       # Email configuration (create this)
├── data.txt              # Memory storage file
├── screenshot/           # Screenshot storage directory
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## ⚙️ Configuration

### Email Setup
1. Enable 2-factor authentication on your Gmail account
2. Generate an App Password
3. Use the App Password in `email_secrets.py`

### Weather API
1. Sign up at [OpenWeatherMap](https://openweathermap.org/api)
2. Get your free API key
3. Replace the API key in the `get_weather()` function

### Application Paths
Update the `app_paths` dictionary with correct paths for your applications:
```python
app_paths = {
    "notepad": "C:\\Windows\\System32\\notepad.exe",
    "calculator": "C:\\Windows\\System32\\calc.exe",
    # Add more applications as needed
}
```

## 🔧 Customization

### Adding New Commands
1. Add your command logic in the main `while` loop
2. Use `elif 'your_command' in query:` format
3. Implement the corresponding function

### Adding Contacts
Update the contact dictionaries in the email and WhatsApp sections:
```python
email_list = {
    'contact_name': 'email@example.com'
}

user_name = {
    'contact_name': '+91 1234567890'
}
```

## 🐛 Troubleshooting

### Common Issues
- **Microphone not working**: Check microphone permissions and PyAudio installation
- **Voice not recognized**: Ensure clear pronunciation and minimal background noise
- **Email not sending**: Verify email credentials and App Password setup
- **Applications not opening**: Check and update application paths

### Error Handling
The assistant includes comprehensive error handling and will provide audio feedback for most issues.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Inspired by Marvel's J.A.R.V.I.S.
- Built using various open-source Python libraries
- Thanks to the Python community for excellent documentation

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section
2. Search existing issues on GitHub
3. Create a new issue with detailed information

---

**Note**: This is a personal project for educational purposes. Ensure you comply with the terms of service of all third-party services used (Gmail, WhatsApp Web, OpenWeatherMap, etc.).
