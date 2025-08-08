# Natural Language Processing (NLP) Project

This repository contains a comprehensive collection of NLP techniques and implementations, ranging from basic text processing to advanced machine learning applications.

## 📁 Project Structure

```
NLP/
├── README.md
├── download_nltk_data.py
├── tokenization.py
├── stemming.py
├── lemmatization.py
├── bag_of_words.py
├── TF_IDF.py
├── word2vec.py
├── Pos_tagging.py
├── NER.py
└── projects/
    └── spam_classifier/
        ├── spam_classifier.py
        └── data/
            └── SMSSpamCollection.txt
```

## 🚀 Getting Started

### Prerequisites

Before running the scripts, make sure you have the following packages installed:

```bash
pip install nltk spacy scikit-learn pandas numpy gensim
```

### Setup

1. **Download NLTK Data**: Run the setup script to download required NLTK data:
   ```bash
   python download_nltk_data.py
   ```

2. **Install spaCy Model**: Download the English language model for spaCy:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## 📚 Modules Overview

### 1. Text Preprocessing

#### `tokenization.py`
- **Purpose**: Demonstrates sentence and word tokenization using NLTK
- **Features**: 
  - Sentence tokenization
  - Word tokenization
  - Token counting
- **Usage**: 
  ```bash
  python tokenization.py
  ```

#### `stemming.py`
- **Purpose**: Implements Porter Stemmer for word stemming
- **Features**:
  - Porter Stemmer implementation
  - Word normalization
- **Usage**:
  ```bash
  python stemming.py
  ```

#### `lemmatization.py`
- **Purpose**: Demonstrates lemmatization using WordNet
- **Features**:
  - WordNet Lemmatizer
  - Part-of-speech aware lemmatization
- **Usage**:
  ```bash
  python lemmatization.py
  ```

### 2. Feature Extraction

#### `bag_of_words.py`
- **Purpose**: Implements Bag of Words (BoW) feature extraction
- **Features**:
  - Text preprocessing (cleaning, lowercase, stopword removal)
  - Lemmatization
  - CountVectorizer implementation
- **Usage**:
  ```bash
  python bag_of_words.py
  ```

#### `TF_IDF.py`
- **Purpose**: Implements TF-IDF (Term Frequency-Inverse Document Frequency) feature extraction
- **Features**:
  - TF-IDF vectorization
  - Text preprocessing pipeline
- **Usage**:
  ```bash
  python TF_IDF.py
  ```

#### `word2vec.py`
- **Purpose**: Implements Word2Vec for word embeddings
- **Features**:
  - Word2Vec model training
  - Text preprocessing for embeddings
  - Vocabulary extraction
- **Usage**:
  ```bash
  python word2vec.py
  ```

### 3. Linguistic Analysis

#### `Pos_tagging.py`
- **Purpose**: Demonstrates Part-of-Speech (POS) tagging using spaCy
- **Features**:
  - POS tagging
  - Detailed token analysis
  - POS explanations
- **Usage**:
  ```bash
  python Pos_tagging.py
  ```

#### `NER.py`
- **Purpose**: Implements Named Entity Recognition (NER) using spaCy
- **Features**:
  - Named entity detection
  - Entity type classification
  - Detailed token analysis
  - Entity explanations
- **Usage**:
  ```bash
  python NER.py
  ```

## 🤖 Machine Learning Projects

### Spam Classifier (`projects/spam_classifier/`)

A complete spam detection system using machine learning techniques.

#### Features:
- **Dataset**: SMS Spam Collection Dataset
- **Preprocessing**: Text cleaning, lemmatization, stopword removal
- **Feature Extraction**: Bag of Words with CountVectorizer
- **Model**: Multinomial Naive Bayes
- **Evaluation**: Confusion matrix and accuracy metrics

#### Usage:
```bash
cd projects/spam_classifier
python spam_classifier.py
```

#### Dataset:
The spam classifier uses the SMS Spam Collection Dataset located in `projects/spam_classifier/data/SMSSpamCollection.txt`.

## 🔧 Key Technologies Used

- **NLTK**: Natural Language Toolkit for text processing
- **spaCy**: Advanced NLP library for linguistic analysis
- **scikit-learn**: Machine learning library for feature extraction and modeling
- **pandas**: Data manipulation and analysis
- **gensim**: Word embeddings and topic modeling
- **NumPy**: Numerical computing

## 📊 Output Examples

### Tokenization Output:
```
['Natural', 'language', 'processing', '(', 'NLP', ')', 'is', 'a', 'field', 'of', 'artificial', 'intelligence', ...]
len of words 45
```

### POS Tagging Output:
```
Elon ! PROPN NNP proper noun
flew ! VERB VBD verb, past tense
to ! ADP IN adposition
Mars ! PROPN NNP proper noun
yesterday ! NOUN NN noun, singular or mass
```

### NER Output:
```
Entity Text | Label | Description
John Doe    | PERSON| People, including fictional
New York City| GPE  | Countries, cities, states
Google      | ORG  | Companies, agencies, institutions
```

