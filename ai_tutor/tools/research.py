"""
Research Tools for AI Tutor

Handles topic research using web search to enhance knowledge base.
"""

from google.adk.tools import ToolContext


def research_topic(
    topic: str,
    depth_level: str,
    tool_context: ToolContext,
) -> dict:
    """
    Research topic using Google Search to enhance knowledge base.

    Args:
        topic: The subject to research
        depth_level: How deep to research (basic/intermediate/advanced)
        tool_context: ADK tool context

    Returns:
        dict: Research results with key findings and resources
    """
    try:
        # Use Google Search to get real results
        search_query = f"{topic} {depth_level} learning tutorial guide"

        # For now, we'll use a web search tool if available
        # This will be replaced with actual Google Search API integration
        search_results = tool_context.search_web(search_query, max_results=5)

        # Process search results
        key_findings = []
        resources = []

        for result in search_results.get("results", []):
            if result.get("title") and result.get("snippet"):
                key_findings.append(f"{result['title']}: {result['snippet'][:200]}...")
                resources.append(
                    {
                        "title": result["title"],
                        "url": result.get("url", ""),
                        "snippet": result["snippet"],
                    }
                )

        research_results = {
            "status": "success",
            "topic": topic,
            "depth_level": depth_level,
            "key_findings": key_findings,
            "resources": resources,
            "research_confidence": 0.9,
            "search_query": search_query,
            "total_results": len(resources),
        }

    except Exception as e:
        # Fallback to simulated results if search fails
        research_results = {
            "status": "fallback",
            "topic": topic,
            "depth_level": depth_level,
            "key_findings": [
                f"Core concepts in {topic}",
                f"Latest developments in {topic}",
                f"Best practices for {topic}",
            ],
            "resources": [
                f"Official documentation for {topic}",
                f"Community resources for {topic}",
                f"Expert tutorials on {topic}",
            ],
            "research_confidence": 0.7,
            "error": str(e),
        }

    return research_results
