T = "e5ibd"; SET = "20261125"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("overview", "A nurse is reviewing a client's history for possible bowel disease. Which finding points toward IBD rather than IBS?",
 ["A normal-appearing colon on examination || Fits IBS, a functional disorder.",
  "Gas and distention with alternating stool patterns || Fits IBS.",
  "*Bloody stools with nutritional deficits",
  "Symptoms with no structural damage || Fits IBS."],
 "IBS = symptoms without structural damage. IBD = chronic inflammation with tissue injury, such as bloody stools and nutritional deficits.")

q("immune", "A client with ulcerative colitis asks, 'Why is my own immune system attacking my bowel?' Which response is accurate?",
 ["'Your immune response is too weak to protect you.' || Too little response = immunosuppressed.",
  "*'It can't tell self from non-self, so it overreacts against your bowel.'",
  "'A bacteria has permanently infected your colon.' || IBD is autoimmune.",
  "'It's caused only by the foods you eat.' || Diet isn't the sole cause."],
 "IBD is autoimmune: the immune system can't tell 'self' from 'non-self' and mounts an exaggerated attack on the bowel.")

q("compare", "A client with Crohn's disease has painful ulcers in the mouth and asks if they are related. Best response?",
 ["'No, Crohn's affects only the colon and rectum.' || That describes UC.",
  "'No, Crohn's affects only the lining of the colon.' || Crohn's is transmural.",
  "'Only if you also have ulcerative colitis.' || Crohn's alone can do this.",
  "*'Yes, Crohn's can affect any part of the GI tract, mouth to anus.'"],
 "Crohn's is patchy and transmural and can occur anywhere in the GI tract ('gum to bum').")

q("compare", "Which features describe ulcerative colitis rather than Crohn's disease? " + SATA,
 ["*Continuous inflammation without skip areas",
  "Cobblestone appearance || That is Crohn's.",
  "*Inflammation limited to the mucosal layer",
  "*Disease confined to the rectum and colon",
  "Inflammation through all bowel wall layers || That is Crohn's (transmural)."],
 "UC is continuous, mucosal, rectum to colon only, with an ulcerative appearance.")

q("ucassess", "A client is admitted with suspected ulcerative colitis. Which finding is NOT expected with UC and should be reported for further evaluation?",
 ["Stools with blood and mucus || Expected in UC.",
  "Urgency with abdominal cramping || Expected in UC.",
  "*A fistula draining to the skin",
  "Left lower abdominal pain || Expected in UC."],
 "UC findings: frequent bloody, mucus stools, cramps, urgency, left lower pain, anemia and weight loss. Fistulas are a Crohn's complication.")

q("ucassess", "The nurse documents the admission assessment of a client in a UC flare. Which findings are consistent with UC? " + SATA,
 ["*Urgent need to pass stool",
  "Greasy, watery stools without blood || More typical of Crohn's.",
  "*Blood and mucus in the stool",
  "Pain mainly in the right lower abdomen || More typical of Crohn's.",
  "*Recent weight loss"],
 "UC findings include frequent stools with blood and mucus, cramps, urgency, left lower pain, anemia and weight loss.")

q("megacolon", "A client with ulcerative colitis suddenly passes large amounts of bright red blood. HR is 124 and BP is falling. Which complication does the nurse suspect?",
 ["*Hemorrhage",
  "Abscess || A Crohn's complication.",
  "Stricture || A Crohn's complication.",
  "An expected flare || Gross bleeding with shock signs is not expected."],
 "UC complications are hemorrhage, perforation, toxic megacolon and colorectal cancer; report gross bleeding or signs of shock.")

q("megacolon", "A client who has had ulcerative colitis for many years asks about long-term risks. Which complication needs ongoing screening?",
 ["Fistula formation || A Crohn's complication.",
  "Strictures from fibrosis || A Crohn's complication.",
  "*Colorectal cancer",
  "Abscesses || A Crohn's complication."],
 "UC complications include colorectal cancer; keep colorectal cancer screening on schedule.")

q("cdassess", "A client with Crohn's disease notices stool leaking from a new opening on the skin of the abdomen. Which complication does the nurse recognize?",
 ["Toxic megacolon || Most associated with UC.",
  "Hemorrhage || Bleeding, not a new tract to the skin.",
  "A stricture || A narrowing, not an opening.",
  "*Fistula"],
 "Crohn's transmural inflammation leads to strictures, obstruction, fistulas and abscesses.")

q("cdassess", "Which findings in a client with Crohn's disease suggest a complication? " + SATA,
 ["*Cramping, vomiting and distention with no stool",
  "*Fever with a tender, swollen area beside the anus",
  "Two soft stools after breakfast || Not a complication.",
  "*Drainage from a new opening on the skin",
  "Hunger before meals || Not a complication."],
 "Crohn's complications: strictures and obstruction, fistulas and abscesses.")

q("dx", "Which test result helps the nurse identify malnutrition in a client with Crohn's disease?",
 ["Stool culture || Rules out infection.",
  "*Serum albumin",
  "CT scan of the bowel || Imaging of the bowel wall.",
  "Endoscopy with biopsy || Confirms mucosal changes."],
 "Albumin reflects malnutrition; electrolytes and CBC are also checked.")

q("fe", "A client in an IBD flare has had frequent diarrhea for several days. Which imbalance does the nurse anticipate?",
 ["Metabolic alkalosis || Diarrhea causes acidosis.",
  "Hyperkalemia || Diarrhea causes hypokalemia.",
  "*Metabolic acidosis",
  "Hypernatremia || Diarrhea causes hyponatremia."],
 "Frequent diarrhea can cause hyponatremia, hypokalemia, hypomagnesemia, chloride loss, metabolic acidosis and dehydration.")

q("nursing", "A client admitted with a severe UC flare asks for a breakfast tray. Which response is best?",
 ["'Sure, a high-fiber cereal will firm your stools.' || High fiber isn't used in a flare.",
  "*'For now your bowel is resting, so you'll be NPO with IV fluids.'",
  "'Eat whatever you like; diet doesn't matter.' || Severe flares use bowel rest.",
  "'You can have a large meal if you take an antidiarrheal.' || Antidiarrheals need caution."],
 "Severe flare: NPO bowel rest with IV fluids as ordered, plus nutrition support such as parenteral nutrition if needed.")

q("nursing", "A client in a Crohn's flare has frequent stools and reddened perianal skin. Which actions should the nurse take? " + SATA,
 ["*Protect the perianal skin",
  "Encourage large, high-fiber meals || Not used in a severe flare.",
  "*Record stool frequency and any blood or mucus",
  "Give antidiarrheals freely for comfort || Use caution with antidiarrheals.",
  "*Monitor weight and intake and output"],
 "Flare care includes perianal skin protection and monitoring of vital signs, weight, I&O and stool output.")

q("steroid", "A client taking oral prednisone for a Crohn's flare makes four statements. Which needs correction?",
 ["'This medicine is for my flare.' || Correct.",
  "'My provider will watch for side effects.' || Correct; monitor adverse effects.",
  "*'I'll stay on prednisone for life to keep me in remission.'",
  "'Other drugs will keep me in remission later.' || Correct."],
 "Corticosteroids give short-term control of acute exacerbations; other drugs maintain remission.")

q("asa", "A client using rectal mesalamine asks, 'Is this a steroid for flares?' Which response is accurate?",
 ["'Yes, it's used only during acute flares.' || It's a maintenance drug.",
  "'Yes, and it's also given by IV.' || Mesalamine is oral or rectal.",
  "*'No, it's a 5-ASA anti-inflammatory used to maintain remission.'",
  "'No, it's a biologic that needs TB screening.' || It's a 5-ASA."],
 "Sulfasalazine and mesalamine are the 5-ASA maintenance drugs; mesalamine comes in oral and rectal forms.")

q("asa", "A client starting sulfasalazine for UC maintenance repeats back the teaching. Which statements show understanding? " + SATA,
 ["*'I'll take my folic acid supplement.'",
  "'I'll need a TB test before each dose.' || TB screening is for biologics.",
  "*'I'll limit my time in the sun.'",
  "'I'll get it by IV infusion at the clinic.' || It's taken by mouth.",
  "*'This medicine helps keep my UC in remission.'"],
 "Sulfasalazine is an oral 5-ASA for maintenance; teach folic acid supplementation and avoiding sun exposure.")

q("immuno", "A client starting mercaptopurine for Crohn's disease asks what follow-up to expect. Which response is best?",
 ["'No follow-up labs are needed.' || CBC and liver function are monitored.",
  "*'You'll have regular CBC and liver function blood tests.'",
  "'You'll need a sweat chloride test.' || Not related to this drug.",
  "'You'll get a hemoglobin A1C every week.' || Not the labs monitored."],
 "Immunomodulators (azathioprine, methotrexate, mercaptopurine): monitor CBC and liver function; infection precautions apply.")

q("bio", "A client newly prescribed risankizumab for Crohn's asks how it will be given. Which response is accurate?",
 ["'As a pill you take every day.' || That describes immunomodulators.",
  "'As a rectal enema.' || Mesalamine has a rectal form.",
  "*'By IV infusion or an injection under the skin.'",
  "'By inhaler twice a day.' || Not a route for biologics."],
 "Biologics (ustekinumab, adalimumab, risankizumab, vedolizumab) are given by IV infusion or subcutaneous injection.")

q("bio", "Four clients are scheduled for biologic doses today. Which client should the nurse question giving the dose to before contacting the provider?",
 ["Client in remission with no new complaints || No contraindication.",
  "Client asking about the cost of the drug || Not a safety concern.",
  "Client whose TB screening was completed || Screening is required first.",
  "*Client with a fever and a productive cough"],
 "Biologics suppress immunity; screen for infection and TB first and report signs of infection.")

q("nutri", "A client in a Crohn's flare asks for a snack. Which choice fits the flare diet best?",
 ["*A ripe banana",
  "A bowl of popcorn || High fiber; avoid in a flare.",
  "A raw apple with the skin || Raw, high fiber; avoid in a flare.",
  "Whole-grain crackers || Whole grains aren't flare foods."],
 "Flare diet: soft, bland, low-fiber foods such as bananas, fully cooked skinless vegetables and lean protein.")

q("nutri", "A client whose UC is in remission plans meals. Which choice should the nurse suggest the client limit?",
 ["Calcium-rich yogurt || Calcium-rich foods fit remission.",
  "Baked lean fish || Lean protein fits remission.",
  "*Packaged, processed snack foods",
  "Fiber-rich whole foods || These fit remission."],
 "Remission diet: fiber-rich whole foods, lean protein and calcium-rich foods, and avoid processed foods.")

q("tpn", "The nurse is about to hang a new bag of TPN. Which action should come first?",
 ["Hang it by gravity to save time || TPN runs on an infusion pump.",
  "*Check the label for accuracy against the order",
  "Piggyback the client's IV antibiotic into it || No other medications in the TPN line.",
  "Remove the micron filter from the tubing || Tubing uses a micron filter."],
 "TPN: check the label for accuracy, run on an infusion pump, use tubing with a micron filter and give no other medications in the line.")

q("tpn", "Which nursing actions help prevent central line infection in a client receiving TPN? " + SATA,
 ["*Keep all ports sterile",
  "Piggyback IV antibiotics into the TPN line || Use a dedicated line.",
  "*Use the line only for TPN",
  "Change the dressing only when it falls off || Change it every 7 days.",
  "*Change the central line dressing every 7 days"],
 "Central line infection is the priority risk: sterile technique, a dedicated line and dressing changes every 7 days.")

q("surg", "A client with Crohn's disease has a stricture causing a bowel obstruction. Which surgery does the nurse expect?",
 ["J-pouch creation || A UC surgery.",
  "*Bowel resection",
  "Proctocolectomy with permanent ileostomy || A UC surgery.",
  "Appendectomy || Doesn't treat Crohn's complications."],
 "Crohn's: bowel resection for complications, though disease can return. UC: J-pouch or proctocolectomy with permanent ileostomy.")

q("surg", "A client with UC who had a proctocolectomy with permanent ileostomy asks if the UC can come back in the colon. Best response?",
 ["'Yes, UC returns in most clients after surgery.' || Colon removal can be definitive for UC.",
  "'Yes, surgery only treats complications of UC.' || That describes Crohn's resection.",
  "*'Removing the colon and rectum can be definitive for UC.'",
  "'Only a J-pouch can prevent UC from returning.' || Both UC surgeries remove the colon."],
 "UC surgery that removes the colon can be definitive; Crohn's can come back after bowel resection.")

q("health", "A client newly diagnosed with Crohn's says, 'I don't know anyone else living with this.' Which nursing action is best?",
 ["Tell the client the worry is all in their head || Dismissive.",
  "Change the subject to medication teaching || Ignores the concern.",
  "*Refer the client to the Crohn's & Colitis Foundation",
  "Tell the client support groups are only for ostomy clients || Support fits all IBD clients."],
 "Psychosocial support: refer to the Crohn's & Colitis Foundation, address body image and ostomy adjustment and support stress management.")
