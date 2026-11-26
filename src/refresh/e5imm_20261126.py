T = "e5imm"; SET = "20261126"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("cycle", "A 47-year-old accountant starting chemotherapy asks what happens in the G2 phase. Which response is accurate?", [
  "'The cell makes a copy of its DNA.' || DNA is made in S phase",
  "*'The cell prepares for mitosis.'",
  "'The cell divides into two cells.' || Division happens in M phase",
  "'The cell rests and does its specialized job.' || That is G0"],
  "G1 prepares, S makes DNA, G2 prepares for mitosis and M divides. G0 cells rest and carry out their specialized function.")

q("types", "A 40-year-old firefighter is told his tumor began in the soft tissue of his upper arm. Which type of cancer does the nurse recognize?", [
  "Carcinoma || Carcinoma starts in epithelial tissue",
  "Lymphoma || Lymphoma starts in lymph tissue",
  "Leukemia || Leukemia starts in blood-forming tissue",
  "*Sarcoma"],
  "Cancer is classified by the tissue where it starts: sarcoma = bone/soft tissue, carcinoma = epithelial, lymphoma = lymph, leukemia = blood-forming tissue.")

q("why", "A nursing student explains chemotherapy scheduling to a 64-year-old client. Which student statement needs correction?", [
  "'Each cycle reaches cells as they enter vulnerable phases.' || This is accurate",
  "*'The breaks between cycles let the tumor grow so drugs work better.'",
  "'Several drugs together impact more than one phase.' || This is accurate",
  "'Different drug types and routes may be combined.' || This is accurate"],
  "Chemo is given in cycles so the drug is available as cells grow back and enter susceptible phases. Drugs are combined because each hits different cell-cycle phases.")

q("tox", "A 30-year-old graphic designer on chemotherapy asks why her hair is falling out. Which explanation is accurate?", [
  "'The drug causes an allergic reaction in the scalp.' || It is not an allergy",
  "'The cancer has spread to your hair follicles.' || It is not spread of cancer",
  "*'Hair follicle cells divide fast, so chemo harms them like cancer cells.'",
  "'Hair loss means the drug attacks only cancer cells.' || Chemo also harms normal cells"],
  "Chemo destroys rapidly dividing normal cells, such as hair follicles, GI lining and bone marrow, the same way it destroys cancer cells, causing alopecia.")

q("nadir", "A 37-year-old teacher is on day 11 after chemotherapy and wants to return to her classroom, where the flu is going around. Which response is best?", [
  "'Go ahead; your counts are at their highest now.' || Counts are lowest at days 10–14",
  "*'Your counts are lowest now, so avoid people who are ill.'",
  "'You only need precautions if you develop pus.' || Infection may occur without pus",
  "'Take your temperature rectally each morning.' || Rectal temperatures are avoided"],
  "The nadir, about day 10–14, is when blood counts are lowest and infection risk is greatest. Teach handwashing, avoiding ill people and reporting fever or sore throat.")

q("nadir", "A client with thrombocytopenia is at the chemotherapy nadir. Which findings suggest bleeding and should be reported? " + SATA, [
  "*Bleeding from the gums",
  "*Black, tarry stools",
  "Hair on the pillow in the morning || Alopecia is not a bleeding sign",
  "Asking for an electric razor || This is a bleeding precaution, not a sign",
  "Choosing a soft toothbrush || This is a bleeding precaution, not a sign"],
  "At the nadir, bleeding risk is greatest. Watch for bleeding from the gums and GI tract (melena), and use a soft toothbrush and electric razor.")

q("antimet", "A client taking methotrexate reports new shortness of breath. Why is this a concern?", [
  "It is an expected sign of hair loss || It is not related to alopecia",
  "*Methotrexate can cause pulmonary fibrosis",
  "It is a sign of hemorrhagic cystitis || That is a cyclophosphamide effect",
  "It means the folic acid level is too high || That is not a listed effect"],
  "Methotrexate, a folic acid analog, can cause liver damage and pulmonary fibrosis. Teach to report shortness of breath and yellowing of the skin or eyes.")

q("alkyl", "A nursing student describes how alkylating agents work. Which statement is accurate?", [
  "*'They break DNA bonds and cause abnormal pairing, mostly in S and G1.'",
  "'They stop the mitotic spindle during G2 and M.' || That describes antimitotics",
  "'They look like folate and block DNA replication.' || That describes antimetabolites",
  "'They block estrogen in breast cancer cells.' || That describes tamoxifen"],
  "Alkylating agents cause breaks in DNA bonds and abnormal DNA pairing, acting mostly in S and G1. Examples are cyclophosphamide and carmustine.")

q("alkyl", "A nurse plans care for a 46-year-old client receiving cyclophosphamide. Which actions are appropriate? " + SATA, [
  "*Monitor the CBC",
  "*Tell the client early about hair loss and that it grows back",
  "*Give mesna with each dose as ordered",
  "Restrict fluids to protect the bladder || Fluids are increased",
  "Expect the lowest counts 4–6 weeks later || That is carmustine's delayed nadir"],
  "Cyclophosphamide can cause hemorrhagic cystitis, alopecia, severe N/V and leukopenia. Increase fluids, give mesna, monitor the CBC and teach early about reversible hair loss.")

q("vesicant", "Which drugs from the lecture require vesicant precautions during IV infusion? " + SATA, [
  "*Doxorubicin",
  "*Carmustine",
  "*Vincristine",
  "Mesna || Mesna is a bladder protectant",
  "Leucovorin || Leucovorin is an antidote for methotrexate"],
  "Doxorubicin and carmustine are vesicants, and vincristine extravasation has its own protocol (heat and hyaluronidase). Assess the IV site often for pain, swelling or redness.")

q("vesicant", "A nurse suspects extravasation during a vesicant infusion. Which sequence of actions is correct?", [
  "Slow the rate, then recheck the site in an hour || Stop the infusion immediately",
  "Apply heat and continue the infusion || Stop first; treatment is drug-specific",
  "Flush the line forcefully, then notify the provider || Never flush forcefully",
  "*Stop the infusion, notify the provider, follow the drug protocol"],
  "Stop the infusion immediately, then notify the provider and follow the drug-specific extravasation protocol. Not every agent uses the same antidote or temperature.")

q("cis", "A 41-year-old client received cisplatin. On which day after treatment is the nurse most concerned about low blood counts?", [
  "Day 2 || The critical time is days 18–23",
  "Day 12 || The critical time is days 18–23",
  "*Day 20",
  "Week 5 || That fits carmustine's delayed nadir"],
  "The critical time for low counts after cisplatin is days 18–23. Monitor the CBC before each treatment and weekly after.")

q("cis", "A client is about to start cisplatin. Which order should the nurse question?", [
  "IV fluids before the infusion || This is expected",
  "*IV furosemide with the infusion",
  "An antiemetic 30 minutes before || This is expected",
  "A baseline hearing evaluation || This is expected"],
  "Other ototoxic drugs such as furosemide raise the risk of permanent hearing loss with cisplatin. Before cisplatin, infuse IV fluids, give an antiemetic, check hearing and weigh the client.")

q("doxo", "A 58-year-old client with bladder cancer is starting doxorubicin, an antitumor antibiotic. Which client statement needs correction?", [
  "'This drug works on the DNA of the cancer cells.' || This is accurate",
  "'My urine may look red for a day or two.' || This is accurate",
  "*'This antibiotic will also clear my bladder infection.'",
  "'I'll report chest pain even after treatment ends.' || This is accurate"],
  "Antitumor antibiotics interfere with cancer cell DNA and treat cancer only. Doxorubicin is cardiotoxic, may cause red urine, and heart damage can appear months or years later.")

q("doxo", "Which findings in a client's history are contraindications to doxorubicin? " + SATA, [
  "*An existing cardiac disorder",
  "*Existing bone marrow suppression",
  "*A full course of doxorubicin in the past",
  "A diagnosis of breast cancer || This is a cancer it treats",
  "A diagnosis of bladder cancer || This is a cancer it treats"],
  "Doxorubicin is contraindicated in existing cardiac disorders, existing marrow suppression and after a prior full course of doxorubicin.")

q("antimit", "Before giving vincristine, the nurse finds absent bowel sounds and no bowel movement for several days. What should the nurse do?", [
  "Give the dose with a stool softener || Ileus is a contraindication",
  "Give the dose and recheck tomorrow || Ileus is a contraindication",
  "*Hold the dose and notify the provider",
  "Give the dose faster to finish sooner || Rate won't change the risk"],
  "Vincristine causes severe constipation and is contraindicated in intestinal ileus. Monitor bowel sounds and bowel function.")

q("antimit", "A nurse prepares to give the solvent form of paclitaxel. Which medications are given 30 minutes before? " + SATA, [
  "*An antihistamine",
  "*A corticosteroid",
  "*An H2 blocker",
  "Mesna || Mesna protects the bladder with cyclophosphamide",
  "Leucovorin || Leucovorin is a methotrexate antidote"],
  "Solvent paclitaxel is premedicated with an antihistamine, a corticosteroid and an H2 blocker 30 minutes before to prevent allergic reactions, then infused over 3 hours with an in-line filter.")

q("topo", "A client receiving topotecan has bleeding gums and new bruises. What does the nurse recognize?", [
  "*Thrombocytopenia from severe marrow suppression",
  "Hemorrhagic cystitis from the infusion || That is a cyclophosphamide effect",
  "An expected effect that needs no report || Bleeding signs are reported",
  "Liver toxicity from an androgen blocker || That is a flutamide effect"],
  "Topotecan, a topoisomerase inhibitor, causes severe bone marrow suppression. Watch for neutropenia and thrombocytopenia.")

q("horm", "A 61-year-old postmenopausal client is taking anastrozole. Which client statement needs correction?", [
  "'I'll increase my calcium and vitamin D.' || This is accurate",
  "'I'll do weight-bearing exercise.' || This is accurate",
  "*'I'll take estrogen pills to help my hot flashes.'",
  "'I'll take it at the same time every day.' || This is accurate"],
  "Anastrozole, an aromatase inhibitor, lowers estrogen production in postmenopausal hormone-sensitive breast cancer. Teach calcium, vitamin D and weight-bearing exercise; monitor bone health.")

q("horm", "A 49-year-old client is starting tamoxifen. Which risks should the nurse include in teaching? " + SATA, [
  "*Blood clots",
  "*Uterine cancer",
  "*Retinopathy and cataracts",
  "Liver toxicity as its main risk || That is flutamide",
  "Hemorrhagic cystitis || That is cyclophosphamide"],
  "Tamoxifen blocks estrogen in breast cancer cells and raises the risk of clots (DVT, PE, stroke), uterine cancer and retinopathy/cataracts. Regular eye exams are needed.")

q("target", "A client is starting imatinib. Which client statement shows understanding?", [
  "'I'll take it on an empty stomach.' || Take it with a meal",
  "'Grapefruit juice is a good way to take it.' || Avoid grapefruit juice",
  "'Sudden weight gain is expected and fine.' || Report sudden weight gain",
  "*'I'll take it with a meal and a full glass of water.'"],
  "Imatinib is taken with a meal and at least 8 oz of water; avoid grapefruit juice. It causes fluid retention that can lead to pulmonary edema.")

q("hivgoal", "A nurse reviews the HIV life cycle. Which drug class blocks the FIRST step?", [
  "*Entry/fusion inhibitors",
  "Reverse transcriptase inhibitors || These block the second step",
  "Integrase inhibitors || These block the third step",
  "Protease inhibitors || These block the last step"],
  "Life cycle order: entry, reverse transcription, integration, protease maturation. Entry/fusion inhibitors keep HIV from entering the CD4 cell.")

q("hivgoal", "A 34-year-old client says, 'My viral load is undetectable now, so I can take breaks from my HIV pills.' Which response is best?", [
  "'Yes, short breaks are fine once the virus is low.' || Missed doses allow resistance",
  "*'Missed doses let the virus mutate and resist the drugs.'",
  "'Yes, you can double up when you restart.' || Take them exactly as prescribed",
  "'Breaks only change the side effects you feel.' || Missed doses allow resistance"],
  "Take antiretrovirals exactly as prescribed. Missed doses let the virus mutate and become drug-resistant; adherence keeps viral load low and CD4 high.")

q("entry", "A client on maraviroc asks why the nurse wants to review every medication they take. Which response is accurate?", [
  "'Maraviroc has no drug interactions.' || Maraviroc has many interactions",
  "'It's only needed for injected drugs.' || Maraviroc has many interactions",
  "*'Maraviroc has many drug interactions.'",
  "'It's to check your CCR5 test result.' || That is a separate test"],
  "Maraviroc blocks CCR5 co-receptors and has many interactions. Monitor for liver injury: rash, abdominal pain and jaundice.")

q("rti", "A client taking zidovudine has a low hemoglobin after 3 weeks. Which medication may be ordered?", [
  "Leucovorin || Leucovorin is the methotrexate antidote",
  "Mesna || Mesna protects the bladder",
  "*Epoetin alfa",
  "Dexrazoxane || Dexrazoxane protects the heart"],
  "Zidovudine causes bone marrow suppression: anemia in 2–4 weeks and neutropenia after about 6 weeks. Epoetin alfa or filgrastim may be given.")

q("rti", "Which statements about reverse transcriptase inhibitors are accurate? " + SATA, [
  "*They block conversion of viral RNA into DNA",
  "*Zidovudine is a nucleoside RTI",
  "*Delavirdine can cause liver toxicity",
  "Delavirdine's signature effect is marrow suppression || Delavirdine causes rash",
  "They keep HIV from entering the CD4 cell || That is entry/fusion inhibitors"],
  "RTIs block conversion of viral RNA into DNA. Zidovudine (NRTI) causes marrow suppression; delavirdine (NNRTI) causes rash and liver toxicity.")

q("pi", "A 41-year-old client taking ritonavir wants to start St. John's wort for low mood. What should the nurse say?", [
  "'It's a safe natural supplement to add.' || St. John's wort is contraindicated",
  "'Take it at a different time of day.' || St. John's wort is contraindicated",
  "'Supplements don't affect HIV drugs.' || Supplements must be reviewed",
  "*'St. John's wort is contraindicated with ritonavir.'"],
  "Ritonavir has many interactions: statins, midazolam, alprazolam and St. John's wort are contraindicated. Review all prescriptions, OTC drugs and supplements.")

q("pi", "A 50-year-old client on ritonavir has rising blood glucose and lipid levels. How should the nurse interpret this?", [
  "A sign of muscle injury from the drug || That is raltegravir (high CK)",
  "*A known effect of ritonavir that is monitored",
  "A sign the viral load is falling || Glucose doesn't reflect viral load",
  "An injection-site reaction || That is enfuvirtide"],
  "Ritonavir, a protease inhibitor, raises glucose and lipids and causes fat redistribution, so glucose and lipids are monitored.")
