T = "e5slera"; SET = "20261128"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("big", "A nurse is building a comparison chart of RA and SLE for a study group. Which feature belongs under SLE only?",
 ["A chronic autoimmune course || Both RA and SLE are chronic autoimmune diseases.",
  "Periods of flares and remissions || Both RA and SLE flare and remit.",
  "*Immune complexes in the kidneys, blood and nerves",
  "The synovium as the main target || The synovium is the main target in RA."],
 "RA and SLE are both chronic systemic autoimmune diseases with flares and remissions. RA mainly attacks the synovium; SLE is a multisystem autoantibody disease with immune complexes in the skin, joints, kidneys, blood, heart, lungs and nervous system.")

q("rapatho", "A nurse teaches a 37-year-old bank teller newly diagnosed with RA. Which client statement shows understanding of the disease?",
 ["*'My immune system is inflaming the lining of my joints.'",
  "'My joints are wearing out from years of heavy use.' || That describes OA, not RA.",
  "'RA is the most common arthritis in older adults.' || OA is the most common arthritis in older adults.",
  "'Uric acid crystals are building up in my joints.' || Crystals are not the RA mechanism."],
 "RA is an inflammatory autoimmune disease that primarily targets the synovial lining of the joints. OA is degenerative wear and tear and is the most common arthritis in older adults.")

q("rapatho", "Client A, age 74, has joint changes from degenerative wear and tear. Client B, age 35, has inflamed synovium in both wrists. Which statement is accurate?",
 ["Client A has the most common autoimmune arthritis || Wear and tear describes OA, which is not autoimmune.",
  "Both clients have an autoimmune attack on the synovium || Only RA is an autoimmune synovial attack.",
  "*Client B's disease is inflammatory and autoimmune",
  "Client B's disease is degenerative wear and tear || Inflamed synovium points to RA, not OA."],
 "RA is inflammatory and autoimmune, targets the synovial lining and is often symmetric with systemic signs; it is the most common autoimmune arthritis. OA is degenerative wear and tear and is the most common arthritis in older adults.")

q("rarisk", "A 31-year-old client with RA had few symptoms during her pregnancy. Two months after delivery her joint pain has returned. Which explanation by the nurse is accurate?",
 ["'Your RA has most likely turned into lupus.' || RA does not turn into SLE.",
  "*'Many clients remit while pregnant, then relapse after delivery.'",
  "'Pregnancy should have cured your RA for good.' || Pregnancy does not cure RA.",
  "'RA symptoms never change during pregnancy.' || Many clients go into remission in pregnancy."],
 "Per the textbook, many clients with RA go into remission during pregnancy and relapse after delivery; the reasons aren't fully known.")

q("ramani", "A nurse is assessing a 40-year-old client with suspected early RA. Which finding should the nurse expect?",
 ["Crepitus from bone rubbing on bone only || That is not a typical RA joint finding.",
  "*Morning stiffness with warm, swollen hand joints",
  "Bony nodes on the distal finger joints || That is not the RA joint pattern.",
  "Pain and swelling in only the big toe || RA is symmetric in the hands, wrists and feet."],
 "RA joint findings include pain, warmth and swelling, morning stiffness and reduced range of motion and grip, with symmetric involvement of the MCP and PIP joints of the hands, plus wrists and feet.")

q("raextra", "A nurse reviews the record of a 59-year-old client with RA. Which findings are systemic (extra-articular) RA manifestations? " + SATA,
 ["*Weight loss",
  "Ulnar deviation of the fingers || This is a joint deformity, not an extra-articular finding.",
  "*Anemia",
  "Malar rash across the cheeks || A butterfly rash points to SLE.",
  "*Rheumatoid nodules"],
 "Systemic RA findings include fatigue, low-grade fever, weight loss, rheumatoid nodules, anemia and dry eyes and mouth. Pulmonary and cardiovascular complications can also occur.")

q("radx", "A nurse is precepting a student who is reviewing RA lab work. Which statement by the student needs correction?",
 ["'Anti-CCP is the most specific antibody for RA.' || This statement is accurate.",
  "'A CBC is used to check for anemia.' || This statement is accurate.",
  "*'An elevated ESR and CRP confirm RA by themselves.'",
  "'Imaging can show changes inside the joints.' || This statement is accurate."],
 "No single test confirms RA; history, exam, joint pattern, inflammatory markers, antibodies and imaging are combined. ESR and CRP show inflammation and track activity; anti-CCP is most specific; the CBC checks for anemia.")

q("radx", "A nurse is reviewing the RA workup with a new graduate. Which pairings of a test with its purpose are correct? " + SATA,
 ["*CBC: checks for anemia",
  "RF: confirms RA when positive alone || No single test confirms RA.",
  "*ESR: shows inflammation and tracks activity",
  "Anti-dsDNA: the most specific RA antibody || Anti-dsDNA is more specific for SLE.",
  "*Imaging: shows changes in the joints"],
 "In RA, anti-CCP is the most specific antibody and RF is also used, ESR and CRP show inflammation and track activity, the CBC checks for anemia, and imaging shows joint changes. No single test confirms RA.")

q("ranpharm", "A nurse teaches a 52-year-old client with RA about comfort measures. Which client statements show understanding? " + SATA,
 ["*'I'll use cold when my joints are hot and swollen.'",
  "'I'll go for hard runs during a flare to stay loose.' || High-impact activity is avoided during a flare.",
  "*'A warm bath can ease my morning stiffness.'",
  "*'I'll rest my joints while they are inflamed.'",
  "'A hot soak is best for acutely hot, swollen joints.' || Cold is used for acutely hot, swollen joints."],
 "Cold is used for acutely swollen, hot, painful joints; moist heat such as a warm tub bath relieves stiffness. Rest during active inflammation; low-impact exercise and ROM when tolerated.")

q("ranpharm", "A nurse is reviewing four clients with RA. For which client is moist heat the most appropriate comfort measure?",
 ["A client whose ankles are acutely hot and swollen || Cold is used for acutely hot, swollen joints.",
  "*A client with morning stiffness and no current flare",
  "A client whose wrists turned red and hot today || Acutely inflamed joints call for cold and rest.",
  "A client in a flare with very painful, swollen knees || Cold is used during an acute flare."],
 "Moist heat, such as a warm tub bath, relieves stiffness without an acute flare. Cold application is the priority for acutely swollen, hot, painful joints.")

q("rameds", "A 58-year-old client has taken prednisone for RA for 4 years. Which finding should the nurse recognize as an adverse effect of long-term use?",
 ["Improved bone density on a scan || Long-term steroids cause osteoporosis, not stronger bone.",
  "*An elevated blood glucose level",
  "A falling CRP level || A falling CRP reflects less inflammation.",
  "Less morning stiffness || This is a therapeutic effect, not an adverse one."],
 "Long-term corticosteroids can cause osteoporosis, infection, high glucose and high BP, and they should not be stopped abruptly.")

q("rameds", "A nurse is comparing RA medications for a client who wants to know what each one does. Which statement is accurate?",
 ["'Ibuprofen keeps the disease from progressing.' || NSAIDs don't prevent disease progression.",
  "'Prednisone cures RA if it is started early.' || Steroids relieve symptoms; they don't cure RA.",
  "*'Methotrexate aims to limit joint destruction.'",
  "'Steroids can replace the need for a DMARD.' || Steroids don't replace DMARDs."],
 "DMARDs such as first-line methotrexate aim to limit inflammation and joint destruction, not just relieve pain. NSAIDs and steroids relieve symptoms but don't replace DMARDs.")

q("biologic", "A nurse is reviewing how targeted RA drugs work. Which statement is accurate?",
 ["JAK inhibitors work by binding TNF || Adalimumab and infliximab bind TNF.",
  "*Some other biologics block interleukin-6",
  "Adalimumab works by blocking COX enzymes || Adalimumab binds TNF.",
  "Infliximab boosts the immune response || These drugs suppress the immune system."],
 "Adalimumab and infliximab bind TNF, which drives joint destruction; other biologics block interleukin-6, and JAK inhibitors block the JAK enzyme. All suppress the immune system, so clients report fever or infection.")

q("ranurse", "A 62-year-old client with RA says she is exhausted by the time she finishes cleaning her kitchen. Which teaching by the nurse is best?",
 ["Carry heavy pots with the fingers to build strength || Carrying heavy loads with the fingers stresses joints.",
  "Stop all household tasks to save the joints || Avoiding all activity is not advised.",
  "*Use energy conservation with planned rest breaks",
  "Add high-impact exercise to build stamina || Low-impact movement is taught."],
 "RA teaching includes energy conservation, joint protection, adaptive equipment and low-impact movement, with coordination of physical and occupational therapy.")

q("slepatho", "A nursing student is describing SLE pathophysiology. Which statement by the student needs correction?",
 ["'Loss of self-tolerance leads to autoantibodies.' || This statement is accurate.",
  "'Immune complexes deposit in tissues and inflame them.' || This statement is accurate.",
  "*'Damage comes from bacteria spreading through tissues.'",
  "'Severity ranges from skin signs to organ disease.' || This statement is accurate."],
 "In SLE, loss of self-tolerance creates autoantibodies; immune complexes deposit in tissues and cause inflammation. It flares and remits, ranging from skin and joint symptoms to life-threatening organ disease.")

q("sletrig", "A 29-year-old client with SLE is admitted with a new flare. Which recent events in her history could be triggers? " + SATA,
 ["*A week of sunbathing at the lake",
  "Eating several high-purine meals || Diet is not a listed SLE trigger.",
  "*A recent urinary tract infection",
  "*A medication started last month",
  "Walking outdoors in cold weather || Cold weather alone is not a listed trigger."],
 "SLE results from genetics (HLA-DR2 and HLA-DR3 variants) plus environmental triggers (UV light, infections, certain medications) and hormones (estrogen).")

q("sletrig", "A 44-year-old mother with SLE asks whether genes play a part in lupus. Which response by the nurse is accurate?",
 ["'Lupus is linked to HER2 overexpression.' || HER2 is not an SLE factor.",
  "*'HLA-DR2 and HLA-DR3 variants are linked to lupus.'",
  "'Lynch syndrome is the gene change behind lupus.' || Lynch syndrome is not an SLE factor.",
  "'Genes play no part; only sunlight causes it.' || Genetics plus environment drive SLE."],
 "SLE results from genetics (HLA-DR2 and HLA-DR3 variants) plus environmental triggers (UV light, infections, certain medications) and hormones (estrogen).")

q("ravsle", "Client 1 has RA and Client 2 has SLE; both report joint pain. Which statement about their joint disease is accurate?",
 ["*Client 1's joints are more likely to show erosions",
  "Client 2's joints are likely to form pannus || Pannus is an RA process.",
  "Both clients have the same erosive joint pattern || SLE joint disease isn't usually erosive.",
  "Client 2's disease is limited to the synovium || SLE inflames many organs."],
 "RA attacks the synovial membrane and forms pannus that erodes cartilage and bone, causing narrowing, erosions and deformity. SLE joint disease isn't usually erosive like RA.")

q("ravsle", "A nurse is explaining the SLE disease process to a client's family. Which statements are accurate? " + SATA,
 ["*Autoantibodies form immune complexes",
  "The synovium thickens into pannus || Pannus is an RA process.",
  "*Immune complexes can inflame the skin and kidneys",
  "*Its joint disease usually isn't erosive",
  "Uric acid crystals collect in the joints || Crystals are not part of SLE."],
 "SLE forms autoantibodies and immune complexes that inflame many organs, including the skin, kidneys, joints and blood vessels. SLE joint disease isn't usually erosive like RA, which forms pannus.")

q("sleskin", "A nurse is assessing a 30-year-old client with SLE. Which finding should the nurse NOT attribute to SLE?",
 ["Discoid skin lesions || Discoid lesions are an SLE skin finding.",
  "Ulcers inside the nose || Oral or nasal ulcers are SLE mucosal findings.",
  "Patchy hair loss || Alopecia is an SLE skin finding.",
  "*Koplik spots"],
 "SLE skin and mucosal findings include malar rash, photosensitivity, discoid lesions, alopecia and oral or nasal ulcers. Koplik spots are not an SLE finding.")

q("sleskin", "A 24-year-old client with SLE asks whether the butterfly rash is the only skin sign to watch for. Which response by the nurse is accurate?",
 ["'Yes, the rash is the only skin sign of lupus.' || SLE has several skin and mucosal signs.",
  "*'No, sun sensitivity, mouth sores and hair loss occur too.'",
  "'No, but the only other sign is Koplik spots.' || Koplik spots are not an SLE finding.",
  "'Skin signs occur in RA, not in lupus.' || Skin signs are characteristic of SLE."],
 "The malar (butterfly) rash is characteristic of SLE but not universal. Other skin signs include photosensitivity, discoid lesions, alopecia and oral or nasal ulcers.")

q("sleorgan", "A nurse is caring for four clients with SLE. Which client should the nurse assess FIRST?",
 ["A client with mild hair thinning unchanged for months || This is a stable skin finding.",
  "*A client who had new seizure activity this morning",
  "A client with aching knees asking about warm baths || Joint aches are not the most urgent.",
  "A client asking which sunscreen to buy || This is routine teaching."],
 "SLE nervous system findings include headache, seizures and cognitive or mood changes; new seizures or psychosis need prompt reporting. The major concern in SLE is organ damage.")

q("slerenal", "A nurse is teaching a 27-year-old client with SLE what to watch for at home. Which new finding should the client report as possible lupus nephritis?",
 ["Mild morning stiffness in both knees || This is a joint finding, not a kidney sign.",
  "*Swelling in both ankles and lower legs",
  "A malar rash that has been fading || This is a stable skin finding.",
  "Tiredness after a long work shift || Fatigue alone is not a kidney sign."],
 "Lupus nephritis presents with proteinuria, hematuria, edema, hypertension and rising creatinine and needs prompt evaluation; it can progress to kidney failure needing dialysis or transplant.")

q("slerenal", "A nurse reviews data on four clients with SLE. Which finding most suggests kidney involvement?",
 ["A positive ANA result || ANA is not a kidney finding.",
  "Oral ulcers on the inside of the cheek || This is a mucosal finding.",
  "*Serum creatinine rising over 3 visits",
  "Morning stiffness in the hands || This is a joint finding."],
 "Rising creatinine, along with proteinuria, hematuria, edema and hypertension, suggests lupus nephritis, the SLE red flag. Renal function and vital signs are the priority monitoring.")

q("sledx", "A nurse is reviewing the SLE workup with a student. Which pairings of a test with its purpose are correct? " + SATA,
 ["*Kidney biopsy: confirms lupus nephritis",
  "ANA: diagnoses SLE by itself || ANA is often positive but not diagnostic alone.",
  "*CBC: checks for blood-cell abnormalities",
  "*Anti-dsDNA: helps assess disease activity",
  "Anti-CCP: the key antibody for SLE || Anti-CCP is most specific for RA."],
 "ANA is often positive but not diagnostic alone; anti-dsDNA is more specific and helps assess activity; complement may drop during active disease; the CBC checks blood-cell abnormalities; a kidney biopsy confirms lupus nephritis.")

q("sledx", "A 33-year-old client has a positive ANA, and the provider adds an anti-Smith test. The client asks why. Which response by the nurse is best?",
 ["*'Anti-Smith is more specific for lupus than ANA.'",
  "'Anti-Smith is more sensitive for lupus than ANA.' || Anti-Smith is less sensitive than ANA.",
  "'Anti-Smith is the key test for RA instead.' || Anti-CCP is the most specific RA antibody.",
  "'Anti-Smith measures how well your kidneys work.' || Creatinine and BUN check kidney function."],
 "Anti-Smith is more specific but less sensitive than ANA. ANA is often positive in SLE but not diagnostic by itself.")

q("slemeds", "A 25-year-old client with SLE has mild joint aching and no organ involvement. Which medication does the nurse anticipate?",
 ["Cyclophosphamide for the joint aches || Immunosuppressants are for moderate-to-severe disease.",
  "*An NSAID such as naproxen",
  "Methylprednisolone for organ disease || Steroids are for active or organ-threatening disease.",
  "Oseltamivir to calm the immune system || Oseltamivir is not an SLE drug."],
 "SLE drugs: NSAIDs for mild joint symptoms (monitor GI and kidney effects), hydroxychloroquine, corticosteroids for active or organ-threatening disease and immunosuppressants for moderate-to-severe disease.")

q("slemeds", "The parent of a 10-year-old with active SLE asks whether belimumab could be used for her child. Which response by the nurse is accurate?",
 ["'No, it is approved only for adults over 65.' || It is approved for adults and children 5 and older.",
  "*'It is approved for children 5 and older with active SLE.'",
  "'No, it is an antimalarial used only in adults.' || Belimumab is not an antimalarial.",
  "'No, it is an NSAID used mainly for RA.' || Belimumab is not an NSAID."],
 "Belimumab is the first FDA-approved drug specifically designed for SLE; it decreases B-lymphocyte activity and is given IV or SQ to adults and children 5 and older with active SLE.")

q("slenurse", "A 31-year-old client with SLE says, 'I take my medicine and wear sunscreen. What else can help prevent flares?' Which response by the nurse is best?",
 ["'Stopping your medicine when well gives you a break.' || Treatment adherence prevents flares.",
  "*'Rest, activity pacing and stress management also help.'",
  "'Lab visits are needed only during a flare.' || Lab follow-ups are kept even when well.",
  "'Pushing through fatigue will build your stamina.' || Rest and pacing are taught."],
 "SLE flare prevention includes sun protection, adequate rest and activity pacing, stress management, treatment adherence and keeping lab follow-ups.")

q("slenurse", "A nurse is admitting a 43-year-old client with SLE who takes immunosuppressants. Which assessments belong in the plan of care? " + SATA,
 ["*Intake and output with urine findings",
  "Hearing checks as the main focus || Hearing is not a listed SLE priority.",
  "*Temperature and signs of infection",
  "*New neurologic changes",
  "Skipping vital signs while the client is stable || BP, weight and edema are monitored."],
 "SLE monitoring includes BP, weight and edema, I&O and urine findings, temperature and infection signs, and new neurologic changes. Immunosuppressive drugs raise infection risk.")
