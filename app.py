import streamlit as st
import pandas as pd
import joblib

# Load the saved model
loaded_model_rfc = joblib.load('model_rf.pkl')

# Define the columns of the dataset
columns = ['Age (yrs)', 'BMI', 'Cycle(R/I)', 'Cycle length(days)', 'AMH(ng/mL)',
           'RBS(mg/dl)', 'Weight gain(Y/N)', 'hair growth(Y/N)', 'Skin darkening (Y/N)',
           'Pimples(Y/N)', 'Fast food (Y/N)', 'Follicle No. (L)', 'Follicle No. (R)',
           'Avg. F size (L) (mm)', 'Avg. F size (R) (mm)']

# Function to collect user input
def collect_input():
    st.sidebar.header('User Input')
    inputs = {}
    for col in columns:
        if col == 'Cycle(R/I)':
            inputs[col] = st.sidebar.selectbox(col, ['Regular', 'Irregular'])
        elif col in ['Weight gain(Y/N)', 'hair growth(Y/N)', 'Skin darkening (Y/N)', 'Pimples(Y/N)', 'Fast food (Y/N)']:
            inputs[col] = st.sidebar.radio(col, ['Yes', 'No'])
        else:
            inputs[col] = st.sidebar.text_input(col, '')
    return inputs

# Function to preprocess input data
def preprocess_input(inputs):
    # Convert 'Cycle(R/I)' from string to numerical value
    inputs['Cycle(R/I)'] = 1 if inputs['Cycle(R/I)'] == 'Regular' else 0
    # Convert 'Weight gain(Y/N)', 'hair growth(Y/N)', 'Skin darkening (Y/N)', 'Pimples(Y/N)', 'Fast food (Y/N)' to binary values
    binary_cols = ['Weight gain(Y/N)', 'hair growth(Y/N)', 'Skin darkening (Y/N)', 'Pimples(Y/N)', 'Fast food (Y/N)']
    for col in binary_cols:
        inputs[col] = 1 if inputs[col] == 'Yes' else 0
    return inputs

# Function to predict PCOS
def predict_pcos(inputs):
    input_df = pd.DataFrame([inputs])
    prediction = loaded_model_rfc.predict(input_df)
    return prediction[0]

# Main function for Streamlit app
def main():
    st.title('PCOS Prediction App')
    inputs = collect_input()
    if st.button('Predict'):
        inputs = preprocess_input(inputs)
        prediction = predict_pcos(inputs)
        if prediction == 1:
            st.error('The patient is predicted to have PCOS.')
            st.subheader('PCOS Diet Plan')
            st.write("- Focus on complex carbohydrates like whole grains, fruits, and vegetables.")
            st.write("- Include lean protein sources such as poultry, fish, tofu, and legumes.")
            st.write("- Limit saturated fats and instead opt for healthy fats like those found in nuts, seeds, and avocado.")
            st.write("- Choose low-glycemic index foods to help manage insulin levels.")
            st.write("- Stay hydrated by drinking plenty of water throughout the day.")
            st.write("- Incorporate anti-inflammatory foods like berries, leafy greens, and fatty fish to reduce inflammation associated with PCOS.")
            st.write("- Consider taking supplements like inositol, vitamin D, and omega-3 fatty acids, which may help manage PCOS symptoms (consult with your healthcare provider first).")
            st.write("For more information, you can visit the [PCOS Nutrition Center](https://www.pcosnutrition.com/pcos-diet/) website.")

            st.header("Do's for PCOS:")
            st.write("- Regular exercise, such as aerobic activities and strength training, can help improve insulin sensitivity and manage weight.")
            st.write("- Incorporate fiber-rich foods like vegetables, fruits, and whole grains into your diet to support digestion and keep you feeling full.")
            st.write("- Monitor your carbohydrate intake and choose complex carbs over simple sugars to help regulate blood sugar levels.")
            st.write("- Practice mindful eating habits and pay attention to hunger and satiety cues.")
            st.write("- Get enough sleep and manage stress, as both can affect hormone levels and exacerbate PCOS symptoms.")

            st.header("Don'ts for PCOS:")
            st.write("- Avoid sugary beverages and processed foods, as they can cause spikes in blood sugar levels.")
            st.write("- Limit consumption of red meat and high-fat dairy products, which may contribute to inflammation and insulin resistance.")
            st.write("- Reduce intake of refined carbohydrates like white bread, pasta, and sugary snacks, as they can lead to rapid spikes in blood sugar.")
            st.write("- Don't skip meals or follow restrictive diets, as this can disrupt metabolism and hormone balance.")
            st.write("- Avoid excessive consumption of caffeine and alcohol, which can worsen PCOS symptoms.")
        else:
            st.success('The patient is predicted to not have PCOS.')

            st.subheader("Recommendations for Non-PCOS Individuals")

            # Balanced Diet
            st.markdown("Balanced Diet: Opt for a balanced diet rich in fruits, vegetables, whole grains, lean proteins, and healthy fats. Limit processed foods, sugars, and excessive fats.")
            st.markdown("[PCOS Diet Recommendations from Johns Hopkins Medicine](https://www.hopkinsmedicine.org/health/wellness-and-prevention/pcos-diet)")

            # Regular Exercise
            st.markdown("Regular Exercise: Incorporate regular physical activity into your routine. Aim for at least 30 minutes of moderate exercise most days of the week.")

            # Maintain a Healthy Weight
            st.markdown("Maintain a Healthy Weight: Strive to maintain a healthy weight through a combination of diet and exercise. Consult with a healthcare provider for personalized advice.")

            # Manage Stress
            st.markdown("Manage Stress: Practice stress-reducing techniques such as mindfulness, meditation, yoga, or deep breathing exercises to manage stress levels.")

            # Adequate Sleep
            st.markdown("Adequate Sleep: Ensure you get enough quality sleep each night. Aim for 7-9 hours of sleep for optimal health.")

            # Regular Health Check-ups
            st.markdown("Regular Health Check-ups: Schedule regular check-ups with your healthcare provider for preventive screenings and overall health assessment.")

            # Stay Hydrated
            st.markdown("Stay Hydrated: Drink plenty of water throughout the day to stay hydrated and support bodily functions.")
if __name__ == '__main__':
    main()
