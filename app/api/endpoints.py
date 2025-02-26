from fastapi import APIRouter
from app.services.data_fetcher import TestDataFetcher
from app.services.data_cleaner import TestDataCleaner
from app.models.qa_model import QAModel

router = APIRouter()
fetcher = TestDataFetcher("https://your-firebase-api-url")
cleaner = TestDataCleaner()
qa_model = QAModel()

@router.get("/tests")
async def get_processed_tests():
    raw_data = fetcher.get_tests()
    return cleaner.clean_test_data(raw_data)

@router.post("/ask")
async def answer_question(question: str, context: str):
    return qa_model.generate_answer(question=question, context=context)