# Frame-Semantic Parsing

For the identification of causal features, we utilized the methodology presented by [Swayamdipta et al. (2017)](https://arxiv.org/abs/1706.09528) in their project [Open-SESAME](https://github.com/swabhs/open-sesame). They develop a frame-semantic parser to automatically detect FrameNet frames and frame-elements from sentences. In our context, these soft-max margin segmental recurrent neural nets help us identify important features in food insecurity prediction. An example of the frame-semantic parse is shown below: 

<p align="center">
<img src="https://raw.githubusercontent.com/spfraib/food_crisis_predictions_nlp/main/1.%20Fig1_causal_feature_extraction/fig/fsp-example.png"/>
<p/>

You can follow their instructions [here](https://github.com/swabhs/open-sesame) to replicate the causal feature extraction for your own project. You can use the example file "sentences.txt" that we have provided. Please note that input needs to be specified in a file containing one sentence per line.

---

Follow the rest of our project's methodology with the [Keyword Expansion](...).