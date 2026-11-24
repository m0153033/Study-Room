T = "e2w61"; SET = "20261124"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("fiveps", "A 15-year-old with a new forearm cast reports tingling and numbness in the fingers. How does the nurse interpret this?",
 ["A late sign showing permanent damage || Paresthesia is an early sign.",
  "*An early neurovascular warning sign to report",
  "An expected finding needing no follow-up || Report 5-P changes.",
  "A sign of normal bone healing || Signals neurovascular compromise."],
 "5 Ps: pain, pallor/poikilothermia, paresthesia, pulselessness, paralysis. Paresthesia early; pulselessness/paralysis late.")

q("painscale", "A 4-year-old who can point to pictures has a wrist fracture. Which pain scale fits best?",
 ["FLACC || For nonverbal/impaired clients or children who can't point.",
  "Numeric 0–10 || Wong-Baker fits a child who can point.",
  "Verbal descriptor || Wong-Baker fits a child who can point.",
  "*Wong-Baker faces"],
 "Wong-Baker for kids who can point; FLACC for nonverbal/impaired or young children. Reassess after analgesia.")

q("labs", "Which pairings of test and meaning are correct? " + SATA,
 ["*ALP: bone healing",
  "MRI: best view of a simple fracture || X-ray shows fracture; MRI shows soft tissue.",
  "*CRP/ESR: inflammation",
  "CT: best view of soft tissue || CT is for complex areas like pelvis/spine.",
  "*CK and myoglobin: muscle destruction"],
 "X-ray: fracture; CT: complex (pelvis/spine); MRI: soft tissue.")

q("soft", "A 33-year-old with an ankle sprain receives POLICE teaching. Which instruction is correct?",
 ["Ice continuously for several hours || Ice 10–15 min at a time.",
  "Strict non-weight-bearing for weeks || Controlled weight-bearing as tolerated.",
  "*Ice 10–15 minutes every few hours",
  "Keep the ankle below heart level || Elevation is part of POLICE."],
 "POLICE: Protection, Optimal Loading, Ice, Compression, Elevation. Sprain = ligament; strain = muscle/tendon.")

q("fxtype", "Which description matches a comminuted fracture?",
 ["*Bone broken into more than 3 fragments",
  "A partial break common in children || That's greenstick.",
  "Bone penetrating through the skin || That's open (compound).",
  "A twisting break of the bone || That's spiral."],
 "Comminuted = >3 fragments. Open fractures carry the highest infection risk; spiral in children → assess for abuse.")

q("healing", "A 78-year-old with a wrist fracture asks why healing takes longer than for a 22-year-old grandson. What is accurate?",
 ["'Everyone heals in about 1 week.' || Young adults take ~4–6 weeks.",
  "'Older adults heal faster than young adults.' || Older adults heal slower.",
  "'Healing takes about 3 days with rest.' || Far too short.",
  "*'Older adults often need 2–3 months or more; young adults about 4–6 weeks.'"],
 "Stages: hematoma → granulation → callus (3–6 wk) → true bone → consolidation/remodeling (up to 1 yr).")

q("cast", "Which reports from a client with a new cast should be reported to the provider? " + SATA,
 ["*A foul odor coming from the cast",
  "'I keep it elevated above my heart.' || Correct care, nothing to report.",
  "*The cast feels too tight",
  "Plaster feels warm while drying || Plaster is hot while it dries.",
  "*New numbness in the toes"],
 "Report 5-P changes, odor and tightness. Keep dry, elevate, nothing inside.")

q("traction", "During rounds on a client in skin traction, which finding requires the nurse to correct it?",
 ["Weights are hanging freely || Correct.",
  "*Ropes have slipped out of the pulleys",
  "Body is in proper alignment || Correct.",
  "Velcro boot with 5–10 lb applied || Expected for skin traction."],
 "Weights hang freely, ropes in pulleys, alignment maintained. Skeletal traction: pins/tongs, 15–30 lb.")

q("pins", "Day 2 after external fixation, a pin site has a small amount of clear drainage without odor. Interpretation?",
 ["Definite osteomyelitis; pins must be removed || Early clear drainage can be normal.",
  "Pin sites now only need weekly checks || Assess every 8–12 hours.",
  "*Can be normal in the first 48–72 hours; keep assessing",
  "More traction weight is needed || Unrelated to drainage."],
 "Worsening drainage, odor or redness → infection (osteomyelitis/MRSA). Monitor distal 5 Ps.")

q("amp", "Two hours after a below-knee amputation, which finding needs the nurse's immediate action?",
 ["Burning sensation in the missing foot || Phantom pain; not life-threatening.",
  "Asking when a prosthesis will be fitted || Address later.",
  "*BP 84/48, HR 130, pale skin",
  "Incisional pain rated 4/10 || Manage, but not the priority."],
 "Hemorrhage/shock: hypotension, tachycardia, pallor, low H/H.")

q("ampcare", "Which actions help prevent hip flexion contracture after an above-knee amputation? " + SATA,
 ["*Prone position 20–30 min every 3–4 hours",
  "Residual limb on a pillow at all times || Elevate only initially.",
  "*Firm mattress",
  "Sitting in a recliner most of the day || Promotes hip flexion.",
  "*Maintain body alignment"],
 "ABCs/vitals first post-op, then bleeding, infection, pain, contracture prevention and psychosocial support.")

q("crutch", "Which observation shows correct crutch fit and use?",
 ["Pads pressing firmly into the axilla || Pads sit 1.5–2 in below the axilla.",
  "Body weight resting on the armpits || Weight goes through the hands.",
  "Crutch tips 1 inch to the side || About 6 in to the side, 2 in in front.",
  "*Elbows flexed about 30 degrees"],
 "Stairs: up with the good, down with the bad.")

q("acs", "A client with a casted tibial fracture has suspected compartment syndrome. Which actions are correct? " + SATA,
 ["*Remove restrictive dressings",
  "Elevate the leg well above the heart || Keep at heart level only.",
  "*Keep the extremity at heart level",
  "Recheck the 5 Ps in 4 hours || Check every 15 minutes.",
  "*Notify the provider and prepare for fasciotomy"],
 "Early: pain out of proportion, pain with passive stretch, paresthesia, tense compartment. Late: pulselessness, paralysis.")

q("fes", "A 20-year-old is 36 hours post femur fracture with suspected fat embolism syndrome. Which finding often appears LAST?",
 ["Shortness of breath || Lung involvement isn't typically last.",
  "*Petechiae",
  "Confusion || Brain involvement isn't typically last.",
  "Pain with passive stretch || Suggests compartment syndrome."],
 "FES 12–48 hr: lungs + brain + petechiae. ABCs, O2, ABGs.")

q("rhabdo", "A crush-injury client with rhabdomyolysis is placed on a cardiac monitor. What is the reason?",
 ["Myoglobin causes hypoglycemia || Not the danger.",
  "Fat emboli travel to the heart || That's fat embolism.",
  "*High potassium can cause dysrhythmias",
  "To track urine output || Strict I&O does that."],
 "Myoglobin → AKI. Aggressive isotonic IV fluids, UO ~200–300 mL/hr, ECG for high K.")

q("carpal", "The nurse taps over the median nerve at the wrist and the client feels tingling. Which test is this?",
 ["*Tinel's",
  "Phalen's || That's wrist flexion for 60 seconds.",
  "Homans' || Not a carpal tunnel test.",
  "Trendelenburg || Not a carpal tunnel test."],
 "Median nerve: thumb, index, middle, half ring; worse at night; thenar atrophy late.")
