# Spoken Letter Recognition

This project uses OpenAI's Whisper model to transcribe audio files containing single letters into text.
The model is designed to recognize isolated spoken letters without interpreting them as words, such as transcribing "c" correctly rather than interpreting it as "see."

## Installation

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd spoken-letter-recognition
   ```

3. **Create a Virtual Environment**:

   ```bash
   python -m venv .venv
   ```

4. **Activate the Virtual Environment**:

   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

5. **Install Requirements**:
   Install the necessary Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Program**:

   ```bash
   python from_wav_to_letter.py
   ```

2. **Select an Audio File**:
   When prompted, select a `.wav` audio file containing isolated spoken letters.

3. **Read the Transcription**:
   The transcription will output the closest letter mappings based on the provided audio file.

## Code Explanation

- `map_to_letter(text: str)`: Maps Whisper's transcription of spoken sounds to individual letters based on predefined phonetic sounds.
- `transcribe_audio_as_letters(audio_path: str)`: Processes the selected audio file, loads the model, transcribes the audio as single letters, and outputs the mapped transcription.
- `select_wav_file()`: Opens a file dialog to select the `.wav` file.
- `main()`: Main function to execute the letter transcription workflow.

## Notes

- This code uses the OpenAI Whisper model locally, which is loaded from a specified directory or cache to avoid repeated downloads.
- The model expects isolated letter sounds (e.g., "a", "b", "c") in the audio input, not full words or sentences.
- If running on a CPU, the model will use FP32 by default as FP16 is not supported.

## Troubleshooting

If you encounter any warnings, such as FP16 being unsupported on CPU, these are generally harmless and do not affect the program’s functionality.
