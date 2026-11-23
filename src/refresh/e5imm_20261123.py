T = "e5imm"; SET = "20261123"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("cycle", "A nursing student reviews the cell cycle before caring for a 55-year-old client starting chemotherapy. Which statement by the student needs correction?",
  ["G0 is a resting phase when cells do their specialized job || correct: G0 cells carry out their differentiated function",
   "M is the phase when the cell divides into two || correct: M phase is division",
   "*G1 is the phase when the cell makes its DNA",
   "G2 is when the cell prepares for mitosis || correct: G2 prepares for mitosis"],
  "DNA is made in S phase, not G1. G1 prepares, S makes DNA, G2 prepares for mitosis, M divides, and G0 cells rest and do their specialized job.")

q("types", "A 27-year-old client is told the cancer began in the blood-forming tissue. Which type of cancer does the nurse recognize this as?",
  ["Carcinoma || carcinoma starts in epithelial tissue",
   "Sarcoma || sarcoma starts in bone or soft tissue",
   "Lymphoma || lymphoma starts in lymph tissue",
   "*Leukemia"],
  "Cancer is classified by the tissue where it starts: leukemia = blood-forming tissue, carcinoma = epithelial, sarcoma = bone/soft tissue, lymphoma = lymph.")

q("why", "A 61-year-old client asks why the chemotherapy is spread out with weeks between treatments instead of given all at once. Which response is best?",
  ["'The break lets the tumor grow a bit so the next drugs work better.' || chemo is not timed to let the tumor grow",
   "*'Each cycle hits cells as they regrow and enter vulnerable phases.'",
   "'Chemotherapy only works once a month, so more often would be wasted.' || there's no monthly rule for chemo working",
   "'Spacing the doses out is how we prevent every side effect.' || cycles don't prevent all adverse effects"],
  "Chemo is given in cycles so the drug is available as cells grow back and enter susceptible phases of the cell cycle.")

q("tox", "A 38-year-old client receiving chemotherapy for breast cancer develops painful mouth sores and asks why. Which explanation is accurate?",
  ["'Your mouth has a bacterial infection that spread from the cancer.' || the lecture explains this as drug damage to dividing cells",
   "'It's an allergic reaction to one of the drugs in your regimen.' || side effects come from the shared cell-killing mechanism, not allergy",
   "*'The drug harms fast-dividing normal cells, like your GI lining.'",
   "'It means the chemo is attacking only the cancer cells in your mouth.' || chemo also destroys normal cells"],
  "Chemo destroys normal rapidly dividing cells in the same way it destroys cancer cells; damage to the GI lining causes stomatitis and GI ulceration.")

q("nadir", "A 66-year-old client is on day 12 after a chemotherapy treatment. Which finding should the nurse report to the provider first?",
  ["Hair shedding on the pillow || alopecia is an expected effect and hair grows back",
   "Asking for a soft toothbrush || this is an appropriate bleeding precaution, not a problem",
   "*New fever and sore throat",
   "Asking when the next cycle is scheduled || this is a routine question, not a safety concern"],
  "Day 10–14 is the nadir, when blood counts are lowest and the risk of infection and bleeding is greatest. Fever or sore throat must be reported.")

q("nadir", "A client at the chemotherapy nadir has low white blood cells and low platelets. Which nursing actions are appropriate? " + SATA,
  ["*Monitor the CBC (complete blood count)",
   "*Teach scrupulous handwashing and avoiding people who are ill",
   "*Apply prolonged pressure after any injection",
   "Take the temperature rectally each shift || rectal temperatures are avoided in neutropenia",
   "Massage injection sites firmly afterward || vigorous massage increases bleeding"],
  "During the nadir, monitor the CBC and follow neutropenic and bleeding precautions: handwashing, avoiding sick contacts, small-gauge needles and prolonged pressure.")

q("antimet", "A client taking methotrexate asks the nurse whether an over-the-counter NSAID (nonsteroidal anti-inflammatory drug) is okay for a headache. Which response is best?",
  ["'Yes, NSAIDs help protect your liver during methotrexate therapy.' || NSAIDs don't protect the liver",
   "'Yes, NSAIDs have no effect at all on how methotrexate works.' || NSAIDs and salicylates interact with methotrexate",
   "'Yes, and take extra folic acid with it to balance the effect.' || clients shouldn't take extra folic acid on their own",
   "*'NSAIDs can cause methotrexate toxicity; ask your provider first.'"],
  "NSAIDs and salicylates can cause methotrexate toxicity. Methotrexate is a folic acid analog that can also cause liver damage and pulmonary fibrosis.")

q("alkyl", "The nurse teaches a 49-year-old client starting cyclophosphamide. Which client statement shows correct understanding?",
  ["'I'll limit my fluids so I don't have to urinate as often.' || fluids are increased to protect the bladder",
   "*'I'll empty my bladder before each dose and drink extra fluids.'",
   "'My hair loss from this drug will be permanent.' || hair loss from cyclophosphamide grows back",
   "'Mesna is only given if I notice blood in my urine.' || mesna is given with each dose"],
  "Voiding before the dose and increasing fluid intake help prevent hemorrhagic cystitis. Mesna is given with each dose, and blood in the urine or pain with voiding is reported.")

q("alkyl", "A client is receiving IV (intravenous) carmustine. Which statements about this drug are accurate? " + SATA,
  ["*It crosses the blood-brain barrier",
   "*Blood counts are lowest about 4–6 weeks after each treatment",
   "*It can cause irreversible pulmonary fibrosis",
   "Its signature adverse effect is hemorrhagic cystitis || that's cyclophosphamide",
   "It acts mainly by stopping the mitotic spindle || that's antimitotics; alkylating agents break DNA bonds"],
  "Carmustine is a nitrosourea alkylating agent that crosses the blood-brain barrier, has a delayed nadir (4–6 weeks), can cause pulmonary fibrosis and can be a vesicant IV.")

q("vesicant", "A nurse is planning IV (intravenous) access for a client who will receive doxorubicin, a vesicant. Which choice best reduces the risk of serious extravasation injury?",
  ["A vein in the antecubital space || extravasation near joints can injure tendons and nerves",
   "A small vein on the back of the wrist || veins near the wrist are avoided for vesicants",
   "*A central line",
   "A hand vein close to a knuckle joint || veins near joints are avoided for vesicants"],
  "A central line is used when possible for vesicants. Extravasation near the wrist, antecubital space or other joints can cause necrosis and tendon or nerve injury.")

q("vesicant", "A carmustine infusion infiltrates, and the nurse stops the infusion right away. Which drug-specific treatment does the nurse anticipate?",
  ["*Cold therapy and sodium bicarbonate as ordered",
   "Warm compress and a local hyaluronidase injection || that's the treatment for vincristine",
   "Leucovorin given as the antidote to the infiltration || leucovorin is the methotrexate antidote",
   "Mesna injected around the infiltrated site || mesna protects the bladder with cyclophosphamide"],
  "Extravasation treatment is drug-specific: carmustine uses bicarbonate and cold; vincristine uses heat and hyaluronidase.")

q("cis", "A 24-year-old client is receiving cisplatin. Which client statement indicates a need for more teaching?",
  ["'Nausea may start about an hour after the infusion begins.' || correct: severe N/V usually starts about 1 hour in",
   "'I'll have my hearing checked before and during treatment.' || correct: cisplatin is ototoxic",
   "*'I'll wait to take my antiemetic until the vomiting starts.'",
   "'The nurse will weigh me and watch my kidney tests.' || correct: cisplatin is nephrotoxic and causes fluid retention"],
  "Cisplatin causes severe nausea and vomiting starting about 1 hour into the infusion, so an antiemetic is given 30 minutes BEFORE, not after vomiting begins.")

q("cis", "Which ongoing monitoring does the nurse plan for a client receiving cisplatin? " + SATA,
  ["*BUN (blood urea nitrogen) and creatinine",
   "*Hearing, including reports of ringing in the ears",
   "*Weight and fluid balance",
   "Urine for expected red color || red urine is a doxorubicin effect",
   "Heart rate for bradycardia during infusion || that's a paclitaxel concern"],
  "Cisplatin is nephrotoxic and ototoxic and causes fluid retention, so monitor renal function, hearing, weight and fluid balance. CBC is also checked; the critical time is days 18–23.")

q("doxo", "A 50-year-old client finished doxorubicin therapy 6 months ago and now reports palpitations and shortness of breath. How should the nurse interpret this?",
  ["*Possible delayed heart damage that must be reported",
   "An expected effect that ended when the infusions stopped || heart damage can appear months or years later",
   "A sign of hemorrhagic cystitis from the earlier doses || that's a cyclophosphamide effect with blood in the urine",
   "A normal effect of hair regrowth after treatment ends || hair regrowth doesn't cause cardiac symptoms"],
  "Doxorubicin is cardiotoxic, and heart damage can show up months or years later. Palpitations, shortness of breath or chest pain must be reported.")

q("doxo", "A client is about to start doxorubicin. Which medication may be ordered to help protect the heart?",
  ["Mesna || mesna protects the bladder during cyclophosphamide",
   "Leucovorin || leucovorin is the antidote for methotrexate",
   "Hyaluronidase || hyaluronidase is used for vincristine extravasation",
   "*Dexrazoxane"],
  "Dexrazoxane or an ACE (angiotensin-converting enzyme) inhibitor may be ordered to protect the heart during doxorubicin therapy.")

q("antimit", "Which nursing interventions help prevent or detect complications of vincristine? " + SATA,
  ["*Encourage fluids and give stool softeners as ordered",
   "*Monitor bowel sounds and bowel function",
   "*Check Achilles reflexes and hand/foot strength",
   "Give mesna with each dose || mesna is for cyclophosphamide",
   "Check hearing before each dose || hearing tests are for cisplatin"],
  "Vincristine causes peripheral neuropathy and severe constipation that can lead to ileus. Prevent constipation and check deep tendon reflexes; the dose may be lowered if neuropathy develops.")

q("antimit", "A nurse is preparing to give the solvent form of paclitaxel. Which action is correct?",
  ["Give it by rapid IV (intravenous) push || it is infused over 3 hours",
   "Give premedications only if a reaction occurs || premedication is given 30 minutes before",
   "*Infuse it over 3 hours through an in-line filter",
   "Skip cardiac monitoring if vital signs are normal || severe bradycardia can occur during infusion"],
  "Solvent paclitaxel is given after premedication (antihistamine, corticosteroid, H2 blocker) 30 minutes before, infused over 3 hours with an in-line filter, with cardiac monitoring.")

q("topo", "A client received topotecan today. Around which day will the nurse be most concerned about neutropenia?",
  ["Day 1, the day of the infusion || counts don't bottom out on the day of infusion",
   "*About day 12 after the infusion",
   "Weeks 4–6 after the infusion || that's the delayed nadir of carmustine",
   "Days 18–23 after the infusion || that's the critical time for cisplatin"],
  "Topotecan's neutropenia nadir is about day 12. It causes severe bone marrow suppression; filgrastim is given 24 hours after the infusion is complete.")

q("horm", "A 70-year-old client with prostate cancer is starting leuprolide. Which adverse effects should the nurse include in teaching? " + SATA,
  ["*Hot flashes",
   "*Decreased libido",
   "*Bone loss",
   "Hemorrhagic cystitis || that's cyclophosphamide",
   "Red urine for 2 days || that's doxorubicin"],
  "Leuprolide is a GnRH agonist: initial flare, then suppression. Effects include hot flashes, decreased libido and bone loss; bone density is monitored.")

q("horm", "For which client is anastrozole an appropriate treatment?",
  ["A 38-year-old premenopausal woman with hormone-sensitive breast cancer || anastrozole is only for postmenopausal clients",
   "*A 64-year-old postmenopausal woman with hormone-sensitive breast cancer",
   "A 72-year-old man with prostate cancer || prostate cancer uses agents like flutamide or leuprolide",
   "A 58-year-old woman with breast cancer who wants estrogen for hot flashes || anastrozole lowers estrogen production"],
  "Anastrozole is an aromatase inhibitor that lowers estrogen production in postmenopausal hormone-sensitive breast cancer. Monitor bone health.")

q("target", "A client taking imatinib reports a sudden weight gain and new ankle swelling. What is the nurse's priority?",
  ["Tell the client this is expected and needs no follow-up at all || these signs must be reported",
   "Encourage a glass of grapefruit juice with each dose to aid absorption || grapefruit juice is avoided",
   "*Report it; imatinib fluid retention can cause pulmonary edema",
   "Tell the client to take the next dose on an empty stomach instead || imatinib is taken with a meal"],
  "Imatinib causes fluid retention that can lead to pulmonary edema. Teach to report sudden weight gain, swelling or shortness of breath.")

q("hivgoal", "A 31-year-old client has been on combination antiretroviral therapy for several months. Which result is most concerning to the nurse?",
  ["Viral load that is now undetectable || this shows therapy is working",
   "CD4 (cluster of differentiation 4) count that is increasing || this shows therapy is working",
   "*Viral load that is rising",
   "Viral load that is steadily decreasing || this shows therapy is working"],
  "Effective therapy lowers the viral load (ideally undetectable) and raises the CD4 count. A rising viral load suggests a problem such as poor adherence or resistance.")

q("hivgoal", "The nurse teaches a client newly started on HIV (human immunodeficiency virus) medications. Which client statement needs more teaching?",
  ["'Taking two or more drugs lowers the chance of resistance.' || correct: that's why combination therapy is used",
   "'Each drug blocks a different step of the virus life cycle.' || correct: drugs target different steps",
   "'I need to take my medicines exactly as prescribed.' || correct: adherence is essential",
   "*'When I feel well, it's okay to skip a few doses.'"],
  "Missed doses let the virus mutate and become drug-resistant. Adherence lowers viral load, raises CD4 and reduces resistance.")

q("entry", "A client who injects enfuvirtide twice a day calls reporting a new cough and fever. Which response is best?",
  ["'This is a normal injection-site reaction.' || cough and fever aren't injection-site reactions",
   "*'Please report this now; enfuvirtide can cause pneumonia.'",
   "'Switch to a deep IM (intramuscular) injection instead.' || enfuvirtide is given subcutaneously",
   "'Inject into scarred skin to slow absorption.' || discolored or scarred skin is avoided"],
  "Enfuvirtide, an entry/fusion inhibitor, can cause pneumonia. Teach to report cough, fever or shortness of breath and to rotate subcutaneous sites.")

q("rti", "A 26-year-old pregnant client with HIV (human immunodeficiency virus) will receive zidovudine to prevent transmission to the fetus. Which plan matches the lecture?",
  ["*Oral doses starting at 14 weeks, then IV during delivery",
   "A single IV (intravenous) dose given only after the baby is born || oral doses start at 14 weeks",
   "Oral doses starting only in the last week of pregnancy || dosing starts at 14 weeks",
   "No medication at all until after the baby is delivered || zidovudine is given during pregnancy and delivery"],
  "Zidovudine is used to prevent maternal HIV transmission to the fetus: oral doses start at 14 weeks, with IV during delivery.")

q("rti", "Which instruction should the nurse give a client starting delavirdine?",
  ["'Take it with an antacid to protect your stomach.' || delavirdine isn't taken with antacids",
   "'A rash is expected and can be ignored.' || severe rash needs prompt evaluation",
   "'You'll need creatine kinase levels checked.' || muscle injury is a raltegravir effect",
   "*'Don't take it with antacids, and report any rash.'"],
  "Delavirdine (NNRTI) can cause rash, including Stevens-Johnson syndrome, and liver toxicity. Don't take it with antacids.")

q("pi", "A 45-year-old client is starting ritonavir. Which teaching points should the nurse include? " + SATA,
  ["*Take it twice daily with food or a snack",
   "*Review all prescriptions, OTC (over-the-counter) drugs and supplements with the provider",
   "*Blood glucose and lipid levels will be monitored",
   "St. John's wort is a safe supplement to add || St. John's wort is contraindicated",
   "Take it on an empty stomach for best effect || it is taken with food"],
  "Ritonavir is taken twice daily with food, has many drug interactions (St. John's wort is contraindicated), and raises glucose and lipids.")

q("pi", "A client who just started raltegravir reports feeling dizzy. Which instruction is most appropriate?",
  ["'Double your next dose to get past the side effect faster.' || consistent dosing is reinforced",
   "*'Avoid driving until you know how the drug affects you.'",
   "'Stop the drug on your own until the dizziness passes.' || consistent dosing is reinforced",
   "'Dizziness is a sign the virus is being cleared.' || dizziness is an adverse effect"],
  "ATI lists nausea, vomiting, diarrhea, dizziness and headache for raltegravir (integrase inhibitor); avoid driving until effects are known. Muscle injury (high CK) is also flagged.")
