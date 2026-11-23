T = "e5hiv"; SET = "20261123"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("what","A client asks if HIV medicine will cure the infection. Best response?",
 ["*'Treatment controls HIV, but the virus stays in the body for life.'","'Yes, after 6 months.' || No cure.","'Only if you start before symptoms.' || Still no cure.","'HIV goes away on its own.' || It persists."],
 "HIV is a retrovirus that attacks CD4 T cells.")
q("trans","Which exposure carries a risk of HIV transmission?",
 ["*Sharing needles with someone who has HIV","Sharing a fork || Saliva doesn't transmit.","Touching sweat on a gym mat || Sweat doesn't transmit.","Using the same toilet || Urine and feces don't transmit."],
 "Blood, semen, vaginal/rectal fluids and breast milk transmit HIV.")
q("trans","A new nursing assistant asks what extra precautions a client with HIV needs. What should the nurse say?",
 ["*'We use standard precautions, the same as for every patient.'","'Gown and mask for every visit.' || Not needed.","'Keep the door closed for airborne isolation.' || Not airborne.","'Avoid touching the client.' || Stigmatizing."],
 "HIV status alone doesn't require isolation.")
q("vl","A client's viral load is 150 copies/mL. Which statement is accurate?",
 ["*The virus is suppressed but may still be detectable","The client is undetectable || Threshold is lower, often 40–75.","Treatment is failing || Under 200 = suppressed.","The client has AIDS || Viral load doesn't define AIDS."],
 "Suppressed doesn't always mean undetectable.")
q("vl","Which lab shows how well the immune system is working in HIV?",
 ["*CD4 count","Viral load || Shows viral replication.","ESR || Inflammation.","Hemoglobin A1C || Glucose."],
 "Low CD4 = more immune compromise.")
q("stages","Three weeks after unprotected sex, a client has fever, rash, sore throat and swollen nodes. Which stage is likely?",
 ["*Stage 1: acute HIV","Stage 2: chronic HIV || Usually asymptomatic.","Stage 3: AIDS || CD4 under 200 or AIDS-defining illness.","No HIV; it's only a cold || Exposure history matters."],
 "Viral load is very high, so transmission risk is highest.")
q("stages","A client with HIV has a CD4 of 180 cells/mm³ and no symptoms. Which stage is this?",
 ["*Stage 3 (AIDS)","Stage 1 || Acute illness after exposure.","Stage 2 || CD4 under 200 defines AIDS.","No stage; they're well || CD4 defines it."],
 "AIDS = CD4 below 200 OR an AIDS-defining condition.")
q("cancer","Which finding in a client with HIV is an AIDS-defining cancer?",
 ["*Invasive cervical cancer","Basal cell carcinoma || Not AIDS-defining.","Actinic keratosis || Precancerous skin lesion.","Benign mole || Not cancer."],
 "Others: Kaposi sarcoma, non-Hodgkin and primary CNS lymphoma.")
q("oi","A client with a CD4 of 90 is started on trimethoprim-sulfamethoxazole. The client asks why. Best response?",
 ["*'It helps prevent Pneumocystis pneumonia when CD4 is under 200.'","'It cures HIV.' || It doesn't.","'It treats thrush.' || Not this drug's role.","'It raises your CD4.' || Not its role."],
 "PJP = dry cough, fever, dyspnea, hypoxia.")
q("oi","Which finding in a client with advanced HIV suggests CMV?",
 ["*New blurred vision","White mouth plaques || Candidiasis.","Red-purple skin lesions || Kaposi sarcoma.","Dry cough and hypoxia || PJP."],
 "CMV retinitis can cause vision loss.")
q("test","A client's 4th-generation antigen/antibody test is reactive. What comes next?",
 ["*An HIV-1/2 differentiation assay","A Western blot || No longer in the algorithm.","Nothing; diagnosis is final || Needs the next step.","A CD4 count only || Not diagnostic."],
 "NAT is used when results are unclear.")
q("monitor","A client started ART 3 weeks ago. When should the viral load be checked per the lecture?",
 ["*2–8 weeks after starting, then every 4–8 weeks until undetectable","Only once a year || Too rare.","Only if symptoms appear || Scheduled.","Never; CD4 is enough || Viral load shows response."],
 "Then every 3–4 months once undetectable.")
q("art","Two weeks after starting ART, a client reports tea-colored urine and yellow eyes. What should the nurse do?",
 ["*Report it immediately","Tell them it's expected and will pass || A red flag.","Have them stop ART on their own || Don't stop without guidance.","Recommend more fluids only || Report first."],
 "These suggest liver toxicity.")
q("art","A client on ART reports mild nausea and fatigue. Which response is best?",
 ["*'These may be manageable; let's talk with your provider, and don't stop your medicine.'","'Stop ART until you feel better.' || Never stop on your own.","'Go to the emergency department.' || Not an emergency.","'That means it isn't working.' || Not true."],
 "Report severe rash, jaundice, dark urine or new depression immediately.")
q("adhere","A client says, 'I keep forgetting my pills when I work double shifts.' Which intervention fits best?",
 ["*Set a phone alarm and use a pillbox","Refer to social work for copays || Not the barrier.","Stop ART on work days || Unsafe.","Tell the client to try harder || Not helpful."],
 "Link doses to a daily habit.")
q("adhere","Which nurse statement is the MOST therapeutic for a client who misses ART doses?",
 ["*'What gets in the way of taking your medicine?'","'You're being irresponsible.' || Judgmental.","'Why would you skip it?' || Blaming.","'You'll end up with AIDS.' || Threatening."],
 "Open-ended, nonjudgmental questions find barriers.")
q("prep","An HIV-negative client whose partner has HIV wants to prevent infection before any exposure. What is this called?",
 ["*Pre-exposure prophylaxis (PrEP)","Post-exposure prophylaxis (PEP) || After exposure.","Antiretroviral therapy (ART) || Treatment for HIV.","U = U || Describes the partner on effective ART."],
 "PrEP doesn't prevent other STIs.")
q("prep","A client had a condom break with a partner of unknown HIV status 30 hours ago. What should the nurse explain?",
 ["*'PEP should start as soon as possible, no later than 72 hours, and continue for 28 days.'","'It's too late for PEP.' || Within 72 hours.","'Wait 3 months and test.' || Start PEP now.","'Start PrEP next month.' || PEP is for after exposure."],
 "Follow-up HIV testing is required.")
q("preg","A pregnant client with HIV has a viral load of 600 copies/mL near delivery. What does the lecture support?",
 ["*Vaginal birth is favored","Scheduled cesarean is required || 1,000 or more.","Stop ART before delivery || Continue ART.","Invasive fetal monitoring || Avoid when possible."],
 "Continue ART through pregnancy, delivery and postpartum.")
q("preg","Which test is used for a newborn of a mother with HIV?",
 ["*Infant nucleic acid test (NAT)","Antibody test at birth || Maternal antibodies interfere.","CD4 count only || Not diagnostic.","Home antibody test || Not for infants."],
 "Maternal antibodies can persist up to 18 months.")
q("needle","A nurse is stuck by a used needle. The source client's lab results won't be back for hours. What should happen?",
 ["*Begin PEP evaluation now; don't wait for the results","Wait for the results before acting || Don't delay PEP.","Wait 72 hours to see if symptoms appear || Too late.","Only document the incident || Evaluation is urgent."],
 "Ideally within 24 hours, no later than 72.")
q("nursing","A client with HIV has a cat. Which teaching is appropriate?",
 ["*'Ask someone else to clean the litter box.'","'Give the cat away.' || Not required.","'Clean the box with bare hands.' || Unsafe.","'Pets have no risk.' || Litter carries risk."],
 "Also avoid undercooked food and sick contacts.")
q("needle","Which actions prevent occupational HIV exposure? "+SATA,
 ["*Wear gloves and eye protection when splashes are possible","*Use sharps safety devices","*Dispose of needles in a sharps container right away","Recap needles with two hands || Raises needlestick risk."],
 "Standard precautions for every patient.")
