# GAIA Multi-Tool AI Agent

This repository contains a general-purpose AI agent built as the final project for the **Hugging Face AI Agents Course**.

The project was designed to solve a subset of **GAIA Level 1 benchmark questions**, which test an AI assistant’s ability to reason, retrieve information, use tools, process files, and return concise factual answers.

The agent achieved **17 correct answers out of 20** in the course evaluation setup, significantly above the required passing threshold of **30%**.

---

## Project Overview

The goal of this project was to build an AI agent capable of answering real-world questions that require more than a simple language model response.

To do this, the agent combines:

- A reasoning LLM through **Groq**
- Agent orchestration with **LangGraph**
- Tool calling with **LangChain**
- Web and document retrieval
- File analysis tools
- Mathematical and code execution tools
- A Supabase vector store for retrieving similar GAIA-style examples

The agent was originally developed and evaluated inside the Hugging Face course environment using the provided API for fetching questions and submitting answers.

---

## Architecture

```text
User Question
     │
     ▼
LangGraph Agent Orchestrator
     │
     ├── System Prompt
     │
     ├── Similar Question Retrieval from Supabase Vector Store
     │       └── metadata.jsonl / GAIA examples embedded with all-mpnet-base-v2
     │
     ├── LLM: ChatGroq(qwen-qwq-32b, temperature=0)
     │
     └── Tool Calling Loop
             ├── Web search via Tavily
             ├── Wikipedia search
             ├── Arxiv search
             ├── YouTube transcript extraction
             ├── PDF/text/image/CSV/Excel analysis
             ├── OCR
             ├── Math tools
             ├── Code execution
             └── Image tools
```
---

## Key Files
agent/agent.py

Main orchestration file. It builds the LangGraph workflow, loads the system prompt, initializes the LLM, binds the tools, and defines the interaction loop between the assistant and the available tools.

The LLM used in this implementation was:

ChatGroq(model="qwen-qwq-32b", temperature=0)
tools/search_tools.py

Contains the search and retrieval tools, including the connection to Supabase.

It uses the following environment variables:

SUPABASE_URL
SUPABASE_SERVICE_KEY

The Supabase vector store is configured with:

table_name = "documents"
query_name = "match_gaia_documents"
metadata.jsonl

Contains GAIA-style question-answer examples used to build the retrieval component in Supabase.

For public GitHub usage, this file should be handled carefully because it may contain benchmark examples and answers. A sample or sanitized version can be used instead if needed.

system_prompt.txt

Contains the system prompt used by the agent during the Hugging Face course evaluation.

---

## Environment Variables

The original project requires secret keys to connect external services.

Example .env structure:

SUPABASE_URL=your_supabase_url
SUPABASE_SERVICE_KEY=your_supabase_service_key
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key

These keys are not included in this repository.

Because the original evaluation was connected to the Hugging Face course API, this GitHub version is mainly intended for documentation, reproducibility, and portfolio purposes. The agent will not run end-to-end unless the required API keys, Supabase database, and external service connections are configured again.

---

## Evaluation Result

This agent was evaluated in the final unit of the Hugging Face AI Agents Course using a subset of 20 GAIA Level 1 questions.

Result:

17 / 20 correct answers
85% accuracy on the course evaluation subset

The course required a minimum score of 30% to pass the final project.

---

## Limitations

This repository is a portfolio version of the original project.

Some components depend on external services and private credentials, including Supabase, Groq, Tavily, and the original Hugging Face course API. Therefore, the project is not expected to run out-of-the-box after cloning unless those services are configured.

The retrieval component is also based on similar GAIA-style examples rather than a general-purpose document knowledge base.

---

## Acknowledgments

This project was developed as part of the Hugging Face AI Agents Course, specifically the final hands-on unit focused on building and evaluating an agent using a subset of the GAIA benchmark. (https://huggingface.co/learn/agents-course/)

GAIA is a benchmark designed to evaluate general AI assistants on tasks involving reasoning, tool use, web browsing, multimodal understanding, and concise factual answer generation. (Read the full paper  https://huggingface.co/papers/2311.12983)

Developed by **Diego Montoya**.

- Hugging Face: https://huggingface.co/tucanco
