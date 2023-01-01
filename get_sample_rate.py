import wave

# Open the audio file
with wave.open('input.wav', 'rb') as wav:
    # Print the sample rate
    print(wav.getframerate())


