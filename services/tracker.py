from models.session import SessionData
from llm.openai_client import generate_message


def build_prompt(session: SessionData) -> str:
    """
    Build a prompt string for the LLM based on session data.

    Args:
        session (SessionData): The session data containing cart info, events, etc.

    Returns:
        str: A formatted prompt for the LLM to generate a customer-facing message.
    """

    if session.cart_items:
        cart_summary = "\n".join(
            [f"- {item.title} (x{item.quantity})" for item in session.cart_items]
        )
    else:
        cart_summary = "No items yet"

    return f"""
A user is browsing an e-commerce site.

- Current page: {session.current_page}
- Time on site: {session.time_on_site} seconds
- Events: {", ".join([e.type for e in session.events]) or "None"}
- Cart contains:
{cart_summary}

Generate a short, helpful, friendly message encouraging them to act.
Mention product names if appropriate.
Limit the message to 1-2 sentences.
""".strip()


def handle_session(session: SessionData) -> dict:
    """
    Handle an incoming session request and determine whether to show a message,
    and if so, generate one using the LLM.

    Args:
        session (SessionData): Incoming session data from the frontend tracker.

    Returns:
        dict: A response object like {"show": bool, "message": str | None}
    """

    if session.current_page == "/" and session.time_on_site == 0:
        if session.cart_items:
            return {
                "show": True,
                "message": f"👋 Welcome back! You still have {len(session.cart_items)} item{'s' if len(session.cart_items) > 1 else ''} in your cart",
            }
        return {"show": True, "message": "👋 Welcome to our store! Take a look around."}

    should_show = (
        session.current_cart_count > 0
        or session.time_on_site > 120
        or session.current_page != "/"
    )

    if not should_show:
        return {"show": False, "message": None}

    prompt = build_prompt(session)
    message = generate_message(prompt)

    return {"show": True, "message": message}
