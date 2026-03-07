# Multi_Language_AI_Translator
🎤 AI Voice Translator
A powerful multi-language voice translation application built with Streamlit. This app allows users to speak in one language and get instant voice translations in multiple Indian and international languages.

🌟 Features
Voice Recording: Record audio directly in the browser

Speech-to-Text: Convert spoken words to text using speech recognition

Multi-Language Support: Translate between 11 different languages

Text-to-Speech: Hear the translated text in the target language

Chat Interface: Clean chat-like UI for easy interaction

Real-time Processing: Fast and efficient translation pipeline

🗣️ Supported Languages
Language	Code
English	en
Hindi	hi
Marathi	mr
Tamil	ta
Telugu	te
Kannada	kn
Bengali	bn
Gujarati	gu
Punjabi	pa
Malayalam	ml
Urdu	ur
🚀 How It Works
Record Voice: Click the "Record" button and speak your message

Automatic Processing: The app automatically:

Converts speech to text

Detects the input language

Parses any language commands

Translates to the target language

Get Results: Receive both translated text and audio output

🛠️ Installation
Clone the repository:

bash
git clone https://github.com/shruzy/Multi_Language_AI_Translator.git
cd ai-voice-translator
Install dependencies:

bash
pip install -r requirements.txt
Set up configuration:

Create necessary directories (if not自动 created)

Configure API keys in config.py if needed

📦 Dependencies
streamlit

audiorecorder

speech_recognition

googletrans==4.0.0-rc1

gTTS

langdetect

pydub

Other dependencies listed in requirements.txt

🎯 Usage
Run the application:

bash
streamlit run streamlit_app.py
Open your browser and go to http://localhost:8501

Click the "Record" button and speak your message (e.g., "my name is Ritesh Shukla convert this into Hindi")

View the translation results in both text and audio format

📁 Project Structure
text
ai-voice-translator/
├── streamlit_app.py          # Main application file
├── config.py                  # Configuration settings
├── requirements.txt           # Python dependencies
├── modules/
│   ├── speech_to_text.py     # Speech recognition module
│   ├── language_detector.py   # Language detection
│   ├── command_parser.py      # Command parsing logic
│   ├── translator.py          # Translation module
│   └── text_to_speech.py      # Text-to-speech conversion
├── audio_input/               # Directory for input audio
└── audio_output/              # Directory for output audio
💡 Usage Examples
"Hello, how are you? translate to Hindi"

"मेरा नाम रितेश है convert this into English"

"Good morning convert this into Tamil"

"What is your name? translate to Bengali"

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Streamlit for the amazing web framework

Google Translate API for translation services

Google Text-to-Speech for audio generation

📧 Contact
For any queries or suggestions, please open an issue on GitHub or contact the maintainer.

