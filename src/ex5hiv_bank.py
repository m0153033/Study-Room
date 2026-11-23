# Week 14.2 HIV/AIDS — updated lecture notes + AhaSlides review questions (11/23 lecture). Professor: know ART/PrEP/PEP/U=U; individual HIV drug names are not the priority.
EXAM = "e5"
T = "e5hiv"
CONCEPTS = {
 "what":"What HIV is & who's at risk",
 "trans":"Transmission",
 "vl":"Viral load, CD4 & U = U",
 "stages":"Stages of HIV",
 "cancer":"AIDS-defining cancers",
 "oi":"Opportunistic infections",
 "test":"Diagnosis & testing sequence",
 "monitor":"Monitoring schedule & labs",
 "art":"ART: start, continue & red flags",
 "adhere":"Adherence & therapeutic communication",
 "prep":"ART vs PrEP vs PEP vs U = U",
 "preg":"Pregnancy, birth & infant care",
 "needle":"Occupational exposure",
 "nursing":"Nursing assessment & teaching",
}
HI = ["vl","stages","oi","prep","art","adhere","preg","needle"]
# Updated lecture leaves these out. Don't write questions on them:
NOT_TESTED = ["individual HIV drug names or brand names (PrEP products, PEP regimens, ART combinations, antifungal names)", "drug classes / mechanisms of specific antiretrovirals",
 "screening age ranges (13–64)", "interrelated-concept lists and prevention levels"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- what ----------
q("what","What does HIV attack?",
 ["*CD4 T lymphocytes, weakening cell-mediated immunity","Red blood cells || Not the target.","Platelets || Not the target.","Liver cells || Not the target."],
 "HIV is a retrovirus that persists for life; treatment controls it but doesn't cure it.")
q("what","Which behaviors increase HIV risk? "+SATA,
 ["*Sharing injection equipment","*Condomless sex","*Multiple sexual partners","Sharing a drinking glass || Not a route."],
 "Perinatal exposure is also a risk.")

# ---------- transmission ----------
q("trans","Which body fluids can transmit HIV? "+SATA,
 ["*Blood","*Semen","*Vaginal and rectal secretions","*Breast milk","Saliva || Not transmitted this way."],
 "Routes: sex, blood exposure, pregnancy/delivery/breastfeeding.")
q("trans","A family member asks if they can catch HIV by hugging and sharing a bathroom. Best response?",
 ["*'No. HIV isn't spread by routine contact, saliva, sweat, urine or feces.'","'Yes, avoid all touching.' || Routine contact doesn't spread it.","'Only if you share a towel.' || Not a route.","'Only if the person coughs.' || Not a route."],
 "Standard precautions apply to every patient.")
q("trans","A client with HIV is admitted. Which precautions does the nurse use?",
 ["*Standard precautions, as for every patient","Airborne isolation || Not needed for HIV.","Contact isolation in a private room || HIV status alone doesn't require it.","Reverse isolation for all HIV clients || Not routine."],
 "HIV status alone doesn't require isolation.")

# ---------- viral load ----------
q("vl","What does viral load measure?",
 ["*HIV RNA copies per mL of blood, showing viral replication and treatment response","CD4 cells per mm³ || That's immune function.","Antibodies to HIV || That's a screening test.","White blood cell count || A different lab."],
 "High viral load = more replication; low CD4 = more immune compromise.")
q("vl","Which viral load means viral SUPPRESSION?",
 ["*Fewer than 200 copies/mL","Over 1,000 copies/mL || Not suppressed.","Exactly 500 copies/mL || Not suppressed.","Any detectable level || Suppression is under 200."],
 "Undetectable = below the lab's threshold (often 40–75 copies/mL).")
q("vl","After starting ART, a client's viral load fell from 250,000 to 150 copies/mL and CD4 rose from 110 to 240 cells/mm³. How does the nurse interpret this?",
 ["*ART is working; the client is virally suppressed but not necessarily undetectable","Treatment is failing || Labs are improving.","The client is cured and can stop ART || No cure.","The client now has AIDS || CD4 is rising above 200."],
 "Suppressed (under 200) doesn't always mean undetectable.")
q("vl","A client has been undetectable for 1 year on ART and asks about sexual transmission risk. What is accurate?",
 ["*Effectively no risk of sexual transmission while they keep taking ART and stay undetectable","Very high risk || Not with sustained suppression.","Zero risk even if ART stops || ART must continue.","Risk is the same as before treatment || U = U."],
 "U = U. Condoms still prevent other STIs.")
q("vl","What is a normal CD4 count per the lecture?",
 ["*About 500–1,600 cells/mm³","Under 200 cells/mm³ || That's AIDS.","About 50 cells/mm³ || Very low.","Over 10,000 cells/mm³ || Not normal."],
 "Falling CD4 = weakening immune system.")

# ---------- stages ----------
q("stages","A client has fever 101.3°F, swollen lymph nodes, night sweats and HR 105, and had unprotected sex about 3 weeks ago. Which cues suggest acute HIV? "+SATA,
 ["*Fever","*Swollen lymph nodes","*Night sweats","*Unprotected sex about 3 weeks ago","*Heart rate 105","Purple skin lesions || Kaposi sarcoma, stage 3."],
 "Recent exposure plus flu-like symptoms = acute infection.")
q("stages","Why is transmission risk highest in acute HIV (stage 1)?",
 ["*Viral load is very high","CD4 is above 1,600 || Not the reason.","Antibodies are highest || Not the reason.","The client has AIDS || That's stage 3."],
 "Antibody-only tests may be negative early.")
q("stages","Which findings indicate AIDS (stage 3)? "+SATA,
 ["*CD4 below 200 cells/mm³","*Kaposi sarcoma","*Lymphoma","*Unintentional weight loss over 10% (wasting)","Viral load under 200 copies/mL || That's suppression."],
 "AIDS = CD4 below 200 OR an AIDS-defining condition.")
q("stages","Without treatment, how long may chronic HIV (stage 2) last?",
 ["*About 10–15 years","1 week || Too short.","6 months || Too short.","It never progresses || It can."],
 "Often asymptomatic, but still transmissible if viral load is detectable.")

# ---------- cancers ----------
q("cancer","A client with AIDS has red-purple lesions on the skin and in the mouth. What does the nurse suspect?",
 ["*Kaposi sarcoma","Candidiasis || White plaques.","Melanoma || Not this picture.","Measles || Not this picture."],
 "Screen skin and mouth.")
q("cancer","Which are AIDS-defining cancers? "+SATA,
 ["*Kaposi sarcoma","*Non-Hodgkin lymphoma","*Primary CNS lymphoma","*Invasive cervical cancer","Basal cell carcinoma || Not AIDS-defining."],
 "Screen cervical cancer risk with Pap/HPV testing.")

# ---------- OIs ----------
q("oi","A client with a CD4 of 150 has a dry cough, fever, dyspnea and hypoxia. What is the likely infection?",
 ["*Pneumocystis jirovecii pneumonia (PJP)","Oral candidiasis || White plaques.","CMV retinitis || Vision loss.","MAC || Fever, sweats, diarrhea."],
 "Hypoxia is the priority cue.")
q("oi","Which drug does the lecture emphasize as PJP prophylaxis when CD4 is below 200?",
 ["*Trimethoprim-sulfamethoxazole","Oseltamivir || Influenza.","Acyclovir || Herpes.","Hydroxychloroquine || Lupus."],
 "Start prophylaxis when CD4 is below 200.")
q("oi","A client with HIV has white plaques in the mouth and pain when swallowing. What does the nurse suspect?",
 ["*Candidiasis, possibly esophageal","Kaposi sarcoma || Red-purple lesions.","PJP || Respiratory.","Toxoplasmosis || Neurologic."],
 "Painful swallowing suggests esophageal involvement.")
q("oi","A client with advanced HIV reports blurred vision and floaters. Which infection is the concern?",
 ["*Cytomegalovirus (CMV) retinitis","Toxoplasmosis || Brain lesions.","Candidiasis || Mouth or esophagus.","MAC || Systemic symptoms."],
 "CMV can also cause colitis or esophagitis.")
q("oi","A client with AIDS has a new headache, confusion and a seizure. Which conditions should the nurse consider? "+SATA,
 ["*Toxoplasmosis","*Primary CNS lymphoma","Oral candidiasis || Not neurologic.","Kaposi sarcoma of the skin || Not neurologic."],
 "Report neurologic changes promptly.")
q("oi","Which findings fit Mycobacterium avium complex (MAC) with very low CD4? "+SATA,
 ["*Fever","*Night sweats","*Diarrhea","*Weight loss","Red-purple skin lesions || Kaposi sarcoma."],
 "TB is screened with IGRA or PPD.")

# ---------- testing ----------
q("test","Which test detects HIV EARLIEST after exposure?",
 ["*HIV nucleic acid test (NAT) / viral load","Antibody-only home test || Misses the window period.","Western blot || No longer recommended.","CD4 count || Not diagnostic."],
 "NAT finds viral genetic material before antibodies form.")
q("test","What is the routine HIV screening sequence?",
 ["*4th-generation antigen/antibody test → HIV-1/2 differentiation assay if reactive → NAT if unclear","Western blot first || Not in the algorithm.","CD4 count alone || Not diagnostic.","Home antibody test only || Needs lab confirmation."],
 "A positive self-test needs lab confirmation.")
q("test","A client's home HIV test was negative 1 week after a high-risk exposure. What should the nurse explain?",
 ["*Antibody-only or home tests can miss early infection during the window period","The negative result rules out HIV || Not that early.","Home tests detect HIV earliest || NAT does.","No further testing is ever needed || Follow-up is needed."],
 "NAT is used when early infection is suspected.")

# ---------- monitoring ----------
q("monitor","How often is the CD4 count monitored per the lecture?",
 ["*Every 3–6 months","Every day || Too often.","Once a lifetime || Too rare.","Only at diagnosis || Ongoing."],
 "Viral load: 2–8 weeks after starting ART, every 4–8 weeks until undetectable, then every 3–4 months.")
q("monitor","Which labs and screens are monitored with HIV? "+SATA,
 ["*CBC","*Kidney and liver function","*Glucose and lipids","*Hepatitis, TB and STI screening","Anti-dsDNA || SLE."],
 "Pap/HPV screening as indicated.")
q("monitor","A client on ART has a rising viral load and falling CD4. What does this suggest?",
 ["*Possible resistance; notify the provider for evaluation","Expected improvement || Opposite trend.","The client is cured || No cure.","Stop ART now || Never stop on your own."],
 "Missed doses allow replication and resistance.")

# ---------- ART ----------
q("art","A newly diagnosed client has a viral load of 120,000 and CD4 of 650. When should ART start?",
 ["*As soon as possible, ideally right away","Only when CD4 drops below 200 || Don't wait.","After symptoms appear || Don't wait.","Only during pregnancy || Everyone with HIV."],
 "ART starts promptly even with a preserved CD4.")
q("art","A client starting ART asks which side effects to report immediately. Which should the nurse include? "+SATA,
 ["*Dark, tea-colored urine","*Yellow skin or eyes","*New depression","*Severe rash with blistering","Mild headache on the first day || Often manageable."],
 "These signal serious toxicity, mood changes or a severe skin reaction.")
q("art","Which discharge statement about ART needs more teaching?",
 ["*'Once my viral load is undetectable, I can stop my medication.'","'I'll take it every day for life.' || Correct.","'I'll check before taking supplements.' || Correct.","'I'll keep my lab appointments.' || Correct."],
 "Undetectable doesn't mean cured; ART continues.")
q("art","Which interactions does the lecture warn about with ART? "+SATA,
 ["*St. John's wort","*Grapefruit with some regimens","*Over-the-counter medicines and supplements","Water || Not an interaction."],
 "Mild nausea, diarrhea or fatigue may be manageable; don't stop ART without guidance.")

# ---------- adherence ----------
q("adhere","A client takes ART only 30% of the time. Which response is best?",
 ["*'Tell me about a typical day and when you usually take your pill.'","'Why aren't you taking your medicine?' || Sounds blaming.","'You'll get AIDS if you keep this up.' || Threatening.","'I'll tell your provider you're noncompliant.' || Not therapeutic."],
 "Open-ended, nonjudgmental questions find barriers.")
q("adhere","Match the adherence barrier with the best intervention. Which pairing is correct?",
 ["*Forgets doses on double shifts — phone alarm or pillbox","Can't afford copays — mental health referral || Social work.","Nausea after pills — stop ART || Notify provider; small meals.","Feels hopeless — pillbox || Mental health and peer support."],
 "Link doses to a daily habit.")
q("adhere","Which interventions match these barriers? "+SATA,
 ["*Nausea after pills: notify the provider and suggest small, frequent meals","*Can't afford copays: social work or case management referral","*Hopeless or isolated: mental health referral and peer support","Forgets doses: tell them to try harder || Use alarms or pillboxes."],
 "Avoid stigma.")
q("adhere","Why does adherence matter so much with ART?",
 ["*Missed doses let HIV replicate and become resistant","Missed doses only cause mild nausea || Resistance is the danger.","Missed doses make ART cure faster || No.","Adherence doesn't matter once undetectable || It still matters."],
 "Combination ART blocks multiple steps of the HIV life cycle.")

# ---------- ART / PrEP / PEP / U=U ----------
q("prep","Match each term with its meaning. Which pairing is correct?",
 ["*PrEP: before exposure, for an HIV-negative person","PEP: lifelong HIV treatment || That's ART.","ART: taken only before exposure || That's PrEP.","U = U: HIV is cured || Not a cure."],
 "PEP = within 72 hours after exposure, for 28 days.")
q("prep","Which statements are correct? "+SATA,
 ["*ART: ongoing, lifelong HIV treatment","*PrEP: HIV-negative person, before possible exposure","*PEP: after exposure, within 72 hours, for 28 days","*U = U: sustained undetectable on ART means no sexual transmission","PrEP prevents other STIs || It doesn't."],
 "Know the categories; drug names aren't the priority.")
q("prep","What must happen before and during PrEP?",
 ["*HIV testing to confirm the client is still negative","Nothing; PrEP needs no testing || Testing is required.","A CD4 count every week || Not required.","Stopping condoms because PrEP prevents all STIs || It doesn't."],
 "PrEP comes as daily oral or long-acting injectable options.")
q("prep","Which PEP teaching is correct? "+SATA,
 ["*Take it for 28 days","*Begin within 72 hours, ideally within 24 hours","*Follow-up HIV testing is required","Start only after baseline labs result || Don't delay.","Take it for 3 days || 28 days."],
 "PEP is time-sensitive.")

# ---------- pregnancy ----------
q("preg","A client with HIV has been undetectable on ART throughout pregnancy. Which statement is accurate?",
 ["*'Your baby will receive HIV medication for about 2 weeks after birth.'","'Your baby won't need any medication.' || Prophylaxis starts promptly.","'Your baby needs three-drug treatment for a year.' || That's high-risk, and not a year.","'You'll stop ART at delivery.' || Continue ART."],
 "High-risk infants get a three-drug regimen.")
q("preg","A pregnant client with HIV has a viral load of 1,500 copies/mL near delivery. What does the lecture support?",
 ["*Scheduled cesarean birth","Vaginal birth with invasive fetal monitoring || Avoid invasive monitoring.","Stopping ART before birth || Continue ART.","No change in plan || 1,000 or more supports cesarean."],
 "Under 1,000 near delivery favors vaginal birth.")
q("preg","Why is an infant NAT used instead of an antibody test?",
 ["*Maternal antibodies can persist up to 18 months","Infants can't give blood samples || Not the reason.","HIV can't infect infants || It can.","Antibody tests detect HIV too early || Not the reason."],
 "High-risk NAT: birth, 14–21 days, 1–2 months and 4–6 months.")
q("preg","A mother with sustained undetectable HIV asks about breastfeeding. What is accurate?",
 ["*Formula or donor milk removes the risk; breastfeeding risk is less than 1%, not zero","Breastfeeding has zero risk with U = U || Not zero.","Breastfeeding is required || Shared decision.","HIV is never in breast milk || It can be."],
 "Provide nonjudgmental, shared counseling.")

# ---------- needlestick ----------
q("needle","A nurse had a needlestick from a client with HIV 1 hour ago. What should the nurse do FIRST?",
 ["*Wash the site with soap and water and start PEP evaluation immediately","Finish the shift, then report || Don't delay.","Squeeze and soak the site in bleach || Not recommended.","Wait for the source client's labs before acting || Don't delay PEP."],
 "Report promptly and seek urgent exposure evaluation.")
q("needle","After a blood splash to the eyes, what should the nurse do?",
 ["*Rinse with water, report immediately and get evaluated for PEP","Apply antibiotic drops only || Not the step.","Do nothing if vision is fine || Evaluate.","Wait a week to see if symptoms appear || PEP within 72 hours."],
 "Prevent exposure with gloves, eye protection and sharps safety.")

# ---------- nursing ----------
q("nursing","Which findings should a client with HIV report? "+SATA,
 ["*Temperature above 100.4°F","*New cough or dyspnea","*Confusion","*Weight loss","Feeling well on ART || Expected."],
 "Also report falling CD4, rising viral load or neutropenia.")
q("nursing","Which infection-prevention teaching fits a client with HIV? "+SATA,
 ["*Hand hygiene and avoiding sick contacts","*Avoid undercooked food","*Ask someone else to clean litter boxes and cages","*Review vaccines; avoid live vaccines in severe immunosuppression as directed","Stop condom use once undetectable || Condoms prevent other STIs."],
 "Support sexual health, disclosure and community resources without stigma.")
