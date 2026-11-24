T = "e2w52"; SET = "20261124"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# bone
q("bone", "A 22-year-old college student asks the nurse why she should focus on bone health now. Which response is accurate?",
  ["'Bone formation speeds up steadily after age 30.' || After about 30, resorption increases",
   "'Osteoclasts build most of your bone in young adulthood.' || Osteoblasts build bone; osteoclasts resorb",
   "*'Peak bone mass is built around 25 to 35; after about 30, resorption increases.'",
   "'Bone mass stays the same throughout your whole life.' || Bone mass decreases after about 30"],
  "Growth and removal balance until about age 30; after that, resorption increases and bone mass decreases. Peak bone mass is built around ages 25 to 35. Osteoblasts build bone.")

# calreg
q("calreg", "A nurse is reviewing calcium regulation. Which hormone keeps calcium in bone?",
  ["PTH (parathyroid hormone) || PTH pulls calcium from bone into the blood",
   "High serum phosphorus || High phosphorus lowers calcium, so calcium is pulled from bone",
   "*Calcitonin",
   "Increased osteoclast activity || Osteoclasts cause bone resorption"],
  "Calcitonin keeps calcium IN bone. PTH pulls calcium FROM bone when serum calcium is low. Rising phosphorus lowers calcium, and calcium is pulled from bone.")

# risk
q("risk", "A nurse is reviewing the history of a 62-year-old client. Which factors increase this client's osteoporosis risk? " + SATA,
  ["*Long-term anticonvulsant use",
   "Walking 30 minutes, 3 times a week || Weight-bearing exercise protects bone",
   "*Drinking alcohol",
   "*Heavy caffeine intake",
   "Taking calcium and vitamin D as directed || These support bone health"],
  "PPIs (proton pump inhibitors), steroids and anticonvulsants increase calcium excretion; smoking, alcohol, caffeine and soda impair absorption; kidney disease raises phosphorus.")

# present
q("present", "A 68-year-old woman tells the nurse, 'I think I'm shrinking; my pants are suddenly too long.' Which understanding guides the nurse's response?",
  ["Height loss comes from cartilage wearing down in the knees || It reflects spinal spongy bone loss",
   "*Height loss is an early sign, since spongy bone in the spine is affected first",
   "Height loss is a late sign that follows changes in the skull || It is one of the earliest signs",
   "Height loss is normal aging and is unrelated to bone loss || It is an early osteoporosis sign"],
  "Loss of height (2 to 3 inches) is one of the earliest signs of osteoporosis because spongy (cancellous) bone in the spine, ribs, pelvis and wrist is affected first.")

# dexa
q("dexa", "A 67-year-old client is scheduled for a DEXA (dual-energy x-ray absorptiometry) scan. Which statements by the nurse are accurate? " + SATA,
  ["*'The scan is noninvasive and painless.'",
   "'A routine x-ray would find bone loss sooner than this.' || X-ray misses loss until about 25% is gone",
   "*'It uses a very low amount of radiation.'",
   "*'It compares your bone to peak bone mass at about age 30.'",
   "'A T-score of -1.5 would mean you have osteoporosis.' || -1 to -2.5 is osteopenia"],
  "DEXA is the gold-standard screening test: noninvasive, painless, very low radiation, comparing to peak bone mass at about age 30. T-scores: 0 to -1 normal; -1 to -2.5 osteopenia; below -2.5 osteoporosis.")

# bisphos
q("bisphos", "A nurse is reviewing orders for alendronate. For which client should the nurse question the order?",
  ["A 71-year-old woman with a T-score of -2.7 || Osteoporosis is the indication",
   "A client who can stay upright for 30 minutes || Staying upright is required, not a concern",
   "*A 66-year-old client with GERD (gastroesophageal reflux disease)",
   "A client who will take it with 8 oz of water || That is correct administration"],
  "Alendronate is taken on an empty stomach about 30 minutes before eating with 8 oz of water, staying upright 30 minutes to prevent esophagitis. It is not for clients with GERD.")

# calcitonin
q("calcitonin", "A client using calcitonin nasal spray says, 'I keep it in the fridge and use one spray in my right nostril every morning.' Which correction should the nurse make?",
  ["'Use two sprays in each nostril every morning.' || The dose is one spray daily",
   "'You can stop your calcium and vitamin D now.' || Calcium and vitamin D are continued",
   "'Spray it while it's still cold from the fridge.' || It is used at room temperature",
   "*'Switch nostrils each day instead of using the same one.'"],
  "Calcitonin nasal spray is one spray daily, alternating nostrils, stored in the fridge but used at room temperature; continue calcium and vitamin D. Ask about salmon allergy first.")

# othermeds
q("othermeds", "Which statement about osteoporosis medication classes is accurate?",
  ["SERMs (selective estrogen receptor modulators) stimulate osteoblasts || PTH analogs stimulate osteoblasts",
   "*RANKL (receptor activator of nuclear factor kappa-B ligand) inhibitors block osteoclasts",
   "PTH (parathyroid hormone) analogs mainly block bone breakdown || PTH analogs build bone",
   "Denosumab is taken by mouth once every day || Denosumab is SQ every 6 months"],
  "RANKL inhibitors (denosumab, SQ every 6 months) and bisphosphonates block breakdown; PTH analogs stimulate osteoblasts; SERMs mimic estrogen, with an emphasized clot risk.")

# diet
q("diet", "A nurse is teaching about calcium and vitamin D. Which factors interfere with calcium absorption or vitamin D synthesis? " + SATA,
  ["*Drinking coffee with calcium-rich meals",
   "Drinking a glass of milk || Milk is a calcium source",
   "*Living in a cloudy, rainy region",
   "*Dark skin pigment",
   "Walking outdoors in the sunshine || Sunlight supports vitamin D synthesis"],
  "Tannins and oxalic acid in tea, iced tea and coffee interfere with calcium; fat also reduces access. Sunscreen, cloudy or rainy regions and dark skin pigment reduce vitamin D synthesis.")

# exercise
q("exercise", "A 72-year-old client with osteoporosis asks which exercise plan will help her bones most. Which plan should the nurse recommend?",
  ["Swimming laps daily || Swimming is not the weight-bearing choice listed",
   "Seated stretching only || Stretching alone is not weight-bearing",
   "*Biking 30 minutes, 3 times a week",
   "Bed rest to protect fragile bones || Inactivity does not keep calcium in bone"],
  "Weight-bearing exercise such as walking, biking or weight training 30 minutes 3 times a week helps; muscle contraction against bone increases density and keeps calcium in bone.")

# falls
q("falls", "A 78-year-old client with osteoporosis takes an antihypertensive and a sedating sleep aid. Which action by the nurse best reduces injury risk?",
  ["*Review the antihypertensive and sedating drugs with the provider",
   "Encourage short sessions of high-impact jumping || High-impact jumping is not a safe measure here",
   "Add scatter rugs over hard floors for cushioning || Scatter rugs should be removed",
   "Advise the client to limit all activity at home || Weight-bearing activity is encouraged"],
  "Fall prevention is of utmost importance; most injuries happen at home. Review antihypertensives (orthostasis) and sedating medications, remove scatter rugs and ensure good lighting.")

# vertebro
q("vertebro", "A 74-year-old client has a vertebral compression fracture more than 3 months old that has not improved with rest, pain management and bracing. Which procedure fits best?",
  ["Vertebroplasty, which is used for recent fractures || Vertebroplasty is for recent fractures",
   "Spinal fusion as the next standard step || Not the listed next step",
   "*Kyphoplasty, using a balloon followed by cement",
   "Traction to realign the fractured vertebra || Not a listed approach"],
  "Conservative care comes first. If it fails, vertebroplasty (cement) is used for recent fractures, and kyphoplasty (balloon then cement) for older fractures more than 3 months old.")

# procedure
q("procedure", "A client has just returned from vertebroplasty. Which assessment is the nurse's priority?",
  ["Serum calcium level || Not the post-procedure priority",
   "Repeat DEXA (dual-energy x-ray absorptiometry) scan || Not a post-procedure priority",
   "Spinal range-of-motion exercises || Not the post-procedure priority",
   "*Neurovascular assessment"],
  "The post-op priority after vertebroplasty is neurovascular assessment. Also watch for a halo sign on the dressing with headache (CSF leak). Before the procedure: NPO, consent validated, blood thinners stopped about 5 to 7 days.")
