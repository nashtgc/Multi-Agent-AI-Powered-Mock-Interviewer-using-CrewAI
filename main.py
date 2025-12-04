#!/usr/bin/env python3
"""
Multi-Agent AI-Powered Mock Interviewer using CrewAI

This script provides a command-line interface for running mock interviews.
"""

import os
import sys
from dotenv import load_dotenv

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from mock_interviewer import MockInterviewerCrew


def main():
    """Run the mock interviewer."""
    # Load environment variables
    load_dotenv()
    
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is not set.")
        print("Please copy .env.example to .env and add your API key.")
        sys.exit(1)
    
    # Example usage
    print("=" * 60)
    print("Multi-Agent AI-Powered Mock Interviewer using CrewAI")
    print("=" * 60)
    print()
    
    # Create the mock interviewer crew
    crew = MockInterviewerCrew()
    
    # Example interview parameters
    job_role = "Senior Software Engineer"
    
    candidate_background = """
    - 5 years of experience in software development
    - Proficient in Python, JavaScript, and TypeScript
    - Experience with React, Node.js, and Django
    - Background in cloud services (AWS, GCP)
    - Led a team of 3 developers on a critical project
    - Strong experience with CI/CD and DevOps practices
    - Computer Science degree from State University
    """
    
    focus_areas = """
    - System design and architecture
    - Python best practices and advanced concepts
    - Leadership and team collaboration
    - Problem-solving and debugging skills
    """
    
    print(f"Starting mock interview for: {job_role}")
    print("-" * 60)
    
    # Run the interview
    result = crew.run(
        job_role=job_role,
        candidate_background=candidate_background,
        focus_areas=focus_areas,
    )
    
    print("\n" + "=" * 60)
    print("INTERVIEW SESSION COMPLETE")
    print("=" * 60)
    print(result)


if __name__ == "__main__":
    main()
