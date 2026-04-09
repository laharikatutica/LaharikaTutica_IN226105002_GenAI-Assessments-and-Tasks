# GenAI Task-1 – Prompt Templates using LangChain

## Objective
Build **dynamic and reusable prompt systems** using **LangChain**. Replace hardcoded prompts with reusable templates, multi-input systems, chat-based prompts, validation layers, and a full prompt generator pipeline.

---

## Tools & Technologies
- Python  
- LangChain  
- Jupyter Notebook / Google Colab  

---

## Task Overview & Outputs

### Task 1: Replace Hardcoded Prompts
- Converted a hardcoded prompt into a reusable **PromptTemplate**.  
- **Example Output:**  
  - Input: `Machine Learning` → Output: `Explain Machine Learning in simple terms for beginners`  

### Task 2: Multi-Input Prompt System
- Template accepts **topic, audience, and tone**.  
- **Example Outputs:**  
  - `AI | beginners | friendly` → `Explain AI for beginners in a friendly tone`  
  - `Python | kids | fun` → `Explain Python for kids in a fun tone`  
  - `Deep Learning | engineers | technical` → `Explain Deep Learning for engineers in a technical tone`  

### Task 3: Prompt Variations Engine
- Three variations: **Teaching, Interview, Storytelling**.  
- **Example Outputs (topic = Machine Learning):**  
  - Teaching: `Explain Machine Learning clearly step by step`  
  - Interview: `Ask 3 questions about Machine Learning`  
  - Storytelling: `Explain Machine Learning as a story`  

### Task 4: ChatPromptTemplate System
- Role-based chat prompts for **Teacher, Interviewer, Motivator**.  
- **Example Outputs:**  
  - Teacher & Neural Networks →  
    ```
    SYSTEM: You are an expert teacher. Explain concepts clearly with examples and step-by-step guidance.
    HUMAN: Explain Neural Networks to me as a student would understand.
    ```  
  - Interviewer & Deep Learning →  
    ```
    SYSTEM: You are a professional interviewer. Ask insightful, thought-provoking questions about the topic.
    HUMAN: Ask me insightful questions about Deep Learning.
    ```  

### Task 5: Input Validation Layer
- Validates **audience** and **tone**. Invalid inputs are corrected to defaults or trigger an error.  
- **Example Output:**  
  - Input: `child, dramatic` → Warnings, defaults applied → `audience=beginner, tone=casual`  

### Task 6: Prompt Generator App
- Combines **validation** and **templates** for dynamic prompt generation.  
- **Example Outputs:**  
  - `Neural Networks | beginner | fun | storytelling` → `Explain Neural Networks for beginner in a fun storytelling style`  
  - `Python | expert | formal | interview` → `Ask 3 questions about Python for expert in a formal tone`  

### Task 7: Template Reusability Test
- Single master template reused for multiple input combinations.  
- **Example Outputs:**  
  - `Machine Learning | beginner | fun | teacher` → `You are a teacher. Explain Machine Learning to a beginner-level learner in a fun tone.`  
  - `Deep Learning | intermediate | casual | motivator` → `You are a motivator. Explain Deep Learning to a intermediate-level learner in a casual tone.`  

---

## Pipeline Workflow
User Input → Validation → Prompt Template → Dynamic Prompt Generation → Output

**Example Full Pipeline Output:**  
- Step 1: `User Input` → `topic=Artificial Intelligence, audience=beginner, tone=fun, style=storytelling`
- Step 2: `Validation` → `audience=beginner, tone=fun`
- Step 3: `Template` → `Style 'storytelling' template selected and formatted`
- Step 4: `Final Output` → `Explain Artificial Intelligence for beginner in a fun storytelling style`
