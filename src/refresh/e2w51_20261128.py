T = "e2w51"; SET = "20261128"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("svt", "A 34-year-old graphic designer has had several episodes of stable SVT over the past year despite medication. Which treatment should the nurse expect the provider to discuss for the recurrent episodes?",
  ["Unsynchronized defibrillation || Defibrillation is for pulseless rhythms",
   "*Ablation",
   "Atropine by IV push || Atropine treats symptomatic bradycardia, not SVT",
   "Transcutaneous pacing || Pacing is for heart block, not SVT"],
  "Stable SVT is treated with vagal maneuvers, then adenosine, then a beta blocker or calcium channel blocker; ablation is used if SVT is recurrent. Unstable SVT is treated with synchronized cardioversion.")

q("adeno", "Adenosine is ordered for a client in stable SVT. Which finding in the client's history should the nurse report to the provider before giving the dose?",
  ["A history of anxiety attacks || Anxiety is not a contraindication to adenosine",
   "Takes a medication for hypertension || Hypertension is not a contraindication to adenosine",
   "*Second-degree AV block on a prior strip",
   "Vagal maneuvers did not convert the SVT || Adenosine is the next step after failed vagal maneuvers"],
  "Adenosine is contraindicated in second- or third-degree AV block and is used with caution in asthma. In stable SVT, it is given after vagal maneuvers fail.")

q("cardiov", "The nurse is assisting with synchronized cardioversion for a client who has been on oxygen by nasal cannula. Which approach to the oxygen is correct?",
  ["Increase the oxygen flow just before the shock || Oxygen is not used during the shock because of fire risk",
   "Leave the oxygen running at the same rate || Oxygen during the shock is a fire risk",
   "*Remove it for the shock, then reapply it after",
   "Stop the oxygen and keep it off for the shift || Oxygen is applied again after the shock"],
  "No oxygen during the shock because of fire risk; apply it after. SYNC must be on so the shock is not delivered on the T wave.")

q("pvc", "The nurse watching a client's cardiac monitor sees two PVCs in a row, followed by a return to the client's normal rhythm. How should the nurse document this?",
  ["A run of ventricular tachycardia || Ventricular tachycardia is 3 or more PVCs in a row",
   "*A couplet",
   "Ventricular fibrillation || V-fib has no organized complexes and no cardiac output",
   "An isolated PVC || An isolated PVC is a single beat, not two in a row"],
  "A couplet is 2 PVCs in a row; 3 or more consecutive PVCs is ventricular tachycardia. Frequent or multifocal PVCs should be reported.")

q("vt", "A 61-year-old client in ventricular tachycardia has a pulse, is alert and has a blood pressure of 124/78. Which actions should the nurse anticipate? " + SATA,
  ["*Give IV amiodarone or lidocaine as ordered",
   "*Correct low potassium and magnesium levels",
   "*Obtain a 12-lead ECG",
   "*Prepare for possible cardioversion",
   "Deliver unsynchronized defibrillation now || Defibrillation is for a pulseless client",
   "Begin chest compressions right away || CPR is for a client without a pulse"],
  "The pulse decides the path in VT. Pulse and stable: amiodarone or lidocaine, correct potassium and magnesium, 12-lead and prepare for cardioversion. Pulse and unstable: synchronized cardioversion. No pulse: CPR and defibrillation.")

q("torsades", "The nurse is reviewing a rhythm strip with a new graduate. Which findings fit torsades de pointes? " + SATA,
  ["*Polymorphic ventricular tachycardia",
   "*QRS complexes that twist around the baseline",
   "*A prolonged QT interval",
   "A PR interval that lengthens until a QRS drops || This describes Wenckebach (second-degree type I)",
   "P waves and QRS complexes that march independently || This describes third-degree heart block"],
  "Torsades is polymorphic VT twisting around the baseline with a long QT. IV magnesium sulfate is first line even if magnesium is normal; if pulseless, use unsynchronized defibrillation.")

q("mag", "Fifteen minutes into an IV magnesium sulfate infusion, a client says, 'My face feels warm and flushed.' Deep tendon reflexes are unchanged from baseline. Which action by the nurse is best?",
  ["Stop the infusion and give calcium gluconate || Flushing is expected; decreased reflexes signal toxicity",
   "*Explain that flushing is expected and keep checking reflexes",
   "Speed up the pump so the dose finishes sooner || Flushing is expected and is no reason to change the rate",
   "Switch the infusion to gravity to ease the flush || Magnesium is never given by gravity"],
  "Flushing is expected with magnesium. Decreased deep tendon reflexes are the earliest sign of toxicity and should be reported; the antidote is calcium gluconate. Magnesium is diluted and run on a pump, never by gravity or routine IV push.")

q("arrest", "A nursing student reviews cardiac arrest rhythms with the nurse. Which statement by the student needs correction?",
  ["'V-fib is shockable, so we start CPR and defibrillate.' || Accurate; V-fib is treated with CPR and unsynchronized defibrillation",
   "*'Asystole is treated with an immediate defibrillation.'",
   "'PEA shows an organized rhythm, but there is no pulse.' || Accurate; PEA is an organized rhythm without a pulse",
   "'For PEA, we give CPR and epinephrine without a shock.' || Accurate; PEA is not shockable"],
  "Asystole is not shockable; it is treated with high-quality CPR, epinephrine and a search for reversible causes. PEA is an organized rhythm with no pulse and is also not shockable. V-fib is shockable: CPR plus unsynchronized defibrillation.")

q("avblock", "A client's rhythm strip shows dropped QRS complexes with a constant PR interval. Which nursing action is most appropriate?",
  ["Document it as a benign rhythm that needs no follow-up || Mobitz II can progress abruptly to complete heart block",
   "Expect atropine to fully correct the rhythm || Atropine is often ineffective for Mobitz II",
   "*Anticipate pacing and monitor closely for complete block",
   "Prepare to give a beta blocker to slow conduction || A beta blocker is not the treatment for this block"],
  "A dropped QRS with a constant PR is second-degree AV block type II (Mobitz II). It is more dangerous and can progress abruptly to complete heart block; anticipate pacing, since atropine is often ineffective.")

q("chb", "A 79-year-old client in third-degree heart block is lightheaded with a blood pressure of 80/46. Which actions should the nurse take? " + SATA,
  ["*Apply transcutaneous pacing pads",
   "*Give oxygen and make sure IV access is in place",
   "*Keep the client on the cardiac monitor",
   "*Notify the provider",
   "Wait to see if atropine works before pacing || Atropine must not delay pacing",
   "Walk the client to the chair to raise the BP || A hypotensive, dizzy client should not ambulate"],
  "Third-degree heart block is complete AV dissociation. Apply pacing pads and give oxygen, IV, monitoring and notify the provider; atropine must not delay pacing. A permanent pacemaker is definitive.")

q("atropine", "Thirty minutes after receiving atropine for symptomatic bradycardia, a client says, 'My mouth is so dry and my vision is blurry.' Which response by the nurse is accurate?",
  ["'This means the dose was too low to work.' || These are expected anticholinergic effects, not signs of underdosing",
   "*'These are expected effects of this medicine.'",
   "'These mean your heart rate is dropping again.' || Atropine raises the heart rate",
   "'These are signs of an allergy to the medicine.' || Dry mouth and blurred vision are expected anticholinergic effects"],
  "Atropine is anticholinergic: tachycardia, dry mouth, blurred vision, urinary retention and confusion in older adults. Use caution after MI because a higher heart rate increases oxygen demand.")

q("pacer", "A client with a new pacemaker has a pacer spike followed by a QRS complex on every beat, but the nurse cannot palpate a pulse that matches the paced rate. Which interpretation is correct?",
  ["Both electrical and mechanical capture are present || Mechanical capture requires a palpable pulse",
   "*Electrical capture is present without mechanical capture",
   "The spikes alone confirm the client is perfused || A spike does not prove perfusion",
   "The demand mode is working exactly as expected || No matching pulse means mechanical capture is absent"],
  "Electrical capture is a pacer spike followed by a complex. Mechanical capture is confirmed by a palpable pulse that matches the paced complexes.")

q("pacecare", "The nurse reviews discharge teaching with a client who had a permanent pacemaker placed 2 days ago. Which statement by the client shows understanding?",
  ["'I can reach over my head to my top shelf right away.' || Avoid raising the affected arm above the shoulder for 2-3 weeks",
   "'I can carry my 30-pound dog by next week.' || No lifting more than 10-15 lb for 2-3 weeks",
   "*'I'll keep strong magnets away from my generator.'",
   "'If I get hiccups that won't stop, it's normal.' || Persistent hiccups may mean the lead is pacing the diaphragm; report it"],
  "After a permanent pacemaker: carry the device ID card, avoid strong magnets over the generator, no lifting more than 10-15 lb or raising the arm above the shoulder for 2-3 weeks, call if the pulse is below the set rate, and report persistent hiccups. Microwaves are safe.")
