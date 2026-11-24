T = "e2w42"; SET = "20261124"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("rls", "A 52-year-old client describes an unpleasant feeling in the legs with an urge to move them. When does the nurse expect these symptoms to be worst?",
  ["During and right after exercise || RLS symptoms occur at rest and are relieved by movement",
   "*At rest, usually at bedtime",
   "First thing in the morning on waking || Symptoms usually occur at bedtime",
   "Mainly while the client is walking || Walking relieves RLS symptoms"],
  "RLS (restless legs syndrome): unpleasant leg sensations plus an urge to move, at rest (usually bedtime), relieved by movement.")

q("rlsrisk", "The nurse reviews client histories in a sleep clinic. Which findings can contribute to restless legs syndrome? " + SATA,
  ["*Multiple sclerosis (MS)",
   "*Taking an antidepressant",
   "A diet rich in iron || Iron DEFICIENCY is the risk factor",
   "*Current pregnancy",
   "Sleeping a full 8 hours nightly || INSUFFICIENT sleep is the risk factor"],
  "RLS risks: insufficient sleep, pregnancy, iron deficiency, MS, dopamine abnormalities; antidepressants, metoclopramide and haloperidol.")

q("rlstx", "A 74-year-old client is starting ropinirole for restless legs syndrome. Which teaching is the priority?",
  ["'Take it each morning with breakfast.' || Ropinirole is taken at night",
   "'It works by replacing the iron you are missing.' || Ropinirole is a dopamine agonist; ferrous sulfate replaces iron",
   "*'Change positions slowly; it can cause dizziness and falls.'",
   "'It blocks dopamine to calm your leg muscles.' || Ropinirole mimics or increases dopamine action"],
  "Ropinirole is a dopamine agonist taken at night. Watch for drowsiness, dizziness, syncope and falls; it may interact with warfarin and raise INR.")

q("insom", "The nurse reviews sleep hygiene with a client who has insomnia. Which client statement indicates a need for MORE teaching?",
  ["'I'll get up at the same time every day, even on weekends.' || Consistent bed and wake times are correct",
   "'I'll keep my bedroom quiet, dark and cool.' || Correct sleep hygiene",
   "'I'll put my phone away before bed.' || Avoiding screens before bed is correct",
   "*'I'll go for my run right before bed so I'm tired.'"],
  "Exercise during the day but NOT right before bed. Sleep hygiene also includes consistent times, a quiet dark cool room, no screens and limiting caffeine later in the day.")

q("zolp", "A client prescribed zolpidem has an early flight and plans to sleep only 5 hours tonight. What should the nurse advise?",
  ["'Take it after dinner so it works by bedtime.' || Take it immediately before bed because of rapid onset",
   "*'Don't take it tonight; plan at least 7 hours of sleep with it.'",
   "'Take half a dose with a glass of wine instead.' || Never take zolpidem with alcohol",
   "'Add an over-the-counter sleep aid to help it.' || Never combine with other sleep meds"],
  "Zolpidem: take immediately before bed (rapid onset), plan at least 7 hours of sleep, and never take with alcohol or other sleep meds.")

q("melat", "A client asks about trying melatonin for sleep. Which statements by the nurse are accurate? " + SATA,
  ["*'It is available over the counter.'",
   "*'It is not habit-forming.'",
   "'Start with 10 mg each night.' || Start with 1 mg and titrate up",
   "*'Take it about 30 minutes before bed.'",
   "*'It is a cost-effective option.'"],
  "Melatonin: OTC (over-the-counter), non-habit-forming, cost-effective, lower confusion and fall risk in older adults. Take 30 minutes before bed; start 1 mg and titrate up.")

q("narco", "A 22-year-old college student reports falling asleep in class several times a day for a few minutes, even after a full night's sleep. Which condition does this suggest?",
  ["Insomnia || Insomnia is difficulty sleeping, not daytime sleep attacks",
   "Restless legs syndrome || RLS causes leg discomfort at rest",
   "*Narcolepsy",
   "Obstructive sleep apnea || OSA is linked to snoring and witnessed apneas"],
  "Narcolepsy: extreme daytime drowsiness plus involuntary sleep attacks lasting seconds to minutes regardless of prior sleep; onset is usually ages 15-30.")

q("narcotx", "Why is methylphenidate only rarely used to treat narcolepsy?",
  ["It is an iron supplement with little effect on sleep || It is not an iron supplement",
   "*It carries a risk of addiction",
   "It is a benzodiazepine that worsens cataplexy || It is not described as a benzodiazepine",
   "It is only approved for restless legs syndrome || That is not why it is rarely used"],
  "First-line narcolepsy drugs are modafinil or armodafinil (non-amphetamine wake-promoting). Methylphenidate is used rarely because of addiction risk.")

q("osa", "A client is being evaluated for obstructive sleep apnea. Which daytime findings does the nurse expect? " + SATA,
  ["*Morning headache",
   "Sudden loss of muscle tone when laughing || That is cataplexy, seen with narcolepsy",
   "*Daytime sleepiness",
   "A crawling leg feeling relieved by walking || That is restless legs syndrome",
   "*Irritability"],
  "OSA (obstructive sleep apnea) daytime findings: morning headache, sleepiness and irritability. OSA is linked with hypertension, CVD and diabetes.")

q("dx", "A client chooses a home sleep apnea test (HSAT) instead of polysomnography (PSG). Which limitation should the nurse explain?",
  ["It is more expensive than an in-lab study || HSAT is cheaper",
   "It must be done overnight in a sleep lab || HSAT is portable and done at home",
   "*It cannot tell obstructive from central sleep apnea",
   "It is the gold standard, so no limits apply || PSG is the gold standard"],
  "HSAT: portable, convenient, cheaper, slightly less accurate, and cannot distinguish OSA from CSA. PSG is the in-lab gold standard that can.")

q("osatx", "An adult client newly diagnosed with mild obstructive sleep apnea asks about having surgery instead of CPAP (continuous positive airway pressure). Which response is accurate?",
  ["*'CPAP is first-line; surgery is a second option if CPAP isn't tolerated.'",
   "'Surgery is first-line for adults with mild sleep apnea.' || CPAP is first-line regardless of severity",
   "'CPAP is only used when the apnea is severe.' || CPAP is first-line regardless of severity",
   "'A wake-promoting drug can replace CPAP for you.' || CPAP is the first-line treatment"],
  "CPAP is first-line for adult OSA regardless of severity. Surgery is secondary if CPAP is not tolerated.")

q("pedosa", "Which statement correctly compares first-line treatment for obstructive sleep apnea in children and adults?",
  ["Both children and adults start with CPAP (continuous positive airway pressure) || Pediatric first-line is adenotonsillectomy",
   "Both children and adults start with adenotonsillectomy || Adult first-line is CPAP",
   "Children start with CPAP; adults start with adenotonsillectomy || This reverses the two",
   "*Children start with adenotonsillectomy; adults start with CPAP"],
  "Pediatric OSA first-line is adenotonsillectomy; adult first-line is CPAP. After surgery, reinforce a follow-up sleep study.")

q("csa", "Which client is at greatest risk for central sleep apnea?",
  ["An obese man with an 18-inch neck who snores loudly || These are OSA risk factors",
   "A pregnant client with low ferritin || These are RLS risk factors",
   "*A client recovering from a stroke who takes opioids",
   "A 20-year-old with cataplexy when laughing || Cataplexy is seen with narcolepsy"],
  "CSA (central sleep apnea): the airway is open but the brain fails to signal breathing. Risks include opioids, HF (heart failure) and stroke; apnea occurs without snoring.")

q("pap", "A client with hyperventilation-type central sleep apnea travels often for work. Which device does the nurse expect?",
  ["BiPAP (bilevel positive airway pressure) || BiPAP is for hypoventilation CSA and is more expensive",
   "Nasal cannula at 2 L || Not the listed device for CSA",
   "*CPAP (continuous positive airway pressure)",
   "No device; CSA has no airway pressure therapy || CPAP or BiPAP is used depending on CSA type"],
  "Hyperventilation CSA uses CPAP: one continuous pressure, 4-20 cm H2O, portable. Hypoventilation CSA uses BiPAP: two pressures, 4-30, more expensive.")
