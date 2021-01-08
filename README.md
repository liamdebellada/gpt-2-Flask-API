# Simple gpt-2 Flask API

## Usage:
1. Download initial pretrained model.
```python
gpt2.download_gpt2(model_name="355M")
```
2. Setup training data (optional).
```python
file_name = "yourdata.txt"
steps = 1000 #change this to your preference
```
3. Run `main.py`.
4. Generating content based on trained data.
```
#Visit localhost on the provided port using your finetuned model from ./checkpoints to generate.
/request/<model_name>/<generationCount>
```

## Known issues:
- Rate limitation is not yet present, and as a result can allow multiple requests to saturate machine resources.
