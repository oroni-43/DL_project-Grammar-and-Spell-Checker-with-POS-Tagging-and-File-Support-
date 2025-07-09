import pandas as pd
import spacy
from textblob import TextBlob
import language_tool_python
import joblib

class GrammarSpellChecker:
    def __init__(self, dataset_path='grammar_dataset.csv'):
        self.tool = language_tool_python.LanguageTool('en-US')
        self.nlp = spacy.load("en_core_web_sm")
        self.dataset = pd.read_csv(dataset_path)

        try:
            self.model = joblib.load('grammar_correction_model.joblib')
            self.vectorizer = joblib.load('tfidf_vectorizer.joblib')
        except Exception as e:
            print("Model load error:", e)
            self.model, self.vectorizer = None, None

    def dataset_lookup(self, text):
        matched = self.dataset[self.dataset['incorrect'].str.lower() == text.strip().lower()]
        if not matched.empty:
            return matched.iloc[0]['correct']
        return None

    def ml_predict(self, text):
        if self.model and self.vectorizer:
            vec = self.vectorizer.transform([text])
            return self.model.predict(vec)[0]
        return None

    def correct_spelling(self, text):
        blob = TextBlob(text)
        return str(blob.correct())

    def correct_grammar(self, text):
        matches = self.tool.check(text)
        corrected = language_tool_python.utils.correct(text, matches)
        issues = [f"{match.ruleId}: {match.message}" for match in matches]
        return issues, corrected

    def pos_tagging(self, text):
        doc = self.nlp(text)
        return [{"word": token.text, "pos": token.pos_} for token in doc]

    def full_correction(self, text):
        corrected = self.dataset_lookup(text)
        if corrected:
            text = corrected
        else:
            ml_pred = self.ml_predict(text)
            if ml_pred and ml_pred.strip().lower() != text.strip().lower():
                text = ml_pred

        spell_corrected = self.correct_spelling(text)
        grammar_issues, grammar_corrected = self.correct_grammar(spell_corrected)
        final_issues, final_corrected = self.correct_grammar(grammar_corrected)

        return {
            "spelling_corrected": spell_corrected,
            "grammar_corrected": grammar_corrected,
            "final_corrected": final_corrected,
            "grammar_issues": final_issues
        }
