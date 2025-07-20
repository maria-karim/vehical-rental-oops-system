import streamlit as st
from oops_myvehicle import Car, Bike, Truck, VehicleManager

# 🔒 Initialize Backend Manager
manager = VehicleManager()

# 🌙 Custom CSS 
import streamlit as st


# Add custom dark yellow theme
st.markdown("""
    <style>
    /* Set full-page background */
    html, body, [class*="stApp"] {
        background-color: #1e1e14 !important;  /* Dark olive yellow */
        color: #FFE873 !important;             /* Soft yellow text */
        font-family: 'Segoe UI', sans-serif;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #FFD700 !important;             /* Golden yellow */
    }

    /* Input fields, text areas */
    input, textarea, select {
        background-color: #3b3b2f !important;  /* Dark input BG */
        color: #ffffff !important;
        border: 1px solid #FFD700 !important;
        border-radius: 8px;
        padding: 8px;
    }

    /* Button styling */
    .stButton>button {
        background-color: #FFD700 !important;
        color: #1e1e14 !important;
        font-weight: bold;
        border-radius: 6px;
        border: none;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease-in-out;
    }

    .stButton>button:hover {
        background-color: #FFC300 !important;
        color: #000000 !important;
    }

    /* Labels, text */
    label, .css-1cpxqw2, .css-1c7y2kd {
        color: #FFE873 !important;
    }

    /* Sidebar styling (optional) */
    [data-testid="stSidebar"] {
        background-color: #2b2b1f !important;
        color: #FFE873 !important;
    }

    hr {
        border-color: #FFD700;
    }
    </style>
""", unsafe_allow_html=True)




st.title("🚘 Vehicle Rental Management System")

# 🧾 Login Section
role = st.sidebar.selectbox("Login as:", ["User", "Admin"])

if role == "Admin":
    password = st.sidebar.text_input("Enter Admin Password", type="password")
    if password != "12345":
        st.error("🔐 Incorrect Password")
        st.stop()
    else:
        st.sidebar.success("✅ Logged in as Admin")

# 👤 USER View
if role == "User":
    st.subheader("🧍 User Portal")
    menu = st.selectbox("Select Action", ["View Available Vehicles", "Rent a Vehicle", "Return a Vehicle"])
    
    if menu == "View Available Vehicles":
        st.markdown("### 🚗 Available Vehicles")
        vehicles = manager.get_available_vehicles()
        if not vehicles:
            st.info("No vehicles available.")
        for v in vehicles:
            st.json(v.to_dict())

    elif menu == "Rent a Vehicle":
        st.markdown("### 📤 Rent a Vehicle")
        vehicle_id = st.text_input("Enter Vehicle ID to Book")
        if st.button("Book Now"):
            if manager.book_vehicle(vehicle_id):
                st.success("✅ Booking Successful")
            else:
                st.error("❌ Invalid ID or Already Booked")

    elif menu == "Return a Vehicle":
        st.markdown("### 📥 Return a Vehicle")
        vehicle_id = st.text_input("Enter Vehicle ID to Return")
        if st.button("Return Now"):
            if manager.cancel_booking(vehicle_id):
                st.success("✅ Returned Successfully")
            else:
                st.error("❌ Invalid ID or Not Booked")

# 🧑‍💼 ADMIN View
elif role == "Admin" and password == "12345":
    st.subheader("👨‍💼 Admin Dashboard")
    menu = st.selectbox("Select Action", ["Add Car", "Add Truck", "Add Bike", "Show All Vehicles", "Cancel Booking"])

    # 🚘 Add Car
    if menu == "Add Car":
        st.markdown("### 🚗 Add Car")
        vehicle_id = st.text_input("Car ID")
        brand = st.text_input("Brand")
        model = st.text_input("Model")
        price = st.number_input("Price per day", min_value=100)
        if st.button("Add Car"):
            car = Car(vehicle_id, brand, model, price)
            manager.add_vehicle(car)
            st.success("✅ Car Added")

    # 🚛 Add Truck
    elif menu == "Add Truck":
        st.markdown("### 🚛 Add Truck")
        vehicle_id = st.text_input("Truck ID")
        brand = st.text_input("Brand")
        model = st.text_input("Model")
        price = st.number_input("Price per day", min_value=200)
        if st.button("Add Truck"):
            truck = Truck(vehicle_id, brand, model, price)
            manager.add_vehicle(truck)
            st.success("✅ Truck Added")

    # 🏍️ Add Bike
    elif menu == "Add Bike":
        st.markdown("### 🏍️ Add Bike")
        vehicle_id = st.text_input("Bike ID")
        brand = st.text_input("Brand")
        model = st.text_input("Model")
        price = st.number_input("Price per day", min_value=50)
        if st.button("Add Bike"):
            bike = Bike(vehicle_id, brand, model, price)
            manager.add_vehicle(bike)
            st.success("✅ Bike Added")

    # 📋 Show All Vehicles
    elif menu == "Show All Vehicles":
        st.markdown("### 📋 All Vehicles (Booked & Available)")
        all_vehicles = manager.vehicles
        for v in all_vehicles:
            st.json(v.to_dict())

    # ❌ Cancel Booking
    elif menu == "Cancel Booking":
        st.markdown("### ❌ Cancel a Booking")
        vehicle_id = st.text_input("Enter Vehicle ID to Cancel Booking")
        if st.button("Cancel Booking"):
            if manager.cancel_booking(vehicle_id):
                st.success("✅ Booking Cancelled")
            else:
                st.error("❌ Invalid ID or Not Booked")


























