#!/usr/bin/env python3
"""
Test script for image generation tool in isolation.
This tests the image generation without WebSockets or agent engine.
"""

import asyncio
import os
from ai_tutor.tools.image_generation import generate_educational_image


class MockToolContext:
    """Mock tool context for testing."""

    def __init__(self):
        self.state = {"loop_iteration": 0}
        self.artifacts = {}

    async def save_artifact(self, name: str, artifact):
        """Mock save_artifact that saves the image locally to disk."""
        print(f"📁 Mock: Saving artifact '{name}' locally")

        # Extract image bytes from the artifact
        if hasattr(artifact, "inline_data") and artifact.inline_data:
            image_bytes = artifact.inline_data.data
        elif hasattr(artifact, "data"):
            image_bytes = artifact.data
        else:
            print(f"❌ Could not extract image data from artifact")
            return False

        # Save to local file
        import base64

        try:
            # Decode base64 if needed
            if isinstance(image_bytes, str):
                image_data = base64.b64decode(image_bytes)
            else:
                image_data = image_bytes

            # Save to file
            file_path = f"generated_images/{name}"
            os.makedirs("generated_images", exist_ok=True)

            with open(file_path, "wb") as f:
                f.write(image_data)

            print(f"💾 Image saved to: {file_path}")
            print(f"📏 Image size: {len(image_data)} bytes")

            self.artifacts[name] = file_path
            return True

        except Exception as e:
            print(f"❌ Error saving image: {e}")
            return False


async def test_image_generation():
    """Test the image generation tool."""

    print("🧪 Testing Image Generation Tool in Isolation")
    print("=" * 50)

    # Check environment variables
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    if not project_id:
        print("❌ GOOGLE_CLOUD_PROJECT environment variable not set")
        print("   Please set it with: export GOOGLE_CLOUD_PROJECT=your-project-id")
        return

    print(f"✅ Using Google Cloud Project: {project_id}")

    # Create mock tool context
    mock_context = MockToolContext()

    # Test parameters
    test_params = {
        "topic": "machine learning",
        "level": "beginner",
        "learning_style": "visual",
        "tool_context": mock_context,
        "specific_concept": "neural networks",
    }

    print(f"🎯 Testing with parameters:")
    print(f"   Topic: {test_params['topic']}")
    print(f"   Level: {test_params['level']}")
    print(f"   Learning Style: {test_params['learning_style']}")
    print(f"   Specific Concept: {test_params['specific_concept']}")
    print()

    try:
        print("🚀 Calling generate_educational_image...")
        result = await generate_educational_image(**test_params)

        print("📊 Result:")
        print(f"   Status: {result.get('status')}")
        print(f"   Message: {result.get('message')}")

        if result.get("status") == "success":
            artifact_name = result.get("artifact_name")
            print(f"   Artifact Name: {artifact_name}")
            print(f"   Files Saved: {list(mock_context.artifacts.values())}")
            print("✅ Image generation successful!")
            print(f"🖼️  You can view the image at: generated_images/{artifact_name}")
        else:
            print(f"❌ Image generation failed: {result.get('message')}")

    except Exception as e:
        print(f"💥 Exception during image generation: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_image_generation())
