import streamlit as st

def main():
    st.title("Hello World!")
    st.write("Welcome to my first Streamlit app!")
    
    # Add a slider
    x = st.slider('Select a value', 0, 100, 50)
    st.write(f'You selected: {x}')
    
    # Add a text input
    name = st.text_input('Enter your name')
    if name:
        st.write(f'Hello {name}!')

if __name__ == "__main__":
    main()
