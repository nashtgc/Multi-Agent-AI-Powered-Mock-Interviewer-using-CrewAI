# Multi-Agent AI-Powered Mock Interviewer using CrewAI

A sophisticated mock interview system powered by multiple AI agents using the [CrewAI](https://github.com/joaomdmoura/crewAI) framework. This project simulates a realistic interview experience with specialized agents for interviewing, evaluation, and feedback.

## 🎯 Overview

This system uses three specialized AI agents that work together to provide a comprehensive mock interview experience:

1. **Technical Interviewer Agent** - Conducts the interview with relevant technical and behavioral questions
2. **Interview Evaluator Agent** - Assesses responses based on multiple criteria
3. **Career Coach Agent** - Provides actionable feedback and improvement suggestions

## ✨ Features

- **Realistic Interview Simulation** - Experience a full interview with introductions, technical questions, behavioral questions, and closing
- **Comprehensive Evaluation** - Get scored on technical competency, communication skills, behavioral competencies, and cultural fit
- **Actionable Feedback** - Receive detailed feedback with specific improvement suggestions and a 30-day action plan
- **Customizable Focus Areas** - Target specific skills or topics during the interview
- **Role-Specific Questions** - Tailored questions based on the job role and candidate background

## 📋 Prerequisites

- Python 3.10 or higher
- OpenAI API key

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nashtgc/Multi-Agent-AI-Powered-Mock-Interviewer-using-CrewAI.git
   cd Multi-Agent-AI-Powered-Mock-Interviewer-using-CrewAI
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

## 💻 Usage

### Command Line

Run the default mock interview:
```bash
python main.py
```

### As a Library

```python
from src.mock_interviewer import MockInterviewerCrew

# Create the crew
crew = MockInterviewerCrew()

# Run a full interview
result = crew.run(
    job_role="Senior Software Engineer",
    candidate_background="""
    - 5 years of experience in software development
    - Proficient in Python and JavaScript
    - Experience with cloud services
    """,
    focus_areas="System design, Python best practices, Leadership"
)

print(result)
```

### Quick Interview

For a simplified interview setup:
```python
result = crew.run_quick_interview(
    job_role="Backend Developer",
    years_experience=3,
    key_skills=["Python", "Django", "PostgreSQL", "Docker"]
)
```

## 🏗️ Project Structure

```
├── main.py                      # Entry point for running interviews
├── requirements.txt             # Python dependencies
├── .env.example                 # Example environment configuration
├── README.md                    # This file
└── src/
    └── mock_interviewer/
        ├── __init__.py          # Package initialization
        ├── agents.py            # AI agent definitions
        ├── tasks.py             # Task definitions for agents
        └── crew.py              # Crew orchestration
```

## 🤖 Agents

### Technical Interviewer
- Conducts professional mock interviews
- Asks relevant technical and behavioral questions
- Provides sample strong answers for reference
- Uses follow-up questions to dig deeper

### Interview Evaluator
- Evaluates responses on a 1-10 scale
- Assesses technical competency (30%)
- Evaluates communication skills (25%)
- Measures behavioral competencies (25%)
- Gauges cultural fit & professionalism (20%)

### Career Coach
- Synthesizes interview performance
- Highlights key strengths to leverage
- Identifies areas for improvement
- Provides a 30-day improvement plan
- Suggests specific resources and practice exercises

## 📊 Sample Output

The system generates a comprehensive report including:

1. **Interview Transcript** - Complete mock interview with questions and ideal answers
2. **Evaluation Report** - Detailed scoring with specific observations
3. **Feedback Report** - Actionable improvement suggestions with timeline

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Required |
| `OPENAI_MODEL_NAME` | Model to use | `gpt-4o-mini` |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) - The multi-agent framework
- [LangChain](https://langchain.com/) - The underlying LLM framework
