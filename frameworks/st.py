import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import altair as alt

st.set_page_config(
    
    page_title= 'Streamlit App Configuration',
    page_icon= '😘',
    layout = 'wide',
    )


st.title('Hello World')

st.header('Stramlit App')

st.subheader('Streamlit is a freamework for Machine Learning and Data Science')

st.write('Hello World')

st.markdown('Hello World')

st.code(print('Hello World'))

st.latex("a^2 + b^2 = c^2")

st.divider()

st.header("this portion is for mertices and message")

st.metric(label = "Revenue", value = 1234, delta = "10%", delta_color="inverse")

st.error("This is an error message")

st.warning("This is a warning message")

st.info("This is an info message")

st.success("This is a success message")

st.exception(ValueError("This is an exception message"))

st.divider()

st.header("3. data Display")

df = pd.DataFrame(np.random.randn(10,2), columns = ['a', 'b'])

st.dataframe(df)
st.table(df)
st.json(df.to_dict())

st.divider()

st.header("4. Charts and Maps")

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

chart = alt.Chart(df.reset_index()).mark_line().encode(x='index', y='a')
st.altair_chart(chart, use_container_width=True)
fig,ax = plt.subplots()
ax.plot(df.index, df.a)
st.pyplot(fig)

st.divider()





