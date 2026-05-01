"""Move / transition command."""

from __future__ import annotations

import json
import sys
from typing import Any

from lazyjira.api import jira_api, transition_issue


def cmd_move(args: Any) -> None:
    """Transition an issue to a new status."""
    success = transition_issue(args.key, args.status)
    if success:
        print(f"✅ {args.key} → {args.status}")
    else:
        # Fetch current status for a better error message
        issue = jira_api("GET", f"/rest/api/3/issue/{args.key}?fields=status")
        current = issue.get("fields", {}).get("status", {}).get("name", "unknown") if not issue.get("error") else "unknown"
        print(f"❌ Could not transition {args.key} to '{args.status}' (currently: {current})", file=sys.stderr)
        transitions = jira_api("GET", f"/rest/api/3/issue/{args.key}/transitions")
        if not transitions.get("error"):
            avail = [t["to"]["name"] for t in transitions.get("transitions", [])]
            print(f"Available transitions: {', '.join(avail) or '(none — may be a terminal state)'}", file=sys.stderr)
        sys.exit(1)
