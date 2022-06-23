import os
import tkinter.filedialog as filedialog
import tkinter as tk

master = tk.Tk()
master.title('WonderSwan SRAM to Flash Masta Save Data Converter')


def input():
    input_path = tk.filedialog.askopenfilename()
    input_entry.delete(1, tk.END)
    input_entry.insert(0, input_path)


def output():
    path = tk.filedialog.askdirectory()
    output_entry.delete(1, tk.END)
    output_entry.insert(0, path)

def begin():
    file_size = os.path.getsize(input_entry.get())
    iterations = 4194304//int(file_size)

    with open(input_entry.get(), 'rb') as f:
        content = f.read()
    f.close()

    with open(output_entry.get()+"/"+"Menuless_Save.wsf",'wb')as g:
        for _ in range(iterations):
            g.write(content)
    g.close()
    absolutepath=os.path.realpath(output_entry.get()+"/")
    os.startfile(absolutepath)
    


top_frame = tk.Frame(master)
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=500, bg="grey80", relief='groove')
line2 = tk.Frame(master, height=1, width=500, bg="grey80", relief='groove')


input_path = tk.Label(top_frame, text="WonderSwan SRAM Save To Convert:")
input_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Select", command=input)

output_path = tk.Label(bottom_frame, text="Output File Destination Folder:")
output_entry = tk.Entry(bottom_frame, text="", width=40)
browse2 = tk.Button(bottom_frame, text="Select", command=output)

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.TOP)
line2.pack(pady=10)

begin_button = tk.Button(text='Convert!',width=40,command=begin)



input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)

output_path.pack(pady=5)
output_entry.pack(pady=5)
browse2.pack(pady=5)


begin_button.pack(pady=20)


master.mainloop()
