"""Shared chat-model configuration for the quantum lab agent."""

import os
from typing import Any

from dotenv import load_dotenv
from beeai_framework.backend import ChatModel, ChatModelError


load_dotenv()

DEFAULT_WATSONX_MODEL = "mistralai/mistral-small-3-1-24b-instruct-2503"


def model_name(agent: str = "LAB") -> str:
    """Return the configured BeeAI ``provider:model`` identifier."""
    configured = os.getenv("LAB_MODEL") or os.getenv("OPERATIONS_MODEL")
    if configured:
        return configured
    watsonx_model = (
        os.getenv("WATSONX_LAB_MODEL")
        or os.getenv("WATSONX_OPERATIONS_MODEL")
        or DEFAULT_WATSONX_MODEL
    )
    return f"watsonx:{watsonx_model}"


def create_chat_model(agent: str = "LAB") -> ChatModel:
    return ChatModel.from_name(model_name(agent))


def explain_error(error: Exception) -> str:
    explain = getattr(error, "explain", None)
    return explain() if callable(explain) else str(error)


async def run_agent_with_retries(agent: Any, prompt: str, *, retries: int = 2) -> Any:
    for attempt in range(1, retries + 2):
        try:
            return await agent.run(prompt)
        except ChatModelError as error:
            if attempt > retries:
                raise
            print(f"⚠️ [Retry] LLM call failed ({explain_error(error)}); retrying ({attempt}/{retries})...")
