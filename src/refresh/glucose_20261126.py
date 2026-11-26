T = "glucose"; SET = "20261126"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# norm
q("norm", "A 45-year-old teacher's pancreas releases insulin after lunch. Which effect does the nurse expect insulin to have?",
  ["The liver breaks down glycogen || That is glucagon's action, which raises glucose",
   "*Potassium moves into cells along with glucose",
   "Ketone production speeds up || Insulin stops the body from making ketones",
   "Blood glucose rises between meals || Insulin moves glucose into cells; glucagon raises it"],
  "Insulin is the key that moves glucose (and potassium) into cells, stores glucose as glycogen in the liver and stops ketone production.")

# metsyn (HI)
q("metsyn", "A 55-year-old male mechanic has a 38-inch waist, HDL of 44 mg/dL, triglycerides of 140 mg/dL and fasting glucose of 104 mg/dL. His BP is 122/78 on a prescribed BP medication. Does he meet metabolic syndrome criteria?",
  ["Yes; his waist and HDL both count for a man || A man needs 40 inches or more and HDL under 40",
   "Yes; his triglycerides and glucose give him 3 criteria || Triglycerides count only at 150 or higher",
   "*No; only his glucose and BP medication count, which is 2 criteria",
   "No; his BP reading is normal, so BP can't count || Taking BP medication counts even with a normal reading"],
  "Three or more of five criteria are needed. Men: waist 40 inches or more and HDL under 40; triglycerides 150 or higher; fasting glucose 100 or higher; BP 130/85 or higher or on BP medication.")
q("metsyn", "A 52-year-old female bus driver has these results. Which findings count toward metabolic syndrome? " + SATA,
  ["*Waist of 37 inches",
   "*HDL of 48 mg/dL",
   "Triglycerides of 140 mg/dL || The cutoff is 150 mg/dL or higher",
   "*BP of 132/86",
   "Fasting glucose of 96 mg/dL || The cutoff is 100 mg/dL or higher"],
  "For women, a waist of 35 inches or more and HDL under 50 count. BP of 130/85 or higher also counts.")

# metsx
q("metsx", "A 49-year-old client has had metabolic syndrome for several years. Which finding does the nurse expect as it progresses?",
  ["Fruity breath and deep breathing || These are signs of DKA",
   "Muscle pain after starting a new medicine || That is a statin side effect",
   "*Fatigue and a growing waistline",
   "Left shoulder pain with fever || That suggests a bariatric leak"],
  "Early metabolic syndrome has no symptoms; as it progresses: growing waist, trouble losing weight, carb cravings, fatigue and fatty liver.")

# metmgmt (HI)
q("metmgmt", "The nurse reviews lifestyle goals with a client who has metabolic syndrome. Which client statements need correction? " + SATA,
  ["I'll aim for at least 150 minutes of moderate exercise a week || Correct; this matches the lecture goal",
   "*I can skip resistance training because only cardio helps my glucose",
   "I'll follow a DASH or Mediterranean eating pattern || Correct; these are the diets taught",
   "*I'll start with medication and change my habits later if needed",
   "I'll choose high-fiber, complex carbs over processed foods || Correct; this fits the diet taught"],
  "Lifestyle modification is the primary intervention. Resistance training helps muscles take up glucose, and at least 150 minutes a week of moderate exercise is the goal.")
q("metmgmt", "A 60-year-old retired firefighter with metabolic syndrome asks why the nurse keeps stressing a 5–10% weight loss. What is the best explanation?",
  ["It removes the need for any follow-up visits || Prevention and health promotion stay the focus",
   "It guarantees a normal BP within a week || The lecture makes no such promise",
   "It reverses type 1 diabetes || Type 1 is autoimmune and needs insulin for life",
   "*It reduces visceral fat and insulin resistance"],
  "Losing 5–10% of body weight within 6 months reduces visceral fat and insulin resistance, the root of metabolic syndrome.")

# metdrugs (HI)
q("metdrugs", "A 63-year-old librarian is starting metformin. Which teaching points should the nurse include? " + SATA,
  ["*Avoid drinking alcohol",
   "*Report muscle aches with fast breathing or confusion",
   "It commonly causes hypoglycemia on its own || Metformin doesn't cause hypoglycemia by itself",
   "*Kidney function will be monitored",
   "*A B12 supplement may be needed over time"],
  "Metformin lowers liver glucose output. Alcohol and cimetidine raise lactic acidosis risk; monitor kidney function; long-term use can cause B12 and folic acid malabsorption.")
q("metdrugs", "A 50-year-old client with severe gastroparesis has a new order for semaglutide. What should the nurse do?",
  ["*Question the order, because severe GI disease is a contraindication",
   "Give it, because it speeds stomach emptying || GLP-1 agonists slow the stomach",
   "Give it with a large meal to prevent nausea || Large meals worsen GLP-1 nausea",
   "Give it and hold the client's metformin || Gastroparesis, not metformin, is the problem"],
  "Semaglutide is contraindicated with medullary thyroid carcinoma, multiple endocrine neoplasia and severe GI disease such as gastroparesis.")

# barind
q("barind", "A 46-year-old client with a BMI of 36 and type 2 diabetes has not lost weight with diet and exercise. The client asks if bariatric surgery is an option. What is accurate?",
  ["No; the BMI must be at least 40 for anyone || BMI 35 or more qualifies with a comorbidity",
   "No; diabetes rules out bariatric surgery || Type 2 diabetes is a qualifying comorbidity",
   "*Yes; a BMI of 35 or more with a comorbidity after failed conservative care qualifies",
   "Yes; any BMI over 30 qualifies || BMI 30–34 alone is not an indication"],
  "Indications: BMI 40 or more, or BMI 35 or more with a comorbidity such as type 2 diabetes, high BP, high lipids or sleep apnea, after failed conservative management.")

# barcare
q("barcare", "The nurse is preparing a client for bariatric surgery next week. Which pre-op teaching topics are appropriate? " + SATA,
  ["*How to use the incentive spirometer",
   "*Splinting the incision when coughing",
   "*Walking early after surgery",
   "Eat a regular diet until surgery || A strict liquid or low-calorie diet 1–2 weeks before shrinks the liver",
   "Skip the psychological evaluation if motivated || A psychological evaluation is required"],
  "Pre-op teaching covers the incentive spirometer, splinting and early walking, along with a liquid or low-calorie diet to shrink the liver.")

# bardc (HI)
q("bardc", "A 38-year-old client is going home after gastric bypass. Which statements show understanding of the discharge diet? " + SATA,
  ["*I'll chew every bite until it's a paste",
   "*I'll stop eating at the first sign of fullness",
   "I'll eat three large meals a day || About 6 small meals a day are taught",
   "*I'll aim for about six small meals a day",
   "I'll stop my vitamins once I reach my goal weight || Supplements are taken for life"],
  "After bariatric surgery: about 6 small meals a day, chew food to a paste, stop at the first sign of fullness, and take supplements for life.")
q("bardc", "Several years after gastric bypass, a client admits they stopped taking calcium citrate and vitamin D. Which complication is this client at risk for?",
  ["Anastomotic leak || A leak is an early surgical complication",
   "*Osteoporosis",
   "Dumping syndrome || Dumping is tied to eating high-carb food",
   "Type 1 diabetes || Type 1 is autoimmune, not a nutrient problem"],
  "Bypassing part of the small intestine impairs calcium absorption, so osteoporosis is a late problem; calcium citrate and vitamin D are taken for life.")

# dx (HI)
q("dx", "The nurse reviews screening results at a health fair. Which results meet the criteria for diabetes? " + SATA,
  ["*A1C of 6.7%",
   "A1C of 6.0% || 5.7–6.4% is prediabetes",
   "*Fasting glucose of 130 mg/dL on two separate days",
   "Fasting glucose of 110 mg/dL || 100–125 is prediabetes",
   "*Random glucose of 215 mg/dL with thirst and frequent urination"],
  "Diabetes: A1C 6.5% or higher, fasting glucose 126 or higher on at least two occasions, or random glucose over 200 with classic symptoms.")
q("dx", "A 57-year-old client with type 2 diabetes has an A1C of 8.6%. How does the nurse interpret this?",
  ["It shows excellent control || The ADA goal for most adults is 7% or below",
   "It means the client has prediabetes || Prediabetes is 5.7–6.4%",
   "It reflects only the last day of glucose || A1C shows about 3 months of control",
   "*It suggests poor glucose control or poor adherence"],
  "An A1C over 8% suggests poor control or poor adherence. The ADA goal for most adults is 7% or below.")

# types
q("types", "A 29-year-old client at 12 weeks of pregnancy asks when she will be screened for gestational diabetes. What does the nurse tell her?",
  ["At the first prenatal visit only || Screening is done later in pregnancy",
   "*Between 24 and 28 weeks",
   "During labor || Screening happens well before delivery",
   "Only if she has symptoms || Screening is routine"],
  "Gestational diabetes screening uses an oral glucose tolerance test at 24–28 weeks: a glucose drink, then blood draws over about 3 hours.")

# t1t2 (HI)
q("t1t2", "A 16-year-old with type 1 diabetes says, 'My grandma switched from insulin to pills. Can I do that too someday?' What is the best response?",
  ["Yes, once your weight is normal || Type 1 is not caused by weight",
   "Yes, metformin replaces insulin in type 1 || Type 1 makes no insulin, so insulin is required",
   "*No; your body makes no insulin, so you'll need insulin for life",
   "Only after puberty ends || Type 1 needs insulin for life"],
  "Type 1 is autoimmune destruction of beta cells; no insulin is made, so insulin is needed for life. Type 2 is insulin resistance, treated with lifestyle and metformin first.")
q("t1t2", "Which features are typical of type 2 diabetes? " + SATA,
  ["*It is based on insulin resistance",
   "*It makes up about 90–95% of cases",
   "Autoimmune destruction of beta cells || That is type 1",
   "*Insulin may be needed later as the disease progresses",
   "It often first shows up as DKA in a child || That is typical of type 1"],
  "Type 2 = insulin resistance, 90–95% of cases, often lifestyle-related; insulin may be needed later as it progresses.")

# monitor
q("monitor", "A 34-year-old graphic designer starting a continuous glucose monitor asks what it shows that a single fingerstick doesn't. What is the best answer?",
  ["Ketone levels in the blood || A CGM reads glucose",
   "Glucose levels in the urine || A CGM reads interstitial fluid",
   "Your A1C every hour || A1C reflects about 3 months",
   "*Trends showing which way glucose is moving and how fast"],
  "A CGM reads glucose in interstitial fluid and shows trends: the direction and speed of change.")

# insulin
q("insulin", "Before giving insulin glargine, the nurse notices the solution in the vial looks cloudy. What should the nurse do?",
  ["Roll the vial; glargine is normally cloudy || Only NPH is the cloudy insulin",
   "*Do not use it; glargine should be clear",
   "Give it, since appearance doesn't matter || Clear insulin that looks cloudy should not be used",
   "Mix it with NPH to clear it up || That doesn't fix a cloudy clear insulin"],
  "NPH is the cloudy insulin. A clear insulin that looks cloudy should not be used.")

# insadmin (HI)
q("insadmin", "Which statements about insulin storage and injection are correct? " + SATA,
  ["*Keep unopened insulin in the refrigerator",
   "*Opened insulin is good for 28 days at room temperature",
   "Keep insulin in the freezer to make it last || Freezing is not the storage method taught",
   "*Write the date on a vial or pen the day it's opened",
   "*A very thin client may need a 45-degree angle"],
  "Unopened insulin is refrigerated; opened insulin lasts 28 days at room temperature, so date it when opened. Inject at 90 degrees, or 45 degrees for thin clients.")
q("insadmin", "A 27-year-old barista uses lispro with an insulin-to-carb ratio. When should the client inject it in relation to meals?",
  ["*0–15 minutes before eating",
   "1 hour before eating || Rapid-acting insulin works within minutes",
   "At bedtime only || Lispro is a mealtime insulin",
   "2 hours after eating || The dose should match the meal as it starts"],
  "Rapid-acting insulin is given 0–15 minutes before meals because its onset is 5–15 minutes.")

# drugint
q("drugint", "A client on insulin has several new medication orders. Which drugs does the nurse expect to RAISE blood glucose? " + SATA,
  ["*Albuterol",
   "*Prednisone",
   "Glipizide || Sulfonylureas add to hypoglycemia risk",
   "*A thiazide diuretic",
   "High-dose aspirin || It adds to hypoglycemia risk"],
  "Prednisone, albuterol, thiazides and thyroid hormone raise glucose. Sulfonylureas, meglitinides and high-dose aspirin add to hypoglycemia risk.")

# injectables (HI)
q("injectables", "A 61-year-old client on semaglutide has vomited for 2 days and now feels dizzy when standing. What does the nurse suspect?",
  ["Expected weight loss, so no action || Ongoing vomiting needs evaluation",
   "Hypoglycemia caused by semaglutide alone || GLP-1s rarely cause lows on their own",
   "*Severe dehydration from vomiting",
   "Lactic acidosis || That is a metformin risk"],
  "GLP-1 agonists cause nausea, vomiting and diarrhea, which can lead to severe dehydration. They rarely cause hypoglycemia alone because they release insulin only when glucose is high.")
q("injectables", "The nurse watches a client with type 1 diabetes draw pramlintide into the same syringe as their insulin. What should the nurse do?",
  ["Praise the client for saving an injection || Pramlintide is never mixed with insulin",
   "Tell the client to inject it after the meal || It is given 30 minutes before meals",
   "Have the client double the insulin dose || Pramlintide with insulin raises the risk of severe lows",
   "*Stop the client and teach that it is never mixed with insulin"],
  "Pramlintide, an amylin mimetic, is injected 30 minutes before meals, never mixed in the same syringe as insulin, and can cause severe lows with insulin.")

# orals
q("orals", "A client who started acarbose last week reports gas and loose stools. How does the nurse interpret this?",
  ["Signs of lactic acidosis || That is a metformin risk",
   "*Expected side effects from blocked carb breakdown",
   "Signs of pancreatitis || Pancreatitis is a gliptin and GLP-1 risk",
   "Dumping syndrome || Dumping follows bariatric surgery"],
  "Acarbose blocks carbohydrate breakdown and is taken with the first bite of each meal; gas, diarrhea and abdominal pain are side effects.")

# sglt2
q("sglt2", "A 66-year-old client is starting dapagliflozin. Which teaching should the nurse include? " + SATA,
  ["*Keep the genital area clean",
   "*Drink enough fluids to stay hydrated",
   "Take it at bedtime || It is taken in the morning",
   "*Take it in the morning, with or without food",
   "Expect it to cause less urination || It increases urination"],
  "SGLT2 inhibitors make the kidneys spill glucose and sodium into the urine. Take in the morning; stay hydrated and keep good hygiene because genital and urinary infections are common.")

# hyper
q("hyper", "A client's fasting glucose has been high every morning. Which check helps the nurse tell the dawn phenomenon from the Somogyi effect?",
  ["An A1C level || A1C shows about 3 months, not overnight",
   "A bedtime urine ketone test || Ketones don't separate these two",
   "A glucose 2 hours after lunch || The key reading is overnight",
   "*A 3 a.m. glucose"],
  "Somogyi = an overnight low then a rebound high; dawn = a rising early-morning glucose from growth hormone. A 3 a.m. glucose tells them apart.")

# hypo (HI)
q("hypo", "Which situations commonly cause hypoglycemia in a client with diabetes? " + SATA,
  ["*Taking too much diabetes medication",
   "Starting prednisone || Prednisone raises glucose",
   "*Eating too little food",
   "*Extra physical activity",
   "Having the flu || Illness raises glucose"],
  "Common causes of hypoglycemia: too much medication, too little food or extra activity.")
q("hypo", "A client's glucose was 59 mg/dL. After two rounds of 15 g of fast carbs, the recheck is 82 mg/dL. What should the nurse do next?",
  ["Give another 15 g of juice || Glucose is now above 70",
   "*Give a snack or a meal",
   "Give the scheduled rapid-acting insulin now || This could cause another low",
   "No further action is needed || A snack or meal follows a treated low"],
  "Repeat the 15-15 rule until glucose is above 70, then give a snack or meal.")

# dka (HI)
q("dka", "A 7-year-old with no history of diabetes arrives with vomiting, deep rapid breathing and a glucose of 480 mg/dL. The parent asks, 'How can this happen with no warning?' What is the nurse's best response?",
  ["*DKA is often the first sign of type 1 diabetes in children",
   "This is HHS, which is common in young children || HHS is more common in type 2",
   "This is caused by eating too much candy || Type 1 is autoimmune",
   "This is low blood sugar from skipping meals || A glucose of 480 is high"],
  "DKA is often the first sign of type 1 in children; type 1 is autoimmune destruction of beta cells.")
q("dka", "Which finding points to DKA rather than HHS?",
  ["Glucose over 600 mg/dL || That is the HHS cutoff",
   "Serum osmolality over 320 || That is an HHS finding",
   "*Ketones with metabolic acidosis",
   "Onset slowly over days to weeks || HHS develops more slowly"],
  "DKA triad: high glucose, ketones and metabolic acidosis. HHS has glucose over 600, high osmolality and little or no ketosis.")

# dkatx (HI)
q("dkatx", "Which insulin order does the nurse expect for an adult in DKA?",
  ["A large IV glargine bolus || Only regular insulin is given IV",
   "Subcutaneous NPH every 12 hours || DKA needs a continuous IV infusion",
   "*A continuous IV regular insulin infusion with no initial bolus",
   "A single lispro bolus, then no more insulin || Insulin runs as a continuous drip"],
  "DKA: regular insulin 0.1 units/kg/hr by continuous IV infusion, with no initial bolus.")
q("dkatx", "A client being treated for DKA now has a pH of 7.34, bicarbonate of 20, anion gap of 10 and glucose of 180 mg/dL. What does the nurse anticipate?",
  ["Increase the insulin drip rate || These results show DKA has resolved",
   "Give sodium bicarbonate || The pH is no longer acidotic",
   "Give IV D50 || The glucose isn't low",
   "*Switching to subcutaneous insulin"],
  "DKA has resolved with pH over 7.30, bicarbonate over 18, anion gap under 12 and glucose under 200; the client can switch to subcutaneous insulin.")

# hhs (HI)
q("hhs", "A 74-year-old nursing home resident with type 2 diabetes is lethargic. Which lab pattern fits HHS?",
  ["pH 7.10 with large ketones || That fits DKA",
   "*Sodium over 145, high BUN and creatinine, high hematocrit",
   "Glucose of 58 mg/dL || That is hypoglycemia",
   "Bicarbonate under 15 with an anion gap over 12 || That fits DKA"],
  "HHS labs: glucose over 600, osmolality over 320, sodium over 145, high BUN/creatinine, bicarbonate over 15 and high hematocrit from hemoconcentration.")
q("hhs", "Which statements about HHS are accurate? " + SATA,
  ["*The fluid deficit is often 8–12 L",
   "It is seen mostly in type 1 diabetes || HHS is more common in type 2",
   "*There is little or no ketosis",
   "*It develops over days to weeks",
   "It has a lower death rate than DKA || HHS has a higher death rate"],
  "HHS develops slowly, is more common in type 2, has a higher death rate than DKA, little or no ketosis, and a typical fluid deficit of 8–12 L.")

# hhstx (HI)
q("hhstx", "During HHS treatment, the client's glucose falls to 290 mg/dL. Which change to the insulin drip does the nurse anticipate?",
  ["Double the infusion rate || Glucose is lowered slowly",
   "Give an extra insulin bolus || Fast drops risk cerebral edema",
   "*Reduce the infusion rate",
   "Keep the same rate until glucose is normal || The drip is reduced under 300"],
  "Reduce the insulin drip when glucose is under 300, or stop it under 250 after provider evaluation; lower glucose 50–70 mg/dL per hour to prevent cerebral edema.")
q("hhstx", "An 81-year-old receiving IV fluids for HHS develops crackles and new shortness of breath. Which complication does the nurse suspect?",
  ["DKA developing || HHS has little or no ketosis",
   "Dumping syndrome || Dumping follows bariatric surgery",
   "Hypoglycemia || Crackles and dyspnea are not low-glucose signs",
   "*Pulmonary edema from fluid overload"],
  "Watch older adults for fluid overload and pulmonary edema during HHS fluid replacement; fluids are adjusted based on heart status.")

# whipple (HI)
q("whipple", "Which pairings of hypoglycemia level and description are correct? " + SATA,
  ["*Level 1: 54–69 mg/dL, awake",
   "*Level 2: under 54 mg/dL",
   "Level 1: under 54 mg/dL with confusion || That is Level 3",
   "*Level 3: under 54 mg/dL with altered consciousness",
   "Level 3: 65 mg/dL and alert || That is Level 1"],
  "Level 1: 54–69, awake. Level 2: under 54. Level 3: under 54 with altered consciousness, treated with IV D50W.")
q("whipple", "A 30-year-old client with anxiety feels shaky and sweaty. The glucose is 112 mg/dL. How does the nurse interpret this?",
  ["Whipple's triad is met, so give juice || The glucose isn't low",
   "*Whipple's triad isn't met; another cause such as anxiety may mimic a low",
   "This is Level 1 hypoglycemia || Level 1 is 54–69",
   "This is the Somogyi effect || Somogyi is an overnight low then a rebound high"],
  "Whipple's triad: low glucose, symptoms, and relief with glucose. Anxiety, migraine, TIA, hyperthyroidism and alcohol can mimic a low, so check the glucose.")

# statin (HI)
q("statin", "A client on atorvastatin asks why unexplained muscle pain must be reported right away. What is the best explanation?",
  ["*Muscle breakdown can damage the kidneys",
   "It means the drug is lowering glucose too much || Statins act on lipids",
   "It is a sign of a liver infection || Muscle pain points to rhabdomyolysis",
   "It means the dose should be doubled || Doubling worsens the risk"],
  "Rhabdomyolysis is muscle breakdown that can damage the kidneys, so report new, unexplained muscle pain or weakness right away.")
q("statin", "A 58-year-old client starting simvastatin asks what the medicine does. Which explanation is accurate?",
  ["It releases more insulin from the pancreas || That describes sulfonylureas",
   "It slows how fast the stomach empties || That describes GLP-1 agonists",
   "*It lowers LDL and triglycerides and stabilizes plaque",
   "It replaces missing vitamin B12 || Statins don't treat B12 deficiency"],
  "Statins lower LDL and triglycerides and stabilize plaque. Monitor baseline and periodic LFTs and report muscle pain.")

# leak (HI)
q("leak", "The nurse is caring for four clients on a bariatric unit. Which client should the nurse see FIRST?",
  ["A client rating incision pain 4 out of 10 || Expected post-op pain",
   "A client asking when solid food can start || A teaching need, not urgent",
   "*A client after sleeve gastrectomy with a heart rate of 126 and new fever",
   "A client wearing SCDs who wants to walk || Early walking is expected"],
  "Unexplained tachycardia over 120 is the earliest sign of an anastomotic leak; with fever, it needs the surgeon immediately.")
q("leak", "A suspected staple line leak after gastric bypass was not treated. Which finding shows it has progressed to peritonitis?",
  ["Cramping 30 minutes after a sweet drink || That is dumping",
   "Mild hunger between meals || Not a complication",
   "Weight loss of 1–2 lb a week || Expected after surgery",
   "*Guarding and a rigid, board-like abdomen"],
  "An untreated leak can cause peritonitis: guarding and a rigid, board-like abdomen.")

# dumping (HI)
q("dumping", "A client asks why sweets cause cramping and diarrhea since their gastric bypass. Which explanation is accurate?",
  ["*High-sugar food moves quickly into the small intestine and pulls fluid in",
   "The staple line is leaking || Leak signs are fever and tachycardia",
   "Insulin levels drop too low after eating || Not the cause taught",
   "The stomach makes too much acid after sugar || Not the cause taught"],
  "In dumping syndrome, high-sugar food moves quickly into the small intestine and pulls fluid in, causing symptoms about 30 minutes after eating.")
q("dumping", "A client 2 months after gastric bypass reviews ways to prevent dumping. Which statement needs correction?",
  ["I'll lie down for 30 minutes if symptoms start || Correct; this slows gastric emptying",
   "I'll eat six small meals a day || Correct; this helps prevent dumping",
   "I'll wait 30 minutes after eating before I drink || Correct; no liquids 30–60 minutes after solids",
   "*I'll have a milkshake with my dinner"],
  "Prevent dumping with six small meals, no sweets and no liquids 30 minutes before or 30–60 minutes after solid food.")

# chronic
q("chronic", "A 70-year-old client with long-standing diabetes and autonomic neuropathy reports only mild fatigue. Why does the nurse stay alert for a heart attack?",
  ["Retinopathy hides chest pain || Retinopathy affects the eyes",
   "*Autonomic neuropathy can cause a silent MI",
   "Nephropathy causes chest pain at rest || The kidney is not the cause here",
   "Low glucose always mimics an MI || Not the reason taught"],
  "Autonomic neuropathy can cause dizziness on standing, early fullness and a silent MI.")

# sick (HI)
q("sick", "A client with diabetes has the flu and can't keep solid food down. What should the nurse teach?",
  ["Skip insulin until you can eat again || Illness raises glucose; keep taking insulin",
   "Stop drinking fluids to avoid vomiting || Drink 8–12 oz of sugar-free fluid hourly",
   "*Use soft or liquid carbs and keep taking your insulin",
   "Check glucose only once a day || Check about every 4 hours"],
  "Sick day rules: keep taking insulin, use soft or liquid carbs if solids aren't tolerated, drink sugar-free fluids and check glucose about every 4 hours.")
q("sick", "The nurse returns calls from four sick clients with diabetes. Which client should go to the emergency department?",
  ["A client with a glucose of 190 and a mild sore throat || Can manage at home with sick day rules",
   "A client drinking sugar-free fluids every hour || That follows the sick day rules",
   "A client using sugar-free cough medicine || That is correct teaching",
   "*A client who has been vomiting for 8 hours"],
  "Go to the ED for vomiting over 6 hours, glucose staying over 240, urine ketones, fruity breath or confusion; these signal DKA risk.")

# dc
q("dc", "A client learning carb counting asks how many carbohydrates to plan for each meal. What does the nurse say?",
  ["About 5–10 g || Far below the slide's target",
   "*About 45–60 g",
   "About 150 g || Far above the slide's target",
   "There is no limit || The slide gives a target"],
  "The carb counting slide suggests about 45–60 g of carbs per meal and 15–30 g per snack.")
