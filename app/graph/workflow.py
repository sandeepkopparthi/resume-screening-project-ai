from langgraph.graph import StateGraph, START, END

from app.models.screening_state import ScreeningState

from app.nodes.resume_parser import ResumeParserNode
from app.nodes.jd_parser import JDParserNode
from app.nodes.candidate_evaluator import CandidateEvaluatorNode
from app.nodes.interview_generator import InterviewGeneratorNode

from app.services.llm_service import LLMService


class ScreeningWorkflow:

    def __init__( self,
        resume_parser: ResumeParserNode,
        jd_parser: JDParserNode,
        candidate_evaluator: CandidateEvaluatorNode,
        interview_generator: InterviewGeneratorNode):

        # Shared infrastructure
        self.llm_service = LLMService()

        # Existing nodes
        self.resume_parser = resume_parser
        self.jd_parser = jd_parser
        self.candidate_evaluator = candidate_evaluator
        self.interview_generator = interview_generator

        # Build workflow
        self.graph = self._build_graph()

    def _build_graph(self):

        builder = StateGraph(ScreeningState)

        # Register nodes
        builder.add_node(
            "resume_parser",
            self.resume_parser.invoke,
        )

        builder.add_node(
            "jd_parser",
            self.jd_parser.invoke,
        )

        builder.add_node(
            "candidate_evaluator",
            self.candidate_evaluator.invoke,
        )

        builder.add_node(
            "interview_generator",
            self.interview_generator.invoke,
        )

        # Define execution flow
        builder.add_edge(
            START,
            "resume_parser",
        )

        builder.add_edge(
            "resume_parser",
            "jd_parser",
        )

        builder.add_edge(
            "jd_parser",
            "candidate_evaluator",
        )

        builder.add_edge(
            "candidate_evaluator",
            "interview_generator",
        )

        builder.add_edge(
            "interview_generator",
            END,
        )

        return builder.compile()

    def invoke(self, state: ScreeningState) -> ScreeningState:
        """
        Execute the complete screening workflow.
        """
        result = self.graph.invoke(state)
        if isinstance(result, dict):
            return ScreeningState.model_validate(result)

        return result