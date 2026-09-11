import streamlit  as st
import predict
import json


st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select page",["Home","Diseases Recognition","About"])

#Home page
if(app_mode == "Home"):
    st.header("MANGO LEAVE DIESEASE RECOGNISION SYSTEM")
    image_path = "Mango anthracnose.jpg"
    st.image(image_path,use_container_width=True)
    st.markdown("""
    Welcome to the Mango Plant Disease Recognition System! 🌿🔍
    
    Our mission is to help in identifying Mango Plant diseases efficiently. Upload an image of a mango plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    ### How It Works
    1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results:** View the results and recommendations for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Disease Recognition** page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
""")
    
# About Page
elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
    #### About Dataset
    ##### Credits:
    Ali, Sawkat, Ibrahim, Muhammad, Ahmed, Sarder Iftekhar, Nadim, Md., Mizanur, Mizanur Rahman, Shejunti, Maria Mehjabin, Jabid, Taskeed (2022), “MangoLeafBD Dataset”, Mendeley Data, V1, doi: 10.17632/hxsnvwty3r.1

    
    <ul>
        <li>Type of data: 240x320 mango leaf images.</li>
        <li>Data format: JPG.</li>
        <li>Number of images: 4000 images. Of these, around 1800 are of distinct leaves, and the rest are prepared by zooming and rotating where deemed necessary.</li>
        <li>Diseases considered: Seven diseases, namely Anthracnose, Bacterial Canker, Cutting Weevil, Die Back, Gall Midge, Powdery Mildew, and Sooty Mould. </li>
        <li>Number of classes: Eight (including the healthy category).
            <ul>
                <li>Anthracnose</li>
                <li>Bacterial Canker</li>
                <li>Cutting Weevil</li>
                <li>Die Back</li>
                <li>Gall Midge</li>
                <li>Healthy</li>
                <li>Powdery Mildew</li>
                <li>Sooty Mould</li>
            </ul>
        </li>
        <li>Distribution of instances: Each of the eight categories contains 500 images.- Data source locations:Four mango orchards of Bangladesh, namely Sher-e-Bangla Agricultural University orchard, Jahangir Nagar University orchard, Udaypur village mango orchard, and Itakhola village mango orchard.
            Where applicable: Suitable for distinguishing healthy and diseases leaves (two-class prediction) as well as for differentiating among various diseases (multi-class prediction).</li>
    </ul>
                
    ##### Technologies Used
    <ul>
        <li>Machine Learning / Deep Learning (CNN)</li>
        <li>Python</li>
        <li>TensorFlow / Keras</li>
        <li>Streamlit (for the web interface)</li>
        <li>OpenCV / Image preprocessing tools</li>
    </ul>
""",unsafe_allow_html=True)
    
#Prediction Page
elif(app_mode=="Diseases Recognition"):
    st.header("Diseases Recognition")
    test_image = st.file_uploader("Choose an image")
    if(st.button("Show Image")):
        if(test_image):
            st.image(test_image,use_container_width=True)
        else:
            st.warning("Please Upload Image First")
    #Predict  Buttom
    if(st.button("Predict")):
        if(test_image):
            with st.spinner("Please Wait.."):
                st.write("Our Prediction")
                result_index = predict.predict(test_image)
                with open("class_name.json","r") as f:
                    data = json.load(f)
                st.success("Model is Predicting it's a {}".format(data["class_name"][result_index]))
        else:
            st.warning("Please Upload Image First")