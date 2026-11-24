T = "e5viral"; SET = "20261124"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("basics", "A nursing student is reviewing viral infections before clinical. Which statement by the student needs correction?", [
  "'Viruses can enter through mucous membranes or broken skin.' || This is accurate; insect bites are another entry route",
  "'A virus has to use host cells to replicate.' || This is accurate; viruses need host cells",
  "*'Most viruses are killed by a course of antibiotics.'",
  "'Some viral infections cause no symptoms at all.' || This is accurate; illness ranges from none to severe"],
  "Viruses need host cells to replicate, contain RNA or DNA, can cause no symptoms or severe illness, and are not killed by most antibiotics. Entry can occur through mucous membranes, broken skin or insect bites.")

q("rota", "A 3-year-old is admitted with severe watery diarrhea, vomiting and fever, and rotavirus is suspected. Which test should the nurse anticipate to confirm it?", [
  "EBV (Epstein-Barr virus) serology || This confirms mononucleosis",
  "A rapid influenza test || This tests for influenza",
  "*A stool antigen EIA (enzyme immunoassay) or PCR (polymerase chain reaction)",
  "An Amsler grid assessment || This is not a test for rotavirus"],
  "Most rotavirus cases are diagnosed clinically; in severe cases, a stool antigen EIA or PCR is used. Rotavirus mostly affects children under 5 and causes severe watery diarrhea, vomiting, fever and abdominal pain.")

q("rotacare", "A 7-month-old with rotavirus is lethargic, has a dry mouth and has had only one wet diaper today. Which intervention is the priority?", [
  "Start an antiviral that treats rotavirus || There is no specific antiviral for rotavirus",
  "Hold formula until the diarrhea stops || Formula or breastfeeding should continue",
  "Move the infant to an airborne isolation room || Rotavirus uses contact, not airborne, precautions",
  "*Rehydrate orally, or with IV (intravenous) fluids if severe"],
  "Dehydration is the major danger with rotavirus, and recognizing and treating it is the priority. Treatment is oral rehydration, or IV fluids for severe dehydration; there is no specific antiviral.")

q("rotacare", "The nurse is caring for a hospitalized 11-month-old with rotavirus. Which actions are appropriate? " + SATA, [
  "*Use standard and contact precautions",
  "Place the infant in a negative-pressure room || Rotavirus does not require airborne precautions",
  "*Monitor stool frequency, intake and I&O (intake and output)",
  "Clean hands with alcohol gel only || Soap-and-water hand hygiene is taught for rotavirus",
  "*Continue the infant's usual formula feedings"],
  "Prevent rotavirus spread with soap-and-water hand hygiene, surface disinfection, and standard and contact precautions. Continue breastfeeding or formula and monitor stool frequency, intake and I&O.")

q("chicken", "A 5-year-old with varicella is admitted to the pediatric unit. Which staffing and precaution plan is correct?", [
  "Droplet precautions; any nurse may be assigned || Varicella needs airborne plus contact precautions",
  "*Airborne plus contact precautions with a varicella-immune nurse",
  "Contact precautions only, with gloves for lesion care || Airborne precautions are also needed",
  "Standard precautions; avoid assigning a pregnant nurse || Standard alone is not enough for varicella"],
  "A hospitalized child with chickenpox needs both airborne and contact precautions, with immune staff caring for the child.")

q("chicken", "The nurse reviews possible complications of chickenpox with a pregnant mother of a child who has the illness. Which complications should be included? " + SATA, [
  "*Pneumonia",
  "Splenic rupture || This is a complication of mononucleosis",
  "*Neurologic problems",
  "*Risks to a fetus",
  "Postherpetic neuralgia || This follows shingles, not chickenpox"],
  "Complications of chickenpox include pneumonia, neurologic problems and fetal risks. Acyclovir is mainly emphasized for severe or immunocompromised cases.")

q("shingles", "The nurse at a community clinic is screening clients for shingles risk. Which client is at greatest risk?", [
  "A 4-year-old who has never had chickenpox || Shingles is reactivation of latent VZV, which this child does not carry",
  "*An 81-year-old with weakened immunity who had chickenpox as a child",
  "A healthy 16-year-old with no VZV (varicella-zoster virus) history || There is no latent virus to reactivate",
  "A healthy 30-year-old who just finished a flu shot || Neither age nor immunity puts this client at risk"],
  "Shingles is reactivation of latent VZV from a past chickenpox infection. Older adults and clients with weakened immunity are at higher risk.")

q("shingles", "A 66-year-old calls the clinic reporting burning and tingling along the left side of the waist for 2 days, with no rash yet. Which response by the nurse is accurate?", [
  "'Shingles pain only begins after the blisters crust over.' || Pain can begin before the rash appears",
  "'That pain means you already have postherpetic neuralgia.' || That is pain persisting after the rash heals",
  "*'Shingles pain can start 1 to 5 days before the rash appears.'",
  "'A rash starting at your hairline will likely follow.' || That pattern describes measles"],
  "Burning, tingling or pain can come 1-5 days before the shingles rash, which is a unilateral, painful stripe of vesicles along a dermatome. The nurse assesses pain, lesion distribution and neurologic symptoms.")

q("zostertx", "A 63-year-old noticed a painful band of shingles vesicles 2 days ago and asks whether it is too late for medicine. Which response is best?", [
  "'It's too late; antivirals only work before any symptoms.' || Antivirals are started after rash onset",
  "'We'll wait until the rash crusts, then start treatment.' || Waiting delays the ideal window",
  "'Medicine is given only if the pain lasts 3 months.' || Antivirals ideally begin within 24-72 hours",
  "*'Antivirals work best started within 24-72 hours of the rash.'"],
  "Antiviral therapy for shingles should ideally begin within 24-72 hours of rash onset. Acyclovir can be given oral, IV or topical; monitor kidney function and encourage hydration.")

q("vzvvax", "A 35-year-old who is immunocompromised after a transplant asks whether she is too young for the shingles vaccine. Which response is accurate?", [
  "'Yes; it's only for adults 50 and older.' || Adults 19 and older with immunocompromise are included",
  "*'It's advised from age 19 for those with immunocompromise.'",
  "'You'll need it only after a second shingles episode.' || Prior shingles is not the criterion",
  "'It's a yearly shot, so start this fall.' || Shingles vaccination is not annual"],
  "The shingles vaccine is recommended for adults 50 and older, or 19 and older with immunocompromise. It is not given annually.")

q("ebv", "A 15-year-old has profound fatigue, fever, sore throat and posterior cervical lymphadenopathy, but the Monospot test is negative. What should the nurse anticipate?", [
  "Ruling out mono and starting antibiotics || A Monospot can be falsely negative",
  "*EBV (Epstein-Barr virus) serology to confirm the diagnosis",
  "A stool antigen test to check for rotavirus || These findings do not suggest rotavirus",
  "A rapid flu test to rule out influenza first || Serology, not a flu test, confirms EBV"],
  "Classic mono findings include profound fatigue, sore throat, fever and posterior cervical lymphadenopathy. A Monospot can be falsely negative; EBV serology confirms.")

q("spleen", "A 20-year-old with mononucleosis has sudden severe left upper quadrant pain that also hurts in the left shoulder. The nurse recognizes the shoulder pain as which finding?", [
  "Postherpetic neuralgia from nerve damage || That is pain after a shingles rash heals",
  "Expected muscle aches from viral fatigue || Sudden severe pain is not an expected mono finding",
  "*Kehr sign, referred pain from splenic rupture",
  "Posterior cervical lymph nodes pressing on nerves || Lymphadenopathy does not cause this pain"],
  "Splenic rupture causes sudden severe LUQ pain radiating to the left shoulder (Kehr sign), with dizziness, tachycardia, pallor and hypotension.")

q("spleen", "The nurse is caring for four adolescents with mononucleosis. Which client should the nurse assess first?", [
  "A 14-year-old with profound fatigue on day 5 || Profound fatigue is an expected mono finding",
  "A 16-year-old with sore throat and fever || These are expected mono findings",
  "A 17-year-old with swollen posterior neck nodes || Posterior cervical lymphadenopathy is expected",
  "*An 18-year-old with sudden LUQ (left upper quadrant) pain and dizziness"],
  "Sudden severe LUQ pain with dizziness suggests splenic rupture, an emergency. The enlarged spleen in mono can rupture, causing pain radiating to the left shoulder, tachycardia, pallor and hypotension.")

q("flu", "The nurse at a family clinic is identifying clients at high risk for influenza complications this season. Which clients are high risk? " + SATA, [
  "*A 26-year-old who is 28 weeks pregnant",
  "A healthy 32-year-old office worker || No high-risk condition is present",
  "*An 84-year-old living in assisted living",
  "*A 55-year-old with chronic heart disease",
  "A healthy 24-year-old graduate student || No high-risk condition is present"],
  "Clients at high risk for influenza include older adults, pregnancy, immunocompromise, and chronic heart or lung disease.")

q("flutx", "The nurse teaches a 45-year-old with influenza how to prevent spreading it to family at home. Which instructions are appropriate? " + SATA, [
  "*Cover coughs and wear a mask around others",
  "*Perform frequent hand hygiene",
  "You can't spread it once your fever is gone || Flu spreads for about 5 days after onset",
  "*Clean commonly touched surfaces",
  "Only your stool carries the virus || Influenza is not spread only through stool"],
  "Teach cough etiquette, masking, hand hygiene and cleaning surfaces. Influenza can spread about 24 hours before symptoms and for about 5 days after onset.")

q("flutx", "A 71-year-old asks the nurse whether there is a flu vaccine option meant for older adults. Which response is accurate?", [
  "'Older adults don't need it once they've had one dose.' || The flu vaccine is annual",
  "'The flu vaccine is only approved for children.' || It is given from 6 months of age onward",
  "*'A high-dose or adjuvanted shot may be used for older adults.'",
  "'You'll need oseltamivir instead of a vaccine.' || Oseltamivir is a treatment, not a vaccine"],
  "Older adults may get a high-dose or adjuvanted flu vaccine. The annual vaccine can be given from 6 months of age and reduces severe illness and hospitalization.")

q("measles", "An unvaccinated 2-year-old sat in a clinic waiting room 1 hour after a child with measles left. The parent asks if her child could have been exposed. Which response is accurate?", [
  "'No; measles spreads only by direct touch.' || Measles is airborne",
  "'No; measles is contagious only after the rash fades.' || This is not how measles spreads",
  "'Only if your child shared food with that child.' || Measles is not spread only in food",
  "*'Yes; measles can stay in the air for up to 2 hours.'"],
  "Measles is very contagious because it is airborne and can stay in the air for up to 2 hours. Incubation is 7-14 days.")

q("measles", "A 4-year-old has had high fever, cough and conjunctivitis for 3 days. Which finding would most help the nurse distinguish measles from other viral illnesses?", [
  "A painful vesicle stripe on one side || This is shingles",
  "*Koplik spots seen inside the mouth",
  "Posterior cervical lymphadenopathy || This is a classic mono finding",
  "Severe watery diarrhea and vomiting || These are classic rotavirus findings"],
  "Koplik spots are unique to measles. The 3-5 day prodrome is high fever, cough, conjunctivitis and Koplik spots, followed by a maculopapular rash from the hairline down.")

q("measlescare", "The parent of a 3-year-old with measles asks whether to give extra vitamin A at home to speed recovery. Which response is best?", [
  "'Give as much as you like; it's a natural vitamin.' || Excessive doses can be toxic",
  "'Vitamin A causes bleeding, so avoid it.' || Bleeding is not the caution for vitamin A",
  "*'Only the short course ordered; too much can be toxic.'",
  "'Vitamin A replaces the need for the MMR vaccine.' || It does not replace MMR (measles, mumps, rubella) vaccination"],
  "Vitamin A may be ordered as a short course for measles; excessive doses can be toxic. MMR is given at 12-15 months and 4-6 years.")

q("rsv", "A parent asks when RSV (respiratory syncytial virus) is most common and how soon symptoms appear after exposure. Which response is accurate?", [
  "'Midsummer; symptoms appear the same day.' || RSV peaks fall to early spring",
  "*'Fall to early spring; symptoms appear 2-8 days later.'",
  "'Year-round equally; symptoms take 2 weeks.' || RSV is seasonal, fall to early spring",
  "'Only in winter; symptoms take a month.' || Symptoms appear 2-8 days after exposure"],
  "RSV is most common from fall to early spring. Symptoms appear 2-8 days after exposure, and a person is contagious about 3-8 days.")

q("rsv", "The nurse receives report on four infants with RSV (respiratory syncytial virus). Which infant should the nurse see first?", [
  "A 6-month-old with a clear runny nose and no distress || A mild runny nose alone is not a priority sign",
  "A 5-month-old feeding well with a mild cough || Good feeding and mild cough are not priority signs",
  "*A 2-month-old who had an episode of apnea",
  "A 7-month-old who is fussy but has wet diapers || Wet diapers suggest adequate hydration"],
  "Priority signs of respiratory distress in infants with RSV are apnea, retractions, nasal flaring, tachypnea and wheezing. RSV can cause bronchiolitis or pneumonia.")

q("rsvprev", "A healthy 78-year-old received the adult RSV (respiratory syncytial virus) vaccine last fall and asks if he needs another dose this year. Which response is accurate?", [
  "*'It's one dose for adults 75 and older, not yearly.'",
  "'Yes, it's given every year like the flu shot.' || The adult RSV vaccine is not annual",
  "'It's only for children, so you shouldn't have had it.' || Adults 75 and older are included",
  "'It's only for pregnant people in the first trimester.' || Adults 75 and older are included"],
  "The adult RSV vaccine is given to adults 75 and older, or 50-74 with increased risk, as one dose that is not annual.")

q("iso", "The nurse is setting up a pediatric unit. Which clients require contact precautions? " + SATA, [
  "*A 9-month-old with rotavirus",
  "A 16-year-old with mononucleosis || Mono requires standard precautions",
  "*A 3-month-old with RSV (respiratory syncytial virus)",
  "*A 6-year-old hospitalized with chickenpox",
  "A 10-year-old with influenza || Influenza requires droplet precautions"],
  "Rotavirus and RSV need contact precautions because they spread on hands and surfaces. Hospitalized varicella needs airborne plus contact precautions. Influenza is droplet and mononucleosis is standard.")

q("iso", "Which client with a viral illness needs only standard precautions?", [
  "A 2-year-old with measles || Measles requires airborne precautions",
  "A 40-year-old with influenza || Influenza requires droplet precautions",
  "*A 19-year-old with mononucleosis",
  "A 1-year-old with rotavirus || Rotavirus requires contact precautions"],
  "Mononucleosis spreads mainly through saliva and uses standard precautions. Measles and chickenpox are airborne, influenza is droplet, and rotavirus and RSV are contact.")
