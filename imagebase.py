try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import os
import PyPDF2

from os.path import splitext

text_file = open("Output.txt", "w")
def traverse_directories(dirName):
    if(os.path.exists(dirName)):
        print(dirName)
        for root, dirs, files in os.walk(dirName):
            path = root.split(os.sep)
            print((len(path) - 1) * '---', os.path.basename(root))
            for file in files:
                try:
                    print(len(path) * '---', file)
                    text_file.write("\n\n\n==========================================================================================")
                    text_file.write("\n==========================================================================================")
                    text_file.write("\n" + file+"\n")
                    text_file.write("------------------------------------------------------------------------------------------\n")
                    print("\n\n\n==========================================================================================")
                    print("\n==========================================================================================")
                    print("\n" + file+"\n")
                    print("------------------------------------------------------------------------------------------\n")
                    file_name,extension = splitext(file)
                    #print(extension)
                    fullFileName = root+"\\"+file
                    if(extension in ".jpg" or extension in ".png" or extension in ".jpeg"):                    
                        im = Image.open(fullFileName) # the second one 
                        txt = pytesseract.image_to_string(im)
                        print(txt)
                        text_file.write(txt)
                        print(root+"\\"+file)
                    elif (extension in ".pdf" or extension in ".PDF"):
                        pdfFileObj = open(fullFileName,'rb')     #'rb' for read binary mode
                        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                        pdfReader.numPages
                        pageObj = pdfReader.getPage(0)
                        print(pageObj.extractText())
                        text_file.write(pageObj.extractText())
                    else:
                        continue
                except:
                    continue    
    else:
        print("Path does not exists")

im = Image.open(".\EBSUploadedDocuments\\608498\\PAN.jpg") # the second one 
txt = pytesseract.image_to_string(im)
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
print(txt)
print(os.listdir())

traverse_directories(".\EBSUploadedDocuments")
text_file.close()



