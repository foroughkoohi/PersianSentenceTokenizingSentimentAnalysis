# Persian Text Analysis Projects

This repository contains two Persian text analysis projects: Sentence Tokenization and Sentiment Analysis.

## Project 1: Persian Sentence Tokenizing

This project tokenizes sentences in Persian texts. It splits the input text into individual sentences and labels them based on the given ratings.

### Features

- **Sentence Tokenization**: Splits the text into separate sentences.
- **Sentiment Labeling**: Labels sentences based on their rating as `positive`, `neutral`, or `negative`.

### Usage

1. **Install Required Libraries**
1. It's suggested to use Python 3.6 or 3.7 for sentence tokenizing and Parsinorm project.
2. It's suggested to run the tokenizing project in a conda environment.
3. Please visit the *[link](https://pypi.org/project/parsinorm/)* and add any necessary files to the Anaconda directories.
4. It's recommended to use Python 3.11 for running sentiment analysis.

### Run the Script


Execute the script using Python. The script will prompt you for the following inputs:

- **File Path**: Path to the input CSV file.
- **Text Column Index**: Index of the column containing text data (e.g., 0 for the first column).
- **Rating Column Index**: Index of the column containing rating data (e.g., 1 for the second column).
- **Output File Name**: Name of the output CSV file where the tokenized data will be saved (e.g., `tokenized_output.csv`).

The script will read the CSV file, tokenize sentences, and save the results to the specified output file.


## Project 2: Sentiment Analysis

This project performs sentiment analysis on Persian sentences using the pre-trained "roberta-sentiment-persian" model. It classifies sentences into one of three categories: `negative`, `positive`, or `neutral`.

### Features

- **Sentiment Analysis**: Classifies sentences into `negative`, `positive`, or `neutral`.
- **Pre-trained Model**: Uses the "roberta-sentiment-persian" model for sentiment classification.

### Usage

1. **Install Required Libraries**

   Install the necessary libraries using the following command:

   ```bash
   pip install transformers torch pandas

### Run the Script

Execute the script using Python. The script will prompt you for the following inputs:

- **File Path**: Path to the input CSV file.
- **Text Column Index**: Index of the column containing text data (e.g., 0 for the first column).
- **Output File Name**: Name of the output CSV file where the sentiment labels will be saved (e.g., `sentiment_output.csv`).

The script will load the model, analyze the sentiment of each sentence, and save the results to the specified output file.
