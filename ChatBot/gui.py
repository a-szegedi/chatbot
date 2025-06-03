import tkinter as tk
from bot import ChatBot

class ChatBotGUI:
    def __init__(self, root, bot):
        self.root = root
        self.bot = bot
        self.root.iconphoto(False, tk.PhotoImage(file="gfn_logo.png"))
        self.root.title("GFN Chat-Bot")
        self.root.geometry("500x400")
        self.root.configure(bg="#1E3A8A")
        self.root.bind('<Return>', lambda event: self.send_question())

        header_frame = tk.Frame(self.root, bg="#007ACC", height=50)
        header_frame.pack(fill="x", padx=8, pady=(45, 10))
        header_frame.pack_propagate(False)

        header = tk.Label(
            header_frame,
            text="Willkommen beim GFN Chat-Bot!",
            font=("Helvetica", 16, "bold"),
            bg="#007ACC",
            fg="white",
            pady=10
        )
        header.pack(fill="x")

        text_frame = tk.Frame(self.root, bg="#007ACC")
        text_frame.pack(pady=10)

        self.input_field = tk.Entry(text_frame, width=60)
        self.input_field.grid(row=0, column=0, padx=5, pady=(10, 5))

        self.send_button = tk.Button(text_frame, text="Frage senden", command=self.send_question)
        self.send_button.grid(row=0, column=1, padx=5, pady=(10, 5))

        self.output_text = tk.Text(text_frame, height=10, width=60, wrap=tk.WORD, state=tk.DISABLED, bg="white")
        self.output_text.grid(row=1, column=0, columnspan=2, pady=10)

    def send_question(self):
        user_input = self.input_field.get().strip()
        if not user_input:
            return
        if user_input.lower() == "exit":
            self.root.quit()
            return

        response = self.bot.find_response(user_input)
        self.display_dialog(user_input, response)
        self.input_field.delete(0, tk.END)

    def display_dialog(self, user_input, response):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, f"Du: {user_input}\n", "user")
        self.output_text.insert(tk.END, f"Bot: {response}\n\n", "bot")
        self.output_text.tag_config("bot", foreground="#1E3A8A")
        self.output_text.tag_config("user", foreground="black")
        self.output_text.config(state=tk.DISABLED)
        self.output_text.see(tk.END)

def main():
    bot = ChatBot("data/faq.json")
    root = tk.Tk()
    app = ChatBotGUI(root, bot)
    root.mainloop()

if __name__ == "__main__":
    main()