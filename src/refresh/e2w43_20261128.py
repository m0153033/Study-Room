T = "e2w43"; SET = "20261128"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("variation", "A nursing student compares hyperplasia with dysplasia. Which statement by the student is accurate?", [
  "'Both terms describe cells that are dying.' || Neither term means cell death",
  "*'Hyperplasia adds normal cells; dysplasia has abnormal structure.'",
  "'Hyperplasia is precancerous; dysplasia is normal growth.' || Dysplasia, not hyperplasia, may be precancerous",
  "'Both terms mean a malignant tumor has formed.' || Neither term means a malignant tumor"],
  "Hyperplasia is an increased number of normal cells in response to a stimulus, such as BPH or gingival hyperplasia from phenytoin. Dysplasia is abnormal cell structure that may be precancerous.")

q("benign", "A 50-year-old is told a removed tumor was benign. Which statement by the client shows understanding?", [
  "'The cells were loosely attached and could migrate.' || Loose adherence and migration describe malignant cells",
  "'It had irregular borders and no capsule.' || Irregular borders without a capsule describe malignancy",
  "*'It had a capsule and is not expected to spread.'",
  "'The cells had abnormal chromosome numbers.' || Aneuploid chromosomes describe malignant cells"],
  "Benign tumors have clear borders, are often encapsulated, show tight adherence and euploid chromosomes, and do not metastasize. Malignant cells are irregular, not encapsulated, loosely adherent, aneuploid and can invade and metastasize.")

q("carcino", "The nurse reviews carcinogenesis with a client. Which sequence of stages is correct?", [
  "Promotion, initiation, metastasis, progression || Initiation comes first, and metastasis is last",
  "*Initiation, promotion, progression, metastasis",
  "Progression, promotion, initiation, metastasis || Initiation, when DNA is altered, comes first",
  "Initiation, progression, metastasis, promotion || Promotion comes before progression"],
  "Carcinogenesis moves from initiation (a carcinogen alters DNA) to promotion (hormones or proteins stimulate growth) to progression (angiogenesis/VEGF) to metastasis.")

q("prevent", "A community nurse is teaching about primary cancer prevention. Which actions should the nurse include? " + SATA, [
  "*Not smoking",
  "*HPV vaccination",
  "*Avoiding UV exposure",
  "A yearly mammogram from age 40 || Screening is secondary prevention",
  "Colonoscopy every 10 years from 45 || Screening is secondary prevention"],
  "Primary prevention keeps cancer from starting: no smoking, HPV (human papillomavirus) vaccine, diet and UV (ultraviolet) avoidance. Secondary prevention is screening and early detection.")

q("caution", "A 62-year-old reports several health changes at a clinic visit. Which report matches a CAUTION warning sign of cancer?", [
  "Sudden weight gain over the past month || Weight gain is not a CAUTION sign",
  "Itchy skin on both arms in winter || Itching is not a CAUTION sign",
  "Trouble falling asleep most nights || Insomnia is not a CAUTION sign",
  "*Hoarseness that has lasted for weeks"],
  "CAUTION: Change in bowel or bladder habits, A sore that won't heal, Unusual bleeding or discharge, Thickening or lump, Indigestion or difficulty swallowing, Obvious change in a wart or mole, Nagging cough or hoarseness.")

q("tnm", "A client asks why her tumor report says T3 when her friend's said T1. Which response by the nurse is accurate?", [
  "*'T is the primary tumor; higher numbers are more concerning.'",
  "'T counts the lymph nodes; higher is less concerning.' || N, not T, describes regional nodes",
  "'T shows distant spread; a lower number is worse.' || M shows distant spread; higher is worse",
  "'T is the nuclear grade, which does not affect stage.' || T describes primary tumor size and extent"],
  "In TNM (tumor, node, metastasis) staging, T is primary tumor size and extent, N is regional lymph nodes, and M is distant metastasis. Higher numbers are more concerning.")

q("surgery", "A client with advanced cancer is scheduled for palliative surgery. Which goal fits this type of surgery?", [
  "Removing high-risk tissue before cancer forms || That describes prophylactic surgery",
  "*Reducing pain and improving quality of life",
  "Removing both breasts due to a BRCA mutation || That is prophylactic surgery",
  "Giving chemotherapy first to shrink the tumor || That is neoadjuvant chemotherapy"],
  "Palliative surgery relieves obstruction, debulks, reduces pain and improves quality of life. Prophylactic surgery removes high-risk tissue, such as mastectomy with a BRCA mutation.")

q("extrad", "The nurse teaches a client starting external beam radiation. Which statement by the client needs correction?", [
  "'I'll use only the unscented lotion I was prescribed.' || Correct skin-care teaching",
  "*'I'll scrub off the skin markings after each session.'",
  "'I'll wash the area gently with a mild soap.' || Correct skin-care teaching",
  "'I'll keep the treated skin out of the sun.' || Correct skin-care teaching"],
  "With external beam radiation, the client keeps tattoo markings, uses mild soap, avoids friction and sun, and uses only prescribed unscented non-drying lotion. The client and body fluids are not radioactive.")

q("brachy", "The nurse plans care for a client with an intracavitary radiation implant. Which plan is correct?", [
  "Keep the door open so staff can watch the client || The door is kept closed",
  "*Wear a lead apron and limit exposure to about 1 hour/day",
  "Assign a pregnant nurse since the dose is low || No pregnant staff are assigned",
  "Move the client to a shared room for company || A private room is required"],
  "An intracavitary implant is radioactive until removed: private room, door closed, lead apron, about 1 hour/day exposure, no pregnant staff or visitors, and long-handled forceps plus a lead container in the room.")

q("chemo", "A float nurse offers to help hang a client's chemotherapy infusion. Which response by the charge nurse is best?", [
  "'Anyone can hang it if they wash their hands.' || Only trained staff handle chemo",
  "*'Only trained staff wearing PPE may handle chemo.'",
  "'You can skip PPE since it is already mixed.' || PPE is used when handling chemo",
  "'Hang it, then use body-fluid precautions for 6 hours.' || Precautions last 48 hours"],
  "Only trained staff handle chemotherapy, with PPE (personal protective equipment). Body-fluid precautions are used for 48 hours after chemo, and a port or central line helps reduce extravasation injury.")

q("nadir", "A client who received chemotherapy 9 days ago is told her blood counts are at their lowest. She asks how long recovery takes. Which response is accurate?", [
  "'Counts recover within a few hours.' || Recovery takes another 5-7 days",
  "'Counts stay low for at least 6 months.' || Recovery takes another 5-7 days",
  "*'Counts usually recover over another 5 to 7 days.'",
  "'Counts never recover without a transfusion.' || Counts recover over another 5-7 days"],
  "Nadir, the lowest blood counts, occurs 7-10 days after chemo, with recovery over another 5-7 days.")

q("sideeff", "A 27-year-old newly diagnosed with cancer hopes to have children someday. When should the nurse discuss egg banking?", [
  "After the first round of chemotherapy || Banking is offered before treatment",
  "*Before chemotherapy is started",
  "Once the cancer is in remission || Banking is offered before treatment",
  "Only if fertility changes are noticed || Banking is offered before treatment"],
  "For fertility changes from cancer treatment, the nurse offers sperm or egg banking before treatment begins.")

q("svc", "A client with lung cancer reports that her face looks puffy, her rings feel tight, and she is short of breath at rest. Which complication should the nurse suspect?", [
  "Spinal cord compression || This presents with back pain worse lying down",
  "*Superior vena cava syndrome",
  "Tumor lysis syndrome || This presents with electrolyte changes",
  "Hypercalcemia || This presents with confusion and constipation"],
  "In SVC (superior vena cava) syndrome a tumor compresses the SVC, most often from lung cancer, causing edema of the face, neck and arms and dyspnea. Care includes monitoring ABCs, elevating the HOB, rest, strict I&O and avoiding fluid overload.")

q("scc", "A client with spinal cord compression is receiving steroids and radiation. Which nursing assessment is the priority?", [
  "Daily weights to check fluid status || Weights are emphasized for SIADH",
  "Mouth checks for mucositis || Mucositis care is not the priority here",
  "*Frequent neurologic checks",
  "Telemetry for potassium changes || Telemetry is emphasized for tumor lysis"],
  "Spinal cord compression is treated with surgery, radiation or steroids, with frequent neuro checks. MRI (magnetic resonance imaging) is the gold standard, and intervention within 24 hours helps prevent paralysis.")

q("hypercal", "A client with cancer-related hypercalcemia asks why calcitonin is not being given by itself. Which response is accurate?", [
  "'It works too slowly to make any difference.' || Calcitonin works fast",
  "'It raises calcium instead of lowering it.' || Calcitonin is used to treat hypercalcemia",
  "'It is used only after the calcium is normal.' || It is part of hypercalcemia treatment",
  "*'It works fast, but calcium can rebound if used alone.'"],
  "Hypercalcemia (10.6 or higher) is treated with rapid rehydration, then furosemide, plus bisphosphonates. Calcitonin works fast but is not used alone because of rebound.")

q("tls", "A client at risk for tumor lysis syndrome has kidney impairment and a rising uric acid level. Which medication should the nurse anticipate?", [
  "Potassium chloride || Potassium is already high in tumor lysis",
  "*Rasburicase",
  "Calcium carbonate || Calcium carbonate does not lower uric acid",
  "Filgrastim || Filgrastim raises neutrophil counts"],
  "Tumor lysis syndrome causes high potassium, uric acid and phosphorus with low calcium. Care includes telemetry, IV hydration, a renal diet low in K/phos and allopurinol; rasburicase is used with kidney impairment, and dialysis if needed.")

q("siadh", "A client with small-cell lung cancer and SIADH asks for a large pitcher of water. Which response by the nurse is best?", [
  "'Drink as much water as you can to flush your kidneys.' || SIADH requires fluid restriction",
  "*'Your fluids are limited, since extra water lowers your sodium.'",
  "'Water is fine, but avoid any salty foods today.' || Extra water further dilutes sodium",
  "'Aim for 3 to 4 quarts a day to stay hydrated.' || That is hypercalcemia teaching"],
  "In SIADH (syndrome of inappropriate antidiuretic hormone), excess ADH causes water retention and dilutional hyponatremia; around 110 mEq/L seizures can occur. Care includes fluid restriction, I&O (intake and output) and daily weights.")

q("neutro", "Four clients receiving chemotherapy have new vital signs and labs. Which client meets the criteria for neutropenic fever?", [
  "Temperature 99.8°F with an ANC of 450/mm³ || The temperature is below 101°F",
  "Temperature 101.6°F with an ANC of 1,800/mm³ || The ANC is not below 500",
  "*Temperature 101.2°F with an ANC of 450/mm³",
  "Temperature 100.4°F with an ANC of 2,000/mm³ || Neither criterion is met"],
  "Neutropenic fever is a temperature of 101°F or higher with an ANC (absolute neutrophil count) under 500. Two culture sets are drawn, then antibiotics are started promptly; no rectal temperatures.")
