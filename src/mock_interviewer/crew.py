"""Main Crew orchestration for the Mock Interviewer system."""

from crewai import Crew, Process
from typing import Optional

from .agents import (
    create_interviewer_agent,
    create_evaluator_agent,
    create_feedback_agent,
)
from .tasks import (
    create_interview_task,
    create_evaluation_task,
    create_feedback_task,
)


class MockInterviewerCrew:
    """
    Multi-Agent Mock Interviewer using CrewAI.
    
    This crew simulates a complete interview process with three specialized agents:
    1. Interviewer - Conducts the mock interview
    2. Evaluator - Assesses the interview performance
    3. Feedback Specialist - Provides actionable improvement suggestions
    """
    
    def __init__(self, llm=None):
        """
        Initialize the Mock Interviewer Crew.
        
        Args:
            llm: Optional language model to use. If None, uses default from env.
        """
        self.llm = llm
        self._interviewer = None
        self._evaluator = None
        self._feedback_agent = None
    
    @property
    def interviewer(self):
        """Get or create the interviewer agent."""
        if self._interviewer is None:
            self._interviewer = create_interviewer_agent(self.llm)
        return self._interviewer
    
    @property
    def evaluator(self):
        """Get or create the evaluator agent."""
        if self._evaluator is None:
            self._evaluator = create_evaluator_agent(self.llm)
        return self._evaluator
    
    @property
    def feedback_agent(self):
        """Get or create the feedback agent."""
        if self._feedback_agent is None:
            self._feedback_agent = create_feedback_agent(self.llm)
        return self._feedback_agent
    
    def run(
        self,
        job_role: str,
        candidate_background: str,
        focus_areas: Optional[str] = None,
    ) -> str:
        """
        Run a complete mock interview session.
        
        Args:
            job_role: The target job role (e.g., "Senior Software Engineer")
            candidate_background: Summary of candidate's experience and skills
            focus_areas: Optional specific areas to focus on
            
        Returns:
            Complete interview report with questions, evaluation, and feedback
        """
        if focus_areas is None:
            focus_areas = "General technical and behavioral assessment"
        
        # Create tasks
        interview_task = create_interview_task(
            interviewer=self.interviewer,
            job_role=job_role,
            candidate_background=candidate_background,
            focus_areas=focus_areas,
        )
        
        evaluation_task = create_evaluation_task(
            evaluator=self.evaluator,
            interview_task=interview_task,
            job_role=job_role,
        )
        
        feedback_task = create_feedback_task(
            feedback_agent=self.feedback_agent,
            interview_task=interview_task,
            evaluation_task=evaluation_task,
            candidate_background=candidate_background,
        )
        
        # Create and run the crew
        crew = Crew(
            agents=[self.interviewer, self.evaluator, self.feedback_agent],
            tasks=[interview_task, evaluation_task, feedback_task],
            process=Process.sequential,
            verbose=True,
        )
        
        result = crew.kickoff()
        return str(result)
    
    def run_quick_interview(
        self,
        job_role: str,
        years_experience: int,
        key_skills: list[str],
    ) -> str:
        """
        Run a quick mock interview with minimal input.
        
        Args:
            job_role: The target job role
            years_experience: Years of relevant experience
            key_skills: List of key technical skills
            
        Returns:
            Complete interview report
        """
        candidate_background = f"""
- {years_experience} years of experience in software development
- Key skills: {', '.join(key_skills)}
- Looking for a {job_role} position
- Previous experience in similar roles
"""
        
        return self.run(
            job_role=job_role,
            candidate_background=candidate_background,
            focus_areas=f"Technical skills: {', '.join(key_skills[:3])}; Leadership and problem-solving",
        )
