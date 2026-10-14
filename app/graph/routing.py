from langgraph.graph import END

from app.models.screening_state import ScreeningState

MIN_INTERVIEW_SCORE = 60


def route_after_evaluation(
    state: ScreeningState,
) -> str:
    """
    Decide whether the candidate should proceed to interview generation.
    """

    evaluation = state.candidate_evaluation

    if evaluation is None:
        return END

    if evaluation.overall_score >= MIN_INTERVIEW_SCORE:
        return "interview_generator"

    return END