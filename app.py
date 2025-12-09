import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ----------------------------
#  Load trained model
# ----------------------------
model = joblib.load("airbnb_price_model.pkl")

# ----------------------------
#  Constants / Choices
# ----------------------------

ROOM_TYPES = [
    "Entire home/apt",
    "Private room",
    "Shared room"
]

# 👉 Replace the [...] with the list you printed from Colab
NEIGHBORHOODS = [
    # Example (dummy) values – REPLACE with your real list:
    # 'Belltown', 'Ballard', 'West Queen Anne', ...
    # ---- paste from Colab below this line ----
]

# If list is empty by mistake, fall back to a simple default
if not NEIGHBORHOODS:
    NEIGHBORHOODS = ["Belltown", "Ballard", "West Queen Anne"]

# ----------------------------
#  Page config
# ----------------------------
st.set_page_config(
    page_title="Airbnb Price Estimator",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Airbnb Price Estimator")
st.caption("Predict the nightly price of an Airbnb listing in Seattle based on its features.")

st.markdown("---")

# ----------------------------
#  Layout: two columns of inputs
# ----------------------------
left_col, right_col = st.columns(2)

with left_col:
    room_type = st.selectbox("Room Type", ROOM_TYPES)

    neighbourhood = st.selectbox(
        "Neighborhood",
        NEIGHBORHOODS,
        help="Choose a neighborhood from the dataset."
    )

    accommodates = st.number_input(
        "Accommodates (Guests)",
        min_value=1,
        max_value=16,
        value=2,
        step=1
    )

    minimum_nights = st.number_input(
        "Minimum Nights",
        min_value=1,
        max_value=30,
        value=1,
        step=1
    )

with right_col:
    bedrooms = st.number_input(
        "Bedrooms",
        min_value=0,
        max_value=10,
        value=1,
        step=1
    )

    beds = st.number_input(
        "Beds",
        min_value=0,
        max_value=10,
        value=1,
        step=1
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.5
    )

    number_of_reviews = st.number_input(
        "Number of Reviews",
        min_value=0,
        max_value=500,
        value=10,
        step=1
    )

review_score = st.slider(
    "Review Score (0–100)",
    min_value=0.0,
    max_value=100.0,
    value=90.0,
    step=0.5,
    help="Average review rating of the listing."
)

instant = st.selectbox(
    "Instant Bookable?",
    ["Yes", "No"]
)
instant_bookable = 1 if instant == "Yes" else 0

st.markdown("---")

# ----------------------------
#  Prepare input for model
# ----------------------------
input_df = pd.DataFrame([{
    "room_type": room_type,
    "neighbourhood_cleansed": neighbourhood,
    "accommodates": accommodates,
    "bedrooms": bedrooms,
    "beds": beds,
    "minimum_nights": minimum_nights,
    "number_of_reviews": number_of_reviews,
    "review_scores_rating": review_score,
    "instant_bookable": instant_bookable,
    "bathrooms": bathrooms
}])

st.subheader("🔍 Listing Summary")
st.dataframe(input_df, width="stretch")

st.markdown("---")

# ----------------------------
#  Predict button + output
# ----------------------------
if st.button("🔮 Predict Price"):
    # Model outputs log(price), so convert back
    pred_log = model.predict(input_df)
    predicted_price = np.expm1(pred_log)[0]

    st.success(f"Estimated Price: **${predicted_price:,.2f} per night**")

    st.caption(
        "Note: This is an estimate based on historical Seattle Airbnb data. "
        "Actual prices can vary based on season, demand, and extra amenities."
    )

