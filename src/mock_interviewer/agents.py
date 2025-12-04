"""Agent definitions for the Mock Interviewer system."""

from crewai import Agent


def create_interviewer_agent(llm=None) -> Agent:
    """
    Create the Interviewer Agent responsible for conducting the interview.
    
    This agent asks technical and behavioral questions, follows up on responses,
    and maintains a professional interview atmosphere.
    """
    return Agent(
        role="Technical Interviewer",
        goal="Conduct a thorough and professional mock interview by asking relevant "
             "technical and behavioral questions based on the candidate's background "
             "and the target job role",
        backstory="You are an experienced technical interviewer with 15+ years in the "
                  "tech industry. You have conducted thousands of interviews for top "
                  "tech companies. You are known for asking insightful questions that "
                  "reveal a candidate's true abilities. You are fair, professional, "
                  "and create a comfortable environment for candidates to showcase "
                  "their skills.",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )


def create_evaluator_agent(llm=None) -> Agent:
    """
    Create the Evaluator Agent responsible for assessing candidate responses.
    
    This agent analyzes responses for technical accuracy, communication skills,
    problem-solving approach, and overall interview performance.
    """
    return Agent(
        role="Interview Evaluator",
        goal="Evaluate the candidate's responses objectively, assessing technical "
             "knowledge, communication skills, problem-solving abilities, and "
             "cultural fit based on industry best practices",
        backstory="You are a senior hiring manager with extensive experience in "
                  "evaluating technical talent. You have a keen eye for identifying "
                  "strong candidates and understanding their potential. You believe "
                  "in providing constructive, actionable feedback that helps "
                  "candidates improve. You evaluate based on technical accuracy, "
                  "communication clarity, logical reasoning, and professionalism.",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )


def create_feedback_agent(llm=None) -> Agent:
    """
    Create the Feedback Agent responsible for providing comprehensive feedback.
    
    This agent synthesizes the interview and evaluation to provide actionable
    improvement suggestions and overall assessment.
    """
    return Agent(
        role="Career Coach & Feedback Specialist",
        goal="Provide comprehensive, constructive feedback to help the candidate "
             "improve their interview skills, technical knowledge, and overall "
             "presentation for future interviews",
        backstory="You are a seasoned career coach specializing in tech industry "
                  "interview preparation. You have helped thousands of candidates "
                  "land their dream jobs at top companies. You believe in honest, "
                  "supportive feedback that empowers candidates. You focus on "
                  "actionable advice, highlighting both strengths and areas for "
                  "improvement with specific suggestions.",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )
