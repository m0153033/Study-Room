T = "e5bowel"; SET = "20261128"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# anat
q("anat", "A client with a new ileostomy asks why the output is watery when a friend with a colostomy has formed stool. Which explanation by the nurse is accurate?",
  ["'Your stool skips the cecum, so bile thins it.' || Bile is not the reason; the colon's water absorption is bypassed",
   "*'Stool leaves before the large intestine can absorb its water.'",
   "'The small intestine adds extra water to stool.' || The small intestine's main job is nutrient absorption",
   "'The ileocecal valve stops working after surgery.' || The valve separates the bowels; it does not make stool watery"],
  "The large intestine absorbs water and carries out elimination; the small intestine (duodenum, jejunum, ileum) absorbs nutrients. An ileostomy diverts stool before the large intestine.")

# types (HI)
q("types", "A 62-year-old client on a medical unit has a distended abdomen. Which history finding points to a PERISTALSIS problem rather than a patency problem?",
  ["A known stricture in the sigmoid colon || A stricture is a mechanical (patency) cause",
   "Several bands of adhesions from old surgeries || Adhesions are a mechanical (patency) cause",
   "*A magnesium level well below the normal range",
   "A hard mass of stool lodged in the rectum || Fecal impaction is a mechanical (patency) cause"],
  "Mechanical obstruction is a patency problem (adhesions, tumors, fecal impaction, volvulus, intussusception, strictures, hernias). Ileus is a peristalsis problem; low potassium or magnesium is a listed cause.")

q("types", "A nurse is sorting causes of bowel obstruction for a study group. Which items belong in the NONmechanical (ileus) column? " + SATA,
  ["*Peritonitis",
   "Intussusception || This is a mechanical cause: bowel telescoping",
   "*Recent abdominal surgery",
   "*Vascular insufficiency",
   "A colon tumor || A tumor is a mechanical cause"],
  "Ileus causes: abdominal surgery, opioids, low potassium or magnesium, peritonitis, diabetes or Parkinson's, and vascular insufficiency. Tumors and intussusception are mechanical.")

# mech
q("mech", "A nurse reviews three mechanical causes of obstruction with a student. Which description matches intussusception?",
  ["Bands of scar tissue left after abdominal surgery || That describes adhesions",
   "A loop of bowel twisting around on itself || That describes volvulus",
   "*One bowel segment telescoping into the next",
   "Bowel pushing through a weak abdominal wall || That describes a hernia"],
  "Intussusception is one segment telescoping into another; it is often discussed in pediatrics and treated with enema reduction or surgery. Adhesions are scar tissue; volvulus is a twist.")

# hernia (HI)
q("hernia", "A client asks where hernias can occur. Which locations did the nurse's teaching include? " + SATA,
  ["*Femoral",
   "*Epigastric",
   "*Incisional (ventral)",
   "Cervical || Cervical was not a listed hernia location",
   "*Inguinal"],
  "Listed hernia locations: inguinal, femoral, umbilical, incisional/ventral and epigastric.")

q("hernia", "A 60-year-old client's inguinal hernia bulge no longer goes back in, but there is no fever, the heart rate is normal and pain is mild. How should the nurse interpret this?",
  ["Strangulated, with blood supply already cut off || Strangulation brings fever, severe pain, tachycardia and vomiting",
   "*Incarcerated, with blood flow intact but able to progress",
   "Reducible, since pain is mild and vitals are normal || A reducible hernia can be pushed back in",
   "A volvulus, since the bowel is now trapped || Volvulus is the bowel twisting on itself"],
  "Incarcerated (irreducible): contents can't be pushed back but blood flow is intact; it can progress to strangulation, where blood supply is compromised (an emergency).")

# partial (HI)
q("partial", "A client with a bowel obstruction is on conservative care. Which new report by the client suggests the obstruction has become COMPLETE?",
  ["'I passed a little gas a few minutes ago.' || Passing gas fits a partial obstruction",
   "'I had a small, loose stool after lunch.' || Some stool, even diarrhea, can pass with partial",
   "*'Nothing, not even gas, has come out since last night.'",
   "'My cramps feel about the same as yesterday.' || Complete obstruction progresses fast, not steadily"],
  "Complete obstruction: no stool or flatus (obstipation), fast progression, medical emergency. Partial: some stool (sometimes diarrhea) or gas passes, slower progression, conservative care may be tried.")

q("partial", "A nurse compares two clients with bowel obstruction. Which statements about a PARTIAL obstruction are accurate? " + SATA,
  ["*Some gas may still pass",
   "*Diarrhea can occur",
   "*Symptoms progress more slowly",
   "It is defined by obstipation || Obstipation is the hallmark of complete obstruction",
   "Conservative care is never an option || Conservative care may be tried for partial"],
  "Partial obstruction: some stool (sometimes diarrhea) or gas passes, progression is slower, conservative care may be tried. Obstipation occurs with complete obstruction.")

# patho
q("patho", "A client with an obstruction had hyperactive bowel sounds this morning. A new nurse says, 'Loud sounds mean the bowel isn't blocked.' Which reply is best?",
  ["'Right, loud sounds rule out a blockage.' || Early hyperactive sounds are common in obstruction",
   "*'Peristalsis increases early above a blockage, so sounds can be loud.'",
   "'Loud sounds mean the bowel has already perforated.' || Hyperactive sounds reflect increased peristalsis",
   "'Loud sounds show fluid is being absorbed normally.' || Fluid builds up in the lumen instead"],
  "Early in an obstruction peristalsis increases above the blockage, so sounds may be hyperactive; they may diminish later. Don't be thrown off by early hyperactive sounds.")

# shock (HI)
q("shock", "A nurse is caring for a client with a small bowel obstruction. Which finding is the EARLIEST clue to poor brain perfusion from hypovolemic shock?",
  ["Warm, flushed skin over the chest || Shock causes pallor and diaphoresis",
   "A slow, steady heart rate || Shock causes tachycardia",
   "*New restlessness and confusion",
   "Rising urine output each hour || Urine output drops in shock"],
  "Hypovolemic shock: hypotension, tachycardia, tachypnea, decreased urine output, anxiety, pallor and diaphoresis. Altered mental status reflects poor brain perfusion.")

q("shock", "A client with a large bowel obstruction is pale, sweaty and anxious, with BP (blood pressure) 82/50. Which plan of care does the nurse anticipate? " + SATA,
  ["*Prescribed IV (intravenous) fluid resuscitation",
   "*Notifying the provider right away",
   "Oral electrolyte drinks every hour || Oral fluids do not support circulation here",
   "*Vasopressors if fluids alone don't help",
   "Ambulation to boost circulation || Ambulation does not treat hypovolemic shock"],
  "Support circulation with prescribed IV fluid resuscitation and notify the provider; possible ICU (intensive care unit) transfer and vasopressors if fluids alone aren't enough.")

# sbolbo (HI)
q("sbolbo", "A 69-year-old with a history of colorectal cancer has a large bowel obstruction. The client asks what to expect next. Which response is accurate?",
  ["'Most large bowel blockages resolve without treatment.' || LBO often needs surgery",
   "*'Large bowel obstructions often need surgery.'",
   "'Adhesions are the most likely cause of yours.' || Adhesions are a common SBO cause",
   "'You will likely vomit bile early and often.' || Early bilious vomiting fits SBO"],
  "LBO (large bowel obstruction): 20-25% of obstructions, often colorectal cancer or volvulus, often needs surgery. SBO (small bowel obstruction): 75-80%, often adhesions or hernia, mostly conservative.")

q("sbolbo", "Which findings would the nurse expect in a client with a SMALL bowel obstruction? " + SATA,
  ["*Mild abdominal distention",
   "*Pain that comes and goes centrally",
   "Absolute obstipation from the start || Absolute obstipation fits LBO; gas and stool may pass early in SBO",
   "*Frequent vomiting early on",
   "Continuous, aching lower pain || This pain pattern fits LBO"],
  "SBO (small bowel obstruction): early, frequent vomiting that may contain bile, central colicky intermittent pain, mild distention, and gas/stool may still pass early.")

# assess
q("assess", "A nurse is collecting a history from a client with a suspected bowel obstruction. Which questions are relevant? " + SATA,
  ["*'When was your last bowel movement?'",
   "*'Do you use laxatives or opioids?'",
   "*'Has anyone in your family had cancer?'",
   "'What is your favorite type of music?' || This does not relate to obstruction risk",
   "*'Do you smoke or drink alcohol?'"],
  "History for obstruction: previous abdominal surgery, opioid or laxative use, passing gas and last BM (bowel movement), unintended weight loss, family history of cancer, age, diet, smoking and alcohol.")

# nursing (HI)
q("nursing", "A client with a bowel obstruction is NPO (nothing by mouth) with an NG (nasogastric) tube. The client reports a dry, sticky mouth. Which action is best?",
  ["Offer ice chips and sips of juice || The client must stay NPO",
   "*Provide frequent oral care",
   "Clamp the NG tube for an hour || NG decompression should continue",
   "Remove the NG tube to ease comfort || The tube is needed for decompression"],
  "Care for bowel obstruction: NPO with oral care, NG decompression (Salem sump), IV (intravenous) fluids for replacement and maintenance, and strict I&O (intake and output) including NG output.")

q("nursing", "At the end of a shift, the NG (nasogastric) tube of a client with a small bowel obstruction drained a large amount. Why does the nurse watch the electrolyte results closely?",
  ["NG drainage adds fluid back to the client || NG output removes fluid; it doesn't add it",
   "*NG output adds to fluid and electrolyte loss",
   "Electrolytes show whether the tube is placed right || Placement is not checked with electrolytes",
   "Low electrolytes mean the obstruction is resolving || Losses do not show resolution"],
  "Strict I&O (intake and output) including NG output is extremely important because NG output adds to fluid and electrolyte loss. Monitor electrolytes closely.")

# interv
q("interv", "A nurse matches bowel obstruction causes with treatments. Which pairing is correct?",
  ["Volvulus: ambulation and prokinetic agents || Volvulus is usually treated with surgery",
   "Postoperative ileus: manual disimpaction || Postoperative ileus is treated with ambulation and prokinetics",
   "*Fecal impaction: enemas and stool softeners",
   "Opioid-related ileus: enema reduction || Opioid ileus is treated with a mu-opioid antagonist"],
  "Fecal impaction: fluids and fiber, stool softeners and laxatives, enemas, manual disimpaction, ambulation. Hernia, volvulus, tumor or stricture: usually surgery. Postoperative ileus: ambulation and prokinetics. Opioid ileus: mu-opioid antagonist.")

# meds (HI)
q("meds", "A client has taken bisacodyl every night for two years and says, 'I can't go without it now.' Which explanation fits this concern?",
  ["Bisacodyl is a prokinetic that causes tardive dyskinesia || That describes metoclopramide",
   "Bisacodyl is a bulk former that needs more fluid || That describes psyllium",
   "*Long-term stimulant laxative use can cause dependence",
   "Bisacodyl blocks gut opioid receptors over time || That describes alvimopan"],
  "Bisacodyl is a stimulant laxative; long-term use can cause dependence.")

q("meds", "A nurse is teaching about docusate sodium. Which statements are accurate? " + SATA,
  ["*It works by softening the stool",
   "*Results may take 1 to 3 days",
   "*Keep up fluid intake while taking it",
   "Keep taking it if diarrhea starts || Stop docusate if diarrhea occurs",
   "It is limited to 15 doses for heart risk || That limit applies to alvimopan"],
  "Docusate softens stool. Teach: maintain fluid intake, stop if diarrhea occurs, may take 1-3 days to work. Alvimopan is the drug limited to 15 doses because of MI (myocardial infarction) risk.")

# crc
q("crc", "A 52-year-old client asks which factors raise colorectal cancer risk. Which statement by the nurse is accurate?",
  ["'Regular exercise is one of the main risks.' || Physical inactivity is the risk factor",
   "*'A personal or family history raises your risk.'",
   "'A low-fat diet is linked with higher risk.' || A diet high in animal fat is the risk",
   "'Risk is highest before age 30.' || Age over 50 is a listed risk"],
  "CRC (colorectal cancer) risks: age over 50, diet high in animal fat, smoking and alcohol, inflammatory bowel disease, physical inactivity, family or personal history, Lynch syndrome and FAP (familial adenomatous polyposis).")

# fap
q("fap", "A 19-year-old with familial adenomatous polyposis (FAP) asks why a colectomy is being discussed so young. Which response is accurate?",
  ["'FAP causes a single large polyp that must be removed.' || FAP causes hundreds to thousands of polyps",
   "*'With FAP, lifetime cancer risk is near 100 percent.'",
   "'FAP comes from diet, so surgery replaces diet change.' || FAP is inherited, not diet-caused",
   "'FAP causes 2 to 4 percent of colon cancers only.' || That figure describes Lynch syndrome"],
  "FAP: hundreds to thousands of polyps, starting as early as the teen years, near 100% lifetime cancer risk; prophylactic colectomy may be discussed.")

# scope
q("scope", "Four hours after a colonoscopy with biopsy, which client report should the nurse act on FIRST?",
  ["'I feel a little bloated and gassy.' || Mild cramping and gas are expected",
   "'I'm still a bit sleepy from the sedation.' || Sleepiness after sedation is expected",
   "*'My belly hurts badly and feels hard.'",
   "'I passed some gas a while ago.' || Passing gas is expected"],
  "After colonoscopy, monitor for bleeding and perforation. Severe pain with a hard, rigid abdomen is the most concerning finding.")

# surg (HI)
q("surg", "A client is recovering from a low anterior resection. Which statement describes this surgery correctly?",
  ["*'The upper rectum was removed and the bowel was reconnected.'",
   "'The rectum and anus were removed, with a permanent colostomy.' || That describes an APR (abdominoperineal resection)",
   "'A rectal stump was left with a temporary colostomy.' || That describes a Hartmann procedure",
   "'A single polyp was removed through the scope.' || That describes a polypectomy"],
  "Low anterior resection removes the upper rectum and reconnects; the anastomosis is low, so nothing goes per rectum.")

q("surg", "A nurse is assigned two clients: one after a Hartmann procedure and one after an APR (abdominoperineal resection). Which statement correctly compares them?",
  ["Both clients will have a permanent colostomy || Hartmann creates a temporary colostomy",
   "Both clients will need perineal wound care || The perineal wound follows APR only",
   "*Only the APR client has a perineal wound to assess",
   "Only the Hartmann client has a colostomy || Both procedures create a colostomy"],
  "APR: permanent colostomy and a perineal wound; monitor both abdominal and perineal sites. Hartmann: rectal stump and temporary colostomy; reconnection may be possible later.")

# periop
q("periop", "A client scheduled for colon cancer surgery with a planned ostomy asks why a wound/ostomy nurse is coming to see him before surgery. Which response is accurate?",
  ["'To start a high-fiber diet before surgery.' || Diet is NPO first, then advanced toward low-residue after surgery",
   "*'To help plan the best site for your stoma.'",
   "'To decide whether you need antibiotics.' || Antibiotics are prescribed by the provider",
   "'To remove sutures from an earlier surgery.' || This is not the purpose of the preop consult"],
  "Preop care before CRC (colorectal cancer) surgery with an ostomy: psychosocial support, wound/ostomy nurse consult for stoma site planning, explaining the surgery and ostomy, prescribed antibiotics, respiratory hygiene and activity teaching.")

# ostomy (HI)
q("ostomy", "A client has a transverse colostomy, and another client has a sigmoid colostomy. How should the nurse compare their expected output?",
  ["Both will have the same liquid output || Output firms the closer the stoma is to the rectum",
   "*The sigmoid output will be firmer than the transverse",
   "The transverse output will be firmer than the sigmoid || The sigmoid is closer to the rectum, so firmer",
   "Neither will pass stool until the stoma heals || Output is expected after surgery"],
  "The closer to the rectum, the more water absorbed and the firmer the stool. Sigmoid colostomy output is more solid.")

q("ostomy", "During a home visit, the nurse assesses a client's colostomy stoma. Which finding is expected and needs no report?",
  ["A stoma that has sunk below the skin || Retraction should be reported",
   "A stoma that sticks out far like a trunk || Excessive protrusion should be reported",
   "*A stoma that is pink, moist and raised",
   "A stoma that has turned dusky and dark || Dark or black color should be reported"],
  "A healthy stoma is pink, moist, shiny and raised (PMS). Report dark or black color, retraction, excessive protrusion, excoriated skin and leakage.")

# ostteach (HI)
q("ostteach", "A client with a new colostomy asks how to prepare the skin barrier. Which instruction is correct?",
  ["'Cut the opening 1 inch wider than the stoma.' || A large gap exposes skin to leakage",
   "*'Measure the stoma and cut within 1/8 inch of it.'",
   "'Cut it to half the size so it fits snugly.' || Too small an opening is not the instruction",
   "'Use the same size you were given at discharge.' || The stoma shrinks, so re-measure"],
  "Measure the stoma and cut the barrier to fit, within 1/8 inch of the stoma. The stoma shrinks over the first several weeks, so re-measure regularly.")

q("ostteach", "A nurse is planning ostomy teaching for an 80-year-old client. Which factors should the nurse assess before teaching self-care? " + SATA,
  ["*How well the client can see",
   "*Fine motor skill in the hands",
   "*Ability to handle supplies alone",
   "The client's favorite foods || Foods matter for odor and gas, not self-care ability",
   "*Concerns about body image"],
  "Lifespan considerations affect ostomy self-care: assess vision, hand dexterity, ability to manage supplies independently, and body image and sexuality concerns.")

# screen
q("screen", "A 45-year-old client at average risk prefers the screening test that is repeated least often. Which option should the nurse describe?",
  ["Stool blood test || This is done every year",
   "Stool DNA (deoxyribonucleic acid)/RNA (ribonucleic acid) test || This is done every 3 years",
   "CT (computed tomography) colonography || This is done every 5 years",
   "*Colonoscopy"],
  "Average-risk screening starts at 45: annual stool blood test, stool DNA/RNA test every 3 years, colonoscopy every 10 years, or CT colonography every 5 years.")
