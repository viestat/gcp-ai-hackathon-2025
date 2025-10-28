"""
Enhanced Image Generation Tool for AI Tutor

Uses Imagen 3 to generate educational images.
Based on the image-scoring and marketing-agency agents from adk-samples.
"""

import os
import logging
from datetime import datetime
from typing import Dict, Any, Optional
from google import genai
from google.genai import types
from google.adk.tools import ToolContext

# Initialize global client like image-scoring
client = genai.Client(
    vertexai=True, project=os.environ.get("GOOGLE_CLOUD_PROJECT"), location="global"
)


async def generate_educational_image(
    topic: str,
    level: str,
    learning_style: str,
    tool_context: ToolContext,
    specific_concept: Optional[str] = None,
) -> dict:
    """
    Generate educational images using Imagen 3.

    Args:
        topic: The learning topic
        level: Content difficulty level
        learning_style: User's preferred learning style
        specific_concept: Specific concept to illustrate
        tool_context: ADK tool context

    Returns:
        dict: Generated image with metadata
    """
    try:
        # Create detailed prompt
        prompt = _create_detailed_image_prompt(
            topic, level, learning_style, specific_concept
        )

        # Generate image using Imagen 3
        return await _generate_image_with_imagen(prompt, tool_context)

    except Exception as e:
        return {
            "status": "error",
            "message": f"Image generation failed: {str(e)}",
        }


def _create_detailed_image_prompt(
    topic: str, level: str, learning_style: str, specific_concept: Optional[str] = None
) -> str:
    """Create a detailed prompt for image generation."""

    # Level-specific descriptions
    level_descriptions = {
        "beginner": {
            "complexity": "simple and easy to understand",
            "detail": "basic concepts with clear labels",
            "style": "clean, minimal design with large text",
        },
        "intermediate": {
            "complexity": "moderately detailed",
            "detail": "comprehensive concepts with explanations",
            "style": "professional and informative",
        },
        "advanced": {
            "complexity": "complex and comprehensive",
            "detail": "detailed technical information",
            "style": "sophisticated and technical",
        },
    }

    # Learning style adaptations
    style_adaptations = {
        "visual": "Include diagrams, charts, flowcharts, and visual representations with clear visual hierarchy",
        "auditory": "Add text annotations, labels, and explanatory text boxes",
        "hands-on": "Show step-by-step processes, examples, and practical applications with numbered steps",
        "theoretical": "Include mathematical formulas, abstract concepts, and theoretical frameworks",
    }

    level_info = level_descriptions.get(level, level_descriptions["beginner"])
    style_info = style_adaptations.get(learning_style, style_adaptations["visual"])

    concept_part = f" focusing on {specific_concept}" if specific_concept else ""

    prompt = f"""Create an educational illustration about {topic}{concept_part} that is {level_info['complexity']} and designed for {learning_style} learners.

Visual Requirements:
- {style_info}
- {level_info['detail']}
- {level_info['style']}
- Professional educational quality
- Clear, readable text and labels
- High contrast colors for readability
- Visually appealing and engaging
- Suitable for learning purposes

The image should help students understand {topic} concepts at the {level} level through {learning_style} learning methods. Make it educational and informative."""

    return prompt


async def _generate_image_with_imagen(
    prompt: str, tool_context: ToolContext
) -> Dict[str, Any]:
    """Generate an image using Imagen 3."""
    try:
        # Generate image using Imagen 3 (using global client)
        response = client.models.generate_images(
            model="imagen-3.0-generate-002",
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="9:16",  # Match image-scoring pattern
                safety_filter_level="block_low_and_above",
                person_generation="allow_adult",
            ),
        )

        if response.generated_images is not None and len(response.generated_images) > 0:
            # Get the image bytes
            image_bytes = response.generated_images[0].image.image_bytes

            # Create artifact name with counter like image-scoring
            counter = str(tool_context.state.get("loop_iteration", 0))
            artifact_name = f"educational_image_{counter}.png"

            # Save as ADK artifact (this is what the frontend can display)
            report_artifact = types.Part.from_bytes(
                data=image_bytes, mime_type="image/png"
            )

            await tool_context.save_artifact(artifact_name, report_artifact)
            logging.info(f"Image saved: {artifact_name}")

            return {
                "status": "success",
                "message": f"Image generated. ADK artifact: {artifact_name}.",
                "artifact_name": artifact_name,
            }
        else:
            # Match image-scoring error handling
            error_details = str(response)
            logging.warning("No images generated")
            return {
                "status": "error",
                "message": f"No images generated. Response: {error_details}",
            }

    except Exception as e:
        return {"status": "error", "message": f"No images generated. {e}"}
