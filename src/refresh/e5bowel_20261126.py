T = "e5bowel"; SET = "20261126"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("anat", "A 50-year-old client asks why stool becomes firmer as it moves through the colon. Which response by the nurse is accurate?",
  ["'The ileocecal valve squeezes the water out of it.' || The ileocecal valve separates the small and large intestines",
   "'The small intestine adds bile that hardens it.' || The small intestine absorbs nutrients",
   "*'The large intestine absorbs water as stool moves along.'",
   "'The rectum adds fiber that firms up the stool.' || The large intestine's job is water absorption and elimination"],
  "The small intestine (duodenum, jejunum, ileum) absorbs nutrients; the large intestine absorbs water and carries out elimination.")

q("types", "A client has abdominal distention and hypoactive bowel sounds. Which finding best supports ileus rather than a mechanical obstruction?",
  ["CT shows the bowel twisted on itself || A twisted bowel (volvulus) is mechanical",
   "*Imaging shows no physical blockage",
   "A tumor is seen narrowing the colon || Tumors are mechanical causes",
   "An incarcerated hernia is found on exam || Hernias are mechanical causes"],
  "Ileus is a nonmechanical obstruction: impaired peristalsis with no physical blockage. Mechanical causes include adhesions, tumors, impaction, volvulus, intussusception, strictures and hernias.")

q("types", "A nursing student describes ileus. Which statements by the student are correct? " + SATA,
  ["*'Ileus is a problem with peristalsis.'",
   "*'A low potassium level can cause ileus.'",
   "*'Vascular insufficiency is one cause.'",
   "'A stricture is a common cause of ileus.' || Strictures are mechanical causes",
   "'Ileus always shows a blockage on CT.' || Ileus has no physical blockage"],
  "Ileus (nonmechanical) is a peristalsis problem with no blockage. Causes: abdominal surgery, opioids, low potassium or magnesium, peritonitis, diabetes or Parkinson's, and vascular insufficiency.")

q("mech", "Which pairing of a mechanical obstruction cause and its description is correct?",
  ["Volvulus: one segment telescopes into the next || That describes intussusception",
   "Intussusception: scar tissue that squeezes the bowel || That describes adhesions",
   "Adhesions: the bowel twisting on itself || That describes volvulus",
   "*Adhesions: scar tissue that can constrict the bowel"],
  "Adhesions are scar tissue, often after abdominal surgery, that constrict the bowel. Volvulus is a twist; intussusception is telescoping.")

q("hernia", "Which hernia description represents an emergency?",
  ["A bulge that goes back in when the client lies down || That is a reducible hernia",
   "*Contents trapped with blood supply compromised",
   "Contents that can't be pushed back but have intact blood flow || That is incarcerated; it can progress but blood flow is intact",
   "A weak spot that has not yet formed a bulge || No hernia has formed yet"],
  "Strangulated hernia: blood supply compromised, leading to ischemia and necrosis, an emergency. Incarcerated hernias can progress to strangulation.")

q("hernia", "A 42-year-old mover with a reducible inguinal hernia explains why it formed. Which statement shows understanding?",
  ["'My low potassium and pain pills caused it.' || Low potassium and opioids cause ileus",
   "'My bowel twisted on itself during a lift.' || A twisted bowel is volvulus",
   "*'A weak spot in my wall plus pressure from lifting.'",
   "'Polyps in my colon pushed through the wall.' || Polyps are not a hernia cause"],
  "A hernia forms from a weak spot in the muscular wall plus increased abdominal pressure (obesity, pregnancy, lifting, coughing, straining).")

q("partial", "Which features describe a COMPLETE bowel obstruction? " + SATA,
  ["*No passage of stool or flatus",
   "Small amounts of diarrhea still passing || This fits partial obstruction",
   "*Symptoms that progress quickly",
   "*It is treated as a medical emergency",
   "Conservative care is usually tried first || Conservative care may be tried for partial obstruction"],
  "Complete obstruction: no stool or flatus passes (obstipation), symptoms progress fast, and it is a medical emergency. Partial: some stool or gas passes, slower progression, conservative care may be tried.")

q("partial", "A client with a partial obstruction had been passing small amounts of gas. Now no gas or stool has passed for 18 hours and symptoms are rapidly worsening. What does this change suggest?",
  ["The obstruction is resolving on its own || Losing all passage of gas and stool is worsening",
   "This is still expected with a partial obstruction || Partial obstruction still lets some gas or stool pass",
   "*Progression to a complete obstruction, an emergency",
   "Simple constipation that needs a laxative || No stool or flatus with fast progression is complete obstruction"],
  "Complete obstruction means no passage of stool or flatus, rapid progression, and a medical emergency.")

q("patho", "A client with a bowel obstruction who is not bleeding asks why large amounts of IV fluid are needed. Which explanation is best?",
  ["'Your bowel is absorbing extra water from your blood.' || Fluid leaks out of the vessels into the bowel",
   "*'Fluid is shifting out of your vessels into the bowel.'",
   "'Your blood pressure is too high and needs diluting.' || Third-spacing lowers circulating volume and BP",
   "'The IV fluid helps dissolve the blockage.' || IV fluids replace volume; they don't clear the blockage"],
  "Rising lumen pressure makes fluid and electrolytes leak from the vessels into the bowel lumen. This third-spacing lowers circulating volume and can cause hypovolemic shock.")

q("shock", "A nurse explains to a student why the urine output of a client with an obstruction has dropped. Which explanation is accurate?",
  ["The NG tube is adding fluid that dilutes the urine || NG output removes fluid; it adds to fluid loss",
   "Low urine output is expected while NPO and needs no action || Decreased urine output is a sign of hypovolemic shock",
   "The client is drinking too much and the kidneys are tired || The client is NPO; fluid is lost to the bowel",
   "*Third-spacing into the bowel lowered circulating volume"],
  "Fluid shifting into the bowel lumen lowers circulating volume. Decreased urine output, with hypotension, tachycardia and tachypnea, signals hypovolemic shock.")

q("shock", "Which assessments should the nurse trend to detect hypovolemic shock in a client with a bowel obstruction? " + SATA,
  ["*Blood pressure",
   "*Heart rate",
   "*Respiratory rate",
   "*Urine output",
   "Number of meals eaten || The client is NPO; this doesn't reflect circulating volume",
   "*Mental status"],
  "Hypovolemic shock: hypotension, tachycardia, tachypnea, decreased urine output, anxiety, pallor and diaphoresis. Altered mental status reflects poor brain perfusion.")

q("sbolbo", "A 68-year-old is admitted with a large bowel obstruction from volvulus. Which vomiting pattern does the nurse expect?",
  ["Early, frequent vomiting that may contain bile || This pattern fits small bowel obstruction",
   "No vomiting at any point || Vomiting does occur in LBO, late in the course",
   "*Late vomiting that may contain feces",
   "Vomiting only right after drinking fluids || Not the LBO pattern"],
  "LBO: prominent distention, continuous aching lower pain, late vomiting that may contain feces, and absolute obstipation. SBO causes early, frequent, possibly bilious vomiting.")

q("sbolbo", "Client A has central, colicky pain that comes and goes. Client B has continuous, aching lower abdominal pain. How should the nurse interpret these patterns?",
  ["*Client A fits SBO; client B fits LBO",
   "Client A fits LBO; client B fits SBO || Reversed: central colicky pain is SBO",
   "Both patterns fit SBO || Continuous aching lower pain is LBO",
   "Both patterns fit postoperative ileus || These are the SBO and LBO pain patterns"],
  "SBO pain is central, colicky and intermittent. LBO pain is continuous, aching and in the lower abdomen.")

q("assess", "During auscultation of a client with a suspected obstruction, the nurse hears no bowel sounds in one quadrant after 15 seconds. What should the nurse do next?",
  ["Record bowel sounds as absent in that quadrant || Listen at least a minute per quadrant if needed",
   "Palpate the quadrant to stimulate sounds || Auscultate before palpating",
   "*Keep listening for at least a minute there",
   "Move straight to palpating all four quadrants || Percussion comes before palpation"],
  "Abdominal assessment order: inspect, auscultate, percuss, palpate. Auscultate before palpating, listening at least a minute per quadrant if needed.")

q("nursing", "A client with a small bowel obstruction has had an NG tube to suction for 2 days. Which lab results need especially close monitoring?",
  ["Lipase levels || Lipase is not listed for obstruction monitoring",
   "*Electrolytes",
   "Troponin levels || Troponin is not part of obstruction monitoring",
   "TSH levels || TSH is not part of obstruction monitoring"],
  "NG output adds to fluid and electrolyte loss, so strict I&O including NG output and close electrolyte monitoring are needed.")

q("nursing", "A client with a bowel obstruction asks why the tube in the nose was placed. Which response is accurate?",
  ["'It gives you nutrition while you can't eat.' || The NG tube is for decompression",
   "'It delivers your IV fluids directly into the bowel.' || IV fluids go into a vein",
   "'It lets us measure your appetite each day.' || It is for decompression, and NG output is measured for I&O",
   "*'It decompresses your bowel while you stay NPO.'"],
  "Obstruction care: NPO with oral care, NG decompression (Salem sump), IV fluids for replacement and maintenance, and strict I&O including NG output.")

q("interv", "Which client's bowel obstruction is usually treated with surgery?",
  ["A client with postoperative ileus || Treated with ambulation and prokinetics",
   "A client with opioid-related ileus || Treated with a mu-opioid antagonist",
   "*A client with a stricture narrowing the colon",
   "A client with fecal impaction || Treated with fluids, fiber, softeners, laxatives, enemas, disimpaction"],
  "Hernia, volvulus, tumor or stricture: usually surgery. Postoperative ileus: ambulation and prokinetics. Opioid ileus: mu-opioid antagonist.")

q("meds", "A client taking psyllium says they drink very little water during the day. What is the nurse's main concern?",
  ["Tardive dyskinesia may develop || This is a metoclopramide concern",
   "The client may become dependent on it || Dependence is linked to bisacodyl",
   "*A thick mass may form and obstruct the bowel",
   "The client faces a higher MI risk || MI risk is linked to alvimopan"],
  "Psyllium is a bulk-forming laxative that enlarges the fecal mass; without enough fluid it can form a thick mass that obstructs.")

q("meds", "Which bowel medication and description pairings are correct? " + SATA,
  ["*Bisacodyl: a stimulant laxative",
   "*Docusate: softens the stool",
   "Metoclopramide: blocks gut opioid receptors || Metoclopramide is a prokinetic that increases motility",
   "*Psyllium: a bulk-forming laxative",
   "Alvimopan: a stool softener || Alvimopan binds GI opioid receptors to prevent postoperative ileus"],
  "Bisacodyl is a stimulant laxative; docusate softens stool; psyllium is bulk-forming; metoclopramide is a prokinetic; alvimopan binds GI opioid receptors.")

q("crc", "Which colorectal cancer symptom results from occult bleeding?",
  ["Unintended weight gain || Weight loss, not gain, is a CRC symptom",
   "Narrower stools || This is a change in stool caliber, not from bleeding",
   "Bloating with poor appetite || These are listed symptoms but not from bleeding",
   "*Anemia and fatigue"],
  "CRC symptoms: change in bowel habits or stool caliber, rectal bleeding, anemia and fatigue from occult bleeding, weight loss, incomplete emptying, bloating and anorexia.")

q("fap", "A genetic counselor and nurse review familial adenomatous polyposis (FAP) with a family. Which statements are accurate? " + SATA,
  ["*Hundreds to thousands of polyps develop",
   "*Polyps can begin in the teen years",
   "It is caused by a high-fat diet || FAP is inherited",
   "*Lifetime cancer risk is near 100%",
   "It is the same condition as Lynch syndrome || Lynch is a separate DNA repair defect"],
  "FAP: hundreds to thousands of polyps, starting as early as the teen years, near 100% lifetime cancer risk; prophylactic colectomy may be discussed.")

q("scope", "A client had a colonoscopy with biopsies this morning. Which findings should be reported promptly? " + SATA,
  ["*Signs of bleeding",
   "Mild cramping and gas || Expected after colonoscopy",
   "*Severe pain with a hard, rigid abdomen",
   "Drowsiness from the sedation || Expected after sedation",
   "Passing small amounts of gas || Expected after colonoscopy"],
  "After colonoscopy, monitor for bleeding and perforation. Severe pain with a rigid abdomen is the most concerning finding.")

q("surg", "A client scheduled for a polypectomy asks what the procedure involves. Which explanation is accurate?",
  ["'The entire colon will be removed.' || That is a colectomy",
   "'The rectum and anus are removed, with a permanent colostomy.' || That is an APR",
   "*'A polyp is removed during an endoscopy.'",
   "'A rectal stump is left and a temporary colostomy made.' || That is a Hartmann procedure"],
  "Polypectomy removes a polyp during endoscopy. Colectomy removes part or all of the colon; APR leaves a permanent colostomy; Hartmann leaves a rectal stump with a temporary colostomy.")

q("surg", "The nurse reviews teaching with a client after a Hartmann procedure. Which statement needs correction?",
  ["'My colostomy is meant to be temporary.' || Correct: Hartmann creates a temporary colostomy",
   "'A rectal stump was left in place.' || Correct: Hartmann leaves a rectal stump",
   "'Reconnection may be possible later on.' || Correct: reconnection may be possible later",
   "*'My rectum was removed, so I have a perineal wound.'"],
  "Hartmann leaves a rectal stump and creates a temporary colostomy; reconnection may be possible later. A permanent colostomy and perineal wound follow APR.")

q("periop", "On day 3 after colon surgery, a client asks for a high-fiber bran cereal. Which response is accurate?",
  ["'Yes, high fiber right away speeds healing.' || Diet starts NPO and advances toward low-residue",
   "*'Your diet will advance as prescribed toward low-residue.'",
   "'You can return to your regular diet today.' || Diet is advanced as prescribed",
   "'You'll stay on liquids permanently after this surgery.' || Diet advances toward low-residue"],
  "After colon surgery: NPO at first, then advanced as prescribed toward a low-residue diet. Monitor I&O, abdomen, bowel sounds, NG, drains, wounds and ostomy output.")

q("ostomy", "A 35-year-old has a new ileostomy. Which output should the nurse expect?",
  ["*Liquid stool",
   "Formed, solid stool || Solid stool comes from a sigmoid colostomy",
   "Semisolid stool || Semisolid stool comes from a descending colostomy",
   "No stool until the stoma heals || Output is expected"],
  "The closer the stoma is to the rectum, the more water is absorbed: ileostomy liquid, descending colostomy semisolid, sigmoid colostomy more solid.")

q("ostomy", "A home health nurse finds a client's pouch leaking and the skin around the stoma red and excoriated. What should the nurse do?",
  ["Document it as expected for a new stoma || Excoriated skin and leakage should be reported",
   "Scrub the skin with a harsh soap to clean it || Clean with warm water, not harsh soap",
   "Cut the wafer opening an inch larger || Cut the barrier to within 1/8 inch of the stoma",
   "*Report the excoriated skin and the leakage"],
  "Report dark or black color, retraction, excessive protrusion, excoriated skin and leakage. Moisture from leaks damages skin.")

q("ostteach", "A 40-year-old with a new colostomy quietly says she worries about intimacy with her partner. What should the nurse do?",
  ["Change the subject to pouch emptying || Body image and sexuality are part of ostomy assessment",
   "*Assess her body image and sexuality concerns",
   "Tell her to wait until the stoma heals to discuss it || Concerns should be assessed now",
   "Advise her to avoid discussing the ostomy || Psychosocial support is part of ostomy care"],
  "Ostomy self-care assessment includes vision, hand dexterity, ability to manage supplies, and body image and sexuality concerns.")

q("ostteach", "A client with a new colostomy reviews home care. Which statements show correct understanding? " + SATA,
  ["*'I can choose a one-piece or a two-piece system.'",
   "*'I'll probably empty the pouch about every 4 to 6 hours.'",
   "'I'll change the whole appliance every few hours.' || Change the appliance about twice a week",
   "*'I'll clean the skin around the stoma with warm water.'",
   "'I'll learn to irrigate even if it's an ileostomy.' || Irrigation applies only to descending or sigmoid colostomies"],
  "Empty before 1/3 full (often every 4 to 6 hours), change the appliance about twice a week, clean with warm water and check skin. One-piece and two-piece systems are available.")

q("screen", "The nurse reviews colorectal cancer prevention with a 49-year-old. Which statement needs correction?",
  ["'I'll keep my weight in a healthy range.' || Correct: maintain a healthy weight",
   "*'Processed deli meats every day are fine for my colon.'",
   "'I'll exercise on most days of the week.' || Correct: exercise regularly",
   "'I'll limit how much alcohol I drink.' || Correct: limit alcohol"],
  "CRC prevention: limit high-fat and processed meats, exercise regularly, avoid smoking, limit alcohol and maintain a healthy weight.")
