# 🎥 YouTube Video Insight

A Streamlit-based AI application that lets you enter a YouTube video URL and ask questions about the video's transcript.

The application uses **LangChain**, **FAISS**, **OpenRouter**, and **YouTube transcripts** to retrieve relevant transcript sections and generate answers using an LLM.

## ✨ Features

- 📺 Extract transcripts from YouTube videos
- ✂️ Split transcripts into smaller chunks
- 🔎 Perform semantic search using FAISS
- 🤖 Ask questions about the video
- 💬 Generate answers using an LLM through OpenRouter
- 🌐 Simple and interactive Streamlit UI
- 🔐 API key management using `.env`

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Web application UI
- **LangChain** – LLM application framework
- **FAISS** – Vector database for similarity search
- **OpenRouter** – LLM and embedding API
- **YouTube Transcript** – Extract video transcripts
- **OpenAI Embeddings** – Generate text embeddings
- **dotenv** – Manage environment variables

## 📁 Project Structure

```text
youtube-assistant/
│
├── main.py
├── langchain_helper.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> **Note:** Never commit your `.env` file or API keys to GitHub.

## ⚙️ How It Works

The application follows this workflow:

```text
YouTube URL
     │
     ▼
YouTube Transcript
     │
     ▼
Text Splitting
     │
     ▼
OpenAI Embeddings
     │
     ▼
FAISS Vector Database
     │
     ▼
User Question
     │
     ▼
Similarity Search
     │
     ▼
Relevant Transcript Chunks
     │
     ▼
OpenRouter LLM
     │
     ▼
Generated Answer
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Princeprem117/youtube-video-insight.git
cd YOUR_REPOSITORY
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .yt
```

Activate it:

```powershell
.yt\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .yt
source .yt/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you haven't created `requirements.txt` yet, you can generate it with:

```bash
pip freeze > requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

Get an API key from OpenRouter.

**Important:** Do not upload `.env` to GitHub.

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run main.py
```

Streamlit will provide a local URL similar to:

```text
http://localhost:8501
```

Open the URL in your browser.

## 💡 Usage

1. Enter a YouTube video URL.
2. Enter a question about the video.
3. Click **Submit**.
4. The application retrieves the video's transcript.
5. Relevant transcript sections are found using FAISS similarity search.
6. The LLM generates an answer based only on the retrieved transcript information.

### Example Questions

```text
What is this video about?

What are the main points discussed in the video?

Explain the concept discussed in the video.

What examples are mentioned?

What are the key takeaways?
```

## 🔑 Environment Variables

The project requires the following environment variable:

| Variable | Description |
|---|---|
| `OPENROUTER_API_KEY` | API key used to access OpenRouter |

Example:

```env
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxx
```

## 🔒 Security

Add the following to `.gitignore`:

```gitignore
.env
.yt/
__pycache__/
*.pyc
```

Never commit API keys, passwords, or other secrets to your public repository.

## 🧠 Architecture

The application uses a Retrieval-Augmented Generation (RAG) approach.

### 1. Transcript Retrieval

The YouTube transcript is loaded using `YoutubeLoader`.

### 2. Text Chunking

The transcript is divided into smaller chunks using `RecursiveCharacterTextSplitter`.

### 3. Embeddings

Each chunk is converted into a vector representation using an embedding model.

### 4. Vector Storage

The embeddings are stored in a FAISS vector database.

### 5. Similarity Search

When the user asks a question, FAISS searches for the most relevant transcript chunks.

### 6. Answer Generation

The retrieved transcript content is passed to the LLM through OpenRouter to generate the final response.

## ⚠️ Limitations

- The video needs to have an accessible transcript.
- Transcript availability depends on YouTube.
- The application answers based on the retrieved transcript content.
- Very long transcripts may require additional optimization.
- API usage may have limits depending on the OpenRouter model and account.

## 🔮 Future Improvements

- Add automatic transcript language detection
- Support multiple transcript languages
- Add video summary generation
- Add chat history
- Improve error handling
- Add transcript caching
- Add timestamp references in answers
- Support multiple YouTube videos
- Deploy the application online
- Add a more advanced chat interface

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit your changes:

```bash
git add .
git commit -m "Add new feature"
```

5. Push the branch:

```bash
git push origin feature/new-feature
```

6. Open a Pull Request.

## 📄 License

This project is open source and available under the **MIT License**.

---
## 👨‍💻 About the Author

### Prince Prem

Aspiring **AI Engineer** focused on building practical AI systems and understanding the engineering foundations behind modern RAG and Agentic AI applications.

**GitHub:**

`https://github.com/Princeprem117`

**LinkedIn:**

`https://www.linkedin.com/in/princeprem14/`