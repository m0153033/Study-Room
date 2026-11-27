T = "e5bowel"; SET = "20261127"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("anat", "A nurse is teaching a group of nursing assistants about the lower GI (gastrointestinal) tract. Which statement by an assistant shows correct understanding?",
  ["'The colon is where most nutrients from food are absorbed.' || Nutrients are absorbed mainly in the small intestine (duodenum, jejunum, ileum)",
   "*'The jejunum is part of the small intestine and absorbs nutrients.'",
   "'The cecum is the first part of the small intestine.' || The ileum empties into the cecum, which is part of the large intestine",
   "'The pyloric sphincter joins the ileum to the colon.' || The ileocecal valve separates the small and large intestines"],
  "The small intestine (duodenum, jejunum, ileum) absorbs nutrients; the large intestine absorbs water and carries out elimination. The ileum empties into the cecum through the ileocecal valve.")

q("types", "A 67-year-old retired teacher is 1 day after a hip surgery and receiving opioids around the clock. Which assessment finding would most support a developing ileus?",
  ["*A distended abdomen with hypoactive sounds and no blockage on imaging",
   "A CT (computed tomography) scan showing the bowel twisted on itself || Volvulus is a mechanical (patency) cause, not ileus",
   "A firm bulge in the groin that cannot be pushed back in || That describes an incarcerated hernia, a mechanical cause",
   "A mass seen narrowing the colon on CT imaging || A tumor is a mechanical cause of obstruction"],
  "Ileus is a nonmechanical obstruction: impaired peristalsis with no physical blockage. Opioids are a listed cause.")

q("types", "A charge nurse asks a new graduate to identify which clients have a MECHANICAL (patency) cause of bowel obstruction. Which clients should the graduate identify? " + SATA,
  ["*A 59-year-old with a stricture narrowing the bowel",
   "*A 72-year-old with a strangulated femoral hernia",
   "A 64-year-old on a continuous opioid infusion || Opioids cause nonmechanical obstruction (ileus)",
   "*A 48-year-old whose colon has twisted (volvulus)",
   "A 55-year-old with a low potassium level || Low potassium causes ileus, a peristalsis problem"],
  "Mechanical obstruction is a patency problem: adhesions, tumors, fecal impaction, volvulus, intussusception, strictures and hernias. Ileus (a peristalsis problem) causes include opioids and low potassium or magnesium.")

q("mech", "A client with a large bowel obstruction is told the cause is a volvulus. The client asks what the usual treatment is. Which response by the nurse is accurate?",
  ["'Enema reduction is the usual first treatment for it.' || Enema reduction is linked with intussusception",
   "'Walking and a prokinetic drug usually correct it.' || Ambulation and prokinetics treat postoperative ileus",
   "*'A twisted bowel like this is usually treated with surgery.'",
   "'A mu-opioid antagonist usually untwists the bowel.' || A mu-opioid antagonist treats opioid-related ileus"],
  "Volvulus is the bowel twisting on itself, a common cause of large bowel obstruction that is usually treated surgically.")

q("hernia", "A 31-year-old pregnant client asks the clinic nurse why she has developed a small umbilical hernia. Which explanation is accurate?",
  ["'Low potassium during pregnancy weakens the bowel.' || Low potassium is linked with ileus, not hernia formation",
   "*'Pregnancy raises abdominal pressure on a weak spot in the wall.'",
   "'The bowel has twisted on itself near the navel.' || Twisting of the bowel is a volvulus",
   "'Scar tissue from the pregnancy is pulling the bowel.' || Scar tissue (adhesions) usually follows abdominal surgery"],
  "A hernia forms from a weak spot in the muscular wall plus increased abdominal pressure, which rises with obesity, pregnancy, lifting, coughing and straining. Umbilical is one listed location.")

q("hernia", "A 53-year-old warehouse worker has an inguinal hernia. Which assessment finding indicates the hernia has progressed to the MOST serious stage?",
  ["A soft bulge that goes back in when he lies flat || This describes a reducible hernia",
   "A bulge that can't be pushed back, with stable vital signs || This describes incarceration with intact blood flow",
   "A bulge that grows larger when he coughs or strains || Coughing and straining raise pressure but don't show strangulation",
   "*A tender bulge with fever, tachycardia and vomiting"],
  "Strangulated hernia: blood supply is compromised, leading to ischemia and necrosis; it is an emergency. Fever, severe pain, tachycardia and nausea/vomiting suggest strangulation. Incarcerated hernias can progress to it.")

q("partial", "A 44-year-old chef with a bowel obstruction reports passing a small amount of watery stool this morning. The nurse documents a suspected partial obstruction. Which finding supports this?",
  ["*Some stool, even diarrhea, can still pass with a partial blockage",
   "Watery stool shows the obstruction has fully resolved || Partial obstruction can still pass some diarrhea",
   "Diarrhea is the main sign of a complete obstruction || In complete obstruction no stool or gas passes",
   "Passing stool means a medical emergency is underway || Complete obstruction, with no passage, is the emergency"],
  "Partial obstruction: some stool (sometimes diarrhea) or gas passes, progression is slower, and conservative care may be tried.")

q("partial", "A nurse precepting a student reviews bowel obstruction types. Which statements by the student need correction? " + SATA,
  ["*'A complete obstruction still lets some gas pass.'",
   "'Obstipation means no stool or flatus is passing.' || This statement is correct",
   "*'A partial obstruction is always a medical emergency.'",
   "'Symptoms of a complete obstruction progress fast.' || This statement is correct",
   "*'Conservative care is never tried for partial obstruction.'"],
  "Partial: some stool (sometimes diarrhea) or gas passes, slower progression, conservative care may be tried. Complete: no stool or flatus (obstipation), fast progression, medical emergency.")

q("patho", "A nursing student asks why the bowel above a blockage swells with fluid and gas. Which explanation of the early sequence is accurate?",
  ["'Peristalsis stops right away, so stool dries out.' || Peristalsis increases early, above the blockage",
   "'The bowel absorbs extra water, which pulls in gas.' || Fluid builds up in the lumen rather than being absorbed",
   "*'Peristalsis increases first, then fluid and gas build up.'",
   "'Blood pressure rises, which forces fluid into the bowel.' || Fluid loss leads to hypovolemia, not high blood pressure"],
  "Sequence: blockage, increased peristalsis, fluid and gas build up, higher lumen pressure, fluid leaks from vessels, hypovolemia/shock. Continued stretching can also cause perforation.")

q("shock", "A 58-year-old truck driver with a bowel obstruction has an hourly urine output that dropped from 50 mL to 18 mL. HR (heart rate) is 120 and BP (blood pressure) is 88/54. What is the nurse's priority action?",
  ["Encourage the client to drink more water || Oral fluids are not appropriate; circulation is supported with IV fluids",
   "Recheck the urine output in 4 hours || These signs of hypovolemic shock need prompt action",
   "*Support circulation with prescribed IV (intravenous) fluids and notify the provider",
   "Help the client walk to improve circulation || Ambulation does not treat hypovolemic shock"],
  "Hypotension, tachycardia and decreased urine output indicate hypovolemic shock from third-spacing. Support circulation with prescribed IV fluid resuscitation and notify the provider; possible ICU (intensive care unit) transfer and vasopressors if fluids alone aren't enough.")

q("shock", "A nurse is teaching a student about hypovolemic shock in a client with a bowel obstruction. Which student statement is correct?",
  ["'Bradycardia with warm, flushed skin is a typical sign.' || Shock causes tachycardia with pallor and diaphoresis",
   "'Vasopressors are always given before any IV (intravenous) fluids.' || Vasopressors are used if fluids alone aren't enough",
   "'Urine output tends to rise as the shock worsens.' || Decreased urine output is a sign of shock",
   "*'Altered mental status reflects poor brain perfusion.'"],
  "Hypovolemic shock: hypotension, tachycardia, tachypnea, decreased urine output, anxiety, pallor and diaphoresis. Altered mental status reflects poor brain perfusion.")

q("sbolbo", "A 39-year-old client with a past hernia repair is admitted with a small bowel obstruction. Which plan of care does the nurse anticipate first?",
  ["Emergency surgery for all clients with SBO (small bowel obstruction) || SBO is mostly treated conservatively",
   "*Mostly conservative treatment, since most SBOs don't need surgery",
   "A colonoscopy to remove the cancer causing the blockage || Colorectal cancer is a common cause of LBO (large bowel obstruction)",
   "Treatment for volvulus, the most common SBO cause || Adhesions and hernias are common SBO causes; volvulus is linked with LBO"],
  "SBO (small bowel obstruction) is 75-80% of obstructions, often from adhesions or hernia, and is mostly treated conservatively. LBO (large bowel obstruction) is often colorectal cancer or volvulus and often needs surgery.")

q("sbolbo", "Which findings would the nurse expect in a client with a LARGE bowel obstruction compared with a small bowel obstruction? " + SATA,
  ["*Severe, prominent abdominal distention",
   "Early, frequent vomiting that may contain bile || Early bilious vomiting points to SBO (small bowel obstruction)",
   "*Absolute obstipation",
   "Central pain that comes and goes in waves || Central, colicky, intermittent pain points to SBO",
   "*Vomiting that appears late and may contain feces"],
  "LBO (large bowel obstruction): prominent, severe distention, continuous aching lower abdominal pain, late vomiting that may contain feces, and absolute obstipation. SBO: early frequent bilious vomiting, central colicky pain, mild distention.")

q("assess", "A client with a suspected bowel obstruction has an abdominal x-ray ordered. Which additional tests does the nurse anticipate? " + SATA,
  ["*CBC (complete blood count) and electrolytes",
   "*Stool test for occult blood (guaiac)",
   "Echocardiogram to check heart valves || An echocardiogram is not a listed bowel obstruction diagnostic",
   "*Tumor marker such as CEA (carcinoembryonic antigen)",
   "*Ultrasound of the abdomen"],
  "Diagnostics for obstruction: CBC and electrolytes, stool for occult blood (guaiac), abdominal x-ray or CT (computed tomography), tumor markers such as CEA, plus MRI (magnetic resonance imaging) and ultrasound.")

q("nursing", "A 70-year-old client with a bowel obstruction has had an NG (nasogastric) tube to low suction for 6 hours. Which entry belongs on the intake and output record?",
  ["Only the IV (intravenous) fluid volume, since the client is NPO || Output, including NG output, must also be recorded",
   "*The volume of NG drainage as part of the client's output",
   "The NG drainage only when it looks bloody || All NG output is counted in strict I&O (intake and output)",
   "The client's appetite rating at each meal || The client is NPO (nothing by mouth); I&O tracks fluid"],
  "Strict I&O (intake and output) including NG output is extremely important because NG output adds to fluid and electrolyte loss. Monitor electrolytes closely.")

q("nursing", "A client with a large bowel obstruction who had been reporting severe cramping suddenly says, 'The pain just went away.' Which action should the nurse take FIRST?",
  ["Document that the obstruction is likely resolving || A sudden decrease in pain can mean perforation",
   "Offer clear liquids since the pain has eased || The client stays NPO (nothing by mouth)",
   "Turn off the NG (nasogastric) suction to rest the bowel || Decompression continues; this does not address perforation",
   "*Assess the abdomen and vital signs, then notify the provider"],
  "Any sudden increase or decrease in pain can mean perforation. Monitor VS (vital signs), pain and the abdomen; rigidity and rising heart rate must be reported promptly.")

q("interv", "A 78-year-old nursing home resident has a bowel obstruction from fecal impaction. Which intervention is LEAST appropriate as the first step?",
  ["Increasing fluids and fiber || Fluids and fiber are listed treatments for fecal impaction",
   "Giving prescribed stool softeners || Stool softeners and laxatives are listed treatments",
   "*Scheduling surgery to remove the impaction",
   "Helping the resident ambulate || Ambulation is a listed treatment for impaction"],
  "Fecal impaction is treated with fluids and fiber, stool softeners and laxatives, enemas, manual disimpaction and ambulation, not surgery as the first step.")

q("meds", "A client starting metoclopramide asks what the nurse will watch for. Which response is accurate?",
  ["'We'll watch for dependence with long-term use.' || Dependence is linked with long-term stimulant laxative use (bisacodyl)",
   "*'We'll watch for tardive dyskinesia, an involuntary movement problem.'",
   "'We'll watch for heart attack risk after 15 doses.' || The MI (myocardial infarction) risk and 15-dose limit apply to alvimopan",
   "'We'll watch for a thick mass that blocks the bowel.' || That risk is with psyllium taken without enough fluid"],
  "Metoclopramide is a prokinetic that increases motility; monitor for tardive dyskinesia.")

q("meds", "A nurse reviews teaching with four clients taking bowel medications. Which client statement needs correction?",
  ["'I'll keep drinking fluids while taking docusate.' || Maintaining fluid intake with docusate is correct",
   "'Psyllium works by adding bulk to my stool.' || Psyllium is a bulk-forming laxative; this is correct",
   "*'Bisacodyl is safe to use every day for years.'",
   "'Alvimopan is only for a short time after surgery.' || Alvimopan is short-term only; this is correct"],
  "Bisacodyl is a stimulant laxative; long-term use can cause dependence. Docusate: maintain fluids. Psyllium: bulk-forming. Alvimopan: short-term only (up to 15 doses) because of MI (myocardial infarction) risk.")

q("crc", "A 62-year-old accountant reports blood in the stool and a recent weight loss without trying. Which additional reports would the nurse recognize as possible colorectal cancer symptoms? " + SATA,
  ["*Stools that are narrower than usual",
   "*Feeling tired, with low blood counts",
   "*Bloating with a poor appetite",
   "A steady gain in body weight || Unintended weight loss, not gain, is a symptom",
   "Stools that are always formed and unchanged || A change in bowel habits is a symptom"],
  "CRC (colorectal cancer) symptoms: change in bowel habits or stool caliber, rectal bleeding or blood in the stool, anemia and fatigue from occult bleeding, unintended weight loss, incomplete emptying, bloating and anorexia.")

q("fap", "A 36-year-old client with Lynch syndrome asks how common it is as a cause of colorectal cancer. Which response is accurate?",
  ["'It causes nearly all colorectal cancers.' || Lynch syndrome accounts for 2-4% of CRC (colorectal cancer)",
   "*'It accounts for about 2 to 4 percent of colorectal cancers.'",
   "'It is the cause of about half of colorectal cancers.' || Lynch syndrome accounts for 2-4% of CRC",
   "'It is not linked to colorectal cancer at all.' || Lynch syndrome is an inherited cancer risk"],
  "Lynch syndrome is an inherited cancer risk linked to impaired DNA (deoxyribonucleic acid) repair and accounts for 2-4% of CRC (colorectal cancer).")

q("scope", "A 57-year-old client is being prepared for a colonoscopy. Which action is the nurse's responsibility before the procedure?",
  ["*Confirm that the client's consent is in place",
   "Give the client a large meal the evening before || A liquid diet is followed for about 24 hours",
   "Restart the client's anticoagulant the morning of the test || Anticoagulants are held as instructed",
   "Skip the bowel prep if the client had a BM (bowel movement) today || Bowel prep is required and must be adequate"],
  "Before colonoscopy: liquid diet about 24 hours, bowel prep, NPO (nothing by mouth) as ordered, hold anticoagulants as instructed and check PT/INR (prothrombin time/international normalized ratio) and PTT, and confirm consent.")

q("surg", "A client is 2 days post low anterior resection and reports constipation. Which prescribed intervention should the nurse question?",
  ["Incentive spirometer use every hour || Respiratory care is appropriate after surgery",
   "*A small-volume enema to relieve stool",
   "Pain medication as prescribed || Pain control is appropriate after surgery",
   "IV (intravenous) fluids at the ordered rate || IV fluids are appropriate after surgery"],
  "After a low anterior resection the anastomosis is low, so nothing goes per rectum: clarify suppositories, enemas and rectal temperatures.")

q("surg", "A nurse is caring for clients after colorectal cancer surgery. Which pairings of surgery and expected outcome are correct? " + SATA,
  ["*APR (abdominoperineal resection): permanent colostomy and a perineal wound",
   "*Hartmann procedure: rectal stump with a temporary colostomy",
   "Low anterior resection: permanent colostomy with rectum removed || Low anterior resection removes the upper rectum and reconnects",
   "*Colectomy: part or all of the colon removed",
   "Polypectomy: rectal stump left for later reconnection || Polypectomy removes a polyp during endoscopy"],
  "APR: permanent colostomy and perineal wound. Hartmann: rectal stump and temporary colostomy; reconnection may be possible later. Low anterior resection: removes the upper rectum and reconnects. Colectomy: removes part or all of the colon.")

q("periop", "A 66-year-old client is scheduled for colon cancer surgery with a planned ostomy and seems withdrawn. Which preoperative nursing actions are appropriate? " + SATA,
  ["*Offer psychosocial support for body-image changes",
   "*Teach respiratory hygiene and activity",
   "Avoid explaining the ostomy to reduce anxiety || The surgery and ostomy should be explained",
   "*Give the prescribed antibiotics",
   "Start a high-fiber diet the night before surgery || A high-fiber diet is not part of listed preop care"],
  "Preop care before CRC (colorectal cancer) surgery with an ostomy: psychosocial support for body-image changes, wound/ostomy nurse consult for stoma site planning, explaining the surgery and ostomy, prescribed antibiotics, and respiratory hygiene and activity teaching.")

q("ostomy", "A client with a new colostomy notices the stoma seems smaller at the 3-week visit. Which action should the nurse teach?",
  ["*Re-measure the stoma and cut the barrier to the new size",
   "Keep using the original wafer size from the hospital || The stoma shrinks, so the wafer must be re-measured",
   "Report the smaller stoma as a sign of failure || Shrinking over the first weeks is expected as swelling goes down",
   "Cut the wafer larger to give the stoma room to grow || The stoma shrinks; it does not grow over time"],
  "The stoma shrinks over the first several weeks as swelling goes down, so re-measure regularly and cut the barrier to fit.")

q("ostomy", "The nurse assesses four clients' stomas. Which finding should the nurse report? " + SATA,
  ["*A stoma that protrudes far out like an 'elephant trunk'",
   "A stoma that is pink and raised above the skin || Pink and raised are healthy findings",
   "*A pouch that keeps leaking onto the skin",
   "A stoma that looks moist and shiny || Moist and shiny are healthy findings",
   "*A stoma that has turned black"],
  "A healthy stoma is pink, moist, shiny and raised (PMS). Report dark or black color, retraction, excessive protrusion ('elephant trunk'), excoriated skin and leakage.")

q("ostteach", "A 74-year-old client with arthritis will care for a new colostomy at home. Which finding most affects the client's ability to perform self-care?",
  ["*Stiff fingers that make cutting the wafer difficult",
   "A preference for a two-piece pouching system || One-piece and two-piece systems are both available options",
   "A plan to clean the skin with warm water || Cleaning with warm water is correct teaching",
   "A question about foods that cause gas || Learning which foods cause odor and gas is part of teaching"],
  "Lifespan considerations affect self-care: assess vision, hand dexterity, ability to manage supplies independently, and body image and sexuality concerns.")

q("ostteach", "A client with a new ileostomy reviews home care with the nurse. Which statements show correct understanding? " + SATA,
  ["*'I'll check the skin around my stoma for irritation.'",
   "*'I'll empty the pouch before it gets one-third full.'",
   "'I'll irrigate my ileostomy each morning.' || Irrigation applies only to descending or sigmoid colostomies",
   "*'I'll keep the pouch from leaking to protect my skin.'",
   "'I'll use a strong soap to sterilize the skin.' || Clean the skin with warm water, not harsh soaps"],
  "Ostomy teaching: empty before 1/3 full, check peristomal skin for irritation, prevent leaks since moisture damages skin, clean with warm water. Irrigation applies only to descending or sigmoid colostomies.")

q("screen", "A 45-year-old client at average risk prefers a yearly test for colorectal cancer screening. Which option fits this preference?",
  ["Colonoscopy || Colonoscopy is done every 10 years",
   "CT (computed tomography) colonography || CT colonography is done every 5 years",
   "*Stool blood test",
   "Stool DNA (deoxyribonucleic acid)/RNA (ribonucleic acid) test || The stool DNA/RNA test is done every 3 years"],
  "Average-risk screening starts at 45: annual stool blood test, stool DNA/RNA test every 3 years, colonoscopy every 10 years, or CT colonography every 5 years.")
