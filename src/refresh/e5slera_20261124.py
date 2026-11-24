T = "e5slera"; SET = "20261124"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# big
q("big", "A 34-year-old client with SLE (systemic lupus erythematosus) says, 'My sister has RA (rheumatoid arthritis), so I guess lupus will mostly just hurt my joints too.' Which response by the nurse is accurate?",
  ["'Yes, both diseases stay limited to the joints over time.' || SLE is multisystem, not limited to joints",
   "'No, lupus mainly attacks the kidneys while RA spares the joints.' || RA mainly attacks the synovial joints",
   "'No, lupus is an infection, while RA is an autoimmune disease.' || Both are autoimmune; SLE is not an infection",
   "*'Lupus can affect the skin, kidneys, blood, heart, lungs and nerves too.'"],
  "RA mainly attacks the synovium. SLE is a multisystem autoantibody disease with immune complexes in the skin, joints, kidneys, blood, heart, lungs and nervous system.")

# rapatho (HI x2)
q("rapatho", "A nurse is comparing RA (rheumatoid arthritis) with OA (osteoarthritis) for a group of nursing students. Which statement is accurate?",
  ["RA is degenerative wear and tear of the joint cartilage || That describes OA; RA is inflammatory and autoimmune",
   "OA is often symmetric with systemic signs such as fever || Symmetric involvement with systemic signs describes RA",
   "*OA is the most common arthritis in older adults; RA is the most common autoimmune arthritis",
   "Both begin as an autoimmune attack on the synovial lining || Only RA is autoimmune; OA is degenerative"],
  "RA is inflammatory and autoimmune, often symmetric with systemic signs; OA is degenerative wear and tear. OA is the most common arthritis in older adults, and RA is the most common autoimmune arthritis.")
q("rapatho", "Which sequence best describes how joint damage progresses in RA (rheumatoid arthritis)?",
  ["Cartilage thins from use, then bone rubs on bone and forms spurs || That is degenerative wear and tear, not RA",
   "Immune complexes lodge in the kidneys first, then spread to the joints || That describes SLE organ deposition",
   "Crystals form in the joint, then the cartilage dissolves and swells || Crystals are not the RA mechanism",
   "*Synovium inflames and thickens into pannus, erodes cartilage and bone, then scars"],
  "RA targets the synovial lining. Inflamed synovium thickens into pannus that invades and erodes cartilage and bone, and resulting scar tissue can immobilize the joint.")

# rarisk
q("rarisk", "A 32-year-old client with RA (rheumatoid arthritis) is 20 weeks pregnant and says her joints feel much better. Which explanation by the nurse is accurate?",
  ["'Pregnancy has permanently cured your RA, so it won't come back.' || It is not cured; relapse often follows delivery",
   "*'Many clients go into remission while pregnant, then relapse after delivery.'",
   "'Your RA has likely changed into lupus during this pregnancy.' || RA does not turn into SLE",
   "'RA always worsens in pregnancy, so your diagnosis may be wrong.' || Remission during pregnancy is common"],
  "Per the textbook, many clients with RA go into remission during pregnancy and relapse after delivery; the reasons aren't fully known.")

# ramani
q("ramani", "A 41-year-old client reports several weeks of joint pain and stiffness. Which assessment finding is most consistent with RA (rheumatoid arthritis)?",
  ["Pain and swelling limited to one knee || RA is symmetric, not a single knee",
   "Bony nodes on the distal finger joints || Distal bony nodes (Heberden's nodes) do not fit RA",
   "*Swelling of the MCP (metacarpophalangeal) and PIP (proximal interphalangeal) joints of both hands",
   "Pain limited to the big toe of one foot || An isolated big toe is not the RA pattern"],
  "RA typically causes symmetric involvement of the MCP and PIP joints of the hands, plus the wrists and feet; larger joints can be involved later.")

# raextra
q("raextra", "A 54-year-old client with RA (rheumatoid arthritis) takes methotrexate and prednisone and asks why the provider is checking her for heart problems. Which response by the nurse is best?",
  ["'Pannus can grow into the coronary arteries and block them.' || Pannus does not block coronary arteries",
   "'RA adds no heart risk; this is just a routine checkup.' || Clients with RA have higher heart disease risk",
   "*'Ongoing inflammation and some RA drugs raise heart disease risk.'",
   "'Your dry eyes and mouth are a sign of heart failure.' || Dry eyes and mouth suggest Sjögren syndrome"],
  "Clients with RA have higher heart disease risk from chronic inflammation plus side effects of drugs like methotrexate and steroids, so the nurse monitors for cardiovascular symptoms.")

# radx (HI x2)
q("radx", "A CBC (complete blood count) is ordered as part of the workup for a 45-year-old client with suspected RA (rheumatoid arthritis). The client asks why. What is the nurse's best explanation?",
  ["'It is the one test that confirms the RA diagnosis.' || No single test confirms RA",
   "*'It checks for anemia, which can occur with RA.'",
   "'It measures the antibody most specific for RA.' || Anti-CCP is the most specific antibody",
   "'It shows erosions and narrowing inside the joints.' || Imaging shows joint changes"],
  "In RA, the CBC checks for anemia. Anti-CCP and RF are antibodies, ESR and CRP track inflammation, and imaging shows joint changes; no single test confirms RA.")
q("radx", "A provider is working to confirm RA (rheumatoid arthritis) in a 37-year-old client. Which data are combined to make the diagnosis? " + SATA,
  ["*Health history and physical exam",
   "*Pattern of joint involvement",
   "A single positive ANA (antinuclear antibody) result || ANA does not confirm RA",
   "*Antibodies such as anti-CCP (anti-cyclic citrullinated peptide) and RF (rheumatoid factor)",
   "*Imaging of the affected joints"],
  "No single test confirms RA. History, exam, joint pattern, inflammatory markers (ESR, CRP), antibodies (anti-CCP is most specific; RF) and imaging are combined.")

# ranpharm (HI x2)
q("ranpharm", "A 44-year-old client with RA (rheumatoid arthritis) is in an active flare with hot, swollen wrists. Which nonpharmacologic measures are appropriate? " + SATA,
  ["*Cold application to the swollen joints",
   "High-impact running to keep the joints loose || High-impact activity during a flare is harmful",
   "*Rest during the active inflammation",
   "*Splints to support the inflamed wrists",
   "Hot tub soaks for the acutely hot joints || Heat is for stiffness, not acutely hot joints"],
  "Cold is used for acutely swollen, hot, painful joints. Rest during active inflammation and splints or assistive devices support the joints.")
q("ranpharm", "A 57-year-old client with RA (rheumatoid arthritis) says, 'I'm worn out all day and sleep poorly. Should I just stop exercising?' Which response by the nurse is best?",
  ["'Yes, stop all activity until the fatigue goes away.' || Complete rest is not advised",
   "'Switch to high-impact workouts to build stamina faster.' || High-impact exercise strains RA joints",
   "*'Regular low-impact activity can actually improve sleep and fatigue.'",
   "'Only exercise on days when your joints are flaring.' || Rest is used during active inflammation"],
  "Low-impact exercise and range of motion when tolerated are encouraged; regular activity can also improve sleep and fatigue.")

# rameds (HI x2)
q("rameds", "A 60-year-old client has taken prednisone for RA (rheumatoid arthritis) for 3 years. Which adverse effects should the nurse monitor for? " + SATA,
  ["*Bone loss leading to osteoporosis",
   "*Signs of infection",
   "Improved bone density over time || Long-term steroids cause osteoporosis",
   "*Elevated blood glucose",
   "*Elevated BP (blood pressure)"],
  "Long-term steroids cause osteoporosis. Watch for infection, high glucose and high BP, and teach the client not to stop the drug abruptly.")
q("rameds", "A 36-year-old client with newly diagnosed RA (rheumatoid arthritis) is started on methotrexate and a short course of prednisone. She asks why she needs both. Which response by the nurse is correct?",
  ["'Prednisone will cure your RA so methotrexate can be stopped.' || Steroids do not cure RA",
   "'Prednisone protects your bones while methotrexate starts.' || Steroids can cause osteoporosis",
   "'Prednisone will permanently take the place of methotrexate.' || Steroids do not replace DMARDs",
   "*'Prednisone eases flares while methotrexate takes time to work.'"],
  "Corticosteroids may be used early as a bridge for flares while longer-term DMARDs (disease-modifying antirheumatic drugs), such as first-line methotrexate, take effect.")

# biologic
q("biologic", "A nurse is reviewing how different drugs for RA (rheumatoid arthritis) work. Which statement is correct?",
  ["JAK (Janus-associated kinase) inhibitors bind TNF (tumor necrosis factor) || JAK inhibitors block the JAK enzyme",
   "*Adalimumab and infliximab bind TNF (tumor necrosis factor)",
   "Adalimumab works by killing bacteria in the joint || Biologics do not kill bacteria",
   "Infliximab works by replacing lost synovial fluid || Infliximab binds TNF"],
  "Adalimumab and infliximab bind TNF, which drives joint destruction. Other biologics block interleukin-6, and JAK inhibitors block the JAK enzyme. All suppress the immune system.")

# ranurse
q("ranurse", "A home health nurse is following a 68-year-old client with long-standing RA (rheumatoid arthritis) who takes DMARDs (disease-modifying antirheumatic drugs). Which ongoing focus is most important?",
  ["Checking visual acuity as the only assessment || Assessment covers pain, mobility, ADLs and more",
   "*Watching for infection, drug toxicity and progressive disability",
   "Assessing aspiration risk at every meal || Aspiration is not an RA priority",
   "Teaching finger strength by carrying heavy loads || Heavy loads on the fingers stress joints"],
  "RA nursing care monitors for infection, medication toxicity and progressive disability, along with pain, stiffness, ROM, ADLs and emotional impact.")

# slepatho
q("slepatho", "A 39-year-old client whose SLE (systemic lupus erythematosus) has caused only mild rash and joint aches asks, 'Will my lupus always stay this mild?' Which response by the nurse is accurate?",
  ["'Yes, lupus that starts mild always stays mild.' || Severity can progress to organ disease",
   "'Lupus only ever affects the skin, so you're safe.' || SLE can damage many organs",
   "*'Lupus flares and remits, and some flares can involve organs.'",
   "'Lupus never flares once the first symptoms settle.' || SLE has flares and remissions"],
  "SLE has flares and remissions; severity ranges from skin and joint symptoms to life-threatening organ disease, so the nurse monitors for organ involvement.")

# sletrig (HI x2)
q("sletrig", "A community health nurse is planning lupus awareness outreach. Which groups carry a higher burden of SLE (systemic lupus erythematosus) and should be focused on?",
  ["Men over 80 years of age only || Not a listed higher-burden group",
   "*Women, including Black/African American and Hispanic women",
   "Young children under 5 years only || Not a listed higher-burden group",
   "Athletes who train outdoors in the cold || Cold weather alone is not a listed factor"],
  "Per the lecture, women, Black/African American clients and Hispanic clients carry a higher burden of SLE.")
q("sletrig", "A 26-year-old client with SLE (systemic lupus erythematosus) had a flare one week after a respiratory illness. Which statement by the nurse best explains the link?",
  ["'Only your genes cause flares; the illness was a coincidence.' || Environmental triggers also matter",
   "'Infections trigger RA flares but have no effect on lupus.' || Infections are an SLE trigger",
   "'Flares are caused by stress alone, not by illness.' || Stress is not the only factor",
   "*'Infections are a known trigger that can set off a lupus flare.'"],
  "SLE results from genetics (HLA-DR2, HLA-DR3 variants) plus environmental triggers (UV light, infections, certain medications) and hormones (estrogen).")

# ravsle (HI x2)
q("ravsle", "A nurse is reviewing data for a client with joint pain. Which findings point to SLE (systemic lupus erythematosus) rather than RA (rheumatoid arthritis)? " + SATA,
  ["*Malar rash with photosensitivity",
   "Pannus with joint erosions on x-ray || Pannus and erosions point to RA",
   "*Proteinuria with hypertension",
   "Positive anti-CCP (anti-cyclic citrullinated peptide) || Anti-CCP is the RA-specific antibody",
   "*Positive anti-Smith antibody"],
  "Malar rash, photosensitivity, proteinuria with hypertension and anti-Smith point to SLE. Pannus with narrowing, erosions and deformity points to RA; SLE joint disease isn't usually erosive.")
q("ravsle", "A student asks why SLE (systemic lupus erythematosus) is called a multisystem disease while RA (rheumatoid arthritis) is mainly a joint disease. Which explanation by the nurse is correct?",
  ["*'SLE immune complexes deposit in many tissues; RA centers on the synovium.'",
   "'SLE pannus spreads from the joints into the organs; RA pannus stays put.' || Pannus is the RA process",
   "'RA immune complexes go mainly to the kidneys; SLE ones go to the joints.' || Reversed; RA targets synovium",
   "'SLE erodes cartilage far more than RA, so it spreads to other organs.' || SLE is usually less erosive than RA"],
  "RA attacks the synovial membrane and forms pannus that erodes cartilage and bone. SLE forms autoantibodies and immune complexes that inflame many organs, including the skin, kidneys, joints and blood vessels.")

# sleskin (HI x2)
q("sleskin", "A nurse is assessing a 47-year-old client with SLE (systemic lupus erythematosus). Which findings are skin or mucosal signs of SLE? " + SATA,
  ["*Discoid lesions",
   "Koplik spots inside the cheeks || Not an SLE finding",
   "*Patchy hair loss (alopecia)",
   "A stripe of vesicles along one dermatome || Not an SLE finding",
   "*Ulcers in the mouth or nose"],
  "SLE skin and mucosal findings include malar rash, photosensitivity, discoid lesions, alopecia and oral or nasal ulcers.")
q("sleskin", "A 22-year-old client with SLE (systemic lupus erythematosus) is tearful about her facial rash and thinning hair. Which nursing action is most appropriate?",
  ["Suggest brief tanning sessions to even out the rash || Sun and tanning beds can trigger flares",
   "Tell her every lupus client gets this rash, so it's expected || Not every client has a malar rash",
   "*Provide gentle skin care and explore her body-image concerns",
   "Scrub the rash firmly each day to remove the scaling || Skin care should be gentle"],
  "Nurses offer gentle skin care and address body-image concerns. The malar rash is characteristic but not universal, and photosensitivity means avoiding excess sun and tanning beds.")

# sleorgan
q("sleorgan", "A nurse reviews the CBC (complete blood count) of a 32-year-old client with SLE (systemic lupus erythematosus). Which pattern is consistent with SLE blood involvement?",
  ["Polycythemia with a high red cell count || Polycythemia is not an SLE finding",
   "Isolated high platelets with normal counts || SLE causes thrombocytopenia, not high platelets",
   "*Anemia, leukopenia and thrombocytopenia",
   "A high red cell count with high white cells || SLE lowers blood cell counts"],
  "SLE blood involvement includes anemia, leukopenia and thrombocytopenia. Nervous system findings include headache, seizures and cognitive or mood changes.")

# slerenal (HI x2)
q("slerenal", "A 40-year-old client is hospitalized with an SLE (systemic lupus erythematosus) flare. Which data should the nurse trend most closely? " + SATA,
  ["*Blood pressure readings",
   "*Serum creatinine",
   "Grip strength as the main measure || Not the priority during a flare",
   "*Urine protein and blood",
   "*Weight and edema"],
  "During an SLE flare, renal function and vital signs are the priority. Lupus nephritis presents with proteinuria, hematuria, edema, hypertension and rising creatinine.")
q("slerenal", "A 28-year-old client with newly diagnosed lupus nephritis asks what could happen if it gets worse. Which response by the nurse is accurate?",
  ["'It always clears up on its own without any treatment.' || It needs prompt evaluation and can progress",
   "*'It can progress to kidney failure needing dialysis or transplant.'",
   "'It mostly spreads to the skin and causes a facial rash.' || Nephritis is kidney involvement",
   "'It causes joint erosions much like rheumatoid arthritis.' || Nephritis affects the kidneys, not joints"],
  "Lupus nephritis is the SLE red flag; it can progress to kidney failure needing dialysis or transplant, so it needs prompt evaluation.")

# sledx (HI x2)
q("sledx", "A 31-year-old client with SLE (systemic lupus erythematosus) has protein and blood in her urine and is scheduled for a kidney biopsy. She asks why. Which response by the nurse is correct?",
  ["'It checks for the antibody that is most specific for RA.' || Anti-CCP is the RA-specific antibody, not a biopsy",
   "'It measures your complement (C3/C4) levels directly.' || Complement is a separate test; biopsy confirms nephritis",
   "*'It confirms whether lupus is affecting your kidneys.'",
   "'It replaces the need for any future urine testing.' || Urinalysis still guides evaluation"],
  "A kidney biopsy confirms lupus nephritis. Urinalysis for protein and blood, serum creatinine and BUN (blood urea nitrogen) also check kidney involvement.")
q("sledx", "A nurse is comparing antibody tests for SLE (systemic lupus erythematosus). Which statement about anti-Smith (anti-Sm) is accurate?",
  ["*It is more specific but less sensitive than ANA (antinuclear antibody)",
   "It is less specific for SLE than ANA (antinuclear antibody) is || Anti-Smith is more specific",
   "It is the most specific antibody for RA (rheumatoid arthritis) || That is anti-CCP",
   "It is positive in every client who has SLE (systemic lupus erythematosus) || It is less sensitive than ANA"],
  "ANA is often positive in SLE but not diagnostic alone. Anti-Smith and anti-dsDNA are more specific; anti-dsDNA also helps assess activity, and complement may drop during active disease.")

# slemeds (HI x2)
q("slemeds", "A 38-year-old client with SLE (systemic lupus erythematosus) takes naproxen for mild joint symptoms. Which should the nurse monitor?",
  ["Hearing changes as the only effect || Not the focus for NSAIDs here",
   "Serum lipase levels each visit || Not a listed NSAID concern",
   "*GI (gastrointestinal) and kidney adverse effects",
   "Peak expiratory flow each morning || Not a listed NSAID concern"],
  "NSAIDs (nonsteroidal anti-inflammatory drugs) are used for mild SLE joint symptoms; monitor GI and kidney adverse effects because SLE already threatens the kidneys.")
q("slemeds", "A nurse is teaching a 15-year-old client with active SLE (systemic lupus erythematosus) and her parent about belimumab. Which statement is accurate?",
  ["'It is an NSAID mainly used to treat RA (rheumatoid arthritis).' || It is not an NSAID",
   "'It is an antimalarial that requires eye exams every 6 months.' || That describes hydroxychloroquine",
   "'It is approved only for adults over 65 years of age.' || It is given to adults and children 5 and older",
   "*'It lowers B-lymphocyte activity and was made specifically for SLE.'"],
  "Belimumab is the first FDA-approved drug specifically designed for SLE; it decreases B-lymphocyte activity and is given IV or SQ to adults and children 5 and older with active SLE.")

# slenurse (HI x2)
q("slenurse", "A home health nurse visits a 45-year-old client with SLE (systemic lupus erythematosus) who takes mycophenolate mofetil. Which assessments should the nurse include? " + SATA,
  ["*Weight and check for edema",
   "*Temperature and signs of infection",
   "Grip strength as the only assessment || SLE monitoring is broader",
   "*New headaches, confusion or mood changes",
   "Skin color only, with no vital signs || BP and temperature are needed"],
  "SLE monitoring includes BP, weight and edema, I&O (intake and output) and urine findings, temperature and infection signs, and new neurologic changes. Immunosuppressive drugs raise infection risk.")
q("slenurse", "A 33-year-old client with SLE (systemic lupus erythematosus) works full time and reports constant fatigue. Which intervention best supports flare prevention?",
  ["Encourage a packed schedule to build stamina || Rest and pacing prevent flares",
   "Advise skipping medicines on days she feels well || Treatment adherence prevents flares",
   "*Help her plan rest periods and pace activities",
   "Suggest outdoor errands at midday for energy || Sun exposure can trigger flares"],
  "SLE flare prevention includes adequate rest and activity pacing, sun protection, stress management, treatment adherence and keeping lab follow-ups.")
