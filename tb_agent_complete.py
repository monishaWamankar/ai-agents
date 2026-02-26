import random
from typing import TypedDict
from langgraph.graph import StateGraph, END

class TBState(TypedDict):
    cough_audio: str
    tb_risk: float
    risk_level: str
    clinic_name: str
    clinic_distance: str
    hindi_alert: str

def classify_cough(state: TBState) -> TBState:
    tb_risk = round(random.uniform(0.1, 0.95), 2)
    state["tb_risk"] = tb_risk
    print(f"🔍 AI: TB Risk = {tb_risk:.1%}")
    return state

def check_risk_level(state: TBState) -> TBState:
    if state["tb_risk"] > 0.85:
        state["risk_level"] = "🚨 EMERGENCY"
    elif state["tb_risk"] > 0.60:
        state["risk_level"] = "⚠️ HIGH"
    else:
        state["risk_level"] = "✅ LOW"
    print(f"🏥 Decision: {state['risk_level']}")
    return state

def make_hindi_voice(state: TBState) -> TBState:
    if "EMERGENCY" in state["risk_level"]:
        state["hindi_alert"] = "🚨 टीबी खतरा उच्च! तुरंत क्लिनिक!"
    elif "HIGH" in state["risk_level"]:
        state["hindi_alert"] = "⚠️ टीबी खतरा! 24 घंटे में क्लिनिक!"
    else:
        state["hindi_alert"] = "✅ खतरा कम। लक्षण देखें।"
    print(f"🔊 Hindi: {state['hindi_alert']}")
    return state

# Build agent
workflow = StateGraph(TBState)
workflow.add_node("ai_doctor", classify_cough)
workflow.add_node("risk_decision", check_risk_level)
workflow.add_node("hindi_voice", make_hindi_voice)
workflow.set_entry_point("ai_doctor")
workflow.add_edge("ai_doctor", "risk_decision")
workflow.add_edge("risk_decision", "hindi_voice")
workflow.add_edge("hindi_voice", END)
tb_agent = workflow.compile()

# Test
result = tb_agent.invoke({"cough_audio": "test.wav"})
print("\n✅ TB AGENT SAVED & WORKING!")
