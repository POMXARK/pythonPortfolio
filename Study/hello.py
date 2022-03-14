import pyttsx3


def talk(message):
    return "Talk " + message


def main():
    print(talk("Hello World"))
    engine = pyttsx3.init()
    engine.say("I will speak this text")
    engine.runAndWait()

if __name__ == "__main__":
    main()

# nuitka --mingw64 --windows-disable-console --show-progress hello.py