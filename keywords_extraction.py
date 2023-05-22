import pandas as pd
import streamlit as st
from keybert import KeyBERT


#@st.cache(allow_output_mutation=True, suppress_st_warning=True, show_spinner=True)
def load_model():
    model = KeyBERT("distilbert-base-nli-mean-tokens")
    return model


model = load_model()

texts = [
    " ",
    "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.",
    "The case stemmed from an allegation Mr Trump directed his former lawyer to pay an adult film actress to stop her speaking out about an alleged affair.\n\nThe lawyer, Michael Cohen, was later jailed on multiple charges.\n\nThe FEC, the regulatory agency tasked with enforcing campaign finance law, announced the case closure Thursday.\n\nIt came after the commission, split evenly between Democrats and Republicans, became deadlocked 2-2 on taking action at a closed-door meeting in February.\n\nThe vote came months after an internal report recommended that there was 'reason to believe' Mr Trump's campaign had knowingly violated campaign finance law.",
    "In natural language understanding (NLU) tasks, there is a hierarchy of lenses through which we can extract meaning — from words to sentences to paragraphs to documents. At the document level, one of the most useful ways to understand text is by analyzing its topics. The process of learning, recognizing, and extracting these topics across a collection of documents is called topic modeling.\nIn this post, we will explore topic modeling through 4 of the most popular techniques today: LSA, pLSA, LDA, and the newer, deep learning-based lda2vec.\nOverview\nAll topic models are based on the same basic assumption:\neach document consists of a mixture of topics, and\neach topic consists of a collection of words.\nIn other words, topic models are built around the idea that the semantics of our document are actually being governed by some hidden, or “latent,” variables that we are not observing. As a result, the goal of topic modeling is to uncover these latent variables — topics — that shape the meaning of our document and corpus. The rest of this blog post will build up an understanding of how different topic models uncover these latent topics\n",
]

placeholder = st.empty()
text_input = placeholder.text_area("Type in some text you want to analyze", height=300)

sample_text = st.selectbox(
    "Or pick some sample texts", [f"sample {i+1}" for i in range(len(texts))]
)

sample_id = int(sample_text.split(" ")[-1])
text_input = placeholder.text_area(
    "Type in some text you want to analyze", value=texts[sample_id - 1], height=300
)


top_n = st.sidebar.slider("Select number of keywords to extract", 5, 20, 10, 1)
min_ngram = st.sidebar.number_input("Min ngram", 1, 5, 1, 1)
max_ngram = st.sidebar.number_input("Max ngram", min_ngram, 5, 3, step=1)
st.sidebar.code(f"ngram_range = ({min_ngram}, {max_ngram})")


params = {
    "docs": text_input,
    "top_n": top_n,
    "keyphrase_ngram_range": (min_ngram, max_ngram),
    "stop_words": "english",
}

add_diversity = st.sidebar.checkbox("Add diversity to the results")

if add_diversity:
    method = st.sidebar.selectbox(
        "Select a method", ("Max Sum Similarity", "Maximal Marginal Relevance")
    )
    if method == "Max Sum Similarity":
        nr_candidates = st.sidebar.slider("nr_candidates", 20, 50, 20, 2)
        params["use_maxsum"] = True
        params["nr_candidates"] = nr_candidates

    elif method == "Maximal Marginal Relevance":
        diversity = st.sidebar.slider("diversity", 0.1, 1.0, 0.6, 0.01)
        params["use_mmr"] = True
        params["diversity"] = diversity


keywords = model.extract_keywords(**params)

if keywords != []:
    st.info("Extracted keywords")
    keywords = pd.DataFrame(keywords, columns=["keyword", "relevance"])
    st.table(keywords)