"""
AI Tutor MVP Package

A personalized AI tutor that creates adaptive learning experiences through
intelligent assessment, dynamic content generation, and multimedia learning support.
"""

import os

import google.auth

_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")

from . import agent
