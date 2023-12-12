import re
from PyPDF2 import PdfReader


class PaperHandling:
    """
    Class to handle input papers which we wish to prompt upon 


    atributes
    -------------
    atr: 


    public_methods
    --------------
    mthd: 

    """
    def __init__(self, paper_name:str):
        """
        method to set attributes of the PaperHandling class
        :param paper_name: the name of the paper in question
        """
        self.paper_name = paper_name

    def __repr__(self):
        """
        repr method
        """
        return (f'{self.__class__.__name__}('f'{self.paper_name!r})')
    
    def text_parse(self, extracted_text:str):
        """
        helper method to parse extracted text 
        :param extracted_text: the extracted text upon which to apply the parser
        """
        

    def unwrap_pdf(self):
        """
        method to unwrap pdf into data we want
        """
        reader = PdfReader(f"./papers/{self.paper_name}.pdf")
        page = reader.pages[0]
        print(page.extract_text())

    def unwrap_images(self):
        """
        method to unwrap images
        """

    def reference_web(self):
        """
        method to implement the reference web
        """


class LLM_Agent:
    """
    
    """



paper = PaperHandling("UJPR-4-1-RW1")
paper.unwrap_pdf()


