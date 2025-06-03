from bot import ChatBot

def main():
    bot = ChatBot("data/faq.json")
    print("Willkommen beim GFN Chat-Bot! (Geben Sie 'exit' ein zum Beenden)\n")

    while True:
        user_input = input("Sie: ")
        if user_input.lower() == "exit":
            print("Bot: Vielen Dank und auf Wiedersehen!")
            break

        response = bot.find_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
