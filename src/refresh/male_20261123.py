T = "male"; SET = "20261123"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("defs", "A 44-year-old client says he couldn't maintain an erection one night after a very stressful week and asks if he has erectile dysfunction. Which response reflects the lecture definition?",
  ["'Yes; any single episode of not keeping an erection is ED.' || ED is persistent; one isolated episode isn't the definition",
   "*'ED is a persistent inability to get or keep a firm erection.'",
   "'ED means an erection that lasts longer than 4 hours at a time.' || that's priapism",
   "'ED means ejaculating sooner than you or your partner desire.' || that describes premature ejaculation"],
  "ED is a persistent inability to develop and/or maintain an erection firm enough for intercourse; one isolated episode doesn't meet the definition.")

q("physio", "Testing shows a client's ED (erectile dysfunction) is caused by poor blood flow to the penis. Which part of the 'spark + flow' model is affected?",
  ["The 'spark,' meaning a neurologic problem || spark refers to nerve signals",
   "Neither; this is a psychogenic cause || reduced blood flow is a physical cause",
   "*The 'flow,' meaning a vascular or perfusion problem",
   "Both are normal, so no erection problem exists || a flow problem impairs erections"],
  "An erection needs nerve signals ('spark') and adequate blood flow ('flow'). No spark = neurologic problem; no flow = vascular/perfusion problem.")

q("incid", "A 48-year-old client with new ED (erectile dysfunction) and no known heart disease asks why the nurse is recommending a cardiovascular checkup. Which explanation is best?",
  ["'ED itself causes heart disease, so we need to prevent it.' || ED doesn't cause heart disease",
   "'ED is only linked to heart disease in heart transplant clients.' || ED can flag heart disease in many clients",
   "'This is just a routine check and has nothing to do with ED.' || ED is linked to cardiovascular disease",
   "*'Penile arteries are small and may show atherosclerosis first.'"],
  "ED can be an early warning sign of cardiovascular disease because smaller penile arteries may show atherosclerosis before the coronary arteries. It can also flag metabolic syndrome.")

q("organic", "Which client's ED (erectile dysfunction) is most likely ORGANIC?",
  ["A 35-year-old with performance anxiety || performance anxiety is psychogenic",
   "*A 52-year-old with multiple sclerosis",
   "A 41-year-old with a negative body image || negative body image is psychogenic",
   "A 39-year-old with relationship stress || relationship problems are psychogenic"],
  "Organic causes include vascular, neurologic (multiple sclerosis, spinal cord injury), hormonal, medication, surgery/trauma and substance causes.")

q("organic", "A 63-year-old client with ED (erectile dysfunction) has hypertension treated with a beta blocker, had a prostatectomy last year and smokes. Which factors are organic contributors? " + SATA,
  ["*Hypertension",
   "*The beta blocker",
   "*The prostatectomy",
   "*Smoking",
   "Worry about letting his partner down || performance anxiety is psychogenic"],
  "Organic causes are vascular (hypertension), medications (beta blockers, diuretics, SSRIs, antipsychotics), surgery (prostatectomy, TURP) and substances (smoking).")

q("psycho", "A client's workup shows normal nerve and blood vessel function, yet he has ED (erectile dysfunction) during periods of depression. Which statement by the nurse is accurate?",
  ["*'Psychogenic ED can occur even with normal nerves and vessels.'",
   "'Normal test results mean the ED can't really be a problem.' || psychogenic ED is real ED",
   "'Depression is considered an organic cause of ED, like diabetes.' || depression is a psychogenic cause",
   "'You'll need a penile implant for this type of ED to improve.' || psychogenic ED is treated with CBT and counseling"],
  "Psychogenic causes (anxiety, depression, performance anxiety, negative body image, relationship stress) can cause ED even when nerves and vessels work normally, once organic causes are ruled out.")

q("assess", "Which topics should the nurse include when taking a sexual history from a client with ED (erectile dysfunction)? " + SATA,
  ["*Any penile curvature",
   "*History of genital or pelvic trauma",
   "*Mental-health history",
   "*Whether the concern is actually premature ejaculation",
   "The client's favorite sports team || not relevant to the sexual history"],
  "The symptom and sexual history includes onset, morning erections, pattern, desire, curvature, trauma, mental-health history and whether the concern is premature ejaculation.")

q("dx", "A provider wants to rate the severity of a client's ED (erectile dysfunction). Which tool does the nurse expect?",
  ["Penile Doppler ultrasound after a vasoactive injection || Doppler measures arterial blood flow",
   "Nocturnal penile tumescence test during sleep || this counts nighttime erections",
   "*IIEF-5 (International Index of Erectile Function)",
   "Serum testosterone level drawn in the morning || this checks for hypogonadism"],
  "The IIEF-5 is used to rate ED severity, though it can't fully separate situational from global ED or reliably separate ED from premature ejaculation.")

q("dx", "Which lab tests are part of an ED (erectile dysfunction) workup? " + SATA,
  ["*Serum testosterone drawn before 11 a.m.",
   "*Lipid panel",
   "*Glucose or HbA1c (hemoglobin A1c)",
   "*Urine testing",
   "Serum testosterone drawn at bedtime || testosterone is drawn in the morning"],
  "If hypogonadism is suspected, testosterone is drawn in the morning before 11 a.m. Other labs include lipids, glucose or HbA1c, and urine testing.")

q("tx", "A 56-year-old client with ED (erectile dysfunction), obesity and poorly controlled diabetes asks for 'just a pill.' Which part of the treatment framework comes first?",
  ["An inflatable penile implant placed right away || implants are used when less-invasive options are inadequate",
   "Cognitive behavioral therapy as the only treatment || CBT is for psychogenic ED",
   "*Lifestyle changes and chronic-disease control",
   "A vacuum device before any other approach || this isn't the first step for everyone"],
  "Lifestyle changes and chronic-disease control (weight loss, diet, smoking cessation, diabetes and heart health) come first, followed by a PDE-5 inhibitor with correct teaching for organic ED.")

q("pde5", "A client is prescribed tadalafil to take as needed. When should the nurse teach him to take it?",
  ["Right before activity || tadalafil needs a lead-in time",
   "*About 2 hours before activity",
   "Only after waking up in the morning || timing is tied to activity, not waking",
   "Three times daily with meals || it's taken daily or as needed, not three times a day"],
  "Tadalafil can be taken daily or as required with about a 2-hour lead-in, and it may last up to 36 hours.")

q("pde5", "The nurse teaches a client about PDE-5 (phosphodiesterase-5) inhibitors. Which client statement needs more teaching?",
  ["'I'll take my vardenafil about an hour before activity.' || correct: vardenafil is taken about 1 hour before",
   "'I'll still need sexual stimulation for the drug to work.' || correct: PDE-5 inhibitors need stimulation",
   "*'I'll take my sildenafil right after a big dinner with wine.'",
   "'I'll try it on at least 6 separate occasions before deciding.' || correct: try at least 6 separate occasions"],
  "Sildenafil is taken about 1 hour before activity, avoiding large meals and alcohol. Perceived failure is often an education failure.")

q("pde5safe", "A client taking sildenafil calls reporting sudden loss of vision in one eye. What should the nurse tell him?",
  ["'This is expected from blood-vessel dilation.' || expected effects are headache, flushing and congestion",
   "'Wait and see if it improves by tomorrow.' || this is an emergency warning",
   "'Take your next dose with food to prevent it.' || food doesn't address an emergency",
   "*'Seek emergency care right away.'"],
  "Sudden vision loss, sudden hearing loss and an erection lasting more than 4 hours are the three emergency warnings with PDE-5 inhibitors.")

q("pde5safe", "Before teaching about vardenafil, which items must the nurse screen for in the client's history? " + SATA,
  ["*Nitrate use, such as isosorbide for angina",
   "*Recreational 'poppers' use",
   "*Other vasodilating antihypertensives",
   "A daily multivitamin || not a listed PDE-5 safety concern",
   "Seasonal allergies || not a listed PDE-5 safety concern"],
  "Never combine PDE-5 inhibitors with nitrates or poppers (life-threatening hypotension); use caution with other vasodilating antihypertensives.")

q("vad", "A 68-year-old client takes a nitrate for angina and wants a noninvasive ED (erectile dysfunction) option without medication. Which option fits best?",
  ["Sildenafil || PDE-5 inhibitors are never combined with nitrates",
   "Inflatable penile implant || implants are surgical and irreversible",
   "*Vacuum assistive device",
   "Intracavernosal alprostadil || this is an injection, not noninvasive"],
  "The vacuum assistive device is noninvasive: suction draws blood into the penis and a band at the base maintains the erection.")

q("vad", "A client using a vacuum assistive device says he usually leaves the constriction band on for about an hour. What is the nurse's main concern?",
  ["The band will lose suction and stop working over time || the concern is blood flow, not suction",
   "*Interrupted blood flow causing ischemia and injury",
   "It can cause sudden hearing loss, like PDE-5 drugs || that's a PDE-5 warning",
   "The band will interact with his daily medications || the band is a mechanical device"],
  "The constriction band must be removed within 30 minutes; longer use interrupts blood flow and can cause ischemia and permanent injury.")

q("inject", "A client with an inflatable hydraulic penile implant asks how it works. Which description is accurate?",
  ["It's a malleable rod that keeps a permanent semi-erection || that's the semi-rigid implant",
   "It uses suction plus a constriction band at the base of the penis || that's the vacuum device",
   "It's a medicine injected into the side of the penile shaft || that's intracavernosal alprostadil",
   "*It uses an abdominal reservoir, scrotal pump and release valve"],
  "The inflatable implant uses an abdominal reservoir and a scrotal pump with a release valve; teaching includes activation and release.")

q("cbt", "A client starting cognitive behavioral therapy for psychogenic ED (erectile dysfunction) says, 'One session should fix this.' Which response is best?",
  ["'Yes, one session is usually all anyone needs to recover.' || several sessions may be needed",
   "*'Several sessions may be needed to change thought patterns.'",
   "'CBT only works if you also take a nitrate every day.' || nitrates aren't part of CBT",
   "'CBT is mainly about preparing you for a penile implant.' || CBT is a psychological therapy"],
  "CBT changes thinking and behavior patterns, recognizing distorted thoughts and reframing with a present-focused approach. Several sessions may be needed.")

q("nurse", "Which task is within the nurse's role in caring for a client with ED (erectile dysfunction)?",
  ["Leading CBT sessions for anxiety and depression || that's the psychologist or therapist",
   "*Screening for nitrate use before PDE-5 teaching",
   "Surgically placing a penile implant after failed medication || that's a surgical procedure",
   "Telling the client to stop his antihypertensive || the nurse supports adherence"],
  "The nurse handles sensitive assessment, teaching, safety screening, adherence support and referrals; the psychologist or therapist addresses anxiety, depression and CBT.")
