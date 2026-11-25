T = "e5imm"; SET = "20261125"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("cycle", "A nurse teaches a 53-year-old client about the cell cycle before chemotherapy begins. Which sequence of phases is correct?",
  ["S → G1 → M → G2 || G1 comes first, and M (division) is last",
   "G1 → G2 → S → M || DNA is made in S before G2",
   "*G1 → S → G2 → M",
   "M → S → G1 → G2 || the cell prepares in G1 before making DNA"],
  "G1 prepares → S makes DNA → G2 prepares for mitosis → M divides. G0 is the resting phase.")

q("types", "A 16-year-old client says, 'The doctor said my cancer started in my thigh bone.' Which type of cancer does the nurse recognize?",
  ["Carcinoma || carcinoma starts in epithelial tissue",
   "*Sarcoma",
   "Lymphoma || lymphoma starts in lymph tissue",
   "Leukemia || leukemia starts in blood-forming tissue"],
  "Cancer is classified by the tissue where it starts: sarcoma = bone/soft tissue, carcinoma = epithelial, lymphoma = lymph, leukemia = blood-forming tissue.")

q("why", "A nurse explains a 57-year-old client's chemotherapy plan. Which statements about how chemo is given are accurate? " + SATA,
  ["*Several drugs are combined because each hits a different cell-cycle phase",
   "Breaks between cycles let the tumor regrow so drugs work better || cycles aren't meant to let the tumor grow",
   "*Cycles keep the drug available as cells regrow and enter vulnerable phases",
   "Combining drugs lets each one target only resting G0 cells || chemo acts on S, G2 and M phases",
   "Giving chemo in cycles prevents every side effect || cycles don't prevent all adverse effects"],
  "Drugs are combined to impact multiple cell-cycle phases, and given in cycles so the drug is available as cells grow back and enter susceptible phases.")

q("tox", "A nurse prepares general chemotherapy teaching for a 44-year-old client. Which adverse effects should be included? " + SATA,
  ["*Numbness or tingling from neuropathy",
   "*Difficulty with thinking or memory",
   "Weight gain from a bigger appetite || nausea and vomiting are expected, not increased appetite",
   "*Possible harm to a fetus during treatment",
   "Thicker, faster hair growth || chemo causes alopecia"],
  "Chemo destroys rapidly dividing normal cells like cancer cells; adverse effects include N/V, alopecia, stomatitis, teratogenic effects, neuropathy, organ damage and cognitive difficulty.")

q("nadir", "A 59-year-old client is entering the nadir after chemotherapy. Which client statement shows correct understanding of infection precautions?",
  ["'I'll check my temperature rectally every morning.' || rectal temperatures are avoided",
   "'I can still babysit my grandson while he has the flu.' || avoid people who are ill",
   "*'I'll wash fresh fruits and vegetables well and cook foods properly.'",
   "'If I have no pus, I can't have an infection.' || leukopenia may prevent pus from forming"],
  "During the nadir (about day 10–14), follow neutropenic precautions: scrupulous handwashing, avoid ill people, wash produce, cook foods properly and report fever or sore throat.")

q("nadir", "A client with chemotherapy-induced thrombocytopenia is on day 13 after treatment. Which finding should the nurse report?",
  ["Hair coming out in the hairbrush || expected alopecia, not a bleeding sign",
   "Asking to use an electric razor || an appropriate bleeding precaution",
   "Choosing a soft toothbrush for mouth care || an appropriate bleeding precaution",
   "*Black, tarry stools since this morning"],
  "At the nadir, bleeding risk is greatest. Watch for bleeding from the gums and GI tract (melena).")

q("antimet", "A nurse plans care for a client starting mercaptopurine. Which actions are appropriate? " + SATA,
  ["*Monitor bilirubin and transaminase levels",
   "Give it by IV push for faster effect || mercaptopurine is oral only",
   "*Ask whether the client takes allopurinol",
   "Give mesna with each dose || mesna is for cyclophosphamide",
   "*Give it by mouth as prescribed"],
  "Mercaptopurine (purine analog) is oral only with weight-based dosing; watch bilirubin and transaminases. Allopurinol can cause mercaptopurine toxicity, so the dose is reduced.")

q("alkyl", "A nurse calls four clients receiving cyclophosphamide. Which report needs the nurse's follow-up first?",
  ["'My hair has started to thin out.' || expected alopecia; it grows back",
   "*'It burns when I urinate, and my urine looks pink.'",
   "'I've been drinking extra fluids every day.' || appropriate bladder protection",
   "'I emptied my bladder before the dose.' || appropriate bladder protection"],
  "Cyclophosphamide can cause hemorrhagic cystitis. Teach to report blood in the urine or pain with voiding; void before the dose, increase fluids and give mesna.")

q("alkyl", "A nursing student compares cyclophosphamide and carmustine. Which statement is accurate?",
  ["Cyclophosphamide is a nitrosourea that crosses the blood-brain barrier || that describes carmustine",
   "Both drugs act mainly by stopping the mitotic spindle || alkylating agents break DNA bonds",
   "*Carmustine has a nadir at 4–6 weeks; cyclophosphamide can cause hemorrhagic cystitis",
   "Carmustine requires mesna with every dose to protect the bladder || mesna is given with cyclophosphamide"],
  "Alkylating agents break DNA bonds and cause abnormal pairing. Cyclophosphamide → hemorrhagic cystitis; carmustine (nitrosourea) crosses the BBB with a delayed 4–6 week nadir.")

q("vesicant", "A nursing student reviews vesicant safety. Which student statement needs correction?",
  ["'Vesicant leakage can cause tissue necrosis.' || accurate statement",
   "'A central line is used for vesicants when possible.' || accurate statement",
   "*'Every vesicant is treated with the same antidote and cold pack.'",
   "'Vincristine extravasation is treated with heat and hyaluronidase.' || accurate statement"],
  "Extravasation treatment is drug-specific: carmustine uses bicarbonate and cold; vincristine uses heat and hyaluronidase.")

q("vesicant", "The nurse explains to a 62-year-old client that the chemo drug is a vesicant. Which client statement shows understanding?",
  ["'It's the drug that protects my bladder during treatment.' || that describes mesna",
   "'It's a drug given to keep me from getting nauseated.' || that describes an antiemetic",
   "'It's only harmful if it is given through a central line.' || a central line lowers the risk",
   "*'If it leaks out of the vein it can blister the skin, so I'll report burning.'"],
  "A vesicant causes blistering and severe tissue damage if it leaks outside the vein. Assess the IV site often for pain, swelling or redness.")

q("cis", "A nurse is preparing a cisplatin infusion. Which step should the nurse question?",
  ["Weighing the client before the infusion || appropriate; cisplatin causes fluid retention",
   "*Drawing up the dose with an aluminum-hub needle",
   "Giving an antiemetic 30 minutes before the infusion || appropriate premedication",
   "Checking the client's hearing at baseline || appropriate; cisplatin is ototoxic"],
  "Don't use equipment containing aluminum with platinum compounds. Before cisplatin, infuse IV fluids, give an antiemetic, check hearing and weigh the client.")

q("cis", "A client is going home after a cisplatin treatment and asks how long to keep taking the antiemetic. Which response is best?",
  ["'Stop it as soon as the infusion is finished.' || antiemetics continue after treatment",
   "*'Keep taking it for several days after treatment.'",
   "'Take it only if you vomit more than twice.' || it's used to prevent nausea, not after",
   "'Nausea never happens after the day of the infusion.' || antiemetics are needed for days"],
  "Cisplatin causes severe nausea and vomiting starting about 1 hour into the infusion. Premedicate 30 minutes before and take antiemetics for several days after treatment.")

q("doxo", "A client received doxorubicin yesterday. Which client report should the nurse act on right away?",
  ["'My urine looks red this morning.' || red urine for up to 2 days is expected",
   "'My tears have a reddish tint.' || temporary red tears can occur",
   "*'I feel short of breath and have chest pain.'",
   "'My hair is coming out in clumps.' || hair loss is expected and reversible"],
  "Doxorubicin (anthracycline) is cardiotoxic; report palpitations, shortness of breath or chest pain. Red urine or tears and reversible hair loss are expected.")

q("doxo", "A nurse plans monitoring for a 54-year-old client receiving doxorubicin. Which should be included? " + SATA,
  ["*Cardiac function",
   "*The IV site for extravasation",
   "Hearing before each dose || that's for cisplatin",
   "*CBC and liver function",
   "Urine for hemorrhagic cystitis || that's for cyclophosphamide"],
  "Doxorubicin is cardiotoxic (priority) and a vesicant. Assess the IV site and monitor the CBC and liver function.")

q("antimit", "A client receiving vincristine has a weak Achilles reflex and reduced grip strength. What does the nurse anticipate?",
  ["Injecting hyaluronidase at the IV site || that treats vincristine extravasation",
   "Increasing the dose to speed treatment || the dose may be decreased instead",
   "*The provider may decrease the dose for neuropathy",
   "No action, since this is expected and harmless || neuropathy must be reported"],
  "Vincristine causes peripheral neuropathy; check deep tendon reflexes (Achilles) and hand/foot strength. The dose may be decreased if neuropathy develops.")

q("antimit", "A nurse is caring for a client during a paclitaxel infusion. Which actions are appropriate? " + SATA,
  ["*Monitor heart rate and rhythm",
   "Give the full dose over 10 minutes || it's infused over 3 hours",
   "*Watch for a hypersensitivity reaction",
   "*Use an in-line filter on the tubing",
   "Give mesna with the infusion || mesna is for cyclophosphamide"],
  "Paclitaxel (taxane) can cause severe bradycardia, hypersensitivity reactions and marrow suppression. Solvent form is infused over 3 hours with an in-line filter.")

q("topo", "A client is receiving topotecan. Which lab findings should the nurse watch most closely? " + SATA,
  ["*A falling neutrophil count",
   "A rising creatine kinase || that's linked to raltegravir",
   "*A falling platelet count",
   "Red blood cells in the urine || that's linked to cyclophosphamide",
   "A rising INR || that's linked to flutamide with warfarin"],
  "Topotecan (topoisomerase inhibitor) causes severe bone marrow suppression; watch for neutropenia and thrombocytopenia.")

q("horm", "A 56-year-old client taking tamoxifen reports abnormal vaginal bleeding. How should the nurse interpret this?",
  ["*It may signal uterine cancer, a known tamoxifen risk, and must be reported",
   "It is an expected hot flash effect that needs no follow-up || abnormal bleeding is reported",
   "It is a sign of liver toxicity from the drug || liver toxicity is linked to flutamide",
   "It shows that estrogen levels are rising too high || tamoxifen blocks estrogen in cancer cells"],
  "Tamoxifen blocks estrogen in breast cancer cells and raises the risk of uterine cancer, clots and retinopathy; report abnormal vaginal bleeding.")

q("horm", "A client with prostate cancer takes warfarin and is starting flutamide. Which lab should the nurse watch for a change?",
  ["Serum creatine kinase || that's linked to raltegravir",
   "Serum potassium || not a listed flutamide interaction",
   "Hearing test results || that's for cisplatin",
   "*INR"],
  "Flutamide blocks androgens, can cause liver toxicity (monitor LFTs monthly at first) and may raise INR with warfarin.")

q("target", "A nurse is giving a client the first dose of trastuzumab. When is an allergic reaction most likely?",
  ["Only after several months of therapy || reactions usually occur early",
   "*With the first dose or within 12 hours",
   "Only after the drug is stopped || reactions occur with dosing",
   "Only if given with doxorubicin || that's a cardiotoxicity concern"],
  "Allergic reactions to trastuzumab usually occur with the first dose or within 12 hours. Also monitor cardiac function.")

q("hivgoal", "A client on combination antiretroviral therapy now has a rising viral load and a falling CD4 count. What should the nurse explore first?",
  ["Whether the client needs fewer drugs in the regimen || 2 or more drugs reduce resistance",
   "Whether the client is ready to stop therapy || HIV therapy isn't stopped when labs worsen",
   "*Whether the client has been missing doses",
   "Whether the labs show the therapy is working || these results show it isn't working"],
  "Missed doses let the virus mutate and become drug-resistant. Adherence leads to lower viral load, higher CD4 and less resistance.")

q("hivgoal", "A nurse reviews where each HIV drug class acts. Which class blocks the LAST step of the viral life cycle?",
  ["Entry/fusion inhibitors || they block the first step",
   "Reverse transcriptase inhibitors || they block the second step",
   "Integrase inhibitors || they block the third step",
   "*Protease inhibitors"],
  "Life cycle order: entry → reverse transcription → integration → protease maturation.")

q("entry", "A client is learning to self-inject enfuvirtide. Which client statement needs more teaching?",
  ["'I'll inject it twice a day.' || correct dosing frequency",
   "'I'll stay away from scarred or discolored skin.' || correct site choice",
   "*'I'll use the same spot on my thigh every time.'",
   "'I'll report a cough, fever or shortness of breath.' || correct; it can cause pneumonia"],
  "Enfuvirtide is a subcutaneous entry/fusion inhibitor given twice a day. Rotate sites (thigh, upper arm, abdomen), avoid scarred skin and report signs of pneumonia.")

q("rti", "A client has taken zidovudine for 7 weeks and now has a low neutrophil count. Which medication may be ordered?",
  ["*Filgrastim",
   "Leucovorin || that's the methotrexate antidote",
   "Mesna || that protects the bladder with cyclophosphamide",
   "Dexrazoxane || that protects the heart with doxorubicin"],
  "Zidovudine (NRTI) causes bone marrow suppression: anemia in 2–4 weeks, neutropenia after about 6 weeks. Epoetin alfa or filgrastim may be given.")

q("rti", "One client takes zidovudine and another takes delavirdine. Which monitoring plan matches each drug?",
  ["Zidovudine: skin for rash; delavirdine: CBC for anemia || the plans are reversed",
   "*Zidovudine: CBC for anemia; delavirdine: skin for rash and liver function",
   "Both drugs: creatine kinase for muscle injury || CK is for raltegravir",
   "Zidovudine: injection sites; delavirdine: hearing tests || neither applies"],
  "Zidovudine (nucleoside RTI) causes marrow suppression; delavirdine (non-nucleoside RTI) causes rash and liver toxicity.")

q("pi", "A client asks why ritonavir was added to another antiretroviral in the regimen. Which response is accurate?",
  ["'It cures HIV when combined with one other drug.' || HIV therapy doesn't cure HIV",
   "'It has no interactions, so it's a safe add-on.' || ritonavir has many interactions",
   "'It blocks reverse transcriptase like zidovudine does.' || ritonavir is a protease inhibitor",
   "*'It boosts the levels of other antiretrovirals.'"],
  "Ritonavir (protease inhibitor) boosts other antiretrovirals and has many drug interactions.")

q("pi", "A nurse teaches a client who is starting raltegravir. Which teaching points are accurate? " + SATA,
  ["*Take every dose consistently as prescribed",
   "Expect red urine for 2 days after each dose || that's doxorubicin",
   "*Report new muscle pain or weakness",
   "*Avoid driving until you know how the drug affects you",
   "Skip a dose on days you feel dizzy || reinforce consistent dosing"],
  "Raltegravir (integrase inhibitor) can cause muscle injury (high CK), dizziness and headache; avoid driving until effects are known and reinforce consistent dosing.")
