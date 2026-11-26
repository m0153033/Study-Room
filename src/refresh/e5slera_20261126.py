T = "e5slera"; SET = "20261126"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("big", "A nurse is teaching a study group how SLE differs from RA. Which features describe SLE but not RA? " + SATA,
 ["*It is a multisystem autoantibody disease",
  "It has periods of flares and remissions || Both RA and SLE flare and remit.",
  "*Immune complexes can affect the kidneys, blood and lungs",
  "It is a chronic autoimmune disease || Both RA and SLE are chronic autoimmune diseases.",
  "The synovium is the main target || The synovium is the main target in RA."],
 "RA and SLE are both chronic systemic autoimmune diseases with flares and remissions. RA mainly attacks the synovium; SLE is a multisystem autoantibody disease with immune complexes in the skin, joints, kidneys, blood, heart, lungs and nervous system.")

q("rapatho", "A nurse is precepting a student on an orthopedic unit. Which statement by the student about RA needs correction?",
 ["'RA is the most common autoimmune arthritis.' || This statement is accurate.",
  "'RA is often symmetric and can cause systemic signs.' || This statement is accurate.",
  "*'RA is the most common arthritis in older adults.'",
  "'RA mainly targets the synovial lining of joints.' || This statement is accurate."],
 "OA is the most common arthritis in older adults; RA is the most common autoimmune arthritis. RA is inflammatory, often symmetric with systemic signs, and targets the synovial lining.")

q("rapatho", "A 55-year-old client asks how RA differs from OA. Which features describe RA? " + SATA,
 ["Degenerative wear and tear of the joint || That describes OA.",
  "*Inflammatory and autoimmune",
  "*Often symmetric",
  "*Can cause systemic signs",
  "Most common arthritis of older adults || OA is most common in older adults."],
 "RA is inflammatory and autoimmune, often symmetric with systemic signs; OA is degenerative wear and tear and the most common arthritis in older adults.")

q("rarisk", "A 28-year-old woman whose mother has RA asks what she can do to lower her own risk. Which response by the nurse is best?",
 ["*'Not smoking is one risk you can control.'",
  "'A low-purine diet will prevent RA.' || A high-purine diet is not an RA risk factor.",
  "'Nothing helps, since RA is only genetic.' || Smoking is a risk factor that can be changed.",
  "'Being female protects you from RA.' || Female sex is a risk factor for RA."],
 "RA risk factors include family history/genetics, female sex, smoking and certain environmental exposures. Not every risk can be prevented, but smoking can be changed.")

q("ramani", "A 43-year-old client with RA says she can no longer grip her coffee mug firmly. How should the nurse interpret this finding?",
 ["It is a sign of SLE skin involvement || This is a joint finding, not a skin finding.",
  "It shows crepitus from bone on bone only || Bone-on-bone crepitus is not a listed RA joint finding.",
  "*Reduced grip and range of motion fit RA",
  "It is unrelated to her joint disease || Reduced grip is a typical RA joint finding."],
 "RA joint findings include pain, warmth and swelling, morning stiffness, and reduced range of motion and grip.")

q("raextra", "While assessing a 64-year-old client with RA, the nurse feels firm lumps under the skin near the elbow. What are these most likely?",
 ["Pannus || Pannus is inflamed synovial tissue inside the joint.",
  "*Rheumatoid nodules",
  "Heberden's nodes || These are bony nodes of the distal finger joints.",
  "Discoid lesions || Discoid lesions are SLE skin findings."],
 "Systemic RA findings include fatigue, low-grade fever, weight loss, rheumatoid nodules, anemia and dry eyes and mouth.")

q("radx", "A client is being followed for RA. Which lab results show inflammation and help track disease activity? " + SATA,
 ["*ESR",
  "Anti-dsDNA || Anti-dsDNA is an SLE antibody.",
  "*CRP",
  "CBC || The CBC checks for anemia.",
  "Anti-CCP || Anti-CCP is the most specific RA antibody, not an activity marker."],
 "ESR and CRP show inflammation and track RA activity. Anti-CCP is the most specific antibody; the CBC checks for anemia.")

q("radx", "A nurse reviews an order set for a client with suspected RA. Which test belongs to the SLE workup rather than the RA workup?",
 ["Anti-CCP || Anti-CCP is the most specific RA antibody.",
  "ESR || ESR tracks RA inflammation.",
  "*Anti-dsDNA",
  "CBC || The CBC checks for anemia in RA."],
 "RA labs include anti-CCP, RF, ESR, CRP and a CBC for anemia, plus imaging. Anti-dsDNA is more specific for SLE.")

q("ranpharm", "A 70-year-old retired baker with RA is between flares and wants to stay active. Which activity should the nurse recommend?",
 ["High-impact running to strengthen joints || High-impact activity is not advised.",
  "Complete bed rest to protect the joints || Rest is for active inflammation, not between flares.",
  "*Low-impact exercise with range of motion",
  "Avoiding all movement to prevent damage || Activity is encouraged when tolerated."],
 "Low-impact exercise and range of motion are encouraged when tolerated; regular activity can also improve sleep and fatigue.")

q("ranpharm", "A nurse visits a 46-year-old client with RA during an acute flare of hot, swollen knees. Which client action requires the nurse to intervene?",
 ["Applying cold packs to the knees || Cold is used for acutely swollen, hot joints.",
  "Resting the inflamed joints today || Rest is appropriate during active inflammation.",
  "Using a splint to support a joint || Splints support inflamed joints.",
  "*Soaking the hot knees in a hot tub"],
 "Cold is the priority comfort measure for acutely swollen, hot, painful joints; moist heat is for stiffness without a flare.")

q("rameds", "A nurse is returning calls from clients with RA. Which client needs follow-up FIRST?",
 ["A client on ibuprofen who reports partial pain relief || Expected NSAID effect.",
  "A client on prednisone waiting for a DMARD to work || Steroids bridge until DMARDs take effect.",
  "*A client on methotrexate with mouth ulcers and a fever",
  "A client on methotrexate with mildly less stiffness || Improvement is an expected effect."],
 "Clients on methotrexate report mouth ulcers, easy bruising, cough or shortness of breath and fever or other signs of infection; monitor CBC, liver tests and platelets.")

q("rameds", "A provider injects a corticosteroid directly into the inflamed knee of a 59-year-old client with RA. Which explanation of its purpose is accurate?",
 ["*'It can give local relief in that joint.'",
  "'It will cure the RA in that knee.' || Steroids do not cure RA.",
  "'It protects the bone from thinning.' || Long-term steroids cause osteoporosis.",
  "'It permanently replaces methotrexate.' || Steroids don't replace DMARDs."],
 "Intra-articular steroid injections can give local relief. Steroids relieve symptoms but don't replace DMARDs such as methotrexate.")

q("biologic", "A nurse is reviewing targeted drugs for RA. Which statements are accurate? " + SATA,
 ["*Adalimumab binds tumor necrosis factor",
  "*Infliximab binds tumor necrosis factor",
  "*JAK inhibitors block the JAK enzyme",
  "They work by blocking COX enzymes || NSAIDs, not biologics, act on COX.",
  "*These drugs suppress the immune system"],
 "Adalimumab and infliximab bind TNF, which drives joint destruction; other biologics block interleukin-6 and JAK inhibitors block the JAK enzyme. All suppress the immune system, so report fever or infection.")

q("ranurse", "A 58-year-old client with RA becomes tearful while describing how she can no longer garden. Which priority assessment area does this reflect?",
 ["Visual acuity || Vision is not the focus of this concern.",
  "Risk for aspiration || Aspiration is not related to this concern.",
  "Urinary elimination || Elimination is not related to this concern.",
  "*Emotional impact of the disease"],
 "RA priority assessments include pain, stiffness and swelling, range of motion and mobility, ability to perform ADLs, and emotional impact and medication tolerance.")

q("slepatho", "A nurse cares for two clients with SLE: one has only a rash and joint aches, and the other has kidney failure. Which statement explains this difference?",
 ["'The first client must have RA instead.' || Mild skin and joint disease can still be SLE.",
  "*'SLE severity ranges from skin and joint symptoms to organ disease.'",
  "'The second client has an infection, not SLE.' || SLE can damage the kidneys.",
  "'SLE always follows the same course in everyone.' || Severity varies widely."],
 "SLE has flares and remissions; severity ranges from skin and joint symptoms to life-threatening organ disease, so the nurse monitors for organ involvement.")

q("sletrig", "A nurse is planning trigger-avoidance teaching for a 30-year-old lifeguard with SLE. Which content should be included? " + SATA,
 ["*Use sun protection when outdoors",
  "Cold weather alone causes lupus flares || Cold weather alone is not a listed trigger.",
  "*Avoid tanning beds",
  "*Infections can set off a flare",
  "A high-purine diet triggers lupus || Diet is not a listed SLE trigger."],
 "SLE triggers include UV light, infections, certain medications and estrogen. Teach sun protection and avoiding tanning beds.")

q("sletrig", "A 22-year-old woman with SLE asks why lupus is more common in women. Which factor should the nurse mention?",
 ["HER2 overexpression || HER2 is not an SLE factor.",
  "Exposure to cold weather || Cold weather alone is not an SLE trigger.",
  "*Estrogen acting as a hormonal trigger",
  "A high-purine diet || Diet is not an SLE trigger."],
 "SLE results from genetics (HLA-DR2 and HLA-DR3 variants) plus environmental triggers (UV light, infections, certain medications) and hormones (estrogen). Women carry a higher burden of SLE.")

q("ravsle", "A nursing student is comparing RA and SLE. Which statement by the student needs correction?",
 ["'RA attacks the synovial membrane of the joints.' || This statement is accurate.",
  "*'SLE forms pannus that erodes cartilage like RA.'",
  "'SLE forms immune complexes that inflame many organs.' || This statement is accurate.",
  "'SLE joint disease usually isn't erosive.' || This statement is accurate."],
 "RA attacks the synovial membrane and forms pannus that erodes cartilage and bone. SLE forms autoantibodies and immune complexes that inflame many organs; its joint disease isn't usually erosive.")

q("ravsle", "Client A has hand x-rays showing erosions and deformity. Client B has a malar rash and photosensitivity. How should the nurse interpret these findings?",
 ["*Client A's findings fit RA; Client B's fit SLE",
  "Client A's findings fit SLE; Client B's fit RA || The pairings are reversed.",
  "Both clients' findings fit RA || Malar rash with photosensitivity points to SLE.",
  "Both clients' findings fit SLE || SLE joint disease isn't usually erosive."],
 "Pannus with joint-space narrowing, erosions and deformity points to RA. Malar rash with photosensitivity points to SLE.")

q("sleskin", "A 19-year-old client with SLE plans to use a tanning bed before a school dance. Which response by the nurse is best?",
 ["'A tan will help hide and heal your rash.' || More sun is not appropriate advice.",
  "'Tanning beds are safer than the sun for lupus.' || Tanning beds should be avoided.",
  "'UV light has no effect on lupus.' || Photosensitivity is common in SLE.",
  "*'UV light can trigger a flare; avoid tanning beds.'"],
 "Photosensitivity is common in SLE; clients avoid excess sun and tanning beds and use sun protection to prevent flares.")

q("sleskin", "A 34-year-old client with SLE notices patchy hair loss and asks if it is related to lupus. Which response by the nurse is accurate?",
 ["'Hair loss happens only with RA.' || Alopecia is an SLE skin finding.",
  "*'Yes, hair loss is a known skin finding of SLE.'",
  "'These are Koplik spots on the scalp.' || Koplik spots are not an SLE finding.",
  "'Hair loss means your kidneys are failing.' || Alopecia is a skin finding, not a renal sign."],
 "SLE skin and mucosal findings include malar rash, photosensitivity, discoid lesions, alopecia and oral or nasal ulcers. The nurse offers gentle skin care and addresses body-image concerns.")

q("sleorgan", "A nurse reviews the problem list of a 31-year-old client with SLE. Which condition is a known cardiopulmonary or vascular finding of SLE?",
 ["Felty syndrome || Felty syndrome is an RA finding with splenomegaly and neutropenia.",
  "Sjögren syndrome || Sjögren syndrome is an RA finding with dry eyes and mouth.",
  "*Pericarditis",
  "Ulnar deviation || Ulnar deviation is an RA finger deformity."],
 "SLE cardiopulmonary and vascular findings include pleuritis or pleural effusion, pericarditis, Raynaud phenomenon and vasculitis.")

q("slerenal", "A nursing student asks why BP and kidney function are the priority checks during an SLE flare. Which explanation by the nurse is best?",
 ["'Kidney problems in lupus always resolve alone.' || Nephritis can progress to kidney failure.",
  "'High BP is the main cause of the malar rash.' || BP relates to nephritis, not the rash.",
  "*'Lupus nephritis can lead to kidney failure.'",
  "'These checks track joint erosion in lupus.' || SLE joint disease isn't usually erosive."],
 "During an SLE flare, renal function and vital signs are the priority. Lupus nephritis can progress to kidney failure needing dialysis or transplant.")

q("slerenal", "A 39-year-old client in an SLE flare is suspected of having lupus nephritis. Which nursing actions are appropriate? " + SATA,
 ["*Monitor blood pressure closely",
  "*Track intake and output",
  "Encourage time in the sun for energy || Sun exposure can trigger flares.",
  "*Check daily weight and edema",
  "Focus on grip strength as the main measure || Renal function and vital signs are the priority."],
 "Lupus nephritis presents with proteinuria, hematuria, edema, hypertension and rising creatinine. Monitor BP, weight and edema, I&O and urine findings.")

q("sledx", "Which antibody is paired with the disease it is most specific for?",
 ["ANA: RA || ANA is often positive in SLE, not specific for RA.",
  "Anti-Smith: RA || Anti-Smith is an SLE antibody.",
  "*Anti-CCP: RA, and anti-dsDNA: SLE",
  "RF: SLE disease activity || RF is used in the RA workup."],
 "Anti-CCP is the most specific antibody for RA. Anti-dsDNA and anti-Smith are more specific for SLE; ANA is often positive in SLE but not diagnostic alone.")

q("sledx", "A 29-year-old client with SLE asks why her anti-dsDNA and complement levels are drawn at every visit. Which response by the nurse is accurate?",
 ["'They confirm lupus is in your kidneys.' || A kidney biopsy confirms lupus nephritis.",
  "*'They help show how active the lupus is.'",
  "'They check you for anemia.' || The CBC checks blood-cell abnormalities.",
  "'They measure your kidney filtration.' || Creatinine and BUN check kidney function."],
 "Anti-dsDNA is more specific for SLE and helps assess activity, and complement (C3/C4) may drop during active disease.")

q("slemeds", "A 26-year-old client with SLE asks what hydroxychloroquine will do for her. Which response by the nurse is accurate?",
 ["'It will cure your lupus over time.' || It reduces flares; it does not cure SLE.",
  "'It decreases B-lymphocyte activity.' || That describes belimumab.",
  "'It is used for organ-threatening disease.' || Corticosteroids are used for that.",
  "*'It reduces how often flares happen.'"],
 "Hydroxychloroquine reduces flare frequency. It can cause retinal changes, so eye exams are needed about every 6 months.")

q("slemeds", "A nurse is teaching a client with active SLE about belimumab. Which statements are accurate? " + SATA,
 ["*It was the first FDA-approved drug designed for SLE",
  "It is an antimalarial drug || Hydroxychloroquine is the antimalarial.",
  "*It decreases B-lymphocyte activity",
  "*It can be given IV or SQ",
  "It is approved only for older adults || It is approved for adults and children 5 and older."],
 "Belimumab is the first FDA-approved drug specifically designed for SLE; it decreases B-lymphocyte activity and is given IV or SQ to adults and children 5 and older with active SLE.")

q("slenurse", "A 35-year-old client with SLE says, 'I feel great, so I'm skipping my lab visit this month.' Which response by the nurse is best?",
 ["'That's fine until symptoms return.' || Lab follow-ups are kept even when well.",
  "*'Please keep your lab visits even when you feel well.'",
  "'You can also stop your medicines for now.' || Treatment adherence prevents flares.",
  "'Labs only matter during a flare.' || Lab follow-up is part of flare prevention."],
 "SLE flare prevention includes sun protection, rest and pacing, stress management, treatment adherence and keeping lab follow-ups.")

q("slenurse", "A 42-year-old client with SLE takes azathioprine. Which new findings should the client report promptly? " + SATA,
 ["*A fever",
  "Mild hair thinning unchanged for months || A stable finding is not new.",
  "*New confusion or mood changes",
  "*Swelling with higher BP readings",
  "Feeling rested after a full night's sleep || This is not a warning sign."],
 "Immunosuppressive drugs raise infection risk, so fever is reported promptly. Monitor BP, weight and edema, urine findings and new neurologic changes.")
