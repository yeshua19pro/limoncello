from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import random
from xhtml2pdf import pisa

def SerialCreation(b=None): #Creacion de Metodo SerialCreation
        lnlist=[]
        string=""
        for j in range(16):#Numero de caracteres en el serial
            serialnumber = random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                        "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
            lnlist.append(serialnumber)
        x= string.join(lnlist)
        return x

def renderToPdf(context, pdfpath):
    template = get_template('plantillaExamen.html')
    html = template.render(context)
    response = BytesIO()
    file= open(pdfpath, "wb")
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), file)
    file.close()