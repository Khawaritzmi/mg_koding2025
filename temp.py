import tkinter as tk
from tkinter import ttk, messagebox


# Fungsi untuk konversi suhu
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)


def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)


def celsius_to_reamur(celsius):
    return celsius * 4 / 5


def reamur_to_celsius(reamur):
    return reamur * 5 / 4


def fahrenheit_to_reamur(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_reamur(celsius)


def reamur_to_fahrenheit(reamur):
    celsius = reamur_to_celsius(reamur)
    return celsius_to_fahrenheit(celsius)


def kelvin_to_reamur(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_reamur(celsius)


def reamur_to_kelvin(reamur):
    celsius = reamur_to_celsius(reamur)
    return celsius_to_kelvin(celsius)


CONVERSIONS = {
    "Celsius to Fahrenheit": ("°C", "°F", celsius_to_fahrenheit),
    "Fahrenheit to Celsius": ("°F", "°C", fahrenheit_to_celsius),
    "Celsius to Kelvin": ("°C", "K", celsius_to_kelvin),
    "Kelvin to Celsius": ("K", "°C", kelvin_to_celsius),
    "Fahrenheit to Kelvin": ("°F", "K", fahrenheit_to_kelvin),
    "Kelvin to Fahrenheit": ("K", "°F", kelvin_to_fahrenheit),
    "Celsius to Reamur": ("°C", "°Ré", celsius_to_reamur),
    "Reamur to Celsius": ("°Ré", "°C", reamur_to_celsius),
    "Fahrenheit to Reamur": ("°F", "°Ré", fahrenheit_to_reamur),
    "Reamur to Fahrenheit": ("°Ré", "°F", reamur_to_fahrenheit),
    "Kelvin to Reamur": ("K", "°Ré", kelvin_to_reamur),
    "Reamur to Kelvin": ("°Ré", "K", reamur_to_kelvin),
}


def convert_temperature(*_):
    try:
        value = float(value_var.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")
        return

    from_unit, to_unit, converter = CONVERSIONS[selected_conversion.get()]
    converted_value = converter(value)
    result_var.set(f"{value:.2f} {from_unit} = {converted_value:.2f} {to_unit}")


def clear_fields():
    value_var.set("")
    result_var.set("Result will appear here")
    value_entry.focus_set()


# Main window setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("430x380")
root.configure(bg="#0d1b2a")
root.resizable(False, False)

style = ttk.Style()
try:
    style.theme_use("clam")
except tk.TclError:
    pass  # Use default theme if clam is unavailable

BG_PRIMARY = "#0d1b2a"
CARD_BG = "#1b263b"
ACCENT_BG = "#415a77"
TEXT_LIGHT = "#e0e1dd"
TEXT_MUTED = "#778da9"

style.configure("TFrame", background=BG_PRIMARY)
style.configure("Card.TFrame", background=CARD_BG)
style.configure("ResultCard.TFrame", background=ACCENT_BG)
style.configure("Title.TLabel", background=BG_PRIMARY, foreground=TEXT_LIGHT, font=("Helvetica", 20, "bold"))
style.configure("Subtitle.TLabel", background=BG_PRIMARY, foreground=TEXT_MUTED, font=("Helvetica", 10))
style.configure("Section.TLabel", background=CARD_BG, foreground=TEXT_LIGHT, font=("Helvetica", 11))
style.configure("ResultTitle.TLabel", background=ACCENT_BG, foreground=TEXT_LIGHT, font=("Helvetica", 10))
style.configure("ResultValue.TLabel", background=ACCENT_BG, foreground="#ffffff", font=("Helvetica", 14, "bold"))
style.configure("TButton", font=("Helvetica", 11))
style.map("TButton", background=[("active", "#f72585")], foreground=[("disabled", "#999")])

container = ttk.Frame(root, padding=20)
container.pack(fill="both", expand=True)

title_label = ttk.Label(container, text="Temperature Converter", style="Title.TLabel")
title_label.pack(anchor="center")

subtitle_label = ttk.Label(
    container,
    text="Enter a value, choose the conversion direction, then hit convert.",
    style="Subtitle.TLabel",
)
subtitle_label.pack(anchor="center", pady=(4, 14))

form_card = ttk.Frame(container, padding=(20, 18), style="Card.TFrame")
form_card.pack(fill="x")
form_card.columnconfigure(0, weight=1)

value_var = tk.StringVar()
selected_conversion = tk.StringVar(value="Celsius to Fahrenheit")
result_var = tk.StringVar(value="Result will appear here")

value_label = ttk.Label(form_card, text="Temperature value", style="Section.TLabel")
value_label.grid(row=0, column=0, sticky="w")
value_entry = ttk.Entry(form_card, textvariable=value_var, font=("Helvetica", 12))
value_entry.grid(row=1, column=0, sticky="ew", pady=(2, 10))

conversion_label = ttk.Label(form_card, text="Conversion type", style="Section.TLabel")
conversion_label.grid(row=2, column=0, sticky="w")
conversion_dropdown = ttk.Combobox(
    form_card,
    textvariable=selected_conversion,
    values=list(CONVERSIONS.keys()),
    state="readonly",
    font=("Helvetica", 11),
)
conversion_dropdown.grid(row=3, column=0, sticky="ew", pady=(2, 14))

button_frame = ttk.Frame(form_card, style="Card.TFrame")
button_frame.grid(row=4, column=0, sticky="ew")
button_frame.columnconfigure((0, 1), weight=1)

convert_button = ttk.Button(button_frame, text="Convert", command=convert_temperature)
convert_button.grid(row=0, column=0, sticky="ew", padx=(0, 8))

clear_button = ttk.Button(button_frame, text="Clear", command=clear_fields)
clear_button.grid(row=0, column=1, sticky="ew")

result_card = ttk.Frame(container, padding=(16, 14), style="ResultCard.TFrame")
result_card.pack(fill="x", pady=(20, 0))

result_title = ttk.Label(result_card, text="Latest result", style="ResultTitle.TLabel")
result_title.pack(anchor="w")

result_label = ttk.Label(result_card, textvariable=result_var, style="ResultValue.TLabel")
result_label.pack(anchor="center", pady=(6, 0))

value_entry.focus_set()
root.bind("<Return>", convert_temperature)

root.mainloop()
