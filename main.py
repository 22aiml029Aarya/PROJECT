import streamlit as st
from data_processing import load_data, process_data

def main():
    st.title('ACPC College Prediction')

    all_df = load_data()

    entered_rank = st.number_input('Enter Rank:', step=1.0, format="%.2f")

    if st.button('Submit'):
        output = process_data(all_df, entered_rank)
        st.write('Output:')
        st.write(output)

if __name__ == '__main__':
    main()
