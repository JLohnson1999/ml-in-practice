import streamlit as st

# Function to calculate expected revenue
def calculate_expected_revenue(sensitivity, specificity, p_mold, p_no_sugar, p_typical_sugar, p_high_sugar):
    # Probabilities and revenues
    p_storm = 0.5
    p_no_storm = 0.5
    revenue_harvest_now = 80000
    revenue_mold = 35000
    revenue_no_mold = 275000
    revenue_no_sugar = 80000
    revenue_typical_sugar = 117500
    revenue_high_sugar = 125000
    
    p_storm_corrected = sensitivity * p_storm / (sensitivity * p_storm + (1 - specificity) * p_no_storm)
    p_no_storm_corrected = specificity * p_no_storm / (specificity * p_no_storm + (1 - sensitivity) * p_storm)
    
    expected_revenue_ml = (p_storm_corrected * (p_mold * revenue_mold + (1 - p_mold) * revenue_no_mold) +
                           p_no_storm_corrected * (p_no_sugar * revenue_no_sugar + 
                                                   p_typical_sugar * revenue_typical_sugar + 
                                                   p_high_sugar * revenue_high_sugar))
    return expected_revenue_ml

# Streamlit app
st.title('Wine Production Decision Model')

# Sensitivity and specificity of the model (assuming these are constants based on your ML model)
sensitivity = 0.8
specificity = 0.9

# User inputs for probabilities
p_mold = st.slider('Chance of botrytis (mold) if storm occurs', min_value=0.0, max_value=1.0, value=0.1)
p_no_sugar = st.slider('Chance of no sugar level increase if no storm', min_value=0.0, max_value=1.0, value=0.6)
p_typical_sugar = st.slider('Chance of typical sugar level increase if no storm', min_value=0.0, max_value=1.0, value=0.3)
p_high_sugar = st.slider('Chance of high sugar level increase if no storm', min_value=0.0, max_value=1.0, value=0.1)

# Calculate the expected revenue and recommended action
expected_revenue_ml = calculate_expected_revenue(sensitivity, specificity, p_mold, p_no_sugar, p_typical_sugar, p_high_sugar)
recommended_action = "Harvest Now" if 80000 > expected_revenue_ml else "Wait for more sugar"

# Display the results
st.write(f'Expected Value (e-value) of the decision: ${expected_revenue_ml:,.2f}')
st.write(f'Recommended alternative: {recommended_action}')
