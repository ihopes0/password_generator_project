import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import asksaveasfilename
import secrets
import string

letter_list = list(string.ascii_letters)
num_list = [str(x) for x in range(10)]
char_list = list('?@#$%*_-')
n = 0


def generate():
    global n
    password = ''
    gen_list = []
    gen_list.clear()

    if chk_state_letters.get() == 1 \
        or chk_state_nums.get() == 1 \
            or chk_state_chars.get() == 1:

        if chk_state_letters.get() == 1:
            gen_list += letter_list
        if chk_state_nums.get() == 1:
            gen_list += num_list
        if chk_state_chars.get() == 1:
            gen_list += char_list
        for i in range(int(spb_length.get())):
            password += secrets.choice(gen_list)
        n += 1
        txt_result.insert(tk.END, f"{n}) {password}\n")
    else:
        return


def save():
    filepath = asksaveasfilename(
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )
    with open(filepath, 'w') as output_file:
        text = txt_result.get("1.0", tk.END)
        output_file.write(text)


def clear():
    global n
    txt_result.delete("1.0", tk.END)
    n = 0


def main():
    global txt_result, window, chk_state_chars, chk_state_letters, \
        chk_state_nums, spb_length
    window = tk.Tk()
    window.title('Password generator by ihopes0')
    window.rowconfigure(0, minsize=100, weight=1)
    window.columnconfigure(1, minsize=100, weight=1)
    frm_left = tk.Frame(window, bg='grey')
    frm_right = tk.Frame(window, bg='grey')
    frm_left.grid(row=0, column=0, sticky='nsew')
    frm_right.grid(row=0, column=1, sticky='nsew')
    frm_right.rowconfigure(1, minsize=100, weight=1)
    frm_right.columnconfigure(0, minsize=250, weight=1)
    txt_result = tk.Text(master=frm_right)
    lbl_result_title = tk.Label(master=frm_right, text='Generated passwords')
    txt_result.grid(row=1, column=0, sticky='nsew', padx=20, pady=5)
    lbl_result_title.grid(row=0, column=0, sticky='ew', pady=5, padx=20)
    lbl_length = tk.Label(
        master=frm_left,
        text="Password length:",
        font=(100),
        bg='grey'
        )
    lbl_letters = tk.Label(
        master=frm_left,
        text="Letters:",
        font=(100),
        bg='grey'
        )
    lbl_nums = tk.Label(
        master=frm_left,
        text="Numbers:",
        font=(100),
        bg='grey'
        )
    lbl_chars = tk.Label(
        master=frm_left,
        text="Characters:",
        font=(100),
        bg='grey'
        )
    spb_length = tk.Spinbox(master=frm_left, width=3, from_=4, to=25)
    chk_state_letters = tk.IntVar()
    chk_state_nums = tk.IntVar()
    chk_state_chars = tk.IntVar()
    chk_state_letters.set(0)
    chk_state_nums.set(0)
    chk_state_chars.set(0)
    chk_letters = ttk.Checkbutton(
        master=frm_left,
        text='On/Off',
        var=chk_state_letters,
        onvalue='1',
        offvalue='0'
        )
    chk_nums = ttk.Checkbutton(
        master=frm_left,
        text='On/Off',
        var=chk_state_nums,
        onvalue='1',
        offvalue='0'
    )
    chk_chars = ttk.Checkbutton(
        master=frm_left,
        text='On/Off',
        var=chk_state_chars,
        onvalue='1',
        offvalue='0'
    )

    lbl_length.grid(row=0, column=0, sticky='w', padx=10, pady=5)
    spb_length.grid(row=0, column=0, sticky='e', pady=5)

    lbl_letters.grid(row=1, column=0, sticky='w', padx=10, pady=5)
    chk_letters.grid(row=1, column=0, sticky='e', pady=5)

    lbl_nums.grid(row=2, column=0, sticky='w', padx=10, pady=5)
    chk_nums.grid(row=2, column=0, sticky='e', pady=5)

    lbl_chars.grid(row=3, column=0, sticky='w', padx=10, pady=5)
    chk_chars.grid(row=3, column=0, sticky='e', pady=5)

    btn_gen = tk.Button(
        master=frm_left,
        relief=tk.RAISED,
        borderwidth=5,
        bg='white',
        command=generate,
        text='Generate password',
        font=(100)
    )

    btn_gen.grid(row=4, column=0, sticky='ew', padx=40, pady=25)

    btn_save = tk.Button(
        master=frm_left,
        relief=tk.RAISED,
        borderwidth=5,
        bg='white',
        command=save,
        text='Save as',
    )

    btn_save.grid(row=5, column=0, sticky='ew', padx=20, pady=5)

    btn_clear = tk.Button(
        master=frm_left,
        relief=tk.RAISED,
        borderwidth=5,
        bg='white',
        command=clear,
        text='Clear',
    )

    btn_clear.grid(row=6, column=0, sticky='ew', padx=20, pady=5)

    lbl_tg = tk.Label(
        master=frm_left,
        relief=tk.RIDGE,
        borderwidth=10,
        text="t.me/wo_xiwang_so",
        bg='grey',
        fg='white',
        width=50,
        height=3,
        font=100,
    )
    lbl_tg.grid(row=7, column=0, sticky='nsew', pady=10, padx=5)

    window.mainloop()


if __name__ == '__main__':
    main()
