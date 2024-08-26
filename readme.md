# Article Summarizer

Welcome to the Article Summarizer! This project leverages the power of Cohere embeddings and the LangChain framework to provide summarized insights from articles. The application is built using Streamlit, allowing for an interactive and user-friendly experience.

## Introduction

The Article Summarizer is designed to help users quickly obtain summaries and insights from multiple news articles. By simply inputting URLs of news articles, the application processes the content, splits it into manageable chunks, and applies state-of-the-art NLP techniques to retrieve the most relevant information based on user queries.

## Features

- **🔗 URL-based Content Retrieval:** Input multiple article URLs for processing.
- **✂️ Text Splitting:** Automatically splits long articles into smaller, manageable chunks for better analysis.
- **🔍 Contextual Compression:** Uses Cohere's reranking model to compress and retrieve relevant content.
- **🗨️ Interactive Query Interface:** Users can ask questions related to the articles and receive concise, relevant answers.
- **💾 Session Persistence:** Maintains state across queries to provide a smooth user experience.


## Installation

To install and run the project locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ananty1/article-summarizer.git
   cd article-summarizer
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Create a `.env` file in the root directory and add your Cohere API key:
   ```makefile
   COHERE_API_KEY=your-cohere-api-key
   ```

5. **Run the Application**
   ```bash
   streamlit run main.py
   ```

## Usage

Open the application in your browser.

- Input up to three URLs of news articles in the sidebar.
- Click "Process URLs" to load and analyze the content.
- Enter a query in the main interface to retrieve summarized insights based on the processed articles.
- Optionally, click "Quit" to clear the session state and end the session.

## Technologies Used

- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) The core programming language for the project.
- ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) Used for building the interactive web interface.
- ![LangChain](https://img.shields.io/badge/LangChain-0091D5?style=for-the-badge&logo=python&logoColor=white) Provides the framework for handling document loading, splitting, and retrieval.
- ![Cohere](https://img.shields.io/badge/Cohere-6B8E23?style=for-the-badge&logo=python&logoColor=white) Powers the embeddings and reranking models for text processing and retrieval.
- ![FAISS](https://img.shields.io/badge/FAISS-0033A0?style=for-the-badge&logo=python&logoColor=white) Utilized for vector storage and similarity search.
- ![dotenv](https://img.shields.io/badge/dotenv-11A1F7?style=for-the-badge&logo=python&logoColor=white) Manages environment variables securely.


## Project Structure
news-article-summarizer/
    \
      ├── main.py                    # Main application script \
      ├── requirements.txt           # Python dependencies \
      ├── .env                       # Environment variables (not included in the repo)\
      ├── README.md                  # Project documentation\
      └── other necessary files...
## Contributing
Contributions are welcome! If you have suggestions for improvements, feel free to fork the repository, create a new branch, and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Contact
For any inquiries or suggestions, please contact ananty@iitbhilai.ac.in.
