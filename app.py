import streamlit as st
import datetime
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("⚠️ API Key not found. Please set GROQ_API_KEY in your .env file.")
    st.stop()

# Initialize Groq client
client = Groq(api_key=api_key)

# Streamlit page setup
st.set_page_config(page_title="AI Test", layout="centered")
st.title("Application of Groq")
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Choose a feature:", ["AI Q&A Bot", "Text Summarizer", "Expense Tracker"])

# ---------------------- Q&A BOT ----------------------

def generate_prompt(user_question):
    """
    Wraps the user's question in a structured template.
    """
    prompt = f"""
You are a helpful assistant. Please answer the following question in a structured format:

Question:
{user_question}

Answer:
1. Short summary (1-2 sentences)
2. Detailed explanation
3. Optional example (if applicable)
"""
    return prompt

def summarizer_prompt(text):
    """
    Wraps the input text in a structured summarization template.
    """
    prompt = f"""
You are an expert content summarizer. Summarize the following text clearly and concisely in exactly 3 sentences. 
Format your answer as follows:

1. Key Point Summary: <one-sentence main idea>
2. Important Details: <one sentence elaborating key details>
3. Implication/Example: <one sentence giving example or implication if applicable>

Text to summarize:
{text}
"""
    return prompt


if choice == "AI Q&A Bot":
    st.header("Ask me anything")
    question = st.text_input("Enter your question:")
    
    if st.button("Get Answer"):
        if not question.strip():
            st.warning("Please enter a question!")
        else:
            with st.spinner("Thinking..."):
                try:
                    prompt = question  # You probably want to use the actual question here
                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",  # Groq LLaMA model
                        messages=[
                            {"role": "system", "content": "You are an excellent, helpful and most pro-efficient assistant."},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    st.success(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error: {e}")



# ---------------------- TEXT SUMMARIZER ----------------------

elif choice == "Text Summarizer":
    st.header("Text Summarizer")
    text = st.text_area("Paste an article/blog post:")
    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "You are an excellent, helpful and most pro-efficient assistant summarizer."},
                        {"role": "user", "content": f"Summarize this in 3 sentences and cover all the important topics, keywords etc. into it and also add the formula wherever it is necessary :\n{text}"}
                    ]
                )
                st.info(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")

# ---------------------- EXPENSE TRACKER ----------------------
elif choice == "Expense Tracker":
    st.header("Personal Expense Tracker")
    st.write("Add your daily expenses and see weekly/monthly summary.")

    if "expenses" not in st.session_state:
        st.session_state["expenses"] = []

    category = st.selectbox("Category:", ["Food", "Rent", "Travel", "Other"])
    amount = st.number_input("Amount:", min_value=0.0, step=0.5)
    if st.button("Add Expense"):
        st.session_state["expenses"].append({
            "category": category,
            "amount": amount,
            "date": datetime.date.today()
        })
        st.success(f"Added {amount} for {category}")

    if st.session_state["expenses"]:
        st.subheader("Expense Summary")
        total = sum(e["amount"] for e in st.session_state["expenses"])
        st.write(f"**Total Expenses:** {total}")

        today = datetime.date.today()
        week_expenses = [e["amount"] for e in st.session_state["expenses"] if (today - e["date"]).days <= 7]
        st.write(f"**Last 7 Days:** {sum(week_expenses)}")

        month_expenses = [e["amount"] for e in st.session_state["expenses"] if e["date"].month == today.month]
        st.write(f"**This Month:** {sum(month_expenses)}")

        categories = {}
        for e in st.session_state["expenses"]:
            categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]
        st.bar_chart(categories)
