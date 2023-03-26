
from gtts import gTTS
import os
import numpy as np
from pydub import AudioSegment

def text_to_speech(text, lang='en', slow=False):
    # Create gTTS object
    tts = gTTS(text=text, lang=lang, slow=slow)

    # Save audio file
    audio_file = 'output.mp3'
    tts.save(audio_file)

    # Load audio file
    audio = AudioSegment.from_file(audio_file)

    # Convert audio to numpy array
    audio_array = np.array(audio.get_array_of_samples())

    # Remove audio file
    os.remove(audio_file)

    return audio_array
