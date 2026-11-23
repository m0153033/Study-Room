T = "e5slera"; SET = "20261123"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# big
q("big", "A nursing student caring for two clients, one with RA (rheumatoid arthritis) and one with SLE (systemic lupus erythematosus), asks what the two diseases have in common. Which response by the nurse is accurate?",
  ["Both are acute illnesses that resolve fully once treatment is finished || Both are chronic, not acute or curable",
   "Both are degenerative wear-and-tear joint conditions of older adults || Neither is wear and tear; both are autoimmune",
   "*Both are chronic autoimmune diseases that flare and remit",
   "Both are infections of the joints that respond well to antibiotics || Neither is an infection; both are autoimmune"],
  "RA and SLE are both chronic systemic autoimmune diseases with flares and remissions. RA mainly attacks the synovium; SLE deposits immune complexes in many organs.")

# rapatho (HI x2)
q("rapatho", "A 46-year-old client newly diagnosed with RA (rheumatoid arthritis) asks what is happening inside her finger joints. Which explanation by the nurse is correct?",
  ["'The cartilage is wearing down from years of use.' || That describes osteoarthritis, not RA",
   "*'Your immune system is inflaming the synovial lining of the joint.'",
   "'Uric acid crystals are collecting in the joint space.' || Crystal deposits are not the RA mechanism",
   "'Bacteria have entered the joint and are causing infection.' || RA is autoimmune, not infectious"],
  "RA primarily targets the synovial lining of the joints; it is an inflammatory autoimmune disease, unlike osteoarthritis, which is degenerative wear and tear.")
q("rapatho", "A 58-year-old client with long-standing RA (rheumatoid arthritis) asks why his wrist has become stiff and hard to move. The nurse explains that inflamed synovial tissue has thickened and invaded the joint. What is this tissue called, and what does it cause?",
  ["Heberden's nodes, which form bony enlargements of the distal joints || Heberden's nodes are not the RA tissue process",
   "Malar tissue, which forms a red rash over the skin of the joint || Malar refers to the SLE facial rash",
   "Rheumatoid nodules, which fill the joint space with fluid and swell it || Nodules are a systemic finding, not the invading tissue",
   "*Pannus, which erodes cartilage and bone and can immobilize the joint"],
  "Pannus is thickened, inflamed synovial tissue that invades and erodes cartilage and bone; resulting scar tissue can immobilize the joint.")

# rarisk
q("rarisk", "A nurse is reviewing health histories at a community clinic. Which client has a risk factor for RA (rheumatoid arthritis) that could be modified?",
  ["A 40-year-old woman whose mother has RA || Family history is not modifiable",
   "A 35-year-old woman with a high-purine diet || A high-purine diet is not an RA risk factor",
   "*A 44-year-old man who smokes daily",
   "A 29-year-old woman with no other risk factors || Female sex is not modifiable"],
  "Risk factors for RA include genetics/family history, female sex, smoking and certain environmental exposures. Smoking is the one that can be changed; not every risk can be prevented.")

# ramani
q("ramani", "A nurse is assessing the hands of a 52-year-old client with advanced RA (rheumatoid arthritis). Which findings are consistent with RA deformities? " + SATA,
  ["*Fingers drifting toward the little-finger side",
   "*PIP (proximal interphalangeal) hyperextension with distal joint flexion",
   "Bony nodes on the distal finger joints only || Distal bony nodes (Heberden's nodes) are not RA deformities",
   "*Boutonnière deformity of a finger",
   "Involvement limited to a single knee || RA is symmetric and typically starts in the hands, wrists and feet"],
  "Later RA can cause ulnar deviation (drift toward the little finger), swan-neck deformity (PIP hyperextension with distal flexion) and boutonnière deformity, which can limit self-care and mobility.")

# raextra
q("raextra", "A 61-year-old client with RA (rheumatoid arthritis) has an enlarged spleen, a low neutrophil count, anemia, weight loss and a low-grade fever. Which condition should the nurse recognize?",
  ["Sjögren syndrome || Sjögren syndrome presents with dry eyes and mouth",
   "*Felty syndrome",
   "Lupus nephritis || That is SLE kidney involvement with proteinuria and hypertension",
   "Raynaud phenomenon || Raynaud is listed with SLE, not this cluster"],
  "Felty syndrome is an extra-articular RA manifestation made up of splenomegaly, neutropenia and anemia, along with weight loss and low-grade fever.")

# radx (HI x2)
q("radx", "A 39-year-old client's results show a positive RF (rheumatoid factor). She asks, 'Does this mean I definitely have RA?' Which response by the nurse is best?",
  ["'Yes, a positive RF result by itself is enough to confirm RA.' || No single test confirms RA",
   "'No, only an x-ray of your hands can confirm the diagnosis.' || Imaging alone does not confirm RA either",
   "*'No; no single test confirms RA, so several findings are combined.'",
   "'No, a positive ANA (antinuclear antibody) is what confirms RA.' || ANA does not confirm RA"],
  "RA diagnosis combines history, exam, joint pattern, inflammatory markers, antibodies and imaging. A positive RF alone does not confirm RA.")
q("radx", "The nurse is reviewing labs for a client being evaluated for RA (rheumatoid arthritis). Which result is the MOST specific antibody for RA, and which results (ESR, erythrocyte sedimentation rate; CRP, C-reactive protein) track disease activity?",
  ["Anti-dsDNA (anti-double-stranded DNA) is most specific; C3/C4 complement tracks activity || These are SLE markers",
   "ANA (antinuclear antibody) is most specific; urine protein tracks activity || ANA and urine protein relate to SLE",
   "RF (rheumatoid factor) is most specific; the CBC (complete blood count) tracks activity || Anti-CCP is more specific than RF; CBC checks anemia",
   "*Anti-CCP (anti-cyclic citrullinated peptide) is most specific; ESR and CRP track activity"],
  "Anti-CCP is the most specific antibody for RA. ESR and CRP show inflammation and track disease activity; CBC checks for anemia.")

# ranpharm (HI x2)
q("ranpharm", "A 50-year-old client with RA (rheumatoid arthritis) calls the clinic reporting that her knees are acutely hot, swollen and very painful today. Which instruction should the nurse give?",
  ["'Soak in a hot tub to loosen the joints.' || Heat is for stiffness, not acutely inflamed joints",
   "'Go for a brisk run to keep the joints moving.' || High-impact exercise during a flare is harmful",
   "*'Apply cold to the swollen joints and rest them.'",
   "'Keep the knees permanently splinted and avoid all movement.' || Permanent immobilization is not recommended"],
  "Cold is used for acutely swollen, hot, painful joints, and rest is appropriate during active inflammation.")
q("ranpharm", "A nurse is teaching a 63-year-old client with RA (rheumatoid arthritis) who has morning stiffness but no current flare. Which client statement shows the teaching was understood?",
  ["'I should stay in bed all morning until the stiffness goes away.' || Complete bed rest is not advised",
   "'I'll put ice packs on my hands every hour when I wake up.' || Cold is for acute flares, not stiffness",
   "'I should avoid moving my joints so they don't get damaged.' || Activity and range of motion are encouraged when tolerated",
   "*'A warm tub bath in the morning should help loosen my joints.'"],
  "Moist heat, such as a warm tub bath, relieves stiffness. Low-impact exercise and range of motion are encouraged when tolerated.")

# rameds (HI x2)
q("rameds", "A 47-year-old client with RA (rheumatoid arthritis) is starting methotrexate. Which statements by the client indicate correct understanding? " + SATA,
  ["*'I'll call if I get mouth sores or bruise easily.'",
   "*'I need regular blood work to check my blood counts and liver.'",
   "'I'll call the provider if my joint stiffness gets a little better.' || Mild improvement is the expected effect, not a reason to call",
   "*'A new cough or shortness of breath should be reported.'",
   "'This drug only relieves pain; it won't change the disease.' || Methotrexate is a disease-modifying drug"],
  "Methotrexate is a common first-line DMARD (disease-modifying antirheumatic drug). Report mouth ulcers, easy bruising, cough or shortness of breath and fever; monitor CBC, liver tests and platelets.")
q("rameds", "A client with RA (rheumatoid arthritis) has taken ibuprofen for several months and asks why the provider is adding a DMARD (disease-modifying antirheumatic drug). Which response by the nurse is best?",
  ["'Ibuprofen stops joint damage, but it has too many side effects to keep using.' || NSAIDs do not stop joint destruction",
   "*'Ibuprofen eases pain and swelling, but it doesn't slow the disease.'",
   "'The DMARD will cure your RA, so you can soon stop all of your medicines.' || DMARDs do not cure RA",
   "'The DMARD replaces your need for physical and occupational therapy.' || DMARDs do not replace therapy"],
  "NSAIDs (nonsteroidal anti-inflammatory drugs) relieve pain and inflammation but don't prevent disease progression. DMARDs aim to limit inflammation and joint destruction.")

# biologic
q("biologic", "A 55-year-old client with RA (rheumatoid arthritis) is starting etanercept. Which statement by the client requires further teaching?",
  ["'This medicine suppresses my immune system.' || Correct; biologics suppress immunity",
   "'I should call if I develop a fever.' || Correct; report signs of infection",
   "*'Since this is a biologic, I won't need any lab monitoring.'",
   "'This drug is meant to slow my disease, not just ease pain.' || Correct; DMARDs slow progression"],
  "Etanercept is a DMARD that slows disease progression. Biologics suppress the immune system, so clients report fever or infection signs and should not skip lab monitoring.")

# ranurse
q("ranurse", "A 66-year-old client with RA (rheumatoid arthritis) lives alone and reports difficulty opening jars and buttoning shirts. Which nursing action is most appropriate?",
  ["Teach the client to carry heavy grocery bags with the fingers instead || Heavy loads on the fingers stress joints",
   "Assess only the client's visual acuity before discharge || Assessment should focus on pain, mobility and ADLs",
   "*Coordinate occupational therapy for adaptive equipment",
   "Advise the client to avoid all activity to protect the joints || Low-impact movement is encouraged"],
  "RA nursing care includes assessing ADLs (activities of daily living), coordinating physical and occupational therapy, and teaching joint protection, energy conservation and adaptive equipment.")

# slepatho
q("slepatho", "A 27-year-old client newly diagnosed with SLE (systemic lupus erythematosus) asks what causes the damage in her body. Which explanation by the nurse is accurate?",
  ["'Your cartilage is wearing down faster than normal with age.' || That describes degenerative joint disease",
   "'A bacterial infection has spread through your joints.' || SLE is autoimmune, not bacterial",
   "*'Autoantibodies form immune complexes that inflame your tissues.'",
   "'Uric acid crystals are building up in your organs and joints.' || Crystal deposition is not the SLE mechanism"],
  "In SLE, loss of self-tolerance creates autoantibodies; immune complexes deposit in tissues such as the kidneys, skin, joints and blood vessels and cause inflammation.")

# sletrig (HI x2)
q("sletrig", "A 24-year-old client with SLE (systemic lupus erythematosus) asks what might set off her lupus flares. Which factors should the nurse include? " + SATA,
  ["*UV (ultraviolet) light from the sun or tanning beds",
   "*Infections",
   "Cold weather by itself || Cold weather alone is not a listed trigger",
   "*Estrogen",
   "*Certain medications"],
  "SLE results from genetics plus environmental triggers (UV light, infections, certain medications) and hormones (estrogen). Teach sun protection and avoiding tanning beds.")
q("sletrig", "A nurse is preparing a teaching session on SLE (systemic lupus erythematosus) genetics. Which genetic factor should be included?",
  ["HER2 (human epidermal growth factor receptor 2) overexpression || Not an SLE genetic factor",
   "Lynch syndrome inheritance || Not an SLE genetic factor",
   "*HLA-DR2 and HLA-DR3 (human leukocyte antigen) variants",
   "CCR5 (C-C chemokine receptor type 5) tropism || Not an SLE genetic factor"],
  "HLA-DR2 and HLA-DR3 variants are the genetic factors linked to SLE in the lecture, along with environmental and hormonal triggers.")

# ravsle (HI x2)
q("ravsle", "A 42-year-old client has hand x-rays showing joint-space narrowing, erosions and deformity. Which disease process best explains these findings?",
  ["*RA (rheumatoid arthritis), with pannus eroding cartilage and bone",
   "SLE (systemic lupus erythematosus), with immune complexes eroding the joints || SLE joint disease is not usually erosive",
   "SLE, with photosensitivity damaging the joints || Photosensitivity is a skin finding",
   "RA, with immune complexes damaging the kidneys || Kidney immune-complex damage fits SLE"],
  "RA attacks the synovial membrane and forms pannus that erodes cartilage and bone, causing narrowing, erosions and deformity. SLE joint disease isn't usually erosive.")
q("ravsle", "A nurse is comparing RA (rheumatoid arthritis) and SLE (systemic lupus erythematosus). Which statements are accurate? " + SATA,
  ["*RA mainly attacks the synovial membrane of the joints",
   "*SLE immune complexes can inflame the skin, kidneys, joints and blood vessels",
   "RA is triggered mainly by uric acid crystals || RA is autoimmune synovitis",
   "*SLE joint disease is usually less erosive than RA",
   "SLE damage is limited to the synovium || SLE is multisystem"],
  "RA forms pannus from the synovium that erodes cartilage and bone; SLE forms autoantibodies and immune complexes that inflame many organs. SLE joint disease isn't usually erosive like RA.")

# sleskin (HI x2)
q("sleskin", "A nurse is assessing a 31-year-old client with SLE (systemic lupus erythematosus). Which finding is characteristic of SLE?",
  ["A stripe of vesicles along one dermatome || That is not an SLE finding",
   "*A red rash across both cheeks and the bridge of the nose",
   "Koplik spots inside the cheeks || Koplik spots are not an SLE finding",
   "A rash that starts at the hairline and spreads downward || That is not an SLE finding"],
  "The red malar (butterfly) rash across the cheeks and nasal bridge is characteristic of SLE, though not every client has it.")
q("sleskin", "A 35-year-old client with SLE (systemic lupus erythematosus) is planning a summer of outdoor gardening. Which statement by the client indicates a need for further teaching?",
  ["'I'll use sun protection whenever I'm outside in the garden.' || Correct; sun protection prevents flares",
   "'Too much sun exposure could trigger one of my flares.' || Correct; photosensitivity is common",
   "'I'll avoid using tanning beds, even in the winter.' || Correct; tanning beds are a UV source",
   "*'Extra sun will help clear up my facial rash.'"],
  "Photosensitivity is common in SLE; clients should avoid excess sun and use sun protection to prevent flares. Increased sun exposure is not appropriate advice.")

# sleorgan
q("sleorgan", "A 29-year-old client with SLE (systemic lupus erythematosus) is being seen at a routine visit. Which new finding should the nurse report promptly?",
  ["Mild hair thinning that has been unchanged for months || Stable, long-standing thinning is not urgent",
   "*Sharp chest pain that worsens with breathing",
   "Fatigue after a busy work week || Not a new organ-involvement sign",
   "A stable, faded malar rash || A stable rash is not urgent"],
  "Pleuritic chest pain can signal pleuritis or pericarditis, which are SLE organ involvement and need prompt reporting, as do seizures, psychosis and edema with rising BP.")

# slerenal (HI x2)
q("slerenal", "A 33-year-old client with SLE (systemic lupus erythematosus) reports new ankle swelling. Which additional findings would most suggest lupus nephritis? " + SATA,
  ["*Blood in the urine",
   "*Rising serum creatinine",
   "Increased urine concentration alone || Not a listed finding of lupus nephritis",
   "*BP (blood pressure) of 168/98",
   "*Protein in the urine"],
  "Lupus nephritis presents with proteinuria, hematuria, edema, hypertension and rising creatinine; it can progress to kidney failure needing dialysis or transplant.")
q("slerenal", "A nurse is caring for four clients with SLE (systemic lupus erythematosus). Which client should the nurse report to the provider FIRST?",
  ["A client with joint aches who is asking about warm baths || Joint aches are not the red flag",
   "A client with a malar rash who wants sunscreen advice || A teaching need, not urgent",
   "*A client with new edema, proteinuria and hypertension",
   "A client on hydroxychloroquine who is due for a routine eye exam || Routine follow-up, not urgent"],
  "Edema, hypertension and proteinuria suggest lupus nephritis, the SLE red flag that needs prompt evaluation; renal function and vital signs are the priority monitoring.")

# sledx (HI x2)
q("sledx", "A 26-year-old client's ANA (antinuclear antibody) is positive and she asks if this means she has SLE (systemic lupus erythematosus). Which response by the nurse is correct?",
  ["'Yes, a positive ANA confirms lupus every time it is checked.' || ANA is not diagnostic by itself",
   "'No, a positive ANA means you have RA (rheumatoid arthritis).' || ANA is not specific for RA",
   "*'ANA is often positive in lupus but can't diagnose it alone.'",
   "'No, ANA is always negative in people who have lupus.' || ANA is often positive in SLE"],
  "ANA is often positive in SLE but not diagnostic alone. Anti-dsDNA (anti-double-stranded DNA) and anti-Smith are more specific.")
q("sledx", "A client with SLE (systemic lupus erythematosus) is being evaluated for disease activity and kidney involvement. Which results support active disease or nephritis? " + SATA,
  ["*Positive anti-dsDNA (anti-double-stranded DNA)",
   "*Decreasing C3/C4 complement levels",
   "Positive anti-CCP (anti-cyclic citrullinated peptide) || Anti-CCP is the RA-specific antibody",
   "*Protein on urinalysis",
   "Rising complement levels || Complement may decrease, not rise, in active SLE"],
  "Anti-dsDNA is more specific for SLE and helps assess activity; complement may drop during active disease. Urinalysis for protein, creatinine and BUN check kidney involvement, and a kidney biopsy confirms lupus nephritis.")

# slemeds (HI x2)
q("slemeds", "A 30-year-old client with SLE (systemic lupus erythematosus) is starting hydroxychloroquine. Which instruction is the priority?",
  ["*'Schedule regular eye exams while taking this drug.'",
   "'Expect your urine to turn red while taking this drug.' || Not a listed effect",
   "'Stop the drug whenever you notice a lupus flare.' || It reduces flare frequency and should not be stopped",
   "'Limit your fluid intake while you are taking it.' || Not a listed instruction"],
  "Hydroxychloroquine can cause retinal changes, so vision exams are needed about every 6 months; it reduces the frequency of SLE flares.")
q("slemeds", "A 23-year-old client with SLE (systemic lupus erythematosus) asks about birth control. Her provider advised avoiding estrogen-containing oral contraceptives. Which explanation by the nurse is correct?",
  ["'Estrogen causes RA (rheumatoid arthritis).' || Not the reason given",
   "'Estrogen makes your ANA (antinuclear antibody) drop to zero.' || Not the reason given",
   "'Estrogen's only effect is to make you sensitive to the sun.' || Not the reason given",
   "*'Estrogen can trigger an acute lupus episode.'"],
  "Estrogen is a hormonal trigger of SLE and can trigger an acute episode, so estrogen-containing oral contraceptives may be avoided.")

# slenurse (HI x2)
q("slenurse", "A 37-year-old client with SLE (systemic lupus erythematosus) takes azathioprine and reports a temperature of 100.6°F (38.1°C). What is the nurse's best action?",
  ["Tell the client a low fever can be ignored || Fever must be reported on immunosuppression",
   "*Report the fever promptly to the provider",
   "Advise the client to double the steroid dose || Never change doses without an order",
   "Encourage the client to rest in the sun || Sun exposure can trigger flares"],
  "Immunosuppressive drugs raise infection risk, so fever in a client with SLE on immunosuppression is reported promptly and infection precautions are reinforced.")
q("slenurse", "A nurse is reinforcing flare-prevention teaching with a 28-year-old client with SLE (systemic lupus erythematosus). Which client statements show understanding? " + SATA,
  ["*'I'll pace my activities and get enough rest.'",
   "'Once I feel well, I can stop my medicines.' || Treatment adherence prevents flares",
   "*'I'll keep my lab follow-up appointments.'",
   "*'Learning stress management can help prevent flares.'",
   "'I'll only check my blood pressure if I have a headache.' || BP, weight and edema should be monitored routinely"],
  "SLE flare prevention includes sun protection, rest and pacing, stress management, treatment adherence and keeping lab follow-ups; monitor BP, weight, edema and urine findings.")
