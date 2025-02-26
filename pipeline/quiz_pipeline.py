from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from app.services.data_fetcher import TestDataFetcher
from app.services.data_cleaner import TestDataCleaner
import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

@data_loader
def load_data(*args, **kwargs):
    fetcher = TestDataFetcher("https://your-firebase-api-url")
    return fetcher.get_tests()

@transformer
def transform_data(data, *args, **kwargs):
    cleaner = TestDataCleaner()
    return cleaner.clean_test_data(data)

@model
def train_model(data, *args, **kwargs):
    from app.models.qa_model import QAModel
    model = QAModel()
    return model

@data_exporter
def export_data(data, *args, **kwargs):
    pd.DataFrame(data).to_csv("processed_tests.csv")