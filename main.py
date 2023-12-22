from customtkinter import *
import pronotepy
from pronotepy.ent import ent_hdf


def main():
    def setup():
        set_appearance_mode("dark")
        set_default_color_theme("green")

        window = CTk()
        window.title("CelPod")
        window.geometry("850x550")
        window.resizable(width=False, height=False)

        canvas = CTkCanvas(master=window, width=250, height=200)
        canvas.place(x=20, y=40)
        canvas.create_text(125, 100, text="DEVOIRS", font=("Arial", 10))

        canvas2 = CTkCanvas(master=window, width=250, height=200)
        canvas2.place(x=300, y=40)
        canvas2.create_text(125, 100, text="NOTES", font=("Arial", 10))

        canvas3 = CTkCanvas(master=window, width=250, height=200)
        canvas3.place(x=580, y=40)
        canvas3.create_text(125, 100, text="PENSE-BÊTE", font=("Arial", 10))

        canvas4 = CTkCanvas(master=window, width=250, height=200)
        canvas4.place(x=20, y=300)
        canvas4.create_text(125, 100, text="MOYENNE", font=("Arial", 10))

        canvas5 = CTkCanvas(master=window, width=250, height=200)
        canvas5.place(x=300, y=300)
        canvas5.create_text(125, 100, text="???", font=("Arial", 10))

        canvas6 = CTkCanvas(master=window, width=250, height=200)
        canvas6.place(x=580, y=300)
        canvas6.create_text(125, 100, text="TO-DO", font=("Arial", 10))

        window.mainloop()

    client = pronotepy.Client("https://0620052v.index-education.net/pronote/eleve.html",  # lien du pronote du lycée
                              username="c.pihen13",
                              password="Celeste9*LOL",
                              ent=ent_hdf)

    if client.logged_in:
        print("Client connecté !")
        setup()
    else:
        print("Client pas connecté !")


if __name__ == "__main__":
    main()
