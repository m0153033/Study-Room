T = "cardinf"; SET = "20261127"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("risk", "A clinic nurse is screening several clients. Which clients have a listed risk factor for cardiac infection? " + SATA,
  ["*A 16-year-old who got a tongue piercing last week",
   "*A 30-year-old born with a congenital heart defect",
   "*A 52-year-old who had a dental procedure yesterday",
   "*A 44-year-old who has had a heart transplant",
   "A 25-year-old who sprained an ankle playing soccer || An ankle sprain is not a listed risk factor"],
  "Risk factors for cardiac infection include congenital defects, transplant, rheumatic fever, central lines, dental procedures, piercing, untreated strep, overcrowding, IV (intravenous) drug use, hemodialysis, pacemakers and valve replacements.")

q("labs", "A 48-year-old electrician is admitted with suspected endocarditis. Blood cultures and an IV (intravenous) antibiotic are both prescribed. What should the nurse do FIRST?",
  ["Give the antibiotic now and draw cultures after the dose || Cultures must be drawn before antimicrobials",
   "Draw one culture set from the existing IV line || Two sets from separate sites are needed",
   "*Draw two culture sets from separate sites before the antibiotic",
   "Hold all cultures until the client's fever resolves || Cultures are drawn before antibiotics, not after fever ends"],
  "For suspected endocarditis, blood cultures are drawn before antibiotics: 2 sets from separate sites about 12 hours apart.")

q("rfpath", "A 10-year-old is admitted with rheumatic carditis. Which findings does the nurse expect? " + SATA,
  ["*A murmur of mitral regurgitation",
   "*A prolonged PR interval on the ECG (electrocardiogram)",
   "*A friction rub with tachycardia",
   "Splinter hemorrhages under the nail beds || This is a sign of infective endocarditis",
   "*Fever with precordial pain"],
  "Primary findings of rheumatic fever include fever, tachycardia, precordial pain, friction rub, a murmur (often mitral regurgitation), prolonged PR and AFib (atrial fibrillation).")

q("jones", "A nursing student is reviewing the diagnosis of rheumatic fever. Which statement by the student needs correction?",
  ["'The E in the HEART mnemonic stands for an enlarged heart.' || This is correct",
   "*'The modified Jones criteria are used to diagnose endocarditis.'",
   "'A throat culture can provide evidence of a prior strep infection.' || This is correct",
   "'Prior strep plus 1 major and 2 minor criteria can confirm it.' || This is correct"],
  "The modified Jones criteria diagnose rheumatic fever; the modified Duke criteria diagnose infective endocarditis. Jones requires evidence of prior strep plus 2 major, or 1 major plus 2 minor.")

q("jones", "A nurse is reviewing a 13-year-old's chart for possible rheumatic fever. Which result provides evidence of a prior strep infection?",
  ["ASO (antistreptolysin O) titer of 120 IU || Positive evidence is a titer above 200 IU",
   "Positive blood cultures with a valve vegetation || This is central evidence for endocarditis",
   "Elevated troponin with a normal throat culture || Troponin does not show prior strep",
   "*ASO (antistreptolysin O) titer of 260 IU"],
  "Evidence of prior strep for the modified Jones criteria comes from a throat culture or an ASO (antistreptolysin O) titer above 200 IU.")

q("rftx", "A school nurse cares for a 9-year-old with a history of rheumatic fever who now reports a sore throat. What is the BEST action?",
  ["Offer throat lozenges and recheck in a few days || Every sore throat must be swabbed or cultured",
   "*Arrange for the child's throat to be swabbed or cultured",
   "Advise waiting 2 weeks before seeing a provider || Delay risks another immune response",
   "Tell the parent the child no longer needs follow-up || Prophylaxis and follow-up last years"],
  "The Sore Throat Rule: every sore throat must be swabbed or cultured. Teach the chain: throat infection, immune response, heart-valve damage.")

q("rftx", "An 11-year-old with acute rheumatic fever has severe carditis and heart failure. Which medication does the nurse expect for the inflammation?",
  ["*Prednisone",
   "An anticoagulant || Anticoagulants do not treat the inflammation",
   "Diltiazem || This is not a listed treatment for rheumatic carditis",
   "An antiviral || Rheumatic fever is an immune response to strep, not a virus"],
  "Acute inflammation of rheumatic carditis is treated with high-dose aspirin or an NSAID (nonsteroidal anti-inflammatory drug); prednisone is used if there is severe carditis or heart failure. Also rest, avoid strenuous activity, and gentle hydration if heart failure.")

q("iepath", "A nurse is reviewing clients' histories. Which factors increase the risk of infective endocarditis? " + SATA,
  ["*A prosthetic heart valve",
   "*Hemodialysis three times a week",
   "*Poor dental hygiene",
   "Regular aerobic exercise || Exercise is not a listed risk factor",
   "*A permanent pacemaker"],
  "IV (intravenous) drug use is the most common listed risk for infective endocarditis. Others: prosthetic valve, central line, hemodialysis, pacemaker and poor dental hygiene.")

q("iesigns", "While trimming the nails of a 70-year-old with infective endocarditis, the nurse notes thin reddish-brown lines under several nail beds. How should the nurse interpret this?",
  ["Roth spots caused by retinal bleeding || Roth spots are seen on an eye exam",
   "*Splinter hemorrhages from microemboli",
   "Osler nodes from an immune reaction || Osler nodes are painful finger-pad nodules",
   "Janeway lesions from vegetations || Janeway lesions are on the palms and soles"],
  "Splinter hemorrhages are thin reddish-brown lines under the nail beds and are a sign of microemboli in infective endocarditis.")

q("iesigns", "A nurse is performing a focused assessment for signs of infective endocarditis. Which actions are appropriate? " + SATA,
  ["*Inspect the conjunctiva for petechiae",
   "*Palpate the finger pads for tender nodules",
   "Inspect the trunk for erythema marginatum || This rash is a rheumatic fever finding",
   "*Inspect the palms and soles for painless spots",
   "*Inspect the nail beds for thin dark lines"],
  "IE (infective endocarditis) findings include petechiae on the conjunctiva or palms, Osler nodes (painful finger pads), Janeway lesions (painless palms/soles) and splinter hemorrhages (nail beds).")

q("duke", "A client with suspected infective endocarditis meets 5 minor modified Duke criteria and no major criteria. What does the nurse understand about this result?",
  ["At least 1 major criterion is always required || 5 minor criteria alone can confirm it",
   "*The diagnosis of endocarditis can be confirmed",
   "Only 2 minor criteria were needed for this || The threshold is 5 minor if no major",
   "The modified Jones criteria must now be used || Jones criteria are for rheumatic fever"],
  "The modified Duke criteria confirm infective endocarditis with 2 major, 1 major plus 3 minor, or 5 minor criteria.")

q("duke", "A 66-year-old client with an invasive line is evaluated for endocarditis. Which chart findings count as minor modified Duke criteria? " + SATA,
  ["*Temperature of 38.6°C (101.5°F)",
   "Temperature of 37.4°C (99.3°F) || Fever must be above 38°C (100.4°F)",
   "*Immunologic phenomena",
   "*Cultures that don't meet major criteria",
   "Diffuse concave ST elevation || This is an ECG finding of pericarditis"],
  "Minor Duke criteria: fever above 38°C (100.4°F), IV (intravenous) drug use or an invasive line, vascular or embolic phenomena, immunologic phenomena, and cultures that don't meet major criteria.")

q("iecomp", "A client with infective endocarditis has new ankle edema, a 2 kg weight gain and poor appetite. Which complication does the nurse suspect?",
  ["Left-sided heart failure || Left HF causes fatigue, SOB and crackles",
   "Splenic infarct || This causes abdominal pain radiating to the left shoulder",
   "*Right-sided heart failure",
   "Embolic stroke || This causes neuro changes such as slurred speech"],
  "Heart failure is the most common complication of IE (infective endocarditis). Right HF: edema, weight gain, anorexia. Left HF: fatigue, SOB (shortness of breath), crackles.")

q("iecomp", "A nurse is caring for a retired teacher with infective endocarditis. Which finding requires IMMEDIATE action?",
  ["Mild fatigue after walking in the hallway || Not an urgent change",
   "Small painless palm spots noted yesterday || Janeway lesions are expected IE signs",
   "Eating half of lunch due to poor appetite || Not an emergency finding",
   "*New facial droop with one-sided weakness"],
  "Vegetations can embolize and cause an embolic stroke, so frequent neuro checks are essential. Sepsis, heart failure and embolic events are the big threats.")

q("ietx", "A client is on day 8 of the correct IV (intravenous) antibiotics for infective endocarditis and still has fever and positive cultures. What does the nurse anticipate?",
  ["Stopping antibiotics since they have failed || IV therapy continues; surgery is evaluated",
   "*Evaluation for surgery on the infected valve",
   "Starting routine anticoagulation for the client || Routine anticoagulation is generally avoided",
   "Changing to a 3-day course of oral antibiotics || IV therapy lasts 4-6 weeks"],
  "Surgery indications include fever or positive cultures after 7 days of correct antibiotics, vegetation over 15 mm, severe regurgitation or pulmonary edema, and valvular abscess. Surgery is needed in nearly 50% of cases.")

q("ienurse", "A home health nurse is caring for a client receiving IV (intravenous) antibiotics through a PICC (peripherally inserted central catheter) line for endocarditis. Which action is essential?",
  ["Use clean technique when changing the dressing || PICC care must be sterile",
   "Encourage contact sports to rebuild stamina || This is not appropriate",
   "*Use sterile technique for all PICC line care",
   "Stop the antibiotics once the fever resolves || The full course must be completed"],
  "Nursing care for infective endocarditis includes sterile care of the PICC line, frequent neuro checks and cardiac auscultation for a new murmur.")

q("myo", "A 24-year-old warehouse worker had flu-like symptoms 2 weeks ago. Troponin is elevated and the ECG (electrocardiogram) looks like an MI (myocardial infarction), but there is no coronary blockage. Which condition is most likely?",
  ["Infective endocarditis || Hallmark is high fever with a new or changing murmur",
   "Rheumatic fever || Follows strep throat in ages 5-14",
   "*Myocarditis",
   "Constrictive pericarditis || Causes right-sided HF signs after repeated inflammation"],
  "Myocarditis is the 'great mimicker' because it can look like an MI without a coronary blockage. Viral causes include coxsackie B, adenovirus and COVID-19; young males are predisposed. Labs: elevated troponin, BNP, CRP and ESR.")

q("myotx", "A 19-year-old college basketball player is being discharged after myocarditis. Which statement shows understanding of the teaching?",
  ["'I can play again as soon as I feel better.' || Feeling better doesn't mean the muscle has healed",
   "'I'll start with full practices next week.' || Strenuous activity is avoided for 3-6 months",
   "*'I'll avoid strenuous activity for 3 to 6 months.'",
   "'Rest isn't needed since I'm young and fit.' || Strict rest prevents the 'sudden crash'"],
  "After myocarditis, avoid strenuous activity for 3-6 months; feeling better doesn't mean the muscle has healed. Strict rest prevents the 'sudden crash'.")

q("myotx", "A nurse is planning care for a client admitted with myocarditis. Which actions are appropriate? " + SATA,
  ["*Continuous telemetry monitoring",
   "*Daily weight",
   "*Strict intake and output",
   "Draw serial ASO (antistreptolysin O) titers || ASO titers are for rheumatic fever",
   "*Oxygen to keep SpO2 (oxygen saturation) above 94%"],
  "The nurse prevents the 'sudden crash' with continuous telemetry and hemodynamic monitoring, watching for SVT, V-tach, low MAP, low urine output and edema, with daily weight and strict I&O. Oxygen keeps SpO2 above 94%.")

q("peri", "A 38-year-old chef is admitted with acute pericarditis. Which pain description does the nurse expect?",
  ["*Sharp pain that radiates to the left trapezius",
   "Crushing pressure relieved by nitroglycerin || This pattern fits an MI",
   "Pain that improves when lying flat || Pericarditis pain is worse lying flat",
   "Painful nodules on the fingertips only || Osler nodes are an endocarditis sign"],
  "Pericarditis pain is sharp, pleuritic and positional; it radiates to the left trapezius and is relieved by sitting up and leaning forward.")

q("peri", "A client with acute pericarditis had diffuse concave ST elevation on admission. Days later, the ECG (electrocardiogram) shows T-wave inversion. How does the nurse interpret this?",
  ["It confirms a new localized MI (myocardial infarction) || Localized ST elevation suggests MI",
   "*It can be a late ECG change of pericarditis",
   "It is electrical alternans from tamponade || Alternans is beat-to-beat QRS variation",
   "It means the ECG is not useful here || ECG is the gold standard for pericarditis"],
  "The ECG is the gold standard for pericarditis: diffuse concave ST elevation with PR depression, and late T-wave inversion may follow.")

q("perimi", "A client in the emergency department has chest pain. Which findings favor MI (myocardial infarction) over pericarditis? " + SATA,
  ["*Crushing chest pressure",
   "*Relief with rest or nitroglycerin",
   "*ST elevation localized to a few leads",
   "A scratchy pericardial friction rub || This favors pericarditis",
   "*An S3 or S4 heart sound"],
  "MI: crushing pain, relief with nitroglycerin/rest, localized ST elevation, S3/S4. Pericarditis: sharp pleuritic pain, relief sitting up and leaning forward, diffuse ST elevation, friction rub.")

q("tamp", "A client asks why a pericardial effusion can become dangerous. Which explanation by the nurse is accurate?",
  ["'The fluid makes your valves grow infected growths.' || That describes endocarditis vegetations",
   "'The fluid turns the sac thick and stiff over years.' || That describes constrictive pericarditis",
   "*'If fluid compresses the heart, it can't fill properly.'",
   "'Any fluid around the heart is always an emergency.' || Effusion alone is fluid present"],
  "Effusion means fluid is present; tamponade means fluid compresses the heart and impairs filling.")

q("tamp", "The nurse receives report on four clients. Which client should the nurse see FIRST?",
  ["A client with pericarditis rating pain 3/10 while leaning forward || Expected and stable",
   "*A client with an effusion who has hypotension, JVD and muffled heart sounds",
   "A client with myocarditis with a stable weight for 3 days || Stable finding",
   "A client with endocarditis awaiting a PICC dressing change || Routine care"],
  "Hypotension, JVD (jugular vein distension) and muffled heart sounds are Beck's triad, which indicates cardiac tamponade and requires emergency pericardiocentesis.")

q("constrict", "A client with chronic constrictive pericarditis is scheduled for a pericardiectomy and asks what it will do. Which response is accurate?",
  ["'A needle will drain the fluid one time.' || That is pericardiocentesis",
   "'An opening will let fluid drain continuously.' || That is a pericardial window",
   "'Your damaged heart valve will be replaced.' || Valve replacement is not this procedure",
   "*'The scarred sac is removed so your heart can fill.'"],
  "In constrictive pericarditis the pericardium becomes thick and stiff like a corset. Pericardiectomy, the definitive treatment, removes the scarred sac so the heart can fill.")

q("peritx", "A nurse is assisting with a pericardiocentesis. Which complication should the nurse watch for during the procedure?",
  ["*Ventricular arrhythmias on the monitor",
   "Sydenham chorea || This is a rheumatic fever finding",
   "Hepatic engorgement || This is a constrictive pericarditis sign",
   "Janeway lesions on the palms || This is an endocarditis sign"],
  "Ventricular arrhythmias can occur during pericardiocentesis, so prepare a code cart, large-bore IV (16- or 18-gauge), continuous cardiac monitoring and oxygen to keep SpO2 above 94%.")

q("peritx", "A 55-year-old client returns from surgery after a pericardial window. Which actions belong in the post-op plan? " + SATA,
  ["*Monitor for bleeding and infection",
   "*Provide pain control with a PCA (patient-controlled analgesia) pump",
   "*Perform care of the drain",
   "Give aspirin for incision pain || Aspirin is avoided in pericarditis",
   "*Monitor for clots"],
  "A pericardial window removes part of the pericardium so fluid drains continuously. Post-op: monitor for bleeding, infection and clots; PCA pain control; drain care.")

q("perinurse", "A client in the acute phase of pericarditis asks when they can be up and walking. Which response is accurate?",
  ["'You can resume full activity today.' || Bed rest is used in the acute phase",
   "*'Rest in bed for now, then increase activity gradually.'",
   "'You'll need strict bed rest for 6 months.' || Activity increases gradually after the acute phase",
   "'Lie flat in bed to ease the pain.' || Upright and leaning forward eases pain"],
  "Pericarditis care: bed rest in the acute phase, then gradually increase activity. Position upright and leaning forward for comfort.")
