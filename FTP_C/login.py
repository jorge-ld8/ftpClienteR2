import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import main
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark

root = customtkinter.CTk()

class Login():
    
    def __init__(self):
        super().__init__()
        self.mywindow = root
        self.mywindow.geometry("750x600")
        self.mywindow.resizable(0,0)
        self.mywindow.title("Cliente")
            
        title = tk.StringVar(value="FTP Genesis I")
        self.label_t = customtkinter.CTkLabel(master=root,textvariable=title,width=120,height=25,corner_radius=8, font=("Century",25))
        self.label_t.place(relx=0.5, rely=0.1, anchor=tk.N)

        title = tk.StringVar(value="Host")
        self.label_h = customtkinter.CTkLabel(master=root,textvariable=title,width=120,height=25,corner_radius=8)
        self.label_h.place(relx=0.4, rely=0.3, anchor=tk.E)
        self.entry_h = customtkinter.CTkEntry(master=root,placeholder_text="HOST",width=200,height=30,border_width=1,corner_radius=8)
        self.entry_h.place(relx=0.4, rely=0.3, anchor=tk.W)

        title = tk.StringVar(value="Port")
        self.label_pr = customtkinter.CTkLabel(master=root,textvariable=title,width=120,height=25,corner_radius=8)
        self.label_pr.place(relx=0.4, rely=0.4, anchor=tk.E)
        self.entry_pr = customtkinter.CTkEntry(master=root,placeholder_text="PORT",width=200,height=30,border_width=1,corner_radius=8)
        self.entry_pr.place(relx=0.4, rely=0.4, anchor=tk.W)

        title = tk.StringVar(value="Username")
        self.label_u = customtkinter.CTkLabel(master=root,textvariable=title,width=120,height=25,corner_radius=8)
        self.label_u.place(relx=0.4, rely=0.5, anchor=tk.E)
        self.entry_u = customtkinter.CTkEntry(master=root,placeholder_text="USERNAME",width=200,height=30,border_width=1,corner_radius=8)
        self.entry_u.place(relx=0.4, rely=0.5, anchor=tk.W)

        title = tk.StringVar(value="Password")
        self.label_p = customtkinter.CTkLabel(master=root,textvariable=title,width=120,height=25,corner_radius=8)
        self.label_p.place(relx=0.4, rely=0.6, anchor=tk.E)
        self.entry_p = customtkinter.CTkEntry(master=root,placeholder_text="PASSWORD",width=200,height=30,border_width=1,corner_radius=8, show = "*")
        self.entry_p.place(relx=0.4, rely=0.6, anchor=tk.W)
        
        button = customtkinter.CTkButton(master=root, text="Entrar", command=self.validar_login)
        button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        self.mywindow.mainloop()

    def directorio(self, ftp):
        self.v_dir = customtkinter.CTkToplevel()
        self.v_dir.geometry("750x600")
        self.v_dir.resizable(0,0)
        self.v_dir.title("Cliente")
        self.v_dir.state(newstate = "normal")
        self.mywindow.state(newstate = "withdraw")

        btn_p = customtkinter.CTkButton(master=self.v_dir, text="Perfil", command= lambda:self.perfil(ftp))
        btn_p.place(relx=0.1, rely=0.1, anchor=tk.N)

        btn_s = customtkinter.CTkButton(master=self.v_dir, text="Subir Archivo", command= lambda:self.select_file(ftp))
        btn_s.place(relx=0.3, rely=0.1, anchor=tk.N)

        btn_c = customtkinter.CTkButton(master=self.v_dir, text="Crear Carpeta", command= lambda:self.crear_directorio(ftp))
        btn_c.place(relx=0.5, rely=0.1, anchor=tk.N)

        btn_e = customtkinter.CTkButton(master=self.v_dir, text="Eliminar Carpeta", command= lambda:self.eliminar_directorio(ftp))
        btn_e.place(relx=0.7, rely=0.1, anchor=tk.N)

        btn_cs = customtkinter.CTkButton(master=self.v_dir, text="Cerrar Sesion", command= lambda:self.cerrar_sesion(ftp))
        btn_cs.place(relx=0.9, rely=0.1, anchor=tk.N)

        btn_f_e = customtkinter.CTkButton(master=self.v_dir, text="❌ Eliminar Archivo", width=50, command= lambda:self.eliminar_archivo(ftp))
        btn_f_e.place(relx=0.2, rely=0.2, anchor=tk.N)
        
        btn_f_d = customtkinter.CTkButton(master=self.v_dir, text="⬇️ Bajar Archivo", width=50, command= lambda:self.bajar_archivo(ftp))
        btn_f_d.place(relx=0.5, rely=0.2, anchor=tk.N)

        btn_f_c = customtkinter.CTkButton(master=self.v_dir, text="📤 Compartir Archivo", width=50, command= lambda:self.compartir_archivos(ftp))
        btn_f_c.place(relx=0.8, rely=0.2, anchor=tk.N)

        arch = main.ver_arch(ftp)
        i = 0
        x = 0.2
        y = 0.3
        for name in arch:
            if(i == 0):
                frame = customtkinter.CTkFrame(master=self.v_dir,width=200,height=100,corner_radius=10)
                frame.place(relx=x, rely=y, anchor=tk.N)
                i = i + 1
            elif(i == 1):
                x = x + 0.3
                frame = customtkinter.CTkFrame(master=self.v_dir,width=200,height=100,corner_radius=10)
                frame.place(relx=x, rely=y, anchor=tk.N)
                i = i + 1
            elif(i == 2):
                x = x + 0.3
                frame = customtkinter.CTkFrame(master=self.v_dir,width=200,height=100,corner_radius=10)
                frame.place(relx=x, rely=y, anchor=tk.N)
                i = 0
                x = 0.2
                y = y + 0.3
            
            title = tk.StringVar(value=name)
            self.label_ver = customtkinter.CTkLabel(master=frame,textvariable=title,width=100,height=50,corner_radius=8)
            self.label_ver.place(relx=0.5, rely=0.4, anchor=tk.N)

        self.v_dir.mainloop()  

    def eliminar_archivo(self, ftp):
        self.dialog = customtkinter.CTkInputDialog(text="Ingrese el nombre del archivo a eliminar", title="Eliminar Archivo")
        nombre = self.dialog.get_input()
        main.elim_arch(ftp,nombre)
        self.mywindow.after(1000, self.actualizar_ventana(ftp))

    def actualizar_ventana(self,ftp):
        self.v_dir.state(newstate = "withdraw")
        self.directorio(ftp)

    def bajar_archivo(self, ftp):
        self.dialog = customtkinter.CTkInputDialog(text="Ingrese el nombre del archivo que desea bajar", title="Bajar Archivo")
        nombre = self.dialog.get_input()
        a = main.bajar_arch(ftp,nombre)
        showinfo(
                title='Informacion',
                message=a
            )
    
    def compartir_archivos(self, ftp):
        self.dialog = customtkinter.CTkInputDialog(text="Ingrese el nombre del archivo que desea compartir", title="Compartir Archivo")
        nombre = self.dialog.get_input()

        self.dialog2 = customtkinter.CTkInputDialog(text="Ingrese el nombre del usuario al que desea enviar el archivo", title="Compartir Archivo")
        usuario = self.dialog2.get_input()

        a = main.comp_arch(ftp, nombre.strip(), usuario.strip())
        showinfo(
                title='Informacion',
                message=a
            )

    def cerrar_sesion(self, ftp):
        main.c_sesion(ftp)
        self.v_dir.state(newstate = "withdraw")
        self.mywindow.state(newstate = "normal")
        self.entry_h.delete(0,"end")
        self.entry_pr.delete(0,"end")
        self.entry_u.delete(0,"end")
        self.entry_p.delete(0,"end")

    def select_file(self,ftp):

        filetypes = (
            
            ('All files', '*.*'),
            ('text files', '*.txt'),
            ('doc files', '*.docx')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        print(filename)

        main.subir_arch(ftp, filename)
        self.mywindow.after(1000, self.actualizar_ventana(ftp))

    def crear_directorio(self, ftp):
        self.dialog = customtkinter.CTkInputDialog(text="Escribe el nombre de la carpeta", title="Crear Carpeta")
        nombre = self.dialog.get_input()
        main.crear_dir(ftp, nombre)
        self.mywindow.after(1000, self.actualizar_ventana(ftp))
    
    def eliminar_directorio(self, ftp):
        self.dialog = customtkinter.CTkInputDialog(text="Escribe el nombre de la carpeta", title="Eliminar Carpeta")
        nombre = self.dialog.get_input()
        main.elim_dir(ftp, nombre)
        self.mywindow.after(1000, self.actualizar_ventana(ftp))

    def validar_login(self):

        #PRUEBA DE LOGIN Y ABRE OTRA VENTANA
        ftp = main.main(self.entry_h.get(), int(self.entry_pr.get()), self.entry_u.get(), self.entry_p.get())
        '''login_data = []
        login_data.append(self.entry_h.get())
        login_data.append(self.entry_pr.get())
        login_data.append(self.entry_u.get())
        login_data.append(self.entry_p.get())
        admin = ['1111','12','1111','1111']
        if(login_data == admin):
            self.directorio()'''
        self.directorio(ftp)

    def perfil(self, ftp):
        self.v_perfil = customtkinter.CTkToplevel()
        self.v_perfil.geometry("750x600")
        self.v_perfil.resizable(0,0)
        self.v_perfil.title("Cliente")
        self.v_perfil.state(newstate = "normal")
        self.v_dir.state(newstate = "withdraw")

        self.btn_vol = customtkinter.CTkButton(master=self.v_perfil, text="⬅️Volver",width=100, command= lambda:self.volver_menu(ftp))
        self.btn_vol.place(relx=0.1, rely=0.1, anchor=tk.N)

        title = tk.StringVar(value="Cambio de Contraseña")
        self.label_contra = customtkinter.CTkLabel(master=self.v_perfil,textvariable=title,width=120,height=25,corner_radius=8)
        self.label_contra.place(relx=0.5, rely=0.2, anchor=tk.N)

        title = tk.StringVar(value="Nueva contraseña")
        self.label_contraN = customtkinter.CTkLabel(master=self.v_perfil,textvariable=title,width=120,height=25,corner_radius=8)
        self.label_contraN.place(relx=0.4, rely=0.3, anchor=tk.E)
        self.entry_contraN = customtkinter.CTkEntry(master=self.v_perfil,placeholder_text="Nueva contraseña",width=200,height=30,border_width=1,corner_radius=8)
        self.entry_contraN.place(relx=0.4, rely=0.3, anchor=tk.W)

        title = tk.StringVar(value="Repita la contraseña")
        self.label_contraRC = customtkinter.CTkLabel(master=self.v_perfil,textvariable=title,width=120,height=25,corner_radius=8)
        self.label_contraRC.place(relx=0.4, rely=0.4, anchor=tk.E)
        self.entry_contraRC = customtkinter.CTkEntry(master=self.v_perfil,placeholder_text="Repita la contraseña",width=200,height=30,border_width=1,corner_radius=8, show = "*")
        self.entry_contraRC.place(relx=0.4, rely=0.4, anchor=tk.W)
        
        self.btn_contra= customtkinter.CTkButton(master=self.v_perfil, text="Confirmar", command= lambda:self.cambio_contraseña(ftp))
        self.btn_contra.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        self.v_perfil.mainloop()  

    def volver_menu(self, ftp):
        self.v_perfil.state(newstate = "withdraw")
        self.directorio(ftp)

    def cambio_contraseña(self, ftp):
        if(self.entry_contraN.get() == self.entry_contraRC.get()):
            c1 = self.entry_contraN.get()
            self.dialog2 = customtkinter.CTkInputDialog(text="Ingrese su contraseña antigua para confirmar el cambio", title="Cambio Contraseña")
            contra = self.dialog2.get_input()
            main.cambio_contra(ftp,c1, contra)
        else:
            showinfo(
                title='ERROR',
                message="Las contraseñas son diferentes, ingreselas nuevamente"
            )

if __name__ == "__main__":
    
    app = Login()
       

