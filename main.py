from  fpdf import   FPDF # class 
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4") # pdf = object
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():  # iterrows(): method it is used to take index and row. 
    pdf.add_page() #ist step
    pdf.set_font(family="Times" , style="B", size=12)
    pdf.set_text_color(0, 255, 0) # for topics
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10,20,200,20) # x1, y1, x2, y2

    for i in range(row["Pages"] - 1):
        pdf.add_page()
    
    # set footers
    pdf.ln(275)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")
    
pdf.output("output.pdf")    




# 1st Create a Multiple Page PDF
# 2nd Call CSV to PDF
# 3rd Add Footer
# 4th Created line on all pdf page