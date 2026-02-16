# 🌱 Technical test

**First working version of an agentic product.**

---

##How to use

- Make sure Docker Desktop is installed and running before starting the backend or frontend containers.
- Note: docker run will download the image the first time you use it, which may take a few minutes.
- Default ports are 8000 (backend), 5173 (frontend).

**Windows**
- Start Docker Desktop from the Start menu
- Run start_backend.bat
- Run start_frontend.bat
- Open http://localhost:5173/
- Type and submit your question

**Mac or manual command line**
- Open Docker Desktop from Applications
- docker run -p 8000:8000 ghcr.io/ludorif/technical_test:be-v0.1
- docker run -p 5173:80 ghcr.io/ludorif/technical_test:fe-v0.1
- Open http://localhost:5173/
- Type and submit your question

**Questions example**
- How can you help me?
- What are the main genes involved in lung cancer?
- What is the median value expression of genes involved in breast cancer?
- What is the median value expression of genes involved in esophageal cancer?
- gastric median?
- glioblastoma target?
---

## ✨ Architecture

- **Backend:** Python with FastAPI
- **Frontend:** React (Typescript)
- **CI/CD:** Github pipelines
- **Dataset & Tools:** Uses owkin_take_home_data.csv containing gene expression values by cancer type.
- **Focus:** Deliver a runnable prototype within 4 hours. Simple file structure and minimal frontend styling for speed and clarity.


---

##Tradeoffs of AI components in the prototype
- With more time, an LLM could translate user questions into the internal function context, allowing more flexible natural language queries.

##Pros and cons of using AI-assisted coding in this case
** Pros **
- Can help with architecture
- Can help with format (i.e. workflow yml files)
- Can help with performance and optimization
- Can speed up some coding

** Cons **
- Relying too much on AI to write code can create lack of knowledge or understanding of the code and an incapacity to be able to fix or improve it
- AI may produce incorrect solutions if context is incomplete
- Human validation remains essential

## 🗺 Next steps

- Unit testing
- Integrate LLM for flexible natural language understanding
- Asynchronous API calls for performance
- Questions history and multi-step queries
- api_key to limit number of requests

# Copyright (c) 2025 Ludovic Riffiod
