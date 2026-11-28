T = "e2w52"; SET = "20261128"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("bone", "A nursing student is reviewing bone cells and bone mass. Which statement by the student needs correction?",
 ["'Osteoblasts are the cells that build bone.' || This statement is accurate.",
  "*'Osteoclasts are the cells that build new bone.'",
  "'After about age 30, resorption increases.' || This statement is accurate.",
  "'Peak bone mass is built around ages 25 to 35.' || This statement is accurate."],
 "OsteoBlasts build bone; osteoclasts carry out resorption. Growth and removal balance until about age 30; after that resorption increases and bone mass decreases. Peak bone mass is built around 25 to 35.")

q("calreg", "A nurse is reviewing calcium regulation with a study group. Which pairing is correct?",
 ["PTH: keeps calcium in bone || PTH pulls calcium from bone when serum calcium is low.",
  "*Calcitonin: keeps calcium in bone",
  "High phosphorus: raises serum calcium || Rising phosphorus lowers calcium.",
  "Calcitonin: pulls calcium from bone || PTH pulls calcium from bone."],
 "Calcitonin keeps calcium in bone. PTH pulls calcium from bone into the blood when serum calcium is low. Rising phosphorus lowers calcium, and calcium is pulled from bone.")

q("risk", "A nurse at a community clinic is reviewing histories. Which client has the most osteoporosis risk factors?",
 ["A client who walks 30 minutes, 3 times a week || Weight-bearing exercise is protective.",
  "*A client who smokes and takes a long-term PPI",
  "A client who takes calcium and vitamin D || Supplements as directed are not a risk factor.",
  "A client who bikes and drinks mostly water || These are not listed risk factors."],
 "PPIs, steroids and anticonvulsants increase calcium excretion; smoking, alcohol, caffeine and soda impair absorption; kidney disease raises phosphorus.")

q("present", "A nursing student asks why bone in osteoporosis takes on a honeycomb appearance. Which explanation by the nurse is accurate?",
 ["'Compact bone thickens and fills with holes.' || Spongy bone is affected first.",
  "*'Resorption exceeds formation in spongy bone.'",
  "'Cartilage replaces the bone inside the spine.' || Cartilage does not replace bone.",
  "'Bone stores too much calcium and swells.' || Bone is losing mass, not overstoring calcium."],
 "Osteoporosis begins in spongy (cancellous) bone of the spine, ribs, pelvis and wrist, which takes on a honeycomb appearance as resorption exceeds formation. Loss of height is an early sign.")

q("dexa", "A 66-year-old client asks why a DEXA scan was ordered instead of a regular x-ray. Which response by the nurse is best?",
 ["'A regular x-ray gives a more accurate T-score.' || DEXA is the gold-standard screening test.",
  "*'An x-ray may not show loss until about 25% is gone.'",
  "'DEXA is used because it is an invasive test.' || DEXA is noninvasive and painless.",
  "'DEXA compares your bone to bone at age 80.' || DEXA compares to peak bone mass at about 30."],
 "DEXA is the gold-standard screening test: noninvasive, painless and very low radiation, comparing to peak bone mass at about age 30. A routine x-ray misses loss until about 25% is lost.")

q("bisphos", "A 70-year-old client starting alendronate says, 'I'll take it with my morning coffee and then lie back down.' Which response by the nurse is best?",
 ["'That's fine, as long as you take it every day.' || Coffee and lying down are not safe with alendronate.",
  "*'Take it with 8 oz of water and stay upright 30 minutes.'",
  "'Take it at bedtime with a snack instead.' || It is taken on an empty stomach in the morning.",
  "'Lying down helps the drug absorb more fully.' || Staying upright prevents esophagitis."],
 "Alendronate is taken first thing in the morning on an empty stomach about 30 minutes before eating, with 8 oz of water, staying upright 30 minutes to prevent esophagitis. It is not for clients with GERD.")

q("calcitonin", "A client using calcitonin nasal spray says, 'Now that I'm on the spray, I can stop my calcium and vitamin D.' Which response by the nurse is best?",
 ["'Yes, the spray replaces both supplements.' || Calcium and vitamin D are continued.",
  "*'Keep taking calcium and vitamin D with the spray.'",
  "'Stop the vitamin D, but keep the calcium.' || Both calcium and vitamin D are continued.",
  "'Use two sprays instead of the supplements.' || The dose is one spray daily."],
 "Calcitonin nasal spray is a salmon derivative used as one spray daily, alternating nostrils, stored in the fridge but used at room temperature; calcium and vitamin D are continued.")

q("othermeds", "A 64-year-old client with osteoporosis is prescribed a SERM. Which teaching point should the nurse emphasize?",
 ["'This drug builds bone by stimulating osteoblasts.' || PTH analogs stimulate osteoblasts.",
  "'This drug is given SQ every 6 months.' || That describes denosumab, a RANKL inhibitor.",
  "*'Report possible blood clot symptoms promptly.'",
  "'This drug works by blocking osteoclasts directly.' || RANKL inhibitors block osteoclasts."],
 "SERMs mimic estrogen, increasing bone density and reducing resorption, with an emphasized clot risk. PTH analogs stimulate osteoblasts; RANKL inhibitors such as denosumab (SQ every 6 months) and bisphosphonates block breakdown.")

q("diet", "A nurse is helping a client with osteoporosis plan meals. Which choice best supports calcium absorption?",
 ["A calcium-rich meal with a glass of iced tea || Tannins and oxalic acid in tea interfere.",
  "A calcium-rich meal with a cup of coffee || Coffee interferes with calcium absorption.",
  "*A calcium-rich meal with a glass of water",
  "A calcium-rich meal that is very high in fat || Fat reduces access to calcium."],
 "Tannins and oxalic acid in tea, iced tea and coffee interfere with calcium absorption, and fat also reduces calcium access.")

q("exercise", "A nurse teaches a 69-year-old client with osteoporosis about exercise. Which client statement shows understanding?",
 ["'Bed rest will protect my fragile bones best.' || Weight-bearing exercise is recommended.",
  "*'I'll do weight training 30 minutes, 3 times a week.'",
  "'Seated stretching alone is all I need.' || Weight-bearing exercise is recommended.",
  "'Exercise pulls calcium out of my bones.' || Muscle pull keeps calcium in bone."],
 "Weight-bearing exercise such as walking, biking or weight training 30 minutes 3 times a week is recommended; muscle contraction against bone increases density and keeps calcium in bone.")

q("falls", "A home health nurse is planning care for an 80-year-old client with osteoporosis. Which actions reduce the client's injury risk? " + SATA,
 ["*Remove scatter rugs from the floors",
  "Limit the client to no activity at home || Limiting all activity is not advised.",
  "*Make sure the home has good lighting",
  "*Review sedating drugs with the provider",
  "Add soft rugs over hard floors || Scatter rugs increase fall risk."],
 "Fall prevention is of utmost importance; most injuries happen at home. Remove scatter rugs, ensure good lighting and review antihypertensives (orthostasis) and sedating medications.")

q("vertebro", "A 76-year-old client has a recent vertebral compression fracture that has not improved with rest, pain management and bracing. Which procedure does the nurse anticipate?",
 ["Kyphoplasty, used for fractures over 3 months old || Kyphoplasty is for older fractures.",
  "*Vertebroplasty, with cement for a recent fracture",
  "Spinal fusion as the standard next step || Spinal fusion is not the listed next step.",
  "Traction to realign the fractured vertebra || Traction is not the listed approach."],
 "Conservative care (rest, pain management, temporary bracing) comes first. If it fails, vertebroplasty (cement) is used for recent fractures, and kyphoplasty (balloon then cement) for fractures more than 3 months old.")

q("procedure", "A nurse is preparing a 71-year-old client for vertebroplasty. Which actions are appropriate? " + SATA,
 ["*Keep the client NPO as ordered",
  "Serve a full breakfast before the procedure || The client is kept NPO before the procedure.",
  "*Validate that consent has been obtained",
  "*Ask whether the client takes blood thinners",
  "Skip the consent check if the client agrees || The nurse validates consent."],
 "Before vertebroplasty: NPO, the nurse validates consent and screens for blood thinners, usually stopped about 5 to 7 days before. After: neurovascular assessment is the priority, and a halo sign with headache suggests a CSF leak.")
