# Authorized Voice Command Executer

## Project Overview
This project is a personal voice authentication system that allows only the registered user to execute commands on a computer system. The system provides a lightweight, offline biometric security mechanism by integrating voice recognition with system command execution.

## Features
- **Speaker Verification:** Identify if the speaker matches a registered voice profile.
- **Voice Profile Creation:** Generate unique voice embeddings from recorded samples.
- **Similarity Scoring:** Uses cosine similarity to compare voice embeddings.
- **Offline Processing:** Designed to run locally with minimal dependencies.
- **Transcription:** Integrated Whisper model for transcribing voice commands.

## Installation

### Prerequisites
- Python 3.8+
- [PortAudio](http://www.portaudio.com/) (required for `sounddevice`)
- [FFmpeg](https://ffmpeg.org/) (required for `openai-whisper`)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/authorized-voice-command-executor.git
   cd SpeechAI
   ```

2. Install the required dependencies:
   ```bash
   pip install numpy resemblyzer sounddevice scipy openai-whisper
   ```

3. Create the necessary directories:
   ```bash
   mkdir Samples Voice_Profiles Test_voices
   ```

## Usage

### 1. Record Voice Samples
Run `voice_rec.py` to collect audio samples of your voice. Rename the saved file after each recording to avoid overwriting (e.g., `Samples/sample_1.wav`, `Samples/sample_2.wav`).
```bash
python voice_rec.py
```

### 2. Generate Voice Profile
After collecting several samples in the `Samples/` directory, run `voice_auth.py` to create your biometric voice profile (`Voice_Profiles/Voice_Profile.npy`).
```bash
python voice_auth.py
```

### 3. Verify Identity
To test the authentication, run `voice_ver.py`. It will record 5 seconds of audio and compare it against your stored profile.
```bash
python voice_ver.py
```

### 4. Run the Integrated System
Execute the main script to perform voice authentication, transcription, and command execution in one flow.
```bash
python main.py
```
The system will:
1. Record your voice for authentication.
2. Verify your identity against the stored profile.
3. If authorized, transcribe your command using OpenAI's Whisper `base` model.
4. Execute the corresponding system command.

Currently supported commands (searched in transcription):
- **"browser"**: Opens the `librewolf` web browser.
- **"terminal"**: Opens the `kitty-terminal`.
- **"close"**: Kills the currently focused window using `xdotool`.
- **"shutdown"**: Initiates a system shutdown.
- **"restart"** or **"reboot"**: Reboots the system.

## Project Structure
- `main.py`: The entry point for the integrated system.
- `voice_rec.py`: Records voice samples for training.
- `voice_auth.py`: Generates a voice profile from the collected samples.
- `voice_ver.py`: Performs live voice authentication.
- `speech_rec.py`: Transcribes audio using Whisper.
- `command_exec.py`: Executes system commands based on transcription.
- `commands.txt`: Stores the transcription of the latest voice command.
- `command.wav`: Temporary file for recording verification and command audio.
- `Samples/`: Directory for storing training voice samples.
- `Voice_Profiles/`: Directory for storing the generated `.npy` profile.
- `Test_voices/`: Directory for storing temporary recordings for verification.

## Future Goals
- Implement wake word and wake word authentication.
- Expand the list of supported system commands.
- Improve security with anti-spoofing techniques.

## Acknowledgements
This project uses the following open-source libraries:
- Resemblyzer for speaker verification
- Whisper for speech recognition
- sounddevice for recording audio