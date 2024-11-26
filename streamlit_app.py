import streamlit as st  
import datetime
from PIL import Image

st.set_page_config(page_title="My Biography", layout='wide')

# ---- HEADER SECTION ----
st.title("BIOGRAPHY")
st.subheader("Hello, I'm Kc")
st.write("A 1st Year student")
# ---- Personal Info (Left Side) ----
# ---- ID (Right Side) ----
with st.container():
    left_column, right_column=st.columns(2)
#allignment
    with left_column: #similar to if-else statement
        st.subheader("Personal Information")
#medium font size
    with left_column: #similar to if-else statement
        st.title("Image File")
        #File uploader
        uploaded_file= st.file_uploader("Upload an image", type=["jpg","jpeg","png"])

        #Display the image if a file is uploaded
        if uploaded_file is not None:
            #Open the image using PIL 
            image= st.image("")
            caption="Upload image",
            use_column_width=True
        else:
            st.write("No file uploaded yet")

        name= st.text_input("Name", "Kc D. Monencillo")

        #age
        age=st.selectbox(
            "Age",
            ("18", "19", "20",
             "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", 
             "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", 
             "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", 
             "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", 
             "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", 
             "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", 
             "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", 
             "91", "92", "93", "94", "95", "96", "97", "98", "99", "100")
        )

        #bday
        bday=st.date_input("Birthday",datetime.date(2005,12,29))

        #gender
        options=["Male","Female"]
        gender=st.pills("Gender",options,selection_mode="single")

        #Family Bcakground
        #Mother
        st.subheader("Family Background")
        mother=st.text_input("Mother's name","Flordelita D. Monencillo")
        mbday=st.date_input("Birthday",datetime.date(1969,4,27))

        #Father
        father=st.text_input("Father's Name","Alwin L. Monencillo")
        mbday=st.date_input("Birthday",datetime.date(1974,6,14))

        st.subheader("Educational Background")
#medium font size
        elem=st.text_area("Elementary","Clementino V. Die Memorial Central Elementary School ")
        hs=st.text_area("Junior High School","Surigao Del Norte National High School ")
        shs=st.text_area("Senior High School","Surigao Del Norte National High School  ")
        college=st.text_area("College","Surigao State University ")
        course=st.text_area("Course","Bachelor of Science in Computer Engineering")
        st.write("---")

#button to change picture
        st.write(" ")
        st.subheader("Social Media Accounts")
        fb=st.text_input("Facebook","Kc Monencillo")
        instagram=st.text_input("Instagram","zzupk")

        with left_column: #similar to if-else statement
            st.subheader("Organization")
#medium font size
            st.write("- I am a member of the Philippine Red Cross youth Surigao del Norte chapter.")
                     





