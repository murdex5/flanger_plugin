with wave.open('output.wav', 'wb') as wav:
    # Set the sample rate
    wav.setframerate(44100)
    # Set the number of channels
    wav.setnchannels(1)
    # Set the sample width
    wav.setsampwidth(2)
    # Write the audio data
    wav.writeframes(flanged.astype(np.int16))
