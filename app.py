import pickle
import pandas as pd
import streamlit as st


class BoatListingModel:
    def __init__(self, model_file_path):
        self.model = self.load_model(model_file_path)

    def load_model(self, model_file_path):
        with open(model_file_path, "rb") as f:
            return pickle.load(f)

    def predict_views(self, data):
        x = pd.DataFrame(data, index=[0])
        return int(self.model.predict(x)[0])


class BoatListingApp:
    LOCATIONS = (
        "Germany",
        "Italy",
        "France",
        "Switzerland",
        "Netherlands",
        "Croatia (Hrvatska)",
        "Spain",
        "United Kingdom",
        "Denmark",
        "Other",
    )

    BOAT_TYPES = (
        "Motor Yacht",
        "Center console boat",
        "Sport Boat",
        "Fishing Boat",
        "Catamaran",
        "Pontoon Boat",
        "Runabout",
        "Deck Boat",
        "Pilothouse",
        "Cabin Boat",
        "Working Boat",
        "Classic",
        "Bowrider",
        "Trawler",
        "Launch",
        "Flybridge",
        "Water ski",
        "Hardtop",
        "Offshore Boat",
        "Wakeboard/Wakesurf",
        "Passenger boat",
        "House Boat",
        "Ketch",
        "Mega Yacht",
        "Motorsailer",
        "RIB",
    )

    MANUFACTURERS = (
        "Sea Ray",
        "BÃ©nÃ©teau",
        "Quicksilver (Brunswick Marine)",
        "Cranchi",
        "Boesch",
        "Sessa",
        "Sunseeker",
        "Jeanneau",
        "Bayliner",
        "Quicksilver",
        "Fairline",
        "Pedro",
        "Princess",
        "Azimut",
        "Galeon",
        "Bavaria",
        "Sealine",
        "Prestige Yachts",
        "Other",
    )

    MATERIALS = (
        "GRP",
        "Thermoplastic",
        "Aluminium",
        "PVC",
        "Plastic",
        "Steel",
        "Wood",
        "Hypalon",
        "Carbon Fiber",
        "Reinforced concrete",
        "Rubber",
        "Others",
    )

    BOAT_CONDITIONS = (
        "new boat from stock",
        "Used boat",
        "new boat on order",
        "Display Model",
    )

    ENGINE_TYPES = (
        "Diesel",
        "Unleaded",
        "Electric",
        "Gas",
        "Hybrid",
        "Propane",
        "Others",
    )

    def __init__(self):
        self.model = BoatListingModel("./models/boat_listing_model.pickle")

    def show_header(self):
        st.title("Boat Listing Optimisation using Predictive Analytics")
        st.markdown(
            """
        This web application is an implementation of a predictive model 
        for estimating the views of a boat listing on a boat-selling platform. 
        The model takes inputs such as the boat's location, boat type, 
        manufacturer, price, age, and others, and predicts the number of views the listing will receive.

        <div style="background-color:#f63366;
                    border-radius: 25px;
                    padding:5px">
            <h2 style="color:white;
                       text-align:center;">
                Boat Listing Views Prediction
            </h2>
        </div>
        """,
            unsafe_allow_html=True,
        )

    def get_input_data(self):
        location = st.selectbox("Choose a Location: ", self.LOCATIONS)
        boat_type = st.selectbox("Choose a Boat Type: ", self.BOAT_TYPES)
        price_usd = st.text_input("Input Price (USD) of Boat: ")
        manufacturer = st.selectbox("Choose a Manufacturer: ", self.MANUFACTURERS)
        material = st.selectbox("Choose a Material: ", self.MATERIALS)
        age = st.text_input("Input Age of Boat: ")
        boat_condition = st.selectbox("Choose Boat Condition: ", self.BOAT_CONDITIONS)
        length = st.text_input("Input Length (meters) of Boat: ")
        width = st.text_input("Input Width (meters) of Boat: ")
        engine_type = st.selectbox("Choose Boat Condition: ", self.ENGINE_TYPES)

        data = {
            "boat_type": boat_type,
            "manufacturer": manufacturer,
            "length": length,
            "width": width,
            "material": material,
            "location": location,
            "price_usd": price_usd,
            "boat_condition": boat_condition,
            "engine_type": engine_type,
            "age": age,
        }

        return data

    def show_prediction_result(self, views):
        st.success(f"Estimated number of views per week: {views}")

    def run(self):
        self.show_header()
        data = self.get_input_data()
        if st.button("Predict View"):
            views = self.model.predict_views(data)
            self.show_prediction_result(views)


if __name__ == "__main__":
    app = BoatListingApp()
    app.run()
