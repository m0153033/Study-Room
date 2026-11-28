T = "e2w61"; SET = "20261128"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("fiveps", "Six hours after a long-leg cast is applied, a 42-year-old mail carrier reports new tingling in the toes. Which action is best?",
 ["Document it as an expected finding || Paresthesia is an early warning sign.",
  "Recheck tomorrow if pulses are present || Don't wait; report 5-P changes.",
  "*Report this early neurovascular change",
  "Wait until the toes become pale and cool || Waiting misses the early sign."],
 "5 Ps: pain, pallor/poikilothermia, paresthesia, pulselessness, paralysis. Paresthesia is early; pulselessness/paralysis are late.")

q("painscale", "Which pairings of client and pain scale are appropriate? " + SATA,
 ["*FLACC for a nonverbal adult with dementia",
  "Wong-Baker for an unresponsive older adult || FLACC fits nonverbal/impaired adults.",
  "*Wong-Baker for a 5-year-old who can point",
  "Numeric 0–10 for a cognitively impaired adult || FLACC fits impaired clients."],
 "FLACC (Face, Legs, Activity, Cry, Consolability) for nonverbal/impaired or young children; Wong-Baker for kids who can point.")

q("labs", "Three weeks after a tibial fracture, a client's ALP is elevated. How does the nurse interpret this?",
 ["Ongoing muscle destruction || CK and myoglobin show muscle destruction.",
  "*Expected bone healing activity",
  "Active inflammation in the limb || CRP/ESR show inflammation.",
  "Need for an MRI of the fracture || MRI shows soft tissue, not ALP."],
 "ALP = bone healing; CK + myoglobin = muscle destruction; CRP/ESR = inflammation.")

q("soft", "A 26-year-old soccer player overstretched a hamstring muscle during a game. Which term does the nurse use?",
 ["Sprain || A sprain is a ligament injury.",
  "*Strain",
  "Subluxation || Partial joint displacement, as in nursemaid elbow.",
  "Bursitis || Not an overstretched muscle."],
 "Strain = muscle/tendon. Sprain = ligament (bone to bone). POLICE for care.")

q("fxtype", "Which pairings of fracture type and description are correct? " + SATA,
 ["*Spiral: a twisting break",
  "Comminuted: a partial break in children || Comminuted = more than 3 fragments.",
  "*Open: bone penetrates the skin",
  "Greenstick: more than 3 bone fragments || Greenstick = partial break."],
 "Spiral = twisting (assess children for abuse); open = bone through skin, highest infection risk; greenstick = partial break; comminuted = >3 fragments.")

q("healing", "A client asks what happens after the hematoma forms at a fracture site. Which stage comes next?",
 ["Callus formation || Callus follows granulation.",
  "*Granulation",
  "Consolidation/remodeling || This is the final stage.",
  "True bone formation || Follows callus formation."],
 "Hematoma (24–72 hr) → granulation → callus (3–6 wk) → true bone → consolidation/remodeling (up to 1 yr).")

q("cast", "Two hours after a plaster arm cast is applied, the client says, 'It feels warm.' Which response is best?",
 ["*'Plaster gives off heat as it dries over about 24 hours.'",
  "'Warmth means infection; I'll call the provider now.' || Heat is expected while drying.",
  "'The cast is fully dry, so warmth is unexpected.' || Plaster takes ~24 hr to dry.",
  "'Warmth means it's too tight; I'll trim the edges.' || Heat is expected while drying."],
 "Plaster takes ~24 hr to dry, is hot and absorbs drainage. Fiberglass dries quickly.")

q("traction", "Which nursing action is specific to a client in skeletal traction rather than skin traction?",
 ["Keeping the weights hanging freely || Applies to all traction.",
  "*Performing pin-site care",
  "Checking the Velcro boot fit || Velcro boot is skin traction.",
  "Keeping ropes in the pulleys || Applies to all traction."],
 "Skin traction: Velcro/boot, 5–10 lb. Skeletal traction: pins/tongs, 15–30 lb, with pin-site care.")

q("pins", "On day 5 after external fixation, which pin-site findings should the nurse report? " + SATA,
 ["*Drainage that is increasing each day",
  "*A foul odor at the pin site",
  "*Spreading redness around a pin",
  "Pins assessed every 8–12 hours || This is the correct schedule."],
 "Clear drainage in the first 48–72 hr can be normal; worsening drainage, odor or redness suggests infection (osteomyelitis/MRSA).")

q("amp", "Three days after a below-knee amputation, a client reports cramping in the missing foot. Which medication does the nurse anticipate?",
 ["Allopurinol || Not used for phantom limb pain.",
  "*Gabapentin",
  "Adenosine || Not used for phantom limb pain.",
  "Calcitonin || Not used for phantom limb pain."],
 "Phantom limb pain (burning, cramping, tingling) is treated with neuropathic/antiepileptic meds such as gabapentin or pregabalin.")

q("ampcare", "On day 3 after an above-knee amputation, a client asks to keep the residual limb on a pillow all day. Which response is best?",
 ["'Yes; keep it on a pillow until discharge.' || Elevate initially only.",
  "*'Lying prone 20–30 minutes every 3–4 hours helps prevent contracture.'",
  "'Sitting in a recliner most of the day is better.' || Promotes hip flexion contracture.",
  "'Keep the hip flexed on pillows for comfort.' || Promotes hip flexion contracture."],
 "Prevent hip flexion contracture: prone q3–4h for 20–30 min, alignment, firm mattress; elevate the residual limb initially only.")

q("crutch", "A client with a sprained right ankle is going DOWN stairs on crutches. Which instruction is correct?",
 ["'Lead with your good left leg.' || Down with the bad.",
  "*'Lead with your injured right leg.'",
  "'Step down with both legs together.' || Down with the bad.",
  "'Lean your armpits on the pads.' || Weight goes through the hands."],
 "Stairs: up with the good, down with the bad. Pads 1.5–2 in below the axilla; weight through the hands.")

q("acs", "Which findings are EARLY signs of acute compartment syndrome? " + SATA,
 ["*Pain out of proportion to the injury",
  "*Pain with passive stretch",
  "Pulselessness in the extremity || Late sign.",
  "*A tense compartment",
  "Tissue necrosis || Late sign."],
 "Early: pain out of proportion, pain with passive stretch, paresthesia, tense compartment. Late: pulselessness, paralysis, coolness, necrosis.")

q("fes", "Thirty hours after a femur fracture, a client becomes restless and short of breath. The nurse gives oxygen. Which test does the nurse anticipate next?",
 ["*ABGs",
  "Serum ALP || Reflects bone healing.",
  "CK level || Reflects muscle destruction.",
  "MRI of the femur || Shows soft tissue."],
 "Fat embolism (12–48 hr): lungs + brain + petechiae. ABCs, O2, ABGs.")

q("rhabdo", "A client with a crush injury has rhabdomyolysis. Which nursing actions are appropriate? " + SATA,
 ["*Give aggressive isotonic IV fluids",
  "Restrict fluids to protect the kidneys || Aggressive fluids are needed.",
  "*Keep strict intake and output",
  "Give a potassium supplement || Potassium is high in rhabdo.",
  "*Monitor the ECG"],
 "Rhabdo: myoglobin → AKI. Aggressive isotonic IV fluids (UO ~200–300 mL/hr), strict I&O, ECG for high K.")

q("carpal", "A client with long-standing carpal tunnel syndrome is assessed. Which finding suggests LATE disease?",
 ["Tingling in the thumb and index finger || Typical median nerve symptom.",
  "Symptoms worse at night || Common, not specifically late.",
  "*Thenar muscle atrophy",
  "Tingling with Phalen's test || A diagnostic test finding."],
 "Median nerve: thumb, index, middle, half ring; worse at night; thenar atrophy late.")
