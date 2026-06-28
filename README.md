# AI-Research Portal 

An enterprise-grade SaaS application designed to automate the extraction and analysis of financial metrics from corporate earnings transcripts. It leverages Cohere's Large Language Models to parse raw PDF documents and generates structured insights, presenting them on a dynamic, responsive React dashboard.

**Live Demo:** [Insert Correct Vercel/Frontend Link Here]

##  Core Features

* **Automated Document Parsing:** Upload raw corporate transcripts (PDFs) directly via the frontend.
* **Intelligent Extraction:** Uses Cohere LLM (low temperature for zero hallucination) to accurately extract Management Tone, Confidence Levels, Key Positives, and Forward Guidance.
* **Enterprise UI/UX:** A clean, responsive dashboard featuring status badges, split-grid layouts, and action rows, built with modular CSS.
* **Document Vault:** Maintains a localized session history of processed documents with status tracking and timestamps.
* **Strict Data Validation:** Backend enforces strict JSON schema validation using Pydantic, ensuring predictable frontend rendering.

##  Tech Stack

**Frontend:**
* React.js (Component-driven architecture)
* Custom CSS (CSS Modules/Variables for scoped styling)
* Fetch API (for client-server communication)

**Backend:**
* Python 3.x
* FastAPI (High-performance asynchronous API framework)
* Pydantic (Data validation and settings management)
* Cohere API (LLM integration for NLP tasks)
* Regex & JSON (For sanitizing LLM markdown outputs)

##  System Architecture

1.  **Client:** User uploads a PDF via the React dashboard (`UploadZone`).
2.  **API Layer:** FastAPI receives the document, parses the text, and constructs a strict prompt.
3.  **Inference:** Cohere's model analyzes the text to extract financial data points.
4.  **Validation:** FastAPI parses the LLM output, validates it against the `AnalysisReport` schema, and returns a sanitized JSON response.
5.  **Rendering:** React updates the UI state and dynamically renders the `ReportViewer`.

##  Local Development Setup

### Prerequisites
* Node.js (v16+)
* Python (3.9+)
* Cohere API Key

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend

 ###  Create and activate a virtual environment:

 python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

 ### Install dependencies:

 pip install -r requirements.txt

 ### Create a .env file in the root backend directory and add your key:

 COHERE_API_KEY=your_api_key_here

 
 ### Start the FastAPI server:

 uvicorn main:app --reload


 ## Frontend Setup

 ### Navigate to the frontend directory:
 cd frontend

 ### Install dependencies:
 npm install

 ### Start the development server:
 npm start

