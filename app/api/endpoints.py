from fastapi import APIRouter
from pydantic import BaseModel
from app.services.data_fetcher import TestDataFetcher
from app.services.data_cleaner import TestDataCleaner
from app.models.qa_model import QAModel

router = APIRouter()
fetcher = TestDataFetcher("https://your-firebase-api-url")
cleaner = TestDataCleaner()
qa_model = QAModel()

class QARequest(BaseModel):
    question: str
    context: str

@router.get("/tests")
async def get_processed_tests():
    raw_data = fetcher.get_tests()
    return cleaner.clean_test_data(raw_data)

@router.post("/ask")
async def answer_question(request: QARequest):
    return qa_model.generate_answer(
        question=request.question,
        context=request.context
    )