
import pandas as pd
from pycaret.classification import load_model, predict_model
from pydantic import BaseModel
from fastapi import FastAPI

# Create the app
app = FastAPI()

# Add title and description to the API
app.title = 'Mental Health Predictor'
app.description = 'This API predicts whether the User has Depression, Anxiety, Panic Attacks or None mentioned based on the Questionnaire of 36 questions'

# Create PyDantic model class
class PredictRequest(BaseModel):
    gender: str = "Male"
    age: str = "13-19"
    education: str = "College"
    marital: str = "single"
    income: str = "<10"
    loan: str = "no"
    friend_no: str = "none"
    friend_help: str = "no"
    friend_interact: str = "0"
    share_feel: str = "no"
    have_someone: str = "no"
    lonely: str = "yes"
    bullied: str = "yes"
    family_support: str = "no"
    compare_life: str = "no"
    social_media: str = "<2 hours"
    hangout: str = "none"
    home_time: str = "<24"
    religious: str = "no"
    goal: str = "no"
    suicidal: str = "no"
    sleep_disorder: str = "yes"
    love_someone: str = "no"
    die_someone: str = "no"
    thoughts_command: str = "yes"
    self_harm: str = "yes"
    thoughts_acted: str = "yes"
    thoughts_acted2: str = "yes"
    thoughts_time: str = "night"
    voices: str = "no"
    harming_others: str = "yes"
    suicide: str = "yes"
    suicidal_thoughts: str = "no"
    therapy: str = "no"


# Load trained Pipeline
model = load_model('./artifacts/pycaretModels/finalRFmodel_21APR2022')


@app.get('/')
async def root():
    '''
    This is the index page!
    '''
    return {'Instructions': 'Type [/docs] after the localhost address for viewing the Swagger UI'}


@app.get('/healthcheck', status_code=200)
async def healthcheck():
    return 'Mental Health Predictor is all ready to go!'



# Define predict function
@app.post('/predict')
def predict(request: PredictRequest):
    """ This endpoint predicts whether the User has Depression, Anxiety, Panic Attacks or None mentioned based on the Questionnaire of 36 questions"""
    data = request.dict()
    data = pd.DataFrame([data])
    data.columns = ['gender', 'age', 'education', 'marital', 'income', 'loan', 'friend_no', 'friend_help', 'friend_interact', 'share_feel', 'have_someone', 'lonely', 'bullied', 'family_support', 'compare_life', 'social_media', 'hangout', 'home_time', 'religious', 'goal', 'suicidal', 'sleep_disorder', 'love_someone', 'die_someone', 'thoughts_command', 'self_harm', 'thoughts_acted', 'thoughts_acted2', 'thoughts_time', 'voices', 'harming_others', 'suicide', 'suicidal_thoughts', 'therapy']
    
    
    predictions = predict_model(model, data=data) 
    return {'prediction': list(predictions['prediction_label']),
            'score': list(predictions['prediction_score'])[0]*100}

# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=8000)