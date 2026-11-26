T = "e5viral"; SET = "20261126"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("basics", "A community health nurse teaches a group of new parents about how viruses get into the body. Which entry routes should the nurse include? " + SATA,
  ["*Mucous membranes",
   "*Broken skin",
   "*Insect bites",
   "Only through swallowed antibiotics || viruses are not spread by antibiotics",
   "Only through intact, healthy skin || entry occurs through broken skin"],
  "Viruses can enter through mucous membranes, broken skin or insect bites; they need host cells to replicate and are not killed by most antibiotics.")

q("rota", "A 20-month-old in a daycare program is brought to the clinic with severe watery diarrhea, vomiting, fever and abdominal pain. Which statement by the nurse comparing causes is accurate?",
  ["'Rotavirus affects mostly older adults, unlike norovirus.' || rotavirus mostly affects children under 5",
   "'Both viruses spread only through mosquito bites.' || rotavirus spreads fecal-oral",
   "*'Rotavirus mostly affects children under 5; norovirus affects all ages.'",
   "'Rotavirus is diagnosed only with a Monospot test.' || severe cases use a stool antigen EIA or PCR"],
  "Rotavirus most commonly affects children under 5, while norovirus affects all ages; it causes severe watery diarrhea, vomiting, fever and abdominal pain.")

q("rotacare", "A 10-month-old with rotavirus has a dry mouth, no tears and a sunken fontanelle. What should the nurse identify as the major danger?",
  ["*Dehydration",
   "Splenic rupture || this is a mono complication",
   "Postherpetic neuralgia || this follows shingles",
   "Encephalitis from measles || this is a measles complication"],
  "Dehydration is the major danger with rotavirus, and recognizing and treating it is the priority.")

q("rotacare", "A parent of an 8-month-old with rotavirus asks what the nurse will be doing during the hospital stay. Which response is accurate?",
  ["'We'll give an antiviral that cures rotavirus.' || there is no specific antiviral",
   "'We'll keep her in an airborne negative-pressure room.' || rotavirus uses standard and contact precautions",
   "'We'll hold her breast milk until the diarrhea stops.' || breastfeeding should continue",
   "*'We'll track her stools, intake and output closely.'"],
  "Rotavirus care is oral rehydration (IV fluids if severe), continuing breastfeeding or formula, and monitoring stool frequency, intake and I&O; there is no specific antiviral.")

q("chicken", "An 8-year-old is diagnosed with chickenpox. Which statement by the parent indicates understanding of home care?",
  ["'I'll give him aspirin to bring the fever down.' || aspirin is avoided because of Reye syndrome",
   "*'He stays home until every lesion has crusted over.'",
   "'He can go back to school once his fever breaks.' || return is when all lesions have crusted",
   "'I'll let his nails grow so he scratches less.' || nails should be trimmed"],
  "With chickenpox, the child returns to school when all lesions have crusted; trim nails, encourage rest, and avoid aspirin because of Reye syndrome.")

q("chicken", "The nurse is teaching a parent about chickenpox in a 4-year-old. Which statements are accurate? " + SATA,
  ["*'It spreads by air and by contact with the lesions.'",
   "*'The virus stays latent in the nerves and can return as shingles.'",
   "'It is a bacterial infection treated with antibiotics.' || chickenpox is the primary VZV infection",
   "*'Acyclovir is mainly for severe or immunocompromised cases.'",
   "'The rash is a painful stripe on one side of the body.' || that describes shingles"],
  "Chickenpox is the primary VZV infection, spread by air and contact with lesions; VZV stays latent in the sensory dorsal root ganglia and reactivates as shingles; acyclovir is mainly for severe or immunocompromised cases.")

q("shingles", "A 75-year-old with a shingles rash is being assessed in the clinic. Which nursing assessments are priorities? " + SATA,
  ["*Pain level",
   "*Distribution of the lesions",
   "*Neurologic symptoms",
   "Koplik spots inside the cheek || this is a measles finding",
   "Stool frequency and output || this is a rotavirus focus"],
  "For shingles, the nurse assesses pain, lesion distribution and neurologic symptoms.")

q("shingles", "Four clients with shingles call the clinic. Which client needs the most urgent follow-up?",
  ["A 69-year-old with vesicles on the right flank || this is the classic pattern",
   "*A 77-year-old with forehead lesions and blurred vision",
   "A 60-year-old with itching as lesions crust || this is not sight-threatening",
   "A 72-year-old with mild burning before the rash || prodromal pain is expected"],
  "Ophthalmic shingles can threaten sight and needs an urgent ophthalmology referral.")

q("zostertx", "A 76-year-old with shingles lives with a daughter who is pregnant and a newborn grandson. Which instruction is most important?",
  ["'Wrap the rash in tight dressings to stop itching.' || nonadherent dressings and loose clothing are used",
   "'Limit your fluids while on acyclovir.' || hydration protects the kidneys",
   "*'Avoid close contact with them until the lesions crust.'",
   "'Stop acyclovir once the pain improves.' || the full course should be finished"],
  "Avoid exposing newborns, pregnant people and immunocompromised contacts until lesions crust; use nonadherent dressings and loose clothing, encourage hydration and finish the acyclovir course.")

q("vzvvax", "A 58-year-old with no immune problems got the shingles vaccine series last year and asks whether she needs it again this fall. Which response is accurate?",
  ["'Yes; it's a yearly shot like the flu vaccine.' || shingles vaccination is not annual",
   "'Only if you've had shingles twice already.' || this is not the criterion",
   "*'No; the shingles vaccine is not given every year.'",
   "'It's only for infants, so you didn't need it.' || it's for adults 50 and older"],
  "The shingles vaccine is for adults 50 and older, or 19 and older with immunocompromise, and it is not annual.")

q("ebv", "A 21-year-old college student with mononucleosis asks how long the illness lasts and how she caught it. Which statement by the nurse is accurate?",
  ["'It spreads fecal-oral and goes away in 3 days.' || mono spreads by saliva and fatigue can last weeks",
   "'It's airborne and the virus leaves your body completely.' || EBV spreads by saliva and stays latent for life",
   "'It came from a mosquito bite about 2 days ago.' || incubation is 4-6 weeks",
   "*'It spreads through saliva, and fatigue may last weeks to months.'"],
  "Mono spreads mainly through saliva, has a 4-6 week incubation, stays latent for life, and its fatigue may last weeks to months.")

q("spleen", "An 18-year-old with mononucleosis is a high school wrestler. Which instruction is the priority?",
  ["*'No contact sports for 4-6 weeks; your spleen could rupture.'",
   "'Return to practice once your sore throat is gone.' || the spleen can still rupture",
   "'Take antibiotics so you can compete sooner.' || mono is viral and treated supportively",
   "'There is no activity restriction with mono.' || contact sports are avoided for 4-6 weeks"],
  "The enlarged spleen in mono can rupture, so contact sports are avoided for 4-6 weeks.")

q("spleen", "A 17-year-old with mononucleosis calls the nurse line. Which reported symptoms require emergency evaluation? " + SATA,
  ["*Sudden severe pain in the left upper abdomen",
   "*Pain spreading to the left shoulder",
   "*Feeling dizzy with a racing heart",
   "Ongoing tiredness for 2 weeks || fatigue is an expected mono finding",
   "A sore throat that improves with gargles || this is expected and improving"],
  "Splenic rupture causes sudden severe LUQ pain radiating to the left shoulder (Kehr sign), dizziness, tachycardia, pallor and hypotension.")

q("flu", "A 79-year-old in a long-term care facility develops influenza. Which complications should the nurse monitor for? " + SATA,
  ["*Pneumonia",
   "*Dehydration",
   "*Worsening of chronic illness",
   "Splenic rupture || this is a mono complication",
   "Postherpetic neuralgia || this follows shingles"],
  "Influenza complications include pneumonia, dehydration, febrile seizures in children and worsening chronic illness; rarely myocarditis, encephalitis, sepsis or Reye syndrome.")

q("flutx", "A 39-year-old who is 30 weeks pregnant has had flu symptoms for 18 hours. Which action by the nurse is best?",
  ["Tell her to wait 2 weeks to see if it resolves || oseltamivir works best early",
   "*Expect oseltamivir to be started now, as she is high risk",
   "Explain that oseltamivir is used only after pneumonia || it is started within 24-48 hours",
   "Delay treatment until after she delivers || early treatment is advised for high-risk clients"],
  "Oseltamivir should ideally be started within 24-48 hours of symptoms, especially for high-risk clients such as pregnant clients.")

q("flutx", "A home health nurse visits a 54-year-old recovering from influenza. Which statement by the client needs correction?",
  ["'I'm wearing a mask when my wife is near me.' || masking is correct teaching",
   "'I clean the doorknobs and remote each day.' || cleaning surfaces is correct",
   "'I cover my coughs around the kids.' || cough etiquette is correct",
   "*'My fever is gone, so I can't spread flu now.'"],
  "Influenza can spread about 24 hours before symptoms and for about 5 days after onset; teach cough etiquette, masking, hand hygiene and cleaning surfaces.")

q("measles", "The nurse reviews the timeline of measles with the parent of an unvaccinated 6-year-old. Which statement is accurate?",
  ["*'Incubation is 7-14 days, then 3-5 days of fever and cough.'",
   "'Incubation is 1-3 days, then watery diarrhea.' || this describes rotavirus",
   "'Symptoms start 4-6 weeks later with fatigue.' || this describes mono",
   "'The rash appears first, before any fever.' || the prodrome comes before the rash"],
  "Measles incubation is 7-14 days, followed by a 3-5 day prodrome of high fever, cough, conjunctivitis and Koplik spots, then the rash.")

q("measles", "A 3-year-old with measles is admitted to the pediatric unit. Which assessments should the nurse prioritize to watch for complications? " + SATA,
  ["*Breathing and lung status",
   "*Hydration status",
   "*Neurologic changes",
   "Lesions along one dermatome || this is a shingles pattern",
   "Left upper quadrant tenderness || this is a mono concern"],
  "Measles complications include otitis media, pneumonia, encephalitis and pregnancy complications, so the nurse watches breathing, hydration and neurologic changes.")

q("measlescare", "A nonimmune 30-year-old daycare worker asks about MMR (measles, mumps, rubella) vaccination. Which response is accurate?",
  ["'Adults never need MMR after childhood.' || nonimmune adults may need 1-2 doses",
   "*'You may need 1-2 doses; your immunity should be verified.'",
   "'You'll need a dose every year like the flu shot.' || MMR is not annual",
   "'Vitamin A can replace the vaccine for adults.' || vitamin A is a short course for measles"],
  "MMR is given at 12-15 months and 4-6 years; nonimmune adults may need 1-2 doses, and immunity should be verified.")

q("rsv", "A 3-month-old with RSV (respiratory syncytial virus) is drinking only half of usual feedings. Why is this finding important?",
  ["*Poor feeding can lead to dehydration",
   "It means the infant has splenic rupture || this is a mono complication",
   "It shows the infection is resolving || poor feeding is a concern",
   "It means oseltamivir is needed || oseltamivir treats influenza"],
  "In infants with RSV, poor feeding can cause dehydration, so nursing care includes monitoring hydration and feeding.")

q("rsv", "The nurse is caring for a 5-month-old with RSV (respiratory syncytial virus) bronchiolitis. Which actions are appropriate? " + SATA,
  ["*Watch for retractions and nasal flaring",
   "*Work with respiratory therapy",
   "Start oseltamivir as the RSV treatment || this treats influenza",
   "*Teach the parents when to seek urgent care",
   "Place the infant in airborne isolation || RSV uses contact precautions"],
  "Nursing care for RSV is supportive: monitor oxygenation, respiratory effort, hydration and feeding, collaborate with respiratory therapy and teach parents when to seek urgent care.")

q("rsvprev", "A 64-year-old with heart failure asks whether he should get the adult RSV (respiratory syncytial virus) vaccine. Which response is accurate?",
  ["'No; it's only for adults 75 and older.' || adults 50-74 with increased risk also qualify",
   "*'Yes; adults 50-74 with increased risk get one dose.'",
   "'Yes, and you'll repeat it every fall.' || it is one dose, not annual",
   "'No; it's only given to pregnant people.' || adults at risk receive it"],
  "The adult RSV vaccine is for adults 75 and older, or 50-74 with increased risk, as one dose that is not annual.")

q("iso", "The nurse is admitting a 10-year-old with influenza. Which precaution should be used?",
  ["Airborne in a negative-pressure room || this is for measles and chickenpox",
   "Contact with gown and gloves only || this is for rotavirus and RSV",
   "*Droplet precautions",
   "Standard precautions only || this is for mononucleosis"],
  "Influenza uses droplet precautions; measles and chickenpox are airborne, rotavirus and RSV are contact, and mono is standard.")

q("iso", "A nurse assigned to a 17-year-old with mononucleosis asks whether a gown, N95 respirator or mask is needed. Which response by the charge nurse is accurate?",
  ["'Use an N95 in a negative-pressure room.' || airborne is for measles and chickenpox",
   "*'Standard precautions; mono spreads mainly by saliva.'",
   "'Wear a mask for droplet precautions.' || droplet is for influenza",
   "'Wear a gown and gloves for contact precautions.' || contact is for rotavirus and RSV"],
  "Mononucleosis spreads mainly through saliva and uses standard precautions; measles and chickenpox are airborne, influenza is droplet, and rotavirus and RSV are contact.")
