"""
Prompts module for FreshAI backend.
Contains system prompts and prompt templates for AI analysis.
"""

from .ticket_analysis_prompt import (
    TICKET_ANALYSIS_SYSTEM_PROMPT,
    TICKET_ANALYSIS_PROMPT_TEMPLATE
)

__all__ = [
    "TICKET_ANALYSIS_SYSTEM_PROMPT",
    "TICKET_ANALYSIS_PROMPT_TEMPLATE"
]
