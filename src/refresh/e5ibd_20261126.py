T = "e5ibd"; SET = "20261126"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("overview", "A 26-year-old barista has IBS-C. She asks what the 'C' means. Which response is accurate?",
 ["'It stands for colitis, like UC.' || IBS is not colitis.",
  "*'It means the constipation type of IBS.'",
  "'It means it can turn into Crohn's.' || IBS does not become Crohn's.",
  "'It means a higher colon cancer risk.' || IBS does not raise cancer risk."],
 "IBS is a functional disorder with episodes of diarrhea and/or constipation; IBS-D is the diarrhea type and IBS-C is the constipation type.")

q("immune", "A nurse explains how immune response relates to disease. Which statement is correct?",
 ["Too little response causes autoimmune disease || Too little = immunosuppressed.",
  "A normal response causes autoimmune disease || Normal is homeostasis.",
  "*Too little response = immunosuppressed; too much = autoimmune",
  "Autoimmune disease means the immune system is absent || It is exaggerated, not absent."],
 "Too little immune response = immunosuppressed; too much = autoimmune. In IBD the immune system can't tell self from non-self and attacks the bowel.")

q("compare", "A nurse is caring for one client with UC and one with Crohn's disease. Which pain location pairing is typical?",
 ["UC: right lower; Crohn's: left lower || Reversed.",
  "Both: right upper quadrant || Not typical of either.",
  "*UC: left lower; Crohn's: right lower",
  "Both: only around the umbilicus || Not the typical locations."],
 "UC pain is often left lower abdomen with cramps and urgency; Crohn's pain is often right lower abdomen.")

q("compare", "Which findings point toward Crohn's disease rather than ulcerative colitis? " + SATA,
 ["*Inflammation through every layer of the bowel wall",
  "Continuous inflammation starting at the rectum || That is UC.",
  "*A cobblestone appearance",
  "*Disease in the small intestine",
  "Inflammation limited to the mucosal layer || That is UC."],
 "Crohn's is patchy, transmural, cobblestone and can occur anywhere in the GI tract. UC is continuous, mucosal and limited to the rectum and colon.")

q("ucassess", "A 33-year-old accountant with UC reports fatigue, and her hemoglobin is low. How does the nurse interpret this?",
 ["Unrelated to UC || Anemia is an expected UC finding.",
  "*Anemia is an expected finding with UC",
  "A sign of a draining fistula || Fistulas are a Crohn's complication.",
  "A sign of IBS || IBS does not cause anemia."],
 "UC findings include frequent stools with blood and mucus, cramps, urgency, left lower pain, anemia and weight loss.")

q("ucassess", "A nurse teaches a client newly diagnosed with UC. Which client statement shows understanding of where the disease occurs?",
 ["'It can show up in my mouth and small intestine.' || That describes Crohn's.",
  "*'It starts in my rectum and spreads up my colon without skipping.'",
  "'It goes through every layer of my bowel wall.' || That is Crohn's (transmural).",
  "'It forms patches with healthy bowel between them.' || That is Crohn's."],
 "UC begins in the rectum and spreads continuously through the colon, affecting the mucosal layer only.")

q("megacolon", "A client is in a severe UC flare. Which assessment cluster should the nurse watch most closely to detect toxic megacolon?",
 ["Peak flow and lung sounds || Not related to toxic megacolon.",
  "Food journal entries || Diet tracking, not a danger sign.",
  "Hand skin turgor and appetite || Not specific cues.",
  "*Increasing abdominal distention, fever and heart rate"],
 "Marked distention with fever and tachycardia in severe UC can signal toxic megacolon or perforation and must be reported immediately.")

q("megacolon", "Which complication pairing for UC and Crohn's disease is correct?",
 ["*UC: toxic megacolon; Crohn's: fistulas",
  "UC: fistulas; Crohn's: toxic megacolon || Reversed.",
  "UC: abscesses; Crohn's: hemorrhage || Abscesses are a Crohn's complication.",
  "UC: strictures; Crohn's: colorectal cancer only || Strictures are Crohn's; both raise cancer risk."],
 "UC complications: hemorrhage, perforation, toxic megacolon, colorectal cancer. Crohn's complications: strictures, obstruction, fistulas, abscesses.")

q("cdassess", "A nurse teaches a client with Crohn's disease which complications to report. Which client statements show understanding? " + SATA,
 ["*'I'll report vomiting and swelling with no stool.'",
  "*'I'll report drainage from a new opening on my skin.'",
  "'I'll report feeling hungry before meals.' || Not a complication.",
  "*'I'll report fever with a painful swelling near my anus.'",
  "'I'll report one soft stool after lunch.' || Not a complication."],
 "Crohn's transmural inflammation causes strictures and obstruction, fistulas and abscesses.")

q("cdassess", "A nurse compares the stools of clients with Crohn's disease and UC. Which statement is accurate?",
 ["Crohn's stools are hard and infrequent || Crohn's stools are loose.",
  "*Blood in the stool is less typical in Crohn's than in UC",
  "Crohn's stools always contain bright red blood || Blood is less typical.",
  "UC stools are greasy without blood || UC stools have blood and mucus."],
 "Crohn's: loose, watery or greasy stools, often right lower pain, malabsorption and weight loss; blood is less typical than in UC.")

q("dx", "A complete blood count is drawn for a client with an IBD flare. What information does the CBC give the nurse?",
 ["Bowel wall thickness || CT or MRI shows the bowel wall.",
  "*Anemia, infection and inflammation",
  "Confirmation of mucosal changes || Endoscopy with biopsy confirms this.",
  "Level of malnutrition || Albumin reflects malnutrition."],
 "CBC/WBC shows anemia, infection and inflammation; albumin shows malnutrition; CT or MRI shows the bowel wall; endoscopy with biopsy confirms the diagnosis.")

q("fe", "A client with long-standing Crohn's disease in remission is at risk for osteoporosis. Which diet teaching addresses this risk?",
 ["Avoid all dairy and calcium foods || Calcium is needed.",
  "Increase sodium intake || Not related to bone loss here.",
  "*Include calcium-rich foods",
  "Drink only clear liquids || Not a remission diet."],
 "Calcium deficiency in IBD raises osteoporosis risk; calcium-rich foods are part of the remission diet.")

q("nursing", "A client in a UC flare has frequent bloody diarrhea. Which nursing data best help detect hypovolemia?",
 ["*Vital signs, weight, intake and output, and stool output",
  "Peak flow readings || Not related.",
  "Food preferences only || Does not show fluid status.",
  "Pain score alone || Does not track fluid loss."],
 "Frequent diarrhea and bleeding can cause hypovolemia and anemia; monitor vital signs, weight, I&O and stool output.")

q("nursing", "A nurse is caring for a client with Crohn's disease. Which client statement needs immediate action?",
 ["'Can you give me information on the Crohn's & Colitis Foundation?' || Not urgent.",
  "'My cramping eased after my last stool.' || Not urgent.",
  "'Could I have a banana as a snack?' || Fits the flare diet.",
  "*'I'm passing a lot of blood and I feel faint.'"],
 "Gross bleeding, severe pain or distention, fever and signs of shock must be reported immediately; they can signal hemorrhage or perforation.")

q("steroid", "A client is admitted with an acute IBD exacerbation. Which drug does the nurse expect for short-term control of the flare?",
 ["Mesalamine || A 5-ASA maintenance drug.",
  "Azathioprine || An immunomodulator for maintenance.",
  "*Methylprednisolone",
  "Vedolizumab || A biologic for maintenance."],
 "Corticosteroids (methylprednisolone by mouth, rectally or IV; prednisone by mouth) give short-term control of acute exacerbations; the other drugs maintain remission.")

q("asa", "A client asks why a folic acid supplement was added after starting a new IBD medicine. Which medicine was most likely started?",
 ["Azathioprine || Teaching is CBC and liver monitoring.",
  "Adalimumab || Teaching is TB and infection screening.",
  "Prednisone || A short-term steroid for flares.",
  "*Sulfasalazine"],
 "Sulfasalazine is an oral 5-ASA for maintenance; teach folic acid supplementation and avoiding sun exposure.")

q("asa", "Which statements about 5-ASA drugs for IBD are accurate? " + SATA,
 ["*They are used to maintain remission",
  "They are given by IV infusion for acute flares || Steroids treat flares.",
  "*Mesalamine can be given rectally",
  "They require TB screening before each dose || That applies to biologics.",
  "*Sulfasalazine is taken by mouth"],
 "Sulfasalazine and mesalamine are the 5-ASA maintenance drugs; mesalamine comes in oral and rectal forms, and sulfasalazine is oral.")

q("immuno", "A client taking methotrexate for Crohn's disease reports a fever. What is the nurse's main concern?",
 ["An expected flare symptom || Fever needs evaluation.",
  "*Infection, because immunomodulators broadly suppress immunity",
  "Sun sensitivity from the drug || That is sulfasalazine teaching.",
  "Low folic acid only || Not the concern for fever."],
 "Immunomodulators (azathioprine, methotrexate, mercaptopurine) broadly suppress immunity; monitor CBC and liver function and follow infection precautions.")

q("bio", "A client receiving vedolizumab asks whether it is only for flares. Which response is accurate?",
 ["'Yes, it's used only during acute flares.' || Corticosteroids are for flares.",
  "'It's a steroid that works short term.' || It's a biologic.",
  "'It's a 5-ASA anti-inflammatory.' || 5-ASAs are sulfasalazine and mesalamine.",
  "*'It's a biologic used to keep the disease in remission.'"],
 "Biologics (ustekinumab, adalimumab, risankizumab, vedolizumab) are maintenance drugs given by IV infusion or subcutaneous injection.")

q("bio", "A nurse prepares to give a client a scheduled dose of adalimumab. Which findings should the nurse report to the provider before giving it? " + SATA,
 ["*A new fever",
  "The client is in remission || Expected goal of therapy.",
  "*A productive cough",
  "*No record of TB screening",
  "The client asks about the drug's cost || Not a reason to hold."],
 "Biologics suppress immunity: screen for infection and TB first, report signs of infection and monitor during injections and infusions.")

q("nutri", "A client is in a UC flare. Which teaching points fit the flare diet? " + SATA,
 ["*Drink 8-10 glasses of fluid a day",
  "Eat raw vegetables at each meal || Flare diet is low fiber.",
  "*Eat small, frequent meals",
  "*Choose lean protein",
  "Add whole-grain bran cereal || Too high in fiber for a flare."],
 "Flare diet: soft, bland, low fiber, bananas, fully cooked skinless vegetables and lean protein. In both phases: hydrate, eat small frequent meals, keep a food journal and avoid trigger foods.")

q("nutri", "A client whose Crohn's is in remission reviews the diet plan. Which client statement needs correction?",
 ["'I'll add fiber-rich whole foods.' || Correct for remission.",
  "*'Now that I'm well, I can stop keeping my food journal.'",
  "'I'll include calcium-rich foods.' || Correct for remission.",
  "'I'll keep eating small, frequent meals.' || Correct in both phases."],
 "A food journal, small frequent meals, hydration and avoiding trigger foods apply in both remission and flare.")

q("tpn", "A client starting TPN asks what is in the bag. Which client statement shows understanding?",
 ["'It's mostly whole blood.' || TPN does not contain blood.",
  "'It's just sugar water.' || It contains much more.",
  "*'It has protein, carbs, fats, electrolytes, vitamins and minerals.'",
  "'It only contains fats.' || It contains all macronutrients."],
 "TPN contains macronutrients (protein, carbohydrates, lipids) plus electrolytes, vitamins and minerals.")

q("tpn", "Which actions are correct when managing a client's TPN infusion? " + SATA,
 ["*Use tubing with a micron filter",
  "Change the central line dressing every 24 hours || The dressing is changed every 7 days.",
  "*Run the TPN on an infusion pump",
  "*Use the line for TPN only",
  "Hang the TPN by gravity || TPN runs on a pump."],
 "TPN: infusion pump, check the label, fingerstick glucose every 6 hours, tubing every 24 hours with a micron filter, central dressing every 7 days, no other medications in the line, sterile ports.")

q("surg", "A client who had a J-pouch created for UC explains the surgery. Which statement shows understanding?",
 ["'I'll have a permanent stoma.' || That is proctocolectomy with permanent ileostomy.",
  "'My colon is still in place.' || The colon and rectum are removed.",
  "*'My pouch was made from the end of my small intestine.'",
  "'The pouch was made from my stomach.' || It's made from the small intestine."],
 "A J-pouch (ileal pouch-anal anastomosis) is an internal reservoir made from the end of the small intestine after the colon and rectum are removed.")

q("surg", "Which statements about surgery for IBD are accurate? " + SATA,
 ["*Bowel resection treats Crohn's complications",
  "A J-pouch is the usual surgery for Crohn's || J-pouch is for UC.",
  "*Proctocolectomy with permanent ileostomy leaves a stoma",
  "*A J-pouch is built after the colon and rectum are removed",
  "Bowel resection cures Crohn's || Crohn's can come back."],
 "Crohn's: bowel resection for complications, but the disease can return. UC: J-pouch or proctocolectomy with permanent ileostomy; removing the colon can be definitive.")

q("health", "A nurse reviews ways to prevent IBD exacerbations. Which client statement needs correction?",
 ["'I'll work on reducing my stress.' || Correct prevention.",
  "'I'll stay well hydrated.' || Correct prevention.",
  "*'I'll stop my maintenance medicine once I feel well.'",
  "'I'll avoid my trigger foods.' || Correct prevention."],
 "Health promotion to prevent exacerbations: avoid trigger foods, reduce stress and stay hydrated; maintenance drugs keep the disease in remission.")
