T = "e2w51"; SET = "20261124"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("svt", "A 27-year-old client in stable SVT at 190 bpm is alert with a normal blood pressure. Vagal maneuvers did not convert the rhythm. Which intervention does the nurse anticipate next?",
  ["Synchronized cardioversion || Cardioversion is for unstable SVT",
   "*Adenosine by rapid IV push",
   "Unsynchronized defibrillation || Defibrillation is for pulseless rhythms",
   "Atropine by IV push || Atropine treats bradycardia, not SVT"],
  "Stable SVT: vagal maneuvers, then adenosine, then a beta blocker or calcium channel blocker; ablation if recurrent. Unstable SVT is treated with synchronized cardioversion.")

q("adeno", "The nurse is preparing to give adenosine to a client with stable SVT. Which actions are correct? " + SATA,
  ["*Use the IV port closest to the client",
   "Push the dose slowly over 2 minutes || Half-life is under 10 seconds; push rapidly",
   "*Follow immediately with a 20 mL normal saline flush",
   "*Warn the client about flushing, chest pressure or a sense of doom",
   "*Elevate the arm after the flush"],
  "Adenosine has a half-life under 10 seconds: rapid push at the closest port, immediate 20 mL normal saline flush, and elevate the extremity. Warn the client about flushing, chest pressure and impending doom; a brief pause is expected.")

q("cardiov", "A 66-year-old client with atrial fibrillation is scheduled for synchronized cardioversion. Which actions should the nurse take before the procedure? " + SATA,
  ["*Confirm that informed consent is signed",
   "*Verify the client's anticoagulation status",
   "Keep oxygen flowing at the bedside during the shock || Oxygen is removed during the shock due to fire risk",
   "*Record a baseline rhythm strip",
   "Turn the SYNC mode off to avoid a delay || SYNC must be on to avoid shocking on the T wave"],
  "Before cardioversion: consent, verify anticoagulation with AFib, baseline rhythm and emergency equipment. SYNC avoids shocking on the T wave. No oxygen during the shock; apply it after.")

q("pvc", "A 76-year-old client taking digoxin develops frequent PVCs on the monitor. Which possible cause should the nurse consider first?",
  ["Elevated magnesium level || Low, not high, magnesium causes PVCs",
   "Elevated potassium level || Low, not high, potassium causes PVCs",
   "*Digoxin toxicity",
   "Excess oxygen in the blood || Hypoxia, not excess oxygen, causes PVCs"],
  "PVC causes include low potassium or magnesium, hypoxia or ischemia, stimulants and digoxin toxicity. Frequent or multifocal PVCs should be reported.")

q("vt", "A 58-year-old client in ventricular tachycardia has a pulse, BP 76/44 and new confusion. Which intervention does the nurse anticipate?",
  ["Unsynchronized defibrillation || Defibrillation is for pulseless VT",
   "IV amiodarone only, then observe || Drug therapy alone is for stable VT with a pulse",
   "Start chest compressions || CPR is for a client without a pulse",
   "*Synchronized cardioversion"],
  "The pulse decides the path in VT. No pulse: CPR and defibrillation. Pulse and unstable: synchronized cardioversion. Pulse and stable: amiodarone or lidocaine and correct potassium and magnesium.")

q("torsades", "A client with a prolonged QT develops torsades de pointes with a pulse. The magnesium level drawn an hour ago was normal, and IV magnesium sulfate is ordered. Which action by the nurse is best?",
  ["Hold the dose because the magnesium level is normal || Magnesium is given even if the level is normal",
   "*Give it; magnesium is first line even with a normal level",
   "Ask the provider to change the order to adenosine || Magnesium, not adenosine, is first line for torsades",
   "Prepare for synchronized cardioversion instead || Varying complexes in torsades can't be synchronized"],
  "Torsades is polymorphic VT twisting around the baseline with a long QT. IV magnesium sulfate is first line even if magnesium is normal. If pulseless, use unsynchronized defibrillation.")

q("mag", "The nurse is caring for a client receiving an IV magnesium sulfate infusion. Which actions are appropriate? " + SATA,
  ["*Run the diluted infusion on an IV pump",
   "Give the dose by routine IV push to work faster || Magnesium is never given by routine IV push",
   "*Monitor deep tendon reflexes during the infusion",
   "Hang it by gravity if a pump is not available || Magnesium is never run by gravity",
   "*Keep calcium gluconate available as the antidote"],
  "Magnesium is diluted and run on a pump, never by gravity or routine IV push. Decreased deep tendon reflexes are the earliest sign of toxicity; flushing is expected. The antidote is calcium gluconate.")

q("arrest", "The nurse responds to several emergencies on a cardiac unit. Which client situation calls for unsynchronized defibrillation?",
  ["Pulseless client with asystole confirmed in two leads || Asystole is not shockable; give CPR and epinephrine",
   "Pulseless client with an organized rhythm on the monitor || This is PEA, which is not shockable",
   "*Unresponsive, pulseless client in ventricular fibrillation",
   "Alert client in stable SVT at a rate of 180 bpm || Stable SVT starts with vagal maneuvers"],
  "V-fib has no cardiac output and is shockable: CPR and unsynchronized defibrillation. Asystole and PEA are not shockable: CPR, epinephrine and reversible causes.")

q("avblock", "The nurse reviews a rhythm strip in which the PR interval gets longer with each beat until a QRS is dropped, and then the pattern repeats. Which rhythm is this?",
  ["*Second-degree AV block type I (Wenckebach)",
   "Second-degree AV block type II (Mobitz II) || Mobitz II has a dropped QRS with a constant PR",
   "First-degree AV block || First-degree has a constant PR over 0.20 with no dropped QRS",
   "Third-degree AV block || In third-degree, P waves and QRS complexes are independent"],
  "Wenckebach: longer, longer, drop. Mobitz II drops a QRS with a constant PR and can progress abruptly to complete heart block. First-degree is a constant PR over 0.20 sec with every P followed by a QRS.")

q("chb", "A client with third-degree heart block asks the nurse which treatment will fix the problem long term. Which response by the nurse is accurate?",
  ["'Atropine will correct the block, so no other treatment is needed.' || Atropine is not definitive and must not delay pacing",
   "'A beta blocker will speed up your heart and restore normal rhythm.' || A beta blocker is not used for heart block",
   "'Adenosine will reconnect the upper and lower chambers of the heart.' || Adenosine is for SVT and is contraindicated in AV block",
   "*'A permanent pacemaker is the definitive treatment for this block.'"],
  "Third-degree heart block is complete AV dissociation. Apply pacing pads, oxygen, IV and monitoring and notify the provider; atropine must not delay pacing. A permanent pacemaker is definitive.")

q("atropine", "An 82-year-old client receives atropine for symptomatic bradycardia. Which finding should the nurse recognize as an expected anticholinergic effect?",
  ["Heart rate dropping to 42 bpm || Atropine causes tachycardia, not bradycardia",
   "*New confusion",
   "Frequent loose stools || Atropine is anticholinergic and does not cause diarrhea",
   "Excessive drooling || Atropine causes dry mouth"],
  "Atropine is anticholinergic: tachycardia, dry mouth, blurred vision, urinary retention and confusion in older adults. Use caution after MI because a higher heart rate increases oxygen demand.")

q("pacer", "A client has a demand pacemaker set at 60 bpm. The client's own heart rate is 80 bpm. What does the nurse expect to see on the monitor?",
  ["A pacer spike before every beat regardless of rate || That describes fixed-rate mode",
   "*Few or no paced beats while the rate stays above 60",
   "A shock delivered whenever the rate goes above 60 || A demand pacemaker paces; it does not shock",
   "A steady paced rate of exactly 80 bpm at all times || Demand mode fires only below the set rate"],
  "Demand mode senses intrinsic beats and fires only when the rate drops below the programmed rate; fixed-rate mode fires regardless. Electrical capture is a spike plus a complex; mechanical capture is a palpable pulse.")

q("pacecare", "The nurse is teaching a client who received a permanent pacemaker yesterday. Which statement by the client indicates a need for more teaching?",
  ["'I'll carry my pacemaker ID card with me at all times.' || Correct teaching",
   "'I'll call if my pulse is lower than my pacemaker's set rate.' || Correct teaching",
   "*'I'll lift my 25-pound grandson as soon as I get home.'",
   "'It's safe for me to keep using my microwave at home.' || Correct; microwaves and household appliances are safe"],
  "After a permanent pacemaker: carry the device ID card, no lifting more than 10-15 lb and no raising the affected arm above the shoulder for 2-3 weeks, call if the pulse is below the set rate, and avoid strong magnets over the generator. Microwaves are safe.")
