T = "e2w43"; SET = "20261124"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("variation", "A 68-year-old with BPH (benign prostatic hyperplasia) asks what 'hyperplasia' means. Which explanation by the nurse is accurate?", [
  "'The cells have an abnormal structure that may be precancerous.' || That describes dysplasia",
  "*'There is an increased number of normal cells responding to a stimulus.'",
  "'The cells in the prostate are dying and breaking down.' || That describes necrosis",
  "'A malignant tumor has formed and is spreading.' || Hyperplasia involves normal cells"],
  "Hyperplasia is an increased number of normal cells in response to a stimulus, such as BPH or phenytoin gingival hyperplasia. Dysplasia is abnormal structure that may be precancerous.")

q("benign", "A pathology report describes a tumor with clear borders, a capsule, tightly adherent cells and euploid chromosomes. How should the nurse interpret this?", [
  "Malignant, likely to invade nearby tissue || Malignant cells are irregular and not encapsulated",
  "Malignant, with loosely adherent cells || These cells are described as tightly adherent",
  "*Benign, not expected to metastasize",
  "Precancerous dysplasia that will migrate || These are features of a benign tumor"],
  "Benign tumors have clear borders, are often encapsulated, show tight adherence and euploid chromosomes, and do not metastasize. Malignant cells are irregular, not encapsulated, loosely adherent, aneuploid and can migrate.")

q("carcino", "During which stage of carcinogenesis do hormones or proteins stimulate growth of altered cells?", [
  "Initiation || In initiation, a carcinogen alters DNA",
  "*Promotion",
  "Progression || In progression, the tumor develops its own blood supply",
  "Metastasis || Metastasis is spread after progression"],
  "Carcinogenesis moves from initiation (DNA altered) to promotion (hormones or proteins stimulate growth) to progression (angiogenesis/VEGF) to metastasis.")

q("prevent", "A 22-year-old asks how often she should have cervical cancer screening, as taught in lecture. Which response is accurate?", [
  "'A yearly test starting at age 40.' || Yearly from 40 is the mammogram schedule",
  "'Every 10 years starting at age 45.' || That is the colonoscopy schedule",
  "*'A Pap test every 3 years, starting at age 21.'",
  "'Starting around age 50 with a yearly exam.' || Around 50 applies to PSA/DRE and lung CT screening"],
  "As taught: Pap every 3 years from 21, mammogram yearly at 40, colonoscopy at 45 every 10 years, PSA/DRE around 50, and low-dose CT for smokers around 50.")

q("caution", "A 58-year-old asks the nurse which changes should prompt a cancer check-up. Which are CAUTION warning signs? " + SATA, [
  "*Unusual bleeding or discharge",
  "*A thickening or lump in the breast or elsewhere",
  "Frequent itching of the skin || Itching is not part of CAUTION",
  "*Indigestion or difficulty swallowing",
  "Sudden weight gain || Weight gain is not part of CAUTION"],
  "CAUTION: Change in bowel or bladder habits, A sore that won't heal, Unusual bleeding or discharge, Thickening or lump, Indigestion or difficulty swallowing, Obvious change in a wart or mole, Nagging cough or hoarseness.")

q("tnm", "A client's cancer report lists a TNM (tumor, node, metastasis) stage. The client asks which letter tells whether cancer has spread to distant sites. Which is correct?", [
  "T || T describes primary tumor size and extent",
  "N || N describes regional lymph node involvement",
  "*M",
  "The nuclear grade || Grade is not a letter in TNM"],
  "In TNM staging, T is primary tumor size and extent, N is regional lymph nodes, and M is distant metastasis. Higher numbers are more concerning.")

q("surgery", "A 38-year-old with a BRCA gene mutation and no cancer has both breasts removed to lower her risk. This surgery is classified as:", [
  "Palliative || Palliative surgery relieves symptoms and improves quality of life",
  "Curative || There is no cancer to cure",
  "Diagnostic || The goal is not to diagnose",
  "*Prophylactic"],
  "Prophylactic surgery removes high-risk tissue, such as mastectomy with a BRCA mutation. Palliative surgery relieves obstruction, debulks, reduces pain and improves quality of life.")

q("extrad", "A client is starting external beam radiation. Which effects should the nurse prepare the client to expect? " + SATA, [
  "*Skin dermatitis in the treatment area",
  "Radioactive urine for 48 hours || External beam does not make the client or fluids radioactive",
  "*Fatigue",
  "*Bone marrow suppression",
  "Needing to avoid hugging family || The client is not radioactive"],
  "With external beam radiation the client and body fluids are not radioactive. Expect dermatitis, fatigue and marrow suppression. Keep tattoo markings and use only prescribed unscented lotion.")

q("brachy", "A client has an intracavitary radiation implant. Her daughter, who is 5 months pregnant, arrives to visit. Which action by the nurse is best?", [
  "Let her visit if she wears a lead apron || No pregnant visitors are allowed",
  "*Explain that pregnant visitors can't visit while the implant is in",
  "Allow a brief visit with the door left open || The door stays closed and pregnant visitors are not allowed",
  "Let her sit at the bedside for up to 1 hour || Pregnant visitors are not allowed"],
  "An intracavitary implant is radioactive until removed: private room, door closed, lead apron, about 1 hour/day exposure, no pregnant staff or visitors, and forceps plus a lead container in the room.")

q("chemo", "A client finished surgery for colon cancer and is now scheduled for chemotherapy to treat any remaining cancer. The nurse identifies this timing as:", [
  "Neoadjuvant || Neoadjuvant is given before surgery",
  "*Adjuvant",
  "Prophylactic || Prophylactic refers to removing high-risk tissue",
  "Palliative || Palliative care relieves symptoms"],
  "Adjuvant chemotherapy is given after surgery; neoadjuvant is given before surgery to shrink a tumor. Only trained staff handle chemo, with PPE, and body-fluid precautions last 48 hours after.")

q("nadir", "A client receiving chemotherapy has low RBC (red blood cell) counts. Which medication should the nurse anticipate?", [
  "Filgrastim || Filgrastim increases neutrophils",
  "Pegfilgrastim || Pegfilgrastim increases neutrophils",
  "Dexrazoxane || Dexrazoxane is a cytoprotectant",
  "*Epoetin alfa"],
  "Epoetin alfa and darbepoetin raise RBCs. Filgrastim and pegfilgrastim raise neutrophils. Nadir, the lowest counts, occurs 7-10 days after chemo, with recovery over another 5-7 days.")

q("sideeff", "The nurse teaches a client with chemotherapy-induced mucositis. Which statement by the client needs more teaching?", [
  "'I'll suck on ice chips or ice pops.' || This is correct mucositis care",
  "'I'll rinse my mouth with baking soda.' || This is correct mucositis care",
  "*'I'll rinse with my alcohol mouthwash.'",
  "'I'll do mouth care often each day.' || This is correct mucositis care"],
  "Mucositis care includes ice or ice pops, frequent oral care, baking-soda rinses, and avoiding alcohol mouthwash.")

q("svc", "A client with lung cancer has SVC (superior vena cava) syndrome with facial and arm edema. Which nursing plan is appropriate?", [
  "Lay flat and give a rapid IV (intravenous) fluid bolus || Elevate the HOB and avoid fluid overload",
  "Apply warm compresses to the neck and face || This is not part of SVC syndrome care",
  "*Monitor ABCs, strict I&O (intake and output), avoid fluid overload",
  "Encourage walking in the hall several times daily || Rest is encouraged"],
  "In SVC syndrome a tumor compresses the SVC, most often from lung cancer. Care includes monitoring ABCs, elevating the HOB, rest, strict I&O and avoiding fluid overload.")

q("scc", "A client with metastatic cancer has new back pain that worsens when lying down, and spinal cord compression is suspected. Within what time frame should treatment begin to help prevent paralysis?", [
  "Within 1 week || This delay risks paralysis",
  "*Within 24 hours",
  "Within 72 hours || The goal is within 24 hours",
  "At the next routine visit || This is a red flag needing prompt action"],
  "Suspected spinal cord compression needs intervention within 24 hours to prevent paralysis. MRI is the gold standard; treatment is surgery, radiation or steroids, with frequent neuro checks.")

q("hypercal", "A client with cancer-related hypercalcemia is being discharged. Which instructions should the nurse include? " + SATA, [
  "*Drink 3-4 quarts of fluid a day if allowed",
  "Take calcium antacids for indigestion || Avoid calcium vitamins and antacids",
  "*Eat a high-fiber diet",
  "Stay on bed rest until calcium is normal || Ambulate if safe",
  "*Walk if safe and follow fall precautions"],
  "Hypercalcemia teaching: 3-4 qt/day oral fluids if allowed, I&O, high fiber, ambulate if safe, fall precautions, and avoid calcium vitamins and antacids.")

q("tls", "A client is receiving chemotherapy for a large tumor and is at risk for tumor lysis syndrome. Which nursing actions are appropriate? " + SATA, [
  "*Place the client on telemetry",
  "Give potassium supplements || Potassium rises in tumor lysis syndrome",
  "*Give IV (intravenous) hydration as ordered",
  "Encourage a high-phosphorus diet || Phosphorus rises; the diet is low in K/phos",
  "*Provide a renal diet low in potassium and phosphorus"],
  "In tumor lysis syndrome dying cells spill potassium, uric acid and phosphorus, with low calcium. Care includes telemetry, IV hydration, a renal diet low in K/phos, allopurinol, rasburicase with kidney impairment, and dialysis if needed.")

q("siadh", "A client with small-cell lung cancer is diagnosed with SIADH (syndrome of inappropriate antidiuretic hormone). Which order should the nurse anticipate?", [
  "*Fluid restriction with daily weights",
  "Encourage 3-4 quarts of oral fluid daily || Extra fluid worsens dilutional hyponatremia",
  "Allopurinol to lower uric acid || Allopurinol is used in tumor lysis syndrome",
  "A high-fiber diet with ambulation || This is hypercalcemia teaching"],
  "In SIADH excess ADH causes water retention and dilutional hyponatremia; around 110 mEq/L seizures can occur. Care includes fluid restriction, I&O and daily weights.")

q("neutro", "A client with neutropenia from chemotherapy has several visitors. Which visitor action requires the nurse to intervene?", [
  "Washing hands before entering the room || Handwashing is encouraged",
  "Waiting outside because of a cold || Avoiding sick people is correct",
  "*Bringing in a vase of fresh flowers",
  "Telling the nurse the client feels feverish || Fever should be reported immediately"],
  "Neutropenic teaching: frequent handwashing, avoid crowds, sick people, fresh fruit and flowers, and report fever immediately. Use oral or axillary temperatures only.")
