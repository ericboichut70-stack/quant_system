# 📁 Collaboration mentorale
import pandas as pd

def load_mentor_feedback(path="utils/mentor_feedback_log.txt"):
    """
    Charge les feedbacks mentoraux pour collaboration.
    """
    df = pd.read_csv(path, sep="|", names=["timestamp", "ScenarioType", "mentor", "decision", "comment"])
    return df


def submit_mentor_feedback(timestamp, scenario, mentor, decision, comment, path="utils/mentor_feedback_log.txt"):
    """
    Enregistre un feedback mentoral collaboratif.
    """
    from datetime import datetime
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | {scenario} | {mentor} | {decision} | {comment}\n")
