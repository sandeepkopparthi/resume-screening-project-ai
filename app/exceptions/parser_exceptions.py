class ResumeParserError(Exception):
    """
    Raised when the resume parser cannot produce
    a valid Resume object.
    """
    pass 

class ApplicationException(Exception):
    """Base exception for the application."""
    pass

class ParserException(ApplicationException):
    """Raised when parsing fails."""
    pass

class EvaluationException(ApplicationException):
    """Raised when candidate evaluation fails."""
    pass