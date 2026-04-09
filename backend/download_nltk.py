import nltk
import os

def download_required_data():
    # Define the directory where NLTK data will be stored
    # Using 'backend/nltk_data' relative to the project root
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, 'nltk_data')
    
    if not os.path.exists(data_path):
        os.makedirs(data_path)
        
    print(f"Downloading NLTK data to: {data_path}")
    
    # Required datasets
    packages = [
        'punkt',
        'averaged_perceptron_tagger',
        'maxent_ne_chunker',
        'words',
        'omw-1.4',
        'stopwords'
    ]
    
    for package in packages:
        print(f"Downloading {package}...")
        nltk.download(package, download_dir=data_path)
    
    print("NLTK data download complete.")

if __name__ == "__main__":
    download_required_data()
