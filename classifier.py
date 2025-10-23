def classify_ticket(ticket):
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

    if "error" in summary or "exception" in summary or "crash" in summary:
        decision = "AI_Code_Patch"
        reasoning = "Detected technical error suggesting a code-level issue."
        next_actions = [
            "Generate AI patch for identified module",
            "Simulate patch in staging environment",
            "Validate and deploy fix"
        ]
    elif "payment" in summary or "transaction" in summary:
        decision = "AI_Code_Patch" if severity in ["high", "critical"] else "Vibe_Coded_Workflow"
        reasoning = "Payment-related issue prioritized for AI fix due to financial impact."
        next_actions = [
            "Analyze transaction logs",
            "Run AI repair model for backend scripts",
            "Verify with QA tests before release"
        ]
    elif "login" in summary or "access" in summary:
        reasoning = "Access-related issue suitable for pre-coded troubleshooting flow."
        next_actions = [
            "Reset user session",
            "Re-run authentication test workflow",
            "Notify customer about access recovery"
        ]
    elif "slow" in summary or "performance" in summary:
        reasoning = "Performance degradation—requires system metrics analysis via coded workflow."
        next_actions = [
            "Run performance diagnostic scripts",
            "Identify bottleneck module",
            "Apply patch if required"
        ]

    return {
        "decision": decision,
        "reasoning": reasoning,
        "next_actions": next_actions
    }
