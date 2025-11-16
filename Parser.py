import re
from models import PlayerAdvice

def parse_ai_response(ai_text: str):
    """
    A SAFE parser that:
    - never crashes
    - extracts players even if Gemini formatting changes
    - extracts advice sections reliably
    """

    players_list = []
    advice_list = []

    # -----------------------------
    # EXTRACT PLAYERS
    # -----------------------------
    players_pattern = r"PLAYERS:\s*(.*?)\n\s*ANALYSIS"
    players_match = re.search(players_pattern, ai_text, re.DOTALL | re.IGNORECASE)

    if players_match:
        players_block = players_match.group(1)
        for line in players_block.split("\n"):
            line = line.strip()
            if line.startswith("-"):
                line = line[1:].strip()

                # Remove position if present
                name = re.split(r"[—\-]", line)[0].strip()
                if name:
                    players_list.append(name)

    # Fallback: if AI did not include PLAYERS: section
    if not players_list:
        # Try to find names in advice section
        possible_names = re.findall(r"-\s*([A-Za-z '.]+):", ai_text)
        players_list = list(set(n.strip() for n in possible_names))

    # -----------------------------
    # EXTRACT ADVICE BLOCKS
    # -----------------------------
    advice_pattern = r"ADVICE:\s*(.*)"
    advice_match = re.search(advice_pattern, ai_text, re.DOTALL | re.IGNORECASE)

    if not advice_match:
        # If no advice section, return at least players
        return players_list, advice_list

    advice_block = advice_match.group(1)

    # Split blocks: each starts with "- Player Name:"
    entries = re.split(r"\n-\s*", advice_block)
    entries = entries[1:]  # first chunk is empty text before the first "-"

    for entry in entries:
        lines = [l.strip() for l in entry.splitlines() if l.strip()]
        if not lines:
            continue

        # First line: "Player Name:"
        name = lines[0].replace(":", "").strip()

        recommendation = ""
        explanation = ""
        confidence = 0.0

        for line in lines[1:]:
            if line.lower().startswith("recommendation"):
                recommendation = line.split(":", 1)[1].strip()

            elif line.lower().startswith("explanation"):
                explanation = line.split(":", 1)[1].strip()

            elif line.lower().startswith("confidence"):
                try:
                    confidence = float(line.split(":", 1)[1].strip())
                except:
                    confidence = 0.0

        advice_list.append(
            PlayerAdvice(
                player=name,
                recommendation=recommendation,
                explanation=explanation,
                confidence=confidence,
            )
        )

    return players_list, advice_list
