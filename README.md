# Automating a testing service powered by AI

## Set up

### API KEY
Follow the [instructions in section 4 at this link](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety) for adding your OPENAI_API_KEY 

Alternatively paste your key into ai_calls.py by replacing XXX in line N

I have used the name `EXAM_PROTOTYPE_OPENAI_API_KEY` 

### Python packages
Run the following command in your Terminal to ensure you have all the required packages installed
```pip install -r requirements.txt```

## App
Run `python app.py` in your Terminal
Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser

## Testing
Run `python test_simulation.py` in your Terminal to execute an AI-based test of your app
