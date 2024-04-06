# Libraries
from parsinorm import Tokenizer
import pandas as pd

# Defining tokenizer
tokenizer = Tokenizer()
tokenized_list = []

# File and information 
file_path = input("Please provide the path of the CSV file:")
text_column_index_str = input("Please provide the index for the text column:")
rating_column_index_str = input("Please provide the index for the rating column:")

try:
    text_column_index = int(text_column_index_str)
    rating_column_index = int(rating_column_index_str)
except:
    print("The input for the column index is incorrect.")

tokenized_file_name = input("Please provide the name of the output file along with its file format(.csv):")

# Reading CSV file
try:
    df = pd.read_csv(file_path)
except:
    print("There seems to be an issue with the file path!")

# Defining Variables
tokenized_dict = {}
label = None

# Sentence Tokenizing and Labeling
for index, row in df.iterrows():
    comment_list = tokenizer.sentence_tokenize(row[text_column_index], verb_seperator=True)
    sentence_index = [index] * len(comment_list)
    sentence_rating = row[rating_column_index]

    if sentence_rating>=4:
        label = 'positive'
    elif (sentence_rating <4) and (sentence_rating <= 3):
        label = 'neutral'
    else:
        label = 'negative'
    
    sentence_label = [label] * len(comment_list)
    

    tokenized_dict = {'Index':sentence_index, 'Sentences':comment_list, 'Label':sentence_label}
    df_tokenized = pd.DataFrame(tokenized_dict)
    df_tokenized.to_csv(tokenized_file_name, mode = 'a', index = False, header = False, sep = ",")
    
