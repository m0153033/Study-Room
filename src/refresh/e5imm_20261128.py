T = "e5imm"; SET = "20261128"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("cycle", "A nurse reviews which cell-cycle phase each drug class acts on. Which class works mainly during G2 and M?", [
  "Antimetabolites || They act during S phase",
  "*Antimitotics",
  "Alkylating agents || They act mostly in S and G1",
  "Hormonal agents || They block hormone receptors, not mitosis"],
  "Antimitotics disrupt mitosis during G2 and M. Antimetabolites act in S phase, alkylating agents mostly in S and G1, and platinum compounds arrest cells at G2/M.")

q("types", "A nursing student says, 'Leukemia and lymphoma both start in blood-forming tissue.' Which correction is accurate?", [
  "'Both of them start in epithelial tissue.' || Epithelial cancer is carcinoma",
  "*'Lymphoma starts in lymph tissue, not blood-forming tissue.'",
  "'Both of them start in bone and soft tissue.' || Bone or soft tissue cancer is sarcoma",
  "'Leukemia starts in lymph tissue, not blood tissue.' || Leukemia starts in blood-forming tissue"],
  "Cancer is classified by the tissue where it starts: carcinoma = epithelial, sarcoma = bone or soft tissue, lymphoma = lymph tissue, leukemia = blood-forming tissue.")

q("why", "A 50-year-old electrician asks why three chemotherapy drugs are used instead of one strong drug. Which response is best?", [
  "'Using three drugs keeps them from harming normal cells.' || Normal cells are still harmed",
  "'One drug always fails, so the others are backups.' || That is not the reason",
  "*'Each drug acts on a different phase of the cell cycle.'",
  "'Three drugs together let us skip the rest weeks.' || Chemo is still given in cycles"],
  "Chemotherapy drugs are combined because different drugs hit different phases of the cell cycle, so several types and routes together impact multiple phases.")

q("tox", "A client on chemotherapy has mouth sores, thinning hair and low blood counts. Which single explanation links all three findings?", [
  "The cancer has spread to the mouth, scalp and marrow || These are drug effects, not spread",
  "*Chemotherapy harms fast-dividing normal cells too",
  "An allergic reaction to one drug in the regimen || These findings are not allergic",
  "A bacterial infection that started in the tumor || Infection does not explain these"],
  "Chemo destroys rapidly dividing normal cells, such as the GI lining, hair follicles and bone marrow, the same way it destroys cancer cells, causing stomatitis, alopecia and marrow suppression.")

q("nadir", "An oncology nurse returns four phone messages. Which client should the nurse call back first?", [
  "Day 2 after chemo, asking when hair loss begins || Hair loss is not urgent",
  "*Day 12 after chemo, reporting chills and a sore throat",
  "Day 3 after chemo, asking about a soft toothbrush || This is a routine question",
  "Day 25 after chemo, asking about the next cycle || This is a routine question"],
  "The nadir, about day 10–14, is when blood counts are lowest and infection risk is greatest. Fever, sore throat or unusual fatigue must be reported.")

q("nadir", "A 58-year-old client on day 11 after chemotherapy reports feeling exhausted all day. Which part of marrow suppression explains this?", [
  "Low platelets || Low platelets cause bleeding",
  "Low white blood cells || Low white cells cause infection risk",
  "*Anemia",
  "Rising neutrophil counts || Counts are at their lowest now"],
  "Chemo-induced bone marrow suppression brings infection from low white blood cells, bleeding from low platelets and fatigue from anemia. Monitor the CBC.")

q("antimet", "A 41-year-old client is starting methotrexate. Which client statement needs correction?", [
  "'I'll report any yellowing of my skin or eyes.' || Correct; liver damage can occur",
  "*'A glass of wine with dinner should be fine.'",
  "'I'll use contraception during and after therapy.' || Correct teaching for this drug",
  "'I'll call the clinic if I get short of breath.' || Correct; pulmonary fibrosis can occur"],
  "Methotrexate, a folic acid analog, can cause liver damage and pulmonary fibrosis. Teach to avoid alcohol, use contraception, and report jaundice or shortness of breath.")

q("alkyl", "A client starting cyclophosphamide asks when the mesna will be given. Which response is accurate?", [
  "'Only if blood shows up in your urine.' || It is given with every dose",
  "*'It is given with each dose of your chemotherapy.'",
  "'Only after your final treatment cycle ends.' || It is given with every dose",
  "'Only if your hair begins to fall out.' || Mesna protects the bladder"],
  "Mesna is the chemo-protectant given with each cyclophosphamide dose to help prevent hemorrhagic cystitis, along with voiding before the dose and increased fluid intake.")

q("alkyl", "A nursing student asks what makes carmustine different from cyclophosphamide. Which answer is accurate?", [
  "Carmustine's signature effect is hemorrhagic cystitis || That is cyclophosphamide",
  "Carmustine works by stopping the mitotic spindle || That is an antimitotic",
  "*Carmustine crosses the blood-brain barrier",
  "Carmustine is a folic acid analog drug || That describes methotrexate"],
  "Carmustine, a nitrosourea alkylating agent, crosses the blood-brain barrier, has a delayed 4–6 week nadir, can cause irreversible pulmonary fibrosis and can be a vesicant IV.")

q("vesicant", "A vincristine infusion has infiltrated and the nurse has stopped it. Which actions does the nurse anticipate? " + SATA, [
  "*Notify the provider right away",
  "*Apply a warm compress as ordered",
  "*Give a local hyaluronidase injection as ordered",
  "Apply cold packs and sodium bicarbonate || That is the carmustine protocol",
  "Restart the infusion at a slower rate || The infusion must stay stopped"],
  "After stopping the infusion, notify the provider and follow the drug-specific protocol: vincristine uses heat and hyaluronidase, while carmustine uses cold and bicarbonate.")

q("vesicant", "A 67-year-old client is receiving carmustine through a peripheral IV. Which client statement needs correction?", [
  "'I'll tell you right away if the site burns.' || Correct; burning must be reported",
  "'Swelling near my IV could mean a leak.' || Correct; swelling suggests extravasation",
  "*'If the IV site hurts, I'll wait until the bag finishes.'",
  "'Drug leaking out can damage my skin.' || Correct; vesicants cause blistering"],
  "Carmustine can be a vesicant. Pain, swelling or redness at the IV site suggests extravasation, which can cause blistering and necrosis, so the infusion is stopped immediately.")

q("cis", "A nursing student describes cisplatin to the nurse. Which statement is accurate?", [
  "'It is an antimetabolite that works in S phase.' || That describes antimetabolites",
  "'It is a vinca alkaloid that stops the spindle.' || That describes vincristine",
  "*'It is a platinum compound that arrests cells at G2/M.'",
  "'It is an aromatase inhibitor that lowers estrogen.' || That describes anastrozole"],
  "Cisplatin is a platinum (heavy metal) compound that causes cell-cycle arrest during G2/M. It causes severe nausea and vomiting, ototoxicity, nephrotoxicity, fluid retention and peripheral neuropathy.")

q("cis", "A nurse reviews data before a client's next cisplatin dose. Which finding should be reported to the provider?", [
  "Weight unchanged since the last clinic visit || This shows no fluid retention",
  "Hearing unchanged from the baseline test || This shows no ototoxicity",
  "*BUN and creatinine higher than before the last dose",
  "An antiemetic was given 30 minutes ago || This is correct premedication"],
  "Cisplatin is nephrotoxic, so BUN and creatinine are the most important labs to check. Also monitor hearing, weight and fluid balance.")

q("doxo", "A client receiving doxorubicin has trastuzumab ordered for the same infusion visit. Why does the nurse question this?", [
  "Both drugs can cause hemorrhagic cystitis || Neither is linked to cystitis",
  "*The two drugs together add to heart damage",
  "Both drugs can cause severe hearing loss || Ototoxicity is a cisplatin effect",
  "The two drugs together turn the urine red || Red urine comes from doxorubicin alone"],
  "Doxorubicin, an anthracycline, is cardiotoxic, and trastuzumab should not be given at the same time as an anthracycline because of combined cardiotoxicity.")

q("doxo", "A 61-year-old client finished doxorubicin 2 years ago and asks whether the heart can still be affected. Which response is best?", [
  "'No, heart effects stop when the infusions end.' || Damage can appear years later",
  "'Only if your urine turns red again.' || Red urine is temporary and expected",
  "'Only if your hair does not grow back in.' || Hair regrowth is unrelated",
  "*'Yes, so report palpitations or shortness of breath.'"],
  "Doxorubicin is cardiotoxic, and heart damage can show up months or years later. Teach the client to report palpitations, shortness of breath or chest pain.")

q("antimit", "A nurse prepares several chemotherapy drugs. Which drug requires an antihistamine, a corticosteroid and an H2 blocker 30 minutes beforehand?", [
  "Vincristine || This premedication is not listed for it",
  "Cyclophosphamide || Mesna is given with this drug",
  "*Paclitaxel in its solvent form",
  "Cisplatin || An antiemetic is given before this drug"],
  "Solvent paclitaxel is given after premedication with an antihistamine, a corticosteroid and an H2 blocker 30 minutes before to prevent allergic reactions, then infused over 3 hours with an in-line filter.")

q("antimit", "A 70-year-old client is receiving vincristine. Which findings should the nurse report? " + SATA, [
  "*Numbness and tingling in both feet",
  "*No bowel movement for 4 days",
  "*Absent bowel sounds on assessment",
  "Red-colored urine after the dose || Red urine is linked to doxorubicin",
  "New ringing in both ears || Ringing in the ears is linked to cisplatin"],
  "Vincristine, a vinca alkaloid, causes peripheral neuropathy and severe constipation that can lead to ileus or obstruction, so monitor bowel sounds and bowel function.")

q("topo", "A client received topotecan 12 days ago and now has a fever. How does the nurse interpret this timing?", [
  "A hormone flare before suppression begins || Flare belongs to leuprolide",
  "*It fits topotecan's neutropenia nadir",
  "A delayed nadir seen at 4–6 weeks || The delayed nadir belongs to carmustine",
  "An expected flu-like drug reaction || Flu-like symptoms belong to interferon alfa"],
  "Topotecan, a topoisomerase inhibitor, causes severe bone marrow suppression, and its neutropenia nadir is about day 12.")

q("horm", "A 66-year-old postmenopausal client starting anastrozole asks what the drug does. Which response is accurate?", [
  "'It blocks estrogen inside the breast cancer cells.' || That describes tamoxifen",
  "*'It lowers how much estrogen your body produces.'",
  "'It blocks the effects of androgens in your body.' || That describes flutamide",
  "'It causes a brief flare before hormones drop.' || That describes leuprolide"],
  "Anastrozole is an aromatase inhibitor that lowers estrogen production in postmenopausal hormone-sensitive breast cancer. Monitor bone health, since osteoporosis is a risk.")

q("horm", "A nurse teaches four clients on hormonal agents. Which client statement needs correction?", [
  "Tamoxifen: 'I'll report calf pain or swelling.' || Correct; clot risk is raised",
  "Anastrozole: 'I'll do weight-bearing exercise.' || Correct; bone loss is a risk",
  "*Flutamide: 'My liver tests are only needed after 5 years.'",
  "Leuprolide: 'I'll get enough calcium and vitamin D.' || Correct; bone loss is a risk"],
  "Flutamide blocks androgens and can cause liver toxicity, so liver function tests are monitored monthly for the first few months. Tamoxifen raises clot risk; anastrozole and leuprolide cause bone loss.")

q("target", "A client is receiving a first dose of trastuzumab and develops wheezing and hypotension. What should the nurse do first?", [
  "Speed the infusion to finish the dose || The infusion must be stopped",
  "*Stop the infusion and prepare epinephrine as prescribed",
  "Give the dose mixed in dextrose instead || Changing the fluid does not treat this",
  "Document it as an expected first-dose effect || This reaction needs action"],
  "Allergic reactions to trastuzumab usually occur with the first dose or within 12 hours. Stop the infusion and prepare epinephrine as prescribed; also monitor cardiac function.")

q("hivgoal", "A 30-year-old client on combination antiretroviral therapy says, 'I take my pills whenever I remember.' Which outcome should the nurse explain?", [
  "'Irregular dosing raises your CD4 count faster.' || Missed doses lower CD4 gains",
  "'Irregular dosing only changes your side effects.' || It also causes resistance",
  "*'Missed doses let the virus mutate and resist the drugs.'",
  "'Irregular dosing is fine once you feel well.' || Doses must be taken as prescribed"],
  "Antiretrovirals must be taken exactly as prescribed. Missed doses let the virus mutate and become drug-resistant; adherence lowers viral load, raises CD4 and reduces resistance.")

q("hivgoal", "A nurse reviews the HIV life cycle with a student. Which steps do antiretroviral classes block? " + SATA, [
  "*Entry of the virus into the CD4 cell",
  "*Reverse transcription of viral RNA",
  "*Integration of viral DNA into host DNA",
  "*Protease maturation of new virus",
  "Replacement of destroyed CD4 cells || No drug class replaces CD4 cells"],
  "Life cycle order: entry, reverse transcription, integration, protease maturation. The drug classes are entry/fusion inhibitors, reverse transcriptase inhibitors, integrase inhibitors and protease inhibitors.")

q("entry", "A client who has been self-injecting enfuvirtide for 2 months has firm, reddened areas at the usual site. Which teaching is most appropriate?", [
  "'Inject deeper into the muscle from now on.' || It is a subcutaneous injection",
  "'Use that same site so other skin is spared.' || Sites should be rotated",
  "*'Rotate among the thigh, upper arm and abdomen.'",
  "'Inject into scarred skin to slow absorption.' || Scarred skin is avoided"],
  "Enfuvirtide, an entry/fusion inhibitor, is injected subcutaneously twice a day and causes injection-site reactions. Rotate sites (thigh, upper arm, abdomen) and avoid discolored or scarred skin.")

q("rti", "A client has taken zidovudine for 7 weeks and has a neutrophil count that is now low. Which drug does the nurse expect to be ordered?", [
  "Epoetin alfa || That is given for the anemia from this drug",
  "*Filgrastim",
  "Mesna || Mesna protects the bladder with cyclophosphamide",
  "Dexrazoxane || Dexrazoxane protects the heart with doxorubicin"],
  "Zidovudine, a nucleoside reverse transcriptase inhibitor, causes marrow suppression: anemia in 2–4 weeks and neutropenia after about 6 weeks. Epoetin alfa or filgrastim may be given.")

q("rti", "A client taking delavirdine develops a rash with fever and mouth lesions. What is the nurse's priority action?", [
  "Apply lotion and continue the drug || This may be Stevens-Johnson syndrome",
  "Give an antacid with the next dose || Antacids are not taken with this drug",
  "*Report it, since the drug may need to be stopped",
  "Document it as an expected drug effect || A severe rash needs prompt evaluation"],
  "Delavirdine, a non-nucleoside reverse transcriptase inhibitor, can cause rash including Stevens-Johnson syndrome, and liver toxicity. A severe rash needs prompt evaluation.")

q("pi", "A 35-year-old client taking ritonavir uses oral contraceptives and asks if anything changes. Which response is accurate?", [
  "'Ritonavir raises your contraceptive levels.' || It lowers those levels",
  "*'Ritonavir can lower your contraceptive levels.'",
  "'Ritonavir has no effect on other medicines.' || It has many interactions",
  "'Your contraceptive dose should be doubled.' || Dose changes are not taught here"],
  "Ritonavir, a protease inhibitor, has many drug interactions and lowers oral contraceptive levels. Review all prescriptions, over-the-counter drugs and supplements with the provider.")

q("pi", "A client starting raltegravir reports new muscle aches and weakness. Which action is most appropriate?", [
  "Tell the client to double the next dose || Doses are not doubled",
  "Tell the client this needs no follow-up || Muscle injury must be reported",
  "*Report it and expect a creatine kinase level",
  "Tell the client to stop the drug today || Antiretrovirals are not stopped this way"],
  "Raltegravir, an integrase inhibitor, can cause muscle injury with a high creatine kinase level, so new muscle pain or weakness is reported and the CK is checked.")
