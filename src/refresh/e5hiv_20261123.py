T = "e5hiv"; SET = "20261123"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("concepts", "A community health nurse is planning HIV (human immunodeficiency virus) prevention activities for a county clinic. Which activity is an example of PRIMARY prevention?",
  ["Offering HIV screening to adults at a health fair || Screening and early diagnosis is secondary prevention",
   "Testing a 22-year-old pregnant client at her first prenatal visit || Testing for early diagnosis is secondary prevention",
   "*Safer-sex education and support for a high school group",
   "Rapid HIV testing in labor for a client with unknown status || This is screening/early diagnosis, which is secondary prevention"],
  "Primary prevention for HIV is safer-sex education and support, which aims to stop infection before it happens. Screening and early diagnosis are secondary prevention.")

q("what", "A 52-year-old client newly diagnosed with HIV (human immunodeficiency virus) asks what the virus does in the body. Which response by the nurse is accurate?",
  ["'It attacks your red blood cells and mainly causes anemia.' || HIV attacks CD4 T lymphocytes, not red blood cells",
   "'It clears from your body once the first flu-like illness ends in a few weeks.' || HIV is a retrovirus that persists in the body",
   "'It mainly destroys liver cells over many years.' || HIV targets CD4 T lymphocytes, not hepatocytes",
   "*'It is a retrovirus that attacks CD4 T cells and can progress to AIDS.'"],
  "HIV is a retrovirus that attacks CD4 (cluster of differentiation 4) T lymphocytes and persists in the body; untreated, it can progress to AIDS (acquired immunodeficiency syndrome).")

q("trans", "A nurse is teaching a group of college students how HIV (human immunodeficiency virus) is transmitted. Which routes should the nurse include? " + SATA,
  ["*Sexual contact",
   "*Sharing injection equipment",
   "Sharing eating utensils at meals || Saliva in ordinary contact does not transmit HIV",
   "*Pregnancy, delivery or breastfeeding",
   "Using the same toilet as an infected person || Urine and feces do not spread HIV in ordinary circumstances"],
  "HIV is transmitted through sex, shared injection equipment, pregnancy/delivery/breastfeeding and rare needlesticks, via blood, semen, vaginal/rectal secretions and breast milk. Casual contact, saliva, sweat, urine and feces do not spread it in ordinary circumstances.")

q("trans", "The roommate of a 23-year-old client with HIV (human immunodeficiency virus) is learning about transmission. Which statement by the roommate needs MORE teaching?",
  ["'Hugging him is safe.' || Correct: casual contact does not spread HIV",
   "*'I shouldn't share a drinking glass with him.'",
   "'Sweat on shared gym equipment won't spread it.' || Correct: sweat does not transmit HIV in ordinary circumstances",
   "'Breast milk is one fluid that can carry the virus.' || Correct: breast milk can transmit HIV"],
  "Saliva in ordinary contact does not transmit HIV, so sharing a drinking glass is not a risk. Casual contact and sweat do not spread HIV; blood, semen, vaginal/rectal secretions and breast milk can.")

q("vl", "A 38-year-old client on ART (antiretroviral therapy) has a viral load of 150 copies/mL and a CD4 (cluster of differentiation 4) count of 650 cells/mm³. How should the nurse interpret these results?",
  ["Treatment failure that needs resistance testing || Failure is a rising viral load with a falling CD4; these results are favorable",
   "*Viral suppression with a CD4 count in the normal range",
   "Stage 3 HIV (AIDS) || Stage 3 requires a CD4 below 200 or an AIDS-defining condition",
   "Undetectable, so HIV cannot be passed by any route || 150 is above the undetectable threshold, and U = U covers sexual transmission only"],
  "A viral load under 200 copies/mL means viral suppression, and a normal CD4 count is about 500-1,600 cells/mm³. Viral load reflects response to ART; CD4 reflects immune status.")

q("vl", "A client with a sustained undetectable viral load on ART (antiretroviral therapy) says, 'Now I can't pass HIV to anyone in any way.' Which response by the nurse is BEST?",
  ["'That's right, because undetectable means the virus is cured and gone for good.' || ART controls HIV but does not cure it",
   "'That's true, so you can stop your lab monitoring.' || U = U should be confirmed with ongoing lab monitoring",
   "*'It prevents sexual spread, but pregnancy and breast-milk risk isn't zero.'",
   "'Undetectable means your CD4 count is normal now.' || Viral load measures HIV RNA, not CD4 cells"],
  "U = U (undetectable equals untransmittable) means sustained viral suppression with ART prevents SEXUAL transmission. It must be confirmed with lab monitoring, and perinatal and breast-milk risk is not zero.")

q("stages", "A 26-year-old client has fever, rash, sore throat, swollen lymph nodes and mouth ulcers 3 weeks after condomless sex. An antibody-only HIV (human immunodeficiency virus) test is negative. What should the nurse understand?",
  ["The negative test rules out HIV infection || Antibodies may not have formed yet (window period)",
   "These symptoms mean the client has stage 3 HIV || Stage 3 is defined by CD4 below 200 or an AIDS-defining condition",
   "Transmission risk is low because antibodies haven't formed and the test is negative || Viral load is high in acute HIV, so transmission risk is high",
   "*This may be acute HIV in the window period, with high transmission risk"],
  "Acute HIV (stage 1) usually starts 2-4 weeks after exposure as a flu-like illness. An antibody-only test can be negative in the window period; viral load is high, so transmission risk is high. 4th-generation antigen/antibody tests detect infection earlier.")

q("stages", "A 44-year-old client with HIV (human immunodeficiency virus) has a CD4 (cluster of differentiation 4) count of 180 cells/mm³ and no opportunistic infections. How does the nurse classify this stage?",
  ["*Stage 3 (AIDS)",
   "Stage 1 (acute HIV) || Acute HIV is the flu-like illness 2-4 weeks after exposure",
   "Stage 2 (chronic HIV) because no AIDS-defining condition is present || A CD4 below 200 alone defines stage 3",
   "It can't be staged until an opportunistic infection appears || CD4 below 200 is enough for stage 3"],
  "Stage 3 HIV (AIDS) is defined by a CD4 below 200 cells/mm³ OR an AIDS-defining condition. Either one is enough.")

q("cancer", "A 45-year-old client with AIDS (acquired immunodeficiency syndrome) has Kaposi sarcoma involving the GI (gastrointestinal) tract and lungs. Which complications should the nurse monitor for? " + SATA,
  ["*Bleeding",
   "Painless white oral plaques || White plaques suggest candidiasis, not Kaposi sarcoma",
   "*Obstruction",
   "*Breathing problems",
   "A rising CD4 (cluster of differentiation 4) count || A rising CD4 is not a complication of Kaposi sarcoma"],
  "Kaposi sarcoma (HHV-8 related) causes red-purple lesions of the skin and mouth and can also involve the GI tract or lungs. Watch for bleeding, obstruction and breathing problems.")

q("oi", "A nurse is caring for four clients with advanced HIV (human immunodeficiency virus). Which client should the nurse assess FIRST?",
  ["A client with white plaques in the mouth || Candidiasis needs treatment but is not the priority over hypoxia",
   "A client with night sweats and diarrhea || These suggest MAC, which is less urgent than hypoxia",
   "*A client with a CD4 of 130, dry cough, dyspnea and hypoxia",
   "A client with chronic fatigue, stable vital signs and a normal temperature || Stable fatigue is less urgent than hypoxia"],
  "Dry cough, fever, dyspnea and hypoxia with a CD4 under 200 suggest Pneumocystis jirovecii pneumonia (PJP). Hypoxia is the priority cue.")

q("oi", "Which pairings of an opportunistic infection with its finding or drug are correct? " + SATA,
  ["*PJP (Pneumocystis jirovecii pneumonia): TMP-SMX (trimethoprim-sulfamethoxazole) prophylaxis when CD4 is below 200",
   "Candidiasis: treated with TMP-SMX (trimethoprim-sulfamethoxazole) || Listed drugs for candidiasis are nystatin, clotrimazole or fluconazole",
   "*CMV (cytomegalovirus): retinitis with blurred vision and floaters",
   "*MAC (Mycobacterium avium complex): fever, night sweats, diarrhea and weight loss",
   "Toxoplasmosis: white plaques in the mouth || White oral plaques are candidiasis"],
  "TMP-SMX is PJP prophylaxis when CD4 is below 200 (also mentioned for toxoplasmosis with very low CD4). CMV causes retinitis (blurred vision, floaters), colitis and esophagitis. MAC causes fever, night sweats, diarrhea and weight loss in advanced disease. Candidiasis is treated with nystatin, clotrimazole or fluconazole.")

q("test", "A 19-year-old client's 4th-generation antigen/antibody HIV (human immunodeficiency virus) test is reactive. Which test does the nurse expect NEXT?",
  ["A Western blot to confirm || Western blot is no longer the recommended confirmatory test",
   "A CD4 (cluster of differentiation 4) count to confirm the diagnosis || CD4 reflects immune status and is not the confirmatory step",
   "*An HIV-1/2 antibody differentiation assay",
   "A repeat 4th-generation test in one year || This delays diagnosis; a reactive result is followed by a differentiation assay"],
  "The recommended sequence is a 4th-generation antigen/antibody test, then an HIV-1/2 antibody differentiation assay if reactive, then a NAT (nucleic acid test) if results are unclear.")

q("monitor", "A 33-year-old client started ART (antiretroviral therapy) 3 weeks ago. Which statement about the monitoring plan is correct?",
  ["*Viral load at 2-8 weeks, then every 4-8 weeks until undetectable",
   "The CD4 (cluster of differentiation 4) count will be checked every day || CD4 is monitored every 3-6 months",
   "Viral load is checked only once at diagnosis, since CD4 shows the response to ART || Viral load is repeated to track response to ART",
   "Labs stop once the client feels well on ART || Ongoing labs are needed; resistance testing is done if treatment fails"],
  "Viral load is checked 2-8 weeks after starting ART, every 4-8 weeks until undetectable, then every 3-4 months. CD4 is checked every 3-6 months.")

q("art", "A 31-year-old client is starting ART (antiretroviral therapy). Which statement indicates the client understands the teaching?",
  ["'I can stop my pills once my viral load is undetectable.' || ART continues lifelong",
   "'Missing a dose now and then won't really matter.' || Missed doses let HIV replicate and become resistant",
   "'St. John's wort should be fine with my regimen.' || The slides warn about St. John's wort with some regimens",
   "*'I'll use one pharmacy and set reminders so I don't miss doses.'"],
  "Adherence is critical: missed doses let HIV replicate and become resistant. Encourage one pharmacy, reminders and early reporting of side effects. ART is lifelong and controls but does not cure HIV.")

q("art", "A client taking an integrase inhibitor-based ART (antiretroviral therapy) regimen calls the clinic reporting yellowing skin and dark urine. What is the nurse's BEST action?",
  ["Tell the client to stop ART until the symptoms go away || Clients should never interrupt ART on their own",
   "*Report the findings to the provider promptly as urgent",
   "Reassure the client that this is an expected mild effect || Jaundice and dark urine are urgent to report",
   "Advise waiting until the next routine visit in 3 months || These are urgent adverse effects, not routine"],
  "Jaundice or dark urine is an URGENT ART adverse effect to report, like a blistering rash, hypersensitivity reaction or severe mood changes. Clients should never interrupt ART on their own.")

q("prep", "A 27-year-old HIV-negative woman who has receptive vaginal sex asks about PrEP (pre-exposure prophylaxis). Which listed option is NOT appropriate for her?",
  ["Daily oral emtricitabine/tenofovir disoproxil fumarate || This is a listed PrEP option without that restriction",
   "Cabotegravir injection every 2 months || This is a listed PrEP option",
   "*Daily oral emtricitabine/tenofovir alafenamide",
   "Lenacapavir injection every 6 months || This is a listed PrEP option"],
  "Emtricitabine/tenofovir alafenamide is the PrEP option NOT for receptive vaginal sex. Other listed options are daily emtricitabine/tenofovir disoproxil fumarate, cabotegravir every 2 months and lenacapavir every 6 months.")

q("prep", "A 30-year-old client is starting PrEP (pre-exposure prophylaxis). Which client statement needs MORE teaching?",
  ["'I need a negative HIV test before I start.' || Correct: negative HIV testing is confirmed first",
   "'My kidney function will be checked because I take tenofovir.' || Correct: kidney function is monitored with tenofovir",
   "'If I'm ever off PrEP and exposed, PEP must start within 72 hours.' || Correct: PEP starts as soon as possible, within 72 hours",
   "*'Since I'm on PrEP, I won't need condoms to prevent other STIs.'"],
  "PrEP is taken BEFORE possible exposure by HIV-negative people and does not prevent other STIs (sexually transmitted infections) or pregnancy. Confirm negative HIV testing, screen for STIs and monitor kidney function with tenofovir.")

q("preg", "A pregnant client with HIV (human immunodeficiency virus) has a viral load of 600 copies/mL near delivery. What birth plan does the slide support?",
  ["Scheduled cesarean birth || Cesarean is supported at 1,000 copies/mL or higher",
   "*Vaginal birth",
   "Stopping ART (antiretroviral therapy) before labor || ART continues through pregnancy, delivery and postpartum",
   "Routine invasive fetal monitoring || Invasive fetal monitoring should be avoided when possible"],
  "A viral load below 1,000 copies/mL supports vaginal birth; 1,000 or higher supports scheduled cesarean. Continue ART throughout and avoid invasive fetal monitoring when possible.")

q("preg", "A low-risk newborn was born to a mother with HIV (human immunodeficiency virus). Which actions are part of the infant's care? " + SATA,
  ["*Zidovudine for about 2 weeks",
   "*NAT (nucleic acid test) testing at the specified intervals",
   "Antibody testing to determine the infant's status || Maternal antibodies cross to the infant, so antibody tests are unreliable",
   "Starting prophylaxis only if the infant shows symptoms || Newborn prophylaxis starts soon after birth",
   "Three-drug treatment for every exposed newborn || Three-drug treatment is for high-risk newborns"],
  "Newborn prophylaxis starts soon after birth: low-risk newborns get zidovudine for about 2 weeks; high-risk newborns get three-drug treatment. Maternal antibodies make infant antibody tests unreliable, so NAT is used.")

q("needle", "Which practices help prevent occupational HIV (human immunodeficiency virus) exposure for nurses? " + SATA,
  ["*Using sharps containers",
   "*Using safety devices",
   "*Wearing gloves and eye protection",
   "Squeezing a needlestick site and soaking it in bleach || The site is washed with soap and water, then reported",
   "Waiting for symptoms before reporting an exposure || Exposures are reported immediately"],
  "Prevent injury with sharps containers, safety devices, gloves and eye protection. After a needlestick, wash with soap and water and report immediately; after a splash, rinse with water and report.")

q("needle", "A nurse had a needlestick from a client with HIV (human immunodeficiency virus) 4 hours ago. The nurse plans to be evaluated in 4 days if symptoms appear. Which response by the charge nurse is BEST?",
  ["'Waiting is fine as long as you don't develop any fever or flu-like symptoms.' || Waiting for symptoms delays PEP",
   "*'Get evaluated now; PEP should start within 72 hours.'",
   "'Soak the site in bleach and you won't need PEP.' || Wash with soap and water; bleach soaks are not recommended",
   "'Only eye splashes need a PEP evaluation.' || Needlesticks also need urgent PEP evaluation"],
  "After washing the site and reporting immediately, seek urgent evaluation for PEP (post-exposure prophylaxis) within 72 hours; earlier is better. PEP lasts 28 days with follow-up HIV testing.")

q("nursing", "A 48-year-old client with HIV (human immunodeficiency virus) tells the clinic nurse, 'I've had a fever of 101°F and a new cough for 3 days.' What is the nurse's BEST action?",
  ["Tell the client these are expected effects of ART || Fever over 100.4°F and persistent cough should be reported",
   "Advise rest and a recheck at the next routine visit || These findings need to be reported now",
   "Tell the client to hold ART until the fever resolves || ART should never be interrupted on one's own",
   "*Report the findings to the provider"],
  "Clients with HIV should report fever over 100.4°F, weight loss, persistent cough, new sores or lesions, confusion and medication reactions. Nurses report fever, cough, dyspnea, confusion and worsening immunosuppression.")
