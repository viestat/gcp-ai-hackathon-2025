"""
AI Tutor MVP - Main Coordinator Agent

This agent orchestrates the 7-step learning flow for personalized education.
Combines patterns from multiple ADK samples for comprehensive tutoring.
"""

from google.adk.agents import Agent
from .tools import (
    conduct_adaptive_interview,
    assess_user_profile,
    research_topic,
    create_learning_roadmap,
    generate_learning_content,
    evaluate_knowledge,
    adapt_roadmap,
    save_user_progress,
    load_user_progress,
    track_learning_analytics,
)


# Create the main AI Tutor agent
root_agent = Agent(
    name="ai_tutor",
    model="gemini-2.5-flash",
    instruction="""
    You are an AI Tutor that provides personalized learning experiences through a 7-step process:
    
    1. ASSESSMENT: Interview users to understand their goals, experience level, and learning style
    2. RESEARCH: Enhance knowledge base using Google Search for the topic
    3. ROADMAP CREATION: Create personalized learning roadmaps with milestones
    4. CHECKPOINT PLANNING: Plan adaptive checkpoints (text quizzes, multimedia assessments)
    5. CONTENT GENERATION: Generate learning materials (text, images, videos, audio)
    6. EVALUATION: Assess knowledge through various methods
    7. ADAPTATION: Adjust roadmap based on progress and feedback
    
    Always be encouraging, adaptive, and focus on the user's learning goals. Use the available tools
    to provide comprehensive, personalized education experiences.
    """,
    tools=[
        conduct_adaptive_interview,
        assess_user_profile,
        research_topic,
        create_learning_roadmap,
        generate_learning_content,
        evaluate_knowledge,
        adapt_roadmap,
    ],
)
