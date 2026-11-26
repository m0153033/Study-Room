T = "hf"; SET = "20261126"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("co", "A 48-year-old teacher with heart failure learns her EF is 35%. Which explanation by the nurse is accurate?", [
  "EF tells how full the ventricle is at the end of diastole || That describes preload",
  "*Her left ventricle pushes out a smaller-than-normal percent of its blood each beat",
  "Her EF falls within the normal range for adults || Normal EF is 55–70%",
  "EF measures the resistance the ventricle pushes against || That describes afterload"],
  "EF is the percent of left ventricle blood pushed out with each beat; normal is 55–70%. Preload is end-diastolic fullness and afterload is resistance to ejection.")

q("targets", "A nurse reviews a heart failure medication list. Which drug is matched with the part of heart function it mainly targets?", [
  "Digoxin — lowers preload || Digoxin targets contractility",
  "Furosemide — strengthens contractility || Furosemide lowers preload",
  "*Hydralazine — lowers afterload",
  "Milrinone — lowers afterload || Milrinone targets contractility"],
  "Preload: diuretics, nitrates, SGLT2 inhibitors. Afterload: ACE inhibitor/ARB/ARNI and hydralazine. Contractility: digoxin, dobutamine and milrinone.")

q("causes", "A 70-year-old retired mechanic with stable heart failure is admitted with fluid overload. Which client statement most likely explains the trigger?", [
  "'I've been walking 20 minutes every morning.' || Regular activity is not a trigger",
  "'I've been taking every pill right on schedule.' || Missed meds, not adherence, are a trigger",
  "'I've started reading food labels for salt.' || Limiting salt prevents overload",
  "*'I've been taking ibuprofen every day for my back.'"],
  "Triggers include missed meds, salt or fluid excess, NSAIDs, infection, uncontrolled BP and new A-fib. NSAIDs make the body hold fluid.")

q("comp", "A nursing student reviews how the body compensates in heart failure. Which statements are accurate? " + SATA, [
  "*SNS and RAAS responses help short term but strain the heart long term",
  "*Holding salt and water adds more volume for an already weak heart",
  "*Beta blockers help by calming the SNS response",
  "Compensation makes the kidneys lose extra sodium || RAAS makes the body hold salt and water",
  "Remodeling means the heart heals back to its normal shape || Remodeling is a harmful change in size and shape"],
  "SNS and RAAS 'fixes' hold salt and water and tighten vessels, adding volume and resistance. Beta blockers calm the SNS; ACE/ARB and spironolactone block RAAS and slow remodeling.")

q("sysdia", "Which finding pairs correctly with systolic heart failure (HFrEF)?", [
  "An S4 with an EF of 50% or more || That fits diastolic HFpEF",
  "Stiff, thick walls that can't relax and fill || That fits diastolic HFpEF",
  "*An S3 with an EF of 40% or less",
  "No survival benefit from the four pillars || The four pillars improve survival in HFrEF"],
  "HFrEF: the ventricle can't squeeze; EF 40% or less; S3. HFpEF: can't relax and fill; EF 50% or more; S4.")

q("lr", "A 58-year-old bus driver with heart failure has swollen ankles, RUQ discomfort and a poor appetite. Which other finding would the nurse expect from the same side of failure?", [
  "Orthopnea that needs three pillows || Orthopnea is a left-sided (lung) sign",
  "Pink, frothy sputum || Pink frothy sputum is pulmonary edema, a left-sided sign",
  "Crackles that don't clear with coughing || Crackles are a left-sided (lung) sign",
  "*Jugular vein distension"],
  "Right = rest of the body: JVD, dependent edema, weight gain, an enlarged liver with RUQ discomfort, and nausea or poor appetite. Left = Lungs.")

q("lr", "A nursing student lists findings of RIGHT-sided heart failure. Which item on the list needs correction?", [
  "Dependent edema || Dependent edema is a right-sided sign",
  "*Waking at night short of breath",
  "An enlarged liver || An enlarged liver is a right-sided sign",
  "Nausea and poor appetite || Nausea and poor appetite are right-sided signs"],
  "Waking at night short of breath is a left-sided (lung) finding. Right-sided failure shows in the rest of the body: JVD, dependent edema, weight gain, an enlarged liver and poor appetite.")

q("nyha", "A client admitted in NYHA Class IV heart failure improves with treatment and asks, 'Am I stuck in Class IV forever?' Which response is accurate?", [
  "'Yes, a class is fixed once it is assigned.' || Clients can move between classes",
  "*'No, clients can move up or down the classes.'",
  "'Classes only move up, never back down.' || Clients can move up or down",
  "'Class IV means you have no symptoms at rest.' || Class IV means symptoms at rest"],
  "In NYHA Class IV, symptoms occur at rest, the most severe class. Clients can move up or down classes.")

q("bnp", "A client with dyspnea has a high BNP. Which statement by the nurse is accurate?", [
  "*It supports heart failure, but the echo is the gold standard",
  "It confirms heart failure without any other test || BNP supports but doesn't make the diagnosis alone",
  "It shows that the kidneys are failing || BNP comes from stretched ventricles",
  "One value is enough to guide all treatment || BNP should be trended"],
  "Stretched, overloaded ventricles release BNP; higher BNP means more stretch. BNP supports but doesn't make the diagnosis alone; the echo is the gold standard.")

q("bnp", "A heart failure client's BNP rises steadily over 3 days of hospital care. How should the nurse interpret this trend?", [
  "Treatment is working and the ventricles are relaxing || A falling BNP shows treatment is working",
  "The lungs are the likely cause of the dyspnea || That fits a BNP under 100",
  "*The ventricles are more stretched; failure may be worsening",
  "BNP values can't be compared from day to day || BNP should be trended"],
  "Higher BNP means more ventricular stretch, so a rising trend suggests worsening failure. Trend BNP rather than reacting to one number.")

q("imaging", "A 61-year-old client has just returned from a TEE. Which nursing actions are appropriate? " + SATA, [
  "*Monitor vital signs",
  "*Assess the level of sedation",
  "*Check the gag reflex before giving fluids",
  "Give sips of water right away to soothe the throat || The throat is numbed; check the gag reflex first",
  "Treat severe throat pain as expected || Severe throat pain may mean esophageal injury and is reported"],
  "After a TEE, check vitals, sedation level and gag reflex. Report severe throat pain, trouble swallowing, bleeding or chest pain.")

q("labs", "A client with right-sided heart failure has elevated LFTs. What does the nurse recognize as the likely cause?", [
  "An overactive thyroid gland || Thyroid disease is screened with TSH",
  "Too much salt in the diet || Salt intake doesn't raise LFTs",
  "Improving kidney function || Kidney function is not shown by LFTs",
  "*Liver congestion from the failing right side"],
  "Liver congestion from right-sided failure raises LFTs. Right-sided failure also causes an enlarged liver and RUQ discomfort.")

q("hemo", "Four heart failure clients have their MAP checked. Which reading shows adequate organ perfusion?", [
  "MAP of 58 mmHg || A MAP under 65 doesn't perfuse the organs",
  "MAP of 61 mmHg || A MAP under 65 doesn't perfuse the organs",
  "*MAP of 72 mmHg",
  "MAP of 63 mmHg || A MAP under 65 doesn't perfuse the organs"],
  "A MAP under 65 doesn't perfuse the organs and should be reported. Poor perfusion signs include low urine output, confusion and cool skin.")

q("assess", "A nurse on a cardiac unit receives report on four heart failure clients. Which client should the nurse see first?", [
  "A client with fine basilar crackles unchanged since yesterday || Stable, unchanged crackles are not the emergency",
  "A client with an hourly urine output of 45 mL || Only output under 30 mL/hr is reported",
  "*A client with gurgling breath sounds and pink, frothy sputum",
  "A client asking which foods are high in sodium || A teaching need is not urgent"],
  "Gurgling breath sounds with pink, frothy sputum signal severe pulmonary edema, an emergency. Report urine output under 30 mL/hr.")

q("assess", "A nurse auscultates the lungs of a 67-year-old client with heart failure. Which statements are accurate? " + SATA, [
  "*Crackles that don't change after a cough suggest fluid, not secretions",
  "*Crackles start at the bases and move up as fluid builds",
  "*Wheezing in heart failure improves when diuretics remove fluid",
  "Wheezing in heart failure is best treated with a bronchodilator || Fluid in the airway walls causes it; diuretics fix it",
  "Crackles that clear with coughing mean pulmonary edema || Crackles that clear are secretions"],
  "Crackles that don't change with coughing mean fluid in the lungs; they start at the bases and move up. Wheezing in heart failure comes from fluid in the airway walls and is fixed by diuresis.")

q("weight", "A 52-year-old chef with heart failure describes how he weighs himself at home. Which statement shows correct technique?", [
  "'I weigh myself after dinner when I have time.' || Weigh every morning at the same time",
  "*'I weigh after I urinate, before breakfast, on the same scale.'",
  "'I use whichever scale is closest that day.' || Use the same scale each time",
  "'I weigh myself once at the start of each month.' || Weights should be daily"],
  "Weigh every morning at the same time, after urinating and before breakfast, on the same scale in similar clothes. Consistency makes the trend accurate.")

q("weight", "Why is the daily weight the best way to track a heart failure client's fluid status?", [
  "It shows how well the ventricle squeezes || The echo shows the EF",
  "It measures how stretched the ventricles are || That is what BNP reflects",
  "It replaces the need to listen to lung sounds || Lung sounds are checked at every assessment",
  "*Each 1 kg gained equals about 1 L of fluid"],
  "Daily weight is the best way to track fluid status because 1 kg equals 1 L of fluid. Still listen to lung sounds at every assessment, since new crackles can come early.")

q("edjvd", "A nurse assesses edema and JVD in a heart failure client. Which actions are correct? " + SATA, [
  "*Raise the head of the bed to 30–45 degrees to check JVD",
  "*Check the sacrum for edema in a client on bedrest",
  "*Compare both legs when checking for swelling",
  "Lay the client flat to look for JVD || Position at 30–45 degrees",
  "Assume swelling in only one calf is heart failure edema || One-sided swelling suggests another cause, like DVT"],
  "Check JVD with the head of the bed at 30–45 degrees, looking above the collarbone. Fluid follows gravity, so check the sacrum in bedbound clients, and always compare both sides.")

q("pillars", "A client with HFrEF takes the following drugs. Which one is NOT one of the four pillars?", [
  "Carvedilol || A beta blocker is a pillar",
  "Empagliflozin || An SGLT2 inhibitor is a pillar",
  "*Digoxin",
  "Spironolactone || An aldosterone antagonist is a pillar"],
  "The four pillars are an ARNI (or ACE inhibitor/ARB), a beta blocker, an aldosterone antagonist and an SGLT2 inhibitor. Diuretics and digoxin treat symptoms only.")

q("loop", "A nurse reviews home furosemide teaching with a 63-year-old client. Which client statement shows understanding?", [
  "'I'll take it at bedtime so it works overnight.' || Take it in the morning",
  "'I'll take it only on days my ankles swell.' || It is taken as prescribed, not only when swollen",
  "*'I'll take it in the morning and get up slowly.'",
  "'Ringing in my ears is a normal effect to ignore.' || Ringing in the ears should be reported"],
  "Take oral furosemide in the morning and rise slowly. Report cramps, weakness or ringing in the ears.")

q("loop", "IV furosemide is due for a 77-year-old client with heart failure. Which findings should make the nurse hold the dose and notify the provider? " + SATA, [
  "*Potassium of 3.2 mEq/L",
  "*Low blood pressure",
  "*Signs of dehydration",
  "Crackles in both lung bases || Crackles are a reason the drug is given",
  "Swelling in both ankles || Edema is a reason the drug is given"],
  "Before furosemide, check BP, potassium, weight, I&O and lung sounds. Hold and notify for potassium under 3.5, low BP or dehydration.")

q("spiro", "A client is due spironolactone. Which lab results are most important to review first?", [
  "*Potassium and creatinine",
  "Blood glucose and A1C || These are not the spironolactone checks",
  "TSH and LFTs || These are not the spironolactone checks",
  "Digoxin level and BNP || These are not the spironolactone checks"],
  "Spironolactone keeps potassium in the body. Check potassium and creatinine, and hold for potassium over 5.0 or rising creatinine.")

q("ace", "A 29-year-old client taking lisinopril for heart failure says she hopes to become pregnant soon. What should the nurse do?", [
  "Tell her lisinopril is the preferred drug in pregnancy || ACE inhibitors are avoided in pregnancy",
  "*Explain ACE inhibitors aren't used in pregnancy and notify the provider",
  "Tell her to double the dose once she is pregnant || ACE inhibitors are avoided in pregnancy",
  "Tell her to switch to losartan on her own || ARBs are also avoided in pregnancy"],
  "ACE inhibitors, ARBs and ARNI are all avoided in pregnancy. ACE inhibitors end in -pril and can raise potassium.")

q("arb", "A client starting losartan makes several statements. Which statement needs correction?", [
  "'Losartan shouldn't give me the cough lisinopril did.' || ARBs don't cause a bradykinin cough",
  "'I'll use birth control while I take losartan.' || ARBs are avoided in pregnancy",
  "*'I'll keep taking my lisinopril along with losartan.'",
  "'Losartan ends in -sartan, like valsartan.' || ARBs end in -sartan"],
  "An ARB is not combined with an ACE inhibitor or with sacubitril/valsartan. ARBs end in -sartan, give the same benefits without the cough and are avoided in pregnancy.")

q("arni", "A client switching from enalapril to sacubitril/valsartan asks why there is a 36-hour wait. Which explanation is accurate?", [
  "*Both drugs block bradykinin breakdown, so overlap risks angioedema",
  "Overlap would drop the potassium too low || The danger of overlap is angioedema",
  "Overlap would cause ringing in the ears || The danger of overlap is angioedema",
  "Enalapril must clear so the BNP can drop || The danger of overlap is angioedema"],
  "ACE inhibitors and sacubitril/valsartan both block bradykinin breakdown. A 36-hour gap after an ACE inhibitor prevents angioedema.")

q("arni", "Sacubitril/valsartan is due for a client with HFrEF. Which findings should make the nurse hold it and notify the provider? " + SATA, [
  "*Low blood pressure",
  "*Potassium of 5.6 mEq/L",
  "*New swelling of the lips",
  "An EF of 30% on the last echo || HFrEF is the reason the drug is given",
  "Potassium of 4.2 mEq/L || The hold point is potassium over 5.0"],
  "Before each dose check BP, potassium and creatinine. Hold for low BP, potassium over 5.0 or angioedema.")

q("bb", "A client with HFrEF asks why a drug that slows the heart, carvedilol, helps a weak heart. Which response is best?", [
  "'It makes the heart squeeze harder right away.' || Inotropes such as digoxin do that",
  "'It removes extra fluid from the lungs.' || Diuretics remove fluid",
  "'It is safe to stop once you feel better.' || Stopping suddenly can cause rebound fast HR and high BP",
  "*'Slowing the heart lets it fill better, and EF can improve.'"],
  "Beta blockers slow the heart so it fills better, and EF can improve over time. Never stop them suddenly.")

q("sglt2", "A 66-year-old client taking empagliflozin calls reporting genital pain and swelling with a fever. What should the nurse advise?", [
  "'Keep the area clean; this is expected.' || Genital pain and swelling with fever is reported right away",
  "*'Report this right away; it needs prompt evaluation.'",
  "'Double the dose until the fever is gone.' || Never double the dose",
  "'Drink less fluid until the swelling goes down.' || Fluid restriction won't treat this"],
  "SGLT2 inhibitor teaching: keep the genital area clean and report genital pain or swelling with fever right away. Fournier's gangrene is rare but serious.")

q("dig", "A 6-month-old's apical pulse is 84 before a scheduled dose of digoxin. What should the nurse do?", [
  "Give it, since the pulse is above 60 || 60 is the adult hold point",
  "Count the radial pulse for 15 seconds instead || Count the apical pulse for 1 full minute",
  "*Hold the dose and notify the provider",
  "Give half the dose and recheck later || Don't change doses on your own"],
  "Hold digoxin for an apical pulse under 60 in adults, 70 in children and 90 in infants. Count the apical pulse for 1 full minute.")

q("dig", "A nurse reviews digoxin teaching with an 80-year-old client. Which client statements show understanding? " + SATA, [
  "*'If I miss a dose, I won't double the next one.'",
  "*'I'll check my pulse every day.'",
  "*'I'll report it if I lose my appetite or feel nauseated.'",
  "'Yellow-green halos around lights are normal.' || Halos are a sign of toxicity",
  "'My age makes toxicity less likely.' || Older age raises the risk"],
  "Teach never to double a missed dose and to check the pulse daily. Loss of appetite and nausea are early signs of toxicity; later come halos, confusion and slow HR.")

q("vasoino", "A client is receiving an IV dobutamine infusion. Which plan should the nurse question?", [
  "Running the infusion on a pump and titrating it || Inotropes run on a pump and are titrated",
  "Keeping the client on telemetry || Telemetry is needed",
  "*Stopping the infusion suddenly at shift change",
  "Checking BP and urine output often || Frequent BP and urine checks are needed"],
  "IV dobutamine and milrinone run on a pump, need telemetry and frequent BP and urine checks, and must be weaned, not stopped suddenly.")

q("check", "Which drug is matched with the correct check before giving it?", [
  "Digoxin — a hearing check || Check the apical pulse for 1 full minute",
  "Spironolactone — a blood glucose || Check potassium and creatinine",
  "*Metoprolol — apical heart rate and blood pressure",
  "Nitrates — a potassium level only || Ask about erectile dysfunction drugs"],
  "Check apical HR and BP before every beta blocker dose. Digoxin: apical pulse for 1 full minute. Spironolactone: potassium and creatinine. Nitrates: ask about sildenafil or tadalafil.")

q("check", "A nurse reviews morning findings before giving heart failure medications. Which findings call for holding the dose and notifying the provider? " + SATA, [
  "*Furosemide due; potassium is 3.3 mEq/L",
  "*Spironolactone due; potassium is 5.4 mEq/L",
  "*Digoxin due for an adult; apical pulse is 56",
  "Lisinopril due; potassium is 4.4 mEq/L and BP is normal || No hold parameter is met",
  "Sacubitril/valsartan due; BP is normal and potassium is 4.0 mEq/L || No hold parameter is met"],
  "Hold furosemide for potassium under 3.5, spironolactone and ACE/ARNI for potassium over 5.0, and digoxin for an adult apical pulse under 60.")

q("ape", "Which findings are EARLY signs of acute pulmonary edema? " + SATA, [
  "*Anxiety",
  "*Fast breathing",
  "*A cough",
  "*Crackles",
  "Pink, frothy sputum || This is a late sign",
  "Blue, cool, clammy skin || This is a late sign"],
  "Early signs: anxiety, fast breathing, cough and crackles. Late signs: pink frothy sputum, blue cool clammy skin, falling O2 sat despite oxygen, confusion and low BP.")

q("ape", "A client is in acute pulmonary edema. Which order should the nurse question?", [
  "High-flow oxygen with BiPAP ready || This is expected treatment",
  "IV furosemide || This is expected treatment",
  "Nitroglycerin if the BP allows || This is expected treatment",
  "*An IV fluid bolus"],
  "Acute pulmonary edema is treated with high-flow oxygen, BiPAP readiness, IV furosemide and nitroglycerin if BP allows. An IV fluid bolus is not part of the treatment.")

q("dc", "A 72-year-old client with heart failure is preparing for discharge. Which client statements show understanding? " + SATA, [
  "*'I'll have a follow-up visit within 7 days.'",
  "*'I'll keep my sodium to 1.5–2 grams a day.'",
  "*'I'll read food labels for salt.'",
  "'I'll stay in bed all day to rest my heart.' || Activity is slowly increased",
  "'I'll drink extra water to flush my kidneys.' || Stay within the fluid limit"],
  "Discharge teaching: sodium 1.5–2 g a day, read labels, stay within the fluid limit, weigh daily and follow up within 7 days. Activity is spaced and slowly increased.")

q("adv", "A client with an ICD receives two shocks in an hour and feels dizzy. What should the client do?", [
  "Call the provider at the next office visit || More than one shock needs 911",
  "*Call 911",
  "Hold a magnet over the device || This is not the teaching",
  "Ignore it if the dizziness passes || More than one shock needs 911"],
  "After one shock with feeling fine, call the provider. More than one shock or feeling unwell means call 911.")

q("life", "A 79-year-old client with heart failure is started on furosemide. Which safety risk should the nurse focus on?", [
  "Bleeding from the diuretic || This is not the listed risk",
  "High blood sugar from the diuretic || This is not the listed risk",
  "*Falls from diuresis and dizziness",
  "Lower digoxin toxicity with age || Older age raises digoxin toxicity risk"],
  "In older adults, watch for falls from diuretics and dizziness. Heart failure may show up as fatigue, confusion or poor appetite.")

q("cm", "A nursing student compares types of cardiomyopathy. Which statement is accurate?", [
  "Dilated: a thick septum, often inherited || That describes hypertrophic",
  "Hypertrophic: large, thin, weak chambers || That describes dilated",
  "*Restrictive: stiff walls, a normal EF and right-sided signs",
  "Restrictive: needs aggressive diuresis || Restrictive needs cautious diuresis"],
  "Dilated: large, thin, weak chambers with a low EF. Hypertrophic: usually inherited, sudden death risk. Restrictive: stiff walls, normal EF, right-sided signs, cautious diuresis.")

q("hcm", "A 22-year-old graduate student with hypertrophic cardiomyopathy asks what to avoid. Which should the nurse include? " + SATA, [
  "*Drinking alcohol",
  "*Competitive sports",
  "*Straining",
  "*Standing up suddenly",
  "Drinking enough fluid || HCM needs filling, so staying hydrated helps"],
  "HCM clients avoid alcohol, competitive sports, sudden standing and straining, plus nitroglycerin, digoxin, hot tubs, saunas and heavy diuresis. The ventricle needs filling.")

q("hcm", "A client with hypertrophic cardiomyopathy has chest discomfort. Which order should the nurse question?", [
  "A beta blocker || Beta blockers help HCM",
  "*Nitroglycerin",
  "Verapamil || Verapamil helps HCM",
  "Encourage oral fluids || HCM needs filling"],
  "Nitroglycerin is avoided in HCM. Beta blockers, verapamil and diltiazem slow the heart so the ventricle can fill.")
