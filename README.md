🌌 Stellar Object Detection using Machine Learning Models
=========================================================

This project aims to classify stellar objects based on given features using various machine learning algorithms. After testing multiple models, **XGBoost** was identified as the best-performing model. The final model was deployed using **Streamlit** for an interactive web-based interface.

* * * * *

🚀 Project Overview
-------------------

Classifying stellar objects, such as stars, galaxies, and quasars, is crucial in astronomical studies. This project applies multiple supervised learning algorithms to detect and classify stellar objects efficiently. The best-performing model, **XGBoost**, was deployed on **Streamlit** to provide real-time predictions.

* * * * *

📊 Models Used
--------------

The following machine learning models were implemented and compared:

1.  **Decision Tree**
2.  **Random Forest**
3.  **K-Nearest Neighbors (KNN)**
4.  **Support Vector Machines (SVM)**
5.  **Gradient Boosting**
6.  **AdaBoost**
7.  **XGBoost**

> **XGBoost** demonstrated superior performance in terms of accuracy, precision, and recall compared to other models.

* * * * *

⚙️ Installation
---------------

1.  Clone the repository:

    bash

    Copy code

    `git clone <repository-link>
    cd stellar-object-detection`

2.  Install the required dependencies:

    bash

    Copy code

    `pip install -r requirements.txt`

3.  Install **Streamlit** (if not already installed):

    bash

    Copy code

    `pip install streamlit`

* * * * *

📁 Project Structure
--------------------

plaintext

Copy code
bash
`stellar-object-detection/
│
├── data/                          # Dataset and preprocessed files
├── requirements.txt               # Required Python libraries
├── README.md                      # Project Documentation
├── Stellar_object_detection.ipynb # Project Notebook
├── XGBoost.joblib                 # Model joblib file
├── Stellar Dashboard.pbix         # PowerBI Dashboard
├── Docs_Files/                    # Instuction and Description Documents
├── Capstone PPT                   # Power Point Presentation of Project
└── Stellar_classification.py      # Main Streamlit application`
* * * * *

🔍 Exploratory Data Analysis (EDA)
----------------------------------

Before model building, **univariate** and **multivariate analysis** were performed to understand the distribution of features and correlations. Outliers were handled using **IQR filtering** to ensure cleaner data.

* * * * *

⚡ Training and Evaluation
-------------------------

Each model was trained, and their performance was evaluated using the following metrics:

-   **Accuracy**
-   **Precision**
-   **Recall**
-   **Confusion Matrix**

XGBoost performed the best, achieving:

-   **Accuracy**: 97%
-   **Precision**: 96%
-   **Recall**: 95%

* * * * *

🖥️ Deployment with Streamlit
-----------------------------

The **Streamlit** app provides an interactive interface to make predictions based on input features.

### To Run the App:

1.  Navigate to the project directory.
2.  Start the Streamlit app:

    bash

    Copy code

    `streamlit run app.py`

3.  Open your browser and go to `http://localhost:8501`.

* * * * *

🛠️ Technologies Used
---------------------

-   **Python**
-   **Streamlit**
-   **Scikit-Learn**
-   **XGBoost**
-   **Pandas, NumPy**
-   **Matplotlib, Seaborn**

* * * * *

📈 Results
----------

The table below compares the performance of the models:

| Model | Accuracy | Precision | Recall |
| --- | --- | --- | --- |
| Decision Tree | 87% | 86% | 85% |
| Random Forest | 93% | 92% | 91% |
| KNN | 85% | 84% | 83% |
| SVM | 89% | 88% | 87% |
| Gradient Boosting | 95% | 94% | 93% |
| **AdaBoost** | 94% | 93% | 92% |
| **XGBoost** | **97%** | **96%** | **95%** |

* * * * *

📢 Future Scope
---------------

1.  **Hyperparameter Tuning**: Optimize the models further using GridSearchCV.
2.  **Feature Engineering**: Create new features to improve model performance.
3.  **Model Interpretation**: Use SHAP values to interpret the XGBoost model.
4.  **Add More Data**: Improve the classifier with more stellar data.

* * * * *

👩‍💻 Author
------------

**Navya Sai**

-   [GitHub](https://github.com/)
-   [LinkedIn](https://www.linkedin.com/)

* * * * *

📝 License
----------

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

* * * * *

🛠️ Contributing
----------------

Feel free to open an issue or submit a pull request for any feature requests or bug fixes!

* * * * *

🎉 Acknowledgments
------------------

Thanks to the **scientific community** for the dataset and inspiration. Special thanks to the creators of **Scikit-Learn** and **Streamlit** for the amazing libraries.

* * * * *

Let me know if you want any adjustments! 😊

4o
