<div style="width: 100%;">
  <img src="image1.svg" style="width: 100%;">
</div>

# Machine Learning Study Group

[ML Course](https://www.coursera.org/learn/machine-learning/home/week/1)

# Learning History

<details>
  <summary>Click me</summary>

  **Week 1**
  - `April 18`: Week 1.
      - Week 1, Introduction to ML and learning algorithms.   
      - [Until Jupyter Notebooks](https://www.coursera.org/learn/machine-learning/lecture/lwqzq/jupyter-notebooks)
  - `April 19`: 
  
</details>


## Week 1

> Machine Learning is a field of study that gives computers the ability to learn without being explicitly programmed. Arthur Samuel 1950

- Types of ML algorithms
  - Supervised learning
  - Unsupervised learning
  - Recommender systems
  - Reinforcement learning

**Supervised Learning**
- Algorithms that learning from X input generate Y output.
- Learns from being given right answers.
- Ej. `X: email -> Y: is_spam`, `X:audio -> Y: text transcript`, `X: spanish -> Y: english`, 
- You should train your model with examples inputs X and outputs Y.

*Example of practical use of supervised learning: housing price prediction*
![image](https://github.com/carlogilmar/the-rabbit-notes/assets/17634377/87d9a03d-43b7-4ff2-b4cc-496d76e31d86)

- SL algorithms learn to predict input.
- Classification: breast cancer detection.
- Classification is different than regresion, it predicts categories.
- Can predict a small finite categories.
- You need datasets to train your models.
- Maps input X to output Y.
- Types of SL: classification and regrestion.
  - Regression: predict a number, infinitely possible outputs.
  - Classification: predict categories, small number of possibilities.
 
*Classification*
![image](https://github.com/carlogilmar/the-rabbit-notes/assets/17634377/7b68f57b-5034-4d68-b8ed-d6b28b386a7f)

**Unsupervised Learning**
- Given data is not associated with an specific output.
- Find something interesting in unlabeled data.

![image](https://github.com/carlogilmar/the-rabbit-notes/assets/17634377/a30742b9-6718-42b1-bae2-fc6bfb437176)

- Clustering is one kind of this algorithms
  - DNA microarray genes vs individuals
  - Grouping customers
- Data only comes with inputs X but not output labels
- Algoriths has to find STRUCTURE in the data:
  - Clustering: group similar data.
  - Anomaly detection: Find unusual data points.
  - Dimensionality reduction: Compress data using fewer numbers.

---

  **Linear Regression Model**
  - Predict price of a house is a good example.
  ![image](https://github.com/carlogilmar/the-rabbit-notes/assets/17634377/05e32c6e-0715-44f7-a5dd-e56cb2420d57)

   - Suppose you want to know the proce of a house with 1250 ft.
   - If you have a dataset, then you can create a supervised learning model and train it with "right answers".
   - This is a regression model to predicts numbers.
   - Linear regression is a regression model. (Infinity outputs)
   - Other type of regression model is clasification. (predicts categories, with small number of possible outputs)
   
   **Terminology**
   - Dataset to train a model is `training set`
   - `Input feature` and `output variable`
   - (x, y) = single training example

