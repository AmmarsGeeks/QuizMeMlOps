from datetime import datetime

class TestDataCleaner:
    @staticmethod
    def clean_test_data(raw_data):
        cleaned = []
        for test in raw_data:
            cleaned_test = {
                "test_id": test['id'],
                "name": test['name'],
                "category": test['categoria'],
                "timestamp": datetime.fromtimestamp(test['createdAt']['_seconds']),
                "questions": []
            }
            
            for question in test['questions']:
                cleaned_question = {
                    "text": question['pregunta'],
                    "options": [opt['texto'] for opt in question['options']],
                    "correct_answer": next(opt['texto'] for opt in question['options'] if opt['esCorrecta'])
                }
                cleaned_test['questions'].append(cleaned_question)
                
            cleaned.append(cleaned_test)
        return cleaned