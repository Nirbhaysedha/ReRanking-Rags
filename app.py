from flashrank.Ranker import Ranker,RerankRequest
import streamlit as st 
import json

def get_result(query, passages, choice):
    if choice == "Nano":
        ranker = Ranker()
    elif choice == "Small":
        ranker = Ranker(model_name="ms-marco-MiniLM-L-12-v2", cache_dir="/opt")
    elif choice == "Medium":
        ranker = Ranker(model_name="rank-T5-flan", cache_dir="/opt")
    elif choice == "Large":
        ranker = Ranker(model_name="ms-marco-MultiBERT-L-12", cache_dir="/opt")

    rerankrequest = RerankRequest(query=query, passages=passages)
    results = ranker.rerank(rerankrequest)
    print(results)

    return results

st.set_page_config(layout="wide",
                   page_title="Lost in the middle issue ! Solving ")



def main():
    st.title("Re Ranking by Flash Rank")
    st.sidebar.write("According to model size choose ")
    menu=["Nano","Small","Medium","Large"]
    choice=st.sidebar.selectbox("Choose",menu)


main()

