# Week 14.2 HIV/AIDS — lesson plan, voiceover transcript, PowerPoint slides 1–25 (via notes).
EXAM = "e5"
T = "e5hiv"
CONCEPTS = {
 "concepts":"Interrelated concepts & prevention",
 "what":"What HIV is & who's at risk",
 "trans":"Transmission",
 "vl":"Viral load, CD4 & U = U",
 "stages":"Stages of HIV",
 "cancer":"AIDS-defining cancers",
 "oi":"Opportunistic infections",
 "test":"Screening & testing sequence",
 "monitor":"Monitoring schedule & labs",
 "art":"ART: adherence, resistance & side effects",
 "prep":"PrEP vs PEP",
 "preg":"Pregnancy, birth & infant care",
 "needle":"Occupational exposure",
 "nursing":"Nursing assessment & teaching",
}
HI = ["vl","stages","oi","prep","art","preg","trans","needle"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- concepts ----------
q("concepts","Which concepts does the lecture link to HIV? "+SATA,
 ["*Immunity","*Infection","*Nutrition","*Sexuality","*Tissue integrity","Cognition only || Not the listed set."],
 "The lesson plan also connects gas exchange and fluid/electrolyte balance.")
q("concepts","Which is an example of SECONDARY prevention for HIV?",
 ["*Screening and early diagnosis","Safer-sex education || Primary prevention.","Treating opportunistic infections || Not prevention level asked.","Hand hygiene for all || General."],
 "Primary = safer-sex education and support.")
q("concepts","How can nutrition affect a client with HIV?",
 ["*Nutrition deficits may worsen immune compromise","Nutrition has no effect || It matters.","Poor nutrition cures HIV || Not true.","Only vitamins matter || Overall nutrition matters."],
 "Infections like Kaposi sarcoma lesions and candidiasis impair tissue integrity.")

# ---------- what ----------
q("what","What does HIV attack?",
 ["*CD4 T lymphocytes","Red blood cells || Not the target.","Platelets || Not the target.","Hepatocytes || Not the target."],
 "HIV is a retrovirus that persists in the body; untreated it can progress to AIDS.")
q("what","Which behaviors increase HIV risk? "+SATA,
 ["*Sharing needles or syringes","*Condomless sex","*Multiple sexual partners","Sharing a drinking glass || Not a transmission route."],
 "Provide a nonjudgmental, individualized risk assessment.")

# ---------- transmission ----------
q("trans","Which body fluids can transmit HIV? "+SATA,
 ["*Blood","*Semen","*Vaginal and rectal secretions","*Breast milk","Saliva in ordinary contact || Not transmitted this way."],
 "Routes: sex, shared injection equipment, pregnancy/delivery/breastfeeding, rare needlesticks.")
q("trans","A family member asks if they can catch HIV by hugging and sharing a bathroom. Best response?",
 ["*'No. HIV isn't spread by casual contact, saliva, sweat, urine or feces in ordinary circumstances.'","'Yes, avoid all touching.' || Casual contact doesn't spread it.","'Only if you share a towel.' || Not a route.","'Only if the person sneezes.' || Not a route."],
 "Standard precautions apply to all patients.")

# ---------- viral load ----------
q("vl","What does viral load measure?",
 ["*HIV RNA copies per milliliter of blood; it shows response to ART","CD4 cells per mm³ || That's immune status.","Antibodies to HIV || That's the screening test.","White blood cell count || A different lab."],
 "CD4 reflects immune status; viral load reflects response to ART.")
q("vl","Which viral load means viral SUPPRESSION?",
 ["*Fewer than 200 copies/mL","Over 1,000 copies/mL || Not suppressed.","Exactly 500 copies/mL || Not suppressed.","Any detectable level || Suppression is under 200."],
 "Undetectable is below the assay threshold (slide: about 40–75 copies/mL).")
q("vl","What does U = U (undetectable equals untransmittable) mean?",
 ["*Sustained viral suppression with ART prevents SEXUAL transmission of HIV","HIV is cured || Not a cure.","Condoms are never needed for any reason || They still prevent other STIs.","Breastfeeding carries zero risk || Not zero."],
 "Confirm with lab monitoring; perinatal and breast-milk risk is not zero.")
q("vl","What is a normal CD4 count per the slides?",
 ["*About 500–1,600 cells/mm³","Under 200 cells/mm³ || That's AIDS.","About 50 cells/mm³ || Very low.","Over 10,000 cells/mm³ || Not normal range."],
 "A falling CD4 count means a weakening immune system.")

# ---------- stages ----------
q("stages","When does acute HIV (stage 1) usually start, and what does it look like?",
 ["*2–4 weeks after exposure, as a flu-like illness or no symptoms","Ten years after exposure || That's later progression.","Immediately after exposure with a purple rash || Not acute HIV.","Only with CD4 under 200 || That's stage 3."],
 "Fever, rash, sore throat, fatigue, swollen nodes, night sweats, mouth ulcers. Viral load is high, so transmission risk is high.")
q("stages","Why can an antibody-only test be negative in acute HIV?",
 ["*It's the window period before antibodies develop","The virus is gone || It's present.","Antibody tests never detect HIV || They do later.","The client has AIDS || Not the reason."],
 "4th-generation antigen/antibody tests detect infection earlier.")
q("stages","Which defines stage 3 HIV (AIDS)?",
 ["*CD4 below 200 cells/mm³ or an AIDS-defining condition","Viral load under 200 || That's suppression.","Any positive test || That's infection, not AIDS.","CD4 of 800 || Normal range."],
 "Lock this in for Exam 5.")
q("stages","Without treatment, how long may chronic HIV (stage 2) take to progress?",
 ["*About 10–15 years","1 week || Too short.","6 months || Too short.","It never progresses || It can."],
 "It may be asymptomatic for years.")
q("stages","Which findings fit stage 3 HIV (AIDS)? "+SATA,
 ["*Wasting and weight loss","*Recurrent fever and severe fatigue","*Opportunistic infections","*Neurologic changes","Rising CD4 count || CD4 falls."],
 "Also diarrhea and pneumonia.")

# ---------- cancers ----------
q("cancer","A client with AIDS has red-purple lesions in the mouth and on the skin. What does the nurse suspect?",
 ["*Kaposi sarcoma (HHV-8 related)","Candidiasis || White plaques.","Melanoma || Not HIV-related here.","Measles || Koplik spots."],
 "Lesions can also involve the GI tract or lungs: watch for bleeding, obstruction and breathing problems.")
q("cancer","Which are AIDS-defining cancers? "+SATA,
 ["*Kaposi sarcoma","*Non-Hodgkin lymphoma","*Primary CNS lymphoma","*Invasive cervical cancer","Basal cell carcinoma || Not AIDS-defining."],
 "Pap/HPV screening and HPV vaccination are emphasized.")
q("cancer","A client with AIDS has new headache, confusion and focal weakness. Which conditions should the nurse consider? "+SATA,
 ["*Primary CNS lymphoma","*Toxoplasmosis","Kaposi sarcoma of the skin || Skin lesions, not neuro signs.","Oral candidiasis || Not neuro."],
 "Report new neurologic changes promptly.")

# ---------- OIs ----------
q("oi","A client with a CD4 of 150 has a dry cough, fever, dyspnea and hypoxia. What is the likely infection?",
 ["*Pneumocystis jirovecii pneumonia (PJP)","Oral candidiasis || White plaques.","CMV retinitis || Vision loss.","MAC || Fever, sweats, diarrhea."],
 "Hypoxia is the priority cue.")
q("oi","Which drug is used as PJP prophylaxis when CD4 is below 200?",
 ["*TMP-SMX","Nystatin || Candidiasis.","Fluconazole || Candidiasis.","Oseltamivir || Influenza."],
 "TMP-SMX is also mentioned for toxoplasmosis prophylaxis with very low CD4.")
q("oi","A client with HIV has white plaques in the mouth and pain with swallowing. What does the nurse suspect, and what drugs are listed?",
 ["*Candidiasis (possibly esophageal); nystatin, clotrimazole or fluconazole","Kaposi sarcoma; TMP-SMX || Not this picture.","PJP; nystatin || Not this picture.","CMV; clotrimazole || Not this picture."],
 "Painful swallowing suggests esophageal involvement.")
q("oi","A client with advanced HIV reports blurred vision and floaters. Which infection is the concern?",
 ["*CMV retinitis","Toxoplasmosis || Brain lesions.","Candidiasis || Mouth or esophagus.","MAC || Systemic symptoms."],
 "CMV can also cause colitis and esophagitis.")
q("oi","Which findings fit Mycobacterium avium complex (MAC)? "+SATA,
 ["*Fever","*Night sweats","*Diarrhea","*Weight loss","Purple skin lesions || Kaposi sarcoma."],
 "MAC occurs in advanced disease.")
q("oi","How is TB screened for in a client with HIV?",
 ["*IGRA or PPD, with symptom review and sputum testing as indicated","Monospot || Mono.","Anti-CCP || RA.","Stool antigen || Rotavirus."],
 "Screen for TB, hepatitis and STIs.")

# ---------- testing ----------
q("test","Who should be screened for HIV per the slides?",
 ["*Everyone ages 13–64 at least once, repeated for ongoing risk and during pregnancy","Only people with symptoms || Screening is routine.","Only people over 65 || 13–64.","Only infants || Not the group."],
 "Secondary prevention = screening and early diagnosis.")
q("test","What is the recommended HIV testing sequence?",
 ["*4th-generation antigen/antibody test → HIV-1/2 antibody differentiation assay if reactive → NAT if unclear","Western blot first || Not the recommended algorithm.","CD4 count alone || Not diagnostic.","Viral load first for everyone || Not the sequence."],
 "Western blot is no longer the recommended confirmatory test.")

# ---------- monitoring ----------
q("monitor","How often is the CD4 count monitored?",
 ["*Every 3–6 months","Every day || Too often.","Once a lifetime || Too rare.","Only at diagnosis || Ongoing."],
 "Viral load: 2–8 weeks after starting ART, every 4–8 weeks until undetectable, then every 3–4 months.")
q("monitor","Which baseline and ongoing labs are monitored with HIV? "+SATA,
 ["*CBC","*Kidney and liver function","*Glucose and lipids","*Hepatitis, STI and TB screening","Anti-dsDNA || SLE."],
 "Resistance testing when treatment fails.")
q("monitor","A client's viral load is rising and CD4 is falling on ART. What does this suggest?",
 ["*Possible treatment failure; check adherence and resistance testing","Expected improvement || Opposite trend.","The client is cured || No cure.","A lab error always || Investigate."],
 "Resistance testing guides regimen changes.")

# ---------- ART ----------
q("art","Which statements about ART are correct? "+SATA,
 ["*It combines drugs targeting different life-cycle steps","*It starts promptly and continues lifelong","*It controls HIV but doesn't cure it","*Integrase inhibitor-based regimens are common first-line therapy","Clients can stop once undetectable || Never stop on your own."],
 "Adherence is critical.")
q("art","Which ART adverse effects are URGENT to report? "+SATA,
 ["*Blistering rash","*Hypersensitivity reaction","*Jaundice or dark urine","*Severe mood changes","Mild headache on day 1 || Monitor; not urgent."],
 "Also monitor nausea, diarrhea, fatigue, sleep, lipids, glucose and body-fat changes.")
q("art","Which supplements or foods do the slides warn about with some HIV regimens? "+SATA,
 ["*St. John's wort","*Grapefruit","Water || Not an interaction.","Vitamin C from food || Not listed."],
 "Encourage one pharmacy, reminders, and early reporting of side effects.")
q("art","Why do missed ART doses matter?",
 ["*They let HIV replicate and become resistant","They only cause mild nausea || Resistance is the danger.","They cure faster || No.","They don't matter once undetectable || They still matter."],
 "Never interrupt ART on your own.")

# ---------- PrEP / PEP ----------
q("prep","What is the difference between PrEP and PEP?",
 ["*PrEP is taken BEFORE possible exposure by HIV-negative people; PEP is started AFTER a possible exposure","They're the same || Different timing.","PrEP is taken after exposure || Reversed.","PEP is lifelong || 28 days."],
 "Don't confuse them.")
q("prep","When must PEP be started, and for how long?",
 ["*As soon as possible, within 72 hours, for 28 days","Within 2 weeks, for 1 year || Too late, too long.","Only after a positive test || It's prevention.","Within 72 hours, for 3 days || 28 days."],
 "Arrange follow-up HIV testing.")
q("prep","Before and during PrEP, what should be done? "+SATA,
 ["*Confirm negative HIV testing","*Screen for STIs","*Monitor kidney function with tenofovir","Stop condom use because PrEP prevents STIs || It doesn't prevent other STIs."],
 "PrEP doesn't prevent other STIs or pregnancy.")
q("prep","Which PrEP options are listed in the slides? "+SATA,
 ["*Daily oral Truvada","*Daily oral Descovy (not for receptive vaginal sex)","*Apretude injection every 2 months","*Yeztugo injection every 6 months","Tamiflu || Influenza."],
 "Know which is NOT for receptive vaginal sex: Descovy.")
q("prep","Which is an example PEP regimen in the slides?",
 ["*Raltegravir plus Truvada; current preferred options include Biktarvy or dolutegravir plus tenofovir and emtricitabine/lamivudine","Nystatin plus fluconazole || Antifungals.","TMP-SMX alone || PJP prophylaxis.","Zidovudine alone for 1 year || Not PEP."],
 "Slides contain both examples; follow local protocol.")

# ---------- pregnancy ----------
q("preg","A pregnant client with HIV has a viral load of 1,500 copies/mL near delivery. What does the slide support?",
 ["*Scheduled cesarean birth","Vaginal birth with invasive fetal monitoring || Avoid invasive monitoring.","Stopping ART before birth || Continue ART.","Breastfeeding without discussion || Use shared decision-making."],
 "1,000 or higher supports cesarean; below 1,000 supports vaginal birth.")
q("preg","Why are infant HIV antibody tests unreliable after birth?",
 ["*Maternal antibodies cross to the infant; NAT is used instead","Infants can't make blood || Not the reason.","HIV can't infect infants || It can.","Antibody tests are too sensitive || Not the reason."],
 "Use NAT at the specified infant testing intervals.")
q("preg","Which care applies to a pregnant client with HIV? "+SATA,
 ["*Continue ART through pregnancy, delivery and postpartum","*Avoid invasive fetal monitoring when possible","*IV zidovudine may be used based on viral load","*Newborn prophylaxis starts soon after birth","Stop ART in the third trimester || Continue it."],
 "Low-risk newborns get zidovudine for about 2 weeks; high-risk get three-drug treatment.")
q("preg","A mother with suppressed HIV asks about breastfeeding. What is accurate?",
 ["*Formula or donor milk removes breast-milk exposure; breastfeeding with sustained suppression carries low but nonzero risk","Breastfeeding has zero risk with U = U || Not zero.","Breastfeeding is required || Shared decision.","HIV is never in breast milk || It can be."],
 "Use shared decision-making.")
q("preg","When should HIV testing be repeated in pregnancy?",
 ["*In the third trimester when at risk, with rapid testing in labor if status is unknown","Never after the first visit || Repeat when at risk.","Only after delivery || Test during prenatal care.","Only if the baby is sick || Too late."],
 "Test during prenatal care.")

# ---------- needlestick ----------
q("needle","A nurse gets a needlestick from a client with HIV. What should the nurse do FIRST?",
 ["*Wash the site with soap and water, then report immediately","Squeeze and soak in bleach || Not recommended.","Finish the shift, then report || Report immediately.","Wait for symptoms || PEP must start early."],
 "Seek urgent evaluation for PEP within 72 hours; earlier is better.")
q("needle","After a mucosal splash to the eyes, what should the nurse do?",
 ["*Rinse with water, report immediately and be evaluated for PEP","Apply antibiotic drops only || Not the step.","Do nothing if vision is fine || Evaluate.","Wait 1 week || PEP within 72 hours."],
 "Prevent injury with sharps containers, safety devices, gloves and eye protection.")

# ---------- nursing ----------
q("nursing","Which assessments are priorities for a client with HIV? "+SATA,
 ["*Respiratory and neurologic status","*Skin and mucosa","*Nutrition and daily weight","*CD4, viral load and WBC","Visual acuity only || Not the focus."],
 "Report fever, cough, dyspnea, confusion and worsening immunosuppression.")
q("nursing","Which findings should a client with HIV report? "+SATA,
 ["*Fever over 100.4°F","*Weight loss","*Persistent cough","*New sores or lesions, or confusion","Feeling well after taking ART || Expected."],
 "Also medication reactions.")
q("nursing","Which psychosocial needs should the nurse assess in a client with HIV? "+SATA,
 ["*Stigma and emotional health","*Support system","*Housing, food and transportation barriers","*Partner communication and confidentiality","Favorite hobbies only || Not the focus."],
 "Connect the client with interdisciplinary resources without judgment.")
