import streamlit as st
@st.dialog("Contact Me")
def show_contact_form():
 with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            st.success("Message Successfully Sent!")   
# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("Assets/p-dummy-logo-template-design-600nw-2291517189.jpg.webp", width=230)

with col2:
    st.title("Jany Balasivan", anchor=False)
    st.write(
        "B.Tech from Manipal University,MBA and MS from Christ university and VCU."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()