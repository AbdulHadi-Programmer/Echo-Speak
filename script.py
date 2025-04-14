# import streamlit as st
# import PyPDF2
# import docx
# import nltk
# from nltk.tokenize import sent_tokenize
# from collections import Counter
# import random

# # Download NLTK resources
# nltk.download('punkt')

# def read_pdf(file):
#     pdf_reader = PyPDF2.PdfReader(file)
#     text = "".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
#     return text

# def read_docx(file):
#     doc = docx.Document(file)
#     text = "\n".join([para.text for para in doc.paragraphs])
#     return text

# def read_txt(file):
#     return file.read().decode("utf-8")

# def extract_summary(text, length='medium'):
#     sentences = sent_tokenize(text)
#     summary_length = {'short': 0.2, 'medium': 0.4, 'long': 0.6}
#     num_sentences = max(1, int(len(sentences) * summary_length[length]))
#     return " ".join(sentences[:num_sentences])

# def generate_mcqs(text, num_questions=5):
#     sentences = sent_tokenize(text)
#     words = text.split()
#     common_words = [word for word, freq in Counter(words).most_common(50) if word.isalpha()]
    
#     mcqs = []
#     for _ in range(num_questions):
#         if not common_words:
#             break
#         word = random.choice(common_words)
#         common_words.remove(word)
#         sentence = next((s for s in sentences if word in s), None)
#         if sentence:
#             mcqs.append({
#                 'question': sentence.replace(word, '____'),
#                 'answer': word,
#                 'options': random.sample([word] + random.sample(words, 3), 4)
#             })
#     return mcqs

# def main():
#     st.title("Text Summarizer & MCQ Generator")
#     uploaded_file = st.file_uploader("Upload a .pdf, .docx, or .txt file", type=["pdf", "docx", "txt"])
    
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
        
#         st.subheader("Summarization")
#         summary_length = st.selectbox("Choose summary length", ["short", "medium", "long"])
#         summary = extract_summary(text, length=summary_length)
#         st.text_area("Generated Summary:", summary, height=200)
        
#         st.subheader("MCQ Generation")
#         num_questions = st.slider("Number of MCQs", 1, 10, 5)
#         mcqs = generate_mcqs(text, num_questions)
#         for i, mcq in enumerate(mcqs, 1):
#             st.write(f"**Q{i}: {mcq['question']}**")
#             for option in mcq['options']:
#                 st.write(f"- {option}")
#             st.write(f"**Answer:** {mcq['answer']}")

# if __name__ == "__main__":
#     main()
#########################################################################################
# import streamlit as st
# import PyPDF2
# import docx
# import nltk
# from nltk.tokenize import sent_tokenize
# from collections import Counter
# import random
# import pyperclip

# # Download NLTK resources
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

# def extract_summary(text, length='medium'):
#     sentences = sent_tokenize(text)
#     summary_length = {'short': 0.2, 'medium': 0.4, 'long': 0.6}
#     num_sentences = max(1, int(len(sentences) * summary_length[length]))
#     summary = " ".join(sentences[:num_sentences])
    
#     if length in ['medium', 'long']:
#         summary = f"# Summary\n## Main Points\n{summary}"
#     return summary

# def generate_mcqs(text, num_questions=5):
#     sentences = sent_tokenize(text)
#     words = text.split()
#     common_words = [word for word, freq in Counter(words).most_common(50) if word.isalpha()]
    
#     mcqs = []
#     used_sentences = set()
    
#     for _ in range(num_questions):
#         if not common_words:
#             break
#         word = random.choice(common_words)
#         common_words.remove(word)
#         sentence = next((s for s in sentences if word in s and s not in used_sentences), None)
        
#         if sentence:
#             used_sentences.add(sentence)
#             question = sentence.replace(word, '____', 1)  # Replace only once
#             options = list(set([word] + random.sample(words, 3)))[:4]
#             random.shuffle(options)
#             mcqs.append({'question': question, 'answer': word, 'options': options})
    
#     return mcqs if mcqs else "Not enough data for MCQs. Try increasing text length."

# def main():
#     st.title("Text Summarizer & MCQ Generator")
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
        
#         st.subheader("Summarization")
#         summary_length = st.selectbox("Choose summary length", ["short", "medium", "long"])
#         summary = extract_summary(text, length=summary_length)
        
#         st.text_area("Generated Summary:", summary, height=200)
#         if st.button("Copy Summary"):
#             pyperclip.copy(summary)
#             st.success("Summary copied!")
        
#         st.subheader("MCQ Generation")
#         num_questions = st.slider("Number of MCQs", 5, 25, 10)
#         mcqs = generate_mcqs(text, num_questions)
        
#         if isinstance(mcqs, str):
#             st.warning(mcqs)
#         else:
#             for i, mcq in enumerate(mcqs, 1):
#                 st.write(f"**Q{i}: {mcq['question']}**")
#                 for option in mcq['options']:
#                     st.write(f"- {option}")
#                 st.write(f"**Answer:** {mcq['answer']}")

# if __name__ == "__main__":
#     main()
########################################################################################
# import streamlit as st
# import PyPDF2
# import docx
# import nltk
# from nltk.tokenize import sent_tokenize
# from collections import Counter
# import random
# import pyperclip

# # Download NLTK resources
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

# def extract_summary(text, length='medium'):
#     sentences = sent_tokenize(text)
#     summary_length = {'short': 0.2, 'medium': 0.4, 'long': 0.6}
#     num_sentences = max(1, int(len(sentences) * summary_length[length]))
#     summary = " ".join(sentences[:num_sentences])
    
#     if length in ['medium', 'long']:
#         summary = f"# Summary\n## Main Points\n{summary}"
#     return summary

# def generate_mcqs(text, num_questions=10):
#     sentences = sent_tokenize(text)
#     words = text.split()
#     common_words = [word for word, freq in Counter(words).most_common(100) if word.isalpha()]
    
#     mcqs = []
#     used_sentences = set()
    
#     while len(mcqs) < num_questions and common_words:
#         word = random.choice(common_words)
#         common_words.remove(word)
#         sentence = next((s for s in sentences if word in s and s not in used_sentences), None)
        
#         if sentence:
#             used_sentences.add(sentence)
#             question = sentence.replace(word, '____', 1)
#             options = list(set([word] + random.sample(words, min(3, len(words)))))[:4]
#             random.shuffle(options)
#             mcqs.append({'question': question, 'answer': word, 'options': options})
    
#     return mcqs if mcqs else "Not enough data for MCQs. Try increasing text length."

# def main():
#     st.title("Text Summarizer & MCQ Generator")
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
        
#         st.subheader("Summarization")
#         summary_length = st.selectbox("Choose summary length", ["short", "medium", "long"])
#         summary = extract_summary(text, length=summary_length)
        
#         st.text_area("Generated Summary:", summary, height=200)
#         if st.button("Copy Summary"):
#             pyperclip.copy(summary)
#             st.success("Summary copied!")
        
#         st.subheader("MCQ Generation")
#         num_questions = st.slider("Number of MCQs", 5, 25, 10)
#         mcqs = generate_mcqs(text, num_questions)
        
#         if isinstance(mcqs, str):
#             st.warning(mcqs)
#         else:
#             answers = []
#             for i, mcq in enumerate(mcqs, 1):
#                 st.write(f"**Q{i}: {mcq['question']}**")
#                 for option in mcq['options']:
#                     st.write(f"- {option}")
#                 answers.append(f"Q{i}: {mcq['question']} Answer: {mcq['answer']}")
            
#             if st.button("Show Answers"):
#                 for ans in answers:
#                     st.write(ans)

# if __name__ == "__main__":
#     main()
#############################################################################################################################

# import streamlit as st
# import PyPDF2
# import docx
# import nltk
# from nltk.tokenize import sent_tokenize
# from collections import Counter
# import random
# import pyperclip

# # Download NLTK resources
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

# def extract_summary(text, length='medium'):
#     sentences = sent_tokenize(text)
#     summary_length = {'short': 0.2, 'medium': 0.4, 'long': 0.6}
#     num_sentences = max(1, int(len(sentences) * summary_length[length]))
#     summary = " ".join(sentences[:num_sentences])
    
#     if length in ['medium', 'long']:
#         summary = f"# Summary\n## Main Points\n{summary}"
#     return summary

# def generate_mcqs(text, num_questions=10):
#     sentences = sent_tokenize(text)
#     words = text.split()
#     common_words = [word for word, freq in Counter(words).most_common(200) if word.isalpha()]
    
#     mcqs = []
#     used_sentences = set()
#     attempt_count = 0
    
#     while len(mcqs) < num_questions and common_words and attempt_count < num_questions * 3:
#         word = random.choice(common_words)
#         common_words.remove(word)
#         sentence = next((s for s in sentences if word in s and s not in used_sentences), None)
        
#         if sentence:
#             used_sentences.add(sentence)
#             question = sentence.replace(word, '____', 1)
#             options = list(set([word] + random.sample(words, min(3, len(words)))))[:4]
#             random.shuffle(options)
#             mcqs.append({'question': question, 'answer': word, 'options': options})
#         attempt_count += 1
    
#     return mcqs if mcqs else "Not enough data for MCQs. Try increasing text length."

# def main():
#     st.title("Text Summarizer & MCQ Generator")
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
        
#         st.subheader("Summarization")
#         summary_length = st.selectbox("Choose summary length", ["short", "medium", "long"])
#         summary = extract_summary(text, length=summary_length)
        
#         st.text_area("Generated Summary:", summary, height=200)
#         if st.button("Copy Summary"):
#             pyperclip.copy(summary)
#             st.success("Summary copied!")
        
#         st.subheader("MCQ Generation")
#         num_questions = st.slider("Number of MCQs", 5, 25, 10)
#         mcqs = generate_mcqs(text, num_questions)
        
#         if isinstance(mcqs, str):
#             st.warning(mcqs)
#         else:
#             answers = []
#             for i, mcq in enumerate(mcqs, 1):
#                 st.write(f"**Q{i}: {mcq['question']}**")
#                 for option in mcq['options']:
#                     st.write(f"- {option}")
#                 answers.append(f"Q{i}: {mcq['question']} Answer: {mcq['answer']}")
            
#             if st.button("Show Answers"):
#                 for ans in answers:
#                     st.write(ans)

# if __name__ == "__main__":
#     main()

# # It is working good but the problem the program has that is it generate new mcqs whenever we click show answer instead its show same question correct answer and convert the button into Hide Answer and hide it without changing it original content 

## Working but generate less num of mcqs : 
# import streamlit as st
# import PyPDF2
# import docx
# import nltk
# from nltk.tokenize import sent_tokenize
# from collections import Counter
# import random
# import pyperclip

# # Download NLTK resources
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

# def extract_summary(text, length='medium'):
#     sentences = sent_tokenize(text)
#     summary_length = {'short': 0.2, 'medium': 0.4, 'long': 0.6}
#     num_sentences = max(1, int(len(sentences) * summary_length[length]))
#     summary = " ".join(sentences[:num_sentences])
    
#     if length in ['medium', 'long']:
#         summary = f"# Summary\n## Main Points\n{summary}"
#     return summary

# def generate_mcqs(text, num_questions=10):
#     sentences = sent_tokenize(text)
#     words = text.split()
#     common_words = [word for word, freq in Counter(words).most_common(200) if word.isalpha()]
    
#     mcqs = []
#     used_sentences = set()
#     attempt_count = 0
    
#     while len(mcqs) < num_questions and common_words and attempt_count < num_questions * 3:
#         word = random.choice(common_words)
#         common_words.remove(word)
#         sentence = next((s for s in sentences if word in s and s not in used_sentences), None)
        
#         if sentence:
#             used_sentences.add(sentence)
#             question = sentence.replace(word, '____', 1)
#             options = list(set([word] + random.sample(words, min(3, len(words)))))[:4]
#             random.shuffle(options)
#             mcqs.append({'question': question, 'answer': word, 'options': options})
#         attempt_count += 1
    
#     return mcqs if mcqs else "Not enough data for MCQs. Try increasing text length."

# def main():
#     st.title("Text Summarizer & MCQ Generator")
    
#     if "mcqs" not in st.session_state:
#         st.session_state.mcqs = []
#         st.session_state.show_answers = False

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
        
#         st.subheader("Summarization")
#         summary_length = st.selectbox("Choose summary length", ["short", "medium", "long"])
#         summary = extract_summary(text, length=summary_length)
        
#         st.text_area("Generated Summary:", summary, height=200)
#         if st.button("Copy Summary"):
#             pyperclip.copy(summary)
#             st.success("Summary copied!")
        
#         st.subheader("MCQ Generation")
#         num_questions = st.slider("Number of MCQs", 5, 25, 10)

#         if st.button("Generate MCQs"):
#             st.session_state.mcqs = generate_mcqs(text, num_questions)
#             st.session_state.show_answers = False  # Reset answer visibility

#         if st.session_state.mcqs and isinstance(st.session_state.mcqs, list):
#             answers = []
#             for i, mcq in enumerate(st.session_state.mcqs, 1):
#                 st.write(f"**Q{i}: {mcq['question']}**")
#                 for option in mcq['options']:
#                     st.write(f"- {option}")
#                 answers.append(f"Q{i}: {mcq['question']} Answer: {mcq['answer']}")

#             if st.button("Show Answers" if not st.session_state.show_answers else "Hide Answers"):
#                 st.session_state.show_answers = not st.session_state.show_answers

#             if st.session_state.show_answers:
#                 for ans in answers:
#                     st.write(ans)

# if __name__ == "__main__":
#     main()

## 




# import streamlit as st
# import PyPDF2
# import docx
# import nltk
# from nltk.tokenize import sent_tokenize, word_tokenize
# from collections import Counter
# import random
# import pyperclip

# # Download NLTK resources
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

# def extract_summary(text, length='medium'):
#     sentences = sent_tokenize(text)
#     summary_length = {'short': 0.2, 'medium': 0.4, 'long': 0.6}
#     num_sentences = max(1, int(len(sentences) * summary_length[length]))
#     summary = " ".join(sentences[:num_sentences])
    
#     if length in ['medium', 'long']:
#         summary = f"# Summary\n## Main Points\n{summary}"
#     return summary

# def generate_mcqs(text, num_questions=10):
#     sentences = sent_tokenize(text)
#     words = word_tokenize(text)
    
#     # Use only alphabetic words and filter stopwords
#     words = [word for word in words if word.isalpha()]
    
#     # Select most common words with at least 4 letters (better for MCQs)
#     common_words = [word for word, freq in Counter(words).most_common(500) if len(word) > 3]

#     mcqs = []
#     used_sentences = set()
#     attempt_count = 0
    
#     while len(mcqs) < num_questions and common_words and attempt_count < num_questions * 3:
#         word = random.choice(common_words)
#         common_words.remove(word)
#         sentence = next((s for s in sentences if word in s and s not in used_sentences), None)
        
#         if sentence:
#             used_sentences.add(sentence)
#             question = sentence.replace(word, '____', 1)
#             options = list(set([word] + random.sample(words, min(3, len(words)))))[:4]
#             random.shuffle(options)
#             mcqs.append({'question': question, 'answer': word, 'options': options})
#         attempt_count += 1
    
#     return mcqs if mcqs else "Not enough data for MCQs. Try increasing text length."

# def main():
#     st.title("Text Summarizer & MCQ Generator")
    
#     if "mcqs" not in st.session_state:
#         st.session_state.mcqs = []
#         st.session_state.show_answers = False

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
        
#         st.subheader("Summarization")
#         summary_length = st.selectbox("Choose summary length", ["short", "medium", "long"])
#         summary = extract_summary(text, length=summary_length)
        
#         st.text_area("Generated Summary:", summary, height=200)
#         if st.button("Copy Summary"):
#             pyperclip.copy(summary)
#             st.success("Summary copied!")
        
#         st.subheader("MCQ Generation")
#         num_questions = st.slider("Number of MCQs", 5, 25, 10)

#         if st.button("Generate MCQs"):
#             st.session_state.mcqs = generate_mcqs(text, num_questions)  # Use Full Text instead of Summary
#             st.session_state.show_answers = False  # Reset answer visibility

#         if st.session_state.mcqs and isinstance(st.session_state.mcqs, list):
#             answers = []
#             for i, mcq in enumerate(st.session_state.mcqs, 1):
#                 st.write(f"**Q{i}: {mcq['question']}**")
#                 for option in mcq['options']:
#                     st.write(f"- {option}")
#                 answers.append(f"Q{i}: {mcq['question']} Answer: {mcq['answer']}")

#             if st.button("Show Answers" if not st.session_state.show_answers else "Hide Answers"):
#                 st.session_state.show_answers = not st.session_state.show_answers

#             if st.session_state.show_answers:
#                 for ans in answers:
#                     st.write(ans)

# if __name__ == "__main__":
#     main()

import streamlit as st
import PyPDF2
import docx
from pptx import Presentation
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
import random
import pyperclip

# Download NLTK resources
nltk.download('punkt')

def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for i, page in enumerate(pdf_reader.pages):
        page_text = page.extract_text()
        if page_text:
            text += f"\n--- Page {i+1} ---\n{page_text}\n"
    return text

def read_docx(file):
    doc = docx.Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def read_txt(file):
    return file.read().decode("utf-8")

def read_pptx(file):
    prs = Presentation(file)
    text = "\n".join([shape.text for slide in prs.slides for shape in slide.shapes if hasattr(shape, "text")])
    return text

def extract_summary(text, length='medium'):
    sentences = sent_tokenize(text)
    summary_length = {'short': 0.2, 'medium': 0.4, 'long': 0.6}
    num_sentences = max(1, int(len(sentences) * summary_length[length]))
    summary = " ".join(sentences[:num_sentences])
    
    if length in ['medium', 'long']:
        summary = f"# Summary\n## Main Points\n{summary}"
    return summary

def generate_mcqs(text, num_questions=10):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    words = [word for word in words if word.isalpha() and len(word) > 3]
    common_words = [word for word, freq in Counter(words).most_common(500)]
    
    mcqs = []
    used_sentences = set()
    attempt_count = 0
    
    while len(mcqs) < num_questions and common_words and attempt_count < num_questions * 3:
        word = random.choice(common_words)
        common_words.remove(word)
        sentence = next((s for s in sentences if word in s and s not in used_sentences), None)
        
        if sentence:
            used_sentences.add(sentence)
            question = sentence.replace(word, '____', 1)
            options = list(set([word] + random.sample(words, min(3, len(words)))))[:4]
            random.shuffle(options)
            mcqs.append({'question': question, 'answer': word, 'options': options})
        attempt_count += 1
    
    return mcqs if mcqs else "Not enough data for MCQs. Try increasing text length."

def main():
    st.title("Text Summarizer & MCQ Generator")
    
    if "mcqs" not in st.session_state:
        st.session_state.mcqs = []
        st.session_state.show_answers = False

    uploaded_file = st.file_uploader("Upload a PDF, DOCX, TXT, or PPTX file", type=["pdf", "docx", "txt", "pptx"])
    
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
            st.error("Unsupported file format")
            return
        
        st.subheader("Summarization")
        summary_length = st.selectbox("Choose summary length", ["short", "medium", "long"])
        summary = extract_summary(text, length=summary_length)
        
        st.text_area("Generated Summary:", summary, height=200)
        if st.button("Copy Summary"):
            pyperclip.copy(summary)
            st.success("Summary copied!")
        
        st.subheader("MCQ Generation")
        num_questions = st.slider("Number of MCQs", 5, 25, 10)

        if st.button("Generate MCQs"):
            st.session_state.mcqs = generate_mcqs(text, num_questions)
            st.session_state.show_answers = False

        if st.session_state.mcqs and isinstance(st.session_state.mcqs, list):
            answers = []
            for i, mcq in enumerate(st.session_state.mcqs, 1):
                st.write(f"**Q{i}: {mcq['question']}**")
                for option in mcq['options']:
                    st.write(f"- {option}")
                answers.append(f"Q{i}: {mcq['question']} \n \t Answer: {mcq['answer']}")

            if st.button("Show Answers" if not st.session_state.show_answers else "Hide Answers"):
                st.session_state.show_answers = not st.session_state.show_answers

            if st.session_state.show_answers:
                for ans in answers:
                    st.write(ans)

if __name__ == "__main__":
    main()