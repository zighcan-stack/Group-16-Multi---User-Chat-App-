import tkinter as tk
import time

# creating the main window
app = tk.Tk()
app.title("MultiChat App")
app.geometry("1280x720")


def send_message():
    message = input_box.get()  # gets message from input box
    if message.strip():  # continues if inupt box isnt empty
        timestamp = time.strftime("%H:%M:%S") #shows the message time
        display_chat.config(state="normal")
        display_chat.insert("end", f"You: {message} [{timestamp}]\n")
        display_chat.config(state="disabled")  # locks the chat area
        input_box.delete(0, "end")  # clears the input box after sending
    



# display messages
display_chat = tk.Text(app, state="disabled", wrap="word")
display_chat.pack(padx=10, pady=10, fill="both", expand=True)

input_frame = tk.Frame(app)
input_frame.pack(pady=10, padx=10, fill="x")

input_box = tk.Entry(input_frame, font=("Arial", 15), width=30, bd=2)
input_box.pack(side="left", fill="x", expand=True, padx=(0, 5))

#for enter key to send
input_box.bind("<Return>", lambda event:send_message())


send_button = tk.Button(input_frame, text="Send",
                        font=("Arial", 10), command=send_message)
send_button.pack(side="right")

app.mainloop()
