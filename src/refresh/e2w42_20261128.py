T = "e2w42"; SET = "20261128"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("rls", "A 48-year-old client reports an unpleasant pulling feeling in both legs while watching TV in the evening. Which additional finding best supports restless legs syndrome?",
  ["The feeling gets worse when the client walks || RLS (restless legs syndrome) is relieved by movement",
   "*The client feels a strong urge to move the legs",
   "The client snores and stops breathing at night || That suggests sleep apnea",
   "The client falls asleep suddenly while laughing || Emotion-triggered events suggest narcolepsy"],
  "RLS (restless legs syndrome): unpleasant leg sensations plus an urge to move, at rest (usually bedtime), relieved by movement.")

q("rlsrisk", "A 30-year-old client in her third trimester reports new leg discomfort at bedtime that eases when she walks. Which other history finding would also raise her risk for this problem?",
  ["A diet high in iron-rich foods || Iron deficiency, not a high-iron diet, is the risk",
   "*A low ferritin level on recent labs",
   "Sleeping a full 8 hours each night || Insufficient sleep is the risk",
   "Taking no medications at all || Some drugs (antidepressants, metoclopramide, haloperidol) are risks"],
  "RLS (restless legs syndrome) risks: insufficient sleep, pregnancy, iron deficiency, MS (multiple sclerosis), dopamine abnormalities; antidepressants, metoclopramide and haloperidol.")

q("rlstx", "A client with restless legs syndrome is starting ropinirole. Which teaching points are accurate? " + SATA,
  ["*Take it at night",
   "*Rise slowly to lower fall risk",
   "It replaces missing iron stores || Iron is replaced with ferrous sulfate",
   "*Report dizziness or fainting",
   "It works by blocking dopamine || Ropinirole is a dopamine agonist"],
  "Ropinirole is a dopamine agonist taken at night. Watch for drowsiness, dizziness, syncope and falls; it may interact with warfarin and raise INR (international normalized ratio).")

q("insom", "A nurse on a night shift wants to help a hospitalized client sleep. Which actions are appropriate? " + SATA,
  ["*Cluster care to limit interruptions",
   "*Dim the lights and reduce hallway noise",
   "Keep the overhead light on all night || Light should be managed to promote sleep",
   "*Ask about moving nonessential overnight meds",
   "Offer coffee with the evening snack || Caffeine should be limited later in the day"],
  "Hospitalized: cluster care, manage noise and light, reduce interruptions, and ask to move nonessential overnight med times. Limit caffeine later in the day.")

q("zolp", "A client taking zolpidem asks whether a glass of wine at bedtime is all right on nights it doesn't seem to work. Which response is best?",
  ["'One glass is fine if you take a smaller dose.' || Never take zolpidem with alcohol",
   "'Add an over-the-counter sleep aid instead.' || Never combine with other sleep medicines",
   "*'Never take it with alcohol or other sleep medicines.'",
   "'Take it after dinner so it has more time to work.' || Take it immediately before bed"],
  "Zolpidem: take immediately before bed (rapid onset), plan at least 7 hours of sleep, never with alcohol or other sleep meds. Complex sleep behaviors are a boxed warning.")

q("melat", "An 82-year-old hospitalized client asks for something to help with sleep. The provider orders melatonin. Which rationale best supports this choice?",
  ["It has a boxed warning that guides its use || Melatonin has no boxed warning in the lecture",
   "*It carries lower confusion and fall risk in older adults",
   "It should be started at a high nightly dose || Start low at 1 mg and titrate up",
   "It is a controlled drug that works fastest || It is OTC (over-the-counter) and non-habit-forming"],
  "Melatonin: OTC, non-habit-forming, cost-effective, lower confusion and fall risk in older adults. Take 30 minutes before bed; start 1 mg and titrate up.")

q("narco", "A 24-year-old client describes sudden sleep attacks during the day. Which additional report would most strongly support narcolepsy?",
  ["*'My knees buckle when I laugh hard at a joke.'",
   "'My legs crawl at bedtime until I get up.' || That describes restless legs syndrome",
   "'My partner says I snore loudly all night.' || Snoring suggests obstructive sleep apnea",
   "'I lie awake for hours before falling asleep.' || That describes insomnia"],
  "Narcolepsy: extreme daytime drowsiness plus involuntary sleep attacks regardless of prior sleep; onset usually ages 15-30. Cataplexy is emotion-triggered loss of muscle tone seen with narcolepsy.")

q("narcotx", "A nurse teaches a client newly diagnosed with narcolepsy. Which client statements show correct understanding? " + SATA,
  ["*'I'll plan short naps at set times during the day.'",
   "*'I'll keep the same sleep schedule every day.'",
   "'A drink at night will help me sleep better.' || Avoid alcohol and nicotine",
   "*'I'll exercise on a regular basis.'",
   "'I'll stay up late on weekends to catch up.' || Keep a consistent sleep schedule"],
  "Narcolepsy teaching: keep a sleep schedule, take scheduled naps, avoid alcohol and nicotine, exercise regularly. First-line drugs are modafinil or armodafinil.")

q("osa", "Which client should the nurse identify as having the MOST risk factors for obstructive sleep apnea?",
  ["A 25-year-old woman who sleeps on her side || Side-lying sleep treats mild OSA (obstructive sleep apnea)",
   "*A 60-year-old obese man who drinks alcohol nightly",
   "A 30-year-old runner with a 14-inch neck || Neck over 17 inches is the risk",
   "A 22-year-old nonsmoker of normal weight || This client has no listed risks"],
  "OSA (obstructive sleep apnea) risks: obesity, older age, male sex, neck over 17 inches, smoking/alcohol, airway abnormalities, supine sleep.")

q("dx", "A provider wants to know whether a client's sleep apnea is obstructive or central. Which test does the nurse expect to be ordered?",
  ["Home sleep apnea test (HSAT) || HSAT cannot distinguish OSA (obstructive sleep apnea) from CSA (central sleep apnea)",
   "*In-lab polysomnography (PSG)",
   "Overnight pulse oximetry only || This was not described as able to distinguish types",
   "A two-week sleep journal || A journal cannot distinguish apnea types"],
  "PSG is the in-lab gold standard and distinguishes OSA from CSA. HSAT is portable, convenient and cheaper but slightly less accurate and cannot distinguish them.")

q("osatx", "An adult with moderate obstructive sleep apnea says the CPAP (continuous positive airway pressure) machine is too noisy and the mask hurts. Which nursing action is most appropriate?",
  ["Tell the client surgery is now the first choice || Surgery is secondary, after CPAP fails",
   "Suggest oxygen by nasal cannula instead || Oxygen is not the listed treatment",
   "*Explore a new mask fit, humidification and slow acclimation",
   "Advise using CPAP only on weekends || First-line CPAP is meant for regular use"],
  "CPAP is first-line for adult OSA (obstructive sleep apnea) regardless of severity, but adherence is poor (mask discomfort, noise). Troubleshoot fit, humidification and gradual acclimation; surgery is secondary.")

q("pedosa", "The parent of a 5-year-old with obstructive sleep apnea and large tonsils asks why the child isn't starting CPAP (continuous positive airway pressure) like his grandfather. Which response is accurate?",
  ["'Children use CPAP only after surgery fails first.' || Adenotonsillectomy is first-line in children",
   "*'Removing the tonsils and adenoids is first-line for children.'",
   "'Sleep apnea in children always goes away on its own.' || Treatment and follow-up are needed",
   "'A wake-promoting drug is the first step for children.' || Pediatric first-line is adenotonsillectomy"],
  "Pediatric OSA (obstructive sleep apnea) first-line is adenotonsillectomy; adult first-line is CPAP. After surgery, reinforce a follow-up sleep study.")

q("csa", "A client with heart failure has pauses in breathing during sleep. Which finding helps the nurse tell central sleep apnea from obstructive sleep apnea?",
  ["Loud snoring between pauses || Snoring suggests an obstructed airway (OSA)",
   "*Pauses in breathing effort with no snoring",
   "A neck circumference of 18 inches || This is an OSA (obstructive sleep apnea) risk",
   "Pauses only when sleeping on the back || Supine sleep is an OSA risk"],
  "CSA (central sleep apnea): the airway is open but the brain fails to signal breathing, so there are pauses in effort without snoring. Risks: opioids, HF (heart failure), stroke.")

q("pap", "A nurse compares CPAP (continuous positive airway pressure) with BiPAP (bilevel positive airway pressure). Which statements are accurate? " + SATA,
  ["*CPAP delivers one continuous pressure",
   "*BiPAP uses separate pressures for breathing in and out",
   "CPAP is the costlier, less portable device || BiPAP is more expensive; CPAP is portable",
   "*BiPAP is used for hypoventilation CSA (central sleep apnea)",
   "BiPAP is preferred for hyperventilation CSA || Hyperventilation CSA uses CPAP"],
  "CPAP: one continuous pressure, 4-20 cm H2O, portable; used for hyperventilation CSA. BiPAP: two pressures, 4-30, more expensive; used for hypoventilation CSA.")
