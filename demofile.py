import streamlit as st

st.title('welcom vinod nikam')
st.header ('very nice boy')
st.subheader ('vinod')
st.subheader ('pramod')
st.markdown ('i love my famely')
st.code("""for in range(1,3,5):
         print(hello)
""")
st.code("""for in range(56*8)
         print(hello)
""")
name = st.text_input ("Enter your name :")
fname = st.text_input("Enter your Father name")
adr = st.text_area("Enter your tex")
clasdata = st.selectbox("Enter your class:",(1,2,3,4,5,6,7,8) )
button = st.button("done")
if button :
    st.markdown (f"""
    name: {name} 
    father name : {fname}
    address : {adr}
    class : {clasdata}
    """)
