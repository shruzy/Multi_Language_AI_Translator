# Multi Language AI Voice Translator

## Overview

Multi Language AI Voice Translator is a voice-driven translation application built using Python and Streamlit. The system allows users to speak a sentence in one language and receive an instant translation in another language along with synthesized speech output.

The application provides an interactive chat-style interface where voice input is processed through a pipeline consisting of speech recognition, language detection, command parsing, translation, and text-to-speech generation.

The goal of this project is to demonstrate a practical implementation of multilingual voice interaction using widely available open-source tools.

---

## Key Features

Voice Recording
Users can record audio directly from the browser interface.

Speech-to-Text
Recorded audio is converted into text using speech recognition.

Automatic Language Detection
The system detects the language of the spoken input automatically.

Command Parsing
The application detects instructions such as “convert this into Hindi” and determines the target language.

Text Translation
The recognized sentence is translated into the selected target language.

Text-to-Speech Output
The translated text is converted back into speech so users can hear the result.

Chat Interface
The UI displays both the user input and the translated response in a conversational format.

Real-Time Processing
The full pipeline executes quickly, allowing near real-time voice translation.

---

## Supported Languages

| Language  | Code |
| --------- | ---- |
| English   | en   |
| Hindi     | hi   |
| Marathi   | mr   |
| Tamil     | ta   |
| Telugu    | te   |
| Kannada   | kn   |
| Bengali   | bn   |
| Gujarati  | gu   |
| Punjabi   | pa   |
| Malayalam | ml   |
| Urdu      | ur   |

These languages were selected based on compatibility with the text-to-speech engine used in the project.

---

## System Architecture

The application follows a modular pipeline where each stage processes the output of the previous stage.

```
User
 │
 │  (Voice Input)
 ▼
Browser Audio Recorder
 │
 ▼
Speech Recognition Module
 │
 │  Converts audio → text
 ▼
Language Detection
 │
 │  Identifies spoken language
 ▼
Command Parser
 │
 │  Extracts target language
 │  Removes command phrases
 ▼
Translation Engine
 │
 │  Translates text to target language
 ▼
Text-to-Speech Engine
 │
 │  Converts translated text → speech
 ▼
Streamlit Interface
 │
 │  Displays:
 │  - Recorded Audio
 │  - Recognized Text
 │  - Translated Text
 │  - Translated Audio
 ▼
User Output
```

This pipeline allows the application to remain modular and easy to maintain.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/shruzy/Multi_Language_AI_Translator.git
cd Multi_Language_AI_Translator
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run streamlit_app.py
```

After running the command, open a browser and navigate to:

```
http://localhost:8501
```

---

## Project Structure

```
Multi_Language_AI_Translator
│
├── streamlit_app.py
├── config.py
├── requirements.txt
│
├── modules
│   ├── speech_to_text.py
│   ├── language_detector.py
│   ├── command_parser.py
│   ├── translator.py
│   └── text_to_speech.py
│
├── audio_input
└── audio_output
```

### File Descriptions

**streamlit_app.py**
Main application entry point containing the Streamlit UI and workflow pipeline.

**config.py**
Stores configuration variables such as directory paths and system settings.

**modules/speech_to_text.py**
Handles conversion of recorded audio into text.

**modules/language_detector.py**
Detects the language of the recognized text.

**modules/command_parser.py**
Extracts translation commands and target languages from user input.

**modules/translator.py**
Handles text translation using the translation service.

**modules/text_to_speech.py**
Converts translated text into synthesized speech.

**audio_input/**
Temporary storage for recorded audio files.

**audio_output/**
Stores generated translated speech audio.

---

## Technologies and Libraries Used

### Streamlit

Used to build the interactive web interface. Streamlit enables rapid development of data-driven web applications directly in Python.

### SpeechRecognition

A Python library that converts spoken audio into text using speech recognition engines.

### Googletrans

A lightweight Python interface to Google Translate services that allows translation between many languages.

### gTTS (Google Text-to-Speech)

Generates speech audio from text, enabling users to hear the translated output.

### Langdetect

A language detection library used to identify the language of the spoken sentence automatically.

### Audiorecorder

Provides browser-based audio recording functionality within Streamlit applications.

### Pydub

Used for handling audio file processing and exporting audio recordings.

---

## Design Decisions and Development Challenges

### Initial Plan

The original design explored using more advanced language detection models such as FastText. These models provide high accuracy for multilingual tasks.

### FastText Compatibility Issues

During development, FastText caused installation and compatibility problems on local environments due to compilation dependencies. Because of these issues, the system switched to the lighter Langdetect library, which is easier to install and sufficient for this project.

### Command Parsing Problem

Initially, sentences such as:

“my name is Ritesh convert this into Hindi”

were translated including the command phrase.

To solve this issue, a command parser module was implemented that removes instruction phrases before translation while still detecting the intended target language.

### Text-to-Speech Limitations

Some Indian languages are not supported by the text-to-speech engine used in the project. To maintain stability, only languages supported by the speech synthesis library were included in the final implementation.

### User Interface Improvements

The original UI displayed translation results in a simple layout. It was later redesigned into a chat-style interface to make the interaction more intuitive and easier for users.

---

## Example Usage

Example voice commands supported by the system:

```
Hello how are you translate to Hindi
My name is Ritesh convert this into Marathi
Good morning convert this into Tamil
What is your name translate to Bengali
```

The system extracts the actual sentence and translates it into the requested language.

---

## Future Improvements

Potential future enhancements include:

* Support for additional Indian languages
* Integration with neural machine translation models
* Higher quality speech synthesis engines
* Improved speech recognition accuracy
* Real-time conversation mode
* Cloud deployment for public access

---

## Contributing

Contributions are welcome. If you would like to improve the project, please fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

This project utilizes several open-source technologies including Streamlit, SpeechRecognition, Googletrans, gTTS, and Langdetect that make rapid development of AI-powered applications possible.
