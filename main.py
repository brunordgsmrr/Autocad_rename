# Python script para renomear arquivos usando prefixo e sufixo
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import customtkinter as ct
import os


def main_tk():
    """
        Use a breakpoint in the code line below to debug your script.
    """
    ct.set_appearance_mode("dark")
    # Creating Window of app
    root = ct.CTk()
    root.geometry('400x500')
    lista_desenhos = []
    font_media = ('ARIAL', 16)

    lbl_prefix = ct.CTkLabel(root, text='PREFIX', font=font_media)
    lbl_prefix.place(relx=0.3, rely=0.3, anchor=CENTER)

    txt_prefix = ct.CTkEntry(root, width=100, font=font_media)
    txt_prefix.place(relx=0.3, rely=0.38, anchor=CENTER)

    lbl_suffix = ct.CTkLabel(root, text='SUFFIX', font=font_media)
    lbl_suffix.place(relx=0.7, rely=0.3, anchor=CENTER)

    txt_suffix = ct.CTkEntry(root, width=100, font=font_media)
    txt_suffix.place(relx=0.7, rely=0.38, anchor=CENTER)

    btn_selection = ct.CTkButton(root, text="Selecionar arquivos", font=font_media,
                                 command=(lambda: lista_desenhos.append(select_files()))
                                 )
    btn_selection.place(relx=0.5, rely=0.50, anchor=CENTER)

    btn_rename = ct.CTkButton(root, text="Renomear arquivos", font=font_media,
                              command=(lambda: rename_files(txt_prefix.get(), txt_suffix.get(), lista_desenhos))
                              )
    btn_rename.place(relx=0.5, rely=0.58, anchor=CENTER)

    root.mainloop()


def select_files():
    filetypes = (('Drawing', '*.dwg'), ('All files', '*.*'))
    user = os.getenv('USERPROFILE')

    return fd.askopenfilenames(title='Open files', initialdir=f'{user}/Documents', filetypes=filetypes)


def rename_files(prefix, suffix, list_files):
    # GERAR A LISTA DE DESENHOS
    list_dwg = list(list_files[0])

    # PEGAR NOME DO ARQUIVO E CONCATENAR
    for arquivo in list_dwg:
        path = str(os.path.dirname(os.path.abspath(arquivo))).replace('\\', '/')

        old_name = arquivo.split('/')
        old_name = str(old_name[-1])
        old_name = old_name.removesuffix('.dwg')

        new_name = f'{path}/{prefix}{old_name}{suffix}.dwg'

        os.renames(arquivo, new_name)

    showinfo(title='Renomear arquivo', message='Arquivos renomeados')


if __name__ == '__main__':
    main_tk()
