title: "AI-Powered Streamlit App (GroqAI)"

description: |
  This is my submission for the AI Intern Assignment.  
  The project is a Streamlit app that includes three small AI-powered tools:

  1. **AI Q&A Bot** – Ask any question and get structured AI answers.
  2. **Text Summarizer** – Summarizes any blog/article in 3 structured sentences.
  3. **Expense Tracker** – Track expenses and see a weekly/monthly summary.

  The focus is on effort, resourcefulness, and documentation rather than polish.  
  That’s why I’ve included not only the final working solution but also the issues I faced and how I solved them.

setup_instructions:
  - step: "Clone this repo"
    commands: |
      git clone https://github.com/Ayushmunot-1/AI-Application.git
      cd AI-Application

  - step: "Create a virtual environment (recommended)"
    commands: |
      python -m venv venv
      venv\Scripts\activate

  - step: "Install dependencies"
    commands: |
      pip install -r requirements.txt

  - step: "Set up API Key"
    notes: |
      This project uses Groq AI (LLaMA models).
      Create a .env file in the root folder and add your Groq API key:
    env_file: |
      GROQ_API_KEY=your_api_key_here

  - step: "Run the app"
    commands: |
      streamlit run app.py

documentation_of_journey:
  setup:
    - "Installed Python & Streamlit"
    - "Created repo on GitHub"
    - "Installed groq library to access LLaMA models"
    - "Added .env file to handle API key securely"

  issues_faced:
    - issue: "Secrets.toml error in Streamlit"
      attempt: "Tried using st.secrets['GROQ_API_KEY'] -> got parsing error"
      solution: "Fixed it by switching to .env file + python-dotenv"
    - issue: "Authentication error (Invalid API Key)"
      attempt: "My key was not being read properly"
      solution: "Solved by verifying .env path and using load_dotenv()"
    - issue: "Model decommissioned error"
      attempt: "Initially used llama3-8b-8192 -> got error: model decommissioned"
      solution: "Fixed by switching to llama-3.3-70b-versatile (as recommended in Groq docs)"

implemented_features:
  AI_QA_Bot:
    - "Added a structured prompt template for better responses:"
    - "Key Idea"
    - "Explanation"
    - "Example"

  Text_Summarizer:
    - "Added structured summarization template:"
    - "Key Point Summary"
    - "Important Details"
    - "Implication/Example"

  Expense_Tracker:
    - "Simple form to input expenses (food, rent, travel, etc.)"
    - "Outputs a weekly/monthly summary"
