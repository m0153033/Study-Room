T = "e3w71"; SET = "20261125"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("nt", "A nursing student is sorting neurotransmitters before a pharmacology exam. Which neurotransmitters are EXCITATORY? " + SATA,
  ["*Glutamate",
   "*Dopamine",
   "GABA || GABA is inhibitory; it is the brain's brake pedal",
   "*Acetylcholine",
   "Glycine || Glycine is an inhibitory neurotransmitter"],
  "Excitatory: glutamate, epinephrine, norepinephrine, dopamine, acetylcholine and histamine. Inhibitory: GABA, glycine and serotonin.")

q("benzo", "A client taking diazepam for anxiety says she feels much better and plans to quit the drug this weekend. Which response by the nurse is best?",
  ["'Stopping suddenly is fine once the anxiety is gone.' || Abrupt withdrawal can cause anxiety, tremor, hypertension and seizures",
   "'Take a double dose for a day, then stop completely.' || Clients should not change their own dose",
   "*'This medicine needs a slow taper rather than a sudden stop.'",
   "'Switch to taking it only when you feel panicky instead.' || Scheduled, not as-needed, use applies to buspirone"],
  "Abrupt benzodiazepine discontinuation can cause anxiety, tremor, hypertension and seizures; taper slowly.")

q("busp", "A client prescribed buspirone asks the nurse what to expect in the first week. Which statements by the nurse are accurate? " + SATA,
  ["*'Take it on a regular schedule, not only when anxious.'",
   "*'The full effect builds over time rather than in minutes.'",
   "'It works within minutes of each dose.' || Buspirone has a delayed therapeutic effect",
   "*'Avoid grapefruit juice, which raises the drug level.'",
   "'Flumazenil can reverse it if you take too much.' || Flumazenil reverses benzodiazepines, not buspirone"],
  "Buspirone is scheduled, not PRN, with a delayed therapeutic effect; grapefruit juice increases levels, and it does not depress the CNS like a benzodiazepine.")

q("ssri", "A client who has taken fluoxetine for 3 weeks tells the nurse the depression is only slightly better and wonders whether to quit. Which response is best?",
  ["'If 3 weeks hasn't helped, the drug will not work for you.' || Full effect may take 4-6 weeks",
   "*'Full benefit may take 4 to 6 weeks, so keep taking it.'",
   "'Take an extra dose each evening to speed things up.' || Clients should not change the dose on their own",
   "'Stop it now and we will start an MAOI tomorrow.' || Starting an MAOI without a 14-day wait risks serotonin syndrome"],
  "Fluoxetine's clinical effect may take 4-6 weeks; antidepressants should not be stopped abruptly.")

q("ssri", "The nurse reviews the chart of a client starting fluoxetine. Which findings or orders should the nurse question or follow up on? " + SATA,
  ["*An order for the dose to be given at bedtime",
   "*A home medication list that includes daily ibuprofen",
   "*A serum sodium of 127 mEq/L",
   "An order for a baseline weight || Weight monitoring is appropriate with fluoxetine",
   "A plan to screen for suicidal ideation at each visit || Monitoring for suicidal ideation is appropriate"],
  "Fluoxetine causes CNS excitation, so it is given in the morning; it raises GI bleeding risk with NSAIDs and can cause hyponatremia from increased ADH. Weight and suicidal ideation are monitored.")

q("snri", "A client has taken venlafaxine for 2 months. Which assessment finding is most important for the nurse to report?",
  ["Mild nausea that eases when the dose is taken with food || Expected effect; give with food for GI upset",
   "A report of taking the dose each morning with breakfast || This is correct administration",
   "*A blood pressure of 152/96 with a baseline of 120/78",
   "A 2-pound weight loss since the last clinic visit || Weight loss is watched for but is not the priority report"],
  "Venlafaxine blocks serotonin and norepinephrine reuptake and can cause hypertension, so blood pressure is monitored regularly.")

q("snri", "A client taking venlafaxine ran out of the medication 2 days ago. Which findings would the nurse expect? " + SATA,
  ["*Anxiety and agitation",
   "*Headache",
   "*Tachycardia",
   "Sedation and bradycardia || Withdrawal causes agitation and tachycardia, not sedation and bradycardia",
   "Weight gain over 2 days || Weight loss, not gain, is watched for with venlafaxine"],
  "Abrupt venlafaxine discontinuation causes anxiety, agitation, headache and tachycardia; taper over 2-4 weeks.")

q("tca", "A client taking amitriptyline reports constipation and a dry mouth. Which self-care measures should the nurse suggest? " + SATA,
  ["*Sip water through the day and chew sugar-free gum",
   "*Add more fiber to meals",
   "*Increase fluid intake unless otherwise restricted",
   "Restrict fluids to reduce the dry mouth || Fluids help both dry mouth and constipation",
   "Switch the dose to the morning for comfort || Amitriptyline is sedating and given at bedtime"],
  "For amitriptyline's anticholinergic effects teach gum, hard candy or water for dry mouth and fluids and fiber for constipation; give the dose at bedtime.")

q("bupro", "A client who smokes asks about bupropion as a quit-smoking aid. Which item in the health history is most important for the nurse to report?",
  ["A history of asthma treated with an inhaler || Asthma is not a listed contraindication",
   "A thyroid condition treated with daily medication || Hypothyroidism is not a listed contraindication",
   "*A seizure disorder diagnosed in adolescence",
   "A history of glaucoma treated with eye drops || Glaucoma is not a listed contraindication"],
  "Bupropion increases seizure risk; contraindications include a seizure disorder, a history of an eating disorder and concurrent MAOI use.")

q("maoi", "A client taking phenelzine is planning dinner at a restaurant. Which menu choice should the nurse approve?",
  ["A salami sandwich with aged cheddar || Aged cheese and aged or smoked meat contain tyramine",
   "A smoked sausage platter with a beer || Smoked meat and beer contain tyramine",
   "*Fresh grilled fish with steamed broccoli and rice",
   "A salad topped with aged blue cheese || Aged cheese contains tyramine"],
  "Clients on an MAOI avoid tyramine foods such as aged cheese, aged or smoked meat and beer; fresh whole foods, fruits and vegetables are safer.")

q("sideeff", "A new medication is described as blocking acetylcholine. Which client complaints should the nurse anticipate? " + SATA,
  ["*Trouble starting a urine stream",
   "*Blurry vision when reading",
   "*A persistently dry mouth",
   "Frequent loose stools || Anticholinergic effects cause constipation, not diarrhea",
   "A hypertensive crisis after cheese || That is the tyramine reaction with MAOIs"],
  "Anticholinergic effects from blocking acetylcholine: dry mouth, constipation, urinary retention and blurred vision.")

q("sero", "A client started on an antidepressant 1 week ago is prescribed a second serotonergic medication. Which new findings would the nurse report immediately?" + " " + SATA,
  ["*Agitation and confusion",
   "*Tremor",
   "*Fever and sweating",
   "Bradycardia with a low body temperature || Serotonin syndrome causes fever, not hypothermia and bradycardia",
   "A severe headache after eating aged cheese || That suggests a tyramine hypertensive crisis with an MAOI"],
  "Serotonin syndrome is an emergency: agitation, confusion, tremor, sweating, fever and diarrhea.")

q("lith", "A client with bipolar disorder asks why lithium levels have to be drawn so often. Which response by the nurse is best?",
  ["*'Toxic levels sit close to helpful levels, so we check often.'",
   "'Levels only matter during the first week of therapy.' || The narrow range means ongoing monitoring",
   "'We check levels because lithium is cleared by the liver.' || The kidney handles lithium like sodium",
   "'Testing tells us whether your thyroid dose is correct.' || Thyroid function is monitored separately from lithium levels"],
  "Lithium has a narrow therapeutic range (about 0.8-1.2 mEq/L, with toxicity possible at 1.5), so levels are monitored frequently.")

q("lithtox", "A client taking lithium calls the clinic in July after a long day of yard work in the heat with heavy sweating. Which response by the nurse is best?",
  ["'Cut back on fluids tonight so you don't need the bathroom.' || Fluid restriction raises lithium levels",
   "'Heat makes lithium inactive, so nothing needs to change.' || Fluid and sodium loss raise lithium levels",
   "*'Come in for a lithium level; fluid loss can raise it.'",
   "'Start a salt-free diet until the hot weather passes.' || Low sodium causes the kidneys to retain lithium"],
  "Low body fluid or low sodium from heat, sweating, vomiting or diarrhea makes lithium rise; check a level and hydration.")

q("lithtox", "The nurse reviews new orders and reports for a client stabilized on lithium. Which items should the nurse question? " + SATA,
  ["*A new prescription for naproxen for knee pain",
   "*An order to start a strict low-sodium diet",
   "*A new prescription for hydrochlorothiazide",
   "A plan to drink about 2 to 3 liters of fluid daily || This is correct lithium teaching",
   "An order to take the dose with food for stomach upset || Taking lithium with food or milk helps GI upset"],
  "NSAIDs (except aspirin), diuretics, ACE inhibitors and tetracyclines raise lithium levels, as does a low-sodium diet; teach 2-3 L of fluid daily and consistent sodium.")

q("typical", "A client who began chlorpromazine 3 weeks ago now has a shuffling gait, stiffness and a tremor. Which action by the nurse is best?",
  ["Document it as tardive dyskinesia from long-term therapy || Tardive dyskinesia develops over months to years",
   "*Report these Parkinson-like findings, which occur in the first month",
   "Explain that this is neuroleptic malignant syndrome || NMS adds high fever, rigidity and unstable vital signs",
   "Reassure the client that akathisia resolves without report || Akathisia is restlessness, not gait and tremor changes"],
  "Parkinson-like extrapyramidal findings appear within the first month of a conventional antipsychotic; acute dystonia comes within hours to days and tardive dyskinesia over months to years.")

q("atyp", "A 30-year-old has taken risperidone for 6 months. Which findings should the nurse follow up on? " + SATA,
  ["*A 16-pound weight gain since starting the drug",
   "*A fasting blood glucose of 138 mg/dL",
   "*Triglycerides higher than the previous result",
   "A lower score on a tyramine food diary || Tyramine restriction applies to MAOIs",
   "A serum lithium level that was not drawn || Lithium levels are not monitored for risperidone"],
  "Atypical antipsychotics increase appetite, leading to weight gain, new or worsening diabetes and increased lipids; monitor weight, glucose and cholesterol/triglycerides.")

q("nms", "A client taking haloperidol is found with a temperature of 104°F, rigid muscles, swinging blood pressures and confusion. Which actions should the nurse take? " + SATA,
  ["*Stop the antipsychotic and notify the provider",
   "*Begin cooling measures",
   "*Give fluids for hydration",
   "Apply warm blankets for the chills || Cooling, not warming, is needed",
   "Give an extra antipsychotic dose for the confusion || The antipsychotic is stopped; too much dopamine blockade caused this"],
  "Neuroleptic malignant syndrome is an emergency: stop the antipsychotic, cool and hydrate, notify the provider, and anticipate dantrolene and bromocriptine.")

q("glauc", "A client newly diagnosed with glaucoma asks what the eye drops are meant to do. Which response by the nurse is accurate?",
  ["'They clear an infection on the surface of the eye.' || Glaucoma is a pressure problem, not an infection",
   "'They thicken the optic nerve so pressure cannot hurt it.' || Drops lower pressure; they do not change the nerve",
   "*'They lower eye pressure to protect the optic nerve.'",
   "'They increase how much fluid the eye makes.' || Drops decrease production or increase outflow"],
  "Excess aqueous production and/or decreased outflow raises IOP, damaging the optic nerve and causing peripheral vision loss or blindness; drops lower IOP.")

q("glauc", "The nurse reviews a client's glaucoma drops. Which drug-and-action pairings are correct? " + SATA,
  ["*Timolol: decreases aqueous humor production",
   "*Pilocarpine: constricts the pupil and ciliary muscle to increase outflow",
   "*Echothiophate: inhibits cholinesterase, increasing outflow",
   "Latanoprost: decreases aqueous humor production || Latanoprost increases outflow; timolol decreases production",
   "Timolol: a prostaglandin that may darken the iris || Latanoprost is the prostaglandin analog that darkens pigment"],
  "Timolol, a beta blocker, decreases aqueous production; latanoprost, pilocarpine and echothiophate increase outflow through ciliary/pupil constriction.")

q("drops", "A client will begin two different glaucoma eye drops at home. Which instruction by the nurse is correct?",
  ["'Put both drops in one right after the other.' || Wait at least 5 minutes between different drops",
   "'Rest the dropper tip on the eye for accuracy.' || Don't touch the dropper tip to the eye",
   "*'Wait at least 5 minutes between the two drops.'",
   "'Keep contact lenses in so the drop stays in place.' || Remove contact lenses before instilling drops"],
  "Separate different ophthalmic medications by at least 5 minutes, remove contact lenses first, and don't touch the dropper tip to the eye.")
