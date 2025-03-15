import streamlit as st

# Your main content
st.title("Random Joke Generator")
st.write("Click the button below to generate a random joke")

if st.button("Generate Joke"):
    st.success("Here is a random joke!")

st.divider()

# Footer with fixed position
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            color: #333;
        }
    </style>
    <div class="footer">
        <p>Joke from official joke API</p>
        <p>Built with ❤️ by <a href="https://github.com/ummay480" target="_blank">Ummay Kulsoom</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
