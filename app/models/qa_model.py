from transformers import pipeline

class QAModel:
    def __init__(self):
        self.model = pipeline("question-answering")
    
    def generate_answer(self, context: str, question: str):
        return self.model(question=question, context=context)