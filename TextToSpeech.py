import os
import sys
import boto3

# Create a Polly client
polly = boto3.client('polly', verify=False)

# Set the text to be synthesized
text = "Hello, This is text to voice demo."

# Set the output format and voice ID
output_format = "mp3"
voice_id = "Joanna"

# Call the synthesize_speech method
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
