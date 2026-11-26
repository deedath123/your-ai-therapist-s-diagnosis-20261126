import os

ENTRY = "Diagnosis: acute 2 a.m. doomscrolling. You apologised to Alexa at 3:12 a.m. for yelling at her, and your wife has filed it as your most sincere apology this year."

def main():
    assert ENTRY.strip(), "entry must be non-blank"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
