T = "dys1"; SET = "20261123"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("grid", "A nursing student is estimating a client's heart rate from a 6-second rhythm strip. After counting the QRS complexes, what should the student do next?",
  ["Multiply the count by 6 || The 6-second method multiplies by 10",
   "*Multiply the count by 10",
   "Divide the count by 30 large boxes || 30 large boxes is the length of the strip, not the formula",
   "Count the small squares instead || The 6-second method uses QRS complexes x 10"],
  "6-second method: count the QRS complexes on the strip and multiply by 10. A 6-second strip is 30 large boxes (30 x 0.20 sec).")

q("waves", "The monitor of a 67-year-old client shows an organized rhythm at a normal rate. Why should the nurse still assess the client's pulse and perfusion?",
  ["The ECG directly shows how strongly the heart muscle is squeezing || The ECG shows electrical activity, not the squeeze",
   "Mechanical contraction always happens before the electrical signal || Electrical activity comes first",
   "*Electrical activity comes first, so a strip alone doesn't prove perfusion",
   "Electrical and mechanical activity are the same event on the monitor || They are separate; always pair the strip with perfusion"],
  "Electrical activity comes before the mechanical squeeze. Always pair the strip with perfusion: treat the patient, not only the number.")

q("blocks", "Which rhythm strip description fits Mobitz II, the more serious PR pattern?",
  ["PR of 0.26 second on every beat with no dropped beats || That is 1st-degree AV block",
   "PR that gets longer each beat until a QRS is dropped || That is Mobitz I (Wenckebach)",
   "Sawtooth waves with no distinct P waves || That is atrial flutter",
   "*Fixed PR interval with a sudden dropped QRS"],
  "Mobitz II has a fixed PR with a sudden dropped beat and is the more serious pattern. Mobitz I lengthens progressively; 1st degree has a PR >0.20 but steady.")

q("wide", "A 64-year-old client on telemetry suddenly develops a very fast rhythm with QRS complexes over 0.12 second. Which actions should the nurse anticipate? " + SATA,
  ["*Assess the client's perfusion",
   "*Call a rapid response/ACLS team",
   "*Obtain a 12-lead ECG",
   "*Check electrolytes",
   "Treat it as sinus tachycardia and give fluids || A wide, fast rhythm is treated as V-tach until clarified"],
  "A very fast, wide-QRS rhythm is treated as ventricular tachycardia until clarified: assess perfusion, call rapid response/ACLS, get a 12-lead ECG and check electrolytes.")

q("stt", "Which pairing of ECG finding and possible cause is correct?",
  ["Tall, peaked T waves: hypokalemia || Tall peaked T waves suggest hyperkalemia",
   "Flat or inverted T waves: hyperkalemia || Flat/inverted T waves point to ischemia or hypokalemia",
   "*Tall, peaked T waves: hyperkalemia",
   "ST elevation: always a myocardial infarction || ST elevation isn't always MI; pericarditis can cause it"],
  "Tall/peaked T waves suggest hyperkalemia; flat or inverted T waves suggest ischemia or hypokalemia. ST elevation with symptoms is MI until ruled out, but pericarditis can also alter the ST.")

q("qt", "A 75-year-old client with a QTc of 530 ms who is receiving azithromycin develops torsades de pointes. Which medication should the nurse prepare first?",
  ["Atropine || Atropine treats symptomatic bradycardia",
   "Diltiazem || Diltiazem is a rate-control drug, not torsades treatment",
   "*Magnesium",
   "Heparin || Heparin is an anticoagulant"],
  "A prolonged QT (QTc >500 ms is high risk) can lead to torsades de pointes/V-tach. Azithromycin is a QT-prolonging drug. Magnesium is first-line for torsades.")

q("qt", "The nurse reviews the chart of a client with a prolonged QTc. Which factors can contribute to the prolonged QT? " + SATA,
  ["*Serum potassium below normal",
   "*Serum magnesium below normal",
   "*Bradycardia",
   "*Levofloxacin ordered for pneumonia",
   "Acetaminophen taken for a headache || Acetaminophen is not listed as a QT-prolonging drug"],
  "QT prolongation causes include low potassium, low magnesium, low calcium, congenital factors, bradycardia and medications such as azithromycin, levofloxacin/ciprofloxacin, ondansetron and antiarrhythmics like amiodarone.")

q("tele", "The nurse is teaching a new graduate to apply 5-lead telemetry. Which statement by the new graduate is correct?",
  ["'The four limb electrodes go on the wrists and ankles.' || The limb leads go on the torso, not the limbs",
   "*'Smoke over fire: black goes above red on the left side.'",
   "'White goes below the left clavicle, across from the black.' || White goes on the right, below the right clavicle",
   "'Snow over grass means green goes above white on the right.' || Snow over grass: white goes above green"],
  "White on right; smoke (black) over fire (red); snow (white) over grass (green). Black (LA) below left clavicle, red (LL) lower left torso, green (RL) lower right torso. Limb leads go on the torso.")

q("tele", "The nurse finds that the brown (V1) electrode on a client's 5-lead telemetry is placed at the 4th intercostal space, left sternal border. What should the nurse do?",
  ["Leave it, because V1 only grounds the system || V1 shows atrial activity; it is not just a ground",
   "Move it to just below the left clavicle || That is the black (LA) position",
   "*Move it to the 4th ICS, right sternal border",
   "Move it to the lower right torso below the ribs || That is the green (RL) position"],
  "Brown (V1) goes at the 4th ICS, right sternal border. V1 shows atrial activity and helps with AFib/flutter and wide-complex distinction.")

q("teletech", "An 80-year-old client's monitor alarms and shows a chaotic, bumpy tracing. The client is diaphoretic and the electrodes are peeling. What should the nurse do first?",
  ["Silence the alarm and replace the electrodes later || Always check the patient first",
   "Apply lotion to the skin so the electrodes stick better || Lotion reduces adhesion",
   "Shave the chest before reapplying the electrodes || Clip hair rather than shave",
   "*Check the client, then clean, dry and replace electrodes"],
  "Poor contact causes artifact, false alarms and unreliable tracings, but always check the patient first. Clip hair rather than shave, clean and dry the skin, and change electrodes when loose or sweaty.")

q("sinus", "A 26-year-old client 1 day after surgery rates pain 8/10. The monitor shows a regular rhythm at 118 with an upright P wave before every QRS. Which action is priority?",
  ["Give atropine and recheck the rhythm || Atropine is for symptomatic bradycardia",
   "*Treat the pain and assess perfusion",
   "Prepare the client for catheter ablation || Sinus tachycardia is managed by treating the cause",
   "Ignore it because the rhythm is regular || Persistent tachycardia lowers cardiac output; treat the cause"],
  "This is sinus tachycardia. Causes include pain, fever, hypovolemia, hyperthyroidism, anxiety, exertion and caffeine; treat the cause and assess perfusion. A faster rate shortens diastole and lowers output.")

q("brady", "The nurse is caring for four clients with sinus bradycardia. Which client should the nurse anticipate needing atropine?",
  ["A 24-year-old marathon runner with HR 48 who is alert and has no symptoms || Asymptomatic bradycardia in an athlete may need nothing",
   "A 55-year-old with HR 54, warm pink skin and alert mentation || No symptoms; continue to monitor",
   "*A 72-year-old with HR 42 who is confused, sweaty and reports chest pain",
   "A 60-year-old sleeping comfortably with HR 56 and no complaints || Asymptomatic bradycardia; monitor"],
  "Treat the patient, not the number. Symptomatic bradycardia (dizziness, syncope, confusion, chest pain, sweating) is treated with atropine.")

q("brady", "A 79-year-old client has HR 46 and reports dizziness. Diltiazem is due. Which actions should the nurse take? " + SATA,
  ["*Hold the diltiazem",
   "*Notify the ordering provider",
   "*Start fall precautions",
   "*Assess for confusion, chest pain or sweating",
   "Give the diltiazem because the blood pressure is normal || Rate-slowing drugs are held with symptomatic bradycardia"],
  "Rate-slowing drugs include beta blockers, calcium channel blockers, digoxin and amiodarone. With symptomatic bradycardia, hold the dose, notify the provider, start fall precautions and assess for symptoms; atropine treats symptomatic bradycardia.")

q("afib", "A 62-year-old client with hypertension and heavy alcohol use has a new irregular pulse. The strip shows an irregularly irregular rhythm with no distinct P waves. What does the nurse recognize?",
  ["Atrial flutter || Flutter shows regular sawtooth waves",
   "Mobitz I (Wenckebach) || Mobitz I shows a lengthening PR until a dropped beat",
   "*Atrial fibrillation",
   "Sinus tachycardia || Sinus tach is regular with a P before every QRS"],
  "AFib is irregularly irregular with no distinct P waves; hundreds of disorganized atrial impulses make the atria quiver. Hypertension and excessive alcohol are risk factors.")

q("afib", "A client's AFib rate increases from 88 to 140 and the client becomes more fatigued. Which explanation is correct?",
  ["*A rate over 100 shortens filling and lowers output further",
   "A faster rate increases filling time and raises cardiac output || Faster rate means less filling and lower output",
   "AFib is a ventricular rhythm, so a fast rate is harmless || AFib is an atrial rhythm and rapid rates lower output",
   "Once the rate is fast, the client has no further stroke risk || Stroke risk is present whether the rate is controlled or rapid"],
  "AFib may be controlled (<100) or rapid (>100); a rapid rate lowers output further because a faster rate means shorter diastole and less filling.")

q("afibdx", "Which pairing of AFib diagnostic test and its purpose is correct?",
  ["Holter monitor: real-time inpatient monitoring || Holter is outpatient; telemetry is inpatient real time",
   "TEE: measures the QTc || TEE looks closely for atrial thrombus",
   "*Echocardiogram: shows atrial size and function",
   "12-lead ECG: records the rhythm at home for 72 hours || That is a Holter monitor; the 12-lead confirms rhythm"],
  "The 12-lead confirms the rhythm; echo shows atrial size/function; TEE looks closer for thrombus before cardioversion; Holter records at home for 24-72 hours.")

q("laa", "A client newly diagnosed with AFib asks how an irregular heartbeat could cause a stroke. Which explanation by the nurse is correct?",
  ["'Clots form in the right ventricle and travel to the lungs.' || AFib strokes come from left atrial appendage clots",
   "'A fast heart rate causes bleeding into the brain from high pressure.' || AFib stroke is ischemic from clots, not bleeding",
   "'Plaque in the carotid artery breaks off because of the irregular rhythm.' || 90-95% originate from LAA clots",
   "*'Blood pools in the left atrial appendage, clots, and travels to the brain.'"],
  "Atrial quiver causes blood to pool in the left atrial appendage, where a clot forms and travels to the brain, causing ischemic stroke. 90-95% of AFib-related strokes originate there.")

q("laa", "While reviewing the chart of a client with AFib, the nurse sees a CHA2DS2-VASc score documented. What is the purpose of this score?",
  ["*To quantify stroke risk to guide anticoagulation",
   "To measure the client's level of consciousness || That is the Glasgow Coma Scale",
   "To calculate the client's corrected QT interval || The QTc comes from the ECG, not this score",
   "To decide whether the client needs a pacemaker || It guides anticoagulation, not pacing"],
  "Prescribers use the CHA2DS2-VASc score to quantify stroke risk and guide anticoagulation. Blood stagnates in the LAA and can clot regardless of symptoms.")

q("valv", "Which client with AFib would require warfarin rather than a DOAC (direct oral anticoagulant)?",
  ["A client with a bioprosthetic valve || Bioprosthetic valve is nonvalvular AFib; DOAC preferred",
   "A client with mild mitral regurgitation || Mild regurgitation is nonvalvular AFib",
   "*A client with severe mitral stenosis",
   "A client with moderate mitral regurgitation || Moderate regurgitation is nonvalvular AFib"],
  "Valvular AFib (moderate-to-severe mitral stenosis or a mechanical valve) requires warfarin only. Nonvalvular AFib includes bioprosthetic valves and mild/moderate regurgitation, where a DOAC is preferred.")

q("valv", "The nurse reviews several clients with AFib. Which clients have NONvalvular AFib? " + SATA,
  ["*A client with a bioprosthetic valve",
   "*A client with mild mitral regurgitation",
   "*A client with moderate mitral regurgitation",
   "A client with a mechanical heart valve || A mechanical valve is valvular AFib; warfarin only",
   "A client with moderate-to-severe mitral stenosis || This is valvular AFib; warfarin only"],
  "Nonvalvular AFib includes bioprosthetic valves and mild/moderate regurgitation. Valvular AFib is moderate-to-severe mitral stenosis or a mechanical valve. IV heparin is acute/bridge therapy only.")

q("goals", "Which interventions address the clot and stroke prevention goal of AFib management? " + SATA,
  ["*Heparin",
   "*Warfarin",
   "*Apixaban",
   "*Watchman device",
   "Diltiazem || Diltiazem controls the ventricular rate",
   "Amiodarone || Amiodarone controls the rhythm"],
  "Three AFib goals: prevent clots/stroke (heparin, warfarin, DOACs, Watchman), control the rate (metoprolol, diltiazem), and control or restore the rhythm (amiodarone, ablation).")

q("proc", "A client returned 2 hours ago from a catheter ablation using femoral access. Which finding should the nurse report immediately?",
  ["Strong pedal pulses in both feet || Normal distal neurovascular finding",
   "*A growing hematoma at the groin access site",
   "Telemetry showing a regular rhythm || Expected; continue monitoring",
   "The client asks for water while on bedrest || Not a complication"],
  "After femoral-access ablation or Watchman: monitor the groin for bleeding or hematoma, check distal neurovascular status, keep prescribed bedrest, monitor telemetry and assess for chest pain.")

q("amio", "A client has taken amiodarone for 8 months. Which findings should the nurse recognize as possible adverse effects? " + SATA,
  ["*A new dry cough and shortness of breath",
   "*Seeing halos around lights",
   "*Blue-gray skin on sun-exposed areas",
   "*Elevated liver enzymes",
   "Faster heart rate and shortened QT || Amiodarone causes bradycardia and QT prolongation"],
  "Amiodarone adverse effects: pulmonary toxicity (pneumonitis/fibrosis), thyroid dysfunction, elevated liver enzymes, corneal deposits and halos, photosensitivity and blue-gray skin, bradycardia and QT prolongation.")

q("amio", "A client on amiodarone develops hypothyroidism and asks why. Which explanation by the nurse is correct?",
  ["'Amiodarone blocks beta-1 receptors in the thyroid.' || Amiodarone mainly blocks potassium channels",
   "'It is caused by the drug's effect on factor Xa.' || Factor Xa inhibition is an anticoagulant action",
   "'This is from sun exposure while taking the drug.' || Sun causes photosensitivity and skin effects, not thyroid effects",
   "*'Amiodarone contains iodine, which affects the thyroid.'"],
  "Amiodarone contains iodine, which explains its hypo- or hyperthyroid effects. It blocks potassium channels, prolonging repolarization and the QT.")

q("amioteach", "The nurse teaches a client starting oral amiodarone. Which statement by the client indicates a need for more teaching?",
  ["'I'll take it at the same time every day.' || Correct teaching",
   "'I'll wear sunscreen and avoid too much sun.' || Correct; photosensitivity",
   "*'I can stop it on my own once my heartbeat feels normal.'",
   "'I'll report vision changes or yellowing of my skin.' || Correct; report vision changes and jaundice"],
  "Amiodarone teaching: take at the same time daily, avoid excess sun and wear sunscreen, report vision changes, jaundice or extreme fatigue, don't stop abruptly, and keep bloodwork and ECG follow-up.")

q("heparin", "The nurse changes the rate of a client's heparin infusion per protocol. When should the next aPTT be drawn?",
  ["In 24 hours || aPTT is repeated 6 hours after a rate change",
   "*6 hours after the rate change",
   "Only at the end of the week || Heparin requires close monitoring",
   "No aPTT is needed after a change || Each rate change requires a repeat aPTT"],
  "Heparin is high-alert: use an infusion pump, independent double-check, baseline aPTT, PT/INR and CBC, and repeat aPTT 6 hours after starting or any rate change. Target is usually 1.5-2 times control.")

q("heparin", "A client on a heparin infusion has bleeding gums and dark, tarry stools. The provider orders the heparin stopped and a reversal agent given. Which drug should the nurse prepare?",
  ["*Protamine sulfate",
   "Vitamin K || Vitamin K reverses warfarin",
   "Andexanet alfa || Andexanet alfa reverses factor Xa inhibitors such as apixaban",
   "Magnesium || Magnesium treats torsades"],
  "Protamine sulfate reverses heparin. Clients on heparin are taught to report dark or bloody stools and are on bleeding precautions.")

q("oral", "The nurse teaches a client starting warfarin. Which statement by the client indicates a need for more teaching?",
  ["'I'll get my PT/INR checked on schedule.' || Correct; warfarin needs routine PT/INR",
   "'I may need heparin for a few days until warfarin starts working.' || Correct; onset takes 3-5 days with possible bridging",
   "'I'll tell my dentist I take a blood thinner.' || Correct shared anticoagulant teaching",
   "*'I'll skip greens all week and then eat a big salad on weekends.'"],
  "Warfarin teaching: keep vitamin K intake (leafy greens) consistent, get routine PT/INR checks (usual target 2-3), expect onset in 3-5 days possibly with heparin bridging, and tell every provider and dentist about all meds.")

q("oral", "A client taking rivaroxaban is scheduled for a procedure with epidural anesthesia. Which boxed-warning risk should the nurse be concerned about?",
  ["Blue-gray skin discoloration || That is an amiodarone adverse effect",
   "*Spinal or epidural hematoma",
   "An INR rising well above 3 || INR monitoring is for warfarin",
   "Permanent hearing loss || Not the boxed warning for apixaban/rivaroxaban"],
  "The boxed warning for apixaban and rivaroxaban is spinal or epidural hematoma with neuraxial anesthesia or spinal puncture, which can cause long-term or permanent paralysis.")

q("rate", "A client taking diltiazem for AFib rate control reports swollen ankles and constipation. Which interpretation by the nurse is correct?",
  ["These are signs of masked hypoglycemia || Masking of hypoglycemia is a metoprolol effect",
   "These mean the drug converted the rhythm to sinus || Diltiazem controls rate but does not convert the rhythm",
   "*Known diltiazem effects; report the swelling",
   "These signal early bronchospasm from the drug || Bronchospasm is a metoprolol caution"],
  "Diltiazem-specific adverse effects include peripheral edema, constipation, headache and flushing; teach the client to report leg or foot swelling. It also causes hypotension, bradycardia and AV block.")

q("rate", "Which teaching applies to BOTH metoprolol and diltiazem? " + SATA,
  ["*Do not stop the drug abruptly",
   "*Check HR and BP; hold and notify if below parameters",
   "Take a double dose if the HR is high || Never double doses; check HR/BP and follow parameters",
   "*The drug controls the rate but does not convert AFib",
   "Watch for masked signs of low blood glucose || This is specific to metoprolol"],
  "Both control the ventricular rate without converting the rhythm. Both require HR/BP checks with holding below parameters and no abrupt stop (rebound tachycardia/HTN). Metoprolol specifically masks hypoglycemia signs.")

q("flutter", "A 58-year-old client with recurrent atrial flutter asks why the cardiologist recommends catheter ablation. Which response is best?",
  ["'It closes off the left atrial appendage where clots form.' || That describes the Watchman",
   "'It speeds up your heart rate so the flutter stops on its own.' || Ablation destroys abnormal tissue; it does not speed the heart",
   "'It thins your blood so clots can't form in the atria.' || Anticoagulants prevent clots; ablation targets the reentry focus",
   "*'The flutter circuit is usually in one spot, so success is high.'"],
  "Atrial flutter is an organized reentry circuit at about 250-350/min. Catheter ablation is often definitive because the reentry focus is usually localized.")

q("team", "A client starting warfarin and amiodarone has questions about doses and drug interactions. Which team member is best suited to provide this teaching?",
  ["Case manager || Case managers help with access, INR lab logistics and transportation",
   "*Pharmacist",
   "Electrophysiologist || The electrophysiologist does ablation, cardioversion and devices",
   "Interventional cardiologist || Not the team member focused on medication teaching"],
  "The pharmacist focuses on doses, interactions and adverse-effect teaching for anticoagulants and antiarrhythmics. The case manager/social worker helps with medication access and INR lab logistics; the electrophysiologist is the heart's 'electrician.'")
