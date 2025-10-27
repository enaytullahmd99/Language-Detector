import pandas as pd
import regex as re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
import joblib

# Data loading and cleaning
def cleaning(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r"[^\p{L}\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def load_and_prepare_data(csv_path):
    df = pd.read_csv(csv_path)
    df = df.dropna().drop_duplicates()
    df['Text'] = df['Text'].str.strip().apply(cleaning)
    return df

def train_models(df):
    v = TfidfVectorizer()
    X = v.fit_transform(df['Text'])
    y = df['Language']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    models = {
        "RandomForest": RandomForestClassifier(n_estimators=200, random_state=42),
        "NaiveBayes": MultinomialNB(),
        "LogisticRegression": LogisticRegression(max_iter=1000),
        "SVM": LinearSVC()
    }
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        results[name] = acc
        print(f"{name} Accuracy: {acc:.4f}")
    best_model_name = max(results, key=results.get)
    best_model = models[best_model_name]
    joblib.dump(best_model, f"{best_model_name}_model.pkl")
    joblib.dump(v, "tfidf_vectorizer.pkl")
    print(f"✅ Best model '{best_model_name}' and vectorizer saved!")
    return best_model_name

def predict_language(input_text, model_path, vectorizer_path):
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    cleaned_text = cleaning(input_text)
    X_input = vectorizer.transform([cleaned_text])
    predicted_language = model.predict(X_input)[0]
    return predicted_language

if __name__ == "__main__":
    # Training phase
    df = load_and_prepare_data("languagedetection.csv")
    best_model_name = train_models(df)
    
    # Input/output phase
    model_path = f"{best_model_name}_model.pkl"
    vectorizer_path = "tfidf_vectorizer.pkl"
    while True:
        user_text = input("Enter text to detect language (type 1 to stop): ")
        if user_text.strip() == "1":
            print("\nExiting... 👋")
            break
        predicted_language = predict_language(user_text, model_path, vectorizer_path)
        print(f"Predicted Language: {predicted_language}")
