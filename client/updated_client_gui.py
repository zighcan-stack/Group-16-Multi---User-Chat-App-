import tkinter as tk
from tkinter import ttk
import time

app = tk.Tk()
app.title("MultiChat App")
app.geometry("800x700")
app.configure(bg="#121212")  # Dark background for modern look

# Custom colors for modern UI
DARK_BG = "#121212"
CARD_BG = "#1e1e1e"
ACCENT_COLOR = "#bb86fc"
TEXT_PRIMARY = "#ffffff"
TEXT_SECONDARY = "#b3b3b3"
INPUT_BG = "#2d2d2d"
USER_LIST_BG = "#1a1a1a"

# Header Bar with modern design
header = tk.Frame(app, bg=CARD_BG, height=70)
header.pack(fill="x", pady=(0, 10))

header_label = tk.Label(header, text="MultiChat",
                        bg=CARD_BG, fg=ACCENT_COLOR,
                        font=("Arial", 20, "bold"))
header_label.pack(pady=20)

# Main layout: chat left, users right
main_frame = tk.Frame(app, bg=DARK_BG)
main_frame.pack(fill="both", expand=True, padx=15, pady=5)

# Chat area with modern styling
chat_frame = tk.Frame(main_frame, bg=DARK_BG,
                      highlightbackground=CARD_BG, highlightthickness=1)
chat_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

# Create a custom style for the scrollbar
style = ttk.Style()
style.theme_use('clam')
style.configure("Modern.Vertical.TScrollbar",
                background=ACCENT_COLOR,
                darkcolor=ACCENT_COLOR,
                lightcolor=ACCENT_COLOR,
                troughcolor=CARD_BG,
                bordercolor=CARD_BG,
                arrowcolor=TEXT_PRIMARY,
                relief="flat")

chat_canvas = tk.Canvas(chat_frame, bg=DARK_BG, highlightthickness=0)
scrollbar = ttk.Scrollbar(chat_frame, orient="vertical",
                          command=chat_canvas.yview, style="Modern.Vertical.TScrollbar")
scrollable_frame = tk.Frame(chat_canvas, bg=DARK_BG)

scrollable_frame.bind(
    "<Configure>",
    lambda e: chat_canvas.configure(scrollregion=chat_canvas.bbox("all"))
)

chat_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
chat_canvas.configure(yscrollcommand=scrollbar.set)

chat_canvas.pack(side="left", fill="both", expand=True, padx=5, pady=5)
scrollbar.pack(side="right", fill="y", pady=5)

# User list with modern styling
user_frame = tk.Frame(main_frame, bg=CARD_BG, width=180,
                      highlightbackground=CARD_BG, highlightthickness=1)
user_frame.pack(side="right", fill="y", padx=(10, 0))
user_frame.pack_propagate(False)  # Prevent frame from resizing to content

user_label = tk.Label(user_frame, text="Online Users",
                      bg=ACCENT_COLOR, fg=TEXT_PRIMARY,
                      font=("Segoe UI", 12, "bold"), pady=10)
user_label.pack(fill="x")

# User listbox
user_listbox = tk.Listbox(user_frame, font=("Segoe UI", 11), bg=USER_LIST_BG, fg=TEXT_PRIMARY,
                          selectbackground=ACCENT_COLOR, selectforeground=TEXT_PRIMARY,
                          bd=0, highlightthickness=0, activestyle="none")
user_listbox.pack(fill="both", expand=True, padx=5, pady=5)


def add_message(message, is_user=False):
    message_frame = tk.Frame(scrollable_frame, bg=DARK_BG)
    message_frame.pack(fill="x", pady=5)

    if is_user:
        bubble_color = ACCENT_COLOR
        text_color = TEXT_PRIMARY
        anchor_side = "e"
        bubble_frame = tk.Frame(message_frame, bg=DARK_BG)
        bubble_frame.pack(fill="x", padx=10, anchor=anchor_side)

        # Timestamp
        timestamp = tk.Label(bubble_frame, text=time.strftime("%H:%M"),
                             bg=DARK_BG, fg=TEXT_SECONDARY, font=("Segoe UI", 9))
        timestamp.pack(side="right", padx=(5, 0))

        # Message bubble
        bubble = tk.Label(bubble_frame, text=message,
                          bg=bubble_color, fg=text_color,
                          wraplength=300, justify="left",
                          padx=15, pady=10, font=("Segoe UI", 11),
                          bd=0, relief="flat")
        bubble.pack(side="right")
    else:
        bubble_color = CARD_BG
        text_color = TEXT_PRIMARY
        anchor_side = "w"
        bubble_frame = tk.Frame(message_frame, bg=DARK_BG)
        bubble_frame.pack(fill="x", padx=10, anchor=anchor_side)

        # Message bubble
        bubble = tk.Label(bubble_frame, text=message,
                          bg=bubble_color, fg=text_color,
                          wraplength=300, justify="left",
                          padx=15, pady=10, font=("Segoe UI", 11),
                          bd=0, relief="flat")
        bubble.pack(side="left")

        # Timestamp
        timestamp = tk.Label(bubble_frame, text=time.strftime("%H:%M"),
                             bg=DARK_BG, fg=TEXT_SECONDARY, font=("Segoe UI", 9))
        timestamp.pack(side="left", padx=(5, 0))

    app.update_idletasks()
    chat_canvas.yview_moveto(1.0)


def send_message(event=None):
    message = input_box.get()
    if message.strip():
        add_message(message, is_user=True)
        input_box.delete(0, "end")


# Input Area with modern design
input_frame = tk.Frame(app, bg=DARK_BG, pady=15)
input_frame.pack(fill="x", padx=15)

# Modern input box
input_container = tk.Frame(input_frame, bg=INPUT_BG, relief="flat", height=45)
input_container.pack(fill="x", pady=5)
input_container.pack_propagate(False)

input_box = tk.Entry(input_container, font=("Segoe UI", 12), bg=INPUT_BG,
                     fg=TEXT_PRIMARY, insertbackground=TEXT_PRIMARY,
                     bd=0, relief="flat")
input_box.pack(side="left", fill="both", expand=True, padx=15)

input_box.bind("<Return>", send_message)
input_box.bind("<FocusIn>", lambda e: input_container.configure(
    highlightbackground=ACCENT_COLOR, highlightthickness=1))
input_box.bind("<FocusOut>", lambda e: input_container.configure(
    highlightbackground=INPUT_BG, highlightthickness=0))

# Modern send button
send_button = tk.Button(input_container, text="Send",
                        font=("Segoe UI", 10, "bold"), command=send_message,
                        bg=ACCENT_COLOR, fg=TEXT_PRIMARY, bd=0,
                        padx=20, pady=5, relief="flat", cursor="hand2")
send_button.pack(side="right", padx=10)

app.mainloop()
