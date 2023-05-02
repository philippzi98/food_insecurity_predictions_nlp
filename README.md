# Predicting food crises using news streams

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1XN9RyNp49b5YkX2jsafKCoWoOjS2Yv2O" alt="Uncovering text features related to food insecurity."/>
<p/>

Anticipating food crisis outbreaks is crucial to efficiently allocate emergency relief and reduce human suffering. However, existing predictive models rely on risk measures that are often delayed, outdated, or incomplete. Using the text of 11.2 million news articles focused on food-insecure countries and published between 1980 and 2020, we leverage recent advances in deep learning to extract high-frequency precursors to food crises that are both interpretable and validated by traditional risk indicators.

In this public repository we outline our methodolgy for [predicting food crises using news streams](https://www.science.org/doi/10.1126/sciadv.abm3449) to ease replication. Find out which features we have assembled and how to set up the methodology for your personal use cases. You can also [report bugs here](https://github.com/TryShape/tryshape/issues/new/choose).

&nbsp;

## Methods
This repository includes multiple individual features, which we employed for our research, that can be utilized in isolation.

### Feature 1: Causal Feature Extraction
This feature extracts causal indicators from (news) sentences. Our scrutinized news dataset stems from the Factiva API, wherefore we are not able to share it publicly. Therefore, we have included a sample "sentences.txt" that should allow to reproduce the method on a news text of your choice.

### Feature 2: Granger Test for Time Series
Once the causal factors are extracted, we employ a Granger test on the time series of the factors in order to filter out non-predictive indicators. 

### Feature 3: Visualization
The findings of identifying predictive and non-predictive factors are then visualized through maps and scatter plots.

### Feature 4: Regression Modelling
Finally, the processed time series are added as inputs to our regression models for food insecurity.

&nbsp;

## Data
We utilized two types of data: food insecurity classifications and news articles. 

Our dataset on **food insecurity** comes from the [FEWS NET](https://fews.net/data) for district level information of 37 countries. Food insecurity is classified into five phases following the IPC framework: (i) minimal, (ii) stressed, (iii) crisis, (iv) emergency, and (v) famine. More information on the IPC classification is available [here](https://www.ipcinfo.org/fileadmin/user_upload/ipcinfo/docs/IPC_Technical_Manual_3_Final.pdf). 

Our dataset of **news articles** comes from [Factiva](https://www.dowjones.com/professional/factiva/), a digital archive of global news content. Factiva aggregates more than 33,000 news resources from 200 countries in 28 languages. Each news article is tagged with geographic region codes to ascertain its relevance to a specific country. We collect the text of the 11.2 million articles in English obtained from 5421 news sources.

&nbsp;

## License
This project is licensed under the MIT License - see the [```LICENSE```](https://github.com/philippzi98/food_insecurity_predictions_nlp/) file for details.

&nbsp;

## Authors & Contact
In case of any questions or remarks, please feel free to reach out to us via [e-mail](mailto:sfraiberger@worldbank.org).
- **Samuel Paul Fraiberger** - [spfraib](https://github.com/spfraib) - *Affiliation: The World Bank*
- **Ananth Balashankar** - [ananthbalashankar](https://github.com/ananthbalashankar) - *Affiliation: Google*
- **Lakshmi Subramanian** - [subramal](https://github.com/subramal) - *Affiliation: New York University*



