import re

CENSOR_LIST = [
    r"(Ondra|Ondřej)\s+Mandík",
    r"Alena\s+Reichlová",
    r"(Jára|Jaroslav)\s+Cimrman"
]

def censor_text(text: str) -> str:
    for pattern in CENSOR_LIST:
        text = re.sub(pattern, "[AUTOMATICKY CENZUROVÁNO]", text, flags=re.IGNORECASE)
    return text

def count_words(text: str) -> int:
    words = re.findall(r"[A-Za-zÁ-ž0-9']+", text)
    count = 0
    for w in words:
        if re.fullmatch(r"\d+", w):
            continue
        if re.fullmatch(r"\w+'\w+", w) and w.lower() not in ["can't", "cannot"]:
            count += 2
        else:
            count += 1
    return count
