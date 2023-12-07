import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

from app.schemas.sentiment import Sentiment


class BertSentimentAnalysis:
    def __init__(self) -> None:
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(
            "nlptown/bert-base-multilingual-uncased-sentiment"
        )
        self.model = AutoModelForSequenceClassification.from_pretrained(
            "nlptown/bert-base-multilingual-uncased-sentiment"
        ).to(self.device)
        self.model.eval()

    @torch.no_grad()
    def infer(self, request: Sentiment) -> str:
        inputs = self.tokenizer(request.user_review, return_tensors="pt").to(
            self.device
        )

        with torch.no_grad():
            logits = self.model(**inputs).logits

        predicted_class_id = logits.argmax().item()
        prediction = self.model.config.id2label[predicted_class_id]

        return str(prediction)


bert_sentiment_analysis = BertSentimentAnalysis()
