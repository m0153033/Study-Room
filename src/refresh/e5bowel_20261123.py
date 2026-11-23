T = "e5bowel"; SET = "20261123"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("anat", "A 58-year-old client in a GI clinic asks what the large intestine does compared with the small intestine. Which response by the nurse is correct?",
  ["It mainly absorbs most of the nutrients from digested food || Nutrient absorption is the job of the small intestine (duodenum, jejunum, ileum)",
   "It makes the bile that is used to digest fats || Bile is not made by the large intestine",
   "*It mainly absorbs water and carries out elimination",
   "It produces insulin to control blood glucose || Insulin is not made by the intestine"],
  "The small intestine (duodenum, jejunum, ileum) absorbs nutrients; the large intestine absorbs water and carries out elimination.")

q("types", "A 71-year-old client with Parkinson's disease takes opioids for chronic pain and has a potassium level below normal. The abdomen is distended with hypoactive bowel sounds, and a CT shows no physical blockage. How should the nurse classify this problem?",
  ["Mechanical obstruction caused by adhesions from scar tissue || Adhesions are a physical blockage, and imaging showed none",
   "Mechanical obstruction caused by a volvulus twisting the bowel || Volvulus is a physical twist of the bowel, which imaging would show",
   "Strangulated hernia that needs emergency surgical repair || A hernia is a mechanical cause; no blockage was found",
   "*Nonmechanical obstruction (ileus) from impaired peristalsis"],
  "Ileus is a nonmechanical obstruction: the bowel isn't moving, with no physical blockage. Opioids, low potassium or magnesium, and Parkinson's disease are listed causes.")

q("types", "The nurse reviews several clients on a surgical unit. Which conditions are MECHANICAL causes of bowel obstruction? " + SATA,
  ["*A colon tumor narrowing the lumen",
   "*Fecal impaction in an immobile older adult",
   "*Scar-tissue adhesions from a prior abdominal surgery",
   "Low magnesium in a client with poor intake || Electrolyte imbalance causes nonmechanical obstruction (ileus)",
   "*An intussusception, where one bowel segment telescopes into another"],
  "Mechanical causes are physical blockages: adhesions, tumors, fecal impaction, volvulus, intussusception, strictures and hernias. Low potassium or magnesium causes ileus (impaired peristalsis).")

q("mech", "A nursing student describes the mechanical causes of obstruction. Which statement by the student is correct?",
  ["Volvulus is scar tissue that forms after abdominal surgery and constricts the bowel || That describes adhesions",
   "*Volvulus is the bowel twisting on itself and is usually treated surgically",
   "Volvulus is one bowel segment telescoping into another, reduced by enema || That describes intussusception",
   "Volvulus is bowel pushing through a weak spot in the muscular abdominal wall || That describes a hernia"],
  "Volvulus is a twist of the bowel on itself, a common cause of large bowel obstruction that usually requires surgery. Adhesions are scar tissue; intussusception is telescoping.")

q("hernia", "A nurse teaches a community group about hernia prevention. Which factors raise intra-abdominal pressure and contribute to hernia formation? " + SATA,
  ["*Obesity",
   "*Heavy lifting",
   "*Chronic coughing",
   "*Straining",
   "Low potassium levels || Low potassium is a cause of ileus, not hernia"],
  "A hernia forms from a weak spot in the muscular wall plus increased abdominal pressure. Pressure rises with obesity, pregnancy, lifting, coughing and straining.")

q("hernia", "A 49-year-old client with a known incarcerated inguinal hernia now has a temperature of 101.4 F, severe groin pain, HR (heart rate) 118, and vomiting. What should the nurse conclude?",
  ["The hernia has become reducible and can be pushed back || A reducible hernia doesn't cause fever and severe pain",
   "These are expected findings for an incarcerated hernia || Fever, tachycardia and severe pain are not expected; they signal progression",
   "*The hernia may be strangulated; report it immediately",
   "The client likely has constipation and needs a laxative || These findings point to compromised blood supply, not constipation"],
  "An incarcerated hernia can progress to strangulation. Fever, severe pain, tachycardia and nausea/vomiting suggest the blood supply is compromised, leading to ischemia and necrosis; this is an emergency.")

q("partial", "A client is admitted with a COMPLETE bowel obstruction. Which finding does the nurse expect?",
  ["Small amounts of loose, diarrhea-like stool passing || Some stool or diarrhea passing suggests partial obstruction",
   "Symptoms worsening slowly over several days || Slow progression fits partial obstruction",
   "Occasional passage of flatus || Passing gas suggests partial obstruction",
   "*No passage of stool or gas (obstipation)"],
  "Complete obstruction: no stool or flatus passes (obstipation), symptoms progress fast, and it is a medical emergency.")

q("partial", "Which findings are consistent with a PARTIAL bowel obstruction? " + SATA,
  ["*The client still passes some gas",
   "*Small amounts of stool, sometimes diarrhea, are passing",
   "*Symptoms are progressing more slowly",
   "There has been no flatus or stool for 2 days || Absent stool and gas (obstipation) indicates complete obstruction",
   "Rapid progression that is treated as a medical emergency || Rapid progression describes complete obstruction"],
  "In partial obstruction some stool (sometimes diarrhea) or gas passes, progression is slower, and conservative care may be tried.")

q("patho", "On admission, a client with a bowel obstruction had hyperactive bowel sounds. The next day the sounds are diminished. How should the nurse interpret this?",
  ["The obstruction has resolved and the bowel is back to normal || Diminishing sounds don't mean the blockage cleared",
   "*Early hyperactive sounds may diminish as obstruction progresses",
   "The first assessment was likely done incorrectly by the nurse || Early hyperactive sounds are a known finding",
   "Diminished sounds prove there is no obstruction at all now || Sounds can diminish later in an obstruction"],
  "Early in an obstruction, peristalsis increases above the blockage, so sounds may be hyperactive; don't be thrown off, because they may diminish later.")

q("shock", "A client with a small bowel obstruction has third-spaced a large volume of fluid. Which findings suggest hypovolemic shock is developing? " + SATA,
  ["*Anxiety and diaphoresis",
   "*Pale skin",
   "*Rising respiratory rate",
   "*Urine output dropping",
   "Bradycardia with warm, flushed skin || Hypovolemic shock causes tachycardia and pallor, not bradycardia and flushing"],
  "Hypovolemic shock: hypotension, tachycardia, tachypnea, decreased urine output, anxiety, pallor and diaphoresis. Altered mental status reflects poor brain perfusion.")

q("shock", "A 77-year-old client with a bowel obstruction becomes newly confused. BP (blood pressure) is 86/52 and HR (heart rate) is 126. What best explains the confusion?",
  ["Expected effect of being NPO (nothing by mouth) || Being NPO does not explain new confusion with hypotension",
   "Normal sundowning in an older adult || Confusion with hypotension and tachycardia signals shock, not a normal change",
   "Fluid overload from the IV (intravenous) fluids || Low BP and high HR point to volume loss, not overload",
   "*Poor brain perfusion from hypovolemic shock"],
  "Fluid shifts into the bowel lumen lower circulating volume, causing hypovolemic shock. Altered mental status reflects poor brain perfusion. Fluid resuscitation is supported and the provider notified.")

q("sbolbo", "A 74-year-old client with a history of colorectal cancer has severe, prominent abdominal distention, continuous aching lower abdominal pain, and has passed no stool or gas. Which condition do these findings suggest?",
  ["Small bowel obstruction from adhesions || SBO causes colicky central pain, mild distention and early vomiting",
   "*Large bowel obstruction",
   "Postoperative ileus || Ileus is nonmechanical and follows surgery; this client has a cancer history and LBO findings",
   "Partial obstruction || No passage of stool or gas indicates complete obstruction"],
  "LBO (large bowel obstruction): prominent distention, continuous aching lower pain, late feculent vomiting and absolute obstipation. Colorectal cancer and volvulus are common causes; it often needs surgery.")

q("sbolbo", "A 52-year-old client who had abdominal surgery years ago is admitted with a small bowel obstruction. Which finding is MOST consistent with SBO rather than LBO (large bowel obstruction)?",
  ["Vomiting that contains feces early in the course || Vomiting that may contain feces is a late LBO finding",
   "Severe, prominent distention of the whole abdomen || Prominent distention is typical of LBO; SBO causes mild distention",
   "*Early, frequent vomiting that may contain bile",
   "Continuous, aching pain in the lower abdomen || Continuous lower pain fits LBO; SBO pain is central and colicky"],
  "SBO (75-80% of obstructions, often from adhesions or hernia): early frequent vomiting that may be bilious, central colicky intermittent pain, mild distention, and gas/stool may still pass early. Treatment is mostly conservative.")

q("assess", "A nurse has just inspected the abdomen of a client with suspected bowel obstruction. Which action should the nurse perform NEXT?",
  ["Palpate all four quadrants for tenderness and rigidity || Palpation comes last, after auscultation and percussion",
   "Percuss all four quadrants for tympany and dullness || Auscultation comes before percussion",
   "*Auscultate bowel sounds in all four quadrants",
   "Ask the client to bear down while palpating || Palpation is not the next step"],
  "Abdominal assessment order: inspect, auscultate, percuss, palpate. Auscultate before palpating, listening at least a minute per quadrant if needed.")

q("nursing", "A client with a bowel obstruction has a Salem sump NG (nasogastric) tube to suction. Which actions belong in the plan of care? " + SATA,
  ["*Provide frequent oral care while the client is NPO (nothing by mouth)",
   "*Include NG drainage in the strict I&O (intake and output) record",
   "*Monitor electrolyte results closely",
   "Offer sips of clear liquids for comfort || The client is NPO with NG decompression",
   "*Maintain IV (intravenous) fluids for replacement and maintenance"],
  "Care includes NPO with oral care, NG decompression, IV fluids, and strict I&O including NG output, since NG output adds to fluid and electrolyte loss. Monitor VS, electrolytes, pain and the abdomen.")

q("nursing", "A client with a small bowel obstruction suddenly reports that the abdominal pain has become much worse. The abdomen is rigid and HR (heart rate) has risen. What is the nurse's priority?",
  ["Reposition the client and recheck in an hour || Delaying care is unsafe when perforation is suspected",
   "*Notify the provider promptly about possible perforation",
   "Give a prescribed laxative to relieve the blockage || Laxatives don't treat suspected perforation",
   "Increase the NG (nasogastric) suction pressure || This doesn't address suspected perforation"],
  "Any sudden increase or decrease in pain can signal perforation. A rigid abdomen and rising HR must be reported promptly.")

q("interv", "A 63-year-old client develops an ileus that is attributed to opioid use. Which type of drug does the nurse anticipate?",
  ["A barium enema to clear the bowel || Barium enema is not listed as a treatment for ileus",
   "Immediate surgical repair || Surgery is for causes such as hernia, volvulus, tumor or stricture",
   "*A mu-opioid antagonist",
   "Manual disimpaction of stool || This treats fecal impaction, not opioid-related ileus"],
  "Postoperative ileus is treated with ambulation and prokinetics; opioid-related ileus is treated with a mu-opioid antagonist.")

q("meds", "A nurse reviews a medication list for a client with slowed bowel motility. Which drug is a prokinetic that increases GI (gastrointestinal) motility?",
  ["Bisacodyl || Bisacodyl is a stimulant laxative",
   "Psyllium || Psyllium is a bulk-forming laxative",
   "*Metoclopramide",
   "Docusate sodium || Docusate is a stool softener"],
  "Metoclopramide is a prokinetic that increases motility; the nurse monitors for tardive dyskinesia.")

q("meds", "The nurse teaches a client about bowel medications. Which client statement indicates a need for MORE teaching?",
  ["'I need to keep drinking fluids while I take psyllium.' || Correct; fluids prevent a thick mass that can obstruct",
   "*'I can keep taking alvimopan every day for as long as I need it.'",
   "'Using bisacodyl long-term could make me dependent on it.' || Correct; long-term stimulant use can cause dependence",
   "'Docusate may take 1 to 3 days to work.' || Correct teaching for docusate"],
  "Alvimopan is for short-term use only (up to 15 doses) because of MI (myocardial infarction) risk; it binds GI opioid receptors to prevent postoperative ileus.")

q("crc", "A 60-year-old client with anemia and narrowing stools is told a CEA (carcinoembryonic antigen) level was drawn. The client asks whether this test will show if they have cancer. Which response is best?",
  ["'Yes, a high CEA level by itself confirms that you have colorectal cancer.' || CEA does not confirm the diagnosis",
   "'No, a stool guaiac test for blood is the test that confirms cancer.' || Guaiac detects occult blood but doesn't confirm cancer",
   "'No, an abdominal x-ray is the test that will confirm the diagnosis.' || X-ray does not confirm colorectal cancer",
   "*'CEA mainly monitors treatment; a colonoscopy with biopsy confirms it.'"],
  "Colonoscopy with biopsy confirms colorectal cancer. CEA is a tumor marker used to monitor treatment.")

q("fap", "A 16-year-old whose parent has familial adenomatous polyposis (FAP) asks about the condition. Which statement by the nurse is accurate?",
  ["'FAP is caused by eating a high-fat diet, so diet changes prevent it.' || FAP is inherited, not diet-caused",
   "*'Polyps can start in the teen years; early colon removal may be discussed.'",
   "'FAP is the same condition as Lynch syndrome, just with another name.' || Lynch syndrome is a different inherited risk tied to impaired DNA repair",
   "'FAP rarely leads to cancer, so screening can wait until later in life.' || FAP carries a near 100% lifetime cancer risk"],
  "FAP: hundreds to thousands of polyps, starting as early as the teen years, with near 100% lifetime cancer risk; prophylactic colectomy may be discussed.")

q("scope", "The nurse reviews colonoscopy prep instructions with a 54-year-old client. Which client statement indicates a need for MORE teaching?",
  ["'I'll follow a liquid diet for about 24 hours before the test.' || Correct preparation",
   "'I'll complete the bowel prep and stay NPO as ordered.' || Correct preparation",
   "*'I'll eat a big dinner the night before so I have energy.'",
   "'I'll hold my anticoagulant the way my provider instructed.' || Correct; biopsies make bleeding risk important"],
  "Before colonoscopy: liquid diet about 24 hours, bowel prep, NPO as ordered, hold anticoagulants as instructed with PT/INR and PTT checked, and confirm consent. A large meal is not appropriate.")

q("surg", "A client returns from an abdominoperineal resection (APR) for rectal cancer. Which nursing action is MOST appropriate?",
  ["Teach that the colostomy will be reversed in a few months || APR creates a permanent colostomy",
   "*Assess both the abdominal incision and the perineal wound",
   "Expect only a temporary ileostomy || APR results in a permanent colostomy",
   "Plan to take rectal temperatures || After APR the rectum is removed"],
  "APR results in a permanent colostomy and a perineal wound; the nurse monitors both the abdominal and perineal sites.")

q("surg", "A client is 1 day post low anterior resection. Which orders should the nurse clarify with the provider? " + SATA,
  ["*Rectal temperature every 4 hours",
   "*Tap-water enema for constipation",
   "*Rectal suppository for fever",
   "Incentive spirometer every hour while awake || Appropriate postoperative care",
   "IV (intravenous) fluids at the prescribed rate || Appropriate postoperative care"],
  "After a low anterior resection the anastomosis is low, so nothing goes per rectum: clarify suppositories, enemas and rectal temperatures.")

q("periop", "A client is scheduled for colorectal cancer surgery with a planned ostomy. Which preoperative action is MOST important?",
  ["Avoid discussing the ostomy so the client won't be anxious || Teaching and psychosocial support are part of preop care",
   "Start a high-fiber diet the morning of surgery || Diet is not part of listed preop priorities",
   "*Arrange a wound/ostomy nurse consult to plan the stoma site",
   "Hold all prescribed antibiotics until after surgery || Prescribed antibiotics are part of preop care"],
  "Preop care includes psychosocial support for body-image changes, a wound/ostomy nurse consult for stoma site planning, explaining the surgery and ostomy, and prescribed antibiotics.")

q("ostomy", "On postoperative day 2, the nurse finds that a client's new colostomy stoma is dark purple. What is the priority action?",
  ["Document it as an expected postoperative finding || A healthy stoma is pink, moist and shiny",
   "Cut the wafer larger and recheck tomorrow || Delaying is unsafe; dark color must be reported",
   "Apply warm compresses to the stoma || This doesn't address an abnormal stoma color",
   "*Report the stoma color to the provider promptly"],
  "A healthy stoma is pink, moist, shiny and raised (PMS). Dark or black color, retraction, excessive protrusion, excoriated skin and leakage should be reported.")

q("ostomy", "A client has a new descending colostomy and asks what the stool will be like. Which consistency should the nurse describe?",
  ["*Semisolid",
   "Liquid || Liquid output is expected from an ileostomy",
   "Clear fluid only || This is not expected colostomy output",
   "No stool at all || A colostomy does pass stool"],
  "The closer the stoma is to the rectum, the more water is absorbed and the firmer the stool: ileostomy is liquid, descending colostomy is semisolid, sigmoid colostomy is more solid.")

q("ostteach", "The nurse evaluates a client's ostomy teaching. Which statement indicates a need for MORE teaching?",
  ["'I'll cut the wafer opening to within 1/8 inch of my stoma.' || Correct wafer sizing",
   "'I'll clean the skin around my stoma with warm water.' || Correct skin care",
   "*'I'll wait until the pouch is completely full before I empty it.'",
   "'I'll check the skin around the stoma for irritation.' || Correct; peristomal skin should be checked"],
  "Empty the pouch before it is 1/3 full (often every 4-6 hours). Cut the wafer within 1/8 inch of the stoma, clean with warm water, and check peristomal skin.")

q("ostteach", "Which instructions should the nurse include when teaching a client with a new colostomy? " + SATA,
  ["*Change the appliance about twice a week",
   "*Re-measure the stoma because it shrinks over the first several weeks",
   "*Learn which foods cause odor and gas",
   "Scrub the skin with a harsh soap to sterilize it || Use warm water; harsh soaps irritate the skin",
   "*Prevent leaks, because moisture damages the skin"],
  "Ostomy teaching: empty before 1/3 full, change the appliance about twice a week, measure and cut the barrier to fit, clean with warm water, check skin, prevent leaks, and learn foods that cause odor and gas. The stoma shrinks as swelling goes down, so re-measure.")

q("screen", "A 45-year-old client at average risk asks about colorectal cancer screening options. Which option and interval is correct?",
  ["Colonoscopy every year || Average-risk colonoscopy is every 10 years",
   "CT (computed tomography) colonography every 10 years || CT colonography is every 5 years",
   "*Stool DNA (deoxyribonucleic acid)/RNA test every 3 years",
   "Wait to begin screening until age 60 || Average-risk screening begins at 45"],
  "Average-risk screening begins at 45: annual stool blood test, stool DNA/RNA test every 3 years, colonoscopy every 10 years, or CT colonography every 5 years.")
