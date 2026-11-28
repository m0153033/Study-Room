T = "e5hiv"; SET = "20261128"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# what
q("what", "A nursing student describes HIV during a care conference. Which statement by the student is accurate?",
  ["'HIV mainly destroys platelets and causes bleeding.' || It attacks CD4 T lymphocytes",
   "'HIV clears from the body once symptoms stop.' || HIV persists for life",
   "*'HIV is a retrovirus that stays in the body for life.'",
   "'HIV mainly harms humoral immunity in the liver.' || It weakens cell-mediated immunity"],
  "HIV is a retrovirus that attacks CD4 T lymphocytes, weakening cell-mediated immunity; it persists for life and treatment controls but doesn't cure it.")

# trans
q("trans", "The roommate of a 44-year-old client with HIV asks which activity could actually spread the virus. Which activity does the nurse identify?",
  ["Sharing the same coffee mug || Saliva doesn't spread HIV",
   "*Condomless sex with the client",
   "Washing his sweat-soaked gym clothes || Sweat doesn't spread HIV",
   "Using the same bathroom toilet || Urine and feces don't spread HIV"],
  "HIV spreads through sex, blood exposure, and pregnancy, delivery or breastfeeding; not through routine contact, saliva, sweat, urine or feces.")

# vl (HI)
q("vl", "The nurse reviews viral loads for four clients on ART. Which client has NOT yet reached viral suppression?",
  ["Viral load of 150 copies/mL || Under 200 is suppression",
   "*Viral load of 850 copies/mL",
   "Viral load of 25 copies/mL, threshold 40 || Undetectable",
   "Viral load below the lab's threshold || Undetectable"],
  "Suppression is a viral load under 200 copies/mL; undetectable means below the lab's threshold (often 40–75 copies/mL).")
q("vl", "A 46-year-old chef with HIV sees a CD4 count of 1,100 cells/mm³ and worries it is too high. Which response by the nurse is accurate?",
  ["'That high a count means the virus is replicating.' || Viral load shows replication",
   "'That count means you now meet AIDS criteria.' || AIDS is CD4 below 200",
   "*'That count is within the normal range of about 500–1,600.'",
   "'That count means your treatment is failing.' || A falling CD4 is the concern"],
  "Normal CD4 is about 500–1,600 cells/mm³; a low or falling CD4 means more immune compromise. Viral load reflects replication.")

# stages (HI)
q("stages", "A 38-year-old client with HIV has a CD4 count of 310 cells/mm³ and is newly diagnosed with non-Hodgkin lymphoma. How does the nurse classify the stage?",
  ["Stage 1, since a new diagnosis was made || Stage 1 is acute, after recent exposure",
   "Stage 2, since the CD4 is above 200 || An AIDS-defining condition also counts",
   "*Stage 3 (AIDS), due to an AIDS-defining condition",
   "No stage, until the CD4 drops below 200 || AIDS-defining condition is enough"],
  "AIDS (stage 3) = CD4 below 200 OR an AIDS-defining condition, such as Kaposi sarcoma, lymphoma or wasting.")
q("stages", "Which findings in a client with HIV are each enough on their own to classify stage 3 (AIDS)? " + SATA,
  ["*A CD4 count of 150 cells/mm³",
   "*A new diagnosis of Kaposi sarcoma",
   "A viral load of 50,000 copies/mL || Viral load doesn't define AIDS",
   "*Unintentional weight loss over 10%",
   "Night sweats 3 weeks after an exposure || Suggests acute HIV"],
  "AIDS = CD4 below 200 OR an AIDS-defining condition, such as Kaposi sarcoma, lymphoma or wasting (unintentional weight loss over 10%).")

# cancer
q("cancer", "During oral care, the nurse finds a red-purple lesion on the palate of a client with AIDS. Which action is best?",
  ["Document it as oral candidiasis || Candidiasis causes white plaques",
   "Wait to see if it fades in a week || New lesions need follow-up",
   "*Report it as a possible Kaposi sarcoma lesion",
   "Request a Pap and HPV test || That screens cervical cancer risk"],
  "Kaposi sarcoma, an AIDS-defining cancer, causes red-purple lesions on the skin and in the mouth; screen skin and mouth.")

# oi (HI)
q("oi", "A client with advanced HIV says, 'I keep seeing floaters, so I probably need new glasses.' Which response is best?",
  ["'Floaters are common; see an optician soon.' || Vision changes need prompt follow-up",
   "*'I'll report this; it may be CMV retinitis, which can cause vision loss.'",
   "'This sounds like thrush spreading to your eyes.' || Candidiasis causes white plaques",
   "'Floaters usually mean you need more rest.' || Suggests CMV retinitis"],
  "CMV retinitis causes blurred vision, floaters and vision loss; CMV can also cause colitis or esophagitis.")
q("oi", "Which clients with HIV meet the CD4 threshold for starting PJP prophylaxis? " + SATA,
  ["*CD4 count of 110 cells/mm³",
   "CD4 count of 480 cells/mm³ || Prophylaxis starts below 200",
   "*CD4 count of 190 cells/mm³",
   "CD4 count of 210 cells/mm³ || Prophylaxis starts below 200"],
  "PJP prophylaxis starts when the CD4 count is below 200. PJP causes dry cough, fever, dyspnea and hypoxia.")

# test
q("test", "The nurse teaches a community group about HIV testing. Which participant statement needs correction?",
  ["'A reactive first test is followed by a differentiation assay.' || This is correct",
   "*'A positive home self-test means I definitely have HIV.'",
   "'An antibody-only test can miss very early infection.' || This is correct",
   "'A NAT finds viral genetic material before antibodies form.' || This is correct"],
  "A positive self-test needs lab confirmation. Sequence: 4th-generation antigen/antibody test, HIV-1/2 differentiation assay if reactive, NAT if unclear.")

# monitor
q("monitor", "The nurse reviews a monitoring plan for a client with HIV who has been undetectable on ART. Which item should the nurse question?",
  ["Viral load every 3–4 months || Correct once undetectable",
   "Glucose and lipid levels monitored || Part of HIV monitoring",
   "*CD4 count checked once a year",
   "Kidney and liver function monitored || Part of HIV monitoring"],
  "CD4 is monitored every 3–6 months; viral load every 3–4 months once undetectable. Monitoring also includes CBC, kidney and liver function, glucose and lipids.")

# art (HI)
q("art", "A client on ART plans to start an over-the-counter herbal sleep supplement. Which response by the nurse is best?",
  ["'Herbal products are natural, so they're safe with ART.' || Supplements can interact",
   "'Hold your ART on the nights you use it.' || Don't stop ART without guidance",
   "*'Let's check with your provider first; supplements can interact.'",
   "'Take the supplement instead of your evening ART.' || ART continues for life"],
  "ART interactions include St. John's wort, grapefruit with some regimens, and OTC medicines and supplements; don't stop ART without guidance.")
q("art", "The nurse returns calls from four clients who started ART last month. Which client needs follow-up FIRST?",
  ["Client with mild fatigue in the afternoons || May be manageable",
   "Client with mild nausea after morning doses || May be manageable",
   "*Client with dark urine and yellowing eyes",
   "Client with mild, occasional loose stools || May be manageable"],
  "Mild nausea, diarrhea or fatigue may be manageable. Jaundice, dark urine, severe rash or new depression are reported immediately.")

# adhere (HI)
q("adhere", "A 19-year-old who recently moved away from family says, 'No one understands what I'm going through, so why bother with my pills?' Which intervention fits this barrier?",
  ["Set up a pillbox with a phone alarm || That fits forgetting doses",
   "Refer to social work for copay help || That fits a cost barrier",
   "*Refer to mental health and a peer support group",
   "Suggest small, frequent meals with doses || That fits nausea"],
  "Hopeless or isolated: mental health referral and peer support. Match the intervention to the barrier and avoid stigma.")
q("adhere", "A nurse observes a nursing student talking with a client who misses ART doses. Which student statement needs correction?",
  ["'What usually happens on days you miss a dose?' || Open-ended and nonjudgmental",
   "*'You need to stop being so careless with your pills.'",
   "'Tell me about a typical evening at home.' || Open-ended and nonjudgmental",
   "'How do you feel after you take your pills?' || Open-ended and nonjudgmental"],
  "Open-ended, nonjudgmental questions find barriers to adherence; avoid stigma.")

# prep (HI)
q("prep", "An HIV-negative client shared injection equipment 60 hours ago and asks, 'Is it too late to do anything?' Which response is accurate?",
  ["'Yes; PEP only works within 24 hours.' || 24 hours is ideal; 72 is the limit",
   "'You can start PrEP, which is used after exposures.' || PrEP is before exposure",
   "*'PEP can still start now, since it's within 72 hours.'",
   "'Wait a few months, then get an HIV test.' || PEP is time-sensitive"],
  "PEP: after exposure, as soon as possible (ideally within 24 hours, no later than 72), for 28 days, with follow-up HIV testing.")
q("prep", "A 30-year-old on PrEP says, 'Since I take PrEP, I can skip the HIV tests at my visits.' Which response is best?",
  ["'That's fine; PrEP makes testing unneeded.' || Testing is required during PrEP",
   "*'HIV testing during PrEP confirms you're still negative.'",
   "'You only need a CD4 count each week instead.' || HIV testing is what's needed",
   "'Testing is needed only if you stop using condoms.' || Testing is needed regardless"],
  "PrEP: HIV-negative person, before possible exposure, with HIV testing before and during; it doesn't prevent other STIs.")

# preg (HI)
q("preg", "The nurse cares for two newborns: one whose mother was undetectable throughout pregnancy and one considered high-risk. Which statement is accurate?",
  ["Neither newborn needs any HIV medication after birth || Low-risk infant gets about 2 weeks",
   "*The low-risk infant gets about 2 weeks of medication; the high-risk infant gets three drugs",
   "Both newborns get a three-drug regimen for a year || Low-risk gets about 2 weeks",
   "Both newborns get one antibody test at birth and none after || Infants are tested with NAT"],
  "Infant of a mother undetectable throughout pregnancy: about 2 weeks of HIV medication. High-risk infants get a three-drug regimen and NAT testing.")
q("preg", "A pregnant client with HIV has a viral load of 1,400 copies/mL near delivery and asks why a cesarean is planned. Which explanation is accurate?",
  ["'Every client with HIV needs a cesarean.' || Under 1,000 favors vaginal birth",
   "'A cesarean lets you stop ART before birth.' || ART continues through delivery",
   "'Cesarean is planned when viral load is under 1,000.' || That favors vaginal birth",
   "*'A viral load of 1,000 or more near delivery supports cesarean.'"],
  "Near delivery: viral load under 1,000 favors vaginal birth; 1,000 or more supports a scheduled cesarean. Continue ART through pregnancy, delivery and postpartum.")

# needle (HI)
q("needle", "After a needlestick, a nurse makes several statements. Which statements need correction? " + SATA,
  ["'I'll wash the site with soap and water.' || This is correct",
   "*'I'll wait for the source client's labs before reporting.'",
   "*'It's been 30 hours, so PEP is no longer an option.'",
   "'If I start PEP, I'll take it for 28 days.' || This is correct"],
  "Wash the site, report promptly and seek urgent PEP evaluation without waiting for source labs; PEP ideally starts within 24 hours, no later than 72, for 28 days.")
q("needle", "A nurse is stuck by a used needle while placing it in an overfilled sharps container. After washing the site, what should the nurse do NEXT?",
  ["Replace the sharps container, then report || Reporting comes first",
   "Finish the medication pass, then report || Don't delay evaluation",
   "*Report it now and get urgent PEP evaluation",
   "Watch for symptoms over the next 72 hours || PEP evaluation is urgent"],
  "Wash the site, report promptly and seek urgent exposure evaluation; PEP ideally starts within 24 hours and no later than 72.")

# nursing
q("nursing", "A client with HIV and severe immunosuppression reviews infection-prevention teaching. Which statement needs more teaching?",
  ["'I'll wash my hands often and avoid sick people.' || This is correct",
   "'My partner will clean the cat's litter box.' || This is correct",
   "*'Live vaccines are fine for me right now.'",
   "'I'll cook my eggs and meat all the way through.' || This is correct"],
  "Infection prevention: hand hygiene, avoid sick contacts and undercooked food, have someone else clean litter boxes and cages, and avoid live vaccines in severe immunosuppression as directed.")
