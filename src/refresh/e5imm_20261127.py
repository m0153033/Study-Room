T = "e5imm"; SET = "20261127"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("cycle", "A 36-year-old nursing assistant asks which phase of the cell cycle comes right after the cell finishes making its DNA. Which answer is correct?", [
  "G1 || G1 comes before S phase",
  "*G2",
  "G0 || G0 is the resting phase",
  "M || M follows G2, not S"],
  "G1 prepares, S makes DNA, G2 prepares for mitosis and M divides. G0 cells rest and do their specialized job.")

q("types", "A 45-year-old baker is told his cancer began in the epithelial lining of his colon. Which type of cancer does the nurse recognize?", [
  "Sarcoma || Sarcoma starts in bone or soft tissue",
  "Lymphoma || Lymphoma starts in lymph tissue",
  "*Carcinoma",
  "Leukemia || Leukemia starts in blood-forming tissue"],
  "Cancer is classified by the tissue where it starts: carcinoma = epithelial, sarcoma = bone/soft tissue, lymphoma = lymph, leukemia = blood-forming tissue.")

q("why", "A 60-year-old retired pilot is starting chemotherapy given in cycles. Which client statement shows understanding of why?", [
  "'The rest weeks let the tumor grow so the next dose works better.' || Breaks are not meant to let the tumor grow",
  "'Spacing out the doses is what keeps me free of all side effects.' || Cycles do not prevent all side effects",
  "*'Each round reaches cancer cells as they regrow into vulnerable phases.'",
  "'The drug only works once a month, so more often would be wasted.' || This is not why chemo is cycled"],
  "Chemo is given in cycles so the drug is available as cells grow back and enter susceptible phases of the cell cycle.")

q("tox", "A 55-year-old mail carrier receiving chemotherapy has low blood counts and asks why. Which explanation is accurate?", [
  "'The cancer has spread into your blood.' || Low counts are a chemo effect on normal cells",
  "*'Marrow cells divide fast, so chemo harms them like cancer cells.'",
  "'You are having an allergic reaction to the drug.' || It is not an allergy",
  "'The drug attacks only cancer cells in your marrow.' || Chemo also harms normal cells"],
  "Chemo destroys rapidly dividing normal cells, such as bone marrow, hair follicles and GI lining, the same way it destroys cancer cells, causing marrow suppression, alopecia and stomatitis.")

q("nadir", "A 48-year-old client received chemotherapy 3 days ago and asks when to be most careful about infection and bleeding. Which response is best?", [
  "'Today, since the drug was just given.' || Counts are not lowest right after the dose",
  "'About 6 months after treatment ends.' || The nadir is much sooner",
  "*'About days 10 to 14 after the treatment.'",
  "'Only on the day of each infusion.' || Counts drop after the infusion day"],
  "The nadir, about day 10–14, is when blood counts are lowest and the risk of infection and bleeding is greatest. Follow neutropenic precautions during the nadir.")

q("nadir", "A client at the chemotherapy nadir has severe neutropenia. Which medication does the nurse expect may be ordered to raise the neutrophil count?", [
  "Mesna || Mesna protects the bladder",
  "Leucovorin || Leucovorin is the methotrexate antidote",
  "Dexrazoxane || Dexrazoxane protects the heart",
  "*Filgrastim"],
  "For severe neutropenia, a chemo 'vacation' and/or a colony-stimulating medication like filgrastim, which raises neutrophils, may be ordered.")

q("antimet", "A 34-year-old client received intrathecal cytarabine and now has a headache, fever, nausea and vomiting. What does the nurse suspect?", [
  "Hemorrhagic cystitis || That is linked to cyclophosphamide",
  "*Arachnoiditis",
  "Ototoxicity || That is linked to cisplatin",
  "Pulmonary fibrosis || That is linked to methotrexate and carmustine"],
  "Intrathecal cytarabine (pyrimidine analog) can cause arachnoiditis: nausea, vomiting, headache and fever. Dexamethasone is given with intrathecal cytarabine.")

q("alkyl", "A nurse reviews the care plan for a 57-year-old client receiving cyclophosphamide. Which order should the nurse question?", [
  "Give mesna with each dose || This protects the bladder",
  "*Restrict fluids to 1 L per day",
  "Monitor the urine for blood || This detects hemorrhagic cystitis",
  "Monitor the CBC || Cyclophosphamide causes leukopenia"],
  "Cyclophosphamide can cause hemorrhagic cystitis. Void before the dose, increase fluid intake, give mesna with each dose, monitor the urine for blood and monitor the CBC.")

q("alkyl", "A nurse plans care for a 52-year-old client receiving IV carmustine. Which actions are appropriate? " + SATA, [
  "*Listen to breath sounds",
  "*Monitor pulmonary function tests",
  "*Watch counts closely 4–6 weeks after each dose",
  "Give mesna with each dose || Mesna is used with cyclophosphamide",
  "Expect counts to recover by day 7 || Carmustine has a delayed nadir"],
  "Carmustine (nitrosourea) can cause irreversible pulmonary fibrosis, so listen to breath sounds and monitor pulmonary function tests. Its critical time for low counts is 4–6 weeks after each treatment.")

q("vesicant", "A nurse reviews drug-specific extravasation treatments. Which pairing is correct?", [
  "Vincristine — cold therapy and sodium bicarbonate || That is the carmustine treatment",
  "Carmustine — heat and local hyaluronidase || That is the vincristine treatment",
  "*Carmustine — cold therapy and sodium bicarbonate",
  "Vincristine — leucovorin given as the antidote || Leucovorin is the methotrexate antidote"],
  "Extravasation treatment is drug-specific: carmustine uses bicarbonate and cold; vincristine uses heat (warm compress) and hyaluronidase.")

q("vesicant", "A 29-year-old client is receiving doxorubicin through a peripheral IV. Which client statement requires the nurse's immediate action?", [
  "'My urine looked a little red this morning.' || Red urine is expected with doxorubicin",
  "'I'm worried my hair will fall out soon.' || Hair loss is reversible and not urgent",
  "'I'd like a warm blanket for my legs.' || This is a comfort request",
  "*'The skin around my IV is burning and puffy.'"],
  "Pain, swelling or redness at the IV site suggest extravasation of a vesicant, which can cause blistering and necrosis. Stop the infusion immediately, notify the provider and follow the drug-specific protocol.")

q("cis", "A 33-year-old client with testicular cancer receiving cisplatin reports numbness and tingling in both feet. What does the nurse recognize?", [
  "Ototoxicity from the drug || Ototoxicity affects hearing",
  "*Peripheral neuropathy from the drug",
  "Hemorrhagic cystitis from the drug || That affects the bladder",
  "Cardiotoxicity from the drug || That is linked to doxorubicin"],
  "Cisplatin (platinum compound) causes severe nausea and vomiting, ototoxicity, nephrotoxicity, fluid retention and peripheral neuropathy.")

q("cis", "A client receiving cisplatin asks why the nurse weighs them before treatment. Which response is accurate?", [
  "'It tells us if you have hearing loss.' || Hearing is checked by a hearing evaluation",
  "'It shows if your hair is growing back.' || Weight does not reflect hair growth",
  "*'Cisplatin can cause fluid retention.'",
  "'It checks for blood in your urine.' || Weight does not detect blood in urine"],
  "Cisplatin is nephrotoxic and causes fluid retention, so weigh the client and monitor renal function and fluid balance.")

q("doxo", "A 44-year-old client is receiving doxorubicin. Why does the nurse check the IV site closely during the infusion?", [
  "It is ototoxic and harms hearing || That is cisplatin",
  "It causes hemorrhagic cystitis || That is cyclophosphamide",
  "*It is a vesicant that damages tissue",
  "It causes severe bradycardia || That is paclitaxel"],
  "Doxorubicin (anthracycline) is cardiotoxic and is also a vesicant, so assess the IV site for extravasation.")

q("doxo", "A client starting doxorubicin asks why an ACE inhibitor was prescribed. Which response is accurate?", [
  "'It keeps your urine from turning red.' || Red urine is expected and temporary",
  "*'It may help protect your heart.'",
  "'It keeps your hair from falling out.' || It does not prevent hair loss",
  "'It protects your bladder from bleeding.' || That is mesna with cyclophosphamide"],
  "Doxorubicin is cardiotoxic. Dexrazoxane or an ACE inhibitor may be ordered to protect the heart.")

q("antimit", "A nurse cares for one client receiving vincristine and another receiving paclitaxel. Which monitoring priority matches each drug?", [
  "Vincristine: heart rhythm; paclitaxel: bowel function || The pairs are reversed",
  "Vincristine: hearing; paclitaxel: urine for blood || Neither is listed for these drugs",
  "*Vincristine: bowel function; paclitaxel: heart rhythm",
  "Vincristine: urine color; paclitaxel: hearing || Neither is listed for these drugs"],
  "Vincristine (vinca alkaloid) causes peripheral neuropathy and severe constipation. Paclitaxel (taxane) can cause severe bradycardia during infusion, so cardiac monitoring is the priority.")

q("antimit", "A 66-year-old client is starting vincristine. Which client statement shows correct understanding?", [
  "'I'll cut back on fluids so I don't feel bloated.' || Fluids help prevent constipation",
  "*'I'll drink fluids and use my stool softener as ordered.'",
  "'If I don't have a bowel movement for days, that's harmless.' || This can lead to ileus",
  "'Tingling in my hands is expected, so I won't mention it.' || Neuropathy must be reported"],
  "Vincristine causes severe constipation that can lead to ileus or obstruction, and peripheral neuropathy. Prevent constipation with fluids and ordered stool softeners.")

q("topo", "A 62-year-old client asks how topotecan works against cancer. Which explanation is accurate?", [
  "'It stops the mitotic spindle so the cell can't divide.' || That is an antimitotic",
  "'It blocks estrogen in breast cancer cells.' || That is tamoxifen",
  "'It looks like folate and stops DNA synthesis.' || That is methotrexate",
  "*'It blocks an enzyme that untangles DNA, so DNA can't replicate.'"],
  "Topoisomerase enzymes make temporary breaks in DNA to relieve coiling and tangles so DNA can replicate. Topotecan blocks this; its main risk is severe bone marrow suppression.")

q("horm", "A 71-year-old client with prostate cancer is starting leuprolide and flutamide. He asks what flutamide does. Which response is accurate?", [
  "'It lowers estrogen production in your body.' || That is anastrozole",
  "*'It blocks the effects of androgens.'",
  "'It blocks estrogen in breast cancer cells.' || That is tamoxifen",
  "'It stops the mitotic spindle in cells.' || That is an antimitotic"],
  "Flutamide blocks androgens and begins when the GnRH drug starts. Monitor liver function tests monthly for the first few months.")

q("horm", "A 74-year-old retired farmer started leuprolide 1 week ago and says, 'My prostate symptoms got worse, so this drug must not work.' Which response is best?", [
  "'You may be allergic to it, so stop taking it.' || This is not an allergic reaction",
  "'Worse symptoms mean the drug has failed.' || A brief flare is expected",
  "*'An early flare can happen before hormones are suppressed.'",
  "'This is hemorrhagic cystitis from the drug.' || That is a cyclophosphamide effect"],
  "Leuprolide is a GnRH agonist: an initial hormone flare happens before hormone production is suppressed. Other effects include hot flashes, decreased libido and bone loss.")

q("target", "A nurse reviews targeted therapy drugs. Which drug is paired with its correct target?", [
  "Trastuzumab — abnormal tyrosine kinase || Trastuzumab targets HER2",
  "*Imatinib — abnormal tyrosine kinase",
  "Imatinib — HER2-positive cells || Trastuzumab targets HER2",
  "Interferon alfa — HER2-positive cells || Interferon alfa is a biologic response modifier"],
  "Targeted therapy attacks a specific molecule on cancer cells with less harm to normal cells: trastuzumab targets HER2 and imatinib targets abnormal tyrosine kinase.")

q("hivgoal", "A 27-year-old barista on combination antiretroviral therapy has an undetectable viral load and a rising CD4 count. How should the nurse interpret this?", [
  "The HIV is cured, so therapy can stop || Therapy is not a cure",
  "*The therapy is working; keep taking it",
  "The regimen needs more drugs added || These results show success",
  "Doses can now be skipped safely || Missed doses cause resistance"],
  "Effective therapy lowers viral load (ideally undetectable) and raises CD4. Missed doses let the virus mutate and become drug-resistant, so take antiretrovirals exactly as prescribed.")

q("hivgoal", "A nurse reviews the HIV life cycle. Which drug class blocks the step just before integration?", [
  "Entry/fusion inhibitors || Entry is the first step",
  "Integrase inhibitors || They block integration itself",
  "*Reverse transcriptase inhibitors",
  "Protease inhibitors || Protease maturation is the last step"],
  "Life cycle order: entry → reverse transcription → integration → protease maturation. Drug classes: entry/fusion inhibitors, RTIs, integrase inhibitors, protease inhibitors.")

q("entry", "A nursing student compares enfuvirtide and maraviroc. Which statement is accurate?", [
  "Maraviroc is injected subcutaneously twice a day || That describes enfuvirtide",
  "Enfuvirtide blocks viral DNA from entering host DNA || That is an integrase inhibitor",
  "*Enfuvirtide is a subcutaneous injection; maraviroc needs CCR5-tropic HIV",
  "Both drugs block protease so new virus can't mature || That is a protease inhibitor"],
  "Enfuvirtide is a subcutaneous entry/fusion inhibitor given twice a day. Maraviroc blocks CCR5 co-receptors, so the client's HIV must be CCR5-tropic.")

q("rti", "A client is starting zidovudine. How often does the nurse expect hemoglobin and neutrophils to be monitored?", [
  "Once a year || Monitoring is more frequent",
  "*Monthly",
  "Only if a rash appears || Rash is linked to delavirdine",
  "Only during pregnancy || Marrow suppression can affect any client"],
  "Zidovudine (NRTI) causes severe bone marrow suppression: anemia in 2–4 weeks and neutropenia after about 6 weeks. Monitor hemoglobin and neutrophils monthly.")

q("rti", "A 39-year-old truck driver taking delavirdine says he chews antacid tablets with each dose for heartburn. Which response is best?", [
  "'That's fine; antacids protect your stomach.' || Antacids should not be taken with it",
  "'Take two antacids to work even better.' || Antacids should not be taken with it",
  "*'Delavirdine should not be taken with antacids.'",
  "'Antacids only matter with zidovudine.' || The antacid caution is for delavirdine"],
  "Delavirdine (NNRTI) should not be taken with antacids. It can cause rash, including Stevens-Johnson syndrome, and liver toxicity.")

q("pi", "A client taking ritonavir has a new prescription for simvastatin to lower cholesterol. What should the nurse do?", [
  "Give both drugs together at bedtime || Simvastatin is contraindicated",
  "*Question the order with the provider",
  "Give simvastatin and hold ritonavir || Do not stop antiretrovirals on your own",
  "Give it, since statins don't interact || Statins are contraindicated"],
  "Ritonavir has many interactions; simvastatin and lovastatin, midazolam, alprazolam and St. John's wort are contraindicated with protease inhibitors.")

q("pi", "A 38-year-old client taking ritonavir reports nausea and an altered taste. Which teaching is appropriate?", [
  "'Take it on an empty stomach.' || It is taken with food",
  "'Take it once a week instead.' || It is taken twice daily",
  "'Skip doses when you feel sick.' || Doses should not be skipped",
  "*'Take it with food or a snack.'"],
  "Ritonavir is taken twice daily with food or a snack; food also reduces GI effects and altered taste.")
