from flask import Flask , render_template,jsonify,request,send_file 
from src.exception import CustomException
from src.logger import logging as lg
import os,sys

from src.pipeline.train_pipeline import TrainPipeline
from src.pipeline.predict_pipeline import PredictionPipeline


app = Flask(__name__)


@app.route("/")

def home():
    return render_template('index.html')

@app.route('/train')
def train_route():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()

        return jsonify('Training Successfull.')
    
    except Exception as e:
        raise CustomException (e,sys)
    
    