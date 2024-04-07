from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import pandas as pd

def analyze_sentiment_three_classes(sentence):
    # Load pre-trained model 
    # Load model directly

    tokenizer = AutoTokenizer.from_pretrained("dadashzadeh/roberta-sentiment-persian")
    model = AutoModelForSequenceClassification.from_pretrained("dadashzadeh/roberta-sentiment-persian")
    # Tokenize and process the input sentence
    inputs = tokenizer(sentence, return_tensors="pt", truncation=True)

    # Get the model predictions
    with torch.no_grad():
        outputs = model(**inputs)

    # Get the predicted label
    predicted_label = torch.argmax(outputs.logits, dim=1).item()

    # Print the raw predicted label for debugging
    # print(f"Raw Predicted Label: {predicted_label}")

    # Map the label to sentiment
    sentiment_mapping = {0: "negative", 1: "positive", 2: "neutral"}

    # Update the sentiment_mapping based on the actual predicted label
    if predicted_label not in sentiment_mapping:
        sentiment_mapping[predicted_label] = f"مجهول-{predicted_label}"

    sentiment = sentiment_mapping[predicted_label]

    return sentiment


# Load input CSV file
file_path = input("Please provide the path of the CSV file:")
text_column_index_str = input("Please provide the index for the text column:")

try:
    text_column_index = int(text_column_index_str)
except:
    print("The input for the column index is incorrect.")

try:
    df = pd.read_csv(file_path)
except:
    print("There seems to be an issue with the file path!")
    
# Provide the name of the output CSV file
output_file = input("Please provide the name of the output file along with its file format(.csv):")


# Variables
labeled_dict = {}

# Usage
for index, row in df.iterrows():
    input_sentence = row[text_column_index]
    result = analyze_sentiment_three_classes(input_sentence)
    sentence_index = index
    #print(result)
    labeled_dict = {'sentence':input_sentence, 'label':result}
    #print(labeled_dict)
    df_labeled = pd.DataFrame(labeled_dict, index=[sentence_index])
    df_labeled.to_csv(output_file, mode = 'a', index = False, header = False, sep = ",")
    
