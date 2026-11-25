T = "e5slera"; SET = "20261125"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("big", "A nurse is reviewing RA and SLE with a study group. Which statements are accurate? " + SATA,
 ["*Both are chronic systemic autoimmune diseases",
  "Both are degenerative wear-and-tear diseases || Both are autoimmune, not wear and tear.",
  "*Both have periods of flares and remissions",
  "SLE stays limited to the skin over time || SLE can affect many organs.",
  "*RA mainly attacks the synovium of the joints"],
 "RA and SLE are chronic systemic autoimmune diseases with flares and remissions; RA mainly attacks the synovium, while SLE affects many organs.")

q("rapatho", "A 49-year-old client with RA says, 'My dad has osteoarthritis, so we must have the same problem.' Which response by the nurse is accurate?",
 ["*'No, RA inflames the joint lining; OA is wear and tear.'",
  "'Yes, both are autoimmune attacks on the joint lining.' || OA is degenerative, not autoimmune.",
  "'Yes, both come from cartilage wearing down with use.' || That describes osteoarthritis only.",
  "'No, RA is caused by uric acid crystals in the joint.' || RA targets the synovial lining."],
 "RA is an inflammatory autoimmune disease that targets the synovial lining; OA is degenerative wear and tear.")

q("rapatho", "A nurse is explaining joint damage in RA to a newly diagnosed client. Which statements should the nurse include? " + SATA,
 ["*'The synovial lining of the joint is the main target.'",
  "'The damage starts with cartilage wearing thin from use.' || That is osteoarthritis.",
  "*'Inflamed synovium can thicken into tissue called pannus.'",
  "*'Pannus can erode cartilage and bone, and scarring can stiffen the joint.'",
  "'Pannus is a firm nodule that forms under the skin.' || Pannus is thickened synovial tissue."],
 "RA targets the synovium; pannus is thickened, inflamed synovial tissue that erodes cartilage and bone, and scar tissue can immobilize the joint.")

q("rarisk", "A 74-year-old client has new joint pain and stiffness, and RA is suspected. The client's daughter asks why the diagnosis is taking time. Which response is best?",
 ["'Older adults cannot develop RA, so other causes are being checked.' || RA can occur in older adults.",
  "*'In older adults, RA can be hard to tell apart from osteoarthritis.'",
  "'RA has no symptoms in older adults, so labs must be repeated.' || Findings are similar at any age.",
  "'Lab results are never abnormal in older adults with RA.' || Labs are not always normal."],
 "RA can be hard to diagnose in older adults because it can be difficult to tell apart from osteoarthritis.")

q("ramani", "While assessing a 59-year-old client with long-standing RA, the nurse notes the fingers drift toward the little-finger side. How should the nurse document this finding?",
 ["Swan-neck deformity || That is PIP hyperextension with distal flexion.",
  "Heberden's nodes || Bony distal nodes are not the RA pattern.",
  "Rheumatoid nodule || A nodule is a lump under the skin, not a drift.",
  "*Ulnar deviation"],
 "Later RA can cause ulnar deviation (drift toward the little finger), swan-neck and boutonnière deformities, which can limit self-care.")

q("raextra", "A 48-year-old client with RA asks why she has been tired, has lost weight and was told she is anemic. Which response by the nurse is accurate?",
 ["'These are side effects of cold packs on your joints.' || Not linked to cold therapy.",
  "'These problems mean your RA has changed into lupus.' || RA doesn't turn into SLE.",
  "*'RA is systemic, so fatigue, weight loss and anemia can occur beyond the joints.'",
  "'These problems are never related to RA and need a separate workup.' || They are RA systemic findings."],
 "RA systemic findings include fatigue, low-grade fever, weight loss, rheumatoid nodules, anemia and dry eyes and mouth.")

q("radx", "A client with RA is being followed in the clinic. Which lab results does the nurse trend to track how active the inflammation is?",
 ["Anti-dsDNA and C3/C4 complement || These are SLE tests.",
  "*ESR and CRP",
  "Anti-CCP alone || It is the most specific antibody, not the activity tracker.",
  "ANA alone || ANA is not used to track RA activity."],
 "ESR and CRP show inflammation and track RA disease activity; anti-CCP is the most specific RA antibody.")

q("radx", "A nurse is teaching a client about tests used in the RA workup. Which statements are accurate? " + SATA,
 ["*Anti-CCP is the most specific antibody for RA",
  "A positive RF by itself confirms RA || No single test confirms RA.",
  "*Imaging can show changes in the joints",
  "*A CBC checks for anemia",
  "Anti-dsDNA is the main antibody for RA || Anti-dsDNA is used for SLE."],
 "No single test confirms RA; anti-CCP is most specific, RF is also used, ESR/CRP track activity, CBC checks for anemia and imaging shows joint changes.")

q("ranpharm", "A 62-year-old client with RA has morning stiffness but no flare and plans to put ice on her hands every morning. Which response by the nurse is best?",
 ["'Ice every hour is the best way to loosen stiff joints.' || Heat relieves stiffness.",
  "*'Try a warm bath instead; save cold for hot, swollen joints.'",
  "'Stay in bed until the stiffness goes away on its own.' || Low-impact movement is encouraged.",
  "'Avoid moving your hands at all until the stiffness fades.' || ROM when tolerated is encouraged."],
 "Moist heat such as a warm tub bath relieves stiffness; cold is used for acutely swollen, hot, painful joints.")

q("ranpharm", "A nurse is planning care for a client with RA between flares. Which nonpharmacologic measures are appropriate? " + SATA,
 ["*Low-impact exercise and range of motion as tolerated",
  "Complete bed rest to protect the joints || Regular activity is encouraged between flares.",
  "*Referral to physical and occupational therapy",
  "*Splints and assistive devices as needed",
  "High-impact running to build joint strength || Exercise should be low-impact."],
 "RA comfort measures include low-impact exercise and ROM, rest during active inflammation, splints and assistive devices, and PT/OT.")

q("rameds", "A 53-year-old client with RA has taken methotrexate for 6 months. Which monitoring should the nurse expect to be ordered?",
 ["Eye exams about every 6 months || That is for hydroxychloroquine.",
  "Hearing tests at each visit || Not listed for methotrexate.",
  "Serum lipase levels only || Not listed for methotrexate.",
  "*CBC, liver tests and platelets"],
 "Methotrexate is a common first-line DMARD; monitor CBC, liver tests and platelets and watch for infection.")

q("rameds", "A nurse teaches a client with RA about his medications. Which statement by the client indicates a need for further teaching?",
 ["'Ibuprofen helps the pain but won't slow my disease.' || Accurate; NSAIDs don't stop progression.",
  "'Methotrexate is meant to limit joint damage over time.' || Accurate; DMARDs limit joint destruction.",
  "*'Once my joints feel better, I can just stop my prednisone.'",
  "'Long-term prednisone can weaken my bones.' || Accurate; it can cause osteoporosis."],
 "Corticosteroids should not be stopped abruptly; long-term use can cause osteoporosis, infection, high glucose and high BP.")

q("biologic", "A 50-year-old client with RA is starting a JAK inhibitor and asks how it differs from adalimumab. Which response by the nurse is accurate?",
 ["*'Your drug blocks the JAK enzyme; adalimumab binds TNF.'",
  "'Your drug binds TNF; adalimumab blocks the JAK enzyme.' || Reversed; adalimumab binds TNF.",
  "'Both drugs work by killing bacteria in the joint.' || Neither is an antibiotic.",
  "'Neither drug affects your immune system.' || Both suppress the immune system."],
 "Adalimumab and infliximab bind TNF; JAK inhibitors block the JAK enzyme; all suppress the immune system, so report fever or infection.")

q("ranurse", "A nurse has taught joint protection and energy conservation to a 67-year-old client with RA. Which client statements show understanding? " + SATA,
 ["*'I'll use adaptive equipment to open jars.'",
  "'I'll carry my grocery bags with my fingers.' || Heavy loads on the fingers stress the joints.",
  "*'I'll plan rest breaks between chores.'",
  "*'I'll keep moving with low-impact activity.'",
  "'I'll stop all activity so my joints don't wear out.' || Low-impact movement is encouraged."],
 "RA teaching includes energy conservation, joint protection, adaptive equipment and low-impact movement.")

q("slepatho", "A nursing student asks what goes wrong in the immune system of a client with SLE. Which explanation by the nurse is accurate?",
 ["'Bacteria invade the joints and then the organs.' || SLE is autoimmune, not an infection.",
  "'Cartilage wears down faster than normal with age.' || That describes osteoarthritis.",
  "'Uric acid crystals build up inside the organs.' || That is not the SLE mechanism.",
  "*'The body loses self-tolerance and makes autoantibodies.'"],
 "In SLE, loss of self-tolerance creates autoantibodies; immune complexes deposit in tissues and cause inflammation.")

q("sletrig", "A 25-year-old client newly diagnosed with SLE asks, 'Why did I get lupus?' Which response by the nurse is accurate?",
 ["'Lupus comes only from your genes; nothing else plays a part.' || Environment and hormones also play a role.",
  "*'Genes like HLA-DR2 and HLA-DR3 plus triggers such as UV light.'",
  "'Lupus is caused by exposure to cold weather by itself.' || Cold weather alone is not a listed trigger.",
  "'Lupus is caused by eating a high-purine diet.' || Not a listed SLE trigger."],
 "SLE results from genetics (HLA-DR2, HLA-DR3 variants) plus environmental triggers (UV light, infections, certain medications) and hormones (estrogen).")

q("sletrig", "A nurse reviews SLE triggers with a client. Which client statement needs correction?",
 ["'An infection could set off a flare.' || Accurate; infections are triggers.",
  "'Estrogen can act as a trigger for lupus.' || Accurate; estrogen is a hormonal trigger.",
  "'Some medicines can trigger my lupus.' || Accurate; certain medications are triggers.",
  "*'Lupus is genetic, so the sun can't affect it.'"],
 "Genetics plus environment (UV light, infections, certain medications) and hormones (estrogen) drive SLE; teach sun protection and avoiding tanning beds.")

q("ravsle", "A 30-year-old client with SLE and joint pain says, 'My aunt's RA bent her fingers out of shape. Will lupus do that too?' Which response by the nurse is best?",
 ["'Yes, lupus erodes the joints even more than RA does.' || SLE joint disease is less erosive.",
  "'Lupus never affects the joints at all.' || SLE can cause arthralgia and arthritis.",
  "*'Lupus joint disease usually isn't erosive the way RA is.'",
  "'Lupus forms pannus that destroys the joint lining.' || Pannus is an RA process."],
 "RA forms pannus that erodes cartilage and bone; SLE joint disease isn't usually erosive like RA.")

q("ravsle", "Which disease process describes SLE rather than RA?",
 ["Synovium thickens into pannus that erodes cartilage || This is RA.",
  "*Immune complexes deposit in the kidneys and vessels",
  "Joint damage shows narrowing, erosions and deformity || This points to RA.",
  "The synovial membrane is the main and only target || This is RA."],
 "SLE forms autoantibodies and immune complexes that inflame many organs; RA attacks the synovial membrane and forms pannus.")

q("sleskin", "While assessing a 36-year-old client with SLE, the nurse finds sores on the roof of the mouth. How should the nurse interpret this finding?",
 ["*Oral ulcers are a known mucosal sign of SLE",
  "These are Koplik spots seen with lupus || Koplik spots are not an SLE finding.",
  "Mouth sores are unrelated to lupus || Oral or nasal ulcers occur in SLE.",
  "This is an RA finding, not an SLE finding || Oral ulcers are listed for SLE."],
 "SLE skin and mucosal findings include malar rash, photosensitivity, discoid lesions, alopecia and oral or nasal ulcers.")

q("sleskin", "A 27-year-old client with SLE is planning a week at the beach. Which plans are appropriate? " + SATA,
 ["*Using sun protection whenever outdoors",
  "Spending extra time in the sun to fade the rash || More sun can trigger a flare.",
  "*Limiting time spent in direct sun",
  "Using a tanning bed first to build a base || Tanning beds should be avoided.",
  "*Knowing that sun exposure can trigger a flare"],
 "Photosensitivity is common in SLE; avoid excess sun, use sun protection and avoid tanning beds to prevent flares.")

q("sleorgan", "The partner of a 41-year-old client with SLE reports that the client has been forgetful and moody for 2 weeks. Which action by the nurse is best?",
 ["Explain that moodiness is just stress and needs no follow-up || New neuro changes need assessment.",
  "Encourage more time in the sun to improve mood || Sun can trigger flares.",
  "*Assess further and report the new cognitive and mood changes",
  "Explain that this is a sign of RA, not lupus || SLE can affect the nervous system."],
 "SLE nervous system findings include headache, seizures and cognitive or mood changes; assess for new neurologic symptoms.")

q("slerenal", "A nurse is caring for a client in an SLE flare. Which finding is the most concerning?",
 ["*New hematuria and rising creatinine",
  "Aching and stiffness in both knees || Joint pain is less urgent than kidney signs.",
  "A faded, stable malar rash || Not an organ-threatening finding.",
  "Mild fatigue after a long day || Less urgent than kidney signs."],
 "Lupus nephritis (proteinuria, hematuria, edema, hypertension, rising creatinine) is the SLE red flag; renal function and vital signs are priority monitoring.")

q("slerenal", "A nurse teaches a client with SLE about warning signs of lupus nephritis. Which client statement shows understanding?",
 ["'Kidney problems in lupus always clear up on their own.' || It can progress to kidney failure.",
  "*'I'll report new swelling or high blood pressure readings at home.'",
  "'Only my joint pain needs to be reported to the clinic.' || Kidney signs are the red flag.",
  "'Concentrated urine alone means my kidneys are failing.' || Not a listed nephritis sign."],
 "Lupus nephritis presents with proteinuria, hematuria, edema, hypertension and rising creatinine and needs prompt evaluation.")

q("sledx", "A client with SLE has a positive anti-dsDNA, and her C3/C4 complement levels have dropped over 3 months. How should the nurse interpret these results?",
 ["The results show SLE is in remission || Falling complement suggests active disease.",
  "*The results suggest active SLE disease",
  "The results confirm lupus nephritis || A kidney biopsy confirms nephritis.",
  "The results point to RA instead of SLE || Anti-dsDNA is specific for SLE."],
 "Anti-dsDNA is more specific for SLE and helps assess activity; complement (C3/C4) may drop during active disease.")

q("sledx", "A nurse is reviewing the SLE workup. Which statements are accurate? " + SATA,
 ["*ANA is often positive but is not diagnostic alone",
  "Anti-CCP is the key antibody for SLE || Anti-CCP is the most specific RA antibody.",
  "*Anti-dsDNA is more specific and helps assess activity",
  "Complement levels rise during active SLE || They may decrease.",
  "*A kidney biopsy confirms lupus nephritis"],
 "ANA is often positive but not diagnostic alone; anti-dsDNA and anti-Smith are more specific; complement may drop with active disease; biopsy confirms nephritis.")

q("slemeds", "A 34-year-old client with severe SLE is started on cyclophosphamide. Which monitoring is the priority?",
 ["Eye exams about every 6 months || That is for hydroxychloroquine.",
  "*Blood counts and signs of infection",
  "Peak flow each morning || Not listed for SLE drugs.",
  "Hearing checks at each visit || Not listed for SLE drugs."],
 "Immunosuppressants are used for moderate-to-severe SLE; monitor blood counts, infection and organ toxicity by drug.")

q("slemeds", "Which pairing of an SLE medication and its use is correct?",
 ["NSAIDs for organ-threatening disease || NSAIDs are for mild joint symptoms.",
  "Hydroxychloroquine to cure SLE || It reduces flare frequency.",
  "Belimumab to increase B-lymphocyte activity || It decreases B-lymphocyte activity.",
  "*Corticosteroids for organ-threatening disease"],
 "SLE drugs: NSAIDs for mild joint symptoms, hydroxychloroquine, corticosteroids for active or organ-threatening disease, immunosuppressants for moderate-to-severe disease.")

q("slenurse", "A nurse is teaching home monitoring to a client with SLE who takes immunosuppressants. What should the client track? " + SATA,
 ["*Blood pressure",
  "*Daily weight and any swelling",
  "*Temperature and signs of infection",
  "Peak flow as the only measure || Not the focus for SLE.",
  "Nothing while feeling well || Monitoring continues between flares."],
 "SLE monitoring includes BP, weight and edema, I&O and urine findings, temperature and infection signs, and new neurologic changes.")

q("slenurse", "A 32-year-old client with SLE is starting a demanding new job and asks how to avoid flares. Which response by the nurse is best?",
 ["*'Pace yourself, rest, manage stress and stay on your meds.'",
  "'Push through the fatigue to build your stamina.' || Rest and pacing are needed.",
  "'Skip your medicines on the days you feel well.' || Treatment adherence prevents flares.",
  "'Lab visits can wait until you notice symptoms.' || Keep lab follow-ups."],
 "SLE flare prevention includes sun protection, rest and pacing, stress management, treatment adherence and keeping lab follow-ups.")
