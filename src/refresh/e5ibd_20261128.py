T = "e5ibd"; SET = "20261128"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("overview", "A 40-year-old bus driver asks why his sister's IBD needs long-term medication while his own IBS does not. Which explanation is accurate?",
 ["IBS causes more tissue damage than IBD does || IBS causes no structural damage.",
  "*IBD is chronic inflammation with tissue injury; IBS has no structural damage",
  "IBD is a functional disorder with a normal colon on exam || That describes IBS.",
  "Both conditions are autoimmune and damage the bowel wall || Only IBD is autoimmune with tissue injury."],
 "IBS is a functional GI disorder: symptoms without structural damage, treated with symptom management. IBD is an autoimmune disease with chronic inflammation and tissue injury; treatment aims to maintain remission and limit exacerbations.")

q("immune", "A nurse is teaching a group about the immune system. Which statement correctly describes a client with an immune response that is too weak?",
 ["The client has an autoimmune disease like UC || Too much response = autoimmune.",
  "The client's body attacks its own bowel tissue || That is an exaggerated (autoimmune) response.",
  "*The client is immunosuppressed and at risk for infection",
  "The client is at normal immune homeostasis || A weak response is not homeostasis."],
 "Too little immune response = immunosuppressed; too much = autoimmune. In IBD the immune system can't tell self from non-self and attacks the bowel.")

q("compare", "A nurse reviews the endoscopy report of a 35-year-old welder: patchy inflammation in the small intestine with a cobblestone appearance and healthy bowel between areas. Which complication should the nurse watch for?",
 ["Toxic megacolon || A UC complication.",
  "*Fistula formation",
  "Continuous rectal bleeding from mucosal ulcers || Continuous mucosal disease is UC.",
  "No complications, since the disease is patchy || Crohn's has strictures, fistulas, abscesses."],
 "Patchy, cobblestone disease in the small intestine is Crohn's. Crohn's complications: strictures, obstruction, fistulas and abscesses. UC complications: hemorrhage, perforation, toxic megacolon and colorectal cancer.")

q("compare", "A nurse explains why Crohn's disease can form fistulas but UC usually does not. Which statement is most accurate?",
 ["*Crohn's inflames every layer of the wall; UC inflames only the mucosa",
  "UC inflames every layer of the wall; Crohn's inflames only the mucosa || The depths are reversed.",
  "Crohn's is limited to the rectum and colon || Crohn's can be anywhere in the GI tract.",
  "UC skips areas, so the wall stays strong || UC is continuous, not patchy."],
 "UC is continuous and mucosal, rectum to colon only. Crohn's is patchy and transmural (all layers), which leads to strictures and fistulas.")

q("ucassess", "A nurse collects data on a client admitted with suspected UC. Which question best targets a typical UC finding?",
 ["'Have you noticed greasy stools that float?' || Greasy stools fit Crohn's.",
  "'Is your pain mainly in the lower right side?' || Right lower pain fits Crohn's.",
  "*'Have you seen blood or mucus in your stool?'",
  "'Has any stool drained from an opening in your skin?' || A fistula is a Crohn's complication."],
 "UC findings include frequent stools with blood and mucus, abdominal cramps, urgency, left lower abdominal pain, anemia and weight loss.")

q("ucassess", "A client with UC asks why the provider says the disease is 'continuous.' Which response is accurate?",
 ["'It inflames every layer of the bowel wall.' || Transmural is Crohn's.",
  "'It can appear in your mouth and small intestine.' || UC is rectum and colon only.",
  "'Your symptoms never stop, even in remission.' || 'Continuous' describes the lesion pattern.",
  "*'It starts in the rectum and spreads up the colon with no skipped areas.'"],
 "UC begins in the rectum and spreads continuously through the colon, affecting the mucosal layer only.")

q("megacolon", "A client in a severe UC flare has a PRN antidiarrheal ordered. Which finding should make the nurse hold the dose and report?",
 ["Mild cramping relieved by a stool || Expected and resolving.",
  "Two loose stools since breakfast || Not a sign of toxic megacolon.",
  "*Increasing abdominal distention with fever",
  "The client asks about cancer screening || Teaching need, not a red flag."],
 "Antidiarrheals need caution and can be dangerous in severe UC or suspected toxic megacolon. Marked distention with fever or tachycardia must be reported immediately.")

q("megacolon", "Which findings in a client with ulcerative colitis must the nurse report immediately? " + SATA,
 ["*Rigid, markedly distended abdomen",
  "*Large amount of bright red rectal blood",
  "*Heart rate of 126 with falling blood pressure",
  "Asking when the next colonoscopy is due || A teaching need, not urgent.",
  "Cramping that eased after passing stool || Expected and resolving."],
 "UC complications are hemorrhage, perforation, toxic megacolon and colorectal cancer. Report gross bleeding, severe pain or distention, fever or signs of shock immediately.")

q("cdassess", "A client with Crohn's disease calls the clinic. Which report suggests a bowel obstruction from a stricture?",
 ["'I had three loose stools today.' || Loose stools are typical Crohn's.",
  "*'I'm vomiting, my belly is swelling and I've had no stool.'",
  "'I see mucus in my stool.' || Not an obstruction sign.",
  "'I feel hungry before every meal.' || Not a complication."],
 "Crohn's transmural inflammation causes strictures and obstruction, fistulas and abscesses. Report new distention or constipation, cramping and vomiting.")

q("cdassess", "Which findings would the nurse expect in a client with Crohn's disease? " + SATA,
 ["*Loose, watery stools",
  "*Low albumin with weight loss",
  "*Pain often in the right lower abdomen",
  "Continuous inflammation from the rectum || That is UC.",
  "Inflammation in the mucosa only || Crohn's is transmural."],
 "Crohn's: loose, watery or greasy stools, often right lower pain, patchy skip lesions anywhere in the GI tract, malabsorption and weight loss; blood is less typical than in UC.")

q("dx", "A client with an IBD flare has a new increase in diarrhea. Which test result helps rule out an intestinal infection as the cause?",
 ["Serum albumin || Shows malnutrition.",
  "CT scan of the bowel wall || Shows the bowel and bowel wall.",
  "*Stool culture",
  "Serum electrolytes || Shows fluid and electrolyte losses."],
 "Stool culture rules out intestinal infection. Albumin shows malnutrition; CT or MRI shows the bowel and bowel wall; endoscopy with biopsy confirms the diagnosis; CBC/WBC shows anemia, infection and inflammation.")

q("fe", "A client with Crohn's disease has had many watery stools for 3 days. Which findings suggest dehydration? " + SATA,
 ["*Dizziness and a blood pressure drop on standing",
  "*Decreased urine output",
  "*Pulse of 118",
  "Bounding pulses || Not a listed dehydration sign.",
  "Steady weight gain || Dehydration causes rapid weight loss."],
 "Dehydration from diarrhea shows as tachycardia, orthostatic blood pressure changes, decreased urine output and rapid weight loss. Track stool frequency, weight and I&O.")

q("nursing", "A client with UC in a severe flare is in the bathroom often and has reddened skin around the anus. Which nursing action is best?",
 ["Encourage large, high-fiber meals || Not part of severe flare care.",
  "Give antidiarrheals freely for comfort || Use caution with antidiarrheals.",
  "*Protect the perianal skin and record stool output",
  "Limit IV fluids to reduce stool volume || IV fluids are part of flare care."],
 "Severe flare care: NPO bowel rest with IV fluids, corticosteroids, nutrition support such as parenteral nutrition, perianal skin protection, and monitoring of vital signs, weight, I&O and stools.")

q("nursing", "Which client with IBD should the nurse report to the provider first?",
 ["A client with Crohn's whose cramping eased after a stool || Expected, resolving.",
  "*A client with UC who has a fever and severe abdominal pain",
  "A client in remission asking for a remission diet || Stable; teaching need.",
  "A client asking about the Crohn's & Colitis Foundation || Psychosocial need, not urgent."],
 "Gross bleeding, severe abdominal pain or distention, fever and signs of shock must be reported immediately; they can signal hemorrhage or perforation.")

q("steroid", "A client in remission from UC asks why prednisone was stopped after the last flare. Which response is accurate?",
 ["'Prednisone cured your ulcerative colitis.' || Steroids do not cure IBD.",
  "'Prednisone only works when given IV.' || Prednisone is given by mouth.",
  "'Prednisone is a 5-ASA drug for remission.' || It is a corticosteroid for flares.",
  "*'Steroids control flares short term; other drugs maintain remission.'"],
 "Corticosteroids (methylprednisolone by mouth, rectally or IV; prednisone by mouth) give short-term control of acute exacerbations. Other drugs maintain remission. Monitor for adverse effects.")

q("asa", "A client with UC is prescribed mesalamine. Which statement shows the client understands the drug?",
 ["'I'll take it only during a flare.' || 5-ASA drugs maintain remission.",
  "*'It may come as a pill or a rectal form to keep me in remission.'",
  "'It's a steroid given through my IV.' || It is a 5-ASA, oral or rectal.",
  "'I need a TB test before every dose.' || TB screening is for biologics."],
 "Sulfasalazine and mesalamine are 5-ASA anti-inflammatories that maintain remission; mesalamine comes in oral and rectal forms, and sulfasalazine is oral.")

q("asa", "A nurse reinforces teaching for a client taking sulfasalazine. Which instructions are correct? " + SATA,
 ["*Take the prescribed folic acid supplement",
  "*Wear protection and limit time in the sun",
  "*Keep taking it when you feel well",
  "Give it as an injection under the skin || Sulfasalazine is oral.",
  "Use it only for short-term flare control || That describes steroids."],
 "Sulfasalazine is an oral 5-ASA for maintenance; teach folic acid supplementation and avoiding sun exposure.")

q("immuno", "A client starting azathioprine for Crohn's disease asks what monitoring to expect. Which response is accurate?",
 ["'Only a stool culture each month.' || Not the listed monitoring.",
  "*'Regular blood counts and liver tests, plus infection precautions.'",
  "'No monitoring, since it's an inexpensive pill.' || CBC and liver function are monitored.",
  "'A TB test before each daily dose.' || Not the listed monitoring."],
 "Immunomodulators (azathioprine, methotrexate, mercaptopurine) broadly suppress immunity, are inexpensive oral daily drugs and take weeks to months to work; monitor CBC and liver function and follow infection precautions.")

q("bio", "A nurse is preparing a client for a first dose of adalimumab. Which question is most important to ask first?",
 ["'Are you taking a folic acid supplement?' || That is sulfasalazine teaching.",
  "'Do you prefer the pill or the liquid?' || Biologics are injected or infused.",
  "*'Have you had TB screening and any recent signs of infection?'",
  "'Have you been out in the sun lately?' || Sun teaching is for sulfasalazine."],
 "Biologics suppress immunity: screen for infection and TB first, report signs of infection and monitor during injections and infusions.")

q("bio", "A client asks why the provider chose vedolizumab over methotrexate. Which difference supports this choice?",
 ["Vedolizumab is a cheaper daily pill || Biologics are very expensive infusions/injections.",
  "*Vedolizumab targets specific immune proteins and works in a few weeks",
  "Vedolizumab broadly suppresses immunity || Immunomodulators act broadly.",
  "Vedolizumab is used only for acute flares || Biologics are maintenance drugs."],
 "Biologics (ustekinumab, adalimumab, risankizumab, vedolizumab) target specific immune proteins, work in a few weeks, are very expensive and are given by IV infusion or subcutaneous injection. Immunomodulators take weeks to months.")

q("nutri", "A client with Crohn's disease in a flare asks what to have for dinner. Which meal fits best?",
 ["Raw spinach salad with seeds || Raw vegetables are not for a flare.",
  "Brown rice with raw peppers || Whole grains and raw vegetables fit remission.",
  "*Baked turkey with well-cooked, skinless zucchini",
  "Fried fast-food burger and fries || Not soft, bland or lean."],
 "Flare diet: soft, bland, low-fiber foods such as bananas, fully cooked skinless vegetables and lean protein.")

q("nutri", "A client with UC is now in remission. Which diet teaching is correct? " + SATA,
 ["*Add fiber-rich whole foods",
  "*Include calcium-rich foods",
  "*Continue keeping a food journal",
  "Eat mostly processed foods || Avoid processed foods in remission.",
  "Limit fluids to 3 glasses a day || Drink 8-10 glasses a day."],
 "Remission diet: fiber-rich whole foods, lean protein, calcium-rich foods, avoid processed foods. In both phases: 8-10 glasses of fluid, small frequent meals, a food journal and avoiding trigger foods.")

q("tpn", "A nurse is hanging TPN for a client with Crohn's. Which action is correct?",
 ["Run it by gravity at a slow rate || TPN runs on an infusion pump.",
  "*Use tubing with a micron filter",
  "Add the client's IV antibiotic to the bag || No other medications in the line.",
  "Plan to change the tubing every 7 days || Tubing changes every 24 hours."],
 "TPN: infusion pump, check the label, tubing every 24 hours with a micron filter, fingerstick glucose every 6 hours, central dressing every 7 days, no other medications in the line and sterile ports.")

q("tpn", "A client receiving TPN asks why the nurse is so careful with the line. Which explanation addresses the priority risk?",
 ["'To keep you from getting constipated.' || Not the priority risk.",
  "'To make sure you get enough fiber.' || Not the priority risk.",
  "*'A central line infection is the biggest risk, so we keep it sterile.'",
  "'To keep your hair from falling out.' || Not the priority risk."],
 "Central line infection is the priority TPN risk: sterile technique, keep all ports sterile, a dedicated line and dressing changes every 7 days.")

q("surg", "A client with UC asks how a J-pouch differs from a proctocolectomy with permanent ileostomy. Which response is accurate?",
 ["'Both leave you with a permanent stoma.' || A J-pouch is an internal reservoir.",
  "'A J-pouch keeps your colon in place.' || The colon and rectum are removed.",
  "*'A J-pouch is an internal reservoir; the other leaves a permanent stoma.'",
  "'A J-pouch is made from part of your stomach.' || It is made from the end of the small intestine."],
 "A J-pouch is an internal reservoir made from the end of the small intestine after the colon and rectum are removed. Proctocolectomy with permanent ileostomy leaves a permanent stoma.")

q("surg", "A client with Crohn's disease had part of the bowel removed for a stricture. Which statement needs correction?",
 ["'Surgery was done to treat a complication.' || Correct: resection treats complications.",
  "*'Now that it's removed, my Crohn's is cured.'",
  "'Crohn's could come back in another area.' || Correct: Crohn's can return.",
  "'I had a bowel resection, not a J-pouch.' || Correct: J-pouch is a UC surgery."],
 "Crohn's: bowel resection for complications, though the disease can return. UC: J-pouch or proctocolectomy with permanent ileostomy; removing the colon can be definitive.")

q("health", "A client with UC who recently had an ileostomy says, 'I'm too stressed and embarrassed to go out.' Which nursing actions are appropriate? " + SATA,
 ["*Address body image and ostomy adjustment",
  "*Support stress management",
  "*Refer to the Crohn's & Colitis Foundation",
  "Tell the client the feelings are all in their head || Dismissive; not supportive.",
  "Advise stopping maintenance drugs to feel better || Maintenance drugs keep remission."],
 "Psychosocial support for IBD: refer to the Crohn's & Colitis Foundation, address body image and ostomy adjustment, and support stress management.")
