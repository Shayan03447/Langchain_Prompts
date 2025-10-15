# Langchain_Prompts

A modular prompt-driven chatbot framework built using LangChain. Define prompt templates, generate dynamic prompts, maintain chat history, and provide a UI for interacting with the system.

---

## 🚀 Features

- Template-based prompt management  
- Chat history saving and retrieval  
- Dynamic prompt generation logic  
- UI interface for prompt testing  
- JSON-based prompt templates  
- Easily extendable for new prompt types or LLM backends  

---

## 🧩 Architecture / Components

| File | Responsibility |
|------|----------------|
| `chatbot.py` | Main chatbot logic (sending user prompts, receiving responses) |
| `prompts_generator.py` | Logic to dynamically build or modify prompts based on context |
| `chat_prompt_template.py` | Predefined prompt templates and structures |
| `prompts_ui.py` | Interface or CLI / web UI to test prompt interactions |
| `message_placeholder.py` | Functions to fill in placeholders or variables in prompt templates |
| `messages.py` | Data models or helper functions dealing with message structure |
| `template.json` | JSON file storing prompt templates or schema templates |
| `chat_history.txt` | Plain text log / history of past conversations / prompts |
| `Requirements.txt` | Dependency list to run the project |
| `.gitignore` | Files / folders to ignore in version control |
| `LICENSE` | Project licensing information |

---

## 🛠️ Installation & Setup

1. Clone this repository  
   ```bash
   git clone https://github.com/Shayan03447/Langchain_Prompts.git
   cd Langchain_Prompts
