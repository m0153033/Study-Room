# Daily question refresh (until Exam 5 on Nov 30, 2026)

Each run ADDS a new set of questions; nothing is deleted. The site serves the newest set first
(unseen questions first, ties go to the newest `v`), so the study room feels brand new each day.

## Rotation (America/New_York date of the run)
| Date | Exams |
|---|---|
| Mon 11/23 | Exam 5 + Exam 1 |
| Tue 11/24 | Exam 5 + Exam 2 |
| Wed 11/25 | Exam 5 + Exam 3 |
| Thu 11/26 | Exam 5 + Exam 4 |
| Fri 11/27 | Exam 5 + Exam 1 |
| Sat 11/28 | Exam 5 + Exam 2 |
| Sun 11/29 | Exam 5 + Exam 3 |
After 11/29: do nothing.

## How to write a set
1. `python3 src/tools/topic_ref.py --list` shows topics per exam. `python3 src/tools/topic_ref.py <topic>` prints that
   topic's concepts and every existing question with its answer and rationale. **That output is the only allowed
   source**: new questions may use only facts already stated there (the lecture material). No outside facts.
   If it prints a **NOT TESTED** list (from the professor's updated lecture tips), write NO questions on those items.
2. For every topic of the day's exams, write `src/refresh/<topic>_<YYYYMMDD>.py`:
   ```python
   T = "e5skin"; SET = "20261123"
   SATA = "Select all that apply."
   Q = []
   def q(c, stem, opts, r): Q.append((c, stem, opts, r))
   q("bcc", "A client ...?", ["*Correct answer", "Wrong option || why it's wrong", ...], "Rationale.")
   ```
   - One NEW question for every concept; two for each concept listed as key (HI).
   - New wording, new client scenarios, different angle (priority, teaching, finding, intervention, compare),
     different distractors. Never copy an existing stem or answer set.
   - `*` marks correct options. Every wrong option needs `|| short reason it's wrong`.
   - Select-all questions end the stem with `SATA` and have 2+ correct options; others have exactly 1 correct.
   - Write drugs by generic name only; the build adds "(Brand)" and spells out abbreviations at first use.
   - No dosage calculation or math. Keep options similar in length so the answer isn't the longest one.
3. Build and check: `OUT=$PWD/questions.js python3 src/gen_questions.py` (must print counts with no assertion error),
   then `node -e "global.window=global;eval(require('fs').readFileSync('questions.js','utf8').replace(/^const /gm,'var '))"`.
4. Commit only `src/refresh/*` and `questions.js` to `main` and push. GitHub Pages republishes in about a minute.
