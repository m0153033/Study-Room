# Week 13.1 Viral Syndromes — lesson plan, lecture transcript (via notes), notes.
EXAM = "e5"
T = "e5viral"
CONCEPTS = {
 "basics":"Infection basics & pediatric risk",
 "rota":"Rotavirus: spread & findings",
 "rotacare":"Rotavirus: dehydration care & prevention",
 "chicken":"Chickenpox (varicella)",
 "shingles":"Shingles (herpes zoster)",
 "zostertx":"VZV treatment & nursing",
 "vzvvax":"Varicella & shingles vaccines",
 "ebv":"Mononucleosis (EBV)",
 "spleen":"Mono: splenic rupture & care",
 "flu":"Influenza: spread & findings",
 "flutx":"Influenza: oseltamivir, nursing & vaccine",
 "measles":"Measles (rubeola)",
 "measlescare":"Measles care & MMR",
 "rsv":"RSV in infants & adults",
 "rsvprev":"RSV prevention",
 "iso":"Isolation precautions",
}
HI = ["iso","rotacare","shingles","spleen","measles","rsv","flutx","chicken"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- basics ----------
q("basics","Which statements about viruses are correct? "+SATA,
 ["*They need host cells to replicate","*They contain RNA or DNA","*They can cause no symptoms or severe illness","They are killed by most antibiotics || Antibiotics don't treat viruses."],
 "Entry can occur through mucous membranes, broken skin or insect bites.")
q("basics","Why are children more vulnerable to viral infections? "+SATA,
 ["*Immature immune systems","*Close contact in school or daycare","*Inadequate handwashing","*Limited access to preventive care","Thicker skin || Not a reason."],
 "Related concepts: nutrition, immunity, tissue integrity, inflammation.")

# ---------- rotavirus ----------
q("rota","How is rotavirus spread?",
 ["*Fecal–oral route through hands, surfaces, food or water","Airborne droplets that hang in the air for 2 hours || That's measles.","Saliva from kissing || That's mono.","Mosquito bites || Not rotavirus."],
 "It's highly contagious and persists on surfaces; incubation is 1–3 days.")
q("rota","Which age group does rotavirus most commonly affect, compared with norovirus?",
 ["*Children under 5; norovirus affects all ages","Older adults only || Not the pattern.","Teens and young adults || That's mono.","All ages equally || That's norovirus."],
 "The professor contrasted rotavirus (young children) with norovirus (all ages).")
q("rota","Which findings are typical of rotavirus? "+SATA,
 ["*Severe watery diarrhea","*Vomiting","*Fever","*Abdominal pain","Koplik spots || Measles."],
 "The major danger is dehydration.")
q("rota","How is rotavirus diagnosed in severe cases?",
 ["*Stool antigen EIA or PCR","Monospot test || Mono.","Chest x-ray || Pneumonia.","Throat culture || Strep."],
 "Most cases are diagnosed clinically.")

# ---------- rotavirus care ----------
q("rotacare","Which findings in an infant with rotavirus suggest dehydration? "+SATA,
 ["*Sunken fontanelle","*Fewer wet diapers","*No tears when crying","*Lethargy and dry mouth","Bulging fontanelle || Not dehydration."],
 "Also tachypnea and reduced urine. Recognizing and treating dehydration is the priority.")
q("rotacare","What is the treatment for rotavirus?",
 ["*Oral rehydration, or IV fluids for severe dehydration; no specific antiviral","Oseltamivir || Influenza.","Acyclovir || VZV.","Antibiotics || It's a virus."],
 "Continue breastfeeding or formula and monitor stool frequency, intake and I&O.")
q("rotacare","Which precautions prevent rotavirus spread? "+SATA,
 ["*Soap-and-water hand hygiene","*Surface disinfection","*Standard and contact precautions","Airborne negative-pressure room || Not needed for rotavirus."],
 "The oral rotavirus vaccine (Rotarix or RotaTeq) is given in a 2- or 3-dose series.")
q("rotacare","A mother asks how her baby gets the rotavirus vaccine. Best response?",
 ["*'It's given by mouth in a 2- or 3-dose series.'","'It's a yearly shot.' || That's flu.","'It's given at age 4–6.' || Not the timing.","'There's no vaccine.' || There is one."],
 "Rotarix and RotaTeq are oral.")

# ---------- chickenpox ----------
q("chicken","What is the relationship between chickenpox and shingles?",
 ["*Chickenpox is the primary VZV infection; shingles is reactivation of the latent virus","They're caused by different viruses || Both are VZV.","Shingles comes first, then chickenpox || Reversed.","Chickenpox is bacterial || It's viral."],
 "VZV stays latent in the sensory dorsal root ganglia.")
q("chicken","Which findings fit chickenpox? "+SATA,
 ["*Fever and malaise","*Itchy vesicular rash","*Spread by air and contact with lesions","Unilateral stripe of painful vesicles || That's shingles."],
 "Complications include pneumonia, neurologic problems and fetal risks.")
q("chicken","A parent asks what to give a child with chickenpox for fever. Which should the nurse tell them to AVOID?",
 ["*Aspirin, because of Reye syndrome","Acetaminophen || Recommended.","Calamine lotion || Recommended for itch.","Cool baths || Recommended."],
 "Also trim nails and encourage rest.")
q("chicken","When can a child with chickenpox return to school?",
 ["*When all lesions have crusted","When the fever breaks || Lesions may still be contagious.","After 24 hours of antibiotics || Not bacterial.","As soon as the rash appears || Most contagious then."],
 "Acyclovir is mainly emphasized for severe or immunocompromised cases.")
q("chicken","A hospitalized child has chickenpox. Which precautions are needed?",
 ["*Airborne plus contact precautions, with immune staff caring for the child","Droplet only || Not enough.","Standard only || Not enough.","Contact only || Varicella is also airborne."],
 "The professor emphasized both airborne and contact.")

# ---------- shingles ----------
q("shingles","Which rash pattern is classic for shingles?",
 ["*A unilateral, painful stripe of vesicles along a dermatome","A head-to-toe rash starting at the hairline || Measles.","Itchy vesicles all over the body || Chickenpox.","A rash after taking amoxicillin || Mono."],
 "Burning, tingling or pain can come 1–5 days before the rash.")
q("shingles","A client with shingles has a rash on the forehead near the eye and blurred vision. What is the priority?",
 ["*Urgent ophthalmology referral","Apply calamine and reassess tomorrow || Delays sight-saving care.","Give gabapentin only || Doesn't address the eye.","Schedule the shingles vaccine || Not the priority."],
 "Ophthalmic shingles can threaten sight.")
q("shingles","What is postherpetic neuralgia?",
 ["*Nerve pain that continues after the rash heals, sometimes for months","A second rash on the other side || Not the definition.","Itching during the rash || Not the definition.","Eye involvement || That's ophthalmic shingles."],
 "Pain options: analgesics, gabapentin and TCAs.")
q("shingles","Which clients are at higher risk for shingles? "+SATA,
 ["*Older adults","*Clients with weakened immunity","A child who's never had chickenpox || Shingles is reactivation of prior VZV.","A healthy teen with no VZV history || No latent virus to reactivate."],
 "Assess pain, lesion distribution and neurologic symptoms.")

# ---------- treatment ----------
q("zostertx","When should antiviral therapy for shingles ideally begin?",
 ["*Within 24–72 hours of rash onset","After the rash crusts || Too late.","Only if pain lasts 3 months || Too late.","Before any symptoms || Not possible to time."],
 "Acyclovir can be oral, IV or topical.")
q("zostertx","Which nursing actions apply to a client on acyclovir? "+SATA,
 ["*Monitor kidney function","*Encourage hydration","*Teach to finish the full course","Restrict fluids || Fluids protect the kidneys."],
 "Hydration protects the kidneys during acyclovir therapy.")
q("zostertx","Which comfort and safety care fits shingles? "+SATA,
 ["*Nonadherent dressings","*Loose clothing","*Avoid exposing newborns, pregnant people and immunocompromised contacts until lesions crust","*Emotional support","Tight dressings to stop itching || Use loose, nonadherent coverings."],
 "Also rest and hydration.")

# ---------- vaccines ----------
q("vzvvax","When are the two childhood varicella vaccine doses given?",
 ["*12–15 months and 4–6 years","Birth and 2 months || Not the schedule.","Every year || Not annual.","At 11–12 years only || Not the schedule."],
 "Same timing as MMR.")
q("vzvvax","Who should receive the shingles vaccine?",
 ["*Adults 50 and older, or 19 and older with immunocompromise","All infants || That's varicella.","Everyone every year || It's not annual.","Only people who've had shingles twice || Not the indication."],
 "Shingles vaccination is not annual.")

# ---------- mono ----------
q("ebv","How is mononucleosis (EBV) mainly spread?",
 ["*Saliva: kissing and shared drinks or utensils","Fecal–oral || Rotavirus.","Airborne for 2 hours || Measles.","Mosquito bites || Not EBV."],
 "Incubation 4–6 weeks; latent for life; common in adolescents and young adults.")
q("ebv","Which findings are classic for mono? "+SATA,
 ["*Profound fatigue","*Sore throat and fever","*Posterior cervical lymphadenopathy","*Possible enlarged spleen and liver","Koplik spots || Measles."],
 "A rash after amoxicillin is a classic clue and isn't necessarily a true allergy.")
q("ebv","A teen with a sore throat develops a rash after starting amoxicillin. What does the nurse suspect?",
 ["*Mononucleosis; the rash is a classic EBV clue, not necessarily a true allergy","A true penicillin allergy for sure || Not necessarily.","Measles || Not the pattern.","Shingles || Not the pattern."],
 "A Monospot can be falsely negative; EBV serology confirms.")
q("ebv","Which is the treatment for mononucleosis?",
 ["*Supportive care: rest, hydration, acetaminophen or NSAIDs, saltwater gargles, soft foods","Acyclovir for all cases || Not the lecture treatment.","Oseltamivir || Influenza.","Antibiotics || It's viral."],
 "Avoid alcohol because the liver can be involved; fatigue may last weeks to months.")

# ---------- spleen ----------
q("spleen","A client with mono has sudden severe left upper quadrant pain radiating to the left shoulder, dizziness and tachycardia. What does the nurse suspect?",
 ["*Splenic rupture","Expected fatigue || This is an emergency.","Shingles || Not the pattern.","Influenza || Not the pattern."],
 "Referred left shoulder pain is Kehr sign; also pallor and hypotension.")
q("spleen","How long should a client with mono avoid contact sports?",
 ["*4–6 weeks","2 days || Too short.","1 year || Not the guideline.","There's no restriction || Splenic rupture risk."],
 "The enlarged spleen can rupture.")
q("spleen","Which teaching applies to mono? "+SATA,
 ["*Avoid sharing drinks and utensils while symptomatic","*Avoid alcohol","*Avoid contact sports","Return to football this week || Too soon."],
 "Rest and hydration.")

# ---------- flu ----------
q("flu","When can a person with influenza spread the virus?",
 ["*About 24 hours before symptoms and for about 5 days after onset","Only when febrile || Spread starts before symptoms.","Only 2 weeks after onset || Not the window.","Only through stool || It's respiratory."],
 "High-risk: older adults, pregnancy, immunocompromise, chronic heart or lung disease.")
q("flu","Which findings fit influenza? "+SATA,
 ["*Abrupt fever and chills","*Myalgia and headache","*Cough and sore throat","*Vomiting or diarrhea, especially in children","Slow onset over weeks || It's abrupt."],
 "Also fatigue, weakness and nasal symptoms.")
q("flu","A child's rapid flu test is negative but symptoms are classic. What should the nurse understand?",
 ["*Rapid tests have lower sensitivity, especially in children; a negative result doesn't always rule out flu","The child definitely doesn't have flu || Not reliable enough.","Rapid tests are more sensitive than PCR || PCR is more sensitive.","A chest x-ray diagnoses flu || It checks for pneumonia."],
 "Rapid tests return in 10–15 minutes.")
q("flu","Which are complications of influenza? "+SATA,
 ["*Pneumonia","*Dehydration","*Febrile seizures in children","*Worsening chronic illness","Splenic rupture || Mono."],
 "Rarely myocarditis, encephalitis, sepsis or Reye syndrome.")

# ---------- flu treatment ----------
q("flutx","When should oseltamivir (Tamiflu) ideally be started?",
 ["*Within 24–48 hours of symptoms, especially for high-risk clients","After 2 weeks || Too late.","Only after pneumonia develops || Too late.","Before the flu season, as a vaccine || It's an antiviral, not a vaccine."],
 "Common adverse effects: nausea and vomiting.")
q("flutx","Which nursing assessments are priorities for a client with influenza? "+SATA,
 ["*Respiratory rate and work of breathing","*Oxygenation","*Lung sounds","*Temperature and I&O","Amsler grid || Eyes."],
 "Teach cough etiquette, masking, hand hygiene and cleaning surfaces.")
q("flutx","When can people start getting the annual flu vaccine?",
 ["*From 6 months of age, usually offered beginning September/October","Only after age 65 || From 6 months.","At birth || Not until 6 months.","Once in a lifetime || It's annual."],
 "Older adults may get high-dose or adjuvanted vaccine; it reduces severe illness and hospitalization.")

# ---------- measles ----------
q("measles","Which finding is unique to measles?",
 ["*Koplik spots in the mouth","Posterior cervical lymph nodes || Mono.","Unilateral dermatomal rash || Shingles.","Watery diarrhea || Rotavirus."],
 "The prodrome is high fever, cough, conjunctivitis and Koplik spots for 3–5 days.")
q("measles","How does the measles rash spread?",
 ["*Starts at the hairline/face and spreads downward","Starts on the feet and moves up || Reversed.","Stays on one side of the body || Shingles.","Only on the hands and feet || Not measles."],
 "It's a maculopapular rash.")
q("measles","Why is measles so contagious?",
 ["*It's airborne and can stay in the air for up to 2 hours","It spreads only by touch || It's airborne.","It's spread only in food || Not measles.","It's only contagious after the rash fades || 4 days before to 4 days after rash."],
 "Incubation is 7–14 days.")
q("measles","Which are complications of measles? "+SATA,
 ["*Otitis media","*Pneumonia","*Encephalitis","*Pregnancy complications","Hemorrhagic cystitis || Not related."],
 "Watch breathing, hydration and neurologic changes.")

# ---------- measles care ----------
q("measlescare","Which comfort measures help a child with measles? "+SATA,
 ["*Dim the lights for photophobia","*Cool-mist humidifier","*Elevate the head of the bed","*Fever management and hydration","Bright lights to keep the child alert || Photophobia."],
 "Airborne precautions; notify public health.")
q("measlescare","Which supplement may be ordered for measles, and what is the caution?",
 ["*Vitamin A as a short course; excessive doses can be toxic","Vitamin K; bleeding || Not for measles.","Iron; constipation || Not for measles.","Vitamin C; kidney stones || Not the lecture point."],
 "The professor discussed its role and the risk with excessive dosing.")
q("measlescare","When are the two MMR doses given?",
 ["*12–15 months and 4–6 years","At birth and 6 months || Not the schedule.","Every year || Not annual.","Only for adults || Children get it."],
 "Nonimmune adults may need 1–2 doses; verify immunity.")

# ---------- RSV ----------
q("rsv","Which findings in an infant with RSV are PRIORITY signs of respiratory distress? "+SATA,
 ["*Apnea","*Retractions","*Nasal flaring","*Tachypnea and wheezing","Mild runny nose alone || Common but not distress."],
 "RSV can cause bronchiolitis or pneumonia; poor feeding can cause dehydration.")
q("rsv","When is RSV most common?",
 ["*Fall to early spring","Midsummer only || Not the season.","Year-round equally || Seasonal.","Only in winter in adults || Not the pattern."],
 "Symptoms appear 2–8 days after exposure; contagious about 3–8 days.")
q("rsv","Which adults are at higher risk for severe RSV? "+SATA,
 ["*Older adults","*Clients with COPD, CHF or asthma","*Clients with diabetes or severe obesity","*Immunocompromised clients","Healthy 25-year-old athletes || Low risk."],
 "Severe RSV can cause pneumonia or exacerbations of chronic disease.")
q("rsv","Which nursing care fits an infant with RSV? "+SATA,
 ["*Monitor oxygenation and respiratory effort","*Monitor hydration and feeding","*Collaborate with respiratory therapy","*Teach parents when to seek urgent care","Give oseltamivir || That's influenza."],
 "Supportive respiratory care.")

# ---------- RSV prevention ----------
q("rsvprev","When is the maternal RSV vaccine (Abrysvo) given to protect the newborn?",
 ["*32–36 weeks of pregnancy","First trimester || Not the timing.","At delivery || Not the timing.","After birth to the infant || The infant gets an antibody instead."],
 "Most infants need either maternal vaccine protection OR infant antibody, not both.")
q("rsvprev","What can infants entering their first RSV season receive?",
 ["*A long-acting monoclonal antibody such as nirsevimab or clesrovimab when indicated","Oseltamivir || Flu.","The MMR vaccine || Not for RSV.","Acyclovir || VZV."],
 "Given when the mother didn't receive the RSV vaccine in pregnancy, as indicated.")
q("rsvprev","Who should get the adult RSV vaccine?",
 ["*Adults 75 and older, or 50–74 with increased risk; one dose, not annual","Everyone every year || Not annual.","Only children || Adults.","Only pregnant people in the first trimester || Not the timing."],
 "Per the PowerPoint.")

# ---------- isolation ----------
q("iso","Which viral illnesses require AIRBORNE precautions? "+SATA,
 ["*Measles","*Chickenpox (varicella)","Influenza || Droplet.","Rotavirus || Contact.","Mononucleosis || Standard."],
 "Hospitalized varicella also needs contact precautions.")
q("iso","Which precautions are used for influenza?",
 ["*Droplet","Airborne || Measles and varicella.","Contact || Rotavirus and RSV.","Standard only || Mono."],
 "Teach masking and cough etiquette.")
q("iso","Which precautions are used for rotavirus and RSV?",
 ["*Contact","Airborne || Measles and varicella.","Droplet || Influenza.","None || Precautions are needed."],
 "Both spread on hands and surfaces.")
q("iso","Which precautions are used for mononucleosis?",
 ["*Standard","Airborne || Not for mono.","Droplet || Influenza.","Contact || Rotavirus and RSV."],
 "Mono spreads mainly through saliva.")
q("iso","Match each illness to its precaution. "+SATA,
 ["*Measles — airborne","*Influenza — droplet","*Rotavirus — contact","*Mono — standard","RSV — airborne || RSV = contact."],
 "Know this comparison for Exam 5.")
