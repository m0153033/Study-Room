T = "e3w91"; SET = "20261125"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("delvsdem", "The nurse plans care for a client with long-standing dementia and no new changes. Which nursing priority fits?",
  ["Identify and treat the acute trigger || That is the delirium priority",
   "*Support function, routine, safety and caregivers",
   "Expect full reversal once a cause is found || Dementia is chronic and progressive",
   "Order an urgent workup for infection || A sudden change would prompt this, not stable dementia"],
  "Delirium priority: find and treat the cause, keep the client safe. Dementia priority: support function, routine, safety and caregivers.")

q("deltypes", "Four older adults are on a surgical unit. Whose delirium is MOST likely to be overlooked?",
  ["A client yelling and pulling at the IV || Hyperactive delirium draws attention",
   "A client trying to climb out of bed || Hyperactive delirium draws attention",
   "A client switching between agitation and lethargy || Mixed delirium includes noticeable agitation",
   "*A client who is quiet, slow and withdrawn"],
  "Hypoactive delirium (quiet, withdrawn, lethargic, slow) is easily missed, so the trigger can go untreated.")

q("delcause", "A 79-year-old client becomes confused on day 2 after hip surgery. Which should the nurse check for possible delirium triggers? " + SATA,
  ["*Blood glucose",
   "*Oxygen saturation",
   "*Date of the last bowel movement",
   "*Medication list for opioids or anticholinergics",
   "Shoe size and height || Not related to delirium triggers"],
  "Triggers: infection, meds (anticholinergics, opioids, psychoactives), dehydration/electrolytes, hypoglycemia, hypoxia, surgery/anesthesia, constipation/impaction, poor sleep, relocation.")

q("cam", "A client is fully alert but has had confusion since yesterday that comes and goes, cannot follow a conversation, and speaks in rambling, illogical ideas. What is the CAM result?",
  ["Negative; the client is alert || Alertness isn't required to be altered if thinking is disorganized",
   "*Positive; features 1, 2 and 3 are present",
   "Negative; hallucinations are required || Hallucinations are not a CAM feature",
   "Positive; feature 1 alone is enough || Features 1 and 2 are both required"],
  "CAM positive = feature 1 (acute onset/fluctuating) + feature 2 (inattention) + either feature 3 (disorganized thinking) or 4 (altered LOC).")

q("delcare", "The daughter of a client with delirium from dehydration asks how she can help. Which statement shows correct understanding?",
  ["'I should firmly correct him each time he's wrong.' || Arguing with the client is not helpful",
   "'He'll be like this permanently, so I should plan memory care.' || Delirium is often reversible",
   "*'Staying with him and calmly reassuring him can help.'",
   "'I should keep the lights off and remove the clock.' || Reorientation and a calm, safe space help"],
  "Delirium care: treat the cause, prevent injury, provide a calm, safe environment, reorient, and support and reassure the family.")

q("adover", "Which statement correctly compares early-onset and late-onset Alzheimer's disease?",
  ["Early onset begins after 65 and is more common || Late onset is after 65 and more common",
   "Both types start before age 40 || Early onset is at or before 65",
   "*Early onset is at or before 65 and less common; late onset is after 65",
   "Late onset is reversible; early onset is not || Alzheimer's is irreversible"],
  "Early onset: at or before 65 (less common). Late onset: after 65 (more common).")

q("adstage", "The spouse of a client in the early stage of Alzheimer's asks what changes to expect in the middle stage. Which response is accurate?",
  ["'Your husband will lose all speech and be bedbound.' || That describes the late stage",
   "'He'll only misplace things now and then.' || That describes the early stage",
   "'His memory will steadily improve over time.' || Alzheimer's is progressive",
   "*'He may begin wandering and need help with daily activities.'"],
  "Middle: disorientation, impaired finances, language changes, agitation, wandering, sundowning, possible incontinence, ADL help needed.")

q("addx", "A client with suspected Alzheimer's is scheduled for brain imaging. The family asks what the scan will show. Which response is accurate?",
  ["'The scan will confirm Alzheimer's right away.' || Alzheimer's is confirmed at autopsy",
   "*'Imaging helps rule out other causes of the symptoms.'",
   "'The scan replaces the need for any memory testing.' || Clinical assessment such as MMSE is still used",
   "'The scan measures the MMSE score.' || MMSE is a cognitive screening tool, not imaging"],
  "Alzheimer's is diagnosed on clinical grounds and confirmed by autopsy; imaging helps rule out other causes.")

q("nonpharm", "A client with Alzheimer's keeps asking where her husband is. He died several years ago. Which response by the nurse is best?",
  ["'Your husband died years ago; you know that.' || Don't argue or confront; redirect instead",
   "'He'll be here to visit you this afternoon.' || Reinforces a false belief",
   "*'You miss him. Tell me how the two of you met.'",
   "'Stop asking; you're just confused today.' || Dismissive; acknowledge feelings instead"],
  "Validation: acknowledge feelings without arguing or reinforcing false beliefs; redirect, using preserved long-term memories.")

q("nonpharm", "A family plans to bring a client with moderate Alzheimer's to a holiday gathering. Which tips should the nurse give? " + SATA,
  ["*Plan quiet breaks in a calm room",
   "*Keep the usual daily routine as much as possible",
   "Offer several choices at once to keep the client engaged || Give one simple step at a time",
   "*Use a calm voice and short, direct statements",
   "Explain logically why the client should calm down || Redirect rather than confront"],
  "Limit overstimulation with quiet breaks, keep a predictable routine, use a calm voice and short statements, and redirect rather than confront.")

q("safety", "During a home visit, which statement by the caregiver of a client with Alzheimer's needs follow-up?",
  ["'We added nightlights in the hallway and bathroom.' || Correct fall prevention",
   "'We put in door alarms in case he tries to leave.' || Correct safety measure",
   "*'We put small throw rugs down to cushion any falls.'",
   "'We keep a current photo of him in case he wanders.' || Correct wandering plan"],
  "Falls/injury: remove small rugs, minimize clutter, nightlights, smoke alarms, safety devices and alarm systems. Safety is one of the most important interventions.")

q("safety", "The daughter caring for her father with Alzheimer's needs to travel for a few days and feels guilty leaving him. Which resource should the nurse suggest?",
  ["Lock him in his room with meals left out || Unsafe; supervision is needed",
   "*Respite care",
   "Ask him to stay home alone with a GPS device || Tracking devices aren't foolproof; supervision is needed",
   "Cancel the trip and manage all care alone || Caregiver strain should be prevented with support"],
  "Family support: Alzheimer's Association, day care, respite, case management, memory care, assisted living/LTC. Watch for caregiver stress.")

q("other", "Which pairing of dementia type and feature is correct?",
  ["Vascular — personality and language change first || That is frontotemporal",
   "Lewy body — autosomal dominant inheritance || That is Huntington",
   "Frontotemporal — reduced cerebral blood flow and TIAs || That is vascular",
   "*Prion disease — includes Creutzfeldt–Jakob disease"],
  "Vascular: reduced blood flow/TIAs. Lewy body: hallucinations, REM sleep problems, parkinsonism. Frontotemporal: personality/behavior/language. Huntington: autosomal dominant. Prion: Creutzfeldt–Jakob.")
