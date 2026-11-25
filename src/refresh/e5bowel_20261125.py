T = "e5bowel"; SET = "20261125"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("anat", "A client asks which parts of the bowel absorb most of the nutrients from food. Which answer by the nurse is correct?",
  ["The cecum, colon and rectum || These make up the large intestine, which absorbs water",
   "*The duodenum, jejunum and ileum",
   "The sigmoid colon and the rectum || These are large intestine; their job is water and elimination",
   "The cecum and the ileocecal valve || The valve only separates the small and large intestines"],
  "The small intestine (duodenum, jejunum, ileum) absorbs nutrients; the large intestine absorbs water and carries out elimination.")

q("types", "Bowel elimination depends on patency and peristalsis. Which client has an obstruction caused by a PATENCY problem?",
  ["A client with low potassium and a distended abdomen || Low potassium causes ileus, a peristalsis problem",
   "A client taking opioids around the clock for pain || Opioids cause ileus, a peristalsis problem",
   "A client with peritonitis and absent bowel sounds || Peritonitis causes ileus, a peristalsis problem",
   "*A client whose bowel has twisted on itself (volvulus)"],
  "Mechanical obstruction (adhesions, tumors, impaction, volvulus, intussusception, strictures, hernias) is a patency problem; ileus is a peristalsis problem.")

q("types", "A client develops abdominal distention with no blockage on imaging. Which items in the history are listed causes of this nonmechanical obstruction? " + SATA,
  ["*Abdominal surgery 2 days ago",
   "An incarcerated inguinal hernia || A hernia is a mechanical cause",
   "*A magnesium level below normal",
   "*Long-standing Parkinson's disease",
   "A known tumor narrowing the colon || A tumor is a mechanical cause"],
  "Ileus causes: abdominal surgery, opioids, low potassium or magnesium, peritonitis, diabetes or Parkinson's, and vascular insufficiency.")

q("mech", "A client who has had several abdominal surgeries is admitted with a bowel obstruction. Which mechanical cause does the nurse recognize as very common in this situation?",
  ["Intussusception || Telescoping bowel is often discussed in pediatrics",
   "Volvulus || A twisted bowel isn't tied to prior surgery in the lecture",
   "*Adhesions",
   "Fecal impaction || Impaction is a stool blockage, not surgical scar tissue"],
  "Adhesions are scar tissue, often after abdominal surgery, that can constrict the bowel; they are a very common cause of obstruction.")

q("hernia", "Which statement correctly compares an incarcerated hernia with a strangulated hernia?",
  ["An incarcerated hernia goes back in when the client lies down || That describes a reducible hernia",
   "*Incarcerated has intact blood flow; strangulated has compromised blood supply",
   "A strangulated hernia is less urgent than an incarcerated one || Strangulation is an emergency",
   "Both stages have a compromised blood supply to the bowel || Incarcerated blood flow is intact"],
  "Incarcerated (irreducible): contents can't be pushed back but blood flow is intact. Strangulated: blood supply compromised, leading to ischemia/necrosis; an emergency.")

q("hernia", "A client with an incarcerated umbilical hernia is being sent home to await surgery. Which findings should the nurse teach the client to report right away? " + SATA,
  ["*A new fever",
   "*Severe pain at the hernia site",
   "*A racing heart rate",
   "*Nausea and vomiting",
   "A bulge that is unchanged from yesterday || A stable bulge isn't a sign of strangulation"],
  "An incarcerated hernia can progress to strangulation. Fever, severe pain, tachycardia and nausea/vomiting suggest compromised blood supply, an emergency.")

q("partial", "A client with a bowel obstruction is still passing small amounts of loose stool and gas. The client asks why surgery isn't being done right away. Which response is best?",
  ["'Passing stool means the obstruction is gone.' || Some stool can still pass in a partial obstruction",
   "'Surgery is never used for bowel obstruction.' || Some causes are treated with surgery",
   "*'This looks partial, so conservative care may be tried first.'",
   "'Loose stool means you need a laxative instead.' || Laxatives are not the plan for partial obstruction"],
  "Partial obstruction: some stool (sometimes diarrhea) or gas passes, progression is slower, and conservative care may be tried.")

q("partial", "The nurse is caring for four clients with bowel obstruction. Which client needs the MOST urgent attention?",
  ["*No stool or flatus for a day, with rapidly worsening symptoms",
   "Passing small amounts of gas, with symptoms changing slowly || Partial obstruction progresses more slowly",
   "Small amounts of loose stool, with stable vital signs || Partial obstruction; conservative care may be tried",
   "Mild cramping, still passing some stool each day || Passing stool suggests partial obstruction"],
  "Complete obstruction: no stool or flatus passes (obstipation), symptoms progress fast, and it is a medical emergency.")

q("patho", "Fluid and gas keep building up above a bowel blockage. Besides fluid loss, which complication can continued stretching of the bowel cause?",
  ["Intussusception || Telescoping is a cause of obstruction, not a result of stretching",
   "Fecal impaction || Impaction is a cause of obstruction, not a result",
   "A new hernia || Hernias come from a weak wall plus abdominal pressure",
   "*Perforation"],
  "Blockage, increased peristalsis, fluid and gas buildup, higher lumen pressure, fluid leaks from vessels, hypovolemia/shock. Continued stretching can also cause perforation.")

q("shock", "Which set of findings in a client with a small bowel obstruction is MOST consistent with hypovolemic shock?",
  ["BP 162/94, HR 58, warm and flushed skin || Hypertension and bradycardia don't fit shock",
   "BP 124/78, HR 76, RR 16, alert || These are normal findings",
   "*BP 86/54, HR 128, RR 28, pale and sweaty",
   "BP 150/96, HR 102, warm dry skin || Hypertension doesn't fit hypovolemic shock"],
  "Hypovolemic shock: hypotension, tachycardia, tachypnea, decreased urine output, anxiety, pallor and diaphoresis.")

q("shock", "A client with a large bowel obstruction has received prescribed IV fluid boluses, but the BP is still 80/48. What does the nurse anticipate next?",
  ["Switching to oral fluids to boost volume || The client is NPO with an obstruction",
   "Giving a laxative to clear the obstruction || Doesn't address the shock",
   "Ambulating the client to improve circulation || Not a shock treatment; fluids and vasopressors are",
   "*Possible ICU transfer and vasopressors"],
  "Support circulation with prescribed IV fluid resuscitation and notify the provider; possible ICU transfer and vasopressors if fluids alone aren't enough.")

q("sbolbo", "A client with a large bowel obstruction from volvulus asks why surgery is planned when a roommate with a small bowel obstruction is not having surgery. Best response?",
  ["'Small bowel obstructions always need surgery later.' || SBO is mostly treated conservatively",
   "*'Large bowel blockages often need surgery; small bowel ones are mostly treated without it.'",
   "'Volvulus usually untwists on its own after a few days.' || Volvulus is usually treated surgically",
   "'Surgery is only done when a client is passing gas.' || Passing gas isn't the surgical criterion"],
  "SBO (75-80%, often adhesions or hernia) is mostly conservative. LBO (20-25%, often colorectal cancer or volvulus) often needs surgery.")

q("sbolbo", "A client reports central, crampy pain that comes and goes, and has vomited several times early on; the vomit contains bile. The abdomen is only mildly distended. Which problem do these findings suggest?",
  ["Large bowel obstruction || LBO has continuous aching lower pain and late vomiting",
   "Strangulated hernia || Strangulation shows fever, severe pain and tachycardia",
   "*Small bowel obstruction",
   "Hypovolemic shock || Shock is a complication, not the obstruction site"],
  "SBO: early, frequent vomiting that may contain bile, central colicky intermittent pain, mild distention, and gas/stool may still pass early.")

q("assess", "During an abdominal assessment of a client with suspected obstruction, which step should the nurse perform LAST?",
  ["Inspection || Inspection comes first",
   "Auscultation || Auscultation comes before percussion and palpation",
   "Percussion || Percussion comes before palpation",
   "*Palpation"],
  "Abdominal assessment order: inspect, auscultate, percuss, palpate. Palpation checks tenderness and rigidity.")

q("nursing", "The nurse reviews admission orders for a client with a small bowel obstruction. Which order should the nurse question?",
  ["NG tube to suction for decompression || Expected care",
   "IV fluids for replacement and maintenance || Expected care",
   "*Regular diet as tolerated",
   "Strict intake and output including NG output || Expected care"],
  "Care includes NPO with oral care, NG decompression (Salem sump), IV fluids for replacement and maintenance, and strict I&O including NG output.")

q("nursing", "A client with a bowel obstruction is being monitored for perforation. Which changes should the nurse report promptly? " + SATA,
  ["*A sudden increase in pain",
   "NG tube draining with suction on || An expected finding",
   "*A sudden decrease in pain",
   "*A rigid abdomen with guarding",
   "*A rising heart rate"],
  "Any sudden increase or decrease in pain can mean perforation; abdominal rigidity can signal perforation or peritonitis and must be reported.")

q("interv", "A client develops postoperative ileus 2 days after abdominal surgery. Which intervention does the nurse anticipate?",
  ["*Helping the client ambulate",
   "Emergency surgical repair || Surgery is for hernia, volvulus, tumor or stricture",
   "Enema reduction || Used for intussusception",
   "Manual disimpaction || Used for fecal impaction"],
  "Postoperative ileus is treated with ambulation and prokinetic agents; opioid-related ileus with a mu-opioid antagonist.")

q("meds", "Which pairing of bowel medication and nursing concern is correct?",
  ["Psyllium — limit fluids while taking it || Maintain fluids to avoid a thick mass that can obstruct",
   "Bisacodyl — watch for tardive dyskinesia || Tardive dyskinesia is a concern with metoclopramide",
   "*Alvimopan — short-term use only because of MI risk",
   "Metoclopramide — long-term use causes dependence || Dependence is a concern with bisacodyl"],
  "Alvimopan: short-term only, up to 15 doses, MI risk. Metoclopramide: tardive dyskinesia. Bisacodyl: dependence. Psyllium: maintain fluids.")

q("meds", "The nurse reviews bowel medication teaching. Which client statements show correct understanding? " + SATA,
  ["*'I'll keep drinking fluids with psyllium so it doesn't form a thick mass.'",
   "'I'll stop docusate if my stools become firmer.' || Stop docusate if diarrhea occurs",
   "*'Docusate may take 1 to 3 days to work.'",
   "'Alvimopan is fine to take daily for months.' || Short-term only, up to 15 doses",
   "*'I shouldn't rely on bisacodyl long term.'"],
  "Psyllium: maintain fluids. Docusate: maintain fluids, stop if diarrhea, 1-3 days to work. Bisacodyl: long-term use can cause dependence. Alvimopan: short-term only.")

q("crc", "A 63-year-old client describes recent bowel changes. Which reports should the nurse recognize as possible signs of colorectal cancer? " + SATA,
  ["*Stools that have become narrower",
   "*A feeling of not fully emptying",
   "*Bloating with a poor appetite",
   "Unplanned weight gain || Unintended weight loss is the listed sign",
   "*Fatigue linked to anemia"],
  "CRC symptoms: change in bowel habits or stool caliber, rectal bleeding, anemia and fatigue from occult bleeding, unintended weight loss, incomplete emptying, bloating and anorexia.")

q("fap", "Which statement correctly compares FAP with Lynch syndrome?",
  ["Both are caused by a high-fat diet and can be reversed || Both are inherited",
   "Lynch causes thousands of polyps; FAP is a DNA repair defect || This reverses the two",
   "FAP has a low cancer risk; Lynch has a near 100% risk || FAP carries a near 100% lifetime risk",
   "*FAP causes hundreds to thousands of polyps; Lynch is a DNA repair defect"],
  "FAP: hundreds to thousands of polyps, from the teen years, near 100% lifetime cancer risk. Lynch syndrome: inherited risk from impaired DNA repair, 2-4% of CRC.")

q("scope", "A client finishing bowel prep the evening before a colonoscopy reports the stools still contain solid material. What should the nurse conclude?",
  ["*The prep isn't adequate yet; no solid material should be passing",
   "The prep is complete once any liquid stool has passed || Solid material means prep is inadequate",
   "Solid stool is expected and won't affect the test || Adequate prep is very important",
   "The client should eat a meal to finish the prep || A liquid diet is followed before the test"],
  "The nurse checks that no solid material is passing to confirm adequate prep; adequate prep is very important.")

q("surg", "A client is recovering from a low anterior resection. Which client statement shows correct understanding?",
  ["'I'll have a permanent colostomy from now on.' || A permanent colostomy follows an APR",
   "*'Nothing should go into my rectum because the connection is low.'",
   "'A rectal suppository is fine if I get constipated.' || Nothing per rectum after this surgery",
   "'My rectum and anus were removed, so I have a perineal wound.' || That describes an APR"],
  "Low anterior resection removes the upper rectum and reconnects. The anastomosis is low, so nothing goes per rectum.")

q("surg", "After a partial colectomy, the client asks what 'anastomosis' means. Which explanation is accurate?",
  ["'A polyp was removed through the scope.' || That describes a polypectomy",
   "'A rectal stump was left for later reconnection.' || That describes a Hartmann procedure",
   "*'The remaining ends of the bowel were joined together.'",
   "'A permanent opening was made for stool.' || That describes a permanent colostomy"],
  "Colectomy removes part or all of the colon; the remaining bowel ends may be joined by anastomosis.")

q("periop", "A client scheduled for colorectal cancer surgery asks whether chemotherapy will come before or after the operation. Which response is accurate?",
  ["'Chemotherapy is only ever given after surgery.' || It may be given before or after",
   "*'Chemotherapy and radiation may be given before or after surgery.'",
   "'Surgery replaces the need for chemotherapy or radiation.' || They may still be part of treatment",
   "'Radiation is the only option given before surgery.' || Chemotherapy may also be given before"],
  "Chemotherapy and radiation may be given before or after CRC surgery; CEA is monitored to track treatment.")

q("ostomy", "Which list orders ostomy output from MOST liquid to MOST solid?",
  ["Sigmoid colostomy, descending colostomy, ileostomy || This is reversed",
   "Descending colostomy, ileostomy, sigmoid colostomy || Ileostomy output is the most liquid",
   "Ileostomy, sigmoid colostomy, descending colostomy || Sigmoid is firmer than descending",
   "*Ileostomy, descending colostomy, sigmoid colostomy"],
  "The closer to the rectum, the more water absorbed and the firmer the stool: ileostomy liquid, descending semisolid, sigmoid more solid.")

q("ostomy", "The nurse assesses a new stoma on postoperative day 3. Which findings are HEALTHY? " + SATA,
  ["*Pink color",
   "Black color || Dark or black color should be reported",
   "*Moist surface",
   "Retracted below the skin || Retraction should be reported",
   "*Shiny appearance",
   "*Raised above the skin"],
  "A healthy stoma is pink, moist, shiny and raised (PMS). Report dark or black color, retraction, excessive protrusion, excoriated skin and leakage.")

q("ostteach", "A client with a new colostomy asks how often to empty the pouch and change the appliance. Which response is correct?",
  ["'Empty it when completely full; change the appliance daily.' || Empty before 1/3 full; change about twice a week",
   "*'Empty it before it's 1/3 full; change the appliance about twice a week.'",
   "'Empty it once a day; change the appliance once a month.' || Emptying is often every 4-6 hours",
   "'Empty it at bedtime only; change the appliance every day.' || Empty before 1/3 full, often every 4-6 hours"],
  "Empty the pouch before it is 1/3 full, often every 4-6 hours; change the appliance about twice a week.")

q("ostteach", "A client with a new sigmoid colostomy asks whether irrigation is an option. Which response is accurate?",
  ["'Irrigation is only for clients with an ileostomy.' || Irrigation doesn't apply to ileostomies",
   "'Irrigation can be started on your own without any orders.' || It requires instruction and orders",
   "'Irrigation is not used for any type of colostomy.' || It applies to descending or sigmoid colostomies",
   "*'It applies to descending or sigmoid colostomies, with instruction and orders.'"],
  "Colostomy irrigation applies only to descending or sigmoid colostomies and requires instruction and orders.")

q("screen", "A 46-year-old client at average risk chooses CT colonography for colorectal cancer screening. How often should this test be repeated?",
  ["Every year || The yearly test is the stool blood test",
   "Every 3 years || The stool DNA/RNA test is every 3 years",
   "*Every 5 years",
   "Every 10 years || Colonoscopy is every 10 years"],
  "Average-risk screening starts at 45: annual stool blood test, stool DNA/RNA every 3 years, colonoscopy every 10 years, or CT colonography every 5 years.")
