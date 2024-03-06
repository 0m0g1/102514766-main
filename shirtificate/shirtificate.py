from fpdf import FPDF


class Shirt(FPDF):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def header(self):
        self.image("shirtificate.png", 10, 70, 190, 190)
        self.set_font("helvetica", "B", 47)
        self.cell(0, 57, "CS50 Shirtificate", align="c")

    def footer(self):
        self.set_font("helvetica", "B", 25)
        self.set_text_color(255, 255, 255)
        self.cell(-180, 220, f"{self.name} took CS50", align="c")


def main():
    shirt = Shirt(input("What is your name? "))
    shirt.add_page(orientation="portrait", format="a4")
    shirt.output("shirtificate.pdf")


main()
