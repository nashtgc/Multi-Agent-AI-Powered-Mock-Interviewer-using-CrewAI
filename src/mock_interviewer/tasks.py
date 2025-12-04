"""Task definitions for the Mock Interviewer system."""

from crewai import Task, Agent


def create_interview_task(
    interviewer: Agent,
    job_role: str,
    candidate_background: str,
    focus_areas: str,
) -> Task:
    """
    Create the interview task for the interviewer agent.
    
    Args:
        interviewer: The interviewer agent
        job_role: The target job role for the interview
        candidate_background: The candidate's background/resume summary
        focus_areas: Specific areas to focus on during the interview
    """
    return Task(
        description=f"""Conduct a comprehensive mock interview for a candidate 
applying for a {job_role} position.

**Candidate Background:**
{candidate_background}

**Focus Areas:**
{focus_areas}

**Your Interview Should Include:**
1. A warm introduction and overview of the interview process
2. 3-4 technical questions relevant to the {job_role} position
3. 2-3 behavioral questions using the STAR method
4. Follow-up questions based on typical responses
5. Time for the "candidate" to ask questions
6. A professional closing

For each question, provide:
- The question itself
- What you're looking for in a strong answer
- A sample strong response a candidate might give
- Follow-up questions you might ask

Make the interview realistic and challenging but fair.""",
        expected_output="""A complete mock interview transcript including:
1. Introduction and rapport building
2. Technical questions with ideal answers and scoring criteria
3. Behavioral questions with STAR-format example answers
4. Follow-up questions and their expected responses
5. Candidate Q&A section
6. Professional closing
Each section should be clearly labeled and formatted.""",
        agent=interviewer,
    )


def create_evaluation_task(
    evaluator: Agent,
    interview_task: Task,
    job_role: str,
) -> Task:
    """
    Create the evaluation task for the evaluator agent.
    
    Args:
        evaluator: The evaluator agent
        interview_task: The completed interview task to evaluate
        job_role: The target job role for context
    """
    return Task(
        description=f"""Evaluate the mock interview for the {job_role} position 
based on the interview conducted.

**Evaluation Criteria:**

1. **Technical Competency (30%)**
   - Accuracy of technical knowledge
   - Depth of understanding
   - Problem-solving approach

2. **Communication Skills (25%)**
   - Clarity of expression
   - Structure and organization
   - Active listening indicators

3. **Behavioral Competencies (25%)**
   - Leadership potential
   - Teamwork and collaboration
   - Adaptability and growth mindset

4. **Cultural Fit & Professionalism (20%)**
   - Alignment with company values
   - Professional demeanor
   - Enthusiasm and motivation

For each criterion, provide:
- A score from 1-10
- Specific observations
- Examples from the interview""",
        expected_output="""A detailed evaluation report containing:
1. Overall score and recommendation (Hire/No Hire/Maybe)
2. Breakdown by each evaluation criterion with scores
3. Key strengths identified (at least 3)
4. Areas of concern (at least 2)
5. Comparison to typical candidates at this level
6. Specific examples from the interview supporting each point""",
        agent=evaluator,
        context=[interview_task],
    )


def create_feedback_task(
    feedback_agent: Agent,
    interview_task: Task,
    evaluation_task: Task,
    candidate_background: str,
) -> Task:
    """
    Create the feedback task for the feedback agent.
    
    Args:
        feedback_agent: The feedback agent
        interview_task: The completed interview task
        evaluation_task: The completed evaluation task
        candidate_background: The candidate's background for personalization
    """
    return Task(
        description=f"""Based on the interview and evaluation, provide comprehensive 
feedback to help the candidate improve.

**Candidate Background:**
{candidate_background}

**Your Feedback Should Cover:**

1. **Executive Summary**
   - Overall performance assessment
   - Key takeaways

2. **Strengths to Leverage**
   - What the candidate did well
   - How to emphasize these in future interviews

3. **Areas for Improvement**
   - Specific gaps identified
   - Actionable steps to address each gap

4. **Technical Preparation**
   - Topics to study
   - Resources to explore
   - Practice problems or projects

5. **Communication Enhancement**
   - Tips for clearer responses
   - STAR method refinement
   - Body language and confidence suggestions

6. **Next Steps**
   - 30-day improvement plan
   - Recommended practice schedule
   - Mock interview suggestions""",
        expected_output="""A comprehensive feedback report that includes:
1. Executive summary with overall assessment
2. Top 3 strengths with examples and how to leverage them
3. Top 3 areas for improvement with specific action items
4. Technical study plan with resources and timeline
5. Communication tips with practice exercises
6. 30-day improvement roadmap with milestones
The feedback should be encouraging, specific, and actionable.""",
        agent=feedback_agent,
        context=[interview_task, evaluation_task],
    )
