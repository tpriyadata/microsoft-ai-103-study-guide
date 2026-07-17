import os
from typing import Tuple
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    azure_ai_search_index_name: str = "test-index"
    azure_openai_deployment_name: str = "mock-gpt-4o"

class MockCompletions:
    def create(self, *args, **kwargs):
        class Choice:
            class Message:
                content = "This is a simulated response for schema and routing verification."
                tool_calls = None
            message = Message()
        class MockResponse:
            choices = [Choice()]
        return MockResponse()

class MockChat:
    def __init__(self):
        self.completions = MockCompletions()

class MockAzureOpenAI:
    """Simulates Azure OpenAI REST responses to bypass cloud token charges."""
    def __init__(self, **kwargs):
        print("💰 [Cost Optimization] Local Mock Client Initialized - Zero Azure Fees.")
        self.chat = MockChat()

def initialize_azure_clients() -> Tuple[Settings, MockAzureOpenAI]:
    """Helper factory to return local configuration settings and mock clients."""
    settings = Settings()
    mock_client = MockAzureOpenAI()
    return settings, mock_client