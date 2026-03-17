import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
from resemblyzer import VoiceEncoder, preprocess_wav
from numpy.linalg import norm

SAMPLE_RATE = 16000
DURATION = 5
THRESHOLD = 0.75 # authentication threshold

def cosine_similarity(a, b):
    return np.dot(a, b) / (norm(a) * norm(b))

def verify_voice():
    # Record live audio
    print("Speak your command for authentication and processing...")

    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype="float32")
    sd.wait()
    write("command.wav", SAMPLE_RATE, audio)

    # Check for silence or low audio energy
    audio_energy = np.sqrt(np.mean(audio**2))

    if audio_energy < 0.0001:  # Threshold for silence
        print("Similarity Score: 0.000")
        print("ACCESS DENIED — No voice detected (Silence)")
        return False

    print("Processing voice...")

    encoder = VoiceEncoder()

    wav = preprocess_wav("command.wav")
    current_embedding = encoder.embed_utterance(wav)

    # Load stored voice profile
    voice_profile = np.load("Voice_Profiles/Voice_Profile.npy")

    # Compare voices
    similarity = cosine_similarity(current_embedding, voice_profile)
    print(f"Similarity Score: {similarity:.3f}")

    if similarity > THRESHOLD:
        print("AUTHENTICATED — Voice Match")
        return True
    else:
        print("ACCESS DENIED — Voice Mismatch")
        return False

#verify_voice() debug line