import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from azure.identity import DefaultAzureCredential
from openai import AzureOpenAI

class AzureSettings(BaseSettings):
    azure_ai_foundry_project_endpoint: str = "mock-endpoint"
    azure_openai_endpoint: str = "mock-openai"
    azure_openai_deployment_name: str = "gpt-4o"
    azure_openai_api_version: str = "2024-05-01-preview"
    azure_ai_search_endpoint: str = "mock-search"
    azure_ai_search_index_name: str = "test-index"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

# ===================================================================== #
# COST-OPTIMIZATION: ZERO-COST MOCK CLIENT FOR AGENT PREP WORK          #
# ===================================================================== #
class MockAzureOpenAI:
    """Simulates Azure OpenAI REST responses to bypass cloud token charges."""
    def __init__(self, **kwargs):
        print("💰 [Cost Optimization] Local Mock Client Initialized - Zero Azure Fees.")
        self.chat = self.MockChat()

    class MockChat:
        def __init__(self):
            self.completions = self.MockCompletions()

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

def initialize_azure_clients():
    """Initializes client with an automatic fallback to zero-cost mocks."""
    # Force use of a mock client if developer mode or no credentials exist
    if os.getenv("DEVELOPMENT_MODE") == "true" or not os.path.exists(".env"):
        settings = AzureSettings()
        openai_client = MockAzureOpenAI()
        return settings, openai_client

    try:
        settings = AzureSettings()
        credential = DefaultAzureCredential()
        openai_client = AzureOpenAI(
            azure_endpoint=settings.azure_openai_endpoint,
            api_version=settings.azure_openai_api_version,
            azure_ad_token_provider=credential.get_token_provider(
                "https://cognitiveservices.azure.com/.default"
            )
        )
        print("🔒 Keyless Managed Identity / DefaultAzureCredential connected.")
        return settings, openai_client
    except Exception:
        print("⚠ Live initialization failed or bypassed. Falling back to Mock.")
        return AzureSettings(), MockAzureOpenAI()
