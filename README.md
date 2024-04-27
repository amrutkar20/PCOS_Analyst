# PCOS_Analyst

### What is PCOS?

According to WHO, Polycystic Ovary Syndrome (PCOS) is a common hormonal condition that affects women of reproductive age. It usually starts during adolescence, but symptoms may fluctuate over time.

PCOS can cause hormonal imbalances, irregular periods, excess androgen levels and cysts in the ovaries. Irregular periods, usually with a lack of ovulation, can make it difficult to become pregnant. PCOS is a leading cause of infertility.

The condition affects an estimated 8–13% of women of reproductive age, and up to 70% of cases are undiagnosed. PCOS prevails in South Asian women, especially in Pakistani women, is 52% as compared to white population with 20 - 25% in UK (NIH, 2020), around 2-folds more than worldwide reports.

### Purpose

To address the issue of undiagnosed cases issue, we have created a classification model. This model aims to improve the accuracy of PCOS diagnosis while making it more cost-effective. By considering various factors like blood tests, menstrual cycles, lifestyle, age etc, the model seeks to revolutionize how we identify PCOS, ultimately benefiting those affected by this condition.

### Dataset

The dataset contains 43 physical and clinical parameters to determine PCOS and infertility related issues collected from 10 different hospitals across Kerala, India on a set of 541 samples of fertile female patients. The data was split in 80-20 ratio for training and testing.

### Models Used
Several diiferent models were used including the RandomForestClassifier(), KNeighborsClassifier(), AdaBoostClassifier() and XGBClassifier() etc as welll as the StackingClassifier() using RandomForestClassifier() as the default meta model with promising results.

### Instructions for Use

1. Install the required dependencies from the `requirements.txt` file using the following command:

   ```bash
   pip install -r requirements.txt
   ```

2. Load the model from the PKL file into your application. You can do this by importing the necessary libraries and loading the model as follows:

   ```python
   import joblib
   # Load the model
   loaded_model = joblib.load('your_model.pkl')
   ```

3. Run your Streamlit application by executing the following command in your terminal:

   ```bash
   streamlit run app.py
   ```

4. Once the application is running, open it in your web browser to see it in action.

![WhatsApp Image 2024-04-27 at 03 10 39_bae1cb10](https://github.com/amrutkar20/PCOS_Analyst/assets/104386663/5612b040-0128-49dd-a182-2d8a317a59d4)


![image](https://github.com/amrutkar20/PCOS_Analyst/assets/104386663/d4e13be1-e85c-4888-99e1-1cef5a386775)


![image](https://github.com/amrutkar20/PCOS_Analyst/assets/104386663/4d4e6c86-ac4f-465e-912b-8110229036f9)

Link:
- Kaggle Notebook: [PCOS Classification Notebook](https://www.kaggle.com/code/pamrutkar20/pcos-classification-ipynb#ML-Pipeline)

- Kaggle Datasets: [PCOS Data](https://www.kaggle.com/datasets/pamrutkar20/pcos-data/data)

- GitHub Repository: [PCOS Analyst Repo](https://github.com/amrutkar20/PCOS_Analyst.git)

- Google Drive Notebook: [PCOS Google Drive Notebook](https://drive.google.com/file/d/1VPA5fK_X0YAb4LqGEs6Abg9nep0-E_e9/view?usp=sharing)

- Medium Blog: [Predicting PCOS Using Machine Learning Algorithms: A Binary Classification Approach](https://medium.com/@prathameshamrutkar3/predicting-pcos-using-machine-learning-algorithms-a-binary-classification-approach-d765ab8159fe)



