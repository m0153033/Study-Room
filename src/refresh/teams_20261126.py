T = "teams"; SET = "20261126"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("three", "A charge nurse on a surgical unit is orienting a new graduate nurse to the hospital's response teams. Which statement by the new graduate shows correct understanding?",
  ["'I call the ERT (Emergency Response Team) when one of my inpatients stops breathing.' || The ERT covers visitors and staff; an inpatient in arrest is a Code Blue",
   "'I call a Code Blue when a visitor feels dizzy and sits down in the lobby.' || A visitor who needs help is an ERT call, not a Code Blue",
   "*'I call the RRT (Rapid Response Team) when my patient is getting worse but still has a pulse.'",
   "'I wait to call the RRT until my patient has lost a pulse and stopped breathing.' || No pulse means Code Blue; the RRT is meant to prevent the arrest"],
  "RRT is for an inpatient getting worse, Code Blue is for an inpatient in arrest, and ERT is for a visitor or staff member who needs help. The RRT prevents the arrest; the Code Blue team treats it.")
q("three", "A nurse educator reviews scenarios with staff on a telemetry unit. Which scenarios are matched with the correct team? " + SATA,
  ["*An inpatient with new stridor who is still breathing: Rapid Response Team",
   "A visitor's daughter who faints at the bedside: Rapid Response Team || A visitor is not a patient, so the ERT (Emergency Response Team) responds",
   "*A housekeeper who collapses in the hallway: Emergency Response Team",
   "An awake inpatient with HR (heart rate) 140 and a pulse: Code Blue || A pulse and breathing with HR over 130 is a Rapid Response trigger",
   "*An inpatient found in bed with no pulse: Code Blue"],
  "Choose the team by who the person is and whether they have a pulse and are breathing. RRT (Rapid Response Team) = inpatient getting worse; Code Blue = arrest; ERT = visitor or staff member.")

q("rrtwhy", "The daughter of a 72-year-old client tells the night nurse her mother 'just doesn't seem right' tonight. Which statement about calling a Rapid Response is accurate?",
  ["Only the provider is allowed to activate the Rapid Response Team || Any staff member can call a Rapid Response",
   "Only the charge nurse may call the team for a patient on the unit || Any staff member can call a Rapid Response",
   "The team is called only after the patient's heart has stopped || That is a Code Blue; the Rapid Response Team works to prevent arrest",
   "*Any staff member can call, and many hospitals also let families call"],
  "Any staff member can call a Rapid Response, and many hospitals also let families call. The goal is to catch a patient getting worse early and prevent an arrest.")

q("rrttrig", "The nurse reviews vital signs for several clients on a medical unit. Which readings meet Rapid Response criteria? " + SATA,
  ["HR (heart rate) 58 || The trigger is HR under 40 or over 130",
   "*HR 134",
   "*RR (respiratory rate) 6",
   "O2 (oxygen) sat 95% on 2 L of oxygen || The trigger is O2 sat under 90% despite oxygen",
   "*Systolic BP (blood pressure) 84"],
  "Rapid Response vital sign triggers: HR under 40 or over 130, RR under 8 or over 28, SBP (systolic blood pressure) under 90, and O2 sat under 90% despite oxygen.")
q("rrttrig", "The nurse is assessing a 50-year-old teacher admitted with pneumonia. Which new finding should prompt the nurse to call the Rapid Response Team?",
  ["Long-standing dementia that is unchanged from admission || Neuro triggers are sudden or new changes",
   "*New wheezing with increased work of breathing",
   "Pain that is controlled by the ordered medicine || Controlled pain is not a Rapid Response trigger",
   "BP (blood pressure) of 98/62 with no other changes || Systolic BP is not under 90, so this alone is not a trigger"],
  "Breathing triggers include increased work of breathing, new wheezing, new stridor, bluish lips, using neck muscles to breathe and not being able to finish a sentence. Key words are sudden or new.")

q("rrtroles", "A nurse explains Rapid Response Team roles to a nursing student. Which statement by the nurse needs correction?",
  ["'The RRT (Rapid Response Team) nurse assesses and starts interventions.' || Accurate; this is the RRT nurse's role",
   "'The respiratory therapist manages the airway and oxygen.' || Accurate; this is the respiratory therapist's role",
   "*'The charge nurse is the one who writes the medication orders.'",
   "'The provider gives orders and evaluates the patient.' || Accurate; this is the provider's role"],
  "The charge nurse coordinates support and transfers; the provider gives orders and evaluates. The RRT nurse assesses and starts interventions, and the respiratory therapist handles airway and oxygen.")

q("cbwhen", "Which findings, on their own, mean the nurse should call a Code Blue rather than a Rapid Response? " + SATA,
  ["*No carotid pulse",
   "RR (respiratory rate) of 32 in an alert patient || Breathing with a pulse and RR over 28 is a Rapid Response trigger",
   "*Only gasping breaths",
   "A new seizure while breathing with a pulse || A new seizure with a pulse is a Rapid Response trigger",
   "*Not breathing"],
  "Call a Code Blue when the patient is unresponsive, has no pulse, is not breathing or is only gasping, or suddenly collapses. Code Blue = not breathing and/or no pulse.")
q("cbwhen", "A patient has no pulse. A nursing student says, 'He's gasping now and then, so he's still breathing and doesn't need a code.' Which response by the nurse is best?",
  ["'You're right; let's call the Rapid Response Team instead.' || No pulse means a Code Blue now",
   "'Let's count his breaths for a full minute before we act.' || Counting breaths delays CPR (cardiopulmonary resuscitation)",
   "'Put oxygen on him and recheck the pulse in five minutes.' || A patient with no pulse needs CPR and a Code Blue right away",
   "*'Gasping doesn't count as breathing; call a Code Blue and start CPR.'"],
  "Not breathing or only gasping, or no pulse, means a Code Blue. Agonal gasps don't count as breathing.")

q("cbsteps", "Which sequence matches the Code Blue steps taught in lecture?",
  ["Call, assign roles, get equipment, recognize, start BLS (Basic Life Support), ROSC (return of spontaneous circulation) or termination || Recognizing the arrest comes first",
   "*Recognize, call, start BLS, get equipment, assign roles, ROSC or termination",
   "Get equipment, recognize, start BLS, call, assign roles, ROSC or termination || Equipment comes after recognizing, calling and starting BLS",
   "Assign roles, call, recognize, start BLS, get equipment, ROSC or termination || Roles are assigned after BLS has started"],
  "Code Blue steps: recognize (tap and shout, check ABCs), call, start BLS, get equipment, assign roles, then ROSC or termination.")
q("cbsteps", "A float nurse on an oncology unit finds a patient unresponsive with no pulse. Which are correct ways to call the Code Blue? " + SATA,
  ["*Press the code button",
   "Send the provider a text message || Texting is not a correct way to call a code",
   "*Pull the code cord",
   "Yell 'Help!' without giving a location || The location must be stated clearly",
   "*Dial the emergency number and state the room and unit"],
  "Call a Code Blue by pressing the code button, pulling the cord or dialing the emergency number, and say the location clearly, such as 'Code Blue, Room 312, North Wing.'")

q("cpr", "The nurse is watching a coworker do chest compressions during a code. Which observation requires the nurse to step in?",
  ["The rate is about 110 compressions per minute || 100-120 per minute is correct",
   "The compressions are about 2 inches deep || 2 inches (5 cm) is correct",
   "*The compressor leans on the chest between compressions",
   "The compressor switches with the AED (automated external defibrillator)/monitor person at 2 minutes || Switching about every 2 minutes is correct"],
  "High-quality compressions are 100-120 per minute, 2 inches deep, with full chest recoil. Leaning on the chest prevents full recoil. Compressors switch about every 2 minutes (5 cycles).")

q("cbroles", "During a code on a cardiac unit, which team member is matched with the correct role?",
  ["Recorder: decides when to shock the patient || The team leader decides when to shock or give meds",
   "Primary RN (registered nurse): directs the code || The provider runs the code; the primary RN does compressions",
   "Respiratory therapist: gives the ACLS (Advanced Cardiovascular Life Support) medications || The respiratory therapist handles airway and rescue breaths",
   "*Security: crowd control"],
  "In the Code Blue table, security handles crowd control. The provider runs the code, the primary RN does compressions, the respiratory therapist handles airway and rescue breaths, and the recorder documents times.")

q("aha", "A new ICU (intensive care unit) nurse asks about position 2 on the AHA (American Heart Association) six-person team. Which statement by the nurse educator is accurate?",
  ["*'Position 2 runs the AED (automated external defibrillator)/monitor and is in the resuscitation triangle.'",
   "'Position 2 is in the leadership group with the recorder.' || The leadership group is the team leader, recorder and IV/IO/medications",
   "'Position 2 turns the monitor so only the team leader can see it.' || The monitor goes where the whole team can see it",
   "'Position 2 may leave the triangle once more help arrives.' || No one leaves the triangle except for their own safety"],
  "The resuscitation triangle is the compressor, the AED/monitor/defibrillator (position 2) and the airway. Place the monitor where the whole team can see it, and no one leaves except for their own safety.")
q("aha", "Which roles make up the leadership group of the AHA (American Heart Association) six-person resuscitation team? " + SATA,
  ["Compressor || The compressor is part of the resuscitation triangle",
   "*Team leader",
   "*Recorder",
   "Airway || The airway role is part of the resuscitation triangle",
   "*IV (intravenous)/IO (intraosseous)/medications"],
  "Leadership roles are the team leader, the recorder and IV/IO/medications. The resuscitation triangle is the compressor, AED (automated external defibrillator)/monitor/defibrillator and airway.")

q("comm", "Which statement by a new nurse shows correct understanding of closed-loop communication during a code?",
  ["'I just say okay so I don't slow the team down.' || Vague replies like 'okay' should be avoided",
   "*'I repeat the order back, confirm when it's done, and the leader acknowledges it.'",
   "'I give the drug without replying so the room stays quiet.' || Orders must be read back and confirmed",
   "'Closed-loop is only used when giving an SBAR (Situation, Background, Assessment, Recommendation) report.' || Closed-loop is used for orders during the code"],
  "In closed-loop communication the team member repeats the order, confirms when it is given, and the leader says 'Thank you.' Avoid vague replies like 'okay.'")
q("comm", "A nurse calling the Rapid Response Team says, 'I'd like the team to see him now; he may need to move to the ICU (intensive care unit).' Which part of SBAR (Situation, Background, Assessment, Recommendation) is this?",
  ["Situation || Situation is what is happening right now",
   "Background || Background is history and recent changes",
   "Assessment || Assessment is findings and vital signs",
   "*Recommendation"],
  "Recommendation is what you need done. Situation is what's happening now, Background is history and recent changes, and Assessment is findings and vital signs.")

q("debrief", "After a long code, a 30-year-old pharmacist who helped asks the nurse why the team is meeting to debrief. Which response is best?",
  ["'We find out who caused the delay so they can be written up.' || A debrief is not about blame",
   "'Only physicians attend the debrief, so you are free to go.' || Everyone involved, including pharmacists, should take part",
   "*'We review what worked and what to improve, and support each other.'",
   "'It is mainly done so the code can be billed correctly.' || Billing is not the purpose of a debrief"],
  "A debrief recognizes what worked, finds delays, miscommunication or equipment problems, improves team learning and safety, and acknowledges the emotional toll. Everyone involved should be included.")

q("ert", "A nurse walking into work sees a staff member collapse in the parking garage. Which actions fit the Emergency Response Team process? " + SATA,
  ["*Call the emergency number",
   "*Keep the area safe",
   "Call a Code Blue for an inpatient arrest || A staff member's emergency is an ERT (Emergency Response Team) call",
   "*State the emergency and location clearly",
   "Send the staff member straight to the ICU (intensive care unit) || The ER (emergency room) team decides whether the person needs the ED (emergency department)"],
  "For a visitor or staff member who faints, seizes, falls or looks ill, call the emergency number and keep the area safe. The ER team comes, intervenes and decides whether the person needs the ED.")

q("codes", "A nurse starting at a new hospital asks why she must learn this facility's emergency code chart. Which response is best?",
  ["'Every hospital uses the same colors, so it's only a quick review.' || Codes vary by hospital",
   "'Color codes are meant to alarm visitors so they leave quickly.' || Codes help avoid panicking patients and visitors",
   "'Codes are only used when a patient has a cardiac arrest.' || Code Red is fire and Code Black is a bomb threat",
   "*'Code colors vary by hospital, so follow this facility's protocol.'"],
  "Color codes share urgent information quickly and clearly and avoid panicking patients and visitors. Codes vary by hospital, so follow your facility's protocols.")

q("which", "A 55-year-old client after surgery suddenly has bluish lips and is using her neck muscles to breathe. She is awake and has a pulse. Which action by the nurse is best?",
  ["Call a Code Blue and start compressions || She is breathing and has a pulse, so this is not an arrest",
   "*Call the Rapid Response Team",
   "Call the Emergency Response Team || The ERT is for visitors and staff, not inpatients",
   "Raise the head of the bed and recheck in an hour || These breathing findings are triggers that need action now"],
  "Bluish lips and using neck muscles to breathe are Rapid Response breathing triggers. If the breathing or pulse stops, it becomes a Code Blue.")
q("which", "The nurse is caring for four inpatients. Which client needs a Code Blue rather than a Rapid Response?",
  ["A client who is alert with an RR (respiratory rate) of 32 || RR over 28 with a pulse is a Rapid Response trigger",
   "A client having a new seizure who is breathing with a pulse || A new seizure with a pulse is a Rapid Response trigger",
   "*A client who is unresponsive and has no pulse",
   "A dizzy client with a systolic BP (blood pressure) of 86 || SBP under 90 with a pulse is a Rapid Response trigger"],
  "Code Blue = no pulse and/or not breathing. A patient who is getting worse but still breathing with a pulse needs the Rapid Response Team.")

q("which2", "A pharmacist working in the hospital's outpatient pharmacy becomes short of breath and looks ill. Which team should be called?",
  ["Rapid Response Team || The Rapid Response Team is for inpatients getting worse",
   "Code Blue || She is breathing with a pulse and is not an inpatient",
   "*Emergency Response Team",
   "Code Red || Code Red means fire"],
  "The ERT (Emergency Response Team) responds to visitors, staff and others who faint, seize, fall, look ill or become short of breath.")
q("which2", "Which situations are matched with the correct code or team? " + SATA,
  ["*Smoke coming from a supply closet: Code Red",
   "An inpatient with sudden new confusion: Code Blue || New confusion with a pulse is a Rapid Response trigger",
   "*A caller reports a bomb in the building: Code Black",
   "A fire in the cafeteria kitchen: Code Black || Fire is Code Red",
   "*A visitor having a seizure in the elevator: Emergency Response Team"],
  "Code Red = fire, Code Black = bomb threat, Code Blue = arrest. RRT (Rapid Response Team) = inpatient getting worse; ERT = visitors and staff. Follow your facility's chart.")
