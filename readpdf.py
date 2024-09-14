#pip install pyChatGPT==0.4.3.3 or > 0.4.3.3
#pip install streamlit

import streamlit as st
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from  langchain.text_splitter import RecursiveCharacterTextSplitter

with st.sidebar:
    st.title("Hi ")
    st.markdown ("""
    [test link goto google ]("www.google.com")
    
    
    """)
    add_vertical_space(5)
    
def main():
      st.header("please upload your pdf ...",divider=True)
      pdf=st.file_uploader("upload your pdf",type="pdf")
      if pdf is not None: 
       pdf_reader =PdfReader(pdf)
         
       text=""
       for page in pdf_reader.pages:
             text += page.extract_text()
       text_spiliter =  RecursiveCharacterTextSplitter(
            chunk_size=1000 ,
            chunk_overlap=150 ,
            length_function=len
        
         )
       chunk = text_spiliter.split_text(text=text)
       st.write(chunk)

if __name__ == '__main__':
     main()


