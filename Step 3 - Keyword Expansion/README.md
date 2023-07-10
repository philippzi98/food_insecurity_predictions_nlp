# Keyword Expansion

While the frame-semantic parser allows us to extract 1,211 text features related to food insecurity, it fails to capture words semantically close to a seed that are also relevant. Therefore, we expand the set of 1,211 text features with semantically similar key phrases. We consider as candidate features all the unigrams in our news corpus and all the bigrams and trigrams occurring more than 1,000 times. We obtain the ultimate set of features by keeping the candidates within a certain distance to an original feature. 

To replicate this part, you can run the attached Python file [keyword_expansion.ipynb](...).

---

Follow the rest of our project's methodology with [Validating News Features](https://github.com/philippzi98/food_insecurity_predictions_nlp/tree/main/Step%204%20-%20Validating%20News%20Features).

