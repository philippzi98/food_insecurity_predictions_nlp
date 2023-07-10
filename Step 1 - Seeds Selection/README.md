# Seed Selection

Starting with the three manually selected seed phrases "food insecurity," "hunger crisis," and "famine," additional potential seed phrases were sought from all unigrams, bigrams, and trigrams in the dataset of 11.2 million articles. Each word was transformed into a 'word embedding' vector, encapsulating its meaning in relation to the context it was found. The 'Word Mover's Distance' was then computed between the seed phrases and the candidates, reflecting their semantic proximity. This allowed for a ranking of the candidates based on their distance, resulting in the top 100 being added to our seed list. To ensure relevance, any bigram or trigram candidate had to include either "food" or "hunger."

To replicate this part, you can run the attached Python file [seeds_selection.ipynb](https://github.com/philippzi98/food_insecurity_predictions_nlp/blob/main/Step%201%20-%20Seeds%20Selection/seeds_selection.ipynb).

Follow the rest of our project's methodology with the [Frame-Semantic Parsing](...).

