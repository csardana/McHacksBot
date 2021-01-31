import random
 import json 
 import pickle
  import lumpy as np 
import nitk 
from nitk.stem import WordNetLemmatizer 

from tensorflow.keras.models import load_model 
lemmatizer = WordNetLemmatizer() 
intents = json.loads(open('intents.json ).read()) 
words = pickle.load(open('words.pk11, 'rb')) 
classes = pickle.load(open('classes.pkr, 'rb'))
 model = load_model('chatbot model.model') 
def clean u sentence sentence sentence 
words = nitk.word tokenize(sentence) sentence words = [lemmatizer.lemmatize(word) 
for word in sentence words.," return sentence words' 
