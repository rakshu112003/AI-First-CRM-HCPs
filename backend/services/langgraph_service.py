from typing import TypedDict

from langgraph.graph import StateGraph, END

from app.services.groq_service import generate_ai_response


class AgentState(TypedDict):
    message: str
    response: str


def call_groq(state: AgentState):
    ai_response = generate_ai_response(state["message"])

    return {
        "message": state["message"],
        "response": ai_response
    }


workflow = StateGraph(AgentState)

workflow.add_node("groq", call_groq)

workflow.set_entry_point("groq")

workflow.add_edge("groq", END)

app = workflow.compile()


def run_langgraph(message: str):
    result = app.invoke(
        {
            "message": message,
            "response": ""
        }
    )

    return result["response"]
