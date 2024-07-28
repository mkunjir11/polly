import os
import sys
import boto3

# Create a Polly client
polly = boto3.client('polly', verify=False)

text = "Hello, This is text to voice demo."

output_format = "mp3"
voice_id = "Joanna"

response = polly.synthesize_speech(
    Text=text,
    OutputFormat=output_format,
    VoiceId=voice_id
)

# Save the audio stream to a file
file_name = "speech.mp3"
with open(file_name, "wb") as file:
    file.write(response["AudioStream"].read())

print(f"Speech saved to {file_name}")

if sys.platform == "win32":
    os.startfile(file_name)
else:
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, output])