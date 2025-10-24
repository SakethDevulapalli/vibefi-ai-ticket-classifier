def classify_ticket(ticket):
    """
    Core logic for classifying support tickets into:
    - AI_Code_Patch
    - Vibe_Coded_Workflow

    Returns structured response with decision, reasoning, and checklist.
    """

    channel = ticket.get("channel", "").lower()
    severity = ticket.get("severity", "").lower()
    summary = ticket.get("summary", "").lower()

    decision = "Vibe_Coded_Workflow"
    reasoning = "Defaulted to workflow for general troubleshooting."
    next_actions = [
        "Assign to Vibe workflow handler",
        "Run standard diagnostic scripts",
        "Follow-up with customer if unresolved"
    ]

    # --- Classification Heuristics ---
    if "error" in summary or "exception" in summary or "crash" in summary:
        decision = "AI_Code_Patch"
        reasoning = "Detected technical error suggesting a code-level issue requiring AI-generated remediation."
        next_actions = [
            "Trigger AI code patch generation workflow",
            "Run patch simulation in staging",
            "Validate fix via API test suite"
        ]
    elif "payment" in summary or "transaction" in summary:
        decision = "AI_Code_Patch" if severity in ["high", "critical"] else "Vibe_Coded_Workflow"
        reasoning = "Payment-related issue prioritized for AI remediation due to potential financial impact."
        next_actions = [
            "Analyze transaction logs",
            "Run AI repair model for backend scripts",
            "Verify patch in QA environment"
        ]
    elif "login" in summary or "access" in summary:
        reasoning = "Access-related issue suitable for pre-coded troubleshooting workflow."
        next_actions = [
            "Reset user session tokens",
            "Re-run authentication test scripts",
            "Notify customer about restored access"
        ]
    elif "slow" in summary or "performance" in summary:
        reasoning = "Performance degradation—requires system diagnostics via coded workflow."
        next_actions = [
            "Run performance analysis scripts",
            "Identify and isolate slow modules",
            "Apply performance patch if needed"
        ]

    return {
        "decision": decision,
        "reasoning": reasoning,
        "next_actions": next_actions
    }
