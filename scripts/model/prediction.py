import click
import pandas as pd
import numpy as np
from pycaret.classification import *

@click.command()
@click.argument('data_path', type=click.Path())
@click.argument('model_path', type=click.Path())
def train_model(data_path,model_path):
    """ Loading saved model and making prediction on new data"""
    model_path = model_path + 'finalRFmodel_21APR2022'
    data_path = data_path + 'processed_data.csv'

    df = pd.read_csv(data_path)
    print("Reading processed data - Successful")
    
    record_num = np.random.randint(0,len(df))
    
    print(f"Making prediction on record number {record_num}")
    
    print("Loading saved model...")
    loaded_model = load_model(model_path)
    
    prediction = predict_model(loaded_model,data = df.iloc[[record_num]])
    print(f"Actual class is {list(df.iloc[[record_num]]['mental_disorder'])[0]}")
    print(f"Predicted class is {list(prediction.prediction_label)[0]} with {list(prediction.prediction_score)[0]*100}% confidence")
    
    
if __name__ == "__main__":
    train_model()
