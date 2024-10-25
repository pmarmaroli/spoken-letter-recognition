import torch
import whisper
import os
import tkinter as tk
from tkinter import filedialog
from typing import Optional
import re
import warnings
warnings.filterwarnings(
    "ignore", message="FP16 is not supported on CPU; using FP32 instead")


# Set device
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Letter sound mapping
LETTER_MAP = {
    "a": ["a", "eh"], "b": ["b", "bee"], "c": ["c", "see"], "d": ["d", "dee"],
    "e": ["e", "ee"], "f": ["f", "ef"], "g": ["g", "gee"], "h": ["h", "aitch"],
    "i": ["i", "eye"], "j": ["j", "jay"], "k": ["k", "kay", "okay"], "l": ["l", "el"],
    "m": ["m", "em"], "n": ["n", "en"], "o": ["o", "oh"], "p": ["p", "pee"],
    "q": ["q", "cue"], "r": ["r", "ar"], "s": ["s", "ess"], "t": ["t", "tee"],
    "u": ["u", "you"], "v": ["v", "vee"], "w": ["w", "double-u"], "x": ["x", "ex"],
    "y": ["y", "why"], "z": ["z", "zee", "zed"]
}


def map_to_letter(text: str) -> Optional[str]:
    """Map Whisper output text to a single letter based on phonetic similarity."""
    text = re.sub(r'[^\w\s]', '', text.lower()
                  )  # Remove non-word characters and lowercase
    for letter, sounds in LETTER_MAP.items():
        if text in sounds:
            return letter
    return None


def transcribe_audio_as_letters(audio_path: str) -> str:
    """
    Transcribe audio as letters, avoiding interpretation as words.

    Args:
        audio_path: Path to the audio file to transcribe.

    Returns:
        The transcribed letters as a string.

    Raises:
        FileNotFoundError: If the audio file doesn't exist
        RuntimeError: If there's an issue loading the model or processing audio
    """
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    try:
        # Load the model from a local .pt file

        # Define the path to the local model cache (set to your local model directory)
        model_path = os.path.join(os.getcwd(), 'whisper-models')

        # Load the model
        try:
            model = whisper.load_model(
                "tiny", device=DEVICE, download_root=model_path)
            print("Model loaded from local cache successfully.")
        except Exception as e:
            print(f"Error loading the model: {e}")

        result = model.transcribe(audio_path)

        # Map transcription result to letters
        words = result['text'].split()

        print(f"Raw transcription result: {words}")
        print("Trying to map to letters...")

        transcription = "".join([
            letter for word in words
            if (letter := map_to_letter(word)) is not None
        ])

        print("Closest letter mapping: ", transcription)

    except Exception as e:
        raise RuntimeError(f"Error processing audio: {str(e)}")


def select_wav_file() -> Optional[str]:
    """Open file dialog to select a .wav file."""
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select a .wav file",
        filetypes=(("WAV files", "*.wav"), ("All files", "*.*"))
    )
    return file_path if file_path else None


def main():
    try:
        # Select audio file
        audio_path = select_wav_file()
        if not audio_path:
            print("No file selected. Exiting...")
            return

        # Perform transcription
        transcribe_audio_as_letters(audio_path)

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
