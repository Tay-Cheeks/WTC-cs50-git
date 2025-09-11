"""
    Portrait orientation ("P")
    A4 page ("A4", 210 × 297 mm)
    Centered title: "CS50 Shirtificate"
    Add the shirtificate.png image (provided in the folder), centered horizontally
    Overlay the user’s name on the shirt, in white text
    Output: shirtificate.pdf

    Subclassing FPDF for reusable header() or footer() for every page
    set_auto_page_break(False): ensures the shirt image doesn’t push the content to another page.
    Negative cell heights: can shift text upward for fine positioning
    Centering text: by using cell(0, …, align="C").
    Text color: set_text_color(255, 255, 255) for white.
"""

from fpdf import FPDF

#shirtification class with FPDF subclass
#with a custom __init__ in the subclass, so everything is cleaner and self-contained to lock in defaults
class Shirtificate(FPDF):

    def __init__(self):
        #call the parent class FPDF initialiser
        super().__init__(orientation="P", unit="mm", format="A4")

        #prevent auto page-breaks that might shift page format
        self.set_auto_page_break(False)

    def header(self):
        #add title at the top of every page
        self.set_font("Helvetica", style="B", size=24)
        #printing title
        self.cell(0, 30, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

    def footer(self):
        self.set_y(-10) #20mm from bottom
        self.set_font("Helvetica", "I", 12)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, "CS50, Harvard University", align="C")

def main():
    #prompt user for name
    name = input("Name: ").strip()

    #create pdf
    pdf = Shirtificate()
    pdf.add_page()


    #shirt img centered
    page_width = pdf.w
    img_width = 190
    x = (page_width - img_width) / 2
     #add cs50 shirt img
    pdf.image("shirtificate.png", x=x, y=70, w=img_width)

    #adjust font size dynamically
    if len(name) <= 20:
        name_font_size = 30
    elif len(name) <= 30:
        name_font_size = 24
    else:
        name_font_size = 18

    #overlay name on shirt
    pdf.set_font("Helvetica", style="B", size=name_font_size)

    # Shadow
    pdf.set_text_color(50, 50, 50)
    pdf.set_y(142)#shadow position
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    pdf.set_text_color(255, 255, 255) #white
    pdf.set_y(139)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    #page border
    pdf.set_draw_color(0, 102, 204) #blue border
    pdf.set_line_width(1.5)
    pdf.rect(5, 5, 200, 287-10) #margin rectangle



    #print shirt onto pdf
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()


