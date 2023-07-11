# Predicting food crises using news streams

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1XN9RyNp49b5YkX2jsafKCoWoOjS2Yv2O" alt="Uncovering text features related to food insecurity."/>
<p/>

Anticipating food crisis outbreaks is crucial to efficiently allocate emergency relief and reduce human suffering. However, existing predictive models rely on risk measures that are often delayed, outdated, or incomplete. Using the text of 11.2 million news articles focused on food-insecure countries and published between 1980 and 2020, we leverage recent advances in deep learning to extract high-frequency precursors to food crises that are both interpretable and validated by traditional risk indicators.

In this public repository we outline our methodolgy for [predicting food crises using news streams](https://www.science.org/doi/10.1126/sciadv.abm3449) to ease replication. Find out which features we have assembled and how to set up the methodology for your personal use cases. You can also [report bugs here](https://github.com/TryShape/tryshape/issues/new/choose).

&nbsp;

## Methods
This repository includes multiple individual features, which we employed for our research, that can be utilized in isolation.

### Step 1 - [Seeds Selection](https://github.com/philippzi98/food_insecurity_predictions_nlp/tree/main/Step%201%20-%20Seeds%20Selection)
Starting with the three manually selected seed phrases "food insecurity," "hunger crisis," and "famine," additional potential seed phrases were sought from all unigrams, bigrams, and trigrams in the dataset of 11.2 million articles.

### Step 2 - [Frame-Semantic Parsing](https://github.com/philippzi98/food_insecurity_predictions_nlp/tree/main/Step%202%20-%20Frame-Semantic%20Parsing)
Causal extraction refers to the natural language processing task of extracting cause-effect relations from text, in our case from news sentences. We use a frame-semantic parser to extract semantic causes of food insecurity. Our scrutinized news dataset stems from the [Factiva API](https://www.dowjones.com/professional/factiva/), wherefore we are not able to share it publicly. We have included a sample [sentences.txt](https://github.com/philippzi98/food_insecurity_predictions_nlp/blob/main/Step%202%20-%20Frame-Semantic%20Parsing/sentences.txt) file that should allow to reproduce the method on a news text of your choice.

### Step 3 - [Keyword Expansion](https://github.com/philippzi98/food_insecurity_predictions_nlp/tree/main/Step%203%20-%20Keyword%20Expansion)
While the frame-semantic parser allows us to extract text features related to food insecurity, it fails to capture words semantically close to a seed that are also relevant. Therefore, we expand the set of text features with semantically similar key phrases.

### Step 4 - [Validating News Features](https://github.com/philippzi98/food_insecurity_predictions_nlp/tree/main/Step%204%20-%20Validating%20News%20Features)
After uncovering the text features semantically related to food insecurity in Steps 1 and 2, we cross-reference the extracted features with time-stamped news corpora. Then, we discard non-predictive indicators of the resulting time series using a Granger causality test.

### Step 5 - [Regression Modelling](https://github.com/philippzi98/food_insecurity_predictions_nlp/tree/main/Step%205%20-%20Regression%20Modelling)
The processed time series are added as inputs to our regression model for food insecurity. We employ a Random Forest (RF) regression that is fed with the news features in addition to traditional food insecurity features. The model can be fed with use case dependent external features.

### Step 6 - [Visualizations](https://github.com/philippzi98/food_insecurity_predictions_nlp/tree/main/Step%206%20-%20Visualizations)
The findings of the food insecurity project are visualized through maps and scatter plots. We share code to replicate the visualizations of identifying predictive/non-predictive features and episodes.

&nbsp;

## Data
We utilized two types of data: food insecurity classifications and news articles. 

Our dataset on ```food insecurity``` comes from the [FEWS NET](https://fews.net/data) for district level information of 37 countries. Food insecurity is classified into five phases following the IPC framework: (i) minimal, (ii) stressed, (iii) crisis, (iv) emergency, and (v) famine. More information on the IPC classification is available [here](https://www.ipcinfo.org/fileadmin/user_upload/ipcinfo/docs/IPC_Technical_Manual_3_Final.pdf). 

Our dataset of ```news articles``` comes from [Factiva](https://www.dowjones.com/professional/factiva/), a digital archive of global news content. Factiva aggregates more than 33,000 news resources from 200 countries in 28 languages. Each news article is tagged with geographic region codes to ascertain its relevance to a specific country. We collect the text of the 11.2 million articles in English obtained from 5421 news sources.

&nbsp;

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/philippzi98/food_insecurity_predictions_nlp/) file for details.

&nbsp;

## Citation
If you find this project useful in your research, please cite the following paper.

```bibtex
@article{balashankar2023predicting,
  author = {Ananth Balashankar  and Lakshminarayanan Subramanian  and Samuel P. Fraiberger },
  title = {Predicting food crises using news streams},
  journal = {Science Advances},
  volume = {9},
  number = {9},
  pages = {eabm3449},
  year = {2023},
  doi = {10.1126/sciadv.abm3449},
  URL = {https://www.science.org/doi/abs/10.1126/sciadv.abm3449},
}
```

&nbsp;

## Authors & Contact
In case of any questions or remarks, please feel free to reach out to us via [e-mail](mailto:sfraiberger@worldbank.org).
- **Samuel Paul Fraiberger** - [spfraib](https://github.com/spfraib) - *Affiliation: The World Bank*
- **Ananth Balashankar** - [ananthbalashankar](https://github.com/ananthbalashankar) - *Affiliation: Google*
- **Lakshmi Subramanian** - [subramal](https://github.com/subramal) - *Affiliation: New York University*



