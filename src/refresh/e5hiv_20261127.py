T = "e5hiv"; SET = "20261127"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# what
q("what", "The nurse reviews HIV basics with a 58-year-old retired teacher who was just diagnosed. Which client statement needs correction?",
  ["'The virus targets my CD4 T cells.' || This is correct",
   "*'The virus will leave my body once treatment works.'",
   "'Treatment can keep the virus under control.' || This is correct",
   "'The virus weakens my cell-mediated immunity.' || This is correct"],
  "HIV is a retrovirus that attacks CD4 T lymphocytes and persists for life; treatment controls it but doesn't cure it.")

# trans
q("trans", "A 15-year-old at a youth clinic asks how HIV is spread. Which routes does the nurse include? " + SATA,
  ["*Condomless sex",
   "Kissing a friend on the cheek || Saliva doesn't spread HIV",
   "*Sharing injection needles",
   "Using a public toilet || Urine and feces don't spread HIV",
   "*Breastfeeding"],
  "HIV spreads through sex, blood exposure, and pregnancy, delivery or breastfeeding; not through routine contact, saliva, sweat, urine or feces.")

# vl (HI)
q("vl", "The nurse reviews lab trends for four clients with HIV. Which trend shows the immune system is weakening?",
  ["*CD4 falling from 650 to 410 cells/mm³",
   "Viral load falling from 40,000 to undetectable || Shows treatment response",
   "CD4 rising from 300 to 520 cells/mm³ || Immunity is improving",
   "Viral load staying undetectable for a year || Virus is controlled"],
  "A falling CD4 count means the immune system is weakening; low CD4 = more immune compromise. Viral load reflects replication and treatment response.")
q("vl", "A 36-year-old bus driver has been undetectable on ART for 18 months. Which client statements need correction? " + SATA,
  ["*'Since I'm undetectable, I can stop taking ART.'",
   "'Staying undetectable depends on taking ART consistently.' || This is correct",
   "*'U = U also protects me from other STIs.'",
   "'I effectively can't pass HIV to partners through sex.' || This is correct"],
  "U = U: sustained undetectable on ART means effectively no sexual transmission. ART continues, and condoms still prevent other STIs.")

# stages (HI)
q("stages", "A 23-year-old barista has fever, sore throat, rash and swollen lymph nodes 3 weeks after condomless sex with a new partner. Which statement about this likely stage is accurate?",
  ["*Viral load is likely very high, so transmission risk is highest",
   "A CD4 below 200 cells/mm³ is what defines this stage || That defines stage 3 (AIDS)",
   "This stage usually lasts about 10–15 years || That describes stage 2",
   "Transmission is unlikely until the symptoms resolve || Risk is highest now"],
  "Recent exposure plus flu-like symptoms = acute HIV (stage 1): very high viral load and the highest transmission risk.")
q("stages", "A 61-year-old client with untreated HIV has a CD4 of 420 cells/mm³, no symptoms and a detectable viral load. He says, 'I feel fine, so I can't spread it.' Best response?",
  ["'Right; HIV spreads only when symptoms are present.' || Chronic HIV is still transmissible",
   "*'This stage is often silent but can spread while virus is detectable.'",
   "'You have AIDS, so the risk depends on your CD4.' || CD4 above 200, no AIDS-defining condition",
   "'You're in the acute stage, which has no transmission risk.' || Acute has flu-like symptoms and highest risk"],
  "Chronic HIV (stage 2) is often asymptomatic but still transmissible if the viral load is detectable; untreated it lasts about 10–15 years.")

# cancer
q("cancer", "The nurse teaches a newly diagnosed 29-year-old woman with HIV about cancer risk. Which client statement needs correction?",
  ["'I'll watch my skin and mouth for red-purple spots.' || Correct; screens for Kaposi sarcoma",
   "'Invasive cervical cancer is an AIDS-defining cancer.' || This is correct",
   "*'Pap and HPV tests aren't needed since they don't relate to HIV.'",
   "'Lymphoma can be an AIDS-defining cancer.' || This is correct"],
  "AIDS-defining cancers: Kaposi sarcoma, non-Hodgkin lymphoma, primary CNS lymphoma and invasive cervical cancer; screen cervical risk with Pap/HPV testing.")

# oi (HI)
q("oi", "A 35-year-old client with a CD4 of 60 cells/mm³ has a dry cough, fever, dyspnea and an oxygen saturation of 88%. Which cue is the nurse's priority?",
  ["Temperature of 100.9°F || Important, but hypoxia comes first",
   "*Oxygen saturation of 88%",
   "Dry, nonproductive cough || Expected with PJP; not the priority",
   "CD4 count of 60 cells/mm³ || A risk factor, not the acute priority"],
  "Dry cough, fever, dyspnea and hypoxia suggest PJP; hypoxia is the priority cue.")
q("oi", "A client with advanced HIV is being screened for tuberculosis. Which tests does the nurse expect? " + SATA,
  ["*IGRA (interferon-gamma release assay)",
   "Viral load || Measures HIV replication",
   "*PPD (purified protein derivative)",
   "CD4 count || Measures immune status"],
  "TB is screened with IGRA or PPD. Viral load reflects HIV replication; CD4 reflects immune status.")

# test
q("test", "A 32-year-old long-haul truck driver requests routine HIV screening. Which test does the nurse expect to be done first?",
  ["HIV-1/2 differentiation assay || Done next if the first test is reactive",
   "HIV nucleic acid test || Used if results are unclear",
   "*4th-generation antigen/antibody test",
   "Western blot || Not part of the sequence taught"],
  "Sequence: 4th-generation antigen/antibody test, then HIV-1/2 differentiation assay if reactive, then NAT if unclear.")

# monitor
q("monitor", "A client on ART has a viral load that is falling but still detectable. How often does the nurse expect viral load checks until it is undetectable?",
  ["Every 3–4 months || That is the schedule once undetectable",
   "*Every 4–8 weeks",
   "Once a year || Too infrequent",
   "Only when symptoms appear || Labs are scheduled, not symptom-based"],
  "Viral load: 2–8 weeks after starting ART, every 4–8 weeks until undetectable, then every 3–4 months.")

# art (HI)
q("art", "A 34-year-old graphic designer is starting ART. Which client statement shows a need for more teaching?",
  ["'I'll call right away if my eyes turn yellow.' || Correct; jaundice is reported immediately",
   "'I'll ask before taking any over-the-counter medicine.' || Correct; OTC drugs can interact",
   "*'If I get mild diarrhea, I'll stop my pills until it passes.'",
   "'I'll keep taking it even after I'm undetectable.' || Correct; ART is lifelong"],
  "Mild nausea, diarrhea or fatigue may be manageable; don't stop ART without guidance. Report jaundice, dark urine, severe rash or new depression immediately.")
q("art", "Six weeks after starting ART, a client says, 'I've lost interest in everything and feel sad most days.' Which action is best?",
  ["Reassure the client this is a normal adjustment || New depression is reported",
   "Advise holding ART until the mood improves || Don't stop ART without guidance",
   "Suggest trying St. John's wort for mood || It interacts with ART",
   "*Report the new depression to the provider promptly"],
  "New depression is a red flag on ART and is reported immediately; St. John's wort interacts with ART.")

# adhere (HI)
q("adhere", "A client's viral load has risen after months of being undetectable, and the client admits missing doses. What should the nurse do FIRST?",
  ["Refer the client to social work right away || The barrier isn't known yet",
   "*Ask open-ended questions about what makes doses hard",
   "Explain that the resistance is the client's own fault || Adds stigma",
   "Set up a pillbox and phone alarm || The barrier isn't known yet"],
  "Open-ended, nonjudgmental questions find the barrier so the intervention can match it; avoid stigma.")
q("adhere", "A 63-year-old retiree on a fixed income says she has been skipping ART doses to make her refill last longer. Which intervention fits best?",
  ["Teach her to link doses to a daily habit || That fits forgetting doses",
   "Refer her to a peer support group || That fits isolation",
   "*Refer her to social work or case management",
   "Suggest small, frequent meals || That fits nausea"],
  "Cost barrier: social work or case management referral. Missed doses let HIV replicate and become resistant.")

# prep (HI)
q("prep", "A 27-year-old HIV-negative client whose partner has HIV wants ongoing protection before any exposure. Which statement by the nurse is accurate?",
  ["*'You'll have HIV testing before starting PrEP and while on it.'",
   "'A 28-day course of PEP will protect you long-term.' || PEP is after an exposure",
   "'PrEP will also protect you from other STIs.' || PrEP doesn't prevent other STIs",
   "'You'll start ART because your partner has HIV.' || ART treats people with HIV"],
  "PrEP: HIV-negative person, before possible exposure, daily oral or long-acting injectable, with HIV testing before and during.")
q("prep", "Which clients are candidates for PEP rather than PrEP or ART? " + SATA,
  ["*An HIV-negative client whose condom broke 18 hours ago",
   "An HIV-negative client wanting protection before future exposures || That is PrEP",
   "*An HIV-negative client who shared injection equipment last night",
   "An HIV-negative client exposed 4 days ago || Beyond the 72-hour limit",
   "A client with HIV who needs lifelong treatment || That is ART"],
  "PEP is started after an exposure, as soon as possible (ideally within 24 hours, no later than 72), for 28 days with follow-up HIV testing.")

# preg (HI)
q("preg", "The nurse reviews delivery plans for four pregnant clients with HIV near delivery. Which plan should the nurse question?",
  ["Viral load 300 copies/mL; planned vaginal birth || Under 1,000 favors vaginal birth",
   "*Viral load 1,200 copies/mL; planned vaginal birth",
   "Viral load 2,000 copies/mL; scheduled cesarean || 1,000 or more supports cesarean",
   "Undetectable viral load; planned vaginal birth || Under 1,000 favors vaginal birth"],
  "Near delivery, a viral load under 1,000 favors vaginal birth; 1,000 or more supports a scheduled cesarean.")
q("preg", "Parents of a 3-week-old high-risk infant ask why more blood tests are needed when the test at birth was negative. Best response?",
  ["'One negative test at birth rules out HIV.' || Testing is repeated in high-risk infants",
   "'These tests check your baby's own antibodies.' || Maternal antibodies can persist",
   "*'NAT is repeated at set times, including 1–2 and 4–6 months.'",
   "'Testing continues only until breastfeeding starts.' || Not how the schedule works"],
  "High-risk infant NAT: birth, 14–21 days, 1–2 months and 4–6 months. NAT is used because maternal antibodies can persist up to 18 months.")

# needle (HI)
q("needle", "An emergency department technician is stuck by a used needle. When should PEP ideally begin?",
  ["Within 7 days of the exposure || Too late; limit is 72 hours",
   "*Within 24 hours, and no later than 72 hours",
   "After the source client's labs return || Don't wait for results",
   "Within 28 days of the exposure || 28 days is the length of PEP"],
  "PEP after occupational exposure: as soon as possible, ideally within 24 hours, no later than 72; taken for 28 days.")
q("needle", "A nurse precepting a new graduate observes the following actions. Which actions need correction? " + SATA,
  ["*Recapping a used needle with two hands",
   "Activating the safety device right after an injection || This is correct",
   "*Leaving a used needle on the bedside table to discard later",
   "Wearing eye protection when splashes are possible || This is correct"],
  "Prevent occupational exposure with gloves, eye protection, sharps safety devices and immediate sharps container disposal.")

# nursing
q("nursing", "A 70-year-old client with HIV calls the clinic. Which client report needs prompt follow-up by the provider?",
  ["A temperature of 99.1°F this morning || Below 100.4°F",
   "A stable weight over the past month || Weight loss is the concern",
   "*A temperature of 100.8°F since last night",
   "Feeling well on ART this week || Not a warning sign"],
  "Clients with HIV report temperature above 100.4°F, new cough or dyspnea, confusion and weight loss.")
