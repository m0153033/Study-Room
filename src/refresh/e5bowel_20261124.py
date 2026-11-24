T = "e5bowel"; SET = "20261124"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("anat", "A nursing student says, 'The ileum empties straight into the rectum.' Which correction by the nurse is accurate?",
  ["'The ileum empties into the sigmoid colon through the pyloric sphincter.' || The pyloric sphincter is not between the small and large intestines",
   "'The ileum empties into the duodenum before reaching the colon.' || The duodenum is the first part of the small intestine",
   "*'The ileum empties into the cecum through the ileocecal valve.'",
   "'The ileum empties into the rectum only after the stool is formed.' || The ileum does not empty into the rectum"],
  "The ileocecal valve separates the small and large intestines; the ileum empties into the cecum through it.")

q("types", "The nurse reviews a group of clients. Which clients have a listed cause of NONmechanical obstruction (ileus)? " + SATA,
  ["*A 66-year-old with peritonitis",
   "A 70-year-old with a volvulus || Volvulus is a mechanical cause (the bowel twists)",
   "*A 58-year-old with long-standing diabetes",
   "A 61-year-old with a bowel stricture || Strictures are a mechanical cause",
   "*A 75-year-old with vascular insufficiency"],
  "Ileus (nonmechanical) causes: abdominal surgery, opioids, low potassium or magnesium, peritonitis, diabetes or Parkinson's, and vascular insufficiency. Volvulus and strictures are mechanical.")

q("types", "Bowel elimination depends on patency and peristalsis. Which statement correctly compares mechanical obstruction with ileus?",
  ["Mechanical obstruction is a peristalsis problem; ileus is a patency problem || This reverses the two",
   "Both are patency problems caused by a physical blockage || Ileus has no physical blockage",
   "Both are peristalsis problems caused by low potassium || Mechanical obstruction is a physical blockage",
   "*Mechanical obstruction is a patency problem; ileus is a peristalsis problem"],
  "Mechanical obstruction = patency problem (a physical blockage). Ileus = peristalsis problem: the bowel isn't moving and there is no blockage.")

q("mech", "The parent of a young child diagnosed with intussusception asks what is happening in the bowel. Which explanation is accurate?",
  ["*'One segment of the bowel has telescoped into the next segment.'",
   "'The bowel has twisted around itself and cut off its own path.' || That describes volvulus",
   "'Bands of scar tissue have formed and are squeezing the bowel.' || That describes adhesions",
   "'The bowel has stopped moving even though nothing blocks it.' || That describes ileus"],
  "Intussusception is one bowel segment telescoping into another. It is often discussed in pediatrics and is treated with enema reduction or surgery.")

q("hernia", "A 38-year-old client has an umbilical bulge that goes back in when the client lies down. Which hernia stage does the nurse document?",
  ["Incarcerated || Incarcerated hernia contents can't be pushed back",
   "*Reducible",
   "Strangulated || Strangulation means compromised blood supply with fever and severe pain",
   "Volvulus || Volvulus is a bowel twist, not a hernia stage"],
  "A reducible hernia goes back in. Incarcerated (irreducible) contents can't be pushed back but blood flow is intact; strangulated means the blood supply is compromised.")

q("hernia", "The nurse receives report on four clients with hernias. Which client should the nurse see FIRST?",
  ["A client with a reducible inguinal hernia asking about lifting at work || Teaching can wait; there are no signs of strangulation",
   "A pregnant client asking whether her umbilical hernia will get bigger || A stable concern that can wait",
   "*A client with an incarcerated femoral hernia who now has fever and tachycardia",
   "A client with an incisional hernia who wants a discharge pamphlet || A stable teaching need"],
  "An incarcerated hernia can progress to strangulation. Fever, severe pain, tachycardia and nausea/vomiting suggest compromised blood supply leading to ischemia and necrosis, an emergency.")

q("partial", "A nurse compares partial and complete bowel obstruction for a new graduate. Which statement is correct?",
  ["Partial obstruction progresses fast and is always a medical emergency || Partial progresses more slowly",
   "*Conservative care may be tried for partial; complete is a medical emergency",
   "Complete obstruction still allows small amounts of diarrhea to pass || Passing stool suggests partial obstruction",
   "Both types allow gas to pass, so neither one is urgent || Complete obstruction passes no gas and is an emergency"],
  "Partial: some stool (sometimes diarrhea) or gas passes, slower progression, conservative care may be tried. Complete: no stool or gas passes, symptoms progress fast, medical emergency.")

q("partial", "A client's chart states the client has obstipation. Which finding does this term describe?",
  ["Frequent small amounts of liquid stool || Passing some stool suggests partial obstruction",
   "Hyperactive bowel sounds early in an obstruction || This is a bowel sound finding, not obstipation",
   "Vomiting that may contain bile || This describes SBO vomiting, not obstipation",
   "*No passage of stool or flatus"],
  "Obstipation is no passage of stool or flatus, seen with complete obstruction.")

q("patho", "The nurse explains how fluid is lost in a bowel obstruction. Which event directly leads to fluid leaking out of the blood vessels?",
  ["Peristalsis stopping completely before the blockage forms || The sequence starts with a blockage, then increased peristalsis",
   "*Rising pressure in the lumen from fluid and gas buildup",
   "The client drinking more fluid than the bowel can absorb || Fluid loss is from a shift, not intake",
   "The large intestine absorbing extra water from stool || Fluid shifts into the lumen, not out of it"],
  "Blockage, increased peristalsis, fluid and gas build up, higher lumen pressure, fluid leaks from vessels, hypovolemia/shock. Continued stretching can also cause perforation.")

q("shock", "A client with a bowel obstruction is developing hypovolemic shock. Which actions does the nurse anticipate? " + SATA,
  ["*Prescribed IV (intravenous) fluid resuscitation",
   "Encouraging the client to drink oral fluids || The client is NPO (nothing by mouth) with an obstruction",
   "*Notifying the provider of the findings",
   "*Possible transfer to the ICU (intensive care unit)",
   "*Vasopressors if fluids alone aren't enough"],
  "Hypovolemic shock from third-spacing: support circulation with prescribed IV fluid resuscitation and notify the provider; possible ICU transfer and vasopressors if fluids alone aren't enough.")

q("shock", "Four clients with bowel obstruction are on the nurse's assignment. Which client should the nurse assess FIRST?",
  ["A client with mild distention who is still passing some gas || Partial obstruction findings; stable",
   "A client asking for a warm blanket and help to reposition || A comfort need that can wait",
   "*A client who is anxious, pale and diaphoretic with a falling BP (blood pressure)",
   "A client whose NG (nasogastric) tube is draining with suction on || An expected finding"],
  "Anxiety, pallor, diaphoresis and hypotension are signs of hypovolemic shock from fluid shifting into the bowel lumen. Support circulation with prescribed IV fluids and notify the provider.")

q("sbolbo", "Which statements correctly compare small and large bowel obstruction? " + SATA,
  ["*SBO (small bowel obstruction) makes up about 75-80% of obstructions",
   "LBO (large bowel obstruction) causes early vomiting that may contain bile || Early bilious vomiting is typical of SBO",
   "*LBO is often caused by colorectal cancer or volvulus",
   "SBO pain is continuous and aching in the lower abdomen || SBO pain is central, colicky and intermittent",
   "*SBO is mostly treated conservatively"],
  "SBO: 75-80%, often adhesions or hernia, mostly conservative. LBO: 20-25%, often colorectal cancer or volvulus, often needs surgery, with continuous aching lower pain and late vomiting.")

q("sbolbo", "A client is admitted early in the course of a small bowel obstruction. Which finding does the nurse expect?",
  ["Absolute obstipation from the very start || Absolute obstipation is typical of LBO",
   "Vomiting that may contain feces || Feculent vomiting is a late LBO finding",
   "Severe, prominent abdominal distention || SBO causes mild distention",
   "*Gas and stool may still pass early on"],
  "SBO: early frequent vomiting that may contain bile, central colicky intermittent pain, mild distention, and gas and stool may still pass early.")

q("assess", "Why does the nurse ask a client with suspected obstruction about previous abdominal surgery?",
  ["Previous surgery rules out a mechanical obstruction || Surgery is linked to mechanical causes such as adhesions",
   "*Adhesions after abdominal surgery are a common cause of obstruction",
   "Previous surgery decides whether an x-ray is allowed || Imaging is not limited by surgical history",
   "Previous surgery mainly raises colorectal cancer risk || Surgical history is asked because of adhesions"],
  "Adhesions are scar tissue, often after abdominal surgery, and are a very common cause of obstruction. History also includes opioid or laxative use, gas and last BM, weight loss and family history of cancer.")

q("nursing", "A client with a small bowel obstruction and an NG (nasogastric) tube to suction asks for a glass of water. Which response is best?",
  ["'A few sips of water won't affect your tube, so go ahead.' || The client is NPO (nothing by mouth)",
   "'You can drink as much as you like once the IV is running.' || IV fluids replace losses; the client stays NPO",
   "*'You need to stay NPO for now; I can help you with oral care.'",
   "'I'll get you some juice instead, since it has electrolytes.' || The client is NPO"],
  "Care for bowel obstruction includes NPO with oral care, NG decompression, IV fluids for replacement and maintenance, and strict I&O including NG output.")

q("nursing", "Which assessments should the nurse monitor closely for a client with a bowel obstruction? " + SATA,
  ["*Vital signs",
   "*Electrolyte levels",
   "Percent of each meal eaten || The client is NPO (nothing by mouth)",
   "*Pain level",
   "*Abdominal findings"],
  "Monitor VS (vital signs), electrolytes, pain and the abdomen, along with strict I&O including NG output. A sudden increase or decrease in pain can signal perforation.")

q("interv", "Which pairing of obstruction cause and intervention is correct?",
  ["Postoperative ileus: immediate surgery || Treated with ambulation and prokinetics",
   "Opioid-related ileus: manual disimpaction || Treated with a mu-opioid antagonist",
   "*Intussusception: surgery or enema reduction",
   "Fecal impaction: surgery as the first step || Treated with fluids, fiber, softeners, laxatives, enemas, disimpaction, ambulation"],
  "Hernia, volvulus, tumor or stricture: usually surgery. Intussusception: surgery or enema reduction. Postoperative ileus: ambulation and prokinetics. Opioid ileus: mu-opioid antagonist.")

q("meds", "A client taking docusate sodium calls to report several loose stools. What should the nurse tell the client?",
  ["'Double the dose so it works faster.' || Diarrhea is a reason to stop it, not increase it",
   "'Drink less fluid until the stools firm up.' || Fluid intake should be maintained",
   "'Keep taking it; loose stool means it's working.' || Docusate should be stopped if diarrhea occurs",
   "*'Stop taking the docusate if diarrhea occurs.'"],
  "Docusate softens stool. Teach: maintain fluid intake, stop it if diarrhea occurs, and it may take 1-3 days to work.")

q("meds", "A postoperative client is prescribed alvimopan. The client asks what the drug does. Which explanation is accurate?",
  ["*'It binds opioid receptors in the gut to help prevent postoperative ileus.'",
   "'It softens your stool by drawing water into it.' || That describes a stool softener such as docusate",
   "'It stimulates the bowel and can be used long-term.' || Alvimopan is short-term only",
   "'It adds bulk to your stool to enlarge the fecal mass.' || That describes psyllium"],
  "Alvimopan binds GI (gastrointestinal) opioid receptors to prevent postoperative ileus. Short-term use only, up to 15 doses, because of MI (myocardial infarction) risk.")

q("crc", "Which client has the MOST risk factors for colorectal cancer?",
  ["A 32-year-old nonsmoker who runs daily || Younger age and exercise are not risk factors",
   "A 41-year-old who exercises and avoids alcohol || Few listed risk factors",
   "*A 56-year-old with ulcerative colitis who smokes and is inactive",
   "A 28-year-old who eats a low-fat diet and walks daily || No listed risk factors"],
  "CRC (colorectal cancer) risks: age over 50, high animal-fat diet, smoking and alcohol, inflammatory bowel disease, physical inactivity, family or personal history, Lynch syndrome and FAP.")

q("fap", "A 42-year-old client is told genetic testing shows Lynch syndrome. The client asks what this means. Which response is accurate?",
  ["'You will develop hundreds to thousands of colon polyps.' || That describes FAP (familial adenomatous polyposis)",
   "'It is a type of hernia that can block the bowel.' || Lynch syndrome is an inherited cancer risk",
   "*'It is an inherited cancer risk linked to impaired DNA repair.'",
   "'It was caused by a high-fat diet and can be reversed.' || Lynch syndrome is inherited"],
  "Lynch syndrome is an inherited cancer risk linked to impaired DNA (deoxyribonucleic acid) repair and accounts for 2-4% of CRC (colorectal cancer).")

q("scope", "Before a colonoscopy, the nurse checks PT/INR (prothrombin time/international normalized ratio) and PTT. What is the reason?",
  ["To confirm the bowel prep was adequate || Prep is checked by looking at the stools",
   "*Biopsies are likely, so bleeding risk matters",
   "To decide how long the liquid diet should last || Lab values don't set the diet length",
   "To screen for colorectal cancer tumor markers || CEA (carcinoembryonic antigen) is the tumor marker"],
  "Before colonoscopy: liquid diet about 24 hours, bowel prep, NPO as ordered, hold anticoagulants as instructed and check PT/INR and PTT, confirm consent. Biopsies are likely, so bleeding risk matters.")

q("surg", "A client had a Hartmann procedure and asks whether the colostomy is permanent. Which response is accurate?",
  ["'Yes, this surgery always creates a permanent colostomy.' || That describes an APR (abdominoperineal resection)",
   "'You don't have a colostomy; the bowel was reconnected.' || Hartmann creates a temporary colostomy",
   "'Your rectum was removed, so a perineal wound will heal.' || Rectum removal with a perineal wound describes APR",
   "*'A rectal stump was left, and reconnection may be possible later.'"],
  "The Hartmann procedure leaves a rectal stump and creates a temporary colostomy; reconnection may be possible later.")

q("surg", "Which colorectal surgery results in a PERMANENT colostomy?",
  ["Hartmann procedure || It creates a temporary colostomy",
   "*Abdominoperineal resection (APR)",
   "Low anterior resection || It removes the upper rectum and reconnects",
   "Polypectomy || It removes a polyp during endoscopy"],
  "APR results in a permanent colostomy and a perineal wound. Hartmann: temporary colostomy with a rectal stump. Low anterior resection: reconnects. Polypectomy: removes a polyp endoscopically.")

q("periop", "A client is 1 day post colon surgery. Which assessments should the nurse monitor? " + SATA,
  ["*Intake and output",
   "*Bowel sounds",
   "*NG (nasogastric) tube and drains",
   "Tolerance of a high-fiber breakfast || The client is NPO at first, then advanced toward low-residue",
   "*Ostomy output"],
  "After colon surgery: NPO at first, then advanced as prescribed toward a low-residue diet. Monitor I&O, abdomen, bowel sounds, NG, drains, wounds and ostomy output.")

q("ostomy", "Which client would the nurse expect to have the FIRMEST ostomy output?",
  ["A client with an ileostomy || Ileostomy output is the most liquid",
   "A client with a transverse colostomy || Less water is absorbed than further along the colon",
   "A client with a descending colostomy || Descending output is semisolid",
   "*A client with a sigmoid colostomy"],
  "The closer to the rectum, the more water absorbed and the firmer the stool. Sigmoid colostomy output is more solid.")

q("ostomy", "The nurse assesses a client's colostomy stoma. Which finding should be reported to the provider?",
  ["The stoma is pink in color || Pink is a healthy stoma finding",
   "*The stoma has retracted below the skin",
   "The stoma is moist and shiny || Moist and shiny are healthy findings",
   "The stoma is raised above the skin || Raised is a healthy finding"],
  "Healthy stoma: pink, moist, shiny and raised (PMS). Report dark or black color, retraction, excessive protrusion, excoriated skin and leakage.")

q("ostteach", "A client with a new ileostomy asks whether irrigation will help regulate output. Which response is accurate?",
  ["'Yes, irrigation works for any type of ostomy.' || Irrigation applies only to descending or sigmoid colostomies",
   "*'Irrigation applies only to descending or sigmoid colostomies.'",
   "'Yes, but only if you irrigate at least twice a day.' || Irrigation does not apply to an ileostomy",
   "'Irrigation is mainly used for ascending colostomies.' || Not listed for ascending colostomies"],
  "Colostomy irrigation applies only to descending or sigmoid colostomies and requires instruction and orders.")

q("ostteach", "A home health nurse sees that a client cuts the wafer opening about 1 inch larger than the stoma. What is the nurse's concern?",
  ["The wafer will press on the stoma and cut off blood flow || A larger opening doesn't press on the stoma",
   "The pouch will need to be emptied less often than usual || Opening size doesn't change emptying",
   "*Exposed skin can be damaged by leakage and moisture",
   "The stoma will grow to fill the larger opening || The stoma shrinks over the first weeks"],
  "Cut the barrier to within 1/8 inch of the stoma. Prevent leaks, since moisture damages skin; check the peristomal skin for irritation.")

q("screen", "A 47-year-old client at average risk asks about colorectal cancer screening. Which options and intervals are correct? " + SATA,
  ["*Stool blood test every year",
   "Stool DNA (deoxyribonucleic acid)/RNA test every year || The stool DNA/RNA test is every 3 years",
   "*Colonoscopy every 10 years",
   "*CT (computed tomography) colonography every 5 years",
   "Colonoscopy every 3 years || Average-risk colonoscopy is every 10 years"],
  "Average-risk screening starts at 45: annual stool blood test, stool DNA/RNA test every 3 years, colonoscopy every 10 years, or CT colonography every 5 years.")
