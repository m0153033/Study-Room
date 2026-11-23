T = "cardinf"; SET = "20261123"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("risk", "A nursing student asks how a cardiac infection leads to reduced perfusion. Which sequence should the nurse describe?",
  ["Reduced perfusion first, then organism entry, then inflammation of the valves and tissue || The order is reversed; perfusion drops as the end result",
   "*Organism or immune response, inflammation, tissue/valve damage, reduced perfusion",
   "Valve damage first, then the organism enters, then pain || Organism or immune response starts the process",
   "Inflammation, then organism entry, then improved perfusion || Inflammation follows the organism and perfusion decreases"],
  "Cardiac infection starts with an organism or immune response, which causes inflammation that damages tissue and valves and reduces perfusion. Bacteria are the most common cause.")

q("labs", "A 57-year-old client is being evaluated for a cardiac infection. Which lab results indicate inflammation? " + SATA,
  ["*ESR (erythrocyte sedimentation rate) of 32 mm/hr",
   "hsCRP (high-sensitivity C-reactive protein) of 0.6 mg/L || hsCRP below 1.0 mg/L is normal",
   "*hsCRP (high-sensitivity C-reactive protein) of 5 mg/L",
   "*Elevated WBC (white blood cell count)",
   "ESR (erythrocyte sedimentation rate) of 10 mm/hr || ESR above 20 mm/hr indicates inflammation"],
  "ESR above 20 mm/hr indicates inflammation; hsCRP normal is below 1.0 mg/L and above 3 mg/L means serious inflammation. Elevated WBC, ESR and hsCRP support inflammation but must be paired with condition-specific tests.")

q("rfpath", "The parents of a 7-year-old diagnosed with rheumatic fever ask how their child got it. Which explanation by the nurse is accurate?",
  ["'Bacteria attached to a damaged heart valve and formed growths that broke off.' || This describes infective endocarditis",
   "'A virus infected and inflamed the heart muscle.' || This describes viral myocarditis",
   "*'It's an immune response about 2-3 weeks after a strep throat infection.'",
   "'It spread to the heart from a recent dental procedure.' || Dental procedures are a risk for endocarditis, not the cause of rheumatic fever"],
  "Rheumatic fever is an immune response 2-3 weeks after group A beta-hemolytic strep pharyngitis, most common in ages 5-14. It spreads through oral/respiratory secretions.")

q("jones", "Which combination does the modified Jones criteria require to diagnose rheumatic fever?",
  ["Positive blood cultures plus a vegetation seen on echocardiogram || This is the central evidence for endocarditis (Duke)",
   "2 major, or 1 major plus 3 minor, or 5 minor criteria || This is the modified Duke criteria for endocarditis",
   "*Prior strep evidence plus 2 major, or 1 major plus 2 minor",
   "Hypotension, JVD and muffled heart sounds || This is Beck's triad for tamponade"],
  "The modified Jones criteria diagnose rheumatic fever: evidence of prior strep (throat culture or ASO titer above 200 IU) plus 2 major, or 1 major plus 2 minor.")

q("jones", "A nurse is reviewing the HEART mnemonic for rheumatic fever. Which finding does the letter 'T' represent?",
  ["Tamponade || Tamponade is a pericardial complication, not part of HEART",
   "Troponin elevation || Elevated troponin is a myocarditis lab finding",
   "Tender finger-pad nodules || Painful finger-pad nodules are Osler nodes in endocarditis",
   "*Twitching (Sydenham chorea)"],
  "HEART = Heart failure, Enlarged heart, Arthritis (migratory), Rash (erythema marginatum), Twitching (Sydenham chorea).")

q("rftx", "An 8-year-old with acute rheumatic fever has a documented penicillin allergy. Which antibiotic does the nurse expect?",
  ["IV vancomycin || Vancomycin is an empiric antibiotic for endocarditis",
   "*Erythromycin",
   "Colchicine || Colchicine is an anti-inflammatory used for pericarditis, not an antibiotic",
   "Ceftriaxone || Ceftriaxone is listed as an empiric endocarditis antibiotic"],
  "Acute rheumatic fever is treated with penicillin, or erythromycin if the child is penicillin-sensitive. The full 10-day course must be completed.")

q("rftx", "The parent of a 12-year-old recovering from rheumatic carditis is reviewing discharge teaching. Which statement needs MORE teaching?",
  ["'Every sore throat she gets from now on should be swabbed or cultured first.' || Correct: this is the Sore Throat Rule",
   "'She may need monthly penicillin shots for years.' || Correct: prophylaxis lasts years, up to lifelong",
   "*'Once her 10-day course is finished, she won't need more antibiotics.'",
   "'She should avoid strenuous activity for now.' || Correct: rest and avoiding strenuous activity are part of care"],
  "After rheumatic fever, long-term prophylaxis with monthly IM penicillin G or daily oral penicillin lasts 5-10 years, until age 21-40, or lifelong depending on heart damage. Every sore throat must be swabbed or cultured.")

q("iepath", "A 35-year-old client who injects drugs is diagnosed with infective endocarditis. Which organisms are commonly involved?",
  ["*Streptococcus viridans and Staphylococcus aureus",
   "Group A beta-hemolytic strep via an immune response || This causes rheumatic fever",
   "Coxsackie B virus and adenovirus || These are viral causes of myocarditis",
   "Influenza virus || Viral infection such as influenza is a cause of pericarditis"],
  "In infective endocarditis, organisms such as Streptococcus viridans and Staphylococcus aureus stick to a damaged valve (usually mitral or tricuspid) and form vegetations. IV drug use is the most common listed risk factor.")

q("iesigns", "A 62-year-old client with a prosthetic valve has suspected infective endocarditis. Which sign requires an eye exam to detect?",
  ["Janeway lesions || These are painless spots on the palms and soles",
   "Osler nodes || These are painful nodules on the finger pads",
   "Splinter hemorrhages || These are reddish-brown lines under the nail beds",
   "*Roth spots"],
  "Roth spots are white-centered retinal hemorrhages seen on eye exam in infective endocarditis.")

q("iesigns", "A nursing student is comparing the skin signs of infective endocarditis. Which statement by the student is correct?",
  ["*'Osler nodes are painful; Janeway lesions are painless.'",
   "'Janeway lesions are painful nodules on the finger pads.' || Janeway lesions are painless palm/sole spots",
   "'Roth spots appear as lines under the nail beds.' || Lines under the nails are splinter hemorrhages",
   "'Splinter hemorrhages are white-centered retinal bleeds.' || Those are Roth spots"],
  "Osler = painful (O for 'ouch') finger-pad nodules; Janeway = painless palm/sole spots. Splinter hemorrhages are nail-bed lines from microemboli; Roth spots are retinal.")

q("duke", "A client with suspected infective endocarditis meets ONE major modified Duke criterion. How many minor criteria are needed to confirm the diagnosis?",
  ["2 minor criteria || 1 major plus 2 minor is the Jones rule for rheumatic fever",
   "5 minor criteria || 5 minor criteria alone confirm it when no major criterion is met",
   "*3 minor criteria",
   "1 minor criterion || One minor criterion with one major is not enough"],
  "Modified Duke criteria confirm IE with 2 major, 1 major plus 3 minor, or 5 minor criteria.")

q("duke", "Which findings count toward the modified Duke criteria for infective endocarditis? " + SATA,
  ["*Fever above 38°C (100.4°F)",
   "Migratory polyarthritis || This is a rheumatic fever finding (Jones criteria)",
   "*IV (intravenous) drug use or an invasive line",
   "Positive ASO (antistreptolysin O) titer || This shows prior strep for rheumatic fever",
   "*Vascular or embolic phenomena"],
  "Minor Duke criteria include fever above 38°C, IV drug use or an invasive line, vascular/embolic phenomena, immunologic phenomena and cultures that don't meet major criteria. Positive blood cultures plus vegetation on echo are the central evidence.")

q("iecomp", "A client being treated for infective endocarditis develops fatigue, shortness of breath and crackles. Which complication does the nurse suspect?",
  ["Right-sided heart failure || Right HF presents with edema, weight gain and anorexia",
   "Splenic infarct || This causes abdominal pain radiating to the left shoulder",
   "*Left-sided heart failure",
   "Embolic stroke || This presents with neurologic changes such as slurred speech or weakness"],
  "Heart failure is the most common complication of IE. Left HF: fatigue, SOB (shortness of breath), crackles. Right HF: edema, weight gain, anorexia.")

q("iecomp", "Which complications should the nurse monitor for in a 50-year-old client with infective endocarditis? " + SATA,
  ["*Sepsis",
   "*Renal infarct",
   "Sydenham chorea || This is a rheumatic fever finding",
   "*Septic aneurysm",
   "*Conduction problems"],
  "The three big threats in IE are sepsis, heart failure and embolic events. Also monitor for renal infarct, septic aneurysm and conduction problems.")

q("ietx", "A client with infective endocarditis is receiving IV (intravenous) vancomycin. When should the nurse plan to draw the vancomycin trough?",
  ["After the first dose || The trough is drawn before the 5th dose",
   "*Before the 5th dose",
   "Only after the 4-6 week course is complete || Levels are monitored during therapy",
   "Troughs aren't needed if kidney function is normal || Vancomycin trough and kidney function are both monitored"],
  "Monitor the vancomycin trough before the 5th dose, gentamicin peak/trough and kidney function. IV therapy for IE lasts 4-6 weeks.")

q("ienurse", "A 40-year-old client recovering from infective endocarditis asks about dental care. Which teaching is correct?",
  ["'Skip dental visits to avoid any risk.' || Good oral hygiene and dental care help prevent IE",
   "'Take antibiotics only if you get a fever after dental work.' || Prophylaxis is given before the procedure",
   "*'Take amoxicillin about 1 hour before dental work as prescribed.'",
   "'You'll take antibiotics for a week after each cleaning.' || Prophylaxis is given about 1 hour before the procedure"],
  "Good oral hygiene and prophylactic antibiotics (amoxicillin) about one hour before dental or invasive procedures help prevent infective endocarditis.")

q("myo", "A 22-year-old man with recent flu-like illness has chest pain and palpitations; myocarditis is suspected. Which findings does the nurse expect? " + SATA,
  ["*Elevated troponin",
   "*Elevated BNP (B-type natriuretic peptide)",
   "ASO (antistreptolysin O) titer above 200 IU || This shows prior strep for rheumatic fever",
   "*Elevated CRP (C-reactive protein) and ESR (erythrocyte sedimentation rate)",
   "Janeway lesions on the palms || These are endocarditis findings"],
  "Myocarditis labs include elevated troponin, BNP, CRP and ESR. Cardiac MRI/echo is the noninvasive imaging standard; endomyocardial biopsy is the gold standard reserved for severe cases.")

q("myotx", "A client with myocarditis and heart failure has a new prescription for verapamil for rate control. What is the nurse's BEST action?",
  ["Give the verapamil as prescribed || Non-dihydropyridine CCBs worsen heart failure",
   "Give diltiazem instead || Diltiazem is also avoided in myocarditis",
   "Give the verapamil with food to reduce side effects || The drug should be avoided, not adjusted",
   "*Question the prescription with the provider"],
  "Diltiazem and verapamil are AVOIDED in myocarditis because non-dihydropyridine CCBs (calcium channel blockers) reduce heart rate, pumping strength and EF (ejection fraction), worsening heart failure.")

q("myotx", "A nurse is monitoring a client with myocarditis on telemetry. Which finding warns of the 'sudden crash' and needs IMMEDIATE action?",
  ["*New V-tach with a low MAP and dropping urine output",
   "Stable daily weight and balanced intake and output for 3 days || These are reassuring findings",
   "SpO2 (oxygen saturation) of 96% on oxygen || The goal is SpO2 above 94%",
   "Mild fatigue after bathing || This is less urgent than an arrhythmia with low MAP"],
  "The nurse's primary role in myocarditis is to prevent the 'sudden crash' with continuous telemetry and hemodynamic monitoring: watch for SVT, V-tach, low MAP, low urine output and edema.")

q("peri", "A 34-year-old client is admitted with acute pericarditis. Which findings does the nurse expect? " + SATA,
  ["*Sharp pleuritic chest pain radiating to the left trapezius",
   "*Pain that improves when sitting up and leaning forward",
   "Painless red spots on the palms || Janeway lesions are endocarditis findings",
   "*Diffuse concave ST elevation with PR depression",
   "Water-bottle heart on chest x-ray as a normal finding || A water-bottle heart suggests a large effusion, not a normal finding"],
  "Pericarditis pain is pleuritic and positional, radiates to the left trapezius and is relieved by sitting up and leaning forward. The classic ECG shows diffuse concave ST elevation with PR depression.")

q("peri", "A client who had a recent MI (myocardial infarction) now has sharp chest pain that worsens lying flat and a scratchy, position-dependent sound at the left lower sternal border. What does the nurse suspect?",
  ["Infective endocarditis from a damaged, infected heart valve || IE presents with persistent high fever and a new or changing murmur",
   "*Pericarditis related to recent MI (Dressler syndrome)",
   "Rheumatic fever || Rheumatic fever follows strep pharyngitis",
   "Chronic constrictive pericarditis || Constriction causes right-sided heart failure signs from a stiff pericardium"],
  "Recent MI, including Dressler syndrome, is a cause of pericarditis. Positional pain and a scratchy friction rub heard at the left lower sternal border with the diaphragm fit pericarditis.")

q("perimi", "A client presents with chest pain. Which finding favors MI (myocardial infarction) over pericarditis?",
  ["Diffuse ST elevation across many leads || Diffuse ST elevation favors pericarditis",
   "A pericardial friction rub || A friction rub favors pericarditis",
   "*Crushing pain relieved by nitroglycerin or rest",
   "Relief when sitting up and leaning forward || Positional relief favors pericarditis"],
  "MI: crushing pain relieved by nitroglycerin/rest, localized ST elevation, S3/S4. Pericarditis: sharp pleuritic pain, relief sitting up and leaning forward, diffuse ST elevation, friction rub.")

q("tamp", "A client with a large pericardial effusion is being monitored. Which finding suggests progression to cardiac tamponade?",
  ["Bounding pulses || Tamponade causes hypotension, not bounding pulses",
   "*Systolic BP that drops with each inspiration",
   "Bradycardia || Tachycardia is watched for in tamponade",
   "Increasing urine output over the past several hours || Tamponade causes low urine output"],
  "A BP drop with inspiration (pulsus paradoxus) plus Beck's triad (hypotension, JVD, muffled heart sounds) indicates tamponade, where fluid compresses the heart and impairs filling.")

q("tamp", "A 60-year-old client with pericarditis is at risk for tamponade. Which findings should the nurse watch for? " + SATA,
  ["*Electrical alternans on the monitor",
   "*Tachycardia",
   "Loud, crisp heart sounds || Beck's triad includes muffled heart sounds",
   "*Altered mental status",
   "*Low urine output"],
  "With a large effusion or tamponade, watch for electrical alternans (beat-to-beat QRS variation), tachycardia, low urine output and altered mental status, along with Beck's triad and pulsus paradoxus.")

q("constrict", "A client with a history of repeated pericarditis has JVD (jugular vein distension), hepatic engorgement and dependent edema. Which explanation fits these findings?",
  ["Fluid has suddenly built up within the pericardial sac || Sudden fluid accumulation describes effusion/tamponade",
   "Vegetations are breaking off and embolizing || This describes endocarditis",
   "A virus has inflamed the heart muscle || This describes myocarditis",
   "*A thick, stiff pericardium is impairing filling"],
  "In chronic constrictive pericarditis, repeated inflammation makes the pericardium thick and stiff like a corset, impairing filling and causing right-sided heart failure signs. It resembles diastolic heart failure; echo/CT shows a thickened pericardium.")

q("peritx", "A client with acute pericarditis cannot take NSAIDs (nonsteroidal anti-inflammatory drugs). Which medication does the nurse expect instead?",
  ["*Prednisone",
   "An anticoagulant || Anticoagulants are avoided because bleeding into the sac can cause tamponade",
   "Penicillin || Penicillin treats rheumatic fever, not pericarditis",
   "Diltiazem || Diltiazem is not a pericarditis treatment"],
  "First-line treatment for acute pericarditis is an NSAID plus colchicine; prednisone is used if NSAIDs are contraindicated.")

q("peritx", "A client is discharged on an NSAID (nonsteroidal anti-inflammatory drug) and colchicine for acute pericarditis. Which statement needs MORE teaching?",
  ["'I'll take my NSAID with food or yogurt.' || Correct: this reduces stomach irritation",
   "'My pain may start easing within 48 hours.' || Correct: relief often begins within 48 hours",
   "*'I'll add aspirin for extra pain relief.'",
   "'I shouldn't take blood thinners unless prescribed for another reason.' || Correct: anticoagulants are avoided"],
  "Avoid aspirin and anticoagulants in pericarditis because bleeding into the sac can worsen into tamponade. Take NSAIDs with food or yogurt; relief often begins within 48 hours.")

q("perinurse", "A nurse is caring for a client with acute pericarditis on a busy unit. Which action BEST promotes the client's safety?",
  ["Check an Amsler grid each shift || An Amsler grid is not a pericarditis assessment",
   "Place the client flat on the back to reduce chest pain || Pain is worse lying flat; position upright and leaning forward",
   "*Alert the team to avoid aspirin and anticoagulants",
   "Give anticoagulants to prevent clots || Anticoagulants are avoided in pericarditis"],
  "Make all team members aware to avoid aspirin and anticoagulants. Position upright and leaning forward, and assess pain, friction rub, pulsus paradoxus and electrical alternans.")
