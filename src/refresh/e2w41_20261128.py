T = "e2w41"; SET = "20261128"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("path", "A nurse reviews how a pain impulse travels after a client cuts a finger. Which sequence is correct?", [
  "Brain to spinal cord to nociceptors to injured cells || The pathway runs toward the brain",
  "*Injured cells to nociceptors to spinal cord to brain",
  "Nociceptors to injured cells to brain to spinal cord || Injury comes first",
  "Spinal cord to injured cells to brain to nociceptors || Injury comes first"],
  "Injury releases substance P, bradykinins, histamine and prostaglandins, which stimulate nociceptors, sending the impulse to the spinal cord and then the brain.")

q("inflam", "A client's sprained wrist is swollen. Which part of the inflammatory response does the nurse link to the swelling?", [
  "Vasodilation || Vasodilation causes redness and warmth",
  "*Increased capillary permeability",
  "Sensitized nerve endings || Sensitized nerve endings cause pain",
  "Release of endorphins || Endorphins are natural painkillers"],
  "In inflammation, vasodilation causes redness and warmth, increased capillary permeability causes swelling and edema, and sensitized nerve endings cause pain.")

q("cox1", "A 72-year-old client has taken naproxen daily for a year. Which findings should the nurse report? " + SATA, [
  "*Black, tarry stools",
  "*A rising serum creatinine",
  "*Bleeding gums when brushing",
  "Mild drowsiness in the afternoon || Not a listed COX-1 effect",
  "Blood pressure rising from vasoconstriction || Vasoconstriction is a COX-2 effect"],
  "COX-1 normally protects gastric mucosa, supports platelet aggregation and kidney function. Blocking it causes GI ulcer and bleeding and kidney dysfunction. Hypertension, clots, MI and stroke are COX-2 effects.")

q("cox2", "A nurse reviews a client's new prescription for celecoxib. Which part of the history most concerns the nurse?", [
  "A history of seasonal allergies || Not a listed concern for this drug",
  "A history of frequent heartburn || GI ulcer is a COX-1 effect",
  "*A history of a previous blood clot",
  "A history of gout in the big toe || Gout is treated separately"],
  "COX-2 inhibitors such as celecoxib increase platelet aggregation and cause vasoconstriction, leading to hypertension, clots, MI and stroke.")

q("apap", "A client with a fever and a swollen, painful knee takes acetaminophen and asks why the swelling has not changed. Which response is accurate?", [
  "'The dose is too low to reduce the swelling.' || It never reduces inflammation",
  "*'Acetaminophen does not reduce inflammation.'",
  "'It blocks COX-1 in the joint tissue.' || It works only in the CNS",
  "'Swelling always takes a week to respond.' || The drug does not treat swelling"],
  "Acetaminophen works only in the CNS: it blocks spinal pain pathways and acts on the hypothalamus to reduce fever. It does not reduce inflammation.")

q("opioid", "A 48-year-old client is starting scheduled hydromorphone after surgery. Which teaching point should the nurse include?", [
  "'Expect loose stools while taking this drug.' || Opioids cause constipation",
  "'Expect to feel more alert than usual.' || Opioids cause sedation",
  "'Expect your blood pressure to climb.' || Opioids cause hypotension",
  "*'We will start measures to prevent constipation.'"],
  "Opioid receptors in the GI tract decrease GI motility, causing constipation. Other effects include sedation, hypotension, respiratory depression and euphoria.")

q("nalox", "A client receiving IV morphine becomes very drowsy with shallow, slow breathing. Which drug does the nurse prepare, and why?", [
  "Tramadol, because it reverses sedation || Tramadol is an opioid analgesic",
  "Fentanyl, because it restores comfort || Fentanyl is an agonist and worsens this",
  "*Naloxone, because it blocks the opioid response",
  "Celecoxib, because it replaces the opioid || Celecoxib does not reverse opioids"],
  "Opioid agonists suppress brainstem respiratory centers. Naloxone is the opioid antagonist: it binds the receptor to block or reverse the response.")

q("gout", "A client with gout is choosing from a restaurant menu. Which choice shows a need for more teaching?", [
  "A garden salad with vinaigrette || Low in purines",
  "*Fried shrimp with a cold beer",
  "Grilled vegetables over rice || Low in purines",
  "A baked potato with broccoli || Low in purines"],
  "Purines break down into uric acid, which deposits as crystals in joint spaces, especially the big toe. High-purine foods include red meat, organ meat, beer and seafood.")

q("allo", "A client taking allopurinol reports flank pain and painful urination. What does the nurse suspect?", [
  "A gastric ulcer from the drug || GI ulcer is a COX-1 inhibitor effect",
  "Liver damage from the drug || Hepatotoxicity is an acetaminophen concern",
  "*Uric acid renal stones",
  "Adrenal crisis from the drug || That follows abrupt glucocorticoid withdrawal"],
  "Allopurinol lowers uric acid, and more uric acid excreted by the kidneys raises the risk of uric acid renal stones. Teach increased fluid intake.")

q("gluco", "A 57-year-old client has taken prednisone for 8 months. Which finding should the nurse report first?", [
  "A 5-pound weight gain with mild ankle edema || Fluid retention is an expected effect",
  "*A temperature of 101.8 F with a productive cough",
  "A fasting blood glucose of 142 mg/dL || Hyperglycemia is an expected effect",
  "Mild weakness in the thigh muscles || Muscle wasting is an expected effect"],
  "Glucocorticoids cause immunosuppression, so signs of infection are the priority. Other effects include hyperglycemia, muscle wasting, bone demineralization, fluid retention and weight gain.")

q("taper", "A client who stopped long-term prednisone abruptly 2 days ago arrives at the clinic. Which findings support adrenal crisis? " + SATA, [
  "*A blood pressure of 82/50 mm Hg",
  "*A blood glucose of 52 mg/dL",
  "*Vomiting since yesterday",
  "*New confusion about the date",
  "A blood pressure of 168/94 mm Hg || Adrenal crisis causes hypotension"],
  "Long-term glucocorticoids suppress endogenous production, so abrupt withdrawal causes adrenal crisis: hypotension, hypoglycemia, fever, confusion and vomiting. Taper slowly.")
