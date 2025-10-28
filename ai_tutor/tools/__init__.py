"""Tools module for the AI Tutor agent."""

# Assessment tools
from .assessment import (
    conduct_adaptive_interview,
    assess_user_profile,
)

# Research tools
from .research import (
    research_topic,
)

# Roadmap tools
from .roadmap import (
    create_learning_roadmap,
    adapt_roadmap,
)

# Content generation tools
from .content import (
    generate_learning_content,
)

# Image generation tools
from .image_generation import (
    generate_educational_image,
)

# Evaluation tools
from .evaluation import (
    evaluate_knowledge,
)

# Persistence tools
from .persistence import (
    save_user_progress,
    load_user_progress,
    track_learning_analytics,
)

__all__ = [
    # Assessment
    "conduct_adaptive_interview",
    "assess_user_profile",
    # Research
    "research_topic",
    # Roadmap
    "create_learning_roadmap",
    "adapt_roadmap",
    # Content
    "generate_learning_content",
    # Image Generation
    "generate_educational_image",
    # Evaluation
    "evaluate_knowledge",
    # Persistence
    "save_user_progress",
    "load_user_progress",
    "track_learning_analytics",
]
