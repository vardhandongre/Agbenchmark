def build_zero_shot_prompt(example):
    dialog = "\n".join([f"{turn['speaker'].capitalize()}: {turn['text']}" for turn in example["dialog_context"]])
    return f"""You are an agricultural expert assisting users with planting, pest, and disease issues. 
Given the following conversation, Identify the missing information that is key important for achieving the user's goal and ask a clarification question that would help you better understand the user's goal 

Conversation:
\"\"\"
{dialog}
\"\"\"

Clarification Question:"""
