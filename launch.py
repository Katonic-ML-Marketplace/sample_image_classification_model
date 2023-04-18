
import pandas as pd
from typing import Any, Union,Dict
from transformers import BeitFeatureExtractor, BeitForImageClassification
from PIL import Image
import requests
import json

def loadmodel(logger):
    """Get model from cloud object storage."""
    logger.info("getting model")
    model = BeitForImageClassification.from_pretrained('microsoft/beit-base-patch16-224-pt22k-ft22k')
    return model  

def preprocessing(url:str,logger):
    """ Applies preprocessing techniques to the raw data"""
    def loaddata(url):  
        #url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
        image = Image.open(requests.get(url, stream=True).raw)
        return image
    ## in template keep this False by default, if its there then the return result will be other than False
    image = loaddata(url)
    logger.info("loaded model")
    feature_extractor = BeitFeatureExtractor.from_pretrained('microsoft/beit-base-patch16-224-pt22k-ft22k')
    inputs = feature_extractor(images=image, return_tensors="pt")
    return inputs
    
def predict(features,model,logger):
    """Predicts the results for the given inputs"""
    
    outputs = model(**features)
    logits = outputs.logits
    # model predicts one of the 21,841 ImageNet-22k classes
    predicted_class_idx = logits.argmax(-1).item()
    result_class = model.config.id2label[predicted_class_idx]
    predicted_result = {"Predicted class":result_class}
    pred_results = json.dumps(predicted_result)
    return pred_results
