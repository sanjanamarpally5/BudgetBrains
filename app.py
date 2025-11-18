# app.py
import streamlit as st
import pandas as pd


# ------------------ DUMMY GENERATOR (NO ERRORS) ------------------
class DummyGenerator:
    @staticmethod
    def generate(prompt, max_new_tokens=300, **kwargs):
        return "🤖 *Model response placeholder (Granite not connected)*\n\nYou asked:\n" + prompt


def get_generator():
    return DummyGenerator()


# ------------------ DEMOGRAPHIC DETECTOR ------------------
def detect_user_demographic(profile):
    age = profile.get("age", 0)
    occupation = profile.get("occupation", "").lower()

    if age < 18:
        return "Student"
    elif age > 55:
        return "Senior"
    elif "engineer" in occupation:
        return "Working Professional"
    else:
        return "General User"


# ------------------ HEADER & FOOTER ------------------
def header():
    st.title("💰 Personal Finance Assistant")


def footer():
    st.markdown("---")
    st.caption("© 2025 Personal Finance Bot")


# ------------------ BUDGET FUNCTIONS ------------------
def upload_transactions():
    uploaded_file = st.file_uploader("Upload CSV file with transactions")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        return df
    return None


def show_summary(df):
    if df is None:
        st.warning("Please upload a CSV first.")
        return

    st.subheader("Budget Summary")
    st.write(df.describe(include="all"))


# ------------------ MAIN APP ------------------
def main():
    header()

    # Sidebar
    st.sidebar.title("Settings")

    profile = {
        "name": st.sidebar.text_input("Name", ""),
        "age": st.sidebar.number_input("Age", min_value=0, max_value=120, value=30),
        "occupation": st.sidebar.text_input("Occupation", "")
    }

    user_type = detect_user_demographic(profile)
    st.sidebar.write("Detected user type:", user_type)

    page = st.sidebar.radio("Page", ["Chat", "Budget", "Insights", "Settings"])

    # Load generator (dummy safe version)
    generator = get_generator()

    # ---------------- CHAT PAGE ----------------
    if page == "Chat":
        st.header("Chat with Finance Bot")
        prompt = st.text_area("Ask something:", height=150)
        tone = st.selectbox("Tone level", ["Simple (student)", "Professional (detailed)"])

        if st.button("Send"):
            with st.spinner("Generating response..."):
                full_prompt = (
                    f"UserType: {user_type}\n"
                    f"Tone: {tone}\n"
                    f"Question: {prompt}\n"
                    f"Respond with personal finance guidance."
                )
                answer = generator.generate(full_prompt)

            st.markdown("### 🤖 Bot:")
            st.write(answer)

    # ---------------- BUDGET PAGE ----------------
    elif page == "Budget":
        st.header("Budget Tool")
        df = upload_transactions()

        if st.button("Generate Budget Summary"):
            show_summary(df)

    # ---------------- INSIGHTS PAGE ----------------
    elif page == "Insights":
        st.header("Spending Insights")

        if st.button("Run Insights (Demo)"):
            demo_prompt = (
                "Analyze a user's spending and provide 5 optimization suggestions "
                "and 3 savings goals."
            )
            response = generator.generate(demo_prompt)
            st.write(response)

    # ---------------- SETTINGS PAGE ----------------
    else:
        st.header("Settings")
        st.write("Configure the application settings here.")

    footer()


if __name__ == "__main__":
    main()