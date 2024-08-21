import os
import logging
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

class DeveloperService:
    def __init__(self):
        api_key = os.getenv("MISTRAL_API_KEY")
        endpoint = os.getenv("DLAI_MISTRAL_API_ENDPOINT")

        if not api_key:
            raise ValueError("API key not provided. Please set MISTRAL_API_KEY environment variable.")

        self.client = MistralClient(api_key=api_key, endpoint=endpoint)

    def generate_code(self, description):
        logging.info(f"Generating code for task: {description}")
        try:
            messages = [ChatMessage(role="user", content=description)]
            response = self.client.chat(
                model="mistral-small-latest",
                messages=messages
            )

            # Extract and return only the code part
            code_blocks = self.extract_code_blocks(response.choices[0].message.content)
            return "\n".join(code_blocks)
        except Exception as e:
            logging.error(f"Error generating code: {e}")
            return None

    def extract_code_blocks(self, content):
        """Extracts code blocks from the response content."""
        in_code_block = False
        code_lines = []

        for line in content.splitlines():
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
            elif in_code_block:
                code_lines.append(line)

        return code_lines
