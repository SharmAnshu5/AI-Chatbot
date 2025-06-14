import openai
import os
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
from config import Config

openai.api_key = Config.OPENAI_API_KEY

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
lemmatizer = WordNetLemmatizer()

# Preprocess user input

def preprocess(text):
    tokens = nltk.word_tokenize(text)
    tokens = [word.lower() for word in tokens]
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

# Generate AI response using OpenAI

def get_openai_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"