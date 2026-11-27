T = "e5ibd"; SET = "20261127"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("overview", "A 52-year-old librarian has inflammatory bowel disease. Which goal of treatment does the nurse reinforce?",
 ["*Maintain remission and limit exacerbations",
  "Treat a functional disorder with no tissue injury || That describes IBS, not IBD.",
  "Keep the disease from turning into IBS || IBD does not turn into IBS.",
  "Remove all colon cancer risk for life || IBD increases colon cancer risk."],
 "IBD treatment aims to maintain remission and limit exacerbations. IBS treatment is symptom management because IBS causes no structural damage.")

q("immune", "A nurse reviews four health histories. Which client has the most risk factors for an autoimmune disease such as IBD?",
 ["*A woman with an existing autoimmune condition and a family history of IBD",
  "A man who exercises daily and has no family history of IBD || Exercise is not a listed risk factor.",
  "A man whose immune response is too weak to fight infection || Too little response = immunosuppressed.",
  "A woman who eats fiber-rich foods and has no other illness || Fiber is not a listed trigger."],
 "Risk factors include genetic or family predisposition, an existing autoimmune condition, female gender, and environmental triggers such as smoking, stress, infection or chemical exposure.")

q("compare", "A nursing student describes UC and Crohn's disease. Which statement needs correction?",
 ["'UC affects only the mucosal layer.' || Correct: UC is mucosal.",
  "'Crohn's can have skip lesions.' || Correct: Crohn's is patchy.",
  "*'UC can appear anywhere from mouth to anus.'",
  "'Both raise the risk of colon cancer.' || Correct: both share this risk."],
 "UC is continuous and mucosal, limited to the rectum and colon. Crohn's is patchy, transmural and can occur anywhere in the GI tract ('gum to bum').")

q("compare", "A 44-year-old electrician's colonoscopy shows one continuous ulcerated area starting at the rectum and limited to the mucosa. Which complication should the nurse watch for?",
 ["Fistula draining to the skin || Fistulas are a Crohn's complication.",
  "Abscess beside the anus || Abscesses are a Crohn's complication.",
  "*Toxic megacolon",
  "Stricture from full-thickness scarring || Strictures are a Crohn's complication."],
 "Continuous mucosal disease from the rectum is UC. UC complications: hemorrhage, perforation, toxic megacolon, colorectal cancer. Crohn's complications: strictures, obstruction, fistulas, abscesses.")

q("ucassess", "Which client statement shows understanding of how ulcerative colitis affects the bowel wall?",
 ["'It inflames every layer of my bowel wall.' || That is Crohn's (transmural).",
  "*'Only the inner lining of my colon is inflamed.'",
  "'It leaves healthy patches between sick areas.' || Skip lesions are Crohn's.",
  "'My bowel wall looks normal; it's only symptoms.' || That is IBS."],
 "UC begins in the rectum and spreads continuously through the colon, affecting the mucosal layer only.")

q("ucassess", "A 28-year-old firefighter is being assessed for ulcerative colitis. Which client statements are consistent with UC? " + SATA,
 ["*'When I need to go, I have to go right now.'",
  "*'I've lost weight without trying.'",
  "*'I see mucus and blood in my stool.'",
  "'The pain is mostly in my lower right side.' || Right lower pain fits Crohn's; UC is often left lower.",
  "'My stools are greasy, with no blood.' || Greasy stools fit Crohn's."],
 "UC findings include frequent stools with blood and mucus, cramps, urgency, left lower abdominal pain, anemia and weight loss.")

q("megacolon", "A nurse is assigned four clients with ulcerative colitis. Which client should the nurse see first?",
 ["*A client in a severe flare with new marked distention and a heart rate of 128",
  "A client asking when colorectal cancer screening is due || Important, but not urgent.",
  "A client whose mild cramps eased after a stool || Expected and resolving.",
  "A client in remission asking for a diet handout || Stable; teaching can wait."],
 "Marked distention with tachycardia in severe UC can signal toxic megacolon or perforation; report severe distention, fever or signs of shock immediately.")

q("megacolon", "A nurse teaches a client with ulcerative colitis about complications. Which client statement needs correction?",
 ["'I could have heavy bleeding from my bowel.' || Correct: hemorrhage is a UC complication.",
  "'My colon could perforate.' || Correct: perforation is a UC complication.",
  "*'Fistulas and abscesses are my main risks.'",
  "'I'll need colorectal cancer screening.' || Correct: colorectal cancer is a UC complication."],
 "UC complications are hemorrhage, perforation, toxic megacolon and colorectal cancer. Fistulas and abscesses are Crohn's complications.")

q("cdassess", "A nurse reviews the chart of a client with Crohn's disease. Which documented finding is least consistent with Crohn's and needs clarification?",
 ["Patchy lesions in the small intestine || Typical: skip lesions anywhere in the GI tract.",
  "*Continuous inflammation starting at the rectum",
  "Loose, greasy stools with weight loss || Typical: malabsorption and weight loss.",
  "Abdominal pain in the right lower area || Typical Crohn's pain location."],
 "Crohn's: loose, watery or greasy stools, often right lower pain, patchy skip lesions anywhere in the GI tract, malabsorption and weight loss. Continuous inflammation from the rectum is UC.")

q("cdassess", "A 31-year-old chef with Crohn's disease says, 'I eat plenty, so why do I keep losing weight?' Which response is accurate?",
 ["'You are probably eating too much fat.' || Overeating is not the cause.",
  "'Weight loss is a sign of toxic megacolon.' || Toxic megacolon is a UC complication.",
  "*'Your inflamed bowel can't absorb nutrients well.'",
  "'Weight loss doesn't happen with Crohn's.' || Malabsorption and weight loss are typical."],
 "Crohn's causes malabsorption from inflamed bowel, so nutritional deficits, anemia and weight loss are common.")

q("dx", "A client scheduled for IBD testing reviews what each test shows. Which client statement needs correction?",
 ["'The biopsy will confirm the diagnosis.' || Correct: endoscopy with biopsy confirms it.",
  "'The CT or MRI looks at my bowel wall.' || Correct: shows the bowel and bowel wall.",
  "*'The stool culture tells how malnourished I am.'",
  "'My albumin level checks my nutrition.' || Correct: albumin reflects malnutrition."],
 "Stool culture rules out intestinal infection. Albumin shows malnutrition; CT or MRI shows the bowel and bowel wall; endoscopy with biopsy confirms the diagnosis.")

q("fe", "A nursing student says frequent IBD diarrhea causes metabolic alkalosis and high sodium. Which correction should the nurse give?",
 ["*'Diarrhea causes metabolic acidosis and low sodium.'",
  "'Diarrhea causes high potassium levels.' || Diarrhea causes hypokalemia.",
  "'Diarrhea causes high magnesium levels.' || Diarrhea causes hypomagnesemia.",
  "'Diarrhea causes fluid overload.' || Diarrhea causes dehydration."],
 "Frequent diarrhea can cause hyponatremia, hypokalemia, hypomagnesemia, chloride loss, metabolic acidosis and dehydration.")

q("nursing", "A client is admitted with a severe Crohn's flare. Which order should the nurse question?",
 ["NPO bowel rest with IV fluids || Expected in a severe flare.",
  "Corticosteroids as prescribed || Expected in a severe flare.",
  "*Regular diet with high-fiber snacks",
  "Daily weight with intake and output || Expected monitoring."],
 "Severe flare care: NPO bowel rest with IV fluids, corticosteroids, nutrition support such as parenteral nutrition, perianal skin protection, and monitoring of vital signs, weight, I&O and stools.")

q("nursing", "A 46-year-old mail carrier in a severe UC flare has frequent, heavy bloody diarrhea. For which problems is the nurse monitoring?",
 ["Fluid overload and high blood count || Losses cause the opposite.",
  "*Hypovolemia and anemia",
  "Constipation and weight gain || Not expected with heavy diarrhea.",
  "Metabolic alkalosis and hyperkalemia || Diarrhea causes acidosis and hypokalemia."],
 "Frequent diarrhea and bleeding can cause hypovolemia and anemia; monitor vital signs, weight, I&O and stool output.")

q("steroid", "A client in a UC flare is prescribed methylprednisolone. By which routes can this drug be given?",
 ["Inhaled only || Not a listed route.",
  "Subcutaneous injection only || Not a listed route.",
  "Applied to the skin only || Not a listed route.",
  "*By mouth, rectally or IV"],
 "Methylprednisolone can be given by mouth, rectally or IV; prednisone is given by mouth. Corticosteroids give short-term control of acute exacerbations.")

q("asa", "A client taking sulfasalazine for UC says, 'I stopped my folic acid because I feel fine.' Which response is best?",
 ["'That's fine; folic acid is only for flares.' || Folic acid is part of sulfasalazine teaching.",
  "*'Folic acid supplementation is part of your sulfasalazine therapy.'",
  "'You can stop sulfasalazine too when you feel well.' || It maintains remission.",
  "'You need a TB test instead of folic acid.' || TB screening is for biologics."],
 "Sulfasalazine is an oral 5-ASA for maintenance; teach folic acid supplementation and avoiding sun exposure.")

q("asa", "Which pairing of a 5-ASA drug and its use is correct?",
 ["Mesalamine: IV infusion for acute flares || Mesalamine is oral or rectal, for maintenance.",
  "Sulfasalazine: injected under the skin || Sulfasalazine is taken by mouth.",
  "*Sulfasalazine: taken by mouth for maintenance",
  "Mesalamine: short-term steroid for flares || Mesalamine is a 5-ASA, not a steroid."],
 "Sulfasalazine and mesalamine are 5-ASA anti-inflammatories that maintain remission; sulfasalazine is oral and mesalamine comes in oral and rectal forms.")

q("immuno", "A client asks how azathioprine differs from vedolizumab. Which response is accurate?",
 ["'Both are pills you take every day.' || Vedolizumab is a biologic given by infusion or injection.",
  "'Azathioprine works within a few weeks.' || Immunomodulators take weeks to months.",
  "*'Azathioprine is a daily pill; vedolizumab is given by infusion.'",
  "'Azathioprine targets one specific immune protein.' || It broadly suppresses immunity."],
 "Immunomodulators (azathioprine, methotrexate, mercaptopurine) are inexpensive oral daily drugs that broadly suppress immunity and take weeks to months. Biologics target specific immune proteins and are self-injected or given by IV infusion.")

q("bio", "A 39-year-old teacher is starting ustekinumab for Crohn's disease. Which teaching is the priority?",
 ["Take a folic acid supplement daily || That is sulfasalazine teaching.",
  "*Report a fever or other signs of infection promptly",
  "Expect benefit only after many months || Biologics work in a few weeks.",
  "Use it only during acute flares || Biologics are maintenance drugs."],
 "Biologics suppress immunity: screen for infection and TB first, report signs of infection and monitor during injections and infusions.")

q("bio", "Which statements about biologics for IBD are accurate? " + SATA,
 ["*They target specific immune proteins",
  "*They are very expensive",
  "*They work in a few weeks",
  "They are inexpensive daily pills || That describes immunomodulators.",
  "They need no screening before starting || Screen for infection and TB first."],
 "Biologics (ustekinumab, adalimumab, risankizumab, vedolizumab) target specific immune proteins, work in a few weeks, are very expensive, and are given by IV infusion or subcutaneous injection.")

q("nutri", "A client in a UC flare chooses lunch items. Which choice needs follow-up by the nurse?",
 ["Baked lean fish || Lean protein fits the flare diet.",
  "Fully cooked, skinless squash || Fits the flare diet.",
  "*Whole-grain bread with raw vegetables",
  "A ripe banana || Bananas fit the flare diet."],
 "Flare diet: soft, bland, low-fiber foods such as bananas, fully cooked skinless vegetables and lean protein. Raw vegetables and whole grains fit remission, not a flare.")

q("nutri", "A client with Crohn's asks how much fluid to drink each day. Which response is accurate?",
 ["'Limit fluids to slow the diarrhea.' || Hydration is needed in both phases.",
  "*'Aim for 8 to 10 glasses a day, in a flare or in remission.'",
  "'Only drink extra during a flare.' || Hydration applies in both phases.",
  "'Two or three glasses a day is enough.' || Too little; goal is 8-10."],
 "In both remission and flare: drink 8-10 glasses a day, eat small frequent meals, keep a food journal and avoid trigger foods.")

q("tpn", "A nurse checks a client receiving TPN. Which findings need action? " + SATA,
 ["*The TPN tubing has been hanging for 30 hours",
  "*An IV antibiotic is piggybacked into the TPN line",
  "*A port on the line is open and uncovered",
  "The central dressing was changed 4 days ago || Due every 7 days; not yet due.",
  "The last fingerstick glucose was 5 hours ago || Due every 6 hours; not yet due."],
 "TPN: change tubing every 24 hours with a micron filter, give no other medications in the line, keep all ports sterile, check fingerstick glucose every 6 hours and change the central dressing every 7 days.")

q("tpn", "Besides fingerstick glucose, which data does the nurse monitor for a client receiving TPN?",
 ["Peak flow readings || Not part of TPN monitoring.",
  "Pupil size and reaction || Not part of TPN monitoring.",
  "Food journal entries only || Not part of TPN monitoring.",
  "*Labs, weight and intake and output"],
 "For TPN, monitor fingerstick glucose every 6 hours plus labs, weight and I&O.")

q("surg", "A client with Crohn's disease asks whether a J-pouch could cure the disease. Which response is accurate?",
 ["'Yes, a J-pouch cures Crohn's.' || A J-pouch is a UC surgery.",
  "*'A J-pouch is a UC surgery; Crohn's uses bowel resection for complications.'",
  "'Surgery is never done for Crohn's.' || Bowel resection treats Crohn's complications.",
  "'Bowel resection cures Crohn's permanently.' || Crohn's can come back."],
 "Crohn's: bowel resection for complications, though disease can return. UC: J-pouch or proctocolectomy with permanent ileostomy; removing the colon can be definitive.")

q("surg", "A client had a proctocolectomy with permanent ileostomy for UC. Which client statement shows understanding?",
 ["'My rectum was left in place.' || The colon and rectum are removed.",
  "'The stoma will be closed in a few months.' || The ileostomy is permanent.",
  "*'I will have a stoma from now on.'",
  "'My Crohn's could come back in the colon.' || This client has UC, and the colon is removed."],
 "Proctocolectomy with permanent ileostomy leaves a permanent stoma; UC surgery that removes the colon can be definitive.")

q("health", "A client's Crohn's symptoms began and were diagnosed 3 years ago. The client asks when colorectal cancer screening starts. Which response is accurate?",
 ["'Right now, then every month.' || Too early and too often.",
  "*'About 8 years after diagnosis, then every 1 to 3 years.'",
  "'Only once, at age 75.' || Not the IBD schedule.",
  "'Never; Crohn's doesn't raise cancer risk.' || IBD increases colon cancer risk."],
 "Colorectal cancer screening for IBD begins about 8 years after diagnosis or symptom onset, then every 1-3 years, individualized to risk.")
