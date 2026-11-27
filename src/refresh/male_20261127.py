T = "male"; SET = "20261127"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("defs", "A nursing student tells the clinical instructor, 'Sexual health is really just about whether the body works physically.' Which response by the instructor is accurate?",
  ["'It refers only to the absence of disease in the genitals.' || sexual health is broader than physical function",
   "*'It includes physical, emotional, mental and social well-being.'",
   "'It mainly applies to adults who are younger than age 70.' || sexuality has no age limit",
   "'It is defined the same way for every person you care for.' || its meaning differs from person to person"],
  "Sexual health is physical, emotional, mental and social well-being. Sexuality has no age limit and its meaning differs from person to person.")

q("physio", "A 31-year-old construction worker developed ED (erectile dysfunction) after a spinal cord injury that disrupted nerve signals to the penis. Using the 'spark + flow' model, how should the nurse classify this problem?",
  ["A 'flow' problem, meaning a vascular or perfusion cause || flow refers to blood supply, not nerve signals",
   "*A 'spark' problem, meaning a neurologic cause",
   "A psychogenic problem caused by performance anxiety || disrupted nerve signals are a physical cause",
   "A hormonal problem caused by low testosterone levels || the injury affects nerve signals, not hormones"],
  "An erection needs nerve signals ('spark') and adequate blood flow ('flow'). No spark = neurologic problem; spinal cord injury is a neurologic organic cause.")

q("incid", "A 46-year-old client is newly diagnosed with ED (erectile dysfunction). The nurse explains that ED can be an early warning sign of other conditions. Which conditions may ED flag? " + SATA,
  ["*Cardiovascular disease",
   "*Metabolic syndrome",
   "*Neurologic impairment",
   "Acute appendicitis || not a condition ED is described as flagging",
   "Seasonal allergies || not a condition ED is described as flagging"],
  "ED can be an early warning sign of cardiovascular disease because smaller penile arteries may show atherosclerosis before the coronary arteries. It can also flag metabolic syndrome or neurologic impairment.")

q("organic", "The nurse reviews the history of a 58-year-old long-haul truck driver with ED (erectile dysfunction). Which finding is a NEUROLOGIC organic cause?",
  ["*Multiple sclerosis diagnosed several years ago",
   "Hypertension managed with lifestyle changes || this is a vascular cause",
   "A beta blocker taken daily for heart rate || this is a medication cause",
   "Ongoing stress in his marriage at home || this is a psychogenic cause"],
  "Organic causes include vascular (hypertension), neurologic (multiple sclerosis, spinal cord injury), hormonal, medication (beta blockers), surgery/trauma and substance causes. Relationship stress is psychogenic.")

q("organic", "During an ED (erectile dysfunction) assessment, which client statement points to an ORGANIC contributor?",
  ["'I worry my partner will be disappointed in me.' || performance anxiety is psychogenic",
   "'I've been feeling down about how my body looks.' || negative body image is psychogenic",
   "*'I started a diuretic for my blood pressure recently.'",
   "'My partner and I have been arguing a lot lately.' || relationship problems are psychogenic"],
  "Medications are organic causes; antihypertensives such as diuretics and beta blockers, plus psychotropics, are the main medication causes. Anxiety, body image and relationship stress are psychogenic.")

q("psycho", "Which client is most likely to have psychogenic ED (erectile dysfunction)?",
  ["A 50-year-old with poorly controlled diabetes || diabetes is an organic cause",
   "A 62-year-old who had a prostatectomy last year || surgery is an organic cause",
   "*A 33-year-old with performance anxiety and no organic cause",
   "A 47-year-old who recently started an antipsychotic || medications are organic causes"],
  "Psychogenic causes include anxiety, depression, performance anxiety, negative body image and relationship stress. Organic causes must be ruled out first; psychogenic ED can occur with normal nerves and vessels.")

q("assess", "A 54-year-old bus mechanic comes to the clinic asking for 'a prescription for an ED pill.' Which nursing approach best reflects the lecture?",
  ["Focus the visit only on which ED drug he prefers || this misses the whole-person assessment",
   "*Use a holistic bio-psycho-social assessment approach",
   "Assume his partner's gender before asking questions || assess without assumptions or stigma",
   "Skip the medication history since ED isn't drug related || medications and substances must be reviewed"],
  "Use a holistic bio-psycho-social approach, not just a medication request. Review prescriptions, OTC (over-the-counter) drugs and substances, and assess the relationship and sexual context without assumptions or stigma.")

q("dx", "A client's penile Doppler ultrasound shows a poor arterial response after a vasoactive injection. How should the nurse interpret this result?",
  ["It points to a 'spark' problem with the nerves || Doppler measures arterial blood flow, not nerves",
   "It confirms the ED (erectile dysfunction) is psychogenic || a poor arterial response is a physical finding",
   "It shows his testosterone level is low || testosterone is measured with a blood test",
   "*It points to a 'flow' problem with blood supply"],
  "Penile Doppler ultrasound measures arterial blood flow after a vasoactive injection. Poor flow means a vascular/perfusion ('flow') problem.")

q("dx", "A nursing student describes the IIEF-5 (International Index of Erectile Function) questionnaire. Which statement by the student needs correction?",
  ["'It's used to rate how severe a client's ED (erectile dysfunction) is.' || this is accurate",
   "*'It reliably tells ED apart from premature ejaculation.'",
   "'It can't fully separate situational ED from global ED.' || this is an accurate limitation",
   "'It's a questionnaire, so no injection or blood draw is needed.' || this is accurate"],
  "The IIEF-5 is used for severity, but it can't fully separate situational from global ED or reliably separate ED from premature ejaculation.")

q("tx", "A 49-year-old client's ED (erectile dysfunction) is caused by low testosterone. He asks how hormone replacement can be given. Which routes may be prescribed? " + SATA,
  ["*Topical",
   "*Injection",
   "*Urethral",
   "Nitrate tablets || nitrates are not hormone replacement",
   "Vacuum suction || a vacuum device is not a hormone route"],
  "When ED is from low testosterone, treat the physical cause with hormone replacement as prescribed: topical, injection or urethral.")

q("pde5", "A 52-year-old accountant is prescribed avanafil and asks how the drug helps with ED (erectile dysfunction). Which explanation is accurate?",
  ["'It creates sexual desire, so no stimulation is needed.' || stimulation is still needed",
   "'It is injected into the side of the penile shaft.' || that describes alprostadil",
   "*'It relaxes penile smooth muscle to increase blood flow.'",
   "'It replaces low testosterone to restore erections.' || that describes hormone replacement"],
  "PDE-5 (phosphodiesterase-5) inhibitors relax penile smooth muscle to increase blood flow with sexual stimulation; they don't create arousal.")

q("pde5", "The nurse compares PDE-5 (phosphodiesterase-5) inhibitors for a group of clients. Which statement is accurate?",
  ["'Avanafil is the one that can be taken every day.' || tadalafil is the daily option",
   "'Vardenafil needs about a 2-hour lead-in time.' || vardenafil is taken about 1 hour before",
   "'Sildenafil works best when taken with a large meal.' || large meals should be avoided",
   "*'Tadalafil can be taken daily and may last up to 36 hours.'"],
  "Sildenafil, vardenafil and avanafil are taken about 1 hour before activity, avoiding large meals and alcohol. Tadalafil can be daily or as required with about a 2-hour lead-in and may last up to 36 hours.")

q("pde5safe", "A 70-year-old client taking tadalafil calls the after-hours line at 0300. He reports an erection that started 5 hours ago. What is the nurse's priority instruction?",
  ["'Take another dose to see if it settles down.' || more drug won't treat priapism",
   "*'Go for emergency care right away.'",
   "'This is an expected effect of vessel dilation.' || an erection over 4 hours is an emergency",
   "'Wait until morning and call your provider then.' || delay risks permanent tissue damage"],
  "An erection lasting more than 4 hours (priapism) is a medical emergency needing immediate care to prevent permanent tissue damage.")

q("pde5safe", "After teaching about sildenafil safety, which client statement shows correct understanding?",
  ["'Using poppers is fine if I wait an hour.' || never combine with poppers; severe hypotension can occur",
   "'I can take my angina nitrate if I use less.' || never combine with nitrates at any dose",
   "*'If I suddenly can't hear, I'll get emergency care.'",
   "'Sudden vision loss is a side effect to watch.' || sudden vision loss needs emergency care"],
  "Sudden hearing loss, sudden vision loss and an erection lasting more than 4 hours need emergency care. Never combine PDE-5 (phosphodiesterase-5) inhibitors with nitrates or poppers.")

q("vad", "A 66-year-old client is learning to use a vacuum assistive device. Which client statement shows correct understanding?",
  ["'The device works by injecting a medicine for me.' || it uses suction, not medication",
   "'I can leave the band on while I sleep tonight.' || prolonged use causes ischemia",
   "*'I'll take the band off within 30 minutes of use.'",
   "'The device will be placed during a surgery.' || it's noninvasive, not surgical"],
  "The vacuum device is noninvasive: suction draws blood into the penis and a band at the base maintains it. Remove the band within 30 minutes; longer use interrupts blood flow and can cause ischemia and permanent injury.")

q("vad", "A client new to a vacuum assistive device asks what keeps the erection once the suction draws blood into the penis. Which answer is correct?",
  ["A scrotal pump with a release valve || that's the inflatable implant",
   "*A constriction band at the base of the penis",
   "A medication injected into the penile shaft || that's alprostadil",
   "A malleable rod placed inside the penis || that's the semi-rigid implant"],
  "With a vacuum assistive device, suction draws blood into the penis and a band at the base maintains the erection.")

q("inject", "A 64-year-old retired pilot is learning intracavernosal alprostadil injection. Which statement shows correct understanding?",
  ["'I'll inject it into my abdomen like insulin.' || it's injected into the penile shaft",
   "'It will take about 2 hours before it works.' || it works in about 10 to 15 minutes",
   "'I'll inject at the 12 o'clock spot on top.' || use the 10 or 2 o'clock position",
   "*'It should start working in about 10 to 15 minutes.'"],
  "Intracavernosal alprostadil is injected into the penile shaft at the 10 o'clock or 2 o'clock position and works rapidly, in about 10 to 15 minutes.")

q("cbt", "A 36-year-old teacher has psychogenic ED (erectile dysfunction) after organic causes were ruled out. Which goal fits cognitive behavioral therapy?",
  ["Explore mainly early childhood events at length || CBT is present-focused",
   "*Build confidence and realistic expectations",
   "Prepare him for a semi-rigid rod implant || implants are for when less-invasive options fail",
   "Replace his testosterone to restore desire || that treats low testosterone, not psychogenic ED"],
  "CBT (cognitive behavioral therapy) recognizes distorted thoughts and unrealistic expectations, reframes thinking with a present-focused, problem-solving approach, and builds awareness, confidence and realistic expectations.")

q("nurse", "A nurse plans to ask a 72-year-old widower about his sexual function. Which nurse statement best reflects sensitive communication?",
  ["'Men your age usually stop caring about sex.' || sexuality has no age limit",
   "*'Would it be okay if we talked about sexual health?'",
   "'Let's go over this quickly here in the hallway.' || provide privacy",
   "'So, having trouble down there, buddy?' || use neutral language, not slang"],
  "Provide privacy, use neutral language, ask permission before discussing sexual function, and include a partner if the client wants. Sexuality has no age limit.")
