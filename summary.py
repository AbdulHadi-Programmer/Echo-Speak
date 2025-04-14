# import streamlit as st
# import PyPDF2
# import docx
# import nltk
# from nltk.tokenize import sent_tokenize
# import openai
# import pyperclip

# # Download required NLTK resources
# nltk.download('punkt')

# def read_pdf(file):
#     pdf_reader = PyPDF2.PdfReader(file)
#     text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
#     return text

# def read_docx(file):
#     doc = docx.Document(file)
#     text = "\n".join([para.text for para in doc.paragraphs])
#     return text

# def read_txt(file):
#     return file.read().decode("utf-8")

# def extractive_summary(text, ratio=0.3):
#     sentences = sent_tokenize(text)
#     num_sentences = max(1, int(len(sentences) * ratio))
#     return " ".join(sentences[:num_sentences])

# def abstractive_summary(text):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "system", "content": "Summarize the following text:"},
#                   {"role": "user", "content": text}]
#     )
#     return response["choices"][0]["message"]["content"].strip()

# def main():
#     st.title("Document Summarizer (Extractive & Abstractive)")
#     uploaded_file = st.file_uploader("Upload a PDF, DOCX, or TXT file", type=["pdf", "docx", "txt"])
    
#     if uploaded_file:
#         file_type = uploaded_file.type
#         if "pdf" in file_type:
#             text = read_pdf(uploaded_file)
#         elif "word" in file_type or "docx" in uploaded_file.name:
#             text = read_docx(uploaded_file)
#         elif "text" in file_type:
#             text = read_txt(uploaded_file)
#         else:
#             st.error("Unsupported file format")
#             return
        
#         summary_type = st.selectbox("Select Summary Type", ["Extractive", "Abstractive"])
        
#         if st.button("Generate Summary"):
#             if summary_type == "Extractive":
#                 summary = extractive_summary(text)
#             else:
#                 summary = abstractive_summary(text)
            
#             st.subheader("Generated Summary:")
#             st.text_area("Summary", summary, height=200)
            
#             if st.button("Copy Summary"):
#                 pyperclip.copy(summary)
#                 st.success("Summary copied!")

# if __name__ == "__main__":
#     main()
############################################3

# Perfect Working but some feature are added in next version 
# import streamlit as st
# import PyPDF2
# import docx
# import nltk
# from nltk.tokenize import sent_tokenize
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer
# from sumy.summarizers.lex_rank import LexRankSummarizer

# # Download NLTK resources
# nltk.download('punkt')

# # Function to read PDF
# def read_pdf(file):
#     pdf_reader = PyPDF2.PdfReader(file)
#     text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
#     return text

# # Function to read DOCX
# def read_docx(file):
#     doc = docx.Document(file)
#     text = "\n".join([para.text for para in doc.paragraphs])
#     return text

# # Function to read TXT
# def read_txt(file):
#     return file.read().decode("utf-8")

# # Extractive Summarization using NLTK
# def extractive_summary(text, num_sentences=5):
#     sentences = sent_tokenize(text)
#     return " ".join(sentences[:num_sentences])

# # Abstractive Summarization using Sumy (LSA or LexRank)
# def abstractive_summary(text, num_sentences=5, method="lsa"):
#     parser = PlaintextParser.from_string(text, Tokenizer("english"))
#     if method == "lsa":
#         summarizer = LsaSummarizer()  # LSA Summarizer
#     else:
#         summarizer = LexRankSummarizer()  # LexRank Summarizer

#     summary = summarizer(parser.document, num_sentences)
#     return " ".join(str(sentence) for sentence in summary)

# # Streamlit App
# def main():
#     st.title("Text Summarization (Extractive & Abstractive)")
    
#     uploaded_file = st.file_uploader("Upload a PDF, DOCX, or TXT file", type=["pdf", "docx", "txt"])
    
#     if uploaded_file:
#         file_type = uploaded_file.type
#         if "pdf" in file_type:
#             text = read_pdf(uploaded_file)
#         elif "word" in file_type or "docx" in uploaded_file.name:
#             text = read_docx(uploaded_file)
#         elif "text" in file_type:
#             text = read_txt(uploaded_file)
#         else:
#             st.error("Unsupported file format")
#             return

#         # Select summary type
#         summary_type = st.radio("Choose summary type:", ["Extractive", "Abstractive"])
        
#         num_sentences = st.slider("Select number of sentences:", 3, 20, 5)

#         if summary_type == "Extractive":
#             summary = extractive_summary(text, num_sentences)
#         else:
#             method = st.radio("Choose abstractive method:", ["LSA", "LexRank"])
#             summary = abstractive_summary(text, num_sentences, method.lower())

#         st.subheader("Generated Summary")
#         st.text_area("Summary:", summary, height=200)

# if __name__ == "__main__":
#     main()

##############################################################################
import streamlit as st
import PyPDF2
import docx
import nltk
from nltk.tokenize import sent_tokenize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import pyperclip
from pptx import Presentation

# Download required NLTK resources
nltk.download('punkt')

def read_pptx(file):
    prs = Presentation(file)
    text = "\n".join([
        shape.text for slide in prs.slides for shape in slide.shapes if hasattr(shape, "text")
    ])
    return text

# Function to read PDF
def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    return text

# Function to read DOCX
def read_docx(file):
    doc = docx.Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Function to read TXT
def read_txt(file):
    return file.read().decode("utf-8")

# Extractive Summarization
def extractive_summary(text, num_sentences=5):
    sentences = sent_tokenize(text)
    return " ".join(sentences[:num_sentences])

# Abstractive Summarization using Sumy (LSA / LexRank)
def abstractive_summary(text, num_sentences=5, method="lsa"):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer() if method == "lsa" else LexRankSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return " ".join(str(sentence) for sentence in summary)

# Streamlit App
def main():
    st.title("📝 AI-Powered Summarizer")
    
    uploaded_file = st.file_uploader("📂 Upload a PDF, DOCX, TXT, or PPTX file", type=["pdf", "docx", "txt", "pptx"])

    if uploaded_file:
        file_type = uploaded_file.type
        if "pdf" in file_type:
            text = read_pdf(uploaded_file)
        elif "word" in file_type or "docx" in uploaded_file.name:
            text = read_docx(uploaded_file)
        elif "text" in file_type:
            text = read_txt(uploaded_file)
        elif "pptx" in uploaded_file.name:
            text = read_pptx(uploaded_file)
        else:
            st.error("❌ Unsupported file format")
            return


        # Select summary type
        summary_type = st.radio("🔍 Choose summary type:", ["Extractive", "Abstractive"])
        
        num_sentences = st.slider("✂ Select number of sentences:", 3, 20, 5)

        if summary_type == "Extractive":
            summary = extractive_summary(text, num_sentences)
        else:
            method = st.radio("📌 Choose abstractive method:", ['lsa',"lexrank"])
            st.write("LSA -- Best for structured text (academic papers, well-formatted articles)")
            st.write("LexRank -- Best for noisy or large documents (news, long PDFs, research papers)")
            summary = abstractive_summary(text, num_sentences, method.lower())

        st.subheader("📜 Generated Summary")
        st.text_area("📝 Summary:", summary, height=200)

        # Copy Button
        if st.button("📋 Copy Summary"):
            pyperclip.copy(summary)
            st.success("✅ Summary copied to clipboard!")

        # Download Button
        if st.button("💾 Download Summary"):
            with open("summary.txt", "w", encoding="utf-8") as f:
                f.write(summary)
            st.download_button(label="📥 Download", data=summary, file_name="summary.txt", mime="text/plain")

if __name__ == "__main__":
    main()





long_text = """
Artificial Intelligence (AI) is transforming the world. From self-driving cars to advanced chatbots, AI is integrated into daily life. 
Machine Learning (ML) and Deep Learning (DL) are subsets of AI that improve decision-making. Companies use AI for automation, 
reducing costs, and increasing efficiency. AI also raises ethical concerns regarding data privacy and job displacement.
Governments are working on AI regulations to ensure responsible development. As AI grows, research focuses on making AI systems 
more interpretable and fair. AI’s future holds promise, but careful implementation is needed to avoid risks.
"""

lsa_summary = abstractive_summary(long_text, 3, method="lsa")
lexrank_summary = abstractive_summary(long_text, 3, method="lexrank")

print("LSA Summary:\n", lsa_summary)
print("\nLexRank Summary:\n", lexrank_summary)
