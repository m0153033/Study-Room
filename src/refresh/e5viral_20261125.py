T = "e5viral"; SET = "20261125"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("basics", "A school nurse explains to a parent group why viral illnesses move quickly through a kindergarten class. Which factors should the nurse include? " + SATA,
  ["*Children's immune systems are still immature",
   "*Children are in close contact all day at school",
   "*Children often do not wash their hands well",
   "Children have thicker skin that traps viruses || Thicker skin is not a reason children are vulnerable",
   "*Some families have limited access to preventive care"],
  "Children are more vulnerable to viral infections because of immature immune systems, close contact at school or daycare, inadequate handwashing and limited access to preventive care.")

q("rota", "A toddler in a daycare center was diagnosed with rotavirus 2 days after a playdate. Which statement by the nurse about the illness is accurate?",
  ["*'Incubation is about 1 to 3 days, and it lingers on surfaces.'",
   "'It takes about 4 to 6 weeks before symptoms appear.' || That is the incubation period for mono",
   "'Symptoms appear 7 to 14 days after exposure.' || That is measles incubation",
   "'It cannot survive on toys or changing tables.' || Rotavirus persists on surfaces"],
  "Rotavirus incubation is 1-3 days. It is highly contagious, persists on surfaces, and spreads by the fecal-oral route through hands, surfaces, food or water.")

q("rotacare", "The nurse is planning care for a 15-month-old hospitalized with rotavirus. Which nursing interventions are appropriate? " + SATA,
  ["*Weigh diapers and record intake and output",
   "*Disinfect the crib rails and changing surface",
   "Place the child in a negative-pressure room || Rotavirus needs standard and contact precautions, not airborne",
   "*Offer oral rehydration solution frequently",
   "Hold all milk feedings until stools are formed || Breastfeeding or formula should continue"],
  "Rotavirus care includes oral rehydration, continuing breastfeeding or formula, monitoring stool frequency, intake and I&O, surface disinfection and contact precautions.")

q("rotacare", "A mother asks the clinic nurse whether the rotavirus vaccine is a shot like the others her baby received. Which response is best?",
  ["'It is one shot given at age 4 to 6 years.' || The rotavirus vaccine is oral and given in infancy",
   "'It is a yearly shot given each fall.' || The rotavirus vaccine is not annual",
   "*'It is given by mouth in a 2- or 3-dose series.'",
   "'There is no vaccine; only fluids can help.' || Oral rotavirus vaccines are available"],
  "The oral rotavirus vaccine is given in a 2- or 3-dose series.")

q("chicken", "A 9-year-old with chickenpox has scratched several lesions raw. Which comfort and safety measures should the nurse teach the parent? " + SATA,
  ["*Keep his fingernails trimmed short",
   "*Apply calamine lotion to itchy areas",
   "Give aspirin when he is uncomfortable || Aspirin is avoided because of Reye syndrome",
   "*Offer cool baths and encourage rest",
   "Send him back to school when the itching stops || He stays home until all lesions have crusted"],
  "Chickenpox care: calamine lotion, cool baths, trimmed nails and rest; avoid aspirin because of Reye syndrome, and keep the child home until all lesions have crusted.")

q("chicken", "A 7-year-old is admitted with fever, malaise and an itchy vesicular rash scattered over the trunk, face and arms. Which illness do these findings support?",
  ["Measles, with a rash moving down from the hairline || Measles rash is maculopapular and starts at the hairline",
   "*Chickenpox, the primary varicella-zoster virus infection",
   "Shingles, a reactivation of latent virus || Shingles is a unilateral dermatomal rash, usually in adults",
   "Mononucleosis, with a rash after amoxicillin || That rash follows amoxicillin in mono, not a vesicular rash"],
  "Chickenpox is the primary VZV infection, with fever, malaise and an itchy vesicular rash spread by air and contact with lesions.")

q("shingles", "A 73-year-old is seen for a new rash. Which description best supports herpes zoster?",
  ["Itchy vesicles scattered over the whole body || That pattern fits chickenpox",
   "A maculopapular rash moving from the face downward || That pattern fits measles",
   "*A painful band of vesicles along one dermatome on one side",
   "A rash that appeared after starting amoxicillin || That is a classic clue for mono"],
  "Shingles classically causes a unilateral, painful stripe of vesicles along a dermatome.")

q("shingles", "A 67-year-old whose shingles rash crusted 3 months ago still has burning pain in that area. Which statements by the nurse are accurate? " + SATA,
  ["*'This nerve pain can continue for months after the rash heals.'",
   "*'Gabapentin is one option for this type of pain.'",
   "'This means the rash is about to appear on your other side.' || Postherpetic neuralgia is not a new rash on the other side",
   "*'Analgesics or a tricyclic antidepressant may also be used.'",
   "'Pain this long after the rash means the virus reached your eye.' || Eye involvement causes vision changes, not lingering dermatomal pain"],
  "Postherpetic neuralgia is nerve pain continuing after the rash heals, sometimes for months; options include analgesics, gabapentin and TCAs.")

q("zostertx", "A 70-year-old started acyclovir for shingles yesterday. Which statement by the client indicates a need for more teaching?",
  ["'I'll drink plenty of fluids while taking this.' || Correct; hydration protects the kidneys",
   "'I'll take every dose until the prescription is finished.' || Correct; finish the full course",
   "*'I'll stop the medicine as soon as the blisters dry up.'",
   "'The clinic will check my kidney tests during treatment.' || Correct; kidney function is monitored"],
  "With acyclovir, monitor kidney function, encourage hydration and teach the client to finish the full course.")

q("vzvvax", "A parent asks when her 13-month-old will receive varicella vaccine doses. Which response is accurate?",
  ["'At birth and again at 2 months of age.' || Varicella doses are at 12-15 months and 4-6 years",
   "'Only at 11 to 12 years of age.' || That is not the varicella schedule",
   "*'Now, and again between 4 and 6 years of age.'",
   "'Every year, the same as a flu shot.' || Varicella vaccine is not annual"],
  "The two childhood varicella vaccine doses are given at 12-15 months and 4-6 years, the same timing as MMR.")

q("ebv", "A 16-year-old with a sore throat and fever develops a widespread rash after starting amoxicillin. Which statements by the nurse are accurate? " + SATA,
  ["*'This rash is a classic clue for mononucleosis.'",
   "*'It does not necessarily mean a true penicillin allergy.'",
   "'This confirms measles rather than mono.' || Measles rash starts at the hairline and follows Koplik spots",
   "*'Epstein-Barr virus serology can confirm the diagnosis.'",
   "'A negative Monospot would rule mono out completely.' || A Monospot can be falsely negative"],
  "A rash after amoxicillin is a classic EBV clue and isn't necessarily a true allergy; a Monospot can be falsely negative, so EBV serology confirms.")

q("spleen", "An 18-year-old with mononucleosis asks why the provider keeps checking her upper abdomen. Which response by the nurse is best?",
  ["'We are checking your posterior neck lymph nodes there.' || Those nodes are in the neck, not the abdomen",
   "*'Mono can enlarge the spleen, and an enlarged spleen can rupture.'",
   "'We are looking for the rash that follows amoxicillin.' || That rash is a skin finding, not an abdominal exam",
   "'Abdominal checks tell us when your fatigue will end.' || Fatigue may last weeks to months regardless"],
  "Mono can cause an enlarged spleen and liver; the enlarged spleen can rupture, so contact sports are avoided for 4-6 weeks.")

q("spleen", "A 20-year-old with mononucleosis arrives in the emergency department with sudden severe left upper quadrant pain. Which assessment finding most supports splenic rupture?",
  ["Posterior cervical lymph nodes that are tender || Lymphadenopathy is an expected mono finding",
   "*Pain referred to the left shoulder with pallor and tachycardia",
   "Profound fatigue that has lasted several weeks || Fatigue may last weeks to months with mono",
   "A sore throat that worsens when swallowing || Sore throat is an expected mono finding"],
  "Splenic rupture causes sudden severe LUQ pain radiating to the left shoulder (Kehr sign), with dizziness, tachycardia, pallor and hypotension.")

q("flu", "A 6-year-old with influenza has had vomiting and diarrhea along with fever and cough. The parent says this cannot be the flu. Which response by the nurse is accurate?",
  ["'You're right; stomach symptoms rule out influenza.' || Vomiting or diarrhea can occur with flu, especially in children",
   "'Vomiting means it must be rotavirus instead.' || Rotavirus causes severe watery diarrhea without flu respiratory findings",
   "*'Vomiting and diarrhea can occur with flu, especially in children.'",
   "'Flu never causes fever along with a cough.' || Abrupt fever and cough are typical flu findings"],
  "Influenza findings include abrupt fever and chills, myalgia, headache, cough, sore throat, and vomiting or diarrhea especially in children.")

q("flutx", "A client who started oseltamivir yesterday for influenza calls to report nausea and one episode of vomiting. Which response by the nurse is best?",
  ["'Stop the medicine right away; this is an allergic reaction.' || Nausea and vomiting are common adverse effects",
   "*'Nausea and vomiting are common with this medicine.'",
   "'That means the flu has turned into pneumonia.' || These are drug adverse effects, not signs of pneumonia",
   "'Double the next dose so the drug works faster.' || The dose should not be changed by the client"],
  "Oseltamivir ideally starts within 24-48 hours of symptoms, especially for high-risk clients; nausea and vomiting are common adverse effects.")

q("flutx", "The nurse is caring for a 62-year-old admitted with influenza. Which assessments are priorities? " + SATA,
  ["*Lung sounds",
   "*Oxygenation",
   "*Temperature and intake and output",
   "An Amsler grid assessment || That assesses vision, not influenza",
   "*Respiratory rate and work of breathing"],
  "Priority influenza assessments are respiratory rate and work of breathing, oxygenation, lung sounds, temperature and I&O.")

q("measles", "An unvaccinated 4-year-old has had 4 days of high fever, cough and red, watery eyes, and a rash has now appeared on the face near the hairline. Which statement by the nurse is accurate?",
  ["'The rash will stay on the face and will not spread.' || The measles rash spreads downward from the hairline",
   "'The rash should move from the feet upward next.' || The measles rash moves from the hairline down",
   "*'The maculopapular rash will now spread downward.'",
   "'The rash will stay on one side of the body.' || A one-sided dermatomal rash is shingles"],
  "The measles prodrome is 3-5 days of high fever, cough, conjunctivitis and Koplik spots, followed by a maculopapular rash that starts at the hairline/face and spreads downward.")

q("measles", "The nurse reviews possible complications of measles with the parents of a hospitalized child. Which complications should be included? " + SATA,
  ["*Otitis media",
   "*Pneumonia",
   "Hemorrhagic cystitis || Not a listed measles complication",
   "*Encephalitis",
   "*Complications in a pregnant contact"],
  "Measles complications include otitis media, pneumonia, encephalitis and pregnancy complications.")

q("measlescare", "The nurse sets up the room for a 2-year-old admitted with measles. Which actions are appropriate? " + SATA,
  ["*Dim the room lights",
   "*Set up a cool-mist humidifier",
   "*Elevate the head of the bed",
   "Keep the overhead lights bright to assess the rash || Bright light worsens photophobia",
   "*Notify public health about the case"],
  "Measles comfort care includes dimming lights for photophobia, a cool-mist humidifier, elevating the head of the bed, and fever management and hydration; airborne precautions are used and public health is notified.")

q("rsv", "A 2-month-old with RSV is on the pediatric unit. Which finding should the nurse report immediately?",
  ["A clear runny nose with occasional sneezing || A mild runny nose alone is not a distress sign",
   "Fussiness that settles when the parent holds her || Not a priority sign of respiratory distress",
   "*A 20-second pause in breathing during a feeding",
   "Six wet diapers since the start of the shift || This reflects adequate hydration"],
  "Priority signs of respiratory distress in infants with RSV are apnea, retractions, nasal flaring, tachypnea and wheezing.")

q("rsv", "A 68-year-old with COPD asks why RSV would be more serious for him than for his healthy grandson. Which response is accurate?",
  ["'RSV only affects infants, so you have nothing to worry about.' || Older adults and those with chronic illness are at higher risk",
   "'Adults with lung disease recover faster from RSV.' || Chronic lung disease raises risk of severe RSV",
   "*'RSV can cause pneumonia or worsen your chronic lung disease.'",
   "'RSV in adults is only a risk during the summer months.' || RSV is most common from fall to early spring"],
  "Adults at higher risk for severe RSV include older adults and those with COPD, CHF or asthma, diabetes or severe obesity, and immunocompromised clients; severe RSV can cause pneumonia or worsen chronic disease.")

q("rsvprev", "A term newborn's mother did not receive the RSV vaccine during pregnancy, and the baby is entering her first RSV season. Which intervention should the nurse anticipate?",
  ["*A long-acting monoclonal antibody such as nirsevimab",
   "Oseltamivir given daily through the season || Oseltamivir is for influenza",
   "The MMR vaccine before discharge || MMR is given at 12-15 months and does not prevent RSV",
   "A dose of the adult RSV vaccine for the baby || The adult vaccine is for adults 75 and older, or 50-74 at risk"],
  "Infants entering their first RSV season can receive a long-acting monoclonal antibody such as nirsevimab or clesrovimab when the mother did not receive the RSV vaccine in pregnancy.")

q("iso", "The charge nurse is making assignments on a pediatric unit. Which pairings of illness and precaution are correct? " + SATA,
  ["*Measles - airborne",
   "*Rotavirus - contact",
   "Mononucleosis - droplet || Mono spreads through saliva and needs standard precautions",
   "*Influenza - droplet",
   "Chickenpox - standard only || Hospitalized varicella needs airborne plus contact precautions"],
  "Measles and chickenpox require airborne precautions (varicella also contact), influenza is droplet, rotavirus and RSV are contact, and mono is standard.")

q("iso", "A nurse is preparing to care for a 5-month-old admitted with RSV. Which personal protective plan is correct?",
  ["Negative-pressure room with an N95 respirator || Airborne precautions are for measles and chickenpox",
   "*Gown and gloves for contact precautions",
   "A mask within 3 feet for droplet precautions || Droplet precautions are used for influenza",
   "Standard precautions with no gown or gloves || RSV spreads on hands and surfaces and needs contact precautions"],
  "RSV and rotavirus use contact precautions because they spread on hands and surfaces.")
