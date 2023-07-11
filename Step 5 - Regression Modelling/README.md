# Regression Modelling
We utilize a random forest (RF) regression to predict the IPC index of food insecurity. To showcase the value-add of news data, we use the same model infrastructure for our baseline model only utilizing traditional indicators, the model only utilizing news indicators, and the ultimate model utilizing both traditional and news data. The latter is estimated as follows:

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1FMOd1gVUiJq3T3KYiVRJIcLZVKNyweHS" alt="Random forest regression model to predict IPC index."/>
<p/>

In practical terms, the processed time series from [Step 4 - Validating News Features](https://github.com/philippzi98/food_insecurity_predictions_nlp/tree/main/Step%204%20-%20Validating%20News%20Features) serve as input to this regression model in the attached notebook [rf_regression_modelling.ipynb](https://github.com/philippzi98/food_insecurity_predictions_nlp/blob/main/Step%205%20-%20Regression%20Modelling/rf_regression_modelling.ipynb). The output data can then be used to generate the visuals in [Step 7 - Visualizations](https://github.com/philippzi98/food_insecurity_predictions_nlp/tree/main/Step%207%20-%20Visualizations). Please note that you will require to download the helper files [famine-country-province-district-years-CS.csv](https://github.com/philippzi98/food_insecurity_predictions_nlp/blob/main/Step%205%20-%20Regression%20Modelling/famine-country-province-district-years-CS.csv) and [matching_districts.csv](https://github.com/philippzi98/food_insecurity_predictions_nlp/blob/main/Step%205%20-%20Regression%20Modelling/matching_districts.csv).

If you are not interested in the earlier steps of our methodology, you can use the provided time series data file, [time_series_with_causes_zscore_full.csv](https://github.com/philippzi98/food_insecurity_predictions_nlp/blob/main/Step%205%20-%20Regression%20Modelling/time_series_with_causes_zscore_full.csv), and respectively adapt the filepath in the notebook [rf_regression_modelling.ipynb](https://github.com/philippzi98/food_insecurity_predictions_nlp/blob/main/Step%205%20-%20Regression%20Modelling/rf_regression_modelling.ipynb).

&nbsp;

---

Follow the rest of our project's methodology with [Visualizations](https://github.com/philippzi98/food_insecurity_predictions_nlp/tree/main/Step%206%20-%20Visualizations).
