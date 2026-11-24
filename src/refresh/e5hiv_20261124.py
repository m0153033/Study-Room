T = "e5hiv"; SET = "20261124"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("what", "A 41-year-old client newly diagnosed with HIV explains the illness to a partner. Which statement shows correct understanding?",
 ["'The virus mostly destroys my red blood cells.' || HIV attacks CD4 T lymphocytes.",
  "'Once my symptoms fade, the virus is gone.' || HIV persists for life.",
  "*'The virus attacks my CD4 T cells and weakens my immunity.'",
  "'The virus mainly damages my liver cells.' || CD4 T cells are the target."],
 "HIV is a retrovirus that attacks CD4 T lymphocytes, weakening cell-mediated immunity; treatment controls it but doesn't cure it.")

q("trans", "A school nurse teaches a high school health class about HIV. Which student statements need correction? " + SATA,
 ["'Sharing needles can spread HIV.' || Accurate; blood transmits HIV.",
  "*'You can get HIV from sharing a water bottle.'",
  "'HIV can pass through breast milk.' || Accurate; breast milk transmits HIV.",
  "*'Hugging a friend with HIV can spread it.'",
  "'Condomless sex can spread HIV.' || Accurate; semen and vaginal fluids transmit HIV."],
 "HIV isn't spread by routine contact, saliva, sweat, urine or feces. Blood, semen, vaginal/rectal secretions and breast milk transmit it.")

q("vl", "Which statements about HIV lab results are accurate? " + SATA,
 ["*Viral load measures HIV RNA copies per mL of blood",
  "Suppressed always means undetectable || Undetectable is below the lab threshold, often 40–75.",
  "*A viral load under 200 copies/mL means suppression",
  "A normal CD4 count is under 200 cells/mm³ || Normal is about 500–1,600.",
  "*A falling CD4 count means the immune system is weakening"],
 "High viral load = more replication; low CD4 = more immune compromise.")

q("vl", "A 28-year-old client undetectable on ART for over a year asks if condoms are still worth using. Best response?",
 ["'Condoms are useless once you're undetectable.' || They still prevent other STIs.",
  "'You can stop ART since you can't transmit HIV.' || U = U requires staying on ART.",
  "'Undetectable means the virus is cured.' || HIV stays for life.",
  "*'U = U means no sexual HIV spread, but condoms still prevent other STIs.'"],
 "U = U: sustained undetectable on ART means effectively no sexual transmission; condoms still prevent other STIs.")

q("stages", "Which statement correctly compares stage 1 (acute) and stage 2 (chronic) HIV?",
 ["*Acute has flu-like symptoms and very high viral load; chronic is often silent but transmissible",
  "Chronic HIV can't be transmitted because there are no symptoms || Transmissible if viral load is detectable.",
  "Acute HIV is defined by a CD4 count below 200 cells/mm³ || That defines AIDS (stage 3).",
  "Chronic HIV lasts about 1 week before AIDS develops || Untreated, about 10–15 years."],
 "Acute: very high viral load, highest transmission risk. Chronic: often asymptomatic, still transmissible if detectable.")

q("stages", "A 47-year-old client with HIV has a CD4 count of 350 cells/mm³. Which new finding means the client now meets AIDS criteria?",
 ["Viral load of 150 copies/mL || This is suppression, not AIDS.",
  "CD4 count rising to 500 cells/mm³ || Shows improving immunity.",
  "*A new diagnosis of Kaposi sarcoma",
  "One day of mild fatigue || Not an AIDS-defining condition."],
 "AIDS = CD4 below 200 OR an AIDS-defining condition such as Kaposi sarcoma, lymphoma or wasting.")

q("cancer", "A 36-year-old woman with HIV asks why her provider wants regular Pap and HPV testing. Best response?",
 ["'A Pap test checks your viral load.' || Viral load is a blood test.",
  "*'Invasive cervical cancer is an AIDS-defining cancer, so we screen.'",
  "'A Pap test screens for Kaposi sarcoma.' || Kaposi is screened on skin and mouth.",
  "'A Pap test confirms your HIV diagnosis.' || Diagnosis uses the HIV testing sequence."],
 "AIDS-defining cancers: Kaposi sarcoma, non-Hodgkin lymphoma, primary CNS lymphoma, invasive cervical cancer.")

q("oi", "A nurse cares for four clients with AIDS. Which client should the nurse see FIRST?",
 ["Client with white plaques on the tongue || Candidiasis; not an oxygenation problem.",
  "Client with a red-purple skin lesion || Kaposi sarcoma; not urgent.",
  "Client with weeks of diarrhea and weight loss || MAC; less urgent than hypoxia.",
  "*Client with dry cough, dyspnea and falling oxygen saturation"],
 "Dry cough, fever, dyspnea and hypoxia suggest PJP; hypoxia is the priority cue.")

q("oi", "Which pairings of finding and opportunistic infection are correct? " + SATA,
 ["*Blurred vision and floaters: CMV retinitis",
  "Headache, confusion and seizure: oral candidiasis || Suggests toxoplasmosis or CNS lymphoma.",
  "*White mouth plaques with painful swallowing: candidiasis",
  "Dry cough and hypoxia: CMV colitis || Suggests PJP.",
  "*Fever, night sweats, diarrhea and weight loss: MAC"],
 "CMV can also cause colitis or esophagitis; report neurologic changes promptly.")

q("test", "A 24-year-old client calls to say a home HIV self-test was positive. What should the nurse explain?",
 ["'The home result is final; no lab test is needed.' || A positive self-test needs lab confirmation.",
  "'We'll check a CD4 count to confirm HIV.' || CD4 doesn't diagnose; the testing sequence does.",
  "*'A positive self-test needs lab confirmation.'",
  "'A Western blot is the first lab step.' || Lab testing starts with a 4th-generation antigen/antibody test."],
 "Sequence: 4th-generation antigen/antibody test, then HIV-1/2 differentiation assay if reactive, then NAT if unclear.")

q("monitor", "A client has been undetectable on ART for 6 months. How often does the nurse expect viral load monitoring now?",
 ["Every 2 weeks indefinitely || Once undetectable, every 3–4 months.",
  "*Every 3–4 months",
  "Only when symptoms appear || Monitoring is scheduled.",
  "Once a lifetime || Monitoring is ongoing."],
 "Viral load: 2–8 weeks after starting ART, every 4–8 weeks until undetectable, then every 3–4 months. CD4 every 3–6 months.")

q("art", "A 30-year-old newly diagnosed client with a CD4 of 900 says, 'My immunity is fine, so I'll wait on treatment.' Best response?",
 ["'You're right; start when CD4 drops below 200.' || ART starts promptly regardless.",
  "'Wait until you develop symptoms.' || Don't delay ART.",
  "*'ART is advised as soon as possible, even with a good CD4.'",
  "'ART is only needed during pregnancy.' || ART is lifelong treatment."],
 "ART starts as soon as possible, ideally right away, even with a preserved CD4.")

q("art", "Which client statement shows correct understanding of ART safety teaching?",
 ["'I'll stop my pills if I get mild nausea.' || Don't stop ART without guidance.",
  "'A blistering rash is expected; I'll wait it out.' || Report a severe rash immediately.",
  "'Grapefruit is fine with every regimen.' || Grapefruit interacts with some regimens.",
  "*'I'll ask before taking St. John's wort or any supplement.'"],
 "Interactions: St. John's wort, grapefruit with some regimens, OTC medicines and supplements.")

q("adhere", "A 52-year-old client says, 'I can't afford my copays, so I skip doses.' Which intervention fits best?",
 ["*Refer to social work or case management",
  "Set a phone alarm and use a pillbox || Doesn't address cost.",
  "Refer only to mental health services || Not the stated barrier.",
  "Suggest skipping doses on weekends || Missed doses allow resistance."],
 "Match the intervention to the barrier; missed doses let HIV replicate and become resistant.")

q("adhere", "A client says, 'I feel hopeless and alone since my diagnosis.' Which nurse responses support adherence? " + SATA,
 ["*'I'd like to connect you with mental health support.'",
  "'Why would you feel hopeless? It's treatable.' || Dismissive 'why' question.",
  "*'There's a peer support group you might find helpful.'",
  "'If you skip doses, you'll get AIDS.' || Threatening and stigmatizing.",
  "*'Tell me more about how you've been feeling.'"],
 "Hopeless or isolated: mental health referral and peer support; open-ended, nonjudgmental questions; avoid stigma.")

q("prep", "An HIV-negative 26-year-old starting PrEP asks if condoms are still needed. Best response?",
 ["'No; PrEP prevents all STIs.' || PrEP doesn't prevent other STIs.",
  "*'Yes; PrEP doesn't prevent other STIs.'",
  "'Only after you stop PrEP.' || Condoms still prevent other STIs on PrEP.",
  "'No; PrEP works after exposure instead.' || PrEP is taken before exposure."],
 "PrEP: HIV-negative person, before possible exposure, with HIV testing before and during.")

q("prep", "Which client is an appropriate candidate for PEP?",
 ["Client with HIV who needs lifelong treatment || That is ART.",
  "HIV-negative client wanting protection before future exposures || That is PrEP.",
  "*HIV-negative client exposed to blood 20 hours ago",
  "HIV-negative client exposed 5 days ago || Beyond the 72-hour limit."],
 "PEP: after exposure, as soon as possible, ideally within 24 hours, no later than 72; 28 days; follow-up testing.")

q("preg", "A newborn of a mother with HIV is considered high-risk. Which plan fits the lecture?",
 ["No medication and an antibody test at birth || High-risk infants get a three-drug regimen.",
  "*Three-drug regimen and NAT at birth, 14–21 days, 1–2 months and 4–6 months",
  "About 2 weeks of medication with no testing || Testing is still needed.",
  "One antibody test at 6 months || Maternal antibodies can persist up to 18 months."],
 "Infant NAT is used because maternal antibodies can persist up to 18 months.")

q("preg", "Which teaching fits a pregnant client with HIV? " + SATA,
 ["Breastfeeding has zero risk if undetectable || Risk is less than 1%, not zero.",
  "*Continue ART through pregnancy, delivery and postpartum",
  "*A viral load under 1,000 near delivery favors vaginal birth",
  "Stop ART once the baby is delivered || Continue postpartum.",
  "*Formula or donor milk removes breastfeeding transmission risk"],
 "1,000 or more near delivery: scheduled cesarean. Provide nonjudgmental, shared counseling about feeding.")

q("needle", "A nursing student stuck by a needle from a client with HIV says, 'I'll squeeze it and soak it in bleach.' Best response?",
 ["'Good idea; bleach will kill the virus.' || Wash with soap and water instead.",
  "'Finish your shift, then report it.' || Report promptly.",
  "'Wait until symptoms appear to report.' || PEP is time-sensitive.",
  "*'Wash it with soap and water, then report and get PEP evaluation now.'"],
 "Wash the site, report promptly and seek urgent exposure evaluation.")

q("needle", "A nurse had a needlestick 50 hours ago and never reported it. What is accurate?",
 ["PEP is no longer an option after 24 hours || Ideally within 24, but up to 72 hours.",
  "Only documenting the incident is needed now || Evaluation is still urgent.",
  "*PEP evaluation should still happen now, within the 72-hour limit",
  "Waiting for symptoms is the safest plan || Don't delay PEP."],
 "PEP ideally starts within 24 hours and no later than 72 hours.")

q("nursing", "A client with HIV plans meals for the week. Which choice needs correction?",
 ["Well-cooked chicken || Fully cooked food is safe.",
  "*Rare, undercooked hamburger",
  "Fully cooked scrambled eggs || Fully cooked food is safe.",
  "Thoroughly cooked fish || Fully cooked food is safe."],
 "Infection prevention: avoid undercooked food, practice hand hygiene and avoid sick contacts.")
