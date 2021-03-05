from tkinter import  *

window = Tk()
window.title("Mile - KM Converter")
window.minsize(width=200, height=100)
window.config(padx=50, pady=50)


# Mile -KM converter function
def mile_to_km():
    mile = int(mile_input.get())
    km = round(mile * 1.609, 2)
    output_label.config(text=f"{km}")


# is equal to Label
is_equal_label = Label(text="is equal to", font=("Arial", 8, "bold"))
is_equal_label.grid(column=0, row=1)

# output label
output_label = Label(text="0")
output_label.grid(column=1, row=1)
output_label.config(padx=10, pady=10)

# Entry
mile_input = Entry(width=8)
mile_input.grid(column=1, row=0)

# Button
my_button = Button(text="Calculate", command=mile_to_km, font=("Arial", 8, "bold"))
my_button.grid(column=1, row=2)
my_button.config(padx=5, pady=5)

# Miles label
miles_label = Label(text="Miles", font=("Arial", 8, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

# KM label
km_label = Label(text="Km", font=("Arial", 8, "bold"))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

window.mainloop()
