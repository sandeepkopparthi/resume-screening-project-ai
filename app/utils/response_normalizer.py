from copy import deepcopy


def normalize_resume_response(data: dict) -> dict:
    """
    Normalize common LLM inconsistencies before Pydantic validation.
    """

    normalized = deepcopy(data)

    #
    # Certifications
    #
    certifications = normalized.get("certifications", [])

    normalized["certifications"] = [
        cert["certification"]
        if isinstance(cert, dict)
        else cert
        for cert in certifications
    ]

    return normalized