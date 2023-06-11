from PyPDF2 import PdfReader
import pyttsx3
reader = PdfReader("D:\Books\PDFs\POH.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
count = 0
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.say(text)
engine.runAndWait()

# for image_file_object in page.images:
#     with open(str(count) + image_file_object.name, "wb") as fp:
#         fp.write(image_file_object.data)
#         count += 1
# print(text)

