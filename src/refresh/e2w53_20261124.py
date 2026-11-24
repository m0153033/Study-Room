T = "e2w53"; SET = "20261124"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("patho", "A 64-year-old client with knee OA asks how the 'bone spurs' on the X-ray formed. Which explanation is accurate?",
 ["Uric acid crystals erode the bone ends || Uric acid crystals are not OA.",
  "*Worn cartilage lets bone rub bone, so bone thickens into osteophytes",
  "Synovial inflammation spreads through the body || That is systemic, like RA.",
  "A bone infection spreads into the joint || OA is not an infection."],
 "Cartilage softens and thins, the joint space narrows, bone rubs bone, then bone thickens and forms osteophytes.")

q("oarisk", "A nurse is screening clients at a community clinic. Which clients have risk factors for osteoarthritis? " + SATA,
 ["*A 63-year-old woman who smokes",
  "A 25-year-old nonsmoker at a healthy weight || No listed risk factors.",
  "*A client with obesity",
  "*A factory worker who bends the knees repeatedly all shift",
  "A client whose only risk is being male || Women are at higher risk."],
 "OA risk factors: age over 60, obesity, repetitive joint use, women, smoking and genetics.")

q("oapresent", "A nurse assesses a client with OA of the right knee. Which finding would the nurse expect?",
 ["Fever and generalized fatigue || Systemic symptoms fit RA.",
  "Symmetric joints with all-day morning stiffness || This fits RA.",
  "Uric acid crystals in the joint fluid || Crystals are not OA.",
  "*A grating sound (crepitus) when the knee moves"],
 "OA is local: stiffness after inactivity, crepitus and osteophytes (Heberden's distal, Bouchard's proximal).")

q("oadx", "A client with suspected OA is sent for an X-ray. Which findings can the X-ray show?",
 ["*Joint space narrowing and osteophytes",
  "Detailed view of cartilage health || MRI evaluates cartilage.",
  "The level of inflammation in the blood || ESR and CRP reflect inflammation.",
  "Whether rheumatoid factor is present || RF is a lab used to rule out RA."],
 "X-ray: narrowing and osteophytes. MRI: cartilage. No single lab diagnoses OA.")

q("oameds", "Which medication teaching is correct for a client with OA? " + SATA,
 ["*Do not take more than 4 g of acetaminophen a day",
  "Cortisone can be injected into the joint weekly || Limited to about 4 times a year.",
  "*Wear the lidocaine patch 12 hours on, then 12 hours off",
  "Opioids are started at a high dose || Start low, go slow.",
  "*Cyclobenzaprine may make you sleepy"],
 "Acetaminophen max 4 g/day; lidocaine patch 12 on/12 off; muscle relaxants can cause sleepiness; cortisone ~4x/year; opioids start low, go slow.")

q("nonpharm", "A client with hip OA refuses to attend physical therapy, saying it hurts too much. Which nursing action is best?",
 ["Tell the client to skip PT until the pain is gone || Exercise is part of OA care.",
  "Withhold pain medicine so limits can be felt || Pain control is needed to participate.",
  "*Give prescribed pain medication before the PT session",
  "Suggest running at home instead || Running is high impact; swimming is preferred."],
 "Adequate pain control is needed for participation in PT and OT.")

q("surgind", "Which client with osteoarthritis is the best candidate for joint replacement?",
 ["A newly diagnosed client with mild crepitus || Not at diagnosis or with mild findings.",
  "A client with a positive rheumatoid factor || RF points toward RA, not an OA indication.",
  "A client whose pain is well controlled by acetaminophen || Pain control is adequate.",
  "*A client with severe hip pain, poor pain control and loss of function"],
 "Severe pain plus loss of function or inadequate pain control indicates arthroplasty; about 70% of hip replacements are from OA.")

q("preop", "A client scheduled for total hip replacement next week has a dental abscess. Which action should the nurse take?",
 ["Proceed, since the abscess is not near the hip || Infection anywhere risks prosthetic failure.",
  "Plan a single antibiotic dose in the OR and proceed || Not enough; clear the infection first.",
  "*Notify the surgeon so the infection is cleared before surgery",
  "Cancel joint replacement permanently || Treat the infection, then proceed later."],
 "No infection anywhere before joint replacement; clear it about 2–4 weeks before surgery.")

q("postop", "On post-op day 1 after total knee replacement, the client's foot is pale and cool with a weak pulse and tingling. Which action is the priority?",
 ["*Report the neurovascular changes to the surgeon right away",
  "Put a pillow under the knee and recheck tomorrow || Delays care; no pillow under the knees.",
  "Apply a heating pad to warm the foot || Does not address neurovascular compromise.",
  "Document this as an expected finding || Neurovascular changes are not expected."],
 "Post-op priorities are respiratory and neurovascular: the 6 Ps are pain, pallor, pulses, paresthesia, paralysis and pressure.")

q("hip", "Which client actions after a posterior-approach total hip replacement show correct hip precautions? " + SATA,
 ["*Using a raised toilet seat",
  "Sitting in a low, soft recliner || Low seats cause hip flexion past 90 degrees.",
  "*Keeping an abduction pillow between the legs",
  "Crossing the ankles while lying in bed || No crossing legs.",
  "*Using a long-handled grabber to pick up items"],
 "Hip precautions: no flexion past 90 degrees, no crossing legs, keep abducted, raised toilet seat.")

q("knee", "Two days after total knee replacement, a client keeps the knee bent on pillows because straightening it hurts. Which teaching is best?",
 ["Keep the knee bent so the joint can rest || Risks scar tissue and contracture.",
  "Place an abduction pillow between the legs || That is a hip precaution.",
  "*Work on gradual bending and full extension to prevent contracture",
  "Apply a heating pad before moving the knee || Ice packs are used early after TKR."],
 "Knee: prevent scar tissue and contracture with progressive ROM, bending and full extension; ice first 24 hours.")

q("wb", "A nurse is caring for one client with a cemented hip and another with a press-fit (uncemented) hip. Which statement is correct?",
 ["The cemented hip must stay non-weight-bearing for months || Cemented hips often tolerate PWB or FWB.",
  "Both clients can run on post-op day 1 || Running is not appropriate.",
  "Weight-bearing orders need not be checked first || Know the weight-bearing order before ambulating.",
  "*The press-fit hip may need NWB or toe-touch until bone grows in"],
 "Press-fit is porous and bone grows in over about 3 months, so it may need NWB or toe-touch at first.")
