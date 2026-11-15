# Week 13.3 Dysfunction in Immunity: RA & SLE — lesson plan, notes, assigned textbook (Nursing: A Concept-Based
# Approach to Learning Vol 1, Exemplars 8.C and 8.D), pre-class quiz points. No PowerPoint was supplied.
EXAM = "e5"
T = "e5slera"
CONCEPTS = {
 "big":"RA vs SLE: the big picture",
 "rapatho":"RA pathophysiology: synovitis & pannus",
 "rarisk":"RA risk factors & populations",
 "ramani":"RA joint findings & deformities",
 "raextra":"RA systemic (extra-articular) findings",
 "radx":"RA diagnostics",
 "ranpharm":"RA comfort: heat, cold, rest & exercise",
 "rameds":"RA meds: NSAIDs, steroids, methotrexate",
 "biologic":"Biologics & JAK inhibitors",
 "ranurse":"RA nursing priorities",
 "slepatho":"SLE pathophysiology & course",
 "sleskin":"SLE skin findings & photosensitivity",
 "sleorgan":"SLE organ involvement",
 "slerenal":"Lupus nephritis: the red flag",
 "sledx":"SLE diagnostics",
 "slemeds":"SLE medications",
 "slenurse":"SLE nursing & flare prevention",
}
HI = ["radx","rameds","ranpharm","sleskin","slerenal","sledx","slemeds","slenurse","rapatho"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- big picture ----------
q("big","Which statement best compares RA and SLE?",
 ["*RA mainly attacks the synovial joints; SLE is a multisystem autoantibody disease","Both are wear-and-tear joint diseases || Both are autoimmune.","RA mainly damages the kidneys; SLE mainly damages joints || Reversed emphasis.","SLE is an infection; RA is autoimmune || Both are autoimmune."],
 "RA = synovium; SLE = immune complexes in skin, joints, kidneys, blood, heart, lungs, nervous system.")
q("big","Which disease course do RA and SLE share?",
 ["*Chronic, with flares and remissions","Acute and fully curable || They're chronic.","Always fatal within a year || Not true.","Only affects children || All ages."],
 "Both are chronic systemic autoimmune diseases.")

# ---------- RA patho ----------
q("rapatho","What does RA primarily target?",
 ["*The synovial lining of the joints","Cartilage from wear and tear || That's osteoarthritis.","The kidneys || SLE.","The skin || Not primarily."],
 "Pre-class quiz point.")
q("rapatho","What is pannus?",
 ["*Thickened, inflamed synovial tissue that invades and erodes cartilage and bone","A butterfly rash || SLE.","A bone spur || OA.","A rheumatoid nodule under the skin || Different finding."],
 "Pannus leads to scar tissue that can immobilize the joint.")
q("rapatho","How does RA differ from osteoarthritis?",
 ["*RA is inflammatory and autoimmune, often symmetric with systemic signs; OA is degenerative wear and tear","They're the same disease || Different causes.","OA is autoimmune || RA is.","RA never affects the hands || It often does."],
 "OA is the most common arthritis in older adults; RA is the most common autoimmune arthritis.")

# ---------- RA risk ----------
q("rarisk","Which are risk factors for RA? "+SATA,
 ["*Family history/genetics","*Female sex","*Smoking","*Certain environmental exposures","High-purine diet || Gout."],
 "Not every risk can be prevented.")
q("rarisk","What often happens to RA during pregnancy?",
 ["*Many clients go into remission, then relapse after delivery","It always worsens || Often improves.","It's cured permanently || Relapse often follows.","It turns into SLE || No."],
 "Per the textbook; the reasons aren't fully known.")
q("rarisk","Why can RA be hard to diagnose in an older adult?",
 ["*It can be difficult to tell apart from osteoarthritis","Older adults can't get RA || They can.","RA has no symptoms in older adults || Symptoms are similar.","Labs are never abnormal || Not the reason."],
 "Onset and findings are similar in older and younger clients.")

# ---------- RA joints ----------
q("ramani","Which joint pattern is typical of RA?",
 ["*Symmetric involvement of the MCP and PIP joints of the hands, plus wrists and feet","One knee only || Not typical.","Distal finger joints with bony nodes || More typical of OA.","Only the big toe || Gout."],
 "Larger joints can be involved later.")
q("ramani","Which findings fit RA joints? "+SATA,
 ["*Pain, warmth and swelling","*Morning stiffness","*Reduced range of motion and grip","Crepitus from bone on bone only || More OA."],
 "Inflamed joints look red, warm, swollen and painful.")
q("ramani","Which deformities can develop in later RA? "+SATA,
 ["*Ulnar deviation","*Swan-neck deformity","*Boutonnière deformity","Heberden's nodes || OA."],
 "Joint destruction can limit self-care and mobility.")

# ---------- RA systemic ----------
q("raextra","Which systemic findings occur with RA? "+SATA,
 ["*Fatigue and low-grade fever","*Weight loss","*Rheumatoid nodules","*Anemia","*Dry eyes and mouth","Butterfly rash || SLE."],
 "Pulmonary and cardiovascular complications can also occur.")
q("raextra","A client with RA has dry eyes and a dry mouth. Which associated condition does this suggest?",
 ["*Sjögren syndrome","Felty syndrome || Splenomegaly, neutropenia, anemia.","Lupus nephritis || Kidneys.","Raynaud phenomenon || Fingers."],
 "Sjögren syndrome is an extra-articular RA manifestation.")
q("raextra","Which findings make up Felty syndrome in RA?",
 ["*Splenomegaly, neutropenia and anemia","Dry eyes and mouth || Sjögren.","Butterfly rash and proteinuria || SLE.","Ulnar deviation and nodules || Joint findings."],
 "Also weight loss and low-grade fever.")
q("raextra","Why do clients with RA have higher heart disease risk?",
 ["*Chronic inflammation plus side effects of drugs like methotrexate and steroids","RA directly blocks coronary arteries with pannus || Not the mechanism.","They exercise too much || Not the reason.","There's no added risk || There is."],
 "Monitor for cardiovascular symptoms.")

# ---------- RA dx ----------
q("radx","Which antibody is MOST specific for RA?",
 ["*Anti-CCP","Rheumatoid factor (RF) || May be positive but not specific.","ANA || SLE screening.","Anti-dsDNA || SLE."],
 "Pre-class quiz point.")
q("radx","Which statement about RA diagnosis is correct?",
 ["*No single test confirms RA; history, exam, joint pattern, markers, antibodies and imaging are combined","A positive RF alone confirms RA || RF isn't specific.","An x-ray alone confirms RA || Not alone.","ANA confirms RA || ANA is for SLE."],
 "ESR and CRP show inflammation and track activity.")
q("radx","Which labs help assess RA? "+SATA,
 ["*Anti-CCP and RF","*ESR and CRP","*CBC for anemia","Anti-dsDNA || SLE.","C3/C4 complement || SLE activity."],
 "Imaging can show joint changes.")

# ---------- RA comfort ----------
q("ranpharm","A client's RA joints are acutely swollen, hot and painful. Which comfort measure is a priority?",
 ["*Cold application","Moist heat via a hot tub soak || Heat is for stiffness, not acute inflammation.","Vigorous exercise || Avoid high-impact activity during a flare.","Permanent immobilization || Not recommended."],
 "Pre-class quiz point: cold for acute swollen, painful joints.")
q("ranpharm","A client with RA has morning stiffness without an acute flare. What helps most?",
 ["*Moist heat, such as a warm tub bath","Ice packs every hour || Cold is for acute inflammation.","Complete bed rest || Not recommended.","Avoid all movement || ROM is encouraged."],
 "Heat relieves stiffness.")
q("ranpharm","Which nonpharmacologic measures support RA? "+SATA,
 ["*Low-impact exercise and range of motion when tolerated","*Rest during active inflammation","*Splints and assistive devices","*Physical and occupational therapy","High-impact running during a flare || Avoid."],
 "Regular activity can also improve sleep and fatigue.")

# ---------- RA meds ----------
q("rameds","Which drug is a common FIRST-line disease-modifying treatment for RA?",
 ["*Methotrexate","Ibuprofen || Relieves symptoms but doesn't slow disease.","Prednisone || Used for flares or as a bridge.","Hydroxychloroquine || More emphasized for SLE."],
 "Monitor CBC, liver function and infection.")
q("rameds","Which statement about NSAIDs in RA is correct?",
 ["*They relieve pain and inflammation but don't prevent disease progression","They stop joint destruction || DMARDs slow progression.","They have no side effects || GI bleeding, kidney and heart risks.","They're the same as DMARDs || Different classes."],
 "Use as ordered.")
q("rameds","A client has taken prednisone for RA for 2 years. Which teaching is correct? "+SATA,
 ["*Don't stop it abruptly","*Long-term use can cause osteoporosis","*Watch for infection, high glucose and high BP","Stop it once joints feel better || Must be tapered."],
 "Pre-class quiz point: long-term steroids cause osteoporosis.")
q("rameds","Why may corticosteroids be used early in RA?",
 ["*As a bridge for flares while longer-term DMARDs take effect","As a cure || Not curative.","Because they protect bones || They cause bone loss.","To replace methotrexate permanently || Not the role."],
 "Intra-articular steroid injections can give local relief.")

# ---------- biologics ----------
q("biologic","How do adalimumab and infliximab treat RA?",
 ["*They bind tumor necrosis factor (TNF), which drives joint destruction","They block COX enzymes || NSAIDs.","They kill bacteria || Not antibiotics.","They replace synovial fluid || Not the action."],
 "Other biologics block interleukin-6; JAK inhibitors block the JAK enzyme.")
q("biologic","What is the priority teaching for a client starting a biologic or JAK inhibitor?",
 ["*Report fever or other signs of infection","Expect weight loss || Not the priority.","Take it with grapefruit juice || Not the teaching.","Skip lab monitoring || Monitoring is needed."],
 "These drugs suppress the immune system.")
q("biologic","Which drugs are DMARDs listed for RA? "+SATA,
 ["*Methotrexate","*Sulfasalazine","*Leflunomide","*Etanercept","Ibuprofen || NSAID, not a DMARD."],
 "DMARDs relieve symptoms and slow disease progression.")

# ---------- RA nursing ----------
q("ranurse","Which nursing diagnosis is highly relevant for a client with RA?",
 ["*Chronic pain","Risk for aspiration || Not the focus.","Impaired urinary elimination || Not the focus.","Hyperthermia from heat stroke || Not related."],
 "Pre-class quiz point.")
q("ranurse","Which assessments are priorities for a client with RA? "+SATA,
 ["*Pain, stiffness and swelling","*Range of motion and mobility","*Ability to perform ADLs","*Emotional impact and medication tolerance","Visual acuity only || Not the focus."],
 "Coordinate physical and occupational therapy.")
q("ranurse","Which teaching protects joint function in RA? "+SATA,
 ["*Energy conservation","*Joint protection","*Adaptive equipment","*Low-impact movement","Carrying heavy loads with the fingers || Strains joints."],
 "Monitor for infection, medication toxicity and progressive disability.")

# ---------- SLE patho ----------
q("slepatho","What happens in systemic lupus erythematosus?",
 ["*Loss of self-tolerance creates autoantibodies; immune complexes deposit in tissues and cause inflammation","Bacteria infect the joints || Not infectious.","Cartilage wears down with age || OA.","Uric acid crystals form in joints || Gout."],
 "Damage can occur in the kidneys, skin, joints and blood vessels.")
q("slepatho","Which statement about the SLE course is correct?",
 ["*Flares and remissions; severity ranges from skin and joint symptoms to life-threatening organ disease","It always stays mild || Can be severe.","It affects only the skin || Multisystem.","It never flares || Flares are common."],
 "Monitor for organ involvement.")

# ---------- SLE skin ----------
q("sleskin","Which rash is characteristic of SLE?",
 ["*A red malar (butterfly) rash across the cheeks and bridge of the nose","A dermatomal stripe of vesicles || Shingles.","A rash that starts at the hairline and moves down || Measles.","Rough, scaly patches || Actinic keratosis."],
 "Pre-class quiz point.")
q("sleskin","A client with SLE plans a beach vacation. What should the nurse teach?",
 ["*Photosensitivity is common; avoid excess sun and use sun protection to prevent flares","More sun will help the rash || UV can trigger flares.","Tanning beds are safe || UV exposure.","Sun has no effect on lupus || It does."],
 "Pre-class quiz point: increased sun exposure isn't appropriate advice.")
q("sleskin","Which skin and mucosal findings occur with SLE? "+SATA,
 ["*Malar rash","*Photosensitivity","*Discoid lesions","*Alopecia","*Oral or nasal ulcers","Koplik spots || Measles."],
 "Offer gentle skin care and address body-image concerns.")

# ---------- SLE organs ----------
q("sleorgan","Which cardiopulmonary findings can occur with SLE? "+SATA,
 ["*Pleuritis or pleural effusion","*Pericarditis","*Raynaud phenomenon","*Vasculitis","Bronchiolitis in infants || RSV."],
 "Venous or arterial thrombosis may also develop.")
q("sleorgan","Which blood and nervous system findings can occur with SLE? "+SATA,
 ["*Anemia, leukopenia and thrombocytopenia","*Headache and seizures","*Cognitive or mood changes","Polycythemia || Not listed."],
 "Assess for new neurologic symptoms.")
q("sleorgan","How does SLE joint involvement compare with RA?",
 ["*SLE causes arthralgia and arthritis, but not the same destructive pattern as RA","SLE causes more erosive damage than RA || Less destructive.","SLE never affects joints || It often does.","They're identical || Different patterns."],
 "SLE's major concern is organ damage, especially the kidneys.")

# ---------- renal ----------
q("slerenal","A client with SLE has BP 170/100 and proteinuria. What is the nurse's priority?",
 ["*Report immediately: possible lupus nephritis needing prompt evaluation","Recheck in a week || Needs immediate action.","Encourage more sun exposure || Not appropriate.","Apply cold to the joints || Not the priority."],
 "Pre-class quiz point.")
q("slerenal","Which findings suggest lupus nephritis? "+SATA,
 ["*Proteinuria","*Hematuria","*Edema","*Hypertension","*Rising creatinine","Increased urine concentration only || Not the finding."],
 "Lupus nephritis can progress to kidney failure needing dialysis or transplant.")
q("slerenal","During an SLE flare, which monitoring is the priority?",
 ["*Renal function and vital signs","Visual acuity only || Not the priority.","Grip strength only || More RA.","Height || Not relevant."],
 "Pre-class quiz point.")

# ---------- SLE dx ----------
q("sledx","Which statement about ANA in SLE is correct?",
 ["*Often positive but not diagnostic by itself","It confirms SLE every time || Not diagnostic alone.","It's specific for RA || Not RA.","It's always negative in SLE || Usually positive."],
 "Anti-dsDNA is more specific for SLE.")
q("sledx","Which antibody is MORE specific for SLE and helps assess activity?",
 ["*Anti-dsDNA","Anti-CCP || RA.","Rheumatoid factor || RA, not specific.","ASO titer || Strep."],
 "Complement (C3/C4) may drop during active disease.")
q("sledx","Which tests check for kidney involvement in SLE? "+SATA,
 ["*Urinalysis and urine protein","*Serum creatinine","*BUN","Anti-CCP || RA antibody."],
 "CBC checks for blood-cell abnormalities.")
q("sledx","What happens to complement levels (C3/C4) during active SLE?",
 ["*They may decrease","They always rise || They tend to drop.","They don't change || Trends help monitor.","They become zero || Not the pattern."],
 "Complement trends help monitor inflammation.")

# ---------- SLE meds ----------
q("slemeds","A client on hydroxychloroquine for SLE should be taught to:",
 ["*Have regular eye exams because it can cause vision changes","Expect red urine || Not this drug.","Stop it during flares || Don't stop on your own.","Avoid all fluids || Not the teaching."],
 "The textbook notes retinal changes and vision exams about every 6 months; it reduces flare frequency.")
q("slemeds","What is belimumab?",
 ["*The first FDA-approved drug specifically designed for SLE; it decreases B-lymphocyte activity","An NSAID for RA || Not an NSAID.","An antimalarial || That's hydroxychloroquine.","A vaccine || Not a vaccine."],
 "Given IV or SQ to adults and children 5 and older with active SLE.")
q("slemeds","Which medications are used for SLE? "+SATA,
 ["*NSAIDs for mild joint symptoms","*Hydroxychloroquine","*Corticosteroids for active or organ-threatening disease","*Immunosuppressants for moderate-to-severe disease","Oseltamivir || Influenza."],
 "Monitor CBC, kidney and liver function, and infection.")
q("slemeds","Why might a client with SLE be advised to avoid estrogen-containing oral contraceptives?",
 ["*Estrogen can trigger an acute SLE episode","They cause RA || Not the reason.","They raise ANA to zero || Not the reason.","They cause photosensitivity only || Not the reason."],
 "Per the textbook.")

# ---------- SLE nursing ----------
q("slenurse","Which teaching helps prevent SLE flares? "+SATA,
 ["*Sun protection","*Adequate rest and activity pacing","*Stress management","*Treatment adherence","Stopping medications when feeling well || Don't change therapy on your own."],
 "Keep lab follow-ups.")
q("slenurse","Which monitoring is important for a client with SLE? "+SATA,
 ["*Blood pressure, weight and edema","*I&O and urine findings","*Temperature and infection signs","*New neurologic changes","Peak flow only || Not the focus."],
 "Immunosuppressive drugs raise infection risk.")
q("slenurse","A client with SLE on immunosuppressants has a fever. What should the nurse do?",
 ["*Report it promptly; infection risk is higher on immunosuppression","Encourage sun exposure || Not appropriate.","Ignore a low fever || Report it.","Double the steroid dose || Never self-adjust."],
 "Reinforce prescribed infection precautions.")
