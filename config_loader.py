import os
from typing import Tuple
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    azure_ai_search_index_name: str = "test-index"
    azure_openai_deployment_name: str = "mock-gpt-4o"
    # Placeholder fields if you decide to extend to live connections later
    azure_openai_endpoint: str = "https://mock.openai.azure.com"
    azure_openai_api_version: str = "2024-05-01-preview"

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
    """Initializes client with an automatic fallback to zero-cost mocks."""
    settings = Settings()
    
    # Force use of a mock client if developer mode or no credentials exist
    if os.getenv("DEVELOPMENT_MODE") == "true" or not os.path.exists(".env"):
        mock_client = MockAzureOpenAI()
        return settings, mock_client

    try:
        # In the future, you can import and use live Azure SDK components here
        # For now, we fall back to our local testing framework
        print("⚠ Live initialization bypassed. Falling back to Mock.")
        return settings, MockAzureOpenAI()
    except Exception:
        print("⚠ Live initialization failed. Falling back to Mock.")
        return settings, MockAzureOpenAI()