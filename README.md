# Adaptive AI Tutor - Personalized Learning Agent with Multimodal Capabilities

## Concept

A personalized AI tutor that builds, guides, and continuously adapts a learning roadmap for any topic - powered by autonomous, multimodal AI agents with voice, video, and image interaction capabilities.
It doesn't just teach - it learns how you learn, dynamically adjusting its methods, pace, and content format to optimize understanding through multiple modalities.

This is an MVP implementation that creates adaptive learning experiences through intelligent assessment, dynamic content generation, and multimedia learning support.

## Why this is different

- Truly multimodal: teaches and evaluates using any medium - not just text.
- Autonomous & adaptive: it continually learns from user performance and feedback.
- Scalable & general-purpose: can be applied to any topic - from art history to quantum computing.
- Personal mentor experience: blends reasoning, generative content, and dynamic pacing like a real human tutor.

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

- **Full Multimodal Learning**: Complete voice, video, text, and image support for comprehensive learning
- **Real-time Voice Interaction**: Natural conversation through Gemini Live API with audio streaming
- **Video Communication**: Webcam and screen sharing capabilities for visual learning and demonstrations
- **Adaptive Assessment**: Various evaluation methods including voice responses, image analysis, and multimedia quizzes
- **Real-time Adaptation**: Dynamic roadmap adjustment based on multimodal feedback and performance
- **Personalized Content**: Generated based on learning style and level across all modalities
- **Progress Tracking**: Analytics and performance monitoring with feedback collection
- **Live Audio Processing**: Real-time audio input/output with volume monitoring and transcription
- **Visual Learning Support**: Image generation, analysis, and visual concept explanations
- **Autonomous & Adaptive**: Continuously learns from user performance and feedback across all modalities
- **Scalable & General-purpose**: Can be applied to any topic - from art history to quantum computing
- **Personal Mentor Experience**: Blends reasoning, generative content, and dynamic pacing like a real human tutor

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
   - Node.js 18+ (for frontend)
   - Google Cloud Project with Vertex AI enabled

2. **Installation**

   ```bash
   git clone <your-repo>
   cd gcp-ai-hackathon-2025
   make install
   ```

3. **Configuration**
   ```bash
   export GOOGLE_GENAI_USE_VERTEXAI=true
   export GOOGLE_CLOUD_PROJECT=<your-project-id>
   export GOOGLE_CLOUD_LOCATION=<your-location>
   ```

## Running the Agent

```bash
# Remote Agent with full multimodal interface (voice, video, text, images)
make playground-remote

# Local development with full multimodal interface (voice, video, text, images)
make playground

# Local backend only
make local-backend

# Deploy to Google Cloud
make backend
```

### Deployed Agent Engine Endpoints

If you've deployed the agent to Vertex AI Agent Engine, you can use these endpoints:

- **Query (HTTP)**: `https://us-central1-aiplatform.googleapis.com/v1/projects/qwiklabs-gcp-02-db768a07ab84/locations/us-central1/reasoningEngines/4797024096451821568:query`
- **Streaming (SSE)**: `https://us-central1-aiplatform.googleapis.com/v1/projects/qwiklabs-gcp-02-db768a07ab84/locations/us-central1/reasoningEngines/4797024096451821568:streamQuery?alt=sse`
- **Console (Metrics & Logs)**: `https://console.cloud.google.com/vertex-ai/agents/locations/us-central1/agent-engines/4797024096451821568/metrics?authuser=2&project=qwiklabs-gcp-02-db768a07ab84`

Use these in your client or tooling to send requests to the deployed agent.

### Multimodal Interface Features

The playground interface provides:

- **Voice Input/Output**: Real-time audio streaming with the AI tutor
- **Webcam Support**: Enable your camera for visual demonstrations and explanations
- **Screen Sharing**: Share your screen for collaborative problem-solving
- **Text Chat**: Traditional text-based interaction as backup
- **Image Analysis**: Upload or generate images for visual learning
- **Real-time Transcription**: See live transcription of voice conversations
- **Audio Visualization**: Visual feedback showing when the AI is speaking
- **Feedback System**: Rate and provide feedback on learning sessions

## Example Interaction

### Voice Interaction

```
User: [Speaking] "I want to learn machine learning"

Agent: [Speaking] "Great! Let me understand your background first. What's your current experience with programming and mathematics?"

User: [Speaking] "I have some Python experience and basic calculus knowledge"

Agent: [Speaking] "Perfect! Let me research the latest in machine learning education and create a personalized roadmap for you..."

[Agent performs Google Search and creates initial roadmap]

Agent: [Speaking] "Based on your intermediate programming background, here's your personalized ML learning path:
- Week 1-2: Python for Data Science fundamentals
- Week 3-4: Linear Algebra and Statistics review
- Week 5-8: Supervised Learning algorithms
- Week 9-12: Deep Learning basics

I'll create some visual materials to help you understand these concepts better..."

[Agent generates educational images and videos]

Agent: [Speaking] "Now let's test your understanding. I'll show you a diagram - can you explain what this represents?"

[Shows generated diagram on screen]

User: [Speaking] "This shows a neural network with input, hidden, and output layers..."

Agent: [Speaking] "Excellent! Based on your response, I can see you're grasping the concepts well. Let me adjust your roadmap to move faster through the basics and add some advanced topics..."
```

### Video Interaction

```
User: [Enables webcam] "Can you see my whiteboard? I want to explain my understanding of gradient descent."

Agent: [Speaking] "Yes, I can see your whiteboard! Please go ahead and explain gradient descent using your diagram."

User: [Points to diagram on whiteboard] "So here's the cost function, and gradient descent moves us down this slope..."

Agent: [Speaking] "Perfect! I can see you've drawn the cost function correctly. Your explanation shows you understand the concept well. Let me generate a more detailed visualization to reinforce your learning..."

[Agent generates enhanced educational image]

Agent: [Speaking] "Now let's test this with a practical example. Can you solve this optimization problem using what you've learned?"
```

## Customization

The agent can be customized for different subjects by:

- Modifying the assessment questions
- Updating the research keywords
- Adjusting the roadmap templates
- Customizing the content generation prompts
- Adapting the evaluation criteria

## Technical Architecture

### Multimodal Processing Pipeline

The AI Tutor uses a sophisticated multimodal processing pipeline:

1. **Audio Processing**: Real-time audio streaming with PCM encoding (16kHz) for voice interaction
2. **Video Processing**: WebRTC-based video streaming with JPEG compression for visual communication
3. **Text Processing**: Natural language understanding and generation for conversational learning
4. **Image Processing**: Visual content analysis and generation for educational materials

### Technology Stack

- **Backend**: Python with FastAPI and WebSocket support
- **Frontend**: React with TypeScript for responsive multimodal interface
- **AI Model**: Gemini Live 2.5 Flash Preview with native audio support
- **Real-time Communication**: WebSocket connections for low-latency multimodal streaming
- **Cloud Platform**: Google Cloud Platform with Vertex AI Agent Engine

## Future Enhancements

- Integration with learning management systems (LMS)
- Collaborative learning features with multiple students
- Advanced analytics and reporting dashboard
- Integration with external educational resources and APIs
- Mobile app support for on-the-go learning
- Offline mode for areas with limited connectivity
