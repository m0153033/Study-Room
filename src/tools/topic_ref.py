"""Prints one topic's concepts and every existing question (stem, options, answer, rationale), as the source material
for writing a refresh set. Usage: python3 src/tools/topic_ref.py e5viral   (or: --list to see all topics by exam)"""
import sys, os, json, subprocess, tempfile
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = os.path.join(tempfile.mkdtemp(), "q.js")
subprocess.run([sys.executable, os.path.join(HERE, "gen_questions.py")], env=dict(os.environ, OUT=out), check=True, capture_output=True)
src = open(out, encoding="utf-8").read()
def grab(name):
    i = src.index(f"const {name} = ") + len(f"const {name} = "); j = src.index(";\n", i); return json.loads(src[i:j])
EXAMS, TOPICS, CONCEPTS, HI = grab("EXAMS"), grab("TOPICS"), grab("CONCEPTS"), grab("HI")
BANK = [json.loads(l.rstrip(",")) for l in src[src.index("const BANK = [")+15:src.rindex("];")].splitlines() if l.startswith("{")]
if len(sys.argv) < 2 or sys.argv[1] == "--list":
    for e in EXAMS:
        print(e["name"], ":", ", ".join(f"{t} ({TOPICS[t]}, {len(CONCEPTS[t])} concepts)" for t in e["topics"] if CONCEPTS.get(t)))
    sys.exit()
t = sys.argv[1]
print(f"# {t} — {TOPICS[t]}\n\nKey concepts (HI, get 2 new questions): {HI[t]}\n")
import glob, importlib.util
for f in glob.glob(os.path.join(HERE, "*_bank.py")):
    sp = importlib.util.spec_from_file_location("b", f); b = importlib.util.module_from_spec(sp); sp.loader.exec_module(b)
    if b.T == t and getattr(b, "NOT_TESTED", None):
        print("NOT TESTED per the professor's updated lecture. Write NO questions on these:\n- " + "\n- ".join(b.NOT_TESTED) + "\n")
for c, label in CONCEPTS[t].items():
    print(f"\n## concept `{c}` — {label}")
    for q in [q for q in BANK if q["t"] == t and q["c"] == c]:
        ans = q["a"] if isinstance(q["a"], list) else [q["a"]]
        print(f"- Q: {q['q']}\n  A: " + " | ".join(("*" if i in ans else "") + o for i, o in enumerate(q["o"])) + f"\n  R: {q['r']}")
