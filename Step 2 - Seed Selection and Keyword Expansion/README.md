# Seed Selection and Keyword Expansion

The frame-semantic parser allows us to extract text features related to food insecurity, but fails to capture words semantically close to a seed that are also relevant. We expand our set of text features with semantically similar key phrases. We consider as candidate features all the unigrams in our news corpus and all the bigrams and trigrams occurring more than 1000 times. We compute the word mover’s distance between each original feature and each candidate feature, and we keep the candidates whose distance to an original feature is smaller than 6.

### Seed Selection


&nbsp;

### Keyword Expansion


Follow the rest of our project's methodology with [Validating News Features](https://github.com/philippzi98/food_insecurity_predictions_nlp/tree/main/Step%203%20-%20Validating%20News%20Features).

