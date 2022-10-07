from tkinter import *
import tkinter.font as font

def btn_clicked():
    print("Button Clicked")

def calculate():
    salarioMensual = int(entry2.get())
    horasQueLaboraCadaDia = int(entry1.get())
    horasExtras = int(entry0.get())



    salarioPorDia = salarioMensual/30
    valorDeHora = salarioPorDia/horasQueLaboraCadaDia
    preSueldoFinal = salarioMensual + (valorDeHora * horasExtras)
    sueldoFinal = format(preSueldoFinal, '.2f')

    montoFinal["text"] = sueldoFinal

window = Tk()

window.geometry("1383x795")
window.configure(bg = "#ffffff")

resultSize = font.Font(size=35)
textBoxes = font.Font(size=25)

canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 795,
    width = 1383,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    689.5, 337.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 900, y = -60,
    width = 480,
    height = 128)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 419, y = -60,
    width = 480,
    height = 128)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    728.0, 434.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 498.5, y = 408,
    width = 459.0,
    height = 51)
entry0['font'] = textBoxes

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    728.0, 291.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 498.5, y = 265,
    width = 459.0,
    height = 51)
entry1['font'] = textBoxes


entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    728.0, 162.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry2.place(
    x = 498.5, y = 136,
    width = 459.0,
    height = 51)
entry2['font'] = textBoxes


montoFinal = Message(text = "$0.00", width=320, fg='white')
montoFinal.place(x = 1100, y = 510)
montoFinal.config(bg= '#3C3C3C')
montoFinal['font'] = resultSize

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = calculate,
    relief = "flat")

b2.place(
    x = 449, y = 569,
    width = 899,
    height = 61)

window.resizable(True, True)
window.mainloop()
