import whisper

model = whisper.load_model("base")

def recognize_speech(filename):
    result = model.transcribe(filename,
                              language = "en",
                              fp16 = False
    )

    text = result["text"].strip().lower()
    with open('commands.txt', 'w') as f:
        f.write(text)

    return text

