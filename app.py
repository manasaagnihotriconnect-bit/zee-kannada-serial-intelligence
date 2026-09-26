import streamlit as st
from discovery import search_zee5


st.set_page_config(
    page_title="Zee Kannada Serial Intelligence",
    page_icon="📺",
    layout="wide"
)

st.title("📺 Zee Kannada Serial Intelligence")

st.caption(
    "Automated market research and content intelligence "
    "for Zee Kannada serials"
)

st.divider()

st.subheader("🔎 Analyze a Zee Kannada Serial")

serial_name = st.text_input(
    "Enter Serial Name",
    placeholder="e.g., Lakshmi Nivasa"
)

st.caption(
    "Enter any Zee Kannada serial. The system will automatically "
    "search for the latest available information."
)

if st.button("🚀 ANALYZE SERIAL", type="primary"):

    if not serial_name.strip():

        st.warning("Please enter a serial name.")

    else:

        with st.spinner(
            f"Finding information for {serial_name}..."
        ):

            results = search_zee5(serial_name)

        if not results:

            st.error(
                "No reliable source was found for this serial."
            )

        else:

            st.success(
                f"Sources found for **{serial_name}**"
            )

            st.divider()

            st.header("🔎 Discovered Sources")

            for result in results:

                st.markdown(
                    f"### {result['title']}"
                )

                st.write(
                    result["url"]
                )

            st.divider()

            st.header("📊 Performance")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("TRP", "Not yet available")

            with col2:
                st.metric("TRP Change", "Not yet available")

            with col3:
                st.metric("Latest Episode", "Searching")

            with col4:
                st.metric("Air Date", "Searching")

            st.divider()

            st.header("📖 Storyline")

            st.info(
                "Episode information will be extracted from "
                "the verified source in the next development stage."
            )

            st.header("🔥 High Point")

            st.info(
                "AI will identify the strongest narrative moment."
            )

            st.header("🪝 Major Hook")

            st.info(
                "AI will identify the main reason to watch "
                "the next episode."
            )

            st.header("👤 Character Intelligence")

            st.info(
                "Characters and episode-level developments "
                "will be extracted automatically."
            )

            st.header("💬 Audience Intelligence")

            st.info(
                "Public audience reactions will be analysed "
                "after the source collection layer is connected."
            )

            st.header("🆚 Competitive Intelligence")

            st.info(
                "Relevant Kannada serials will be identified "
                "and compared using publicly available information."
            )
