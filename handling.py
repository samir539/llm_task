import re
from PyPDF2 import PdfReader
import os
import openai


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
        
    #struggles with certain characters
    def unwrap_pdf(self):
        """
        method to unwrap pdf into data we want
        """
        self.content = ""
        reader = PdfReader(f"./papers/{self.paper_name}.pdf")
        for i in range(0, len(reader.pages)):
            self.content += reader.pages[i].extract_text() 
        self.content = str(self.content.encode("utf-8", errors="replace"))
        self.content = self.content.replace("\\n","\n")
        print("the type of bb is ", self.content)
        
        
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
    class to generate an LLM agent which is used to analyse the text in question 

    """
    def __init__(self,temp):
        self.temp = temp

    @staticmethod
    def read_api_key(file_path='keys.txt'):
        with open(file_path, 'r') as file:
            api_key = file.read().strip()
        return api_key

    def openai_verify(self):
        key = self.read_api_key()
        openai.api_key = os.getenv(key) or key
        print(openai.Engine.list())

        



paper = PaperHandling("UJPR-4-1-RW1")
paper.unwrap_pdf()

llm = LLM_Agent(10)
llm.openai_verify()



