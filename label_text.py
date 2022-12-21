import numpy as np
from transformers import pipeline

def get_labels(df, candidate_labels, num_labels, threshold):
# Function to return the top labels of each line of text in a dataframe
# Params:
# df - Dataframe containing reviews (column containing reviews must be called "text")
# candidate_labels - List of labels to classify against 
# num_labels - Number of top labels to show (must be >=1)
# threshold - Minimum score of label to be considered
# Returns df with num_labels number of columns added with top labels

    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli") # Get model
    outputs = [classifier(text, candidate_labels, multi_label=True) for text in df["text"]] # Outputs arranged by score by default
    # While loop for number of labels
    counter = 1
    while counter <= num_labels:
        index = counter - 1
        labels = [output["labels"][index] for output in outputs]
        scores = [output["scores"][index] for output in outputs]
        label_list = [label if score >= threshold else np.nan for label, score in zip(labels, scores)] # Get list of labels if score is above threshold, otherwise null replaces it
        column_name = f"label_{counter}"
        df[column_name] = label_list
        counter += 1
    return df