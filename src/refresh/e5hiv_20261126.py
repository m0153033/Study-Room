T = "e5hiv"; SET = "20261126"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# what
q("what", "During a clinic intake, which client history does the nurse identify as an HIV risk factor?",
  ["A 60-year-old who shares eating utensils with family || Saliva and routine contact don't spread HIV",
   "*A 34-year-old with multiple sexual partners and inconsistent condom use",
   "A 22-year-old who hugs a roommate with HIV || Routine contact doesn't spread HIV",
   "A 45-year-old who shares a bathroom at work || Urine and feces don't spread HIV"],
  "HIV risk: sharing injection equipment, condomless sex, multiple sexual partners and perinatal exposure.")

# trans
q("trans", "A 19-year-old pregnant client with HIV asks how the virus could pass to her baby. Which routes are possible? " + SATA,
  ["*During pregnancy",
   "*During delivery",
   "Cuddling the baby || Routine contact doesn't spread HIV",
   "*Breastfeeding",
   "Kissing the baby's cheek || Saliva doesn't spread HIV"],
  "HIV spreads through sex, blood exposure, and pregnancy, delivery or breastfeeding. It isn't spread by routine contact, saliva or sweat.")

# vl (HI)
q("vl", "The nurse reviews CD4 counts for four clients with HIV. Which client has the MOST immune compromise?",
  ["Client with a CD4 of 1,400 cells/mm³ || Within the normal range",
   "Client with a CD4 of 900 cells/mm³ || Within the normal range",
   "Client with a CD4 of 520 cells/mm³ || Within the normal range",
   "*Client with a CD4 of 120 cells/mm³"],
  "Normal CD4 is about 500–1,600 cells/mm³. A low or falling CD4 means more immune compromise.")
q("vl", "A 39-year-old electrician with HIV asks what the difference is between his viral load and his CD4 count. Which explanation is accurate?",
  ["*Viral load shows how much the virus is replicating; CD4 shows how strong the immune system is",
   "Viral load counts immune cells; CD4 counts virus copies || The two are reversed",
   "Both tests measure HIV antibodies || Neither is an antibody test",
   "A high viral load means the immune system is strong || High viral load = more replication"],
  "Viral load measures HIV RNA copies per mL of blood (replication and treatment response). Low CD4 = more immune compromise.")

# stages (HI)
q("stages", "Which features describe stage 1 (acute) HIV? " + SATA,
  ["*Flu-like symptoms after a recent exposure",
   "*A very high viral load",
   "A CD4 count below 200 cells/mm³ || That defines stage 3 (AIDS)",
   "*The highest risk of transmission",
   "Lasting about 10–15 years without treatment || That describes stage 2"],
  "Acute HIV: recent exposure plus flu-like symptoms, very high viral load and the highest transmission risk.")
q("stages", "A 50-year-old client with HIV has a CD4 count of 260 cells/mm³ and has unintentionally lost more than 10% of body weight. Which stage is this?",
  ["Stage 1, because symptoms are present || Stage 1 follows a recent exposure",
   "Stage 2, because the CD4 is above 200 || An AIDS-defining condition also counts",
   "*Stage 3 (AIDS), because wasting is AIDS-defining",
   "No stage applies, since the CD4 is above 200 || AIDS can be defined by a condition"],
  "AIDS = CD4 below 200 OR an AIDS-defining condition, such as Kaposi sarcoma, lymphoma or wasting (unintentional weight loss over 10%).")

# cancer
q("cancer", "A client with AIDS develops new confusion, and imaging shows a brain tumor. Which AIDS-defining cancer is most likely?",
  ["Kaposi sarcoma of the skin || That causes red-purple skin and mouth lesions",
   "Invasive cervical cancer || That is found with Pap/HPV testing",
   "*Primary CNS lymphoma",
   "Basal cell carcinoma || Not an AIDS-defining cancer"],
  "AIDS-defining cancers: Kaposi sarcoma, non-Hodgkin lymphoma, primary CNS lymphoma and invasive cervical cancer.")

# oi (HI)
q("oi", "A 42-year-old client's CD4 count has dropped to 170 cells/mm³. Which preventive action does the nurse anticipate?",
  ["Stopping ART until the CD4 recovers || ART continues for life",
   "*Starting PJP prophylaxis",
   "Airborne isolation in a private room || HIV needs only standard precautions",
   "Checking the CD4 count daily || CD4 is checked every 3–6 months"],
  "PJP prophylaxis starts when the CD4 count is below 200.")
q("oi", "A client with advanced HIV has CMV infection. Which problems can CMV cause? " + SATA,
  ["*Retinitis",
   "Red-purple skin lesions || That is Kaposi sarcoma",
   "*Colitis",
   "White mouth plaques || That is candidiasis",
   "*Esophagitis"],
  "CMV retinitis causes blurred vision, floaters and vision loss; CMV can also cause colitis or esophagitis.")

# test
q("test", "A 27-year-old client had a high-risk exposure 5 days ago and now has a fever. The provider suspects very early infection. Which test does the nurse expect?",
  ["An antibody-only home test || It can miss early infection",
   "A CD4 count to confirm HIV || CD4 measures immune status",
   "*An HIV nucleic acid test",
   "A Western blot || Not part of the sequence taught"],
  "NAT finds viral genetic material before antibodies form, so it's used when early infection is suspected.")

# monitor
q("monitor", "A 45-year-old client with HIV comes in for a routine monitoring visit. Which lab does the nurse expect to be part of ongoing monitoring?",
  ["Anti-dsDNA || Not part of HIV monitoring",
   "A daily CD4 count || CD4 is checked every 3–6 months",
   "*Glucose and lipid levels",
   "A Western blot || Not part of HIV monitoring"],
  "HIV monitoring includes CBC, kidney and liver function, glucose and lipids, and hepatitis, TB and STI screening, with Pap/HPV as indicated.")

# art (HI)
q("art", "A client on ART asks, 'Is it OK to drink grapefruit juice every morning?' What is the best response?",
  ["Yes; juice has no effect on any ART || Grapefruit interacts with some regimens",
   "*Let's check with your provider; grapefruit interacts with some regimens",
   "Stop your ART on days you drink it || Don't stop ART without guidance",
   "Only drink it at night instead || Timing doesn't remove the interaction"],
  "ART interactions: St. John's wort, grapefruit with some regimens, and OTC medicines and supplements.")
q("art", "Which statements about ART are accurate? " + SATA,
  ["*It is taken for life",
   "It is started only when CD4 drops below 200 || Start as soon as possible, even with a preserved CD4",
   "*It continues even after the viral load is undetectable",
   "It can be stopped for mild nausea || Mild effects may be manageable; don't stop ART",
   "*Jaundice or dark urine should be reported right away"],
  "ART starts as soon as possible and continues for life; undetectable doesn't mean cured. Report jaundice, dark urine, severe rash or new depression immediately.")

# adhere (HI)
q("adhere", "A night-shift security guard says, 'I sleep at odd hours and forget my ART.' Which intervention fits this barrier best?",
  ["Refer to social work for copay help || That fits a cost barrier",
   "Refer to mental health services || That fits hopelessness or isolation",
   "*Link the dose to a daily habit and set a phone alarm",
   "Skip doses on work nights || Missed doses lead to resistance"],
  "For forgotten doses: phone alarm or pillbox and linking doses to a daily habit. Missed doses let HIV replicate and become resistant.")
q("adhere", "A client has been missing ART doses. Which nurse statements are open-ended and nonjudgmental? " + SATA,
  ["*What makes it hard to take your medicine some days?",
   "Why can't you just remember your pills? || 'Why' questions sound judgmental",
   "*Walk me through a typical morning for you.",
   "You're being noncompliant with treatment. || Labeling adds stigma",
   "*How have the pills been making you feel?"],
  "Open-ended, nonjudgmental questions find barriers to adherence; avoid stigma.")

# prep (HI)
q("prep", "A 31-year-old HIV-negative client shared injection equipment 12 hours ago. Which option should the nurse explain?",
  ["PrEP, because it is started after an exposure || PrEP is taken before possible exposure",
   "Lifelong ART right away || ART is treatment for people with HIV",
   "*PEP as soon as possible, continued for 28 days",
   "Wait and test in a few months || PEP is time-sensitive"],
  "PEP: after exposure, as soon as possible (ideally within 24 hours, no later than 72), for 28 days, with follow-up HIV testing.")
q("prep", "A nursing student explains HIV prevention to a peer. Which statements need correction? " + SATA,
  ["ART is ongoing, lifelong treatment for people with HIV || This is correct",
   "*PrEP is started after an exposure has happened",
   "PrEP is for people who are HIV-negative || This is correct",
   "*PEP only needs to be taken for 3 days",
   "U = U requires a sustained undetectable viral load on ART || This is correct"],
  "PrEP is for HIV-negative people before possible exposure. PEP starts within 72 hours after exposure and lasts 28 days.")

# preg (HI)
q("preg", "A 26-year-old pregnant client with HIV says, 'I want to stop my ART until the baby is born so the medicine won't hurt it.' What is the best response?",
  ["Stopping ART during pregnancy is the safest choice || ART continues through pregnancy",
   "*ART should continue through pregnancy, delivery and after birth",
   "You can stop until delivery, then restart || ART isn't paused",
   "Only take ART during labor || ART continues throughout"],
  "Continue ART through pregnancy, delivery and postpartum.")
q("preg", "A mother with HIV who has had a sustained undetectable viral load asks about feeding her newborn. Which statements by the nurse are accurate? " + SATA,
  ["*Formula or donor milk removes the risk of transmission through feeding",
   "Breastfeeding has zero risk because you're undetectable || The risk is less than 1%, not zero",
   "*With sustained undetectable levels, breastfeeding risk is less than 1%",
   "HIV is never found in breast milk || Breast milk can transmit HIV",
   "*We can talk through the options together and decide what fits you"],
  "Formula or donor milk removes the risk; breastfeeding risk with sustained undetectable is less than 1%, not zero. Provide nonjudgmental, shared counseling.")

# needle (HI)
q("needle", "A nurse was stuck by a used needle 3 hours ago. The charge nurse says, 'Finish your shift first; it can wait.' What should the nurse do?",
  ["Finish the shift, then report || PEP is time-sensitive",
   "Wait 72 hours to see if symptoms appear || Symptoms don't guide PEP",
   "*Report it now and get urgent PEP evaluation",
   "Only document it in an incident report || Evaluation is needed now"],
  "Report promptly and seek urgent exposure evaluation; PEP ideally starts within 24 hours and no later than 72.")
q("needle", "A nurse is about to irrigate a wound on a client with HIV, and splashing is possible. Which precautions should the nurse use?",
  ["Gloves alone are enough || Splashes need eye protection too",
   "*Gloves and eye protection",
   "Airborne isolation with an N95 || HIV isn't airborne",
   "No protection is needed with HIV || Standard precautions always apply"],
  "Prevent occupational exposure with gloves, eye protection when splashes are possible and sharps safety; standard precautions apply to every patient.")

# nursing
q("nursing", "A client with HIV keeps a pet bird. Which teaching is appropriate?",
  ["Clean the bird cage yourself with bare hands || Increases infection risk",
   "Pets carry no infection risk || Cleaning cages is an infection risk",
   "You must give the bird away || Not required",
   "*Ask someone else to clean the bird's cage"],
  "Infection prevention: ask someone else to clean litter boxes and cages, avoid undercooked food, practice hand hygiene and avoid sick contacts.")
