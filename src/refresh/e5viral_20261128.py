T = "e5viral"; SET = "20261128"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("basics", "A daycare teacher asks the nurse how a toddler with no symptoms could have passed a virus to classmates. Which response is accurate?", [
  "'Viruses always cause severe symptoms in children.' || Viruses can cause no symptoms or severe illness",
  "*'A viral infection can cause no symptoms at all.'",
  "'Viruses spread only after a high fever starts.' || Viral infections may cause no symptoms at all",
  "'Viruses can live and multiply without host cells.' || Viruses need host cells to replicate"],
  "Viruses need host cells to replicate, contain RNA or DNA, and can cause anything from no symptoms to severe illness. Most antibiotics do not kill them.")

q("rota", "The parent of a 2-year-old with mild watery diarrhea and vomiting asks whether a stool test is needed to confirm rotavirus. Which response is accurate?", [
  "'A Monospot test is used to confirm rotavirus.' || A Monospot is used for mononucleosis",
  "'Every child needs a chest x-ray to confirm it.' || A chest x-ray does not diagnose rotavirus",
  "*'Most cases are diagnosed by symptoms; stool tests are for severe cases.'",
  "'A throat culture is the main test for rotavirus.' || A stool antigen EIA or PCR is used in severe cases"],
  "Most rotavirus cases are diagnosed clinically. In severe cases, a stool antigen EIA (enzyme immunoassay) or PCR (polymerase chain reaction) is used.")

q("rotacare", "The nurse is caring for four infants with rotavirus. Which infant needs the nurse's attention first?", [
  "A 10-month-old who cries with tears and is breastfeeding || Tears and continued feeding are reassuring",
  "A 7-month-old with three wet diapers since morning || Wet diapers suggest adequate output",
  "*A 5-month-old who is lethargic with a sunken fontanelle",
  "A 9-month-old who is fussy but has a moist mouth || A moist mouth is not a dehydration sign"],
  "Dehydration is the major danger with rotavirus, and recognizing and treating it is the priority. Signs include a sunken fontanelle, fewer wet diapers, no tears, lethargy, dry mouth, tachypnea and reduced urine.")

q("rotacare", "The mother of a 2-month-old asks the nurse how to protect her baby from rotavirus. Which statements by the nurse are accurate? " + SATA, [
  "*'The vaccine is given by mouth in a 2- or 3-dose series.'",
  "*'Wash your hands with soap and water after diaper changes.'",
  "*'Disinfect surfaces such as the changing table.'",
  "'The vaccine is one injection repeated every fall.' || The rotavirus vaccine is oral, in a 2- or 3-dose series",
  "'Alcohol gel alone is all the hand cleaning you need.' || Soap-and-water hand hygiene is taught"],
  "Rotavirus prevention includes the oral rotavirus vaccine in a 2- or 3-dose series, soap-and-water hand hygiene, surface disinfection, and standard and contact precautions.")

q("chicken", "A 7-year-old with chickenpox has some lesions still filled with fluid and others crusted. The parent asks if he can return to school tomorrow. Which response is best?", [
  "'Yes, since his fever has already gone away.' || Return depends on all lesions crusting, not the fever",
  "'Yes, as long as he wears a mask in class.' || He stays home until all lesions have crusted",
  "'Yes, once he has had a day of antibiotics.' || Chickenpox is viral; antibiotics do not decide return",
  "*'Not yet; he can go back when all lesions crust.'"],
  "A child with chickenpox returns to school when all lesions have crusted. Chickenpox spreads by air and by contact with lesions.")

q("chicken", "A 6-year-old hospitalized with chickenpox develops a new cough and increased work of breathing. The nurse recognizes this as a possible sign of which complication?", [
  "*Pneumonia",
  "Splenic rupture || Splenic rupture is a mono complication",
  "Postherpetic neuralgia || This is lasting nerve pain after shingles",
  "Kehr sign || Kehr sign is referred shoulder pain from splenic rupture"],
  "Complications of chickenpox include pneumonia, neurologic problems and fetal risks.")

q("shingles", "A 72-year-old has postherpetic neuralgia after a shingles outbreak. Which medications might the nurse expect for the pain? " + SATA, [
  "*Analgesics",
  "*Gabapentin",
  "*A tricyclic antidepressant",
  "Oseltamivir || Oseltamivir is an influenza antiviral",
  "Amoxicillin || Antibiotics do not treat nerve pain from shingles"],
  "Postherpetic neuralgia is nerve pain that continues after the rash heals, sometimes for months. Pain options include analgesics, gabapentin and TCAs (tricyclic antidepressants).")

q("shingles", "A 70-year-old with new shingles lesions on the forehead near the left eye asks why the clinic wants her seen by an eye specialist today. Which response by the nurse is best?", [
  "'The rash will spread to both sides of your face.' || Shingles is unilateral along a dermatome",
  "*'Shingles near the eye can threaten your sight.'",
  "'Eye lesions mean you now have chickenpox too.' || Shingles is reactivation, not a new chickenpox case",
  "'An eye exam tells us when the pain will stop.' || The urgency is the threat to sight"],
  "Ophthalmic shingles can threaten sight and needs an urgent ophthalmology referral.")

q("zostertx", "A 78-year-old is receiving IV acyclovir for shingles. Which results should the nurse monitor most closely during therapy?", [
  "Stool antigen results || Stool antigen testing is for rotavirus",
  "*Kidney function results",
  "Monospot test results || A Monospot is used for mononucleosis",
  "Rapid influenza results || A rapid flu test does not monitor acyclovir"],
  "With acyclovir, the nurse monitors kidney function, encourages hydration and teaches the client to finish the full course.")

q("vzvvax", "A healthy 45-year-old with no immune problems asks whether she should get the shingles vaccine now. Which response is accurate?", [
  "*'It's advised at 50, or from 19 if immune-weakened.'",
  "'Yes, every adult gets it yearly starting at 19.' || It is not annual; healthy adults start at 50",
  "'Only after you have had shingles two times.' || Prior shingles episodes are not the criterion",
  "'No; it's given only to infants with varicella.' || It is an adult vaccine"],
  "The shingles vaccine is recommended for adults 50 and older, or 19 and older with immunocompromise. It is not given annually.")

q("ebv", "A 16-year-old recovering from mononucleosis asks whether the virus will be completely gone once he feels better. Which response is accurate?", [
  "'Yes; it leaves the body once the fever ends.' || EBV stays latent for life",
  "'Yes, after a course of acyclovir clears it.' || Mono treatment is supportive",
  "*'No; Epstein-Barr virus stays latent for life.'",
  "'No; it returns each year as shingles.' || Shingles is VZV reactivation, not EBV"],
  "Mono (EBV, Epstein-Barr virus) spreads mainly through saliva, has a 4-6 week incubation and stays latent for life. It is common in adolescents and young adults.")

q("spleen", "A 19-year-old with mononucleosis is suddenly pale and dizzy with severe left upper quadrant pain, a rising heart rate and falling blood pressure. Which action by the nurse is best?", [
  "Encourage rest and reassess in 4 hours || These signs suggest an emergency",
  "Give a saltwater gargle for comfort || Gargles treat sore throat, not this emergency",
  "*Report the findings at once as possible splenic rupture",
  "Document the findings as expected mono fatigue || These are not expected mono findings"],
  "Sudden severe LUQ (left upper quadrant) pain with dizziness, tachycardia, pallor and hypotension suggests splenic rupture, an emergency. Referred left shoulder pain (Kehr sign) may also occur.")

q("spleen", "The nurse teaches a 16-year-old hockey player who has mononucleosis. Which statement by the client shows understanding?", [
  "'I can play again as soon as my fever goes away.' || Contact sports are avoided for 4-6 weeks",
  "*'I'll skip hockey for 4 to 6 weeks to protect my spleen.'",
  "'Only my liver could be hurt if I get checked hard.' || The enlarged spleen can rupture",
  "'Sharing my water bottle is fine with teammates.' || Avoid sharing drinks while symptomatic"],
  "Mono can enlarge the spleen, which can rupture, so contact sports are avoided for 4-6 weeks. The client also avoids sharing drinks and utensils while symptomatic, avoids alcohol, and rests and hydrates.")

q("flu", "A 10-year-old developed fever, chills and body aches this morning and is diagnosed with influenza. The parent asks how long he may spread it after symptoms begin. Which response is accurate?", [
  "'Only while he still has a fever.' || Spread is not limited to febrile periods",
  "*'For about 5 days after symptoms start.'",
  "'For about 2 weeks after the first symptom.' || Spread lasts about 5 days after onset",
  "'Only until his stools return to normal.' || Influenza is not spread through stool"],
  "A person with influenza can spread the virus about 24 hours before symptoms and for about 5 days after onset.")

q("flutx", "Four clients ask about oseltamivir for influenza. Which client is the best candidate based on the timing taught?", [
  "A healthy 28-year-old who has been sick for 2 weeks || It is ideally started within 24-48 hours",
  "*A 72-year-old with heart disease who became ill yesterday",
  "A 40-year-old who wants it in place of a flu shot || Oseltamivir is not a vaccine",
  "A 55-year-old who plans to wait for pneumonia first || It is not reserved for pneumonia"],
  "Oseltamivir should ideally be started within 24-48 hours of symptoms, especially for high-risk clients such as those with chronic heart disease. Common adverse effects are nausea and vomiting.")

q("flutx", "The nurse is caring for a 58-year-old admitted with influenza. Which finding should the nurse report first?", [
  "Muscle aches in both legs || Myalgia is an expected flu finding",
  "A headache rated 4 out of 10 || Headache is an expected flu finding",
  "*Labored breathing with low oxygenation",
  "Fatigue and weakness since yesterday || Fatigue is an expected flu finding"],
  "Priority influenza assessments are respiratory rate and work of breathing, oxygenation, lung sounds, temperature and I&O (intake and output). Pneumonia is a complication of influenza.")

q("measles", "An unvaccinated 5-year-old was exposed to measles 10 days ago and has no symptoms yet. The parent asks if the child is now safe. Which response by the nurse is accurate?", [
  "'Yes; symptoms always start within 1 to 3 days.' || That is rotavirus incubation",
  "'Yes; measles is spread only by direct touch.' || Measles is airborne",
  "*'Not yet; incubation is 7 to 14 days.'",
  "'Not yet; symptoms take 4 to 6 weeks.' || That is mononucleosis incubation"],
  "Measles incubation is 7-14 days, followed by a 3-5 day prodrome of high fever, cough, conjunctivitis and Koplik spots, then a maculopapular rash from the hairline down.")

q("measles", "A 4-year-old hospitalized with measles is tugging at his ear and is more irritable. The nurse recognizes this may be which complication?", [
  "Postherpetic neuralgia || This follows shingles",
  "Splenic rupture || This is a mono complication",
  "Reye syndrome || Reye syndrome is linked to aspirin use",
  "*Otitis media"],
  "Measles complications include otitis media, pneumonia, encephalitis and pregnancy complications. The nurse watches breathing, hydration and neurologic changes.")

q("measlescare", "A 3-year-old with measles has a cough and congestion. Which room setup best supports the child's breathing?", [
  "*A cool-mist humidifier and the head of the bed raised",
  "A warm, bright room with the child lying flat || Dim lights and an elevated head of bed are used",
  "Removing the humidifier and lowering the bed || A cool-mist humidifier and raised head are used",
  "Opening the blinds and keeping the bed flat || Dim lights help photophobia; elevate the head"],
  "Measles comfort care includes dimming lights for photophobia, a cool-mist humidifier, elevating the head of the bed, and fever management and hydration. Airborne precautions are used and public health is notified.")

q("rsv", "The nurse teaches the parent of a 3-month-old with RSV. Which statement by the parent needs correction?", [
  "'I'll call if the skin between her ribs pulls in.' || Correct: retractions need urgent care",
  "'I'll count her wet diapers each day.' || Correct: poor feeding can cause dehydration",
  "*'If she stops breathing briefly, I'll wait for it to happen again.'",
  "'I'll watch for her nostrils flaring when she breathes.' || Correct: nasal flaring is a distress sign"],
  "Priority signs of respiratory distress in infants with RSV (respiratory syncytial virus) are apnea, retractions, nasal flaring, tachypnea and wheezing. Poor feeding can cause dehydration, and parents are taught when to seek urgent care.")

q("rsv", "A 77-year-old with diabetes and severe obesity is diagnosed with RSV. Which problems should the nurse monitor for? " + SATA, [
  "*Pneumonia",
  "*Worsening of chronic disease",
  "Splenic rupture || Splenic rupture is a mono complication",
  "Postherpetic neuralgia || This follows shingles",
  "Koplik spots || Koplik spots are unique to measles"],
  "Adults at higher risk for severe RSV (respiratory syncytial virus) include older adults, those with COPD, CHF or asthma, diabetes or severe obesity, and immunocompromised clients. Severe RSV can cause pneumonia or exacerbations of chronic disease.")

q("rsvprev", "A healthy 60-year-old with no chronic illness asks whether he should get the adult RSV vaccine. Which response is accurate?", [
  "'Yes; every adult gets it each fall.' || It is one dose and not annual",
  "*'It's advised at 75, or 50 to 74 with increased risk.'",
  "'No; it is given only to infants at birth.' || Infants receive antibody or maternal protection",
  "'No; only pregnant people may receive it.' || There is also an adult RSV vaccine"],
  "The adult RSV (respiratory syncytial virus) vaccine is for adults 75 and older, or 50-74 with increased risk, as one dose that is not annual.")

q("iso", "The nurse is caring for a 7-year-old admitted with measles. Which action shows correct use of isolation precautions?", [
  "Wearing a surgical mask for droplet precautions || Measles requires airborne precautions",
  "Using gown and gloves only, door left open || Measles requires airborne precautions",
  "*Placing the child in a negative-pressure airborne room",
  "Using standard precautions with hand hygiene || Measles requires airborne precautions"],
  "Measles and chickenpox require airborne precautions; measles can stay in the air for up to 2 hours. Influenza is droplet, rotavirus and RSV are contact, and mononucleosis is standard.")

q("iso", "The nurse receives four new admissions on the pediatric unit. Which illness is paired with the correct precaution?", [
  "Rotavirus with droplet precautions || Rotavirus uses contact precautions",
  "Mononucleosis with contact precautions || Mono uses standard precautions",
  "Influenza with airborne precautions || Influenza uses droplet precautions",
  "*Chickenpox with airborne plus contact precautions"],
  "Hospitalized varicella needs airborne plus contact precautions. Influenza is droplet, rotavirus and RSV (respiratory syncytial virus) are contact, and mononucleosis, spread by saliva, is standard.")
