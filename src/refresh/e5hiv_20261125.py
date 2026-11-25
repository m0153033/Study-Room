T = "e5hiv"; SET = "20261125"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("what", "A 33-year-old client with HIV asks why HIV makes it easier to get other infections. Which explanation by the nurse is accurate?",
 ["'HIV lowers your platelets, so infections spread.' || HIV targets CD4 T cells, not platelets.",
  "'HIV damages your liver, which fights infection.' || CD4 T lymphocytes are the target.",
  "'HIV only causes infections until it clears.' || HIV persists for life.",
  "*'HIV destroys CD4 T cells, weakening cell-mediated immunity.'"],
 "HIV is a retrovirus that attacks CD4 T lymphocytes, weakening cell-mediated immunity, and persists for life.")

q("trans", "A daughter caring for her father with HIV at home asks which task carries a risk of HIV transmission. Which task does the nurse identify?",
 ["Washing his sweaty clothes || Sweat doesn't transmit HIV.",
  "*Cleaning up blood from a cut",
  "Emptying his urinal || Urine doesn't transmit HIV.",
  "Sharing meals at the table || Saliva and routine contact don't transmit HIV."],
 "Blood, semen, vaginal/rectal secretions and breast milk transmit HIV; sweat, saliva, urine, feces and routine contact do not.")

q("vl", "A client on ART has a viral load of 30 copies/mL, with a lab threshold of 40, and a CD4 count of 720 cells/mm³. How does the nurse interpret these results?",
 ["Suppressed but still detectable || Below the lab threshold is undetectable.",
  "Viral load shows treatment failure || A low viral load means ART is working.",
  "*Undetectable, with a CD4 count in the normal range",
  "CD4 count is in the AIDS range || Normal is about 500–1,600."],
 "Undetectable means below the lab's threshold (often 40–75 copies/mL); a normal CD4 is about 500–1,600 cells/mm³.")

q("vl", "A client with HIV asks what U = U means for their relationship. Which statements are accurate? " + SATA,
 ["*It requires taking ART consistently",
  "It means HIV has been cured || HIV stays in the body for life.",
  "*It requires a sustained undetectable viral load",
  "It also prevents other STIs || Condoms still prevent other STIs.",
  "*It means effectively no sexual transmission of HIV"],
 "U = U: sustained undetectable on ART means effectively no sexual transmission; condoms still prevent other STIs.")

q("stages", "Which client with HIV is in stage 2 (chronic) HIV?",
 ["Client with a CD4 count of 160 cells/mm³ || Under 200 is AIDS (stage 3).",
  "Client with flu-like illness 3 weeks after exposure || That is acute (stage 1).",
  "*Client with a CD4 of 480, no symptoms and a detectable viral load",
  "Client with over 10% unintentional weight loss || Wasting is AIDS-defining."],
 "Chronic HIV is often asymptomatic but still transmissible if the viral load is detectable; untreated it lasts about 10–15 years.")

q("stages", "A client recently diagnosed with acute HIV asks why the nurse stresses being very careful about transmission right now. Best response?",
 ["'Your CD4 count is the highest it will ever be.' || CD4 level doesn't explain contagiousness.",
  "'You already meet the criteria for AIDS.' || AIDS is stage 3.",
  "'Your antibody levels are at their peak.' || Antibody-only tests may still be negative early.",
  "*'Your viral load is very high in this early stage.'"],
 "In acute HIV (stage 1) the viral load is very high, so transmission risk is highest.")

q("cancer", "The nurse is planning routine assessments for a client with AIDS. Which assessment helps detect Kaposi sarcoma?",
 ["*Inspect the skin and mouth for red-purple lesions",
  "Obtain a Pap and HPV test || Screens for cervical cancer.",
  "Check the viral load monthly || Measures viral replication.",
  "Auscultate the lungs for crackles || Not how Kaposi sarcoma is found."],
 "Kaposi sarcoma causes red-purple lesions on the skin and in the mouth; screen skin and mouth.")

q("oi", "A client with a CD4 count of 40 cells/mm³ reports 3 weeks of fever, night sweats and diarrhea with weight loss. Which infection does the nurse suspect?",
 ["CMV retinitis || Causes blurred vision and floaters.",
  "Oral candidiasis || Causes white mouth plaques.",
  "*Mycobacterium avium complex",
  "Kaposi sarcoma || Causes red-purple lesions."],
 "MAC with very low CD4 causes fever, night sweats, diarrhea and weight loss.")

q("oi", "A client with AIDS who was alert yesterday now has a new headache and is confused. What is the nurse's best action?",
 ["Give an analgesic and recheck in the morning || Neurologic changes need prompt reporting.",
  "*Report the change promptly; consider toxoplasmosis or CNS lymphoma",
  "Inspect the mouth for white plaques || Candidiasis doesn't cause confusion.",
  "Document it as expected fatigue || New confusion is a red flag."],
 "Headache, confusion or seizure suggest toxoplasmosis or primary CNS lymphoma; report neurologic changes promptly.")

q("test", "A client's 4th-generation antigen/antibody test is reactive, and the HIV-1/2 differentiation assay result is unclear. Which test does the nurse expect next?",
 ["A CD4 count to confirm the diagnosis || CD4 doesn't diagnose HIV.",
  "A repeat home self-test || Home tests can miss early infection.",
  "A Western blot || Not part of the sequence taught.",
  "*An HIV nucleic acid test"],
 "Sequence: 4th-generation antigen/antibody test, then HIV-1/2 differentiation assay if reactive, then NAT if unclear.")

q("monitor", "A client who has been undetectable on ART for a year asks how often labs will be drawn. Which statement is accurate?",
 ["'Viral load weekly and CD4 daily.' || Far more often than needed.",
  "*'Viral load every 3–4 months and CD4 every 3–6 months.'",
  "'No labs are needed once you're undetectable.' || Monitoring is ongoing.",
  "'Only a CD4 count once a year.' || Too infrequent; viral load is also tracked."],
 "Once undetectable, viral load is checked every 3–4 months; CD4 is checked every 3–6 months.")

q("art", "A nurse returns phone calls from four clients taking ART. Which client should the nurse call FIRST?",
 ["Client with mild nausea after doses || May be manageable; don't stop ART.",
  "Client asking about a refill date || Routine.",
  "*Client with a new blistering skin rash",
  "Client with mild fatigue this week || May be manageable."],
 "Report a severe or blistering rash, jaundice, dark urine or new depression immediately.")

q("art", "A client on ART says, 'I've been feeling down lately, so I bought St. John's wort.' Which response is best?",
 ["'That's a safe natural choice with ART.' || St. John's wort interacts with ART.",
  "'Stop your ART while you take it.' || Don't stop ART without guidance.",
  "*'New low mood should be reported, and St. John's wort interacts with ART.'",
  "'Feeling down is expected; just wait it out.' || New depression must be reported."],
 "New depression is reported immediately; St. John's wort, grapefruit with some regimens and OTC supplements interact with ART.")

q("adhere", "A client says, 'My pills make me queasy, so I've been skipping them.' Which intervention fits this barrier?",
 ["Refer to social work for copay help || Cost isn't the barrier.",
  "Tell the client to stop ART until the nausea ends || Missed doses allow resistance.",
  "Set up a pillbox and phone alarm || Forgetting isn't the barrier.",
  "*Notify the provider and suggest small, frequent meals"],
 "Nausea after pills: notify the provider and suggest small, frequent meals.")

q("adhere", "Which client statement shows understanding of why ART adherence matters?",
 ["*'If I miss doses, the virus can multiply and resist my medicine.'",
  "'Missing doses only makes me a little nauseated.' || Missed doses allow resistance.",
  "'Once I'm undetectable, skipping doses is fine.' || ART continues daily.",
  "'Skipping weekend doses is fine if I take weekdays.' || Missed doses allow resistance."],
 "Missed doses let HIV replicate and become resistant.")

q("prep", "An HIV-negative client asks about PrEP. Which statements by the nurse are accurate? " + SATA,
 ["*'PrEP is taken before a possible exposure.'",
  "*'You'll have HIV testing before and during PrEP.'",
  "'PrEP also protects you from other STIs.' || It doesn't prevent other STIs.",
  "*'PrEP comes as a daily pill or a long-acting injection.'",
  "'PrEP is started within 72 hours after an exposure.' || That describes PEP."],
 "PrEP: HIV-negative person, before possible exposure, daily oral or long-acting injectable, with HIV testing before and during.")

q("prep", "A client on day 10 of PEP after a sexual exposure says, 'I feel fine, so I'll stop the pills.' Best response?",
 ["'That's fine; 10 days is enough.' || PEP lasts 28 days.",
  "*'PEP is taken for 28 days, and you'll need follow-up HIV testing.'",
  "'Switch to lifelong ART instead.' || ART is for people with HIV.",
  "'You can stop if your partner tests negative.' || Complete the 28 days."],
 "PEP: start as soon as possible, no later than 72 hours, continue for 28 days, with follow-up HIV testing.")

q("preg", "A newborn of a mother with HIV is considered high-risk. At which times does the nurse expect an infant NAT? " + SATA,
 ["*At birth",
  "*At 14–21 days",
  "Only once at 18 months || NAT is done early and repeated.",
  "*At 1–2 months",
  "*At 4–6 months"],
 "High-risk infant NAT: birth, 14–21 days, 1–2 months and 4–6 months; maternal antibodies can persist up to 18 months.")

q("preg", "A client with HIV who just gave birth says, 'Now that the baby is here, I can stop my ART.' Best response?",
 ["'Yes, ART was only needed to protect the baby.' || ART is lifelong.",
  "'Stop until you finish breastfeeding.' || Continue ART postpartum.",
  "*'ART continues after delivery and through the postpartum period.'",
  "'You can stop once the baby's first test is negative.' || Continue ART."],
 "Continue ART through pregnancy, delivery and postpartum.")

q("needle", "A nurse observes four staff actions. Which action increases the risk of occupational HIV exposure and needs correction?",
 ["Placing a used needle in the sharps container right away || Correct practice.",
  "Wearing eye protection when splashes are possible || Correct practice.",
  "Activating the needle's safety device after use || Correct practice.",
  "*Recapping a used needle with two hands"],
 "Prevent exposure with gloves, eye protection, sharps safety devices and prompt sharps disposal.")

q("needle", "A nurse is stuck by a needle used on a client with HIV. Which actions are appropriate? " + SATA,
 ["*Wash the site with soap and water",
  "Squeeze the site and soak it in bleach || Wash with soap and water.",
  "*Report the exposure promptly",
  "Wait for the source client's labs before acting || Don't delay PEP evaluation.",
  "*Seek urgent PEP evaluation"],
 "Wash the site, report promptly and seek urgent PEP evaluation, ideally within 24 hours and no later than 72.")

q("nursing", "A client with HIV and severe immunosuppression asks about getting caught up on vaccines. Which response fits the lecture?",
 ["'People with HIV can't receive any vaccines.' || Vaccines are reviewed, not banned.",
  "'All vaccines, including live ones, are safe for you.' || Avoid live vaccines in severe immunosuppression.",
  "*'Let's review your vaccines; live vaccines may need to be avoided.'",
  "'Vaccines aren't needed once you're on ART.' || Vaccines are still reviewed."],
 "Review vaccines; avoid live vaccines in severe immunosuppression as directed.")
