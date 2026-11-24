T = "e5ibd"; SET = "20261124"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("overview", "A nurse is teaching a 29-year-old client newly diagnosed with IBS. Which client statement shows understanding?",
 ["'IBS will raise my colon cancer risk the way Crohn's does.' || IBD raises colon cancer risk; IBS does not.",
  "'My immune system is attacking the lining of my colon.' || That describes IBD, an autoimmune disease.",
  "*'My bowel can look normal on exams even though I have symptoms.'",
  "'IBS causes permanent damage to the wall of my bowel.' || IBS causes no structural changes; IBD does."],
 "IBS is a functional disorder with no abnormalities when the colon is examined; IBD causes permanent structural changes.")

q("immune", "A 34-year-old client asks what might have set off her Crohn's disease. Which factor does the nurse identify as a possible environmental trigger?",
 ["Regular daily exercise || Exercise is not listed as a trigger.",
  "An immune response that is too weak || Too little response means immunosuppression, not autoimmunity.",
  "Eating foods that contain fiber || IBD is not caused by diet.",
  "*A recent infection or a period of high stress"],
 "Environmental triggers include smoking, stress, infection or chemical exposure; infections can overstimulate the immune system.")

q("compare", "A nurse reviews two endoscopy reports. Which finding belongs to the client with ulcerative colitis?",
 ["Patchy areas with a cobblestone appearance || Patchy, cobblestone lesions are Crohn's.",
  "*Continuous mucosal inflammation starting at the rectum",
  "Inflammation through every layer of the bowel wall || Transmural inflammation is Crohn's.",
  "Lesions in the mouth and the small intestine || Crohn's can occur anywhere 'gum to bum'; UC is rectum and colon only."],
 "UC is continuous, mucosal, rectum to colon only, with an ulcerative appearance.")

q("compare", "A nursing student is studying UC and Crohn's. Which statements are accurate? " + SATA,
 ["*Both conditions increase the risk of colon cancer",
  "UC produces patchy skip lesions || UC is continuous; skip lesions are Crohn's.",
  "*Both can cause anemia and weight loss",
  "Crohn's affects only the mucosal layer || Crohn's is transmural; UC is mucosal.",
  "*Crohn's can affect any part of the GI tract"],
 "Same immune cause, different pattern and depth; both share nutritional deficits, anemia, weight loss and colon cancer risk.")

q("ucassess", "A 41-year-old client is being evaluated for ulcerative colitis. Which additional finding would the nurse expect?",
 ["Fistula draining near the rectum || Fistulas are a Crohn's complication.",
  "Right lower pain with greasy stools || This pattern fits Crohn's.",
  "Normal findings on colonoscopy || A normal exam fits IBS.",
  "*Anemia along with weight loss"],
 "UC findings include frequent bloody, mucus stools, cramps, urgency, left lower pain, anemia and weight loss.")

q("ucassess", "The nurse is performing an abdominal assessment on a client with a UC flare. Where is the client's pain most likely located?",
 ["*Left lower abdomen",
  "Right lower abdomen || Right lower pain is more typical of Crohn's.",
  "Right upper abdomen || Not described for UC.",
  "Only around the umbilicus || Not described for UC."],
 "UC pain is often in the left lower abdomen, with cramps and urgency.")

q("megacolon", "A 38-year-old client is hospitalized with severe ulcerative colitis. Which findings suggest a UC complication is developing? " + SATA,
 ["*Sudden marked abdominal distention with fever",
  "A new fistula opening near the anus || Fistulas are a Crohn's complication.",
  "*Gross bleeding from the rectum",
  "*Signs of shock such as tachycardia",
  "Mild cramping that eases after a stool || Not a complication; monitor."],
 "UC complications are hemorrhage, perforation, toxic megacolon and colorectal cancer.")

q("megacolon", "A client in a severe UC flare has a PRN antidiarrheal ordered and now has new abdominal distention. Which action is best?",
 ["Give the antidiarrheal to slow the stools || Antidiarrheals need caution and can contribute to toxic megacolon.",
  "Offer a high-fiber snack to firm stools || A flare calls for low-fiber food or bowel rest.",
  "*Hold the antidiarrheal and report the distention",
  "Document it as an expected flare finding || Distention must be reported right away."],
 "Antidiarrheals can be dangerous in severe UC or suspected toxic megacolon; report severe pain or distention.")

q("cdassess", "A client with long-standing Crohn's disease has fever and a tender, swollen area beside the anus. Which complication does the nurse suspect?",
 ["Toxic megacolon || This is a UC complication marked by distention.",
  "*Abscess",
  "An IBS flare || IBS causes no structural complications.",
  "Expected remission || Fever and swelling are not remission."],
 "Crohn's complications are strictures, obstruction, fistulas and abscesses.")

q("cdassess", "Which finding in a client with Crohn's disease best reflects its transmural inflammation?",
 ["Inflammation limited to the mucosa || Mucosal-only inflammation is UC.",
  "Continuous lesions from the rectum || Continuous disease from the rectum is UC.",
  "*A stricture narrowing the bowel",
  "A normal bowel on colonoscopy || A normal exam fits IBS."],
 "Transmural inflammation affects every layer of the bowel wall, leading to strictures and fistulas.")

q("dx", "Which test confirms the mucosal changes of inflammatory bowel disease?",
 ["Stool culture || It rules out an intestinal infection.",
  "Serum albumin || It reflects malnutrition.",
  "Serum electrolytes || They reflect fluid and electrolyte losses.",
  "*Endoscopy with biopsy"],
 "Endoscopy with biopsy confirms the diagnosis; CT or MRI shows the bowel and bowel wall.")

q("fe", "A 45-year-old client in a Crohn's flare reports dizziness when standing, and the pulse is 112. Which problem is the nurse's priority concern?",
 ["Metabolic alkalosis || Diarrhea causes metabolic acidosis.",
  "Hyperkalemia || Diarrhea causes hypokalemia.",
  "*Dehydration from diarrhea losses",
  "Fluid overload || These findings point to volume loss."],
 "Tachycardia and orthostatic changes suggest dehydration; frequent diarrhea can cause hypovolemia.")

q("nursing", "A nurse receives report on four clients. Which client should the nurse see first?",
 ["Client with Crohn's asking about the Crohn's & Colitis Foundation || Important but not urgent.",
  "*Client with UC who has a fever and a rigid, distended abdomen",
  "Client in remission requesting a diet handout || Stable; can wait.",
  "Client with UC whose mild cramping eased after a stool || Expected; monitor."],
 "Fever, severe pain or distention, gross bleeding and signs of shock must be reported immediately; they can signal perforation.")

q("nursing", "Which actions belong in the care plan for a 52-year-old client admitted with a severe Crohn's flare? " + SATA,
 ["Encourage large, high-fiber meals || A severe flare calls for bowel rest and low fiber.",
  "*Monitor weight and intake and output",
  "Give antidiarrheals freely for comfort || Antidiarrheals need caution in severe IBD.",
  "*Protect the perianal skin",
  "*Give corticosteroids as prescribed"],
 "Severe flare care: NPO bowel rest with IV fluids, corticosteroids, nutrition support, perianal skin protection, and monitoring of vital signs, weight, I&O and stools.")

q("steroid", "A client admitted with an acute UC flare is NPO. Which medication order would the nurse expect for the flare?",
 ["Oral prednisone || The client is NPO; prednisone is given by mouth.",
  "Oral sulfasalazine || A 5-ASA for maintenance, given by mouth.",
  "*IV methylprednisolone",
  "Oral azathioprine || An immunomodulator for maintenance that takes weeks to months."],
 "Corticosteroids give short-term control of acute flares; methylprednisolone can be given by mouth, rectally or IV.")

q("asa", "A client taking sulfasalazine for UC is planning a beach vacation. Which teaching is the priority?",
 ["Stop the drug while traveling || It is a maintenance drug; stopping can bring a flare.",
  "Skip folic acid while away || Folic acid supplementation is needed.",
  "Get TB screening before leaving || TB screening is for biologics.",
  "*Limit sun exposure and protect your skin"],
 "Sulfasalazine teaching: take folic acid supplementation and avoid sun exposure.")

q("asa", "Which client is receiving a 5-ASA drug?",
 ["*A client using rectal mesalamine for UC maintenance",
  "A client receiving vedolizumab infusions || Vedolizumab is a biologic.",
  "A client taking azathioprine by mouth daily || Azathioprine is an immunomodulator.",
  "A client on IV methylprednisolone for a flare || Methylprednisolone is a corticosteroid."],
 "Sulfasalazine and mesalamine are the 5-ASA maintenance drugs; mesalamine comes in oral and rectal forms.")

q("immuno", "A client with Crohn's disease is starting azathioprine. Which client statement shows understanding?",
 ["'It should work within a few days.' || Immunomodulators take weeks to months.",
  "*'It may take weeks to months before I notice a benefit.'",
  "'I will inject it under my skin.' || It is taken by mouth daily.",
  "'I won't need any blood tests.' || Monitor CBC and liver function."],
 "Immunomodulators broadly suppress immunity, are inexpensive oral daily drugs and take weeks to months to work.")

q("bio", "A 30-year-old client is scheduled for a first vedolizumab infusion. Which nursing actions are appropriate? " + SATA,
 ["*Confirm TB screening was completed",
  "*Assess the client for signs of infection",
  "Give folic acid with the dose || Folic acid is sulfasalazine teaching.",
  "*Monitor the client during the infusion",
  "Have the client take it by mouth || Biologics are IV or SQ."],
 "Biologics suppress immunity: screen for infection and TB first, and monitor during injections and infusions.")

q("bio", "Which statement correctly compares biologics with immunomodulators?",
 ["Biologics are inexpensive pills taken daily || Biologics are very expensive and given IV or SQ.",
  "Biologics are used only for acute flares || Biologics are maintenance drugs.",
  "Biologics broadly suppress the immune system || Broad suppression describes immunomodulators.",
  "*Biologics target specific immune proteins and act sooner"],
 "Biologics target specific immune proteins and work in a few weeks; immunomodulators take weeks to months.")

q("nutri", "A client whose Crohn's is now in remission says, 'I'll stay on soft, bland, low-fiber foods forever.' Which response is best?",
 ["'Yes, low fiber is best at all times.' || The remission diet adds fiber-rich whole foods.",
  "'Switch to clear liquids only.' || Clear liquids are not a remission diet.",
  "*'In remission, add fiber-rich whole foods and lean protein.'",
  "'Processed foods are fine to eat now.' || Avoid processed foods in remission."],
 "Remission: fiber-rich whole foods, lean protein, calcium-rich foods, avoid processed foods. Flare: soft, bland, low fiber.")

q("nutri", "Which teaching points fit a client with IBD during a flare? " + SATA,
 ["*Choose fully cooked, skinless vegetables",
  "Add raw vegetables and whole grains || These are high fiber; a flare needs low fiber.",
  "*Eat small, frequent meals",
  "Stop the food journal until the flare ends || Keep a food journal to find trigger foods.",
  "*Drink 8–10 glasses of fluid a day"],
 "Flare: soft, bland, low fiber; in both phases, hydrate, eat small frequent meals and keep a food journal.")

q("tpn", "The nurse finds a client's TPN infusing by gravity. Which action is correct?",
 ["Leave it on gravity and recheck in an hour || TPN must run on an infusion pump.",
  "*Place the TPN on an infusion pump",
  "Piggyback the client's IV meds into the line || No other medications go through the TPN line.",
  "Change the central line dressing now || The dressing is changed every 7 days."],
 "TPN runs on an infusion pump; check the label, keep ports sterile and monitor glucose, labs, weight and I&O.")

q("tpn", "A client's TPN tubing was hung 24 hours ago, the central dressing was changed 3 days ago, and a glucose check is due. Which actions does the nurse take now? " + SATA,
 ["*Check a fingerstick glucose",
  "Change the central line dressing || It is changed every 7 days; only 3 days have passed.",
  "*Change the tubing with a micron filter",
  "Piggyback an IV antibiotic into the TPN line || No other medications through the TPN line.",
  "Stop the TPN for the rest of the day || Not indicated."],
 "TPN schedule: fingerstick glucose every 6 hours, tubing every 24 hours with a micron filter, central dressing every 7 days.")

q("surg", "A 36-year-old client with UC needs surgery and wants to avoid a permanent stoma. Which procedure would the nurse expect to be discussed?",
 ["Proctocolectomy with permanent ileostomy || This leaves a permanent stoma.",
  "Bowel resection of diseased areas || Bowel resection is the Crohn's surgery.",
  "*J-pouch (ileal pouch–anal anastomosis)",
  "Placement of a stent in the colon || Not a listed IBD surgery."],
 "A J-pouch is an internal reservoir made from the end of the small intestine after the colon and rectum are removed.")

q("surg", "Which statement about surgery for IBD is accurate?",
 ["*Colon removal can be definitive for UC; Crohn's can return",
  "Bowel resection cures Crohn's disease || It treats complications; Crohn's can come back.",
  "A J-pouch is the usual surgery for Crohn's || The J-pouch is a UC surgery.",
  "Surgery is never used to treat UC || Proctocolectomy and J-pouch are UC surgeries."],
 "Crohn's: bowel resection for complications. UC: J-pouch or proctocolectomy with permanent ileostomy.")

q("health", "Two weeks after ileostomy surgery, a client with UC says, 'I can't stand looking at my stoma.' Which nursing action is best?",
 ["Tell the client the feeling is all in their head || Dismissive; chronic symptoms affect daily life.",
  "Change the subject to diet teaching || Avoids the client's concern.",
  "Promise that everyone adjusts within days || False reassurance.",
  "*Address body image and refer to the Crohn's & Colitis Foundation"],
 "Psychosocial support: address body image and ostomy adjustment, support stress management and refer to the Crohn's & Colitis Foundation.")
