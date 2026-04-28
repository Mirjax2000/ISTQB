"""quiz.py"""

import random
import os
from typing import Dict, List, Set
from rich.console import Console
from data.questions_a import QUESTIONS as QUESTIONS_A
from data.questions_b import QUESTIONS as QUESTIONS_B
from data.questions_c import QUESTIONS as QUESTIONS_C


# ---
cons: Console = Console()
# ---

QUESTION_BANKS: Dict[str, tuple] = {
    "a": ("Vzorová zkouška ISTQB A", QUESTIONS_A),
    "b": ("Vzorová zkouška ISTQB B", QUESTIONS_B),
    "c": ("Vzorová zkouška ISTQB C", QUESTIONS_C),
}

ANSWER_COUNT_LABELS: Dict[int, str] = {
    1: "jednu správnou odpověď",
    2: "dvě správné odpovědi",
    3: "tři správné odpovědi",
    4: "čtyři správné odpovědi",
    5: "pět správných odpovědí",
}


def normalize_answer(user_input: str) -> Set[str]:
    """Convert comma-separated letters to a normalized set (lowercase, trimmed)."""
    if not user_input:
        return set()
    parts = user_input.split(",")
    normalized = {part.strip().lower() for part in parts if part.strip()}
    return normalized


def validate_answer(letters: Set[str], options: Dict[str, str]) -> bool:
    """Check that all provided letters exist among available option keys."""
    return all(letter in options for letter in letters) and len(letters) > 0


def is_correct(user_letters: Set[str], correct_letters: List[str]) -> bool:
    """Return True if user set exactly matches the set of correct letters."""
    return user_letters == set(correct_letters)


def format_correct_answers(correct_letters: List[str], options: Dict[str, str]) -> str:
    """Format correct answers for display, e.g. "a,e" plus optional texts."""
    letters_sorted: List[str] = sorted(correct_letters)
    letters_str: str = ",".join(letters_sorted)
    texts: List[str] = [f"{options.get(letter, '')}" for letter in letters_sorted]
    texts_str: str = "; ".join(texts)
    return f"[white bold]{letters_str})[/white bold] {texts_str}".strip()


def print_question_header(q_id: str, text: str) -> None:
    """Print the question rule and body text."""
    cons.print()
    if q_id:
        cons.rule(f"Otázka {q_id}:")
        cons.print()
    cons.print(text)
    cons.print()


def print_options(options: Dict[str, str]) -> None:
    """Print the lettered answer options."""
    for key in sorted(options.keys()):
        cons.print(f"  [cyan]{key}[/cyan]) {options[key]}")


def print_answer_hint(correct: List[str], points: int) -> None:
    """Print the correct-answer-count hint and point value."""
    count = len(correct)
    label = ANSWER_COUNT_LABELS.get(count, f"{count} správných odpovědí")
    cons.print()
    cons.print(f"Tato otázka má [cyan]{label}[/cyan].", style="gray50")
    cons.print(f"Tato otázka má hodnotu {points} bodů.", style="gray50")
    cons.print(
        "Zadejte písmena správných odpovědí oddělená čárkami (např. a,e).",
        style="blue",
    )


def read_valid_answer(options: Dict[str, str]) -> Set[str]:
    """Loop until the user enters a valid answer; return the normalised letter set."""
    while True:
        raw = cons.input("Vaše odpověď: ").strip()
        letters = normalize_answer(raw)
        if validate_answer(letters, options):
            return letters
        cons.print(
            "Neplatná odpověď. Použijte pouze písmena existujících možností, "
            "oddělená čárkami (např. a,e). Zkuste to znovu.",
            style="red",
        )


def print_result(
    correct_flag: bool,
    correct: List[str],
    options: Dict[str, str],
    explanation: str,
) -> None:
    """Print whether the answer was correct, the correct answer, and the explanation."""
    if correct_flag:
        cons.print("Správně!", style="green")
    else:
        cons.print("Nesprávně.", style="red")

    cons.print(
        "Správná odpověď:",
        format_correct_answers(correct, options),
        style="blue",
    )
    cons.print()
    if explanation:
        cons.print("Vysvětlení:", style="grey70")
        cons.print(explanation, style="grey50")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def ask_question(question: Dict) -> bool:
    """Show a single question, read answer from user, return True if correct."""
    if not question:
        cons.print("Chyba: Neplatná otázka.")
        return False

    q_id: str = question.get("id", "")
    text: str = question.get("text", "")
    options: Dict[str, str] = question.get("options", {})
    correct: List[str] = question.get("correct", [])
    explanation: str = question.get("explanation", "")
    points: int = question.get("points", 1)

    print_question_header(q_id, text)
    print_options(options)
    print_answer_hint(correct, points)

    letters = read_valid_answer(options)
    correct_flag = is_correct(letters, correct)

    print_result(correct_flag, correct, options, explanation)
    cons.input("Stiskněte Enter pro pokračování...")
    cons.clear()
    clear_screen()

    return correct_flag


def select_quiz_mode(total_questions: int) -> str:
    """Ask the user to choose sequential or random mode; return '1' or '2'."""
    cons.print()
    cons.print("Vyberte režim kvízu:", style="blue")
    cons.print("  [cyan]1[/cyan]) Otázky postupně")
    cons.print("  [cyan]2[/cyan]) Náhodné otázky")
    cons.print()
    while True:
        mode = cons.input("Zadejte volbu (1/2): ").strip()
        if mode in ("1", "2"):
            cons.clear()
            clear_screen()
            return mode
        cons.print("Neplatná volba. Zadejte prosím 1 nebo 2.", style="red")


def select_start_question(max_question: int) -> int:
    while True:
        raw = input(f"Zadej od jaké otázky začít (1 až {max_question}): ").strip()
        try:
            started_question = int(raw)
        except ValueError:
            cons.print("Zadej platné číslo.", style="red")
            continue
        if 1 <= started_question <= max_question:
            cons.clear()
            clear_screen()
            return started_question
        cons.print(
            f"Číslo musí být v rozsahu 1 až {max_question}. Zkus to znovu.", style="red"
        )


def read_question_count(total_questions: int) -> int:
    """Ask how many random questions to run; return a valid count."""
    cons.print(
        f"Kolik náhodných otázek chcete spustit? (1 až {total_questions})",
        style="blue",
    )
    while True:
        raw = cons.input("Počet otázek: ").strip()
        try:
            num = int(raw)
        except ValueError:
            cons.print("Neplatný vstup. Zadejte celé číslo.", style="red")
            continue
        if 1 <= num <= total_questions:
            return num
        cons.print(
            f"Počet musí být v rozsahu 1 až {total_questions}. Zkuste to znovu.",
            style="red",
        )


def build_question_list(questions_list: List[Dict], mode: str) -> List[Dict]:
    """Return the final ordered/shuffled slice of questions based on chosen mode."""
    questions = list(questions_list)
    if mode == "2":
        count = read_question_count(len(questions))
        random.shuffle(questions)
        return questions[:count]
    return questions


def run_questions(questions: List[Dict]) -> tuple:
    """Ask each question and accumulate score; return (score, total_points)."""
    total_points = sum(q.get("points", 1) for q in questions)
    score = 0
    for question in questions:
        if ask_question(question):
            score += question.get("points", 1)
    return score, total_points


def print_quiz_results(score: int, total_points: int) -> None:
    """Print the final score summary."""
    cons.print()
    cons.print("Kvíz dokončen.")
    cons.print(f"Získali jste {score} z {total_points} bodů.")
    cons.rule()
    if total_points > 0:
        percent = score / total_points * 100
        cons.print(f"Úspěšnost: {percent:.1f} %")


def run_quiz(questions_list: List[Dict]) -> None:
    if not questions_list:
        cons.print("Chyba: Nejsou k dispozici žádné otázky.", style="red")
        return

    mode = select_quiz_mode(len(questions_list))
    if mode == "1":
        max_question = len(questions_list)
        start = select_start_question(max_question)
        questions = questions_list[start - 1 :]
    else:
        questions = questions_list

    questions = build_question_list(questions, mode)
    score, total_points = run_questions(questions)
    print_quiz_results(score, total_points)


def select_bank() -> List[Dict]:
    """Show the question bank selection menu and return the chosen list."""
    cons.print()
    cons.print("Vyberte sadu otázek:", style="blue")
    for key, (name, _) in QUESTION_BANKS.items():
        cons.print(f"  [cyan]{key}[/cyan]) {name}")
    cons.print()

    valid_keys = list(QUESTION_BANKS.keys())
    prompt = "/".join(k.upper() for k in valid_keys)
    while True:
        choice = cons.input(f"Zadejte volbu ({prompt}): ").strip().lower()
        if choice in QUESTION_BANKS:
            break
        cons.print(f"Neplatná volba. Zadejte prosím {prompt}.", style="red")

    name, questions_list = QUESTION_BANKS[choice]
    cons.print(
        f"Zvolena sada: [cyan]{name}[/cyan] ({len(questions_list)} otázek)",
        style="blue",
    )
    return questions_list


def main() -> None:
    cons.clear()

    while True:
        questions_list = select_bank()
        run_quiz(questions_list)
        cons.print()
        again = input("Chcete si kvíz zopakovat? (a/n): ").strip().lower()
        if again != "a":
            cons.print("Děkujeme za použití kvízu. Nashledanou!")
            break


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\nDošlo k chybě:", e)
        import traceback

        traceback.print_exc()
        input("\nStiskněte Enter pro ukončení...")
