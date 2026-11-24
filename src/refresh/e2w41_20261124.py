T = "e2w41"; SET = "20261124"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("path", "A 54-year-old client after hip surgery asks, 'Why do I need pain medicine if my body makes its own painkillers?' Which response is best?",
  ["'Your body only makes substance P, which causes pain.' || substance P stimulates nociceptors",
   "'Your body makes no natural painkillers at all.' || the brain releases endorphins and others",
   "*'Your natural painkillers often aren't enough for severe pain.'",
   "'Histamine is your body's main painkiller.' || histamine stimulates nociceptors"],
  "The brain releases serotonin, enkephalins and endorphins as natural painkillers, but they are often not enough for severe or chronic pain.")

q("inflam", "A nurse teaches about the signs of inflammation after a sprained ankle. Which pairings are correct? " + SATA,
  ["*Vasodilation — redness and warmth",
   "Sensitized nerve endings — warmth || sensitized nerve endings cause pain",
   "*Increased capillary permeability — swelling",
   "*Sensitized nerve endings — pain",
   "Vasodilation — swelling only || vasodilation causes redness and warmth"],
  "Vasodilation causes redness and warmth, increased capillary permeability causes swelling/edema, and sensitized nerve endings cause pain.")

q("cox1", "A 67-year-old client with diabetes takes ibuprofen daily for arthritis. Which body function does the nurse monitor most closely?",
  ["Liver function || liver damage is the acetaminophen danger",
   "*Kidney function",
   "Uric acid level || uric acid relates to gout",
   "Blood glucose level || hyperglycemia is a glucocorticoid effect"],
  "COX-1 supports kidney function; blocking it causes kidney dysfunction, with higher risk in diabetes. It also causes GI ulcer and bleeding.")

q("cox2", "A nursing student compares COX-1 and COX-2 inhibitors. Which statement is correct?",
  ["COX-2 inhibitors mainly cause GI (gastrointestinal) bleeding || that is COX-1",
   "COX-1 inhibitors increase platelet aggregation || COX-1 inhibitors decrease it",
   "COX-2 inhibitors cause vasodilation || they cause vasoconstriction",
   "*COX-2 inhibitors raise clot risk; COX-1 inhibitors raise bleeding risk"],
  "COX-2 inhibitors (celecoxib) increase platelet aggregation and cause vasoconstriction → hypertension, clots, MI, stroke. COX-1 inhibitors (aspirin, ibuprofen, naproxen) decrease platelet aggregation → bleeding.")

q("apap", "A 40-year-old client is taking acetaminophen for back pain. Which client statement shows correct understanding?",
  ["'It will bring down the swelling in my knee.' || acetaminophen does not reduce inflammation",
   "*'Drinking alcohol raises my liver risk with this drug.'",
   "'I can go above 4,000 mg a day if pain is bad.' || 4,000 mg is the maximum daily dose",
   "'It works by blocking COX-1 in my stomach.' || it works only in the CNS"],
  "Acetaminophen works only in the CNS (central nervous system) and does not reduce inflammation. Maximum daily dose is 4,000 mg; the main danger is hepatotoxicity, and alcohol increases liver risk.")

q("opioid", "A nurse is caring for a client receiving scheduled morphine. Which nursing actions address expected opioid effects? " + SATA,
  ["*Monitor respiratory rate",
   "*Monitor blood pressure for hypotension",
   "Plan for expected diarrhea || opioids decrease GI motility",
   "*Plan measures to prevent constipation",
   "Expect increased alertness || opioids cause sedation"],
  "Opioid agonists cause respiratory depression, hypotension (decreased vascular resistance), sedation, euphoria and constipation (decreased GI motility).")

q("nalox", "A nurse reviews a medication list. Which group contains only opioid agonists?",
  ["Morphine, naloxone and fentanyl || naloxone is an antagonist",
   "Naloxone, celecoxib and hydromorphone || naloxone is an antagonist; celecoxib is a COX-2 inhibitor",
   "*Morphine, fentanyl and hydromorphone",
   "Fentanyl, allopurinol and naloxone || allopurinol is an antihyperuricemic"],
  "An agonist binds a receptor to cause a response (morphine, fentanyl, hydromorphone). An antagonist (naloxone) binds to block or reverse the response.")

q("gout", "A 50-year-old client with gout asks why beer should be limited. Which response is best?",
  ["*'Beer is high in purines, which raise uric acid.'",
   "'Beer blocks COX-1 and harms your stomach.' || the gout concern is purines",
   "'Beer lowers uric acid too much.' || purines raise uric acid",
   "'Beer only matters if you take acetaminophen.' || beer is a high-purine food"],
  "Purines break down into uric acid, which deposits as crystals in joints, especially the big toe. High-purine foods include red meat, organ meat, beer and seafood.")

q("allo", "A nurse compares allopurinol with ibuprofen for a client with gout. Which statement is accurate?",
  ["Allopurinol blocks COX-1 like ibuprofen || it decreases uric acid",
   "*Allopurinol lowers uric acid, which raises renal-stone risk",
   "Allopurinol stimulates opioid receptors || that is opioid agonists",
   "Allopurinol works by mimicking cortisol || that is glucocorticoids"],
  "Antihyperuricemics like allopurinol decrease uric acid; more uric acid excreted by the kidneys raises the risk of renal stones, so teach increased fluids.")

q("gluco", "A 61-year-old client has taken prednisone for many months. Which assessment findings does the nurse recognize as glucocorticoid effects? " + SATA,
  ["*Elevated blood glucose",
   "*Weight gain with fluid retention",
   "Steady weight loss || glucocorticoids cause weight gain",
   "*Muscle wasting",
   "*Bone demineralization"],
  "Glucocorticoid effects include immunosuppression, hyperglycemia, muscle wasting, bone demineralization, fluid retention and weight gain.")

q("taper", "Which client does the nurse recognize as at greatest risk for adrenal crisis?",
  ["A client finishing a slow prednisone taper || tapering prevents crisis",
   "A client taking acetaminophen for a fever || acetaminophen doesn't suppress the adrenals",
   "A client starting prednisone today || suppression comes with long-term use",
   "*A client who abruptly stopped long-term prednisone"],
  "Long-term glucocorticoids suppress endogenous production; abrupt withdrawal causes adrenal crisis (hypotension, hypoglycemia, fever, confusion, vomiting). Taper slowly.")
