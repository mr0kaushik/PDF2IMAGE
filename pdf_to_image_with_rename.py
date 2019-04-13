import fitz
doc = fitz.open("E:\\Web\\IPU_Result_Parser\\btech.pdf")
with open("E:\\Web\\IPU_Result_Parser\\Image_data\\name_data.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
j=0

for i in range(len(doc)):
    list = doc.getPageImageList(i)
    list.reverse()
    for img in list:
        if i>62:
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            if pix.n < 5:       # this is GRAY or RGB
                pix.writePNG(content[j]+".png")
                j=j+1
            else:               # CMYK: convert to RGB first
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix.writePNG(content[j]+".png")
                j=j+1
                pix1 = None
            pix = None
