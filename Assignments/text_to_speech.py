from gtts import gTTS

def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    print(f"Text converted to speech and saved as '{output_file}'")

def main():
    text = input("Enter the text you want to convert to speech: ")
    output_file = "output.mp3"  # You can specify the desired output file name here

    text_to_speech(text, output_file)

if __name__ == "__main__":
    main()
