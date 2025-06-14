# agents/tools.py

import math

def tool_router(task):
    """
    Simple tool router:
    - Try to evaluate task as mathematical expression.
    - If fails, fallback to generic processing response.
    """
    try:
        result = eval(task)
        return f"Result: {result}"
    except:
        return f"Processed: {task}"

