# audiobook creator by 'laughing coder'
import gtts
import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


# parse text from PDF
def convert_to_txt(path):
    resource_manager = PDFResourceManager()
    codec = 'utf-8'
    la_params = LAParams()

    with io.StringIO() as return_str:
        with TextConverter(resource_manager, return_str, codec=codec,
                           laparams=la_params) as device:
            with open(path, 'rb') as fp:
                interpreter = PDFPageInterpreter(resource_manager, device)
                password = ""
                max_pages = 0
                caching = True
                page_os = set()

                for page in PDFPage.get_pages(fp,
                                              page_os,
                                              maxpages=max_pages,
                                              password=password,
                                              caching=caching,
                                              check_extractable=True):
                    interpreter.process_page(page)

                return return_str.getvalue()


# create mp3 file
def create_book():
    lang_choice = int(input('Please enter 1 for russian or 2 for english: '))
    if lang_choice == 1:
        tts = gtts.gTTS(convert_to_txt(input('Please enter path to pdf file: ')), lang='ru', slow=False)
    else:
        tts = gtts.gTTS(convert_to_txt(input('Please enter path to pdf file: ')), lang='en', slow=False)
    tts.save('audiobook.mp3')


if __name__ == "__main__":
    create_book()
