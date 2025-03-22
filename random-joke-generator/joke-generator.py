import streamlit as st
import requests

def get_random_joke():
    """Fetches a random joke from the API"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch a joke. Please try again later."
    except requests.RequestException:
        return "Why did the programmer quit his job? \nBecause he didn't get array!"

def main():
    st.title("😂Random Joke Generator")
    st.write("Click the button below to generate a random joke")

    if st.button("Generate Joke"):
        joke = get_random_joke()
        st.success(joke)

    st.divider()

    st.markdown(
        """
        <div style="text-align: center;">  
            <p>Joke from Official Joke API</p>
            <p>Built with ❤️ by <a href="https://github.com/ummay480" target="_blank">Ummay Kulsoom</a></p>
            <p>🌐 <a href="https://ramadan-coding-night-random-joke-generator.streamlit.app/" target="_blank">Try it Live</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
