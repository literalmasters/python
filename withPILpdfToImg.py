# .\EBSUploadedDocuments\\606049\\316781-6-7154283_-_Tushar_Gupta_-_Final.pdf
import PyPDF2
import struct
import io
from PIL import Image
"""
Links:
PDF format: http://www.adobe.com/content/dam/Adobe/en/devnet/acrobat/pdfs/pdf_reference_1-7.pdf
CCITT Group 4: https://www.itu.int/rec/dologin_pub.asp?lang=e&id=T-REC-T.6-198811-I!!PDF-E&type=items
Extract images from pdf: http://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python
Extract images coded with CCITTFaxDecode in .net: http://stackoverflow.com/questions/2641770/extracting-image-from-pdf-with-ccittfaxdecode-filter
TIFF format and tags: http://www.awaresystems.be/imaging/tiff/faq.html
"""


def tiff_header_for_CCITT(width, height, img_size, CCITT_group=4):
    tiff_header_struct = '<' + '2s' + 'h' + 'l' + 'h' + 'hhll' * 8 + 'h'
    return struct.pack(tiff_header_struct,
                       b'II',  # Byte order indication: Little indian
                       42,  # Version number (always 42)
                       8,  # Offset to first IFD
                       8,  # Number of tags in IFD
                       256, 4, 1, width,  # ImageWidth, LONG, 1, width
                       257, 4, 1, height,  # ImageLength, LONG, 1, lenght
                       258, 3, 1, 1,  # BitsPerSample, SHORT, 1, 1
                       259, 3, 1, CCITT_group,  # Compression, SHORT, 1, 4 = CCITT Group 4 fax encoding
                       262, 3, 1, 0,  # Threshholding, SHORT, 1, 0 = WhiteIsZero
                       273, 4, 1, struct.calcsize(tiff_header_struct),  # StripOffsets, LONG, 1, len of header
                       278, 4, 1, height,  # RowsPerStrip, LONG, 1, lenght
                       279, 4, 1, img_size,  # StripByteCounts, LONG, 1, size of image
                       0  # last IFD
                       )
# def pdf_page_to_jpg(pdf_filename):
pdf_filename = '.\EBSUploadedDocuments\\606049\\_Employment2LOA.pdf'
pdf_file = open(pdf_filename, 'rb')
cond_scan_reader = PyPDF2.PdfFileReader(pdf_file)
for i in range(0, cond_scan_reader.getNumPages()):
    page = cond_scan_reader.getPage(i)
    xObject = page['/Resources']['/XObject'].getObject()
    for obj in xObject:
        if xObject[obj]['/Subtype'] == '/Image':                
            if xObject[obj]['/Filter'] == '/CCITTFaxDecode':
                if xObject[obj]['/DecodeParms']['/K'] == -1:
                    CCITT_group = 4
                else:
                    CCITT_group = 3
                width = xObject[obj]['/Width']
                height = xObject[obj]['/Height']
                data = xObject[obj]._data  # sorry, getData() does not work for CCITTFaxDecode
                img_size = len(data)
                print(img_size)
                if(img_size>1000):
                    tiff_header = tiff_header_for_CCITT(width, height, img_size, CCITT_group)
                    img_name = obj[1:] + '.jpg'
                    with open(img_name, 'wb') as img_file:
                        img_file.write(tiff_header + data)
                    im = Image.open(io.BytesIO(tiff_header + data))
                
pdf_file.close()


# def traverse_directories(dirName):
#     if(os.path.exists(dirName)):
        
#         for root, dirs, files in os.walk(dirName):
#             path = root.split(os.sep)
#             print((len(path) - 1) * '---', os.path.basename(root))
#             for file in files:
#                 print(len(path) * '---', file)
#                 text_file.write("\n\n\n==========================================================================================")
#                 text_file.write("\n==========================================================================================")
#                 text_file.write("\n" + file+"\n")
#                 text_file.write("------------------------------------------------------------------------------------------\n")
#                 file_name,extension = splitext(file)
#                 #print(extension)
#                 fullFileName = root+"\\"+file
#                 if (extension in ".pdf" or extension in ".PDF"):
                    
#                     pdfFileObj = open(fullFileName,'rb')     #'rb' for read binary mode
#                     pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#                     pdfReader.numPages
#                     pageObj = pdfReader.getPage(0)
#                     pageCount = pdfReader.numPages
#                     im = pdf_page_to_jpg(fullFileName)
#                     open(im)
#                     # while pageCount>=0:
#                     #     pageObj = pdfReader.getPage(pageCount-1)
#                     #     pdf_page_to_png(pageObj)
#                     #     pageCount = pageCount-1
#                     # print(pageObj.extractText())
#                     # text_file.write(pageObj.extractText())
#                 else:
#                     continue
                
#     else:
#         print("Path does not exists")

# traverse_directories(".\EBSUploadedDocuments")
# text_file.close()