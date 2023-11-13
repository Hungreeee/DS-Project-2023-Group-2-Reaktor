import streamlit as st

import sys

sys.dont_write_bytecode = True
sys.path.insert(1, "../")
from func_import import open_file
import streamlit.components.v1 as components


def render(file_path, title, text, plot, key, file_name: str = "download.csv"):
    with st.expander(title):
        col1, col2 = st.columns([0.88, 0.12])
        col1.markdown(f"## {title}")
        col1.markdown(f"### Description")

        with open(file_path, 'r', encoding='utf-8-sig') as file:
            col2.download_button(
                label="Download data :open_file_folder:",
                data=file,
                file_name=file_name,
                key=key,
            )

        st.markdown(text)
        st.markdown("### Data exploration:")
        if title == "Climate change and butterflies":
            col1, col2 = st.columns([0.85, 0.25])
            year = str(col2.slider("Year slider", 2000, 2008, 2000))
            col1._html(
                open_file(f"./precomp_data/grid_map/butterfly_{year}.html")[1],
                width=1200,
                height=800,
            )
        else:
            components.html(plot, width=1340, height=500)


if __name__ == "__main__":
    render()
