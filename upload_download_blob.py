import os
from datetime import datetime
from joblib import dump, load
from google.cloud import storage

def upload_blob(model, model_name, directory):
# Function to upload model or other object to Cloud Storage bucket
# Params:
# model - Model joblib object to upload
# model_name (str) - Name of model not including timestamp and file extension
# directory (str) - Cloud Storage directory e.g. "gs://bucket_name/folder_name"

    model_timestamp = datetime.now().strftime("%Y%m%d")
    model_filename = model_name + "_" + model_timestamp + ".joblib"
    dump(model, model_filename) # Save model to local filesystem
    storage_path = os.path.join(directory, model_filename)
    blob = storage.blob.Blob.from_string(storage_path, client=storage.Client())
    blob.upload_from_filename(model_filename)
    print(f"Model saved to Cloud Storage bucket: {storage_path}")


def download_blob(model_filename, directory):
# Function to download model or other object from Cloud Storage bucket
# Params:
# model_filename(str) - Model joblib object to download
# directory (str) - Cloud Storage directory e.g. "gs://bucket_name/folder_name"
# Returns: Model object
    
    storage_path = os.path.join(directory, model_filename)
    blob = storage.blob.Blob.from_string(storage_path, client=storage.Client())
    blob.download_to_filename(model_filename)
    model = load(model_filename) # Save model to local filesystem
    return model