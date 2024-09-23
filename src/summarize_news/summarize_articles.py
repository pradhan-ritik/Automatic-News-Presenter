from transformers import pipeline

def summarize_article(article) -> str:
    model = pipeline("summarization", model="Falconsai/text_summarization")
    return model(article.to_text(), max_length=500, min_length=100)