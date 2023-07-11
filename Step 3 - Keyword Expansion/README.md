# Keyword Expansion

### Approach
While the frame-semantic parser allows us to extract 1,211 text features related to food insecurity, it fails to capture words semantically close to a seed that are also relevant. Therefore, we expand the set of 1,211 text features with semantically similar key phrases. We consider as candidate features all the unigrams in our news corpus and all the bigrams and trigrams occurring more than 1,000 times. We obtain the ultimate set of features by keeping the candidates within a certain distance to an original feature. 

To replicate this part, you can run the attached Python file [keyword_expansion.ipynb](https://github.com/philippzi98/food_insecurity_predictions_nlp/blob/main/Step%203%20-%20Keyword%20Expansion/keyword_expansion.ipynb).

&nbsp;

### Visualization
The resulting set of keywords with which we proceed in the methodology were visualized in [Figure 1](https://www.science.org/doi/10.1126/sciadv.abm3449#F1) of our research paper. You can use the data in [fig1_nodes.csv](https://github.com/philippzi98/food_insecurity_predictions_nlp/blob/main/Step%203%20-%20Keyword%20Expansion/fig1_nodes.csv) to replicate the visualization and track the different sources and frequencies of the terms.

---

Follow the rest of our project's methodology with [Validating News Features](https://github.com/philippzi98/food_insecurity_predictions_nlp/tree/main/Step%204%20-%20Validating%20News%20Features).

