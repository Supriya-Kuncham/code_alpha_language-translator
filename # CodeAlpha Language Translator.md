# CodeAlpha Language Translator

This project is a simple language translation tool built with Python and the `googletrans` library. It allows users to translate text between different languages.

## Features
- Select source and destination languages
- Input and translate text easily

## Technologies Used
- Python
- Tkinter (GUI)
- Googletrans API

## Sample Code
```python
from googletrans import Translator
translator = Translator()
translated = translator.translate('Hello', src='en', dest='fr')
print(translated.text)  # Output: Bonjour
