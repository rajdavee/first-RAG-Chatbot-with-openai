# First RAG Chatbot with OpenAI

This is a Retrieval-Augmented Generation (RAG) powered chatbot built using OpenAI's models. The system can answer questions based on the data provided through documents. The chatbot integrates the power of OpenAI's API to retrieve and generate answers relevant to the given data.

## Features

- **Document-based QA**: Allows users to input a document, and the system provides answers specific to the content of that document.
- **Powered by OpenAI**: Uses OpenAI's API for generating responses, with integration for RAG.

## Prerequisites

Before running the app, make sure you have the following:

- Python 3.7 or later
- A valid OpenAI API key (required for generating responses using OpenAI's models)
- Streamlit (for running the app)

## Installation

Follow these steps to set up the project:

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/rajdavee/first-RAG-Chatbot-with-openai.git
cd first-RAG-Chatbot-with-openai
```

### 2. Create a Virtual Environment (Optional but Recommended)

It's recommended to create a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts ctivate
```

### 3. Install Dependencies

Install the required Python libraries using the provided `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables

In the root folder of the project, create a `.env` file. Add your OpenAI API key in the `.env` file as follows:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

Replace `your_openai_api_key_here` with your actual OpenAI API key. You can obtain this key by signing up for OpenAI's API [here](https://beta.openai.com/signup/).

### 5. Run the Application

Run the Streamlit app using the following command:

```bash
streamlit run StreamlitApp.py
```

This will start the Streamlit app in your browser, where you can interact with the chatbot.

## Usage

- After running the Streamlit app, you can input a document and ask questions about the content of that document.
- The chatbot will retrieve relevant information from the document and generate a response using OpenAI's models.

## Additional Notes

- Make sure to monitor your OpenAI API usage, as the API is not free and may incur charges based on the usage.
- If you need to modify the model or the response handling, you can edit the logic within `StreamlitApp.py` or the functions that handle API calls.

## License

This project is open-source and available under the [MIT License](LICENSE).
