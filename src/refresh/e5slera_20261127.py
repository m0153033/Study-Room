T = "e5slera"; SET = "20261127"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("big", "A nursing student is presenting a comparison of RA and SLE at a clinical conference. Which statement by the student needs correction?",
 ["'Both are chronic, systemic autoimmune diseases.' || This statement is accurate.",
  "'Both diseases cycle through flares and remissions.' || This statement is accurate.",
  "*'SLE mainly attacks the synovium, just as RA does.'",
  "'SLE immune complexes can reach the heart and lungs.' || This statement is accurate."],
 "RA and SLE are both chronic systemic autoimmune diseases with flares and remissions. RA mainly attacks the synovium; SLE is a multisystem autoantibody disease with immune complexes in the skin, joints, kidneys, blood, heart, lungs and nervous system.")

q("rapatho", "A 44-year-old schoolteacher with RA asks why her provider warned that her wrist could eventually stop moving. Which explanation by the nurse is accurate?",
 ["'Bony spurs from worn cartilage can fuse the joint.' || That describes wear and tear, not RA.",
  "*'Pannus erodes the joint, and scar tissue can lock it.'",
  "'Crystals collect in the joint and harden over time.' || Crystals are not the RA mechanism.",
  "'Immune complexes in the kidneys spread to the wrist.' || That is not how RA damages joints."],
 "In RA, inflamed synovium thickens into pannus that invades and erodes cartilage and bone; the resulting scar tissue can immobilize the joint.")

q("rapatho", "A 38-year-old mail carrier has swelling in both wrists, fatigue and a low-grade fever. Which type of joint process do these features best fit?",
 ["Degenerative wear and tear, as seen in OA || OA is degenerative, not symmetric with systemic signs.",
  "A bacterial infection inside a single joint || RA is autoimmune, not an infection.",
  "*An inflammatory, autoimmune arthritis such as RA",
  "Cartilage loss from heavy use in older adults || That describes OA, not RA."],
 "RA is inflammatory and autoimmune, often symmetric with systemic signs; OA is degenerative wear and tear. RA is the most common autoimmune arthritis.")

q("rarisk", "A nurse at an employee health fair is reviewing histories. Which client has the MOST risk factors for RA?",
 ["A 50-year-old man who eats a high-purine diet || A high-purine diet is not an RA risk factor.",
  "*A 42-year-old woman who smokes and whose father has RA",
  "A 30-year-old man with no family history who never smoked || This client has no listed risk factors.",
  "A 35-year-old woman with no family history of RA || Female sex is her only listed risk factor."],
 "RA risk factors include family history/genetics, female sex, smoking and certain environmental exposures. This client has three: female sex, smoking and family history.")

q("ramani", "While assessing a 57-year-old client with long-standing RA, the nurse notes a finger with the PIP joint hyperextended and the distal joint flexed. How should the nurse document this?",
 ["Ulnar deviation || Ulnar deviation is fingers drifting toward the little-finger side.",
  "Heberden's nodes || Heberden's nodes are not an RA deformity.",
  "*Swan-neck deformity",
  "Rheumatoid nodule || A nodule is a firm lump under the skin, not a joint position."],
 "Swan-neck deformity is hyperextension of the PIP joint with flexion of the distal joint. Later RA can also cause ulnar deviation and boutonniere deformity, which can limit self-care and mobility.")

q("raextra", "A nurse is reviewing extra-articular RA findings with a student. Which statement by the student needs correction?",
 ["'Fatigue and low-grade fever can occur with RA.' || This statement is accurate.",
  "*'Felty syndrome is the cause of dry eyes and mouth.'",
  "'Firm rheumatoid nodules can form under the skin.' || This statement is accurate.",
  "'Chronic inflammation raises heart disease risk.' || This statement is accurate."],
 "Dry eyes and mouth suggest Sjogren syndrome. Felty syndrome is splenomegaly, neutropenia and anemia, with weight loss and low-grade fever.")

q("radx", "A 51-year-old client with RA has a CRP that has steadily fallen since starting treatment. How should the nurse interpret this trend?",
 ["The RA has been cured and treatment can stop || RA is chronic; CRP does not show a cure.",
  "*The inflammation appears to be less active now",
  "The falling CRP confirms the RA diagnosis || No single test confirms RA.",
  "The client's anemia is getting worse || The CBC checks for anemia, not CRP."],
 "ESR and CRP show inflammation and track RA disease activity. A falling CRP suggests less inflammation.")

q("radx", "A 47-year-old client being evaluated for RA asks why hand x-rays were ordered in addition to blood work. Which response by the nurse is best?",
 ["'The x-ray alone will confirm whether you have RA.' || No single test confirms RA.",
  "'The x-ray measures the most specific RA antibody.' || Anti-CCP is a blood test, not imaging.",
  "*'Imaging can show changes inside the joints.'",
  "'The x-ray checks whether you have anemia.' || The CBC checks for anemia."],
 "RA diagnosis combines history, exam, joint pattern, inflammatory markers, antibodies and imaging. Imaging can show joint changes.")

q("ranpharm", "Which pairing of an RA situation with a comfort measure is correct?",
 ["Acutely hot, swollen joints: a hot tub soak || Cold is used for acutely hot, swollen joints.",
  "*Morning stiffness with no flare: a warm tub bath",
  "Active inflammation: high-impact exercise || Rest is used during active inflammation.",
  "Between flares: complete bed rest || Low-impact exercise is encouraged between flares."],
 "Moist heat such as a warm tub bath relieves stiffness; cold is used for acutely swollen, hot, painful joints. Rest during active inflammation; low-impact exercise and ROM when tolerated.")

q("ranpharm", "A home health nurse visits a 65-year-old client with RA who is between flares. Which client statement needs follow-up teaching?",
 ["'I do my range-of-motion exercises every day.' || ROM when tolerated is encouraged.",
  "'I use a splint and a jar opener when I need them.' || Splints and assistive devices help.",
  "*'I stay in bed all day so my joints don't get worse.'",
  "'My occupational therapist helps me plan my tasks.' || OT is an appropriate measure."],
 "RA comfort measures include low-impact exercise and ROM when tolerated, rest during active inflammation, splints and assistive devices, and PT/OT. Regular activity can also improve sleep and fatigue.")

q("rameds", "A 49-year-old client with RA has been taking methotrexate for a year. Which monitoring should the nurse expect? " + SATA,
 ["*Complete blood count",
  "Eye exams about every 6 months || Routine eye exams are taught for hydroxychloroquine.",
  "*Liver function tests",
  "*Platelet count",
  "*Watching for signs of infection"],
 "Methotrexate is a common first-line DMARD. Monitor CBC, liver tests and platelets and watch for infection; report mouth ulcers, easy bruising, cough or shortness of breath and fever.")

q("rameds", "A 64-year-old client has taken prednisone for RA for 2 years. She calls to say she ran out yesterday and plans to just stop it. Which response by the nurse is best?",
 ["'That's fine, since your joints feel better.' || Feeling better is not a reason to stop.",
  "*'Don't stop it suddenly; let's contact your provider.'",
  "'Stop it, because it is curing your RA.' || Steroids relieve symptoms; they don't cure RA.",
  "'Stop it, because it protects your bones.' || Long-term steroids cause osteoporosis."],
 "Corticosteroids should not be stopped abruptly. Long-term use can cause osteoporosis, infection, high glucose and high BP.")

q("biologic", "A 46-year-old client with RA who receives infliximab calls the clinic reporting a fever and chills. Which action by the nurse is the priority?",
 ["Tell the client fever is an expected effect || Fever can signal infection and must be reported.",
  "Advise doubling fluids and waiting a week || Delaying care is unsafe on immune suppression.",
  "*Report the fever to the provider promptly",
  "Tell the client to stop all lab monitoring || Lab monitoring should not be skipped."],
 "Biologics such as infliximab and JAK inhibitors suppress the immune system, so fever or other signs of infection are reported.")

q("ranurse", "A 60-year-old carpenter with RA reports that walking and climbing stairs have become harder. Which referral should the nurse help coordinate?",
 ["Speech therapy for aspiration risk || Aspiration risk is not the problem described.",
  "*Physical therapy for mobility",
  "A dietitian for a low-purine diet || Purine intake is not part of RA care.",
  "An eye clinic for visual acuity || Vision is not the problem described."],
 "RA nursing care includes assessing ROM and mobility and coordinating physical and occupational therapy, along with teaching joint protection and low-impact movement.")

q("slepatho", "A nurse teaches a 33-year-old client about the course of SLE. Which client statement shows understanding?",
 ["'My lupus will stay mild, since it started mild.' || Severity can range up to organ disease.",
  "'Lupus affects only the skin, so my organs are safe.' || SLE can damage the kidneys and vessels.",
  "*'It may flare and settle, so my organs need monitoring.'",
  "'Once this first flare ends, lupus won't come back.' || SLE has repeated flares and remissions."],
 "SLE has flares and remissions; severity ranges from skin and joint symptoms to life-threatening organ disease, so the nurse monitors for organ involvement.")

q("sletrig", "A nurse is screening clients at a community clinic for lupus education. Which client belongs to a group with a higher burden of SLE?",
 ["A 78-year-old man with knee pain || Older men are not a listed higher-burden group.",
  "*A 27-year-old Black woman with fatigue",
  "A 6-year-old boy with a cold || Young boys are not a listed higher-burden group.",
  "A 45-year-old man who jogs in cold weather || Men and cold weather are not listed risks."],
 "Per the lecture, women, Black/African American clients and Hispanic clients carry a higher burden of SLE.")

q("sletrig", "A nursing student is reviewing SLE triggers. Which statement by the student needs correction?",
 ["'HLA-DR2 and HLA-DR3 variants are linked to lupus.' || This statement is accurate.",
  "'Estrogen can act as a hormonal trigger.' || This statement is accurate.",
  "'Some medications can set off lupus.' || This statement is accurate.",
  "*'HER2 overexpression is a genetic factor in lupus.'"],
 "SLE results from genetics (HLA-DR2 and HLA-DR3 variants) plus environmental triggers (UV light, infections, certain medications) and hormones (estrogen). HER2 is not an SLE factor.")

q("ravsle", "A nurse is reviewing data for a client with chronic joint pain. Which findings point to RA rather than SLE? " + SATA,
 ["*Pannus formation in the joints",
  "Malar rash with photosensitivity || This points to SLE.",
  "*Joint-space narrowing on x-ray",
  "Proteinuria with hypertension || This points to SLE.",
  "*Erosions with joint deformity"],
 "Pannus with joint-space narrowing, erosions and deformity points to RA. Malar rash, photosensitivity, proteinuria with hypertension and anti-Smith point to SLE; SLE joint disease isn't usually erosive.")

q("ravsle", "A 29-year-old client with joint pain has a positive anti-Smith antibody and protein in the urine. Which disease process best explains these findings?",
 ["RA, with pannus eroding cartilage and bone || These findings point to SLE, not RA.",
  "*SLE, with immune complexes inflaming the kidneys",
  "RA, with synovium as the only target || RA does not explain anti-Smith or proteinuria.",
  "SLE, with pannus eroding the joint lining || Pannus is an RA process, not SLE."],
 "SLE forms autoantibodies and immune complexes that inflame many organs, including the kidneys. Positive anti-Smith and proteinuria point to SLE; RA attacks the synovial membrane and forms pannus.")

q("sleskin", "A 26-year-old client says, 'I can't have lupus, because I don't have the butterfly rash.' Which response by the nurse is accurate?",
 ["'You're right; everyone with lupus has that rash.' || Not every client has a malar rash.",
  "*'That rash is common in lupus, but not everyone has it.'",
  "'That rash only appears in children with lupus.' || The rash is not limited to children.",
  "'That rash appears only in men who have lupus.' || The rash is not limited to men."],
 "The red malar (butterfly) rash is characteristic of SLE, but not every client has it. Other skin signs include photosensitivity, oral ulcers and alopecia.")

q("sleskin", "A 41-year-old landscaper with SLE asks how to protect his skin while working outdoors. Which response by the nurse is best?",
 ["'Extra sun will help heal your skin lesions.' || More sun exposure is not appropriate advice.",
  "'Sun has no effect on lupus, so no changes.' || Photosensitivity is common in SLE.",
  "*'Use sun protection and limit excess sun at work.'",
  "'A tanning bed first will help you build a base.' || Tanning beds should be avoided."],
 "Photosensitivity is common in SLE; avoid excess sun, use sun protection and avoid tanning beds to prevent flares.")

q("sleorgan", "A 37-year-old client with SLE and mild joint aches asks what the care team watches most closely. Which response by the nurse is accurate?",
 ["'Joint erosion, since lupus destroys joints more than RA.' || SLE joints are not destroyed like RA.",
  "*'Organ damage, especially to your kidneys.'",
  "'Nothing, since lupus only affects the joints.' || SLE affects many organs.",
  "'Hair thinning, since it is the most serious sign.' || Organ damage is the major concern."],
 "SLE causes arthralgia and arthritis, but not the same destructive pattern as RA. Its major concern is organ damage, especially the kidneys.")

q("slerenal", "A nurse reviews new labs for a 30-year-old client with SLE whose skin and joint symptoms are stable. The serum creatinine has risen since the last visit. Which action is best?",
 ["Recheck it at the next yearly visit || Rising creatinine needs prompt evaluation.",
  "Reassure her since her rash is stable || Stable skin does not rule out nephritis.",
  "Teach cold packs for her joint aches || This does not address the kidney finding.",
  "*Report the rising creatinine promptly"],
 "Rising creatinine is a sign of lupus nephritis, the SLE red flag that needs prompt evaluation; it can progress to kidney failure needing dialysis or transplant.")

q("slerenal", "A 36-year-old client with SLE is seen at a clinic visit. Which findings should the nurse report as possible lupus nephritis? " + SATA,
 ["*Urine dipstick positive for protein",
  "A faded malar rash unchanged for months || This is not a kidney finding.",
  "*New swelling in both ankles",
  "*BP of 166/102",
  "*Blood in the urine"],
 "Lupus nephritis presents with proteinuria, hematuria, edema, hypertension and rising creatinine and needs prompt evaluation.")

q("sledx", "A 32-year-old client with SLE asks why serum creatinine and BUN are drawn at her visits. Which response by the nurse is accurate?",
 ["'They are the most specific antibodies for lupus.' || Anti-dsDNA and anti-Smith are the specific antibodies.",
  "*'They check whether lupus is affecting your kidneys.'",
  "'They check your blood cells for anemia.' || The CBC checks blood-cell abnormalities.",
  "'They confirm the diagnosis of lupus by themselves.' || These are kidney tests, not diagnostic for SLE."],
 "Urinalysis and urine protein, serum creatinine and BUN check for kidney involvement in SLE; the CBC checks for blood-cell abnormalities, and a kidney biopsy confirms lupus nephritis.")

q("sledx", "A nursing student is reviewing antibody tests for SLE. Which statement by the student needs correction?",
 ["'ANA is often positive but can't diagnose lupus alone.' || This statement is accurate.",
  "*'Anti-Smith is more sensitive for lupus than ANA.'",
  "'Anti-dsDNA is more specific and helps assess activity.' || This statement is accurate.",
  "'Complement levels may drop when lupus is active.' || This statement is accurate."],
 "Anti-Smith is more specific but less sensitive than ANA. ANA is often positive but not diagnostic alone; anti-dsDNA is more specific and helps assess activity; complement may drop during active disease.")

q("slemeds", "A 28-year-old client with SLE now has organ-threatening disease. Which medication does the nurse anticipate being ordered?",
 ["Naproxen alone, for its kidney benefits || NSAIDs are for mild joint symptoms and can harm kidneys.",
  "*A corticosteroid such as methylprednisolone",
  "Oseltamivir to calm the immune response || Oseltamivir is not an SLE drug.",
  "Belimumab to raise B-lymphocyte activity || Belimumab decreases B-lymphocyte activity."],
 "SLE drugs: NSAIDs for mild joint symptoms, hydroxychloroquine, corticosteroids for active or organ-threatening disease, and immunosuppressants for moderate-to-severe disease.")

q("slemeds", "A nurse is reviewing the medication lists of clients with moderate-to-severe SLE. Which drugs are immunosuppressants used for SLE? " + SATA,
 ["*Azathioprine",
  "Oseltamivir || Oseltamivir is not an SLE drug.",
  "*Mycophenolate mofetil",
  "Aspirin || Aspirin is an NSAID for mild joint symptoms.",
  "*Cyclophosphamide"],
 "Immunosuppressants for moderate-to-severe SLE include azathioprine, mycophenolate mofetil and cyclophosphamide. Monitor blood counts, infection and organ toxicity by drug.")

q("slenurse", "A nurse is returning calls from clients with SLE. Which client should the nurse follow up with FIRST?",
 ["A client asking which sunscreen to buy || This is routine teaching, not urgent.",
  "A client asking about a stress class || This is routine flare-prevention teaching.",
  "*A client on mycophenolate with a fever of 101°F",
  "A client tired after a long weekend trip || Fatigue alone is not the most urgent."],
 "Immunosuppressive drugs raise infection risk, so fever in a client with SLE on immunosuppression is reported promptly and infection precautions are reinforced.")

q("slenurse", "A nurse reviews flare-prevention habits with a 39-year-old accountant with SLE. Which client action indicates a need for further teaching?",
 ["She keeps a log of her home BP readings || BP monitoring is appropriate.",
  "She plans rest breaks during tax season || Rest and pacing help prevent flares.",
  "*She stopped her medicine because she felt well",
  "She joined a stress management class || Stress management helps prevent flares."],
 "SLE flare prevention includes sun protection, rest and pacing, stress management, treatment adherence and keeping lab follow-ups. Stopping medications when feeling well is not appropriate.")
