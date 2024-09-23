from transformers import pipeline

def summarize_article(article) -> str:
    model = pipeline("summarization", model="Falconsai/text_summarization")
    return model(str(article), max_length=500, min_length=100)