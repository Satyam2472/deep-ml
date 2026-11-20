def inject_reasoning_effort(messages, effort_level):
    """
    messages: list of dicts with keys 'role' and 'content'
    effort_level: one of 'low', 'medium', 'high', 'max'
    Returns: new list of message dicts with reasoning-effort system prompt injected.
    """
    if effort_level not in ['low', 'medium', 'high', 'max']:
        raise ValueError()
    ans = []
    msg = {}

    if effort_level == 'low':
        content = "Reasoning effort: low. Provide concise answers with minimal deliberation."
    elif effort_level == "medium":
        content = "Reasoning effort: medium. Think step by step before answering."
    elif effort_level == 'high':
        content = "Reasoning effort: high. Carefully decompose the problem and verify each step."
    else:
        content = "Reasoning effort: max. Exhaustively decompose the problem, stress-test all edge cases, and document every intermediate step."

    if len(messages) == 0:
        msg['role'] = "system"
        msg['content'] = content
        ans.append(msg)

    elif messages[0]["role"] == "system":
        
        
        msg['role'] = messages[0]["role"]

        msg["content"] = content + "\n" + messages[0]["content"]
        ans.append(msg)

        for i in range(1, len(messages)):
            ans.append(messages[i])


    else:
        msg['role'] = "system"
        msg['content'] = content
        ans.append(msg)

        for i in range(len(messages)):
            ans.append(messages[i])

    return ans
