import os

import streamlit as st
import qrcode
import numpy as np


st.header("Skapa en custom qr-kod")
input_data = st.text_input("Mitt meddelande / url")

qr = qrcode.QRCode( # TODO: fixed size no matter amount of information.
    version=1, # 1-40, if set to None qr.make(fit=True) autodetermines size
    box_size=10, # px size of each little "square", using a big number - made huge difference when reading qr
    error_correction=qrcode.constants.ERROR_CORRECT_L
)

qr.add_data(input_data)
qr.make()
phone_qr = qr.make_image(fill_color="white", back_color="black")

phone_qr_as_np = np.array(phone_qr) # because otherwise I'd have to first store it locally
st.image(phone_qr_as_np)
st.write(input_data)

phone_qr.save("filnamn.png")
with open("filnamn.png", "rb") as f:
    st.download_button("Ladda ner som .png",
                       data=f,
                       file_name=f'{input_data}.png',
                       mime='image/png')

os.remove("filnamn.png")