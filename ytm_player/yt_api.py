"""Thin wrappers around the YouTube Data API v3."""

from __future__ import annotations

from typing import List

from googleapiclient.discovery import build  # type: ignore


def search(api_key: str, query: str) -> List[str]:
    """Return a list of video IDs matching ``query``."""
    youtube = build("youtube", "v3", developerKey=api_key)
    response = (
        youtube.search().list(part="id", q=query, type="video", maxResults=5).execute()
    )
    return [item["id"]["videoId"] for item in response.get("items", [])]


def get_video(video_id: str) -> str:
    """Return a watch URL for ``video_id``."""
    return f"https://www.youtube.com/watch?v={video_id}"


def oauth_device_flow() -> None:
    """TODO: Implement OAuth 2 Device Flow."""
    raise NotImplementedError
