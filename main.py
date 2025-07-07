from assistant import listen, handle_command, speak

def start():
    speak("Hello, I am your AI Assistant.")
    while True:
        query = listen()
        if query:
            if not handle_command(query):
                break

if __name__ == "__main__":
    start()
