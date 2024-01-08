from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

obj = DataIngestion()
train_data,test_data = obj.initiate_data_ingestion()

data_transformation = DataTransformation()
train_array,test_array,preprocessor_path = data_transformation.initiate_data_transformation(train_data,test_data)

model_training = ModelTrainer()
print(model_training.initiate_model_trainer(train_array,test_array))


