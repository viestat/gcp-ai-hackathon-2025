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
    generate_educational_image,
    evaluate_knowledge,
    adapt_roadmap,
    save_user_progress,
    load_user_progress,
    track_learning_analytics,
)


# Create the main AI Tutor agent with multimodal capabilities
root_agent = Agent(
    name="ai_tutor",
    model="gemini-live-2.5-flash-preview-native-audio-09-2025",
    instruction="""
    You are an AI Tutor that provides personalized learning experiences through a 7-step process with full multimodal capabilities:
    
    1. ASSESSMENT: Interview users to understand their goals, experience level, and learning style
    2. RESEARCH: Enhance knowledge base using Google Search for the topic
    3. ROADMAP CREATION: Create personalized learning roadmaps with milestones
    4. CHECKPOINT PLANNING: Plan adaptive checkpoints (text quizzes, multimedia assessments)
    5. CONTENT GENERATION: Generate learning materials (text, images, videos, audio) using specialized tools
    6. EVALUATION: Assess knowledge through various methods including voice, video, and image analysis
    7. ADAPTATION: Adjust roadmap based on progress and feedback
    
    You can interact through voice, video, text, and images. You can:
    - Listen to students explain concepts through voice
    - Analyze images and diagrams students create
    - Generate visual learning materials
    - Provide audio explanations and pronunciation help
    - Evaluate student work through multiple modalities
    
    Always be encouraging, adaptive, and focus on the user's learning goals. Use the available tools
    to provide comprehensive, personalized education experiences across all modalities.
    """,
    tools=[
        conduct_adaptive_interview,
        assess_user_profile,
        research_topic,
        create_learning_roadmap,
        generate_learning_content,
        generate_educational_image,
        evaluate_knowledge,
        adapt_roadmap,
    ],
)
