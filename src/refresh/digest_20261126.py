T = "digest"; SET = "20261126"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("gbpatho", "A nursing student is explaining cholecystitis during clinical conference. Which statement by the student needs correction?",
 ["'Most cases happen when a gallstone blocks the cystic duct.' || Correct: calculous cholecystitis is about 90-95% of cases.",
  "'Acalculous cholecystitis can follow sepsis or trauma.' || Correct: bile stasis, ischemia, trauma or sepsis.",
  "*'The gallbladder makes bile and sends it to the duodenum.'",
  "'Trapped bile can make the gallbladder ischemic or infected.' || Correct: that is the disease process."],
 "The liver makes bile; the gallbladder stores it and squeezes it into the duodenum after a fatty meal. A stone blocking the cystic duct traps bile, causing swelling, inflammation, ischemia or infection.")

q("gbpatho", "A 47-year-old teacher with gallstones asks why her pain began right after a cheeseburger and fries. Which explanation is best?",
 ["'Fatty food stops the liver from making bile.' || The liver keeps making bile; the gallbladder stores it.",
  "'Fat is broken down by insulin from the gallbladder.' || The gallbladder does not make insulin.",
  "*'A fatty meal makes the gallbladder squeeze hard against the blocked duct.'",
  "'Fried food causes the pancreas to digest itself.' || That describes pancreatitis."],
 "The gallbladder squeezes hardest after a fatty meal, which is why cholecystitis pain often starts after fried or fatty food.")

q("gbrisk", "A nurse reviews gallstone risk factors with a 44-year-old client. Which risk factor is the client NOT able to change?",
 ["Obesity || Modifiable through weight management.",
  "Crash dieting with rapid weight loss || Modifiable.",
  "A high-fat, low-fiber diet || Modifiable.",
  "*Native American ethnicity"],
 "Modifiable risks include obesity, rapid weight loss, a high-fat low-fiber diet, oral contraceptives and pregnancy. Being female and Native American ethnicity cannot be changed.")

q("gbsx", "A 39-year-old bus driver is admitted with suspected acute cholecystitis. Which assessment findings support this diagnosis? " + SATA,
 ["*A fast heart rate",
  "Tenderness at McBurney's point || Points to appendicitis.",
  "*A distended abdomen",
  "*RUQ pain lasting more than 6 hours after a meal",
  "Bluish bruising around the umbilicus || Cullen's sign points to pancreatitis."],
 "Acute cholecystitis: RUQ pain over 6 hours, often after eating, spreading to the right shoulder, with fever, nausea, vomiting, a fast heart rate, a distended abdomen and possible jaundice.")

q("gbsx", "A nurse uses the CHOLY mnemonic to review cholecystitis findings. Which letter is matched correctly?",
 ["C: constant left-sided pain || C is colicky RUQ pain.",
  "*Y: yellow skin from jaundice",
  "H: hypothermia || H is high fever.",
  "O: overactive bowel sounds || O is obstructed bile."],
 "CHOLY: colicky RUQ pain, high fever, obstructed bile, leukocytosis, yellow.")

q("gbdx", "A client's abdominal ultrasound is reviewed for acute cholecystitis. Which findings support the diagnosis? " + SATA,
 ["*Gallstones",
  "The gallbladder does not fill with tracer || That is a HIDA scan finding, not ultrasound.",
  "*A thickened gallbladder wall",
  "*Fluid around the gallbladder",
  "An inflamed appendix in the right lower quadrant || Points to appendicitis."],
 "Ultrasound is the first test and shows stones, a thick gallbladder wall and fluid around it. HIDA non-visualization means the cystic duct is blocked.")

q("gbdx", "A 55-year-old client with cholecystitis has a rising bilirubin level. Which problem does the nurse suspect?",
 ["A normal finding in all cholecystitis || Bilirubin rises when the common bile duct is blocked.",
  "Acute kidney injury || Bilirubin is not a kidney test.",
  "*Blockage of the common bile duct",
  "Pernicious anemia || Not linked to bilirubin here."],
 "Expected cholecystitis labs: high WBC and CRP, slightly high AST, ALT and ALP, and high bilirubin if the common bile duct is blocked.")

q("ducts", "A client scheduled for an MRCP asks what the test will do. Which response by the nurse is accurate?",
 ["'A scope will be passed to remove the stones.' || That describes ERCP.",
  "'It shows whether your gallbladder fills with tracer.' || That describes a HIDA scan.",
  "'It removes the head of your pancreas.' || That is the Whipple procedure.",
  "*'It takes detailed pictures of your bile and pancreatic ducts without a scope.'"],
 "Image vs treat: MRCP images the ducts without a scope; ERCP can both see and remove stones, and can cause pancreatitis.")

q("gbtx", "A client is preparing for discharge after a laparoscopic cholecystectomy. Which client statement needs correction?",
 ["'I'll eat low-fat foods for the next 4 to 6 weeks.' || Correct teaching.",
  "*'I can go back to fried foods right away.'",
  "'I'll watch my small puncture sites for signs of infection.' || Correct: infection is a concern.",
  "'I'll report any bleeding from my incisions.' || Correct: bleeding is a concern."],
 "After cholecystectomy, follow a low-fat diet for 4-6 weeks while the body adjusts to bile flowing straight from the liver. Watch for pain, bleeding, infection and breathing problems.")

q("gbtx", "A hemodynamically stable 58-year-old has confirmed acute cholecystitis. Which surgical plan does the nurse expect?",
 ["*Laparoscopic cholecystectomy, usually within 48 hours",
  "Percutaneous cholecystostomy for every client || Reserved for clients too unstable for surgery.",
  "A Whipple procedure || That is for pancreatic cancer.",
  "Surgery only after 6 months of a low-fat diet || Surgery is usually within 48 hours."],
 "Stable clients get laparoscopic cholecystectomy, usually within 48 hours. Unstable clients may get a percutaneous cholecystostomy drain.")

q("gbcomp", "A nurse receives report on four clients with cholecystitis. Which client should the nurse see first?",
 ["A client whose mild nausea is improving || Improving symptoms are not urgent.",
  "A client asking about a low-fat diet || Teaching need, not urgent.",
  "*A client with new confusion and BP 88/52",
  "A client whose pain is controlled after medication || Stable."],
 "Escalate a rigid abdomen, rebound tenderness, jaundice, mental status changes, fever or low BP: they signal perforation, obstruction or sepsis.")

q("gbcomp", "A client admitted with cholecystitis has elevated lipase and amylase. What does the nurse suspect?",
 ["An expected cholecystitis finding || These enzymes are checked to rule out pancreatitis.",
  "*A gallstone has also blocked the pancreatic duct",
  "Acute kidney injury from dehydration || Lipase and amylase are not kidney tests.",
  "A clotting problem || These are not clotting labs."],
 "Lipase and amylase are checked in cholecystitis to rule out pancreatitis, because a gallstone can also block the pancreatic duct.")

q("panpatho", "A 50-year-old client newly diagnosed with acute pancreatitis explains the disease back to the nurse. Which statement shows understanding?",
 ["'My stomach acid ate a hole through my pancreas.' || That is not autodigestion.",
  "*'My pancreatic enzymes turned on too early and began digesting my pancreas.'",
  "'Bile got trapped in my gallbladder and swelled it.' || That describes cholecystitis.",
  "'My insulin is breaking down the pancreas.' || Trypsin, not insulin, digests the pancreas."],
 "Pancreatitis is autodigestion: digestive enzymes such as trypsin activate inside the pancreas and digest it.")

q("panpatho", "Which events are part of the process of acute pancreatitis? " + SATA,
 ["*Digestive enzymes activate early inside the pancreas",
  "*Trypsin digests the pancreatic tissue",
  "Pepsin erodes the pancreatic duct || Trypsin is the enzyme named.",
  "*Inflammation can progress to necrosis and infection",
  "*A body-wide inflammatory response can follow"],
 "A trigger such as a gallstone or alcohol activates enzymes early; enzymes and bile back up and the pancreas digests itself, leading to inflammation, possible necrosis and infection, and possibly a body-wide inflammatory response.")

q("panrisk", "A client with acute pancreatitis has no gallstones, does not drink and has normal triglycerides. The client asks what caused it. Which response is accurate?",
 ["'Pancreatitis always comes from gallstones.' || Many causes exist.",
  "'It must be from your low-fat diet.' || A low-fat diet is not a trigger.",
  "*'In 10 to 20 percent of cases, no cause is found.'",
  "'Only alcohol can cause pancreatitis.' || Gallstones, drugs, ERCP and more can too."],
 "Gallstones and alcohol are the most common causes, with others such as high triglycerides, certain drugs, ERCP, trauma and mumps; 10-20% of cases have no known cause.")

q("panrisk", "A nurse explains how gallstones and alcohol each lead to pancreatitis. Which explanation is correct?",
 ["*Gallstones block the duct; alcohol damages the pancreatic cells",
  "Gallstones damage the cells; alcohol blocks the duct || Reversed.",
  "Both cause pancreatitis by lowering insulin || Not the mechanism given.",
  "Both work by raising fiber intake || Fiber is not a cause."],
 "The two most common causes: gallstones block the duct and alcohol damages the cells.")

q("pansx", "A nurse compares two clients with pancreatitis. Which finding is more typical of ACUTE pancreatitis than chronic?",
 ["Fatty, foul-smelling stools with weight loss || Fits chronic pancreatitis.",
  "Newly diagnosed diabetes || Fits chronic pancreatitis.",
  "*Sudden severe upper abdominal pain boring to the back with vomiting",
  "Painless jaundice with dark urine || Points to pancreatic cancer."],
 "Acute pancreatitis: sudden severe upper-middle abdominal pain through to the back, nausea, vomiting, fever, fast heart rate. Chronic: fatty stools, weight loss, new diabetes, ongoing pain.")

q("pansx", "A 44-year-old warehouse worker is admitted with acute pancreatitis after heavy drinking. Which findings does the nurse expect? " + SATA,
 ["*Nausea and vomiting",
  "*Fever",
  "A positive Murphy's sign || Points to cholecystitis.",
  "*A fast heart rate",
  "*A possibly rigid abdomen"],
 "Acute pancreatitis causes severe pain boring to the back, nausea, vomiting, fever, a fast heart rate and possibly a rigid abdomen.")

q("panmon", "A client with acute pancreatitis has had a steady drop in urine output over the shift. Which complication does the nurse suspect?",
 ["Dumping syndrome || Not a pancreatitis complication.",
  "An expected response to NPO status || Falling urine output needs escalation.",
  "Low blood sugar || Glucose is typically high.",
  "*Acute kidney injury"],
 "Acute pancreatitis complications include shock, acute kidney injury, breathing trouble with pleural effusions and low calcium. Falling urine output needs urgent escalation.")

q("panmon", "A nurse is caring for four clients with acute pancreatitis. Which client needs attention FIRST?",
 ["*A client with new shortness of breath and an O2 sat of 88%",
  "A client whose pain is 5/10 and improving with IV opioids || Routine pain management.",
  "A client asking how to quit smoking || Teaching need, not urgent.",
  "A client who is NPO and asking when he can eat || Expected, not urgent."],
 "Low BP, low O2 sat, falling urine output and new breathing trouble need urgent escalation; pleural effusions and infiltrates can develop.")

q("pandx", "Which lab result is the MOST specific for acute pancreatitis?",
 ["Amylase || Elevated but less specific than lipase.",
  "*Lipase",
  "WBC || Elevated but not specific to the pancreas.",
  "Glucose || Elevated but not specific to the pancreas."],
 "High lipase and amylase confirm acute pancreatitis; lipase is the more specific test.")

q("pandx", "Which lab result does the nurse expect to be LOW in a client with acute pancreatitis?",
 ["Glucose || Glucose is high.",
  "Triglycerides || Triglycerides are high.",
  "*Calcium",
  "WBC || WBC is high."],
 "Lipase, amylase, WBC, glucose, triglycerides, AST, ALT and bilirubin rise in acute pancreatitis; calcium falls and can lead to clotting problems and DIC.")

q("pancare", "A client with acute pancreatitis has repeated vomiting and severe abdominal swelling from an ileus. Which intervention does the nurse anticipate?",
 ["Starting a high-fat oral diet || Clients stay NPO.",
  "Giving oral fluids freely || NPO rests the pancreas.",
  "*Inserting an NG tube",
  "Holding all IV fluids || IV fluids are part of initial care."],
 "An NG tube is used for vomiting or severe abdominal swelling (ileus). Initial care: NPO, IV fluids and electrolytes, IV pain control, glucose control and frequent labs.")

q("pancare", "A nurse teaches a client being discharged after pancreatitis. Which findings should the client report to the provider? " + SATA,
 ["*Worsening abdominal pain",
  "*A fever",
  "Choosing low-fat, high-protein meals || That is the correct diet, not a problem.",
  "*Yellowing of the skin",
  "Feeling less craving to smoke || Expected, not a warning sign."],
 "Discharge teaching: avoid alcohol, stop smoking, eat low-fat high-protein meals, check blood sugar, and report worsening pain, fever or jaundice.")

q("creon", "A client with chronic pancreatitis is taking pancrelipase. Which client statement needs correction?",
 ["'I take it with every meal and snack.' || Correct teaching.",
  "'If I can't swallow it, I sprinkle it on applesauce.' || Correct teaching.",
  "*'I crush the capsules and stir them into water.'",
  "'I swallow the capsules whole when I can.' || Correct teaching."],
 "Pancrelipase is taken with every meal and snack, swallowed whole when possible, or opened and sprinkled on an acidic soft food such as applesauce; do not crush or chew.")

q("creon", "Which pairings of a pancrelipase enzyme with the nutrient it breaks down are correct? " + SATA,
 ["*Lipase: fat",
  "Lipase: protein || Lipase breaks down fat.",
  "*Amylase: carbohydrates",
  "Amylase: fat || Amylase breaks down carbs.",
  "*Protease: protein"],
 "Pancrelipase replaces missing enzymes: lipase for fat, amylase for carbohydrates and protease for protein.")

q("pcsx", "Which finding best distinguishes pancreatic cancer in the head of the pancreas from acute cholecystitis?",
 ["A positive Murphy's sign || Points to cholecystitis.",
  "*Painless jaundice",
  "RUQ pain after a fatty meal spreading to the right shoulder || Points to cholecystitis.",
  "Fever with leukocytosis || Points to cholecystitis."],
 "Painless jaundice is the classic sign of pancreatic cancer in the head of the pancreas; it is usually found late.")

q("pcdx", "A 68-year-old client is being worked up for a suspected pancreatic tumor. Which studies does the nurse expect? " + SATA,
 ["*CT with contrast",
  "*MRI with contrast",
  "A HIDA scan || Evaluates gallbladder function, not a tumor.",
  "*A PET scan",
  "*A CEA level"],
 "CT or MRI with contrast best shows a pancreatic tumor, and PET scans may be used. CA 19-9 and CEA are elevated tumor markers.")

q("whipple", "Two days after a Whipple procedure, a client has nausea and vomiting from delayed gastric emptying. Which intervention does the nurse anticipate?",
 ["*NPO at first and possibly an NG tube",
  "A high-fat meal to stimulate the stomach || The client is kept NPO at first.",
  "Strict bedrest until it resolves || Early walking prevents clots.",
  "Checking blood glucose only || Not the management for this complication."],
 "Delayed gastric emptying after a Whipple is managed with NPO status at first and possibly an NG tube.")

q("whipple", "A nurse is monitoring a client after a Whipple procedure. Which findings should be reported promptly? " + SATA,
 ["*A new fever",
  "Walking in the hallway with SCDs in place || Expected clot prevention.",
  "*Greenish-yellow drainage in the drain",
  "*Falling H&H with incision bleeding",
  "Wearing SCDs while in bed || Expected clot prevention."],
 "After a Whipple, watch for bleeding, infection, fistula and bile leak; report fever, bleeding or unexpected drain output. Greenish-yellow drainage suggests a bile leak.")
