# Adaptive AI Tutor - Personalized Learning Agent

## Concept

A personalized AI tutor that builds, guides, and continuously adapts a learning roadmap for any topic - powered by autonomous, multimodal AI agents.
It doesn't just teach - it learns how you learn, dynamically adjusting its methods, pace, and content format to optimize understanding.

This is an MVP implementation that creates adaptive learning experiences through intelligent assessment, dynamic content generation, and multimedia learning support.

---

## Agent Architecture

The AI Tutor uses a multi-agent system with the following components:

- **Main Coordinator Agent** - Orchestrates the learning flow
- **Assessment Agent** - Handles interviews and level determination
- **Research Agent** - Enhances knowledge via Google Search
- **Roadmap Agent** - Creates and adapts learning paths
- **Content Generation Agent** - Creates multimedia learning materials
- **Evaluation Agent** - Handles quizzes and assessments
- **Adaptation Agent** - Adjusts roadmap based on feedback

---

## Core Learning Flow

1. **User Profiling (AI Interview)**

   - The agent starts by interviewing the learner to understand goals, interests, and experience level (beginner → expert).
   - It builds a learning profile that defines tone, difficulty, and preferred learning style (visual, auditory, text-based, etc.).

2. **Knowledge Enhancement**

   - The agent performs a live web search to enrich its context about the chosen topic.
   - It filters, summarizes, and curates relevant information - building a foundation of up-to-date domain knowledge.

3. **Initial Roadmap Creation**

   - Creates a personalized learning roadmap, divided into stages or milestones (modules, checkpoints, and goals).
   - Each step includes tailored material and adaptive evaluation points.

4. **Dynamic Checkpoint Planning**

   - Based on interaction and progress, the agent injects adaptive checkpoints, including:
   - Text-based quizzes
   - Multimedia quizzes (images, sounds, or short clips, e.g., identifying visuals like nano banana)
   - Mini-projects or open-ended challenges

5. **Learning Material Generation**

   - The tutor can generate teaching content in multiple formats:
   - Images for visual concepts
   - Audio for pronunciation, sound design, or auditory learners
   - Video for dynamic demonstrations
   - Text for explanations, summaries, and references

6. **Multimedia Knowledge Evaluation**

   - The agent can receive and analyze user-submitted content - text, images, audio, or video - to assess comprehension and creativity.
   - Example: a student explaining a concept via a short audio, or uploading an image of a handwritten diagram.

7. **Roadmap Adaptation**
   - Based on the user's performance and engagement, the system updates the roadmap in real time - reordering lessons, generating new examples, or switching modalities to better fit the learner's progress.

---

## Key Features

- **Multimedia Learning**: Text, images, audio, and video support
- **Adaptive Assessment**: Various evaluation methods (quizzes, multimedia)
- **Real-time Adaptation**: Dynamic roadmap adjustment
- **Personalized Content**: Generated based on learning style and level
- **Progress Tracking**: Analytics and performance monitoring
- **Truly multimodal**: teaches and evaluates using any medium - not just text
- **Autonomous & adaptive**: it continually learns from user performance and feedback
- **Scalable & general-purpose**: can be applied to any topic - from art history to quantum computing
- **Personal mentor experience**: blends reasoning, generative content, and dynamic pacing like a real human tutor

---

## Sample Integration

This MVP combines patterns from:

- `customer-service` - Interviewing and personalization
- `academic-research` - Google Search integration
- `financial-advisor` - Multi-agent orchestration
- `image-scoring` - Multimedia content generation
- `short-movie-agents` - Video content creation
- `personalized-shopping` - Recommendation adaptation
- `data-science` - Analytics and progress tracking

---

## Setup and Installation

1. **Prerequisites**

   - Python 3.10+
   - uv for dependency management
   - Google Cloud Project with Vertex AI enabled

2. **Installation**

   ```bash
   git clone https://github.com/google/adk-samples.git
   cd adk-samples/python/agents/ai-tutor-mvp
   uv sync
   ```

3. **Configuration**
   ```bash
   export GOOGLE_GENAI_USE_VERTEXAI=true
   export GOOGLE_CLOUD_PROJECT=<your-project-id>
   export GOOGLE_CLOUD_LOCATION=<your-location>
   ```

## Running the Agent

```bash
# CLI mode
adk run ai_tutor

# Web interface
adk web
```

## Example Interaction

```
User: "I want to learn machine learning"

Agent: "Great! Let me understand your background first. What's your current experience with programming and mathematics?"

User: "I have some Python experience and basic calculus knowledge"

Agent: "Perfect! Let me research the latest in machine learning education and create a personalized roadmap for you..."

[Agent performs Google Search and creates initial roadmap]

Agent: "Based on your intermediate programming background, here's your personalized ML learning path:
- Week 1-2: Python for Data Science fundamentals
- Week 3-4: Linear Algebra and Statistics review
- Week 5-8: Supervised Learning algorithms
- Week 9-12: Deep Learning basics

I'll create some visual materials to help you understand these concepts better..."

[Agent generates educational images and videos]

Agent: "Now let's test your understanding. I'll show you a diagram - can you explain what this represents?"

[Shows generated diagram]

User: [Provides explanation]

Agent: "Excellent! Based on your response, I can see you're grasping the concepts well. Let me adjust your roadmap to move faster through the basics and add some advanced topics..."
```

## Customization

The agent can be customized for different subjects by:

- Modifying the assessment questions
- Updating the research keywords
- Adjusting the roadmap templates
- Customizing the content generation prompts
- Adapting the evaluation criteria

## Future Enhancements

- Integration with learning management systems
- Collaborative learning features
- Advanced analytics and reporting
- Integration with external educational resources
- Voice interaction capabilities
