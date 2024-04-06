from parsinorm import Tokenizer
import pandas as pd

tokenizer = Tokenizer()
tokenized_list = []

file_path = input("Please provide the path of the CSV file:")
column_index_str = input("Please provide the index for the target column:")

try:
    column_index = int(column_index_str)
except:
    print("The input for the culmn index is incorrect.")

tokenized_file_name = input("Please provide the name of the output file along with its file format(.csv):")


df = pd.read_csv(file_path)



for index, row in df.iterrows():
    l = tokenizer.sentence_tokenize(row[column_index], verb_seperator=True)
    tokenized_list = tokenized_list + l

tokenized_dict = {'sentences': tokenized_list}
df_tokenized = pd.DataFrame(tokenized_dict)
df_tokenized.to_csv(tokenized_file_name)