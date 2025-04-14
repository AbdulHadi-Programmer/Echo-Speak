## summary.py :
# 🔍 What are LSA and LexRank?
- Both LSA (Latent Semantic Analysis) and LexRank are summarization techniques used in NLP.

1. **LSA (Latent Semantic Analysis)**
- A `mathematical approach` that analyzes relationships between words in a document.
- Uses `Singular Value Decomposition (SVD)` to find the most relevant sentences.
- Works well when text has strong `thematic structure`.
- `Downside:` It may sometimes generate summaries that are less coherent.

2. **LexRank**
- A `graph-based method` (similar to Google's PageRank).
- Sentences are `nodes` in a graph, and edges represent similarity between sentences.
- Sentences with the `highest importance` score are selected.
- Works well for `long documents`.
- `More reliable` than LSA but slower.


**📌 Which one to use?**
1. **LSA →** Best for structured text (academic papers, well-formatted articles).
2. **LexRank →** Best for noisy or large documents (news, long PDFs, research papers).
