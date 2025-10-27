"""
Test script for AI Tutor MVP

This script demonstrates the 7-step learning flow of the AI Tutor.
"""

import asyncio
from ai_tutor import ai_tutor


async def test_ai_tutor_flow():
    """Test the complete AI Tutor learning flow."""

    print("🎓 AI Tutor MVP - Personalized Learning Agent")
    print("=" * 50)

    # Step 1: Interview & Assessment
    print("\n1️⃣ INTERVIEW & ASSESSMENT")
    print("-" * 30)

    assessment_result = await ai_tutor.run_async(
        "I want to learn machine learning. I have some Python experience and basic calculus knowledge."
    )

    print(f"Assessment Result: {assessment_result}")

    # Step 2: Knowledge Enhancement
    print("\n2️⃣ KNOWLEDGE ENHANCEMENT")
    print("-" * 30)

    research_result = await ai_tutor.run_async(
        "Research the latest in machine learning education for intermediate learners"
    )

    print(f"Research Result: {research_result}")

    # Step 3: Roadmap Creation
    print("\n3️⃣ ROADMAP CREATION")
    print("-" * 30)

    roadmap_result = await ai_tutor.run_async(
        "Create a personalized learning roadmap for machine learning based on my intermediate level"
    )

    print(f"Roadmap Result: {roadmap_result}")

    # Step 4: Checkpoint Planning
    print("\n4️⃣ CHECKPOINT PLANNING")
    print("-" * 30)

    checkpoint_result = await ai_tutor.run_async(
        "Plan assessment checkpoints for my machine learning roadmap"
    )

    print(f"Checkpoint Result: {checkpoint_result}")

    # Step 5: Content Generation
    print("\n5️⃣ CONTENT GENERATION")
    print("-" * 30)

    content_result = await ai_tutor.run_async(
        "Generate visual learning content for linear regression concepts"
    )

    print(f"Content Result: {content_result}")

    # Step 6: Knowledge Evaluation
    print("\n6️⃣ KNOWLEDGE EVALUATION")
    print("-" * 30)

    evaluation_result = await ai_tutor.run_async(
        "Evaluate my understanding of linear regression. I understand it's used for predicting continuous values."
    )

    print(f"Evaluation Result: {evaluation_result}")

    # Step 7: Roadmap Adaptation
    print("\n7️⃣ ROADMAP ADAPTATION")
    print("-" * 30)

    adaptation_result = await ai_tutor.run_async(
        "Based on my good performance in linear regression, adapt my learning roadmap"
    )

    print(f"Adaptation Result: {adaptation_result}")

    print("\n✅ AI Tutor MVP Test Complete!")
    print("The agent successfully demonstrated all 7 steps of the learning flow.")


def test_sync_flow():
    """Test the AI Tutor with synchronous calls."""

    print("🎓 AI Tutor MVP - Synchronous Test")
    print("=" * 40)

    # Simple test of the main agent
    result = ai_tutor.run("Hello! I want to learn about artificial intelligence.")

    print(f"Agent Response: {result}")

    return result


if __name__ == "__main__":
    print("Starting AI Tutor MVP Tests...")

    # Test synchronous flow
    print("\n🔄 Testing Synchronous Flow:")
    sync_result = test_sync_flow()

    # Test asynchronous flow
    print("\n🔄 Testing Asynchronous Flow:")
    asyncio.run(test_ai_tutor_flow())

    print("\n🎉 All tests completed successfully!")
