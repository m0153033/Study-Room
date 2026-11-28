T = "e2w53"; SET = "20261128"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("patho", "A 70-year-old retired mechanic with hip OA asks if the condition will go away with treatment. Which response is accurate?",
 ["'Yes, medication will cure the joint.' || OA is managed, not cured.",
  "*'OA is chronic and progressive, so the goal is to manage it.'",
  "'It will clear once the uric acid is lowered.' || Uric acid is not the OA cause.",
  "'It goes away when the joint infection is treated.' || OA is not an infection."],
 "OA is degeneration of joint cartilage; it is chronic and progressive, so it is managed, not cured.")

q("oarisk", "A nurse plans an OA prevention talk at a senior center. Which modifiable risk factors should the nurse emphasize?",
 ["Age over 60 and female sex || These cannot be changed.",
  "Genetics and family history || These cannot be changed.",
  "*Obesity and smoking",
  "Being male and being under 40 || Not listed OA risk factors."],
 "OA risk factors: age over 60, obesity, repetitive joint use, women, smoking and genetics. Weight control decreases joint stress and pain and slows degeneration.")

q("oapresent", "A nurse compares a client with OA and a client with RA. Which finding belongs to the client with OA?",
 ["Fever and generalized fatigue || Systemic signs fit RA.",
  "All-day morning stiffness in symmetric joints || Fits RA.",
  "*Stiffness after inactivity with nodes on distal finger joints",
  "Uric acid crystals in the big toe joint || Not an OA finding."],
 "OA is local: stiffness after inactivity, crepitus and osteophytes (Heberden's nodes distal, Bouchard's proximal), commonly in weight-bearing joints. RA is systemic.")

q("oadx", "A client asks which test will diagnose OA. Which response by the nurse is accurate?",
 ["'Rheumatoid factor confirms OA.' || RF is used to rule out RA.",
  "'A uric acid level confirms OA.' || Not an OA test.",
  "'An ESR measures your cartilage.' || ESR/CRP reflect inflammation.",
  "*'No single lab diagnoses OA; imaging shows the joint changes.'"],
 "No single lab diagnoses OA. X-ray shows joint space narrowing and osteophytes; MRI evaluates cartilage; RF rules out RA; ESR/CRP reflect inflammation.")

q("oameds", "A client with knee OA has taken an NSAID daily for months and now has stomach upset. Which prescribed medication would the nurse expect to be added?",
 ["Cyclobenzaprine || A muscle relaxant for spasm.",
  "*A proton pump inhibitor",
  "A lidocaine patch worn 24 hours a day || Patch is 12 on, 12 off.",
  "An opioid started at a high dose || Opioids start low, go slow."],
 "NSAIDs can cause GI upset and bleeding, so a PPI is used with long-term use. Acetaminophen (max 4 g/day) is the primary pain-relief choice; opioids if others fail, start low and go slow.")

q("nonpharm", "A client with OA of both hands has trouble dressing and eating. Which items would OT most likely provide? " + SATA,
 ["*Large-handled utensils",
  "*Velcro closures on clothing",
  "*A long-handled gripper",
  "Small buttons on shirts || Hard to manage with OA hands.",
  "Hard, narrow pens || Hard to grip with OA hands."],
 "OT adaptive devices: large-handled utensils, long-handled grippers, shoehorns, large buttons and Velcro. Swimming is a good low-impact exercise.")

q("surgind", "A client with knee OA asks when a knee replacement would be considered. Which response is accurate?",
 ["'As soon as OA is found on X-ray.' || Not at diagnosis.",
  "'When rheumatoid factor turns positive.' || RF rules out RA, not an indication.",
  "*'When pain is severe and you lose function or pain is not controlled.'",
  "'When you first notice a grating sound.' || Mild crepitus is not an indication."],
 "Severe pain plus loss of function or inadequate pain control indicates arthroplasty.")

q("preop", "A client is scheduled for total knee replacement in 3 weeks. Which finding should the nurse report to the surgeon before surgery?",
 ["Knee pain with walking || Expected with OA.",
  "Crepitus in the knee || Expected with OA.",
  "*An infected, draining cut on the hand",
  "Knee stiffness after sitting || Expected with OA."],
 "No infection anywhere before joint replacement because it can cause prosthetic failure; clear it about 2-4 weeks before surgery. An infection anywhere in the body must be reported and treated first.")

q("postop", "A client is on post-op day 3 after total hip replacement. Which actions help prevent DVT? " + SATA,
 ["*Keep SCDs on while in bed",
  "*Give the anticoagulant as prescribed",
  "*Help the client walk as ordered",
  "Keep the client on bed rest for a week || Increases DVT risk.",
  "Place a pillow under the knees || Not a DVT prevention measure."],
 "DVT prevention: SCDs, anticoagulant and early ambulation. DVT/PE risk peaks up to 2 weeks; prophylaxis lasts about 1 month.")

q("hip", "A client 1 day after posterior-approach total hip replacement wants to pick up a dropped phone from the floor. Which nursing response is best?",
 ["'Bend forward slowly to reach it.' || Flexion past 90 degrees risks dislocation.",
  "*'Use the long-handled grabber so you don't bend past 90 degrees.'",
  "'Cross your legs to steady yourself first.' || No crossing legs.",
  "'Sit in the low chair so you're closer.' || Low chairs increase hip flexion."],
 "Hip precautions: no flexion past 90 degrees, no crossing legs, keep abducted, raised toilet seat and a long-handled grabber.")

q("knee", "A nurse plans care for a client returning from total knee replacement. Which interventions fit? " + SATA,
 ["*Apply ice packs in the first 24 hours",
  "*Use a knee immobilizer to keep extension as ordered",
  "*Progress range of motion with bending and full extension",
  "Keep the knee bent on pillows for comfort || Promotes contracture.",
  "Place an abduction pillow between the legs || That is for hip replacement."],
 "Knee replacement: prevent scar tissue and contracture with progressive ROM, bending and full extension; ice packs first 24 hours; knee immobilizer may maintain extension initially.")

q("wb", "Two clients had hip replacement yesterday. Which client is more likely to have a non-weight-bearing or toe-touch order at first?",
 ["*The client with a press-fit (uncemented) hip",
  "The client with a cemented hip || Cemented hips often tolerate PWB/FWB.",
  "Both, for 3 months of bed rest || Bed rest is not ordered.",
  "Neither; weight-bearing orders need not be checked || Always check the order first."],
 "Know the ordered weight-bearing status first. Press-fit is porous and bone grows in over about 3 months, so it may need NWB or toe-touch; cemented hips often tolerate PWB/FWB.")
