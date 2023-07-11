# Validating News Features

### Time Series Extraction
We take the factors that we extracted in Steps 1 and 2, and we cross-reference them with the news data. The latter is in the format of a time-stamped corpus. To replicate this part, you can run the attached Python files. First, we transform our news data into .csv files with [news_corpus_to_csv_files.py](https://github.com/philippzi98/food_insecurity_predictions_nlp/blob/main/Step%204%20-%20Validating%20News%20Features/news_corpus_to_csv_files.py). Then, we extract the actual time series with  [granger_timeline.py](https://github.com/philippzi98/food_insecurity_predictions_nlp/blob/main/Step%204%20-%20Validating%20News%20Features/granger_timeline.py
).

&nbsp;

### Granger Causality Tests
We determine the predictive news factors by employing the Granger Causality Test presented by [Kim (2012)](https://ieeexplore.ieee.org/abstract/document/6244856?casa_token=b3DIUW6sO-0AAAAA:3lAiuuVVVQsyQr_f9LAeYN1AWE2Q_PSl_dTjUdKoYPMyaj2OiD3C3Yso3dA9_OrbB4dw4Gs). Similar to other dimensionality reduction techniques, based on non-zero coefficients, the respective predictive (news) factors are chosen. In practice, the resulting time series values from the **Time Series Extraction** are passed through the attached [granger_parallel.py](https://github.com/philippzi98/food_insecurity_predictions_nlp/blob/main/Step%204%20-%20Validating%20News%20Features/granger_parallel.py) file, which you can use for replication. Please make sure to place the code file with helper functions, [stattools.py](https://github.com/philippzi98/food_insecurity_predictions_nlp/blob/main/Step%204%20-%20Validating%20News%20Features/stattools.py) in your folder.

&nbsp;

---

Follow the rest of our project's methodology with the [Regression Modelling](https://github.com/philippzi98/food_insecurity_predictions_nlp/tree/main/Step%205%20-%20Regression%20Modelling).
