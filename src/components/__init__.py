from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

obj = DataIngestion()
train_data,test_data = obj.initiate_data_ingestion()

data_transformation = DataTransformation()
data_transformation.initiate_data_transformation(train_data,test_data)