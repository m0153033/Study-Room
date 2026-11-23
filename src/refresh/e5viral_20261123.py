T = "e5viral"; SET = "20261123"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("basics", "The parent of a 3-year-old with a viral illness asks the clinic nurse why antibiotics weren't prescribed. Which statement about viruses is accurate?", [
  "Viruses are always severe, so antibiotics wouldn't be strong enough || Viruses can cause anything from no symptoms to severe illness",
  "*Viruses replicate inside host cells and aren't killed by most antibiotics",
  "Viruses contain neither RNA nor DNA, so drugs can't reach them || Viruses contain RNA or DNA",
  "Viruses enter the body only through insect bites || Entry can also occur through mucous membranes and broken skin"],
  "Viruses need host cells to replicate, contain RNA or DNA, and are not killed by most antibiotics. They enter through mucous membranes, broken skin or insect bites and can cause no symptoms or severe illness.")

q("rota", "A daycare director calls because several toddlers have severe watery diarrhea and vomiting from rotavirus. She asks how it spreads between children. Which response is best?", [
  "'It travels in the air and can linger in a room for 2 hours.' || That describes measles, which is airborne",
  "'It's passed mainly through saliva, like sharing cups and utensils.' || Saliva is the main route for mononucleosis",
  "*'It spreads fecal-oral, through hands, surfaces, food or water.'",
  "'It's carried by mosquitoes that bite children on the playground.' || Rotavirus is not spread by mosquito bites"],
  "Rotavirus spreads by the fecal-oral route through hands, surfaces, food or water. It is highly contagious, persists on surfaces, and mostly affects children under 5.")

q("rotacare", "A 9-month-old is admitted with rotavirus after 2 days of diarrhea. Which finding should the nurse report as a sign of dehydration?", [
  "A bulging anterior fontanelle when crying || A bulging fontanelle is not a dehydration sign; a sunken one is",
  "Moist mouth and frequent wet diapers all day || These suggest adequate hydration",
  "Continues to breastfeed every 3 hours || Continued breastfeeding is encouraged and is not a sign of dehydration",
  "*Sunken fontanelle; no tears when crying"],
  "Dehydration is the major danger with rotavirus. Signs in an infant include a sunken fontanelle, fewer wet diapers, no tears, lethargy, dry mouth, tachypnea and reduced urine. Recognizing and treating dehydration is the priority.")

q("rotacare", "The nurse teaches the parents of a 14-month-old with rotavirus. Which statement by a parent needs more teaching?", [
  "'I'll wash my hands with soap and water after every diaper change.' || Correct; soap-and-water hand hygiene prevents spread",
  "*'I'll stop her formula until the diarrhea is gone.'",
  "'I'll tell the nurse if she has fewer wet diapers.' || Correct; fewer wet diapers suggests dehydration",
  "'I'll disinfect the changing table after each use.' || Correct; surface disinfection prevents spread"],
  "Treatment is oral rehydration (IV fluids if severe) with no specific antiviral. Breastfeeding or formula should continue while stool frequency, intake and I&O are monitored.")

q("chicken", "A parent of a 6-year-old with chickenpox asks how to care for him at home. Which instructions should the nurse give? " + SATA, [
  "*Give acetaminophen for fever",
  "*Trim his nails",
  "*Keep him home until all lesions have crusted",
  "Give aspirin for fever || Aspirin is avoided because of Reye syndrome",
  "Send him back to school once the fever breaks || He returns only when all lesions have crusted"],
  "For chickenpox, avoid aspirin because of Reye syndrome; acetaminophen can be used for fever. Trim nails and encourage rest. The child returns to school when all lesions have crusted.")

q("chicken", "A grandmother with a history of shingles asks whether her grandson's chickenpox is related to her illness. Which response is accurate?", [
  "'They're caused by two different viruses that look alike.' || Both are caused by VZV (varicella-zoster virus)",
  "'Shingles always comes first, then chickenpox follows it.' || Chickenpox is the primary infection; shingles comes later",
  "*'Shingles is the same chickenpox virus reactivating later.'",
  "'Chickenpox is bacterial, but shingles is caused by a virus.' || Chickenpox is a viral (VZV) infection"],
  "Chickenpox is the primary VZV infection. The virus stays latent in the sensory dorsal root ganglia, and shingles is reactivation of that latent virus.")

q("shingles", "A 72-year-old reports 3 days of burning and tingling on the right side of the chest. Today a painful band of vesicles appears in the same area on that side only. The nurse recognizes this as:", [
  "*Herpes zoster, a painful vesicular rash along one dermatome",
  "Chickenpox, an itchy vesicular rash all over the body || Chickenpox is generalized, not a one-sided stripe",
  "Measles, a rash that starts at the hairline and spreads down || Measles is a downward-spreading maculopapular rash",
  "A drug rash from amoxicillin seen with mononucleosis || This rash is not linked to amoxicillin"],
  "Shingles classically causes a unilateral, painful stripe of vesicles along a dermatome. Burning, tingling or pain can come 1-5 days before the rash.")

q("shingles", "A 70-year-old's shingles rash healed 2 months ago, but she still has burning pain in the same area. What should the nurse explain?", [
  "'This is a second shingles rash starting on the other side.' || A second rash is not what postherpetic neuralgia means",
  "'Pain after the rash heals means you have chickenpox.' || This is not a new chickenpox infection",
  "'This pain means the virus has spread to your eye.' || Eye involvement is a separate complication",
  "*'This is postherpetic neuralgia, nerve pain after the rash.'"],
  "Postherpetic neuralgia is nerve pain that continues after the rash heals, sometimes for months. Pain options include analgesics, gabapentin and TCAs (tricyclic antidepressants).")

q("zostertx", "A 74-year-old with shingles is started on acyclovir. Which nursing actions are appropriate? " + SATA, [
  "*Monitor kidney function",
  "Restrict fluids to protect the skin lesions || Hydration is encouraged to protect the kidneys",
  "*Teach the client to finish the full course",
  "*Use nonadherent dressings and loose clothing",
  "*Keep the client away from newborns until lesions crust"],
  "With acyclovir, monitor kidney function, encourage hydration and teach to finish the course. Comfort care includes nonadherent dressings and loose clothing; avoid exposing newborns, pregnant people and immunocompromised contacts until lesions crust.")

q("vzvvax", "A healthy 52-year-old who has never had shingles asks whether she should get the shingles vaccine. Which response is accurate?", [
  "'Only if you've already had shingles twice.' || Prior shingles is not the criterion",
  "*'Yes; it's advised for adults 50 and older.'",
  "'Yes, and you'll need a new dose every year.' || Shingles vaccination is not annual",
  "'No, it's only given to infants.' || It is an adult vaccine"],
  "The shingles vaccine is recommended for adults 50 and older, or 19 and older with immunocompromise. It is not given annually.")

q("ebv", "A 17-year-old has profound fatigue, sore throat, fever and posterior cervical lymphadenopathy, and EBV serology is positive. Which treatment plan should the nurse expect?", [
  "A full 10-day course of acyclovir || Acyclovir is not the treatment for mononucleosis",
  "Oseltamivir started within 48 hours || Oseltamivir treats influenza",
  "*Rest, fluids and saltwater gargles",
  "A course of antibiotics for the throat || Antibiotics don't treat this viral illness"],
  "Mono treatment is supportive: rest, hydration, acetaminophen or NSAIDs, saltwater gargles and soft foods. Avoid alcohol because the liver can be involved.")

q("spleen", "A 19-year-old college student diagnosed with mononucleosis last week asks to return to rugby practice next week. Which response is best?", [
  "'You can play once your sore throat and fever are gone.' || Sore-throat relief doesn't remove the spleen risk",
  "'There's no activity restriction with mono, so go ahead.' || Contact sports are restricted",
  "'You'll need to avoid all sports for a full year after this.' || The restriction is 4-6 weeks",
  "*'No contact sports for 4-6 weeks; the spleen can rupture.'"],
  "Clients with mono should avoid contact sports for 4-6 weeks because the enlarged spleen can rupture.")

q("spleen", "A 16-year-old with mononucleosis suddenly reports severe left upper quadrant pain. Which additional findings suggest splenic rupture? " + SATA, [
  "*Pain radiating to the left shoulder",
  "*Tachycardia and hypotension",
  "*Dizziness and pallor",
  "Posterior cervical lymphadenopathy || This is an expected finding of mono, not rupture",
  "Koplik spots in the mouth || Koplik spots are unique to measles"],
  "Splenic rupture causes sudden severe LUQ pain radiating to the left shoulder (Kehr sign), dizziness, tachycardia, pallor and hypotension.")

q("flu", "A nurse woke up with fever, chills and body aches and was diagnosed with influenza. She says, 'At least I couldn't have spread it at work yesterday.' Which response is accurate?", [
  "'Right; flu spreads only while you have a fever.' || It can spread before symptoms start",
  "*'Flu can spread about 24 hours before symptoms begin.'",
  "'Flu is spread only through stool.' || Influenza is not spread only through stool",
  "'You're contagious only 2 weeks after onset.' || Spread lasts about 5 days after onset"],
  "A person with influenza can spread the virus about 24 hours before symptoms and for about 5 days after onset.")

q("flutx", "A 67-year-old with COPD developed flu symptoms 20 hours ago and is prescribed oseltamivir. Which statement by the nurse is accurate?", [
  "'It's an antibiotic that kills the bacteria causing the flu.' || Influenza is a virus; oseltamivir is an antiviral",
  "'We'll start it only if pneumonia develops in the next week.' || It should be started early, not after complications",
  "*'Start it within 24-48 hours; nausea and vomiting are common.'",
  "'It should be started after 2 weeks if you're still sick.' || It should start within 24-48 hours"],
  "Oseltamivir should ideally be started within 24-48 hours of symptoms, especially for high-risk clients such as those with chronic lung disease. Common adverse effects are nausea and vomiting.")

q("flutx", "The parent of a 4-month-old asks when the baby can receive the flu vaccine. Which response is accurate?", [
  "'Right away; it's given at birth before you go home.' || It is not given at birth",
  "'Once, and then she's protected against flu for life.' || The flu vaccine is annual",
  "'Not until she's 65, when older adults get the high-dose shot.' || It's available from 6 months of age",
  "*'At 6 months, then yearly, usually from September or October.'"],
  "The annual flu vaccine can be given from 6 months of age and is usually offered beginning September/October. It reduces severe illness and hospitalization.")

q("measles", "An unvaccinated 3-year-old is being assessed for possible measles. Which findings would the nurse expect? " + SATA, [
  "*High fever, cough and conjunctivitis",
  "*Koplik spots in the mouth",
  "*A maculopapular rash that begins at the hairline and spreads downward",
  "A rash that starts on the feet and moves up || The measles rash starts at the face/hairline and spreads down",
  "A painful stripe of vesicles on one side || That is shingles"],
  "The measles prodrome is high fever, cough, conjunctivitis and Koplik spots for 3-5 days, followed by a maculopapular rash starting at the hairline/face and spreading downward.")

q("measles", "A 5-year-old is hospitalized with measles. Which change should the nurse report as a possible complication?", [
  "*New neurologic changes (possible encephalitis)",
  "The rash spreading from the face down to the trunk || Downward spread is the expected pattern",
  "Fever and cough during the first few days || These are expected prodrome findings",
  "Red, irritated eyes during the prodrome || Conjunctivitis is part of the expected prodrome"],
  "Measles complications include otitis media, pneumonia, encephalitis and pregnancy complications. The nurse watches breathing, hydration and neurologic changes.")

q("measlescare", "A 4-year-old with measles squints and cries when the room lights are on. Which action is best?", [
  "Open the blinds to brighten the room || Brightness worsens photophobia",
  "*Dim the lights in the room",
  "Lay the child flat to rest || The head of the bed should be elevated",
  "Remove the cool-mist humidifier || A cool-mist humidifier is a comfort measure"],
  "Comfort care for measles includes dimming the lights for photophobia, a cool-mist humidifier, elevating the head of the bed, and fever management and hydration.")

q("rsv", "During RSV season, which client should the nurse identify as at highest risk for severe RSV?", [
  "A healthy 25-year-old marathon runner || Healthy young adults are not a high-risk group",
  "A healthy 30-year-old teacher || No listed risk factors",
  "*A 79-year-old with COPD and heart failure",
  "A healthy 22-year-old college athlete || No listed risk factors"],
  "Adults at higher risk for severe RSV include older adults, those with COPD, CHF or asthma, diabetes or severe obesity, and immunocompromised clients. Severe RSV can cause pneumonia or worsen chronic disease.")

q("rsv", "The nurse teaches the parent of a 4-month-old with RSV which signs need urgent care. Which signs should be included? " + SATA, [
  "*Pauses in breathing",
  "*Skin pulling in between the ribs",
  "*Flaring of the nostrils",
  "*Poor feeding with fewer wet diapers",
  "A mild runny nose alone || A mild runny nose alone is not a priority sign"],
  "Priority signs of respiratory distress in infants with RSV are apnea, retractions, nasal flaring, tachypnea and wheezing. Poor feeding can cause dehydration. Teaching parents when to seek urgent care is part of nursing care.")

q("rsvprev", "A client at 34 weeks of pregnancy received the maternal RSV vaccine today. She asks if her newborn will also need nirsevimab. Which response is best?", [
  "'Yes; every baby needs both the vaccine and the antibody.' || Most infants need one or the other, not both",
  "*'Most babies need your vaccine or the antibody, not both.'",
  "'The vaccine only works if given in the first trimester.' || It is given at 32-36 weeks",
  "'Your baby will need oseltamivir instead after birth.' || Oseltamivir is an influenza drug"],
  "The maternal RSV vaccine is given at 32-36 weeks of pregnancy. Most infants need either maternal vaccine protection or infant antibody (such as nirsevimab), not both.")

q("iso", "The charge nurse has one negative-pressure airborne room available. Which client should be placed in it?", [
  "A 2-year-old with influenza || Influenza requires droplet precautions",
  "A 6-month-old with RSV || RSV requires contact precautions",
  "A 17-year-old with mononucleosis || Mono requires standard precautions",
  "*A 4-year-old with measles"],
  "Measles and chickenpox require airborne precautions. Influenza is droplet, RSV and rotavirus are contact, and mononucleosis is standard.")

q("iso", "Which illness-precaution pairings are correct? " + SATA, [
  "*Chickenpox - airborne plus contact",
  "*RSV - contact",
  "*Influenza - droplet",
  "Measles - droplet || measles requires airborne precautions",
  "Rotavirus - airborne || Rotavirus uses contact precautions"],
  "Hospitalized varicella needs airborne plus contact precautions. RSV and rotavirus spread on hands and surfaces (contact). Influenza is droplet. Mono, spread by saliva, is standard.")
