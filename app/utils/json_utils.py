import json
import re


def extract_json(response: str) -> dict:
    """
    Extract the first JSON object from an LLM response.
    """

    match = re.search(r"\{.*\}", response, re.DOTALL)

    if not match:
        raise ValueError("No JSON object found in LLM response.")

    json_string = match.group()

    return json.loads(json_string)