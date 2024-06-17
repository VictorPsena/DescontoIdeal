import tkinter as tk
from tkinter import simpledialog, messagebox

class Aplicativo:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_ui()

    def setup_ui(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.ent_dc = tk.Entry(self.frame)
        self.ent_dc.pack()

        self.button = tk.Button(self.frame, text="Submit", command=self.dc)
        self.button.pack()

    def dc(self):
        try:
            input_text = self.ent_dc.get().lower().strip()
            if not input_text:
                raise ValueError("Entrada vazia. Por favor, insira um valor.")
            c = input_text[0]
            print(f"Primeiro caractere: {c}")
            return c
        except IndexError:
            print("Entrada está vazia.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def bandeira(self):
        try:
            lista = ['v', 'm', 'e']  # Simplificado para letras únicas
            band = self.dc()
            if band:
                if band not in lista:
                    raise ValueError(f"'{band}' não está na lista.")
                print(f"Bandeira válida: {band}")
        except ValueError as ve:
            print(f"Erro de valor: {ve}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def widgets_frame_1_1(self):
        try:
            debcred = self.debcred_popup()
            print(f"DebCred: {debcred}")
        except Exception as e:
            print(f"Ocorreu um erro ao criar DebCred: {e}")

    def debcred_popup(self):
        try:
            msg = "Por favor, insira o valor para DebCred:"
            n = simpledialog.askstring("Entrada Necessária", msg)
            if n is None or not n.strip():
                raise ValueError("Entrada inválida.")
            n = n.upper().strip()[0]
            print(f"Entrada DebCred: {n}")
            return n
        except ValueError as ve:
            messagebox.showerror("Erro", f"Erro de valor: {ve}")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Aplicativo()
    app.run()
