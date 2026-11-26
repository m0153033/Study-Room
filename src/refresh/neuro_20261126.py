T = "neuro"; SET = "20261126"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("nt", "A nursing student is sorting neurotransmitters into 'gas pedal' and 'brake pedal' groups. Which neurotransmitters belong in the excitatory group? " + SATA,
 ["*Norepinephrine",
  "Glycine || Glycine is inhibitory; it calms the nervous system.",
  "*Dopamine",
  "GABA || GABA is the brain's brake pedal (inhibitory).",
  "*Histamine"],
 "Excitatory neurotransmitters include glutamate, epinephrine, norepinephrine, dopamine, acetylcholine and histamine. GABA, glycine and serotonin are inhibitory.")

q("act", "A nurse is reviewing how several neurologic drugs work. Which drug is paired with the correct drug type?",
 ["Pramipexole: enzyme inhibitor || Pramipexole is an agonist that mimics dopamine.",
  "Selegiline: dopamine receptor agonist || Selegiline is an enzyme inhibitor that blocks MAO-B.",
  "*Memantine: antagonist that blocks glutamate at NMDA receptors",
  "Donepezil: glutamate receptor antagonist || Donepezil blocks the enzyme acetylcholinesterase."],
 "Agonists mimic and antagonists block. Memantine blocks glutamate at NMDA receptors; donepezil and selegiline block enzymes (acetylcholinesterase and MAO-B).")

q("baclofen", "A 45-year-old teacher with MS takes baclofen for spasms and reports having hard, infrequent stools. Which advice by the nurse is appropriate?",
 ["'Take each dose on an empty stomach.' || Baclofen is given with food.",
  "*'Increase the fluids and fiber in your diet.'",
  "'Stop the baclofen today until this resolves.' || Baclofen must be tapered, never stopped suddenly.",
  "'Constipation means the dose is too low.' || Constipation is a known side effect, not a sign of low dosing."],
 "Constipation is a side effect of baclofen; give it with food and increase fluids and fiber. Baclofen is tapered over 1-2 weeks, not stopped suddenly.")

q("dantrolene", "A student asks why dantrolene, rather than baclofen, is used for malignant hyperthermia. Which explanation by the nurse is accurate?",
 ["'Baclofen stops calcium release inside the muscle fiber.' || Baclofen acts like GABA in the brain and spinal cord.",
  "'Malignant hyperthermia is a brain infection that needs a central drug.' || It is an inherited muscle calcium problem.",
  "'Dantrolene raises GABA throughout the spinal cord.' || Dantrolene acts peripherally in the muscle.",
  "*'The problem is calcium in the muscle, and dantrolene stops that release.'"],
 "Malignant hyperthermia is an inherited reaction with too much calcium inside skeletal muscle fibers. Peripherally acting dantrolene stops calcium release in the muscle; baclofen acts centrally like GABA.")

q("szpatho", "Based on the lecture's model of seizures, which change in the brain would make a seizure MORE likely?",
 ["*More glutamate activity with less GABA",
  "More GABA activity in the brain || GABA is the brake pedal and calms neurons.",
  "Blocking sodium from entering the cell || Blocking sodium entry stops the signal.",
  "Lowering the amount of glutamate || Lowering glutamate is a seizure treatment."],
 "Seizures come from too much glutamate, too little GABA and too much sodium entering the cell. Seizure drugs lower glutamate, raise GABA or block sodium.")

q("phenytoin", "A 19-year-old college student is starting phenytoin for seizures and takes birth control pills. Which teaching by the nurse is a priority?",
 ["'Phenytoin makes your pills work even better.' || Phenytoin can make birth control pills less effective.",
  "'Stop phenytoin if you plan to change methods.' || Phenytoin should never be stopped suddenly.",
  "*'Phenytoin can make your pills less effective; talk with your provider.'",
  "'These two drugs have no effect on each other.' || Phenytoin can reduce the effect of birth control pills."],
 "Phenytoin can make birth control pills less effective. It should never be stopped suddenly, and any rash should be reported.")

q("phenytoin", "A nurse in the emergency department is preparing to give IV phenytoin to a 62-year-old client. Which actions are appropriate? " + SATA,
 ["*Inject the medication slowly",
  "Flush the line with D5W first || Phenytoin is incompatible with dextrose.",
  "*Monitor the heart rhythm during the infusion",
  "*Watch the BP for a drop during the infusion",
  "Push it rapidly to stop the seizure faster || IV phenytoin is injected slowly."],
 "IV phenytoin is injected slowly with heart rhythm and BP monitoring for dysrhythmias and low BP. It is incompatible with dextrose.")

q("carbamaz", "A 33-year-old accountant starting carbamazepine says, 'I drink a glass of grapefruit juice every morning.' Which response by the nurse is best?",
 ["'Grapefruit juice lowers the drug level, so drink extra.' || Grapefruit juice raises the drug level.",
  "'Take each dose with the juice to help absorption.' || Grapefruit juice should be avoided.",
  "*'Avoid grapefruit juice; it can raise the drug level.'",
  "'Juice is fine as long as you use sunscreen.' || Sunscreen does not change the grapefruit interaction."],
 "Clients on carbamazepine should avoid grapefruit juice because it raises the drug level. Other teaching includes sunscreen, backup birth control and swallowing extended-release tablets whole.")

q("carbamaz", "A 58-year-old client has taken carbamazepine for 3 months. Which findings should the client be taught to report? " + SATA,
 ["*Sore throat with a fever",
  "Swollen, overgrown gums || Gum overgrowth is the signature problem of phenytoin.",
  "*Unusual bruising",
  "Confusion and headache from low sodium || Low sodium is the signature problem of oxcarbazepine.",
  "*A new skin rash"],
 "Carbamazepine can cause bone marrow suppression, so fever, sore throat and bruising are reported and the CBC and WBC are monitored. A rash is reported because of Stevens-Johnson risk.")

q("valproic", "A nurse reviews the history of a 41-year-old client newly prescribed valproic acid. Which finding should the nurse report to the provider before the first dose?",
 ["Asian descent without HLA-B*1502 testing || HLA-B*1502 testing applies to carbamazepine.",
  "*A history of liver disease",
  "Daily use of a diuretic || Diuretics raise the low-sodium risk with oxcarbazepine.",
  "A history of gum disease || Gum overgrowth is a phenytoin concern."],
 "Valproic acid is contraindicated in liver disease and pregnancy. Liver toxicity can be fatal, so liver function tests are monitored.")

q("valproic", "A nurse has taught a 36-year-old warehouse worker about valproic acid. Which client statements show understanding? " + SATA,
 ["*'I'll take it with food to avoid an upset stomach.'",
  "'This is the safest seizure drug if I get pregnant.' || It can cause neural tube defects and is contraindicated in pregnancy.",
  "*'I'll report yellow skin or eyes right away.'",
  "'I'll need dental visits for gum overgrowth.' || Gum overgrowth is a phenytoin side effect.",
  "*'Belly pain with vomiting needs to be reported.'"],
 "Valproic acid is given with food. Report yellow skin (liver damage), belly pain with nausea and vomiting (pancreatitis), easy bruising and confusion (high ammonia).")

q("oxcarb", "Which pair of labs does the nurse monitor for a client taking oxcarbazepine?",
 ["Ammonia and amylase || These are monitored for valproic acid.",
  "Drug level kept at 10-20 mcg/mL || This is the phenytoin therapeutic range.",
  "*Sodium and WBC count",
  "Liver function tests only || Liver tests are the key lab for dantrolene."],
 "Oxcarbazepine can cause low sodium, especially with diuretics; monitor sodium and WBC count.")

q("local", "A provider plans to use lidocaine with epinephrine to repair four different lacerations. For which site should the nurse question this plan?",
 ["A cut on the forearm || The forearm is not an end-artery site.",
  "A cut on the thigh || The thigh is not an end-artery site.",
  "A cut on the upper back || The back is not an end-artery site.",
  "*A cut on the tip of a toe"],
 "Lidocaine with epinephrine is not used on fingers, toes or the nose because epinephrine squeezes the vessels and can cut off blood flow (gangrene) at these end-artery sites.")

q("general", "A nurse is assisting with conscious sedation using midazolam for a 50-year-old client. Which actions are appropriate? " + SATA,
 ["*Push the midazolam slowly",
  "Give the next dose right away if the client is awake || Wait 2 minutes before another dose.",
  "*Wait 2 minutes before giving another dose",
  "*Keep airway and breathing the priority assessment",
  "Stop monitoring once the client looks calm || Sedatives can cause respiratory depression."],
 "Midazolam is pushed slowly, waiting 2 minutes before another dose. Airway and breathing are the priority because these sedatives can cause respiratory depression.")

q("stim", "A 9-year-old has taken methylphenidate for ADHD for 6 months. Which assessments should the nurse include at each visit? " + SATA,
 ["*Height and weight",
  "*Blood pressure",
  "Gums for overgrowth || Gum overgrowth is a phenytoin side effect.",
  "*Heart rate",
  "Serum ammonia level || Ammonia is monitored for valproic acid."],
 "CNS stimulants can raise BP and heart rate and cause poor appetite and weight loss, so height and weight are monitored in children.")

q("stim", "A nurse teaches the parent of a 10-year-old who takes methylphenidate. Which statement by the parent indicates a need for further teaching?",
 ["'I'll give his first dose in the morning.' || Stimulants are taken in the morning.",
  "*'I'll give his afternoon dose with dinner.'",
  "'I'll cut back on his soda and other caffeine.' || Caffeine should be avoided.",
  "'If we stop it, his provider will taper it.' || Stimulants are tapered, not stopped suddenly."],
 "A child should take the last daily dose of methylphenidate by 4 p.m. to prevent trouble sleeping. Take it in the morning, avoid caffeine and taper when stopping.")

q("modafinil", "A 44-year-old client with sleep apnea is starting modafinil. Which teaching by the nurse is correct?",
 ["'Take it at bedtime so it works overnight.' || It promotes wakefulness and is taken in the morning.",
  "*'Take it in the morning.'",
  "'It has a higher misuse risk than methylphenidate.' || Modafinil has low misuse potential.",
  "'It works by increasing GABA in the brain.' || It blocks norepinephrine reuptake."],
 "For narcolepsy and sleep apnea, modafinil is taken in the morning. It promotes wakefulness by blocking norepinephrine reuptake and has low misuse potential.")

q("pdpatho", "A nursing student asks why levodopa works for Parkinson's disease when dopamine itself is not given. Which explanation by the nurse is accurate?",
 ["'Levodopa blocks MAO-B so dopamine lasts longer.' || That describes selegiline.",
  "'Levodopa raises acetylcholine to restore balance.' || Parkinson's already has more acetylcholine than dopamine.",
  "'Levodopa mimics dopamine directly at its receptors.' || That describes pramipexole.",
  "*'Levodopa crosses the blood-brain barrier and becomes dopamine.'"],
 "Dopamine can't cross the blood-brain barrier. Levodopa crosses and is converted to dopamine in the brain; carbidopa keeps it from converting before it gets there.")

q("levodopa", "A 72-year-old retired carpenter taking levodopa/carbidopa reports feeling lightheaded when getting out of bed. Which teaching is the priority?",
 ["'Take your doses with a high-protein meal.' || High-protein meals reduce absorption.",
  "'Add a vitamin B6 supplement each day.' || Vitamin B6 is not taken with this drug.",
  "*'Rise slowly to lower your risk of falling.'",
  "'This means you should stop the drug.' || Rising slowly manages this; stopping is not indicated."],
 "Levodopa/carbidopa can cause orthostatic hypotension, which raises fall risk, so clients rise slowly. Avoid high-protein meals around doses.")

q("levodopa", "Before a client starts levodopa/carbidopa, which findings in the history should the nurse report to the provider? " + SATA,
 ["*Angle-closure glaucoma",
  "Takes acetaminophen for knee pain || Acetaminophen is not a listed interaction.",
  "*A past melanoma",
  "*Took an MAOI antidepressant last week",
  "Prefers to take pills with water || This is not a contraindication."],
 "An MAOI within 2 weeks can cause hypertensive crisis. Levodopa/carbidopa is also contraindicated with angle-closure glaucoma and a history of melanoma.")

q("pramipexole", "A 55-year-old client taking pramipexole for restless legs syndrome asks how to stop it if it is no longer needed. Which response by the nurse is correct?",
 ["*'It should be tapered slowly over about a week.'",
  "'You can stop it the same day you decide.' || Pramipexole is tapered slowly.",
  "'Double the dose for 2 days, then stop.' || Raising the dose is not part of stopping.",
  "'Stop it as soon as your legs feel calm.' || It is tapered slowly over a week."],
 "Pramipexole is tapered slowly over a week when stopping. For restless legs it is taken 2-3 hours before bedtime.")

q("selegiline", "A client taking levodopa/carbidopa for Parkinson's disease is also started on selegiline. Which benefit should the nurse explain?",
 ["'It turns protein into dopamine in the brain.' || Selegiline blocks dopamine breakdown.",
  "*'Dopamine lasts longer, so the levodopa dose may be lowered.'",
  "'It raises acetylcholine to balance dopamine.' || Parkinson's already has excess acetylcholine.",
  "'It cures the loss of dopamine neurons.' || It protects dopamine but does not cure the disease."],
 "Selegiline blocks MAO-B so dopamine isn't broken down, which lets the levodopa dose be lowered.")

q("adpatho", "The daughter of a 79-year-old client with Alzheimer's disease asks, 'Will her disease settle down the way my friend's MS does?' Which response by the nurse is accurate?",
 ["'Yes, Alzheimer's has flare-ups and remissions too.' || Flares and remissions describe MS.",
  "'It is caused by losing dopamine neurons.' || That describes Parkinson's disease.",
  "*'Alzheimer's is progressive; treatment aims to manage symptoms.'",
  "'Memantine will reverse the plaques over time.' || No drug reverses the disease."],
 "Alzheimer's disease is progressive and ultimately fatal, with plaques, tangles and brain shrinkage. The goal of medication is managing symptoms.")

q("donepezil", "A 76-year-old client who started donepezil 2 weeks ago fainted while walking to the bathroom. Which drug effect should the nurse suspect?",
 ["A sleep attack || Sleep attacks are a pramipexole side effect.",
  "Low sodium || Low sodium is linked to oxcarbazepine.",
  "*A slow heart rate",
  "Malignant hyperthermia || This is an inherited muscle reaction during surgery."],
 "Donepezil can slow the heart (bradycardia). The nurse checks the heart rate before giving it and teaches clients to report fainting.")

q("memantine", "Before memantine is started for a client with moderate Alzheimer's disease, which history finding should the nurse report?",
 ["Prefers to take pills without food || Memantine can be taken with or without food.",
  "*Kidney failure",
  "Eats aged cheese most days || Tyramine foods are a selegiline concern.",
  "Eats high-protein meals || Protein affects levodopa absorption."],
 "Memantine is contraindicated in kidney failure. It can be taken with or without food.")

q("ms", "A 30-year-old graphic designer is being evaluated for MS. Which findings would the nurse expect? " + SATA,
 ["*Muscle weakness",
  "*Numbness",
  "Swollen, overgrown gums || Gum overgrowth is a phenytoin side effect.",
  "*Vision problems",
  "*Urinary incontinence"],
 "In MS, white blood cells destroy CNS myelin, with flare-ups and remissions. Signs include weakness, numbness, vision problems, incontinence and cognitive changes.")

q("ms", "A client with MS who uses interferon beta has developed yellow skin, a poor appetite and belly tenderness. What should the nurse suspect?",
 ["Expected flu-like effects of the drug || Flu-like effects are aches and fever after injections.",
  "*Liver damage from the interferon",
  "Low platelets causing bleeding || Low platelets present as bleeding or bruising.",
  "High ammonia from the injections || High ammonia is linked to valproic acid."],
 "Interferon beta can damage the liver (yellow skin, poor appetite, belly tenderness), so liver function tests are monitored along with the CBC.")

q("migraine", "A 38-year-old bartender used SubQ sumatriptan for a migraine 1 hour ago and still has pain. Which statement by the nurse is correct?",
 ["'SubQ sumatriptan can't be repeated.' || SubQ may be repeated once after 1 hour.",
  "'Use another triptan now instead.' || No other triptan within 24 hours.",
  "'Repeat it every 30 minutes until relief.' || SubQ may be repeated only once.",
  "*'You may repeat the SubQ dose once now.'"],
 "SubQ sumatriptan may be repeated once after 1 hour. Another triptan should not be taken within 24 hours.")

q("migraine", "A nurse teaches a 27-year-old client newly prescribed sumatriptan. Which statement by the client shows understanding?",
 ["'I'll take it every morning to prevent migraines.' || Sumatriptan stops a migraine that has started.",
  "'Jaw tightness after a dose is normal to ignore.' || Chest, jaw or throat tightness must be reported.",
  "*'I'll take it once a migraine has started.'",
  "'It works by widening the swollen vessels.' || It constricts the inflamed vessels."],
 "Sumatriptan stops a migraine or cluster headache that has started by activating serotonin receptors to constrict vessels. Valproic acid can prevent migraines.")
