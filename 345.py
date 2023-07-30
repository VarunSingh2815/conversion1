from tkinter import *

window = Tk()
window.title("REWARDS CONVERTER SYSTEM")

window.geometry("550x300+500+350")
window['background']='#ADD8E6'

#globally declare measurement variables
measurement1 = ""
measurement2 = ""

def convert_SI(val, unit_in, unit_out):     #based on unitconverters.net
    SI = {'Credit card point':0.20,'Afghan Afghani':0.96,'Armenian Dram':0.22,'Azerbaijani Manat':48.21,'Bangladeshi Taka':0.76,'Cambodian Riel':0.020,'Chinese Yuan':11.49,'Hong Kong Dollar':10.48,'Indonesian Rupiah':0.0055,'Sri Lankan Rupee':0.27,'Pakistani Rupee':0.37,'Bahraini Dinar':217.43,'Emirati Dirham':22.31,'Saudi Arabian Riyal':21.85,'Euro':89.70,'Macedonian Denar':1.46,'British Pound':104.76,'United States Dollar':81.99,'Canadian Dollar':61.97,'Bajan Dollar':40.99,'Mexican Peso':4.78,'South African Rand':4.49,'Egyptian Pound':2.65,'Australian Dollar':56.31,'New Zealand Dollar':51.04}
    return val*SI[unit_in]/SI[unit_out]

def helpsection():
    pass    #put helpful info text here (e.g. no entering in right entry box else error)

def selectedInput():
    global measurement1
    measurement1 = listbox.get(listbox.curselection())#whatever is currently selected

def selectedOutput():
    global measurement2
    measurement2 = listbox1.get(listbox1.curselection()) #whatever is currently selected

def converter():
    try:
        global measurement1, measurement2
        result.set(str(convert_SI(float(inputEntry.get()), measurement1, measurement2)))

    except:
        result.set("Error")

title = Label(window, text="REWARDS CONVERTER SYSTEM", font="Calibri 24",fg='#f00',bg="#1F45FC")
title.grid(columnspan=3)
result = StringVar()    #initalize dispalyed output variable
#create a top-level menu
filemenu = Menu(window)
filemenu.add_command(label='Help', command=helpsection)
window.config(menu=filemenu)    #displays menu
#input and output entry fields
inputEntry = Entry(window)
inputEntry.grid(row=1, column=0)
arrow = Label(window, text="--->", font="Calibri 25",fg="#8470FF",bg='#A4D3EE').grid(row=1, column=1)
outputEntry = Entry(window, textvariable=result).grid(row=1, column=2)

convertButton = Button(window, text='Convert!', command=converter,font="Calibri 18", fg='#f00',bg='#00CED1').grid(row=2, column=1)

#if nonetype error, because .grid needs to be called on their own line since it always returns None
scrollbar = Scrollbar(window)   #left scrollbar
scrollbar.grid(row=2, column=0, sticky = NE + SE)
listbox = Listbox(window, exportselection=False)   #left listbox
#exportselection option in order to select 2 different listbox at same time
listbox.grid(row=2, column=0)

measurement_list = ['Credit card point','Afghan Afghani','Armenian Dram','Azerbaijani Manat','Bangladeshi Taka','Cambodian Riel','Chinese Yuan','Hong Kong Dollar','Indonesian Rupiah','Sri Lankan Rupee','Pakistani Rupee','Bahraini Dinar','Emirati Dirham','Saudi Arabian Riyal','Euro','Macedonian Denar','British Pound','United States Dollar','Canadian Dollar','Bajan Dollar','Mexican Peso','South African Rand','Egyptian Pound','Australian Dollar','New Zealand Dollar']
for measurement in measurement_list:
    listbox.insert(END, measurement)
listbox.bind("<<ListboxSelect>>", lambda x: selectedInput())   #this instead of command= option
# attach listbox to scrollbar
listbox.config(yscrollcommand=scrollbar.set,background="skyblue4", foreground="black", font=('Aerial 13'))
scrollbar.config(command=listbox.yview)


scrollbar1 = Scrollbar(window)   #right scrollbar
scrollbar1.grid(row=2, column=2, sticky = NE + SE)#add sticky if scrollbar not showing
listbox1 = Listbox(window, exportselection=False)   #right listbox
listbox1.grid(row=2, column=2)

for measurement in measurement_list:
    listbox1.insert(END, measurement)
listbox1.bind("<<ListboxSelect>>", lambda x: selectedOutput())
listbox1.config(yscrollcommand=scrollbar1.set,background="#48D1CC", foreground="black", font=('Aerial 13'))
scrollbar1.config(command=listbox1.yview)

#configure grid layout to adjust whenever window dimensions change
for i in range(3):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)


window.mainloop()
