try:
    import Image
except ImportError:
    from PIL import Image
# from wand.image import Image
import pytesseract
import os
import PyPDF2
import io
from os.path import splitext

text_file = open("Output.txt", "w")

def pdf_page_to_png(src_pdf, pagenum = 0, resolution = 72):
    """
    Returns specified PDF page as wand.image.Image png.
    :param PyPDF2.PdfFileReader src_pdf: PDF from which to take pages.
    :param int pagenum: Page number to take.
    :param int resolution: Resolution for resulting png in DPI.
    """
    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.addPage(src_pdf.getPage(0))

    pdf_bytes = io.BytesIO()
    dst_pdf.write(pdf_bytes)
    pdf_bytes.seek(0)

    img = Image(file = pdf_bytes, resolution = resolution)
    img.convert("png")
    img.save(".\EBSUploadedDocuments\\bbc.png")
    return img


def traverse_directories(dirName):
    if(os.path.exists(dirName)):
        
        for root, dirs, files in os.walk(dirName):
            path = root.split(os.sep)
            print((len(path) - 1) * '---', os.path.basename(root))
            for file in files:
                print(len(path) * '---', file)
                text_file.write("\n\n\n==========================================================================================")
                text_file.write("\n==========================================================================================")
                text_file.write("\n" + file+"\n")
                text_file.write("------------------------------------------------------------------------------------------\n")
                file_name,extension = splitext(file)
                #print(extension)
                fullFileName = root+"\\"+file
                if (extension in ".pdf" or extension in ".PDF"):
                    
                    pdfFileObj = open(fullFileName,'rb')     #'rb' for read binary mode
                    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                    pdfReader.numPages
                    pageObj = pdfReader.getPage(0)
                    pageCount = pdfReader.numPages
                    im = pdf_page_to_png(pdfReader)
                    open(im)
                    # while pageCount>=0:
                    #     pageObj = pdfReader.getPage(pageCount-1)
                    #     pdf_page_to_png(pageObj)
                    #     pageCount = pageCount-1
                    # print(pageObj.extractText())
                    # text_file.write(pageObj.extractText())
                else:
                    continue
                
    else:
        print("Path does not exists")

# im = Image.open(".\EBSUploadedDocuments\\608498\\PAN.jpg") # the second one 
# txt = pytesseract.image_to_string(im)
# im = im.filter(ImageFilter.MedianFilter())
# enhancer = ImageEnhance.Contrast(im)
# im = enhancer.enhance(2)
# im = im.convert('1')
# im.save('temp2.jpg')
# pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
# def tesser_image(image):
#     image = PIL.Image.fromarray(image,'RGB')
#     txt = pytesseract.image_to_string(image)
#     return (txt)
# def screengrabasnumpy(Location)
#     im = numpy.array(PIL.ImageGrab.grab(bbox=(location[0],location[1],location[2],location[3])))
#     return (im)
# print(txt)
# print(os.listdir())

traverse_directories(".\EBSUploadedDocuments")
text_file.close()



