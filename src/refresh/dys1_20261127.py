T = "dys1"; SET = "20261127"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("grid", "A nurse on a step-down unit counts 11 QRS complexes on a client's 6-second rhythm strip. Which heart rate should the nurse document?",
  ["66 bpm || That multiplies by 6; the 6-second method multiplies by 10",
   "*110 bpm",
   "11 bpm || The count must be multiplied by 10",
   "55 bpm || That halves the correct rate; multiply the count by 10"],
  "6-second method: count the QRS complexes on a 6-second strip (30 large boxes x 0.20 sec) and multiply by 10.")

q("waves", "A nursing student measures a client's QRS complex at 0.14 second. Which interpretation is correct?",
  ["It is normal because the QRS is 0.12 to 0.20 second || 0.12-0.20 second is the normal PR interval, not the QRS",
   "It reflects normal atrial depolarization || Atrial depolarization is the P wave",
   "*It is wide, since a normal QRS is 0.06 to 0.10 second",
   "It shows the normal AV delay that lets ventricles fill || The AV delay is reflected in the PR interval"],
  "The QRS represents ventricular depolarization; normal is 0.06-0.10 second (narrow) and >0.12 second is wide. The PR (0.12-0.20 sec, constant) reflects the AV delay.")

q("blocks", "A telemetry nurse reviews four strips. Which finding should the nurse recognize as the MORE serious PR pattern?",
  ["PR of 0.24 second on every beat, no dropped beats || This is 1st-degree block: PR >0.20 but steady",
   "PR lengthening each beat until one QRS drops || This is Mobitz I (Wenckebach), the less serious pattern",
   "*PR fixed at 0.18 second, then a QRS suddenly drops",
   "PR of 0.16 second on every beat with a P before each QRS || This is a normal PR interval"],
  "Mobitz II has a fixed PR with a sudden dropped beat and is the more serious pattern. Mobitz I shows progressive PR lengthening before a dropped beat; 1st degree has a PR >0.20 that stays steady.")

q("wide", "A 47-year-old construction worker on telemetry suddenly shows a very fast rhythm with wide QRS complexes. Which action should the nurse take FIRST?",
  ["Treat it as sinus tachycardia and start IV fluids || A fast, wide rhythm is treated as V-tach until clarified",
   "Assume artifact and wait for the rhythm to settle || Treat it as V-tach until clarified",
   "*Assess the client's perfusion",
   "Document the rhythm and recheck it in an hour || This delays care for possible V-tach"],
  "A very fast, wide-QRS rhythm is treated as ventricular tachycardia until clarified: assess perfusion, call rapid response/ACLS, get a 12-lead ECG and check electrolytes.")

q("stt", "A 58-year-old teacher reports chest discomfort, and the monitor shows new ST elevation. Which statement by the nurse reflects correct thinking?",
  ["'ST elevation is always an MI, so no other cause applies.' || Pericarditis can also alter the ST",
   "'This is most likely low potassium; I'll check a level tomorrow.' || New ST elevation with symptoms needs immediate action",
   "'I'll recheck the strip at the end of my shift.' || This needs immediate assessment and escalation",
   "*'I'll treat this as an MI until it is ruled out.'"],
  "New ST elevation with symptoms is treated as MI (myocardial infarction) until ruled out: assess immediately, alert the provider, get a STAT 12-lead ECG and troponins, and likely call a rapid response. ST elevation isn't always MI; pericarditis can alter the ST too.")

q("qt", "A 39-year-old client with nausea has a QTc of 510 ms and a low magnesium level. Ondansetron is ordered. What should the nurse do?",
  ["Give the ondansetron because nausea is the priority || Ondansetron is QT-prolonging",
   "*Hold the ondansetron and notify the provider",
   "Give ondansetron with acetaminophen to offset it || Acetaminophen does not counter QT prolongation",
   "Give the ondansetron; QTc is high only above 600 ms || QTc >500 ms is prolonged/high risk"],
  "QTc >500 ms is prolonged/high risk for torsades de pointes/V-tach. Avoid QT-prolonging drugs such as ondansetron, replace low potassium and magnesium and use continuous telemetry. Assess the ECG/QTc before starting a QT-prolonging medication.")

q("qt", "The nurse reviews QTc results for several clients. Which results are within the practical target? " + SATA,
  ["*A man with a QTc of 430 ms",
   "*A woman with a QTc of 460 ms",
   "A man with a QTc of 465 ms || The practical target for men is <450 ms",
   "A woman with a QTc of 505 ms || Above 500 ms is prolonged/high risk",
   "*A woman with a QTc of 440 ms"],
  "The practical QTc target is <450 ms for men and <470 ms for women. QTc >500 ms is prolonged/high risk for torsades.")

q("tele", "A nurse is applying 5-lead telemetry to a 66-year-old client. Where should the nurse place the GREEN (RL) electrode?",
  ["Below the right clavicle || That is the white (RA) electrode",
   "Lower left torso below the ribs || That is the red (LL) electrode",
   "*Lower right torso below the ribs",
   "4th intercostal space, right sternal border || That is the brown (V1) electrode"],
  "White (RA) below the right clavicle, black (LA) below the left clavicle, red (LL) lower left torso, green (RL) lower right torso, brown (V1) 4th ICS right sternal border. Snow (white) over grass (green).")

q("tele", "A charge nurse checks a client's 5-lead telemetry. Which finding shows an electrode that needs to be moved?",
  ["White electrode just below the right clavicle || This is correct RA placement",
   "*Red electrode just below the left clavicle",
   "Brown electrode at the 4th ICS, right sternal border || This is correct V1 placement",
   "Green electrode on the lower right torso below the ribs || This is correct RL placement"],
  "Smoke (black) over fire (red): black (LA) goes below the left clavicle and red (LL) goes on the lower left torso below the ribs. Limb leads go on the torso.")

q("teletech", "A nurse prepares to place telemetry electrodes on a 45-year-old client with a hairy chest who just applied body lotion. Which action is correct?",
  ["Shave the chest so the electrodes stick firmly || Clip hair rather than shave",
   "Place the electrodes over the sternum and ribs for stability || Avoid bony areas",
   "Leave the lotion on to protect the skin || Lotion reduces adhesion",
   "*Clip the hair, then clean and dry the skin"],
  "Electrode technique: clip hair rather than shave, clean and dry the skin, place electrodes below or lateral to breast tissue, and change them daily or when loose or sweaty. Lotion, sweat and oil reduce adhesion.")

q("sinus", "A 34-year-old client with hyperthyroidism has a regular rhythm at 122 with an upright P before every QRS. The client asks why a fast rate matters. Which response is correct?",
  ["'A faster rate gives the heart more time to fill.' || A faster rate shortens diastole",
   "*'A fast rate shortens filling, so less blood is pumped.'",
   "'A fast rate raises the amount pumped with each beat.' || Less filling lowers output",
   "'Heart rate has no effect on how much blood is pumped.' || Persistent tachycardia lowers output"],
  "This is sinus tachycardia; hyperthyroidism is a cause. A faster rate shortens diastole, so there is less filling and lower output/perfusion. Treat the cause and assess perfusion.")

q("brady", "A 70-year-old client has a HR of 40, is confused and reports chest pain. Which medication should the nurse anticipate?",
  ["Magnesium || Magnesium is first-line for torsades",
   "Metoprolol || Metoprolol is a rate-slowing drug",
   "*Atropine",
   "Diltiazem || Diltiazem slows the heart further"],
  "Treat the patient, not the number. Confusion and chest pain make this bradycardia symptomatic, and atropine treats symptomatic bradycardia.")

q("brady", "A 52-year-old client with sleep apnea has a HR of 52, warm pink skin and alert mentation, and denies dizziness. Which action is best?",
  ["Give atropine to bring the rate above 60 || Atropine is for symptomatic bradycardia",
   "*Continue to monitor the client",
   "Call a rapid response for the low rate || An asymptomatic client does not need escalation",
   "Prepare the client for a pacemaker || There are no symptoms to treat"],
  "Treat the patient, not the number. Sleep apnea can cause sinus bradycardia; asymptomatic bradycardia may need nothing. Dizziness, syncope, confusion, chest pain or sweating make it symptomatic.")

q("afib", "A 68-year-old retired chef with AFib asks why no chest pain means no stroke risk. Which response is correct?",
  ["'Right, without symptoms your stroke risk is gone.' || AFib can clot regardless of symptoms",
   "'AFib always causes chest pain, so you are not in AFib.' || AFib can be asymptomatic",
   "*'AFib can occur without symptoms and still carry stroke risk.'",
   "'A controlled rate under 100 removes your stroke risk.' || A controlled rate does not remove stroke risk"],
  "AFib is the most common treated arrhythmia and can be asymptomatic. A controlled rate does not mean no stroke risk; blood stagnates in the LAA and can clot regardless of symptoms.")

q("afib", "A 59-year-old client is recovering from cardiac surgery. Why is this client at increased risk for AFib?",
  ["Surgery permanently slows the sinus node || This is not a stated mechanism",
   "*Manipulation and inflammation irritate atrial pathways",
   "Surgery stops the AV node from conducting impulses || This is not the stated mechanism",
   "Anesthesia causes repeated oxygen drops overnight || Repeated oxygen drops describe sleep apnea"],
  "Cardiac surgery irritates atrial pathways through manipulation and inflammation. Other AFib risk factors include sleep apnea, hyperthyroidism, excessive alcohol, hypertension, diabetes, heart failure and smoking.")

q("afibdx", "A 64-year-old client with AFib is scheduled for cardioversion. A TEE is done first. Which client statement shows understanding?",
  ["'It records my heart rhythm at home for three days.' || That describes a Holter monitor",
   "'It measures my QT interval before the shock.' || The ECG measures the QTc",
   "'It places a device that closes part of my heart.' || That describes the Watchman",
   "*'It checks for a clot that could cause a stroke.'"],
  "A TEE looks closely for an atrial thrombus before cardioversion, because restoring contraction could dislodge a clot and cause an embolic stroke. Holter records at home for 24-72 hours.")

q("laa", "A client with AFib asks where most AFib-related strokes come from. Which response by the nurse is correct?",
  ["'From plaque that breaks off in the carotid artery.' || Most come from LAA clots",
   "'From clots that form in the right ventricle.' || Clots form in the left atrial appendage",
   "*'From clots that form in the left atrial appendage.'",
   "'From bleeding caused by a fast heart rate.' || AFib strokes are ischemic"],
  "90-95% of AFib-related strokes originate from clots in the left atrial appendage: atrial quiver causes blood to pool in the LAA, a clot forms and travels to the brain, causing ischemic stroke.")

q("laa", "A 72-year-old client with AFib and no symptoms says, 'I feel fine, so I don't need my blood thinner.' Which response is best?",
  ["'You're right; it's only needed when you have symptoms.' || Clots can form regardless of symptoms",
   "'Your blood thinner is mainly to slow your heart rate.' || Anticoagulants do not control the rate",
   "'Your blood thinner will convert your rhythm to normal.' || Anticoagulants do not convert the rhythm",
   "*'Blood can still pool and clot without any symptoms.'"],
  "Anticoagulation is central in AFib even without symptoms because blood stagnates in the LAA and can clot regardless of symptoms. Prescribers use the CHA2DS2-VASc score to guide anticoagulation.")

q("valv", "A 66-year-old client with AFib has a bioprosthetic valve. Which oral anticoagulant type should the nurse expect?",
  ["Warfarin only, because any valve makes AFib valvular || Bioprosthetic valves are nonvalvular AFib",
   "*A DOAC such as apixaban",
   "IV heparin as long-term home therapy || Heparin is acute/bridge therapy only",
   "No anticoagulant because the valve is tissue || Nonvalvular AFib still needs clot prevention"],
  "Nonvalvular AFib includes bioprosthetic valves and mild/moderate regurgitation, and a DOAC is preferred. Valvular AFib (moderate-to-severe mitral stenosis or a mechanical valve) requires warfarin only.")

q("valv", "A nurse reviews orders for a client with AFib and a mechanical heart valve. Which order should the nurse question?",
  ["Warfarin with routine PT/INR checks || Warfarin is indicated for a mechanical valve",
   "*Rivaroxaban by mouth daily",
   "IV heparin as a bridge until warfarin takes effect || Heparin is used acutely or as a bridge",
   "A higher INR target than usual || The INR target is higher for a mechanical valve"],
  "Valvular AFib (moderate-to-severe mitral stenosis or a mechanical valve) requires warfarin only, so a DOAC such as rivaroxaban should be questioned. The warfarin INR target is higher for a mechanical valve.")

q("goals", "A nurse sorts the AFib medications for a 70-year-old client by management goal. Which pairing is correct?",
  ["Diltiazem: prevent clots and stroke || Diltiazem controls the rate",
   "Apixaban: control or restore the rhythm || Apixaban prevents clots",
   "*Metoprolol: control the ventricular rate",
   "Amiodarone: prevent clots and stroke || Amiodarone controls the rhythm"],
  "Three AFib goals: prevent clots/stroke (heparin, warfarin, DOACs, Watchman), control the rate (metoprolol, diltiazem), and control or restore the rhythm (amiodarone, ablation).")

q("proc", "A client asks how long after a Watchman procedure they may be able to stop their anticoagulant. Which response is correct?",
  ["'You can stop it the same day as the procedure.' || Clients may stop about 30-60 days after",
   "*'Often about 30 to 60 days after the procedure.'",
   "'You will need it for life no matter what.' || The Watchman may allow stopping anticoagulants",
   "'Only after a second ablation is done.' || Ablation is a separate procedure"],
  "The Watchman closes off the left atrial appendage clot source; clients may stop anticoagulants about 30-60 days after. It is used for clients with AFib who can't take anticoagulants.")

q("amio", "A 61-year-old client takes amiodarone and digoxin together. What should the nurse anticipate?",
  ["Weaker digoxin effect and a faster pulse || Amiodarone increases digoxin effects",
   "*Stronger digoxin effect and slower heart rate",
   "No interaction between the two drugs || Amiodarone increases digoxin effects",
   "A faster heart rate and shorter QT || Amiodarone slows the rate and prolongs the QT"],
  "Amiodarone increases warfarin and digoxin effects; combined with AV-node drugs (metoprolol, diltiazem, digoxin) it worsens bradycardia and heart block.")

q("amio", "Which ECG changes should the nurse expect from amiodarone's action? " + SATA,
  ["*Prolonged QT interval",
   "*Prolonged PR interval",
   "*Slower sinus rate",
   "Shortened QT interval || Amiodarone prolongs repolarization and the QT",
   "Faster AV conduction || Amiodarone slows AV conduction"],
  "Amiodarone blocks potassium channels, prolonging repolarization and the QT. It also slows sinus rate and AV conduction (prolongs PR).")

q("amioteach", "A client on oral amiodarone for 4 months has yellowing skin and extreme fatigue. What should the nurse tell the client?",
  ["'Stop the drug right away and wait to feel better.' || Don't stop amiodarone abruptly",
   "'These are expected and do not need to be reported.' || Jaundice and extreme fatigue should be reported",
   "*'Report these now; your liver tests need checking.'",
   "'Wear sunscreen and these will resolve.' || Sunscreen addresses photosensitivity, not jaundice"],
  "Teach clients on amiodarone to report vision changes, jaundice or extreme fatigue and not to stop the drug abruptly. Liver and thyroid function tests are part of baseline and periodic monitoring.")

q("heparin", "A nurse is about to start a heparin infusion for a 63-year-old client. Which action is required before starting?",
  ["Give the first dose by gravity drip || Heparin needs an infusion pump",
   "*Have another RN do an independent double-check",
   "Draw the first aPTT one week after starting || Repeat aPTT 6 hours after starting",
   "Skip baseline labs since heparin is short-acting || Baseline aPTT, PT/INR and CBC are needed"],
  "Heparin is high-alert: use an infusion pump, an independent double-check by another RN, baseline aPTT, PT/INR and CBC, and repeat aPTT 6 hours after starting or any rate change.")

q("heparin", "A client on IV heparin for AFib asks, 'Is this medicine dissolving the clot in my heart?' Which response is correct?",
  ["'Yes, it breaks up clots that are already there.' || Heparin doesn't dissolve existing clots",
   "'No, it mainly works by slowing your heart rate.' || Heparin does not control the rate",
   "*'No, it prevents new clots and stops clots from growing.'",
   "'Yes, and it will also convert your rhythm.' || Heparin doesn't convert the rhythm"],
  "IV heparin prevents new clots and clot extension but doesn't dissolve existing clots. It boosts antithrombin, which inactivates thrombin (IIa) and factor Xa.")

q("oral", "A 77-year-old client on warfarin has an INR far above target and serious bleeding. Which reversal agents should the nurse anticipate? " + SATA,
  ["*Vitamin K",
   "*PCC",
   "*FFP",
   "Protamine sulfate || Protamine reverses heparin",
   "Andexanet alfa || Andexanet alfa reverses factor Xa inhibitors"],
  "Vitamin K reverses warfarin; PCC or FFP (fresh frozen plasma) is used for serious bleeding. Protamine reverses heparin and andexanet alfa reverses apixaban/rivaroxaban.")

q("oral", "A 48-year-old client with end-stage renal disease on dialysis has new AFib. The provider considers apixaban. What should the nurse recognize?",
  ["Apixaban is preferred because no routine labs are needed || No routine labs doesn't mean no risk",
   "Apixaban is safe because it is reversed by vitamin K || Andexanet alfa reverses apixaban",
   "*DOACs aren't recommended for ESRD on dialysis",
   "Apixaban requires weekly INR checks in dialysis || DOACs don't need routine INR checks"],
  "DOACs (direct oral anticoagulants) aren't recommended for end-stage renal disease on dialysis. No routine lab doesn't mean no risk; kidney function is checked. Andexanet alfa reverses factor Xa inhibitors.")

q("rate", "A 55-year-old client with COPD and AFib needs rate control. Which statement by the nurse is correct?",
  ["*'Metoprolol needs caution because bronchospasm can occur.'",
   "'Diltiazem should be avoided because it causes bronchospasm.' || Bronchospasm is a metoprolol caution",
   "'Metoprolol is fully safe because it is beta-1 selective.' || Beta-1 selectivity is dose-dependent",
   "'Either drug will convert the AFib to sinus rhythm.' || Rate-control drugs don't convert AFib"],
  "Metoprolol is a beta-1 selective blocker, but selectivity is dose-dependent, so use caution in asthma/COPD because bronchospasm can occur. Both metoprolol and diltiazem control the rate without converting the rhythm.")

q("rate", "The nurse teaches a client starting diltiazem for AFib. Which client statement indicates a need for more teaching?",
  ["'I'll avoid grapefruit juice while on this drug.' || Correct diltiazem teaching",
   "'I'll report any swelling in my legs or feet.' || Correct diltiazem teaching",
   "'I'll get up slowly from sitting or lying down.' || Correct teaching; rise slowly",
   "*'If I feel fine, I can stop it whenever I want.'"],
  "Diltiazem teaching: avoid grapefruit juice, report leg or foot swelling, take consistently with regard to food, check HR and BP, rise slowly and don't stop abruptly (rebound tachycardia/hypertension).")

q("flutter", "A 69-year-old client in atrial flutter has sawtooth waves and a ventricular rate of about 150. Why is the ventricular rate slower than the atrial rate?",
  ["The SA node fires more slowly than normal || Flutter is an atrial reentry circuit",
   "*The AV node can't conduct every flutter impulse",
   "The ventricles are fibrillating independently || The ventricles follow conducted impulses",
   "Heparin is slowing the ventricular rate || Heparin does not control the rate"],
  "Atrial flutter is an organized reentry circuit at about 250-350/min. The AV node can't conduct every impulse; the conduction ratio (such as 2:1, about 150) sets the ventricular rate.")

q("team", "A client with AFib needs a pacemaker and is also being considered for cardioversion. Which team member performs these procedures?",
  ["Case manager or social worker || They help with access and logistics",
   "Pharmacist || The pharmacist focuses on doses and interactions",
   "*Electrophysiologist",
   "Respiratory therapist || This is not their role"],
  "The electrophysiologist is the heart's 'electrician' and does ablation, cardioversion, pacemakers and ICDs.")
