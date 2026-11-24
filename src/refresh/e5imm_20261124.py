T = "e5imm"; SET = "20261124"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("cycle", "A nurse explains the cell cycle to a 42-year-old client. A GI (gastrointestinal) cell that is busy making mucus is in which phase?",
  ["S phase || S phase is when DNA is made",
   "M phase || M phase is when the cell divides",
   "*G0 phase",
   "G2 phase || G2 is when the cell prepares for mitosis"],
  "G0 cells are metabolically active and carry out their specialized (differentiated) function, such as GI cells making mucus. G1 prepares, S makes DNA, G2 prepares for mitosis, M divides.")

q("types", "Four clients in an oncology clinic describe their diagnoses. Which client statement is accurate?",
  ["'My sarcoma started in my epithelial tissue.' || sarcoma starts in bone or soft tissue",
  "'My carcinoma started in my blood-forming tissue.' || carcinoma starts in epithelial tissue",
   "'My leukemia started in my bone tissue.' || leukemia starts in blood-forming tissue",
   "*'My lymphoma started in my lymph tissue.'"],
  "Cancer is classified by the tissue where it starts: carcinoma = epithelial, sarcoma = bone/soft tissue, lymphoma = lymph, leukemia = blood-forming tissue.")

q("why", "A nursing student asks why a 58-year-old client's regimen uses several chemotherapy drugs together. Which explanation is accurate?",
  ["Combining drugs makes them target only resting G0 cells || chemo attacks DNA synthesis or mitosis",
   "*Different drugs act on different phases of the cell cycle",
   "Combining drugs keeps them from harming normal cells || chemo also destroys normal cells",
   "Combining drugs means cycles over time aren't needed || cycles reach cells as they regrow"],
  "Chemotherapy drugs are combined because different drugs hit different phases of the cell cycle, so together they impact multiple phases.")

q("tox", "A 19-year-old client is in the third week of chemotherapy. Which findings does the nurse link to damage of rapidly dividing normal cells? " + SATA,
  ["*Hair thinning and hair loss",
   "Faster, thicker hair growth || hair follicle damage causes alopecia",
   "*Painful mouth sores",
   "*Low blood cell counts",
   "Sharper nerve sensation in the feet || neuropathy is a listed adverse effect"],
  "Chemo destroys rapidly dividing normal cells (hair follicles, GI lining, bone marrow) the same way it destroys cancer cells, causing alopecia, stomatitis and marrow suppression.")

q("nadir", "A 72-year-old client in long-term care is on day 11 after chemotherapy and has a very low platelet count. Which care plan item should the nurse question?",
  ["Using a small-gauge needle for injections || this reduces bleeding",
   "Applying prolonged pressure after blood draws || this reduces bleeding",
   "*Offering a firm-bristle toothbrush for mouth care",
   "Providing an electric razor for shaving || this reduces bleeding"],
  "Day 10–14 is the nadir, when bleeding risk is greatest. Bleeding precautions include a small-gauge needle, prolonged pressure, a soft toothbrush and an electric razor.")

q("nadir", "A leukopenic client at the chemotherapy nadir has a reddened incision with no pus and a normal temperature. How should the nurse interpret this?",
  ["No infection is present because there is no pus || too few white cells may mean no pus forms",
   "A normal temperature rules out any infection || fever may be a late sign in leukopenia",
   "The wound is healing well and needs no more checks || close monitoring is needed",
   "*Infection may still be present and needs close monitoring"],
  "In leukopenia there may be too few white cells to form pus, and fever may be a late sign, so infection can be present without them. Monitor closely.")

q("antimet", "A nurse reviews the antimetabolites. Which drug is paired with the correct analog type?",
  ["Mercaptopurine — folic acid analog || mercaptopurine is a purine analog",
   "*Cytarabine — pyrimidine analog",
   "Methotrexate — purine analog || methotrexate is a folic acid analog",
   "Cyclophosphamide — pyrimidine analog || cyclophosphamide is an alkylating agent"],
  "Antimetabolites look like normal folate, purines or pyrimidines and act in S phase: methotrexate = folic acid analog, mercaptopurine = purine analog, cytarabine = pyrimidine analog.")

q("alkyl", "A client receiving cyclophosphamide has electrolyte results drawn. Which pattern matches the listed effects of this drug?",
  ["Low potassium and high sodium || the listed effects are the reverse",
   "Low potassium and low sodium || potassium is elevated, not low",
   "High potassium and high sodium || sodium is low, not high",
   "*High potassium and low sodium"],
  "Listed cyclophosphamide effects include hyperkalemia and hyponatremia, along with alopecia, severe nausea and vomiting, leukopenia and hemorrhagic cystitis.")

q("alkyl", "A 63-year-old client reports a new fever 5 weeks after an IV (intravenous) carmustine treatment. What does the nurse recognize?",
  ["Counts have recovered by now, so it is unrelated || carmustine has a delayed nadir",
   "*This falls in carmustine's delayed nadir and must be reported",
   "This is an early sign of hemorrhagic cystitis || that is a cyclophosphamide effect",
   "This is an expected effect of the drug's breakdown || fever signals infection risk"],
  "Carmustine (nitrosourea) has a delayed nadir: the critical time for low counts is 4–6 weeks after each treatment.")

q("vesicant", "A nurse is monitoring a peripheral IV (intravenous) during a vesicant infusion. Which findings suggest possible extravasation? " + SATA,
  ["*Pain at the IV site",
   "Red-colored urine || this is a harmless doxorubicin effect",
   "*Swelling at the IV site",
   "Ringing in the ears || this suggests cisplatin ototoxicity",
   "*Redness at the IV site"],
  "Assess the IV site often for pain, swelling or redness. Vesicant leakage outside the vein can cause blistering, severe tissue damage and necrosis.")

q("vesicant", "A nurse has just stopped a vesicant infusion because of suspected extravasation. What should the nurse do next?",
  ["Apply heat, since all vesicants are treated alike || treatment is drug-specific",
   "Restart the infusion at a slower rate || the infusion stays stopped",
   "*Notify the provider and follow the drug-specific protocol",
   "Flush the line forcefully to clear the drug || this pushes more drug into tissue"],
  "After stopping the infusion, notify the provider and follow the drug-specific extravasation protocol; not every agent uses the same antidote or temperature treatment.")

q("cis", "During a cisplatin infusion, a client develops signs of anaphylaxis. Which medication should the nurse have ready?",
  ["Mesna || mesna protects the bladder with cyclophosphamide",
   "*Epinephrine",
   "Leucovorin || leucovorin is the methotrexate antidote",
   "Dexrazoxane || dexrazoxane protects the heart with doxorubicin"],
  "Epinephrine should be ready for anaphylaxis to platinum compounds. Also avoid equipment containing aluminum when preparing them.")

q("cis", "A 35-year-old client with testicular cancer is receiving cisplatin. Which findings should the nurse report as possible adverse effects? " + SATA,
  ["*A rising serum creatinine",
   "*New ringing in the ears",
   "Red-orange urine for 2 days || this is a doxorubicin effect",
   "*Numbness and tingling in the feet",
   "*Weight gain from fluid retention"],
  "Cisplatin is nephrotoxic and ototoxic and causes fluid retention, peripheral neuropathy and severe nausea and vomiting.")

q("doxo", "A nurse reviews a client's history before giving doxorubicin. Which finding should make the nurse question the order?",
  ["Normal blood counts on today's CBC (complete blood count) || existing marrow suppression is the contraindication",
   "Hair loss from a different chemo drug || hair loss is expected and reversible",
   "*A full course of doxorubicin completed in the past",
   "No prior exposure to doxorubicin || a prior full course is the contraindication"],
  "Doxorubicin is contraindicated in existing cardiac disorders, existing marrow suppression and after a prior full course of doxorubicin.")

q("doxo", "A 47-year-old client is starting doxorubicin. Which client statement needs correction?",
  ["'Red urine for a day or two can be expected.' || correct: red urine can occur for up to 2 days",
   "*'Hair loss from this drug will be permanent.'",
   "'I'll report chest pain even months after I finish.' || correct: heart damage can be delayed",
   "'The nurse will check my IV site closely.' || correct: doxorubicin is a vesicant"],
  "Doxorubicin causes complete but reversible hair loss. It is cardiotoxic (damage can show up months or years later), a vesicant, and can cause red urine.")

q("antimit", "During a paclitaxel infusion, the cardiac monitor shows a heart rate of 44/min. How should the nurse interpret this?",
  ["An expected premedication effect; no action needed || bradycardia needs prompt attention",
   "A sign of the hormone flare seen with this drug || flare is a leuprolide effect",
   "An early sign of ototoxicity from the infusion || ototoxicity is a cisplatin effect",
   "*Severe bradycardia, a known risk of paclitaxel infusion"],
  "Paclitaxel (taxane) can cause severe bradycardia during infusion, so cardiac monitoring of heart rate and rhythm is the priority.")

q("antimit", "A nurse compares the antimitotics. Which drug and adverse effect pairing is correct?",
  ["*Vincristine — severe constipation",
   "Paclitaxel — hemorrhagic cystitis || that is a cyclophosphamide effect",
   "Vincristine — ototoxicity || that is a cisplatin effect",
   "Paclitaxel — red urine || that is a doxorubicin effect"],
  "Vincristine (vinca alkaloid) causes peripheral neuropathy and severe constipation. Paclitaxel can cause bradycardia, hypersensitivity reactions and marrow suppression.")

q("topo", "A client is receiving topotecan. Which client statement shows correct understanding of filgrastim timing?",
  ["'I'll get it right before topotecan starts.' || it is given after the infusion",
   "'I'll get it at the same time as topotecan.' || it is given 24 hours after",
   "*'I'll get it 24 hours after topotecan ends.'",
   "'I won't need it with this drug.' || topotecan causes severe marrow suppression"],
  "Topotecan (topoisomerase inhibitor) causes severe bone marrow suppression. Filgrastim is given 24 hours after the topotecan infusion is complete.")

q("horm", "A 52-year-old client is taking tamoxifen for breast cancer. Which follow-up should the nurse reinforce?",
  ["Monthly hearing tests || hearing loss is a cisplatin effect",
   "*Regular eye exams",
   "Daily urine checks for blood || hemorrhagic cystitis is a cyclophosphamide effect",
   "Monthly liver tests at first || that is the flutamide schedule"],
  "Tamoxifen raises the risk of retinopathy and cataracts, so regular eye exams are needed. It also raises the risk of clots and uterine cancer.")

q("horm", "A 68-year-old client with prostate cancer is on leuprolide and flutamide. Which nursing actions apply? " + SATA,
  ["*Monitor liver function tests",
   "Monitor urine for hemorrhagic cystitis || that is a cyclophosphamide effect",
   "*Monitor bone density",
   "Teach that symptoms never worsen at first || leuprolide causes an initial flare",
   "*Teach daily weight-bearing exercise"],
  "Flutamide blocks androgens and can cause liver toxicity (monitor LFTs). Leuprolide causes an initial flare, then suppression, with bone loss; monitor bone density and teach weight-bearing exercise.")

q("target", "The family of a client on interferon alfa reports the client seems withdrawn and sad. How should the nurse interpret this?",
  ["An expected flu-like symptom that needs no report || mood changes should be reported",
   "*A possible mood change or depression from the drug",
   "A sign of hemorrhagic cystitis || that is a cyclophosphamide effect",
   "Sudden weight gain from fluid retention || that is an imatinib effect"],
  "Interferon alfa (biologic response modifier) can cause flu-like symptoms, mood changes, marrow suppression and liver dysfunction. Watch for depression.")

q("hivgoal", "A nurse explains the HIV (human immunodeficiency virus) life cycle. Which drug class blocks the step right after reverse transcription?",
  ["Entry/fusion inhibitors || entry is the first step",
   "Protease inhibitors || protease maturation is the last step",
   "*Integrase inhibitors",
   "Reverse transcriptase inhibitors || they block reverse transcription itself"],
  "Life cycle order: entry → reverse transcription → integration → protease maturation. Drug classes: entry/fusion inhibitors, RTIs, integrase inhibitors, protease inhibitors.")

q("hivgoal", "A 22-year-old college student asks what taking HIV (human immunodeficiency virus) medicines exactly as prescribed will do. Which outcomes should the nurse describe? " + SATA,
  ["*A lower viral load",
   "*A higher CD4 (cluster of differentiation 4) count",
   "A cure of HIV within a few weeks || therapy controls the virus",
   "*Less drug resistance",
   "Freedom to skip weekend doses || missed doses lead to resistance"],
  "Adherence lowers viral load (ideally undetectable), raises CD4 and reduces resistance. Missed doses let the virus mutate and become drug-resistant.")

q("entry", "A client taking maraviroc calls the clinic. Which report needs prompt follow-up?",
  ["*Abdominal pain and yellowing of the skin",
   "Redness at a subcutaneous injection site || injection-site reactions are an enfuvirtide effect",
   "A question about rotating injection sites || that is enfuvirtide teaching",
   "A question about the CCR5 test result || it was confirmed before starting"],
  "Maraviroc blocks CCR5 co-receptors and can cause liver injury. Allergic signs like rash often come before liver damage; report abdominal pain and jaundice.")

q("rti", "A client who started zidovudine 3 weeks ago reports fatigue, and the hemoglobin is low. What does the nurse recognize?",
  ["Anemia is unlikely this soon after starting || anemia appears in 2–4 weeks",
   "This is muscle injury needing a CK (creatine kinase) || that is a raltegravir effect",
   "*Anemia often appears in 2–4 weeks on zidovudine",
   "This is liver toxicity from an NNRTI || zidovudine is an NRTI causing marrow suppression"],
  "Zidovudine (NRTI) causes bone marrow suppression: anemia in 2–4 weeks and neutropenia after about 6 weeks. Epoetin alfa or filgrastim may be given.")

q("rti", "A nursing student compares the two types of reverse transcriptase inhibitors. Which statement is correct?",
  ["Both block viral entry into the CD4 (cluster of differentiation 4) cell || that is entry inhibitors",
   "Delavirdine is a nucleoside RTI || delavirdine is a non-nucleoside RTI",
   "*Zidovudine is a nucleoside RTI; delavirdine is a non-nucleoside RTI",
   "Zidovudine's signature effect is rash || its signature effect is marrow suppression"],
  "RTIs block conversion of viral RNA into DNA. Zidovudine is a nucleoside RTI (marrow suppression); delavirdine is a non-nucleoside RTI (rash, liver toxicity).")

q("pi", "A client takes both raltegravir and ritonavir. Which statement correctly describes how each drug works?",
  ["*Raltegravir blocks viral DNA insertion; ritonavir blocks protease maturation",
   "Raltegravir blocks entry; ritonavir blocks reverse transcription || these are other classes",
   "Raltegravir blocks protease; ritonavir blocks integrase || the roles are reversed",
   "Both drugs block conversion of viral RNA into DNA || that is reverse transcriptase inhibitors"],
  "Raltegravir (integrase inhibitor) keeps viral DNA from being inserted into host DNA. Ritonavir (protease inhibitor) blocks protease so new virus can't mature.")

q("pi", "A 29-year-old client is starting ritonavir. Which drug-interaction teaching points are accurate? " + SATA,
  ["*Oral contraceptive levels may be lowered",
   "*Sildenafil, if used, needs a reduced dose",
   "Ritonavir has very few drug interactions || it has many interactions",
   "*Midazolam is contraindicated with this drug",
   "Supplements don't need to be reviewed || supplements like St. John's wort interact"],
  "Ritonavir has many interactions: it lowers oral contraceptive levels, PDE-5 inhibitors like sildenafil need reduced doses, and statins, midazolam, alprazolam and St. John's wort are contraindicated.")
