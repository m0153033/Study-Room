T = "e3w82"; SET = "20261125"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("terms", "A client with kidney failure has nitrogen waste building up in the blood along with nausea and confusion. Which term best describes this?",
 ["Azotemia || Azotemia is nitrogen waste without symptoms.",
  "Oliguria || Oliguria describes low urine output.",
  "*Uremia",
  "Cardiorenal syndrome || That is two-way heart–kidney dysfunction."],
 "Azotemia is nitrogen waste in the blood; uremia is azotemia with symptoms.")

q("aki", "A nurse is reviewing four clients who developed AKI. Which client has a POSTRENAL cause?",
 ["Client who hemorrhaged during surgery || Low blood flow is prerenal.",
  "Client who received IV contrast for a CT || Direct kidney damage is intrarenal.",
  "*Older man with an enlarged prostate who can't void",
  "Client with severe burns and dehydration || Low blood flow is prerenal."],
 "Postrenal AKI is blocked urine outflow (BPH, stones, malignancy); prerenal is low blood flow; intrarenal is direct kidney damage.")

q("aki", "A nurse is teaching a new graduate about AKI. Which statements are accurate? " + SATA,
 ["*AKI is a rapid loss of kidney function over hours to days",
  "AKI lasts more than 3 months by definition || That describes CKD.",
  "*AKI may be reversible",
  "*A creatinine rise of at least 0.3 mg/dL within 48 hours meets the criterion",
  "AKI is always permanent once it starts || AKI may recover."],
 "AKI: serum creatinine rises ≥0.3 mg/dL within 48 hours; rapid loss of function over hours to days; AKI may be reversible, CKD is not.")

q("akiphase", "A client with AKI is in the maintenance phase. Which findings should the nurse expect? " + SATA,
 ["*Oliguria",
  "*Fluid retention",
  "*Metabolic acidosis",
  "Large diuresis as nephrons recover || Diuresis occurs in recovery.",
  "*Azotemia"],
 "Maintenance phase: GFR drops, with oliguria, azotemia, fluid retention, electrolyte imbalance and acidosis, often for 1–2 weeks.")

q("akiassess", "A client with AKI has imaging orders. Which order should the nurse question?",
 ["Renal ultrasound of both kidneys || Safe without contrast.",
  "CT of the abdomen without contrast || Safe; no contrast dye.",
  "*IV pyelogram with contrast dye",
  "Routine urinalysis and renal labs || Routine renal tests."],
 "IVP uses contrast dye and is contraindicated with kidney failure; use ultrasound, CT without contrast, renal labs and urinalysis.")

q("akiassess", "A post-op client at risk for AKI has HR 118/min, BP 84/50 mmHg and falling urine output. What should the nurse recognize?",
 ["Signs of fluid overload needing diuretics || Overload shows crackles, edema and weight gain.",
  "*Hypoperfusion; report it and keep MAP above 65",
  "An expected finding after most surgery || Low UO with hypotension needs action.",
  "A reason to wait 6 hours before acting || Waiting lets damage progress."],
 "Assess vital signs for hypoperfusion (tachycardia, hypotension); act early on low urine output and keep MAP above 65.")

q("akitx", "A nurse reviews four clients with AKI. Which client has an indication for renal replacement therapy?",
 ["Client with potassium 5.0 mEq/L || Below the 6.5 threshold.",
  "*Client with severe metabolic acidosis, pH 7.05",
  "Client with creatinine 1.2 mg/dL and no symptoms || Not an RRT criterion.",
  "Client with mild ankle edema and clear lungs || Overload isn't impairing perfusion."],
 "RRT is indicated for symptomatic uremia, K+ >6.5, severe acidosis (pH <7.1) or fluid overload that inhibits tissue perfusion.")

q("ckd", "A 58-year-old African American client with diabetes and hypertension feels well and asks why she is being screened for CKD. Which response is best?",
 ["'CKD only develops after a history of kidney stones.' || Diabetes and hypertension are the leading causes.",
  "'People with CKD always know they have it early.' || About 9 in 10 don't know.",
  "'CKD screening is only needed for children.' || Adults are screened based on risk.",
  "*'Your risk is higher, and most people with CKD don't know it.'"],
 "Diabetes and hypertension are the leading CKD causes; African Americans are at greater risk, and about 9 in 10 adults with CKD don't know it.")

q("ckdsys", "A client with CKD has hematologic changes. Which findings should the nurse anticipate? " + SATA,
 ["*Anemia from decreased erythropoietin",
  "Polycythemia from extra erythropoietin || EPO decreases in CKD.",
  "*Easy bruising or bleeding",
  "*Increased risk of infection",
  "Increased platelet function || Platelet function is impaired."],
 "Hematologic effects of CKD: anemia (low EPO), impaired platelet function (bleeding) and reduced immunity (infection).")

q("ckdcare", "A nurse is teaching a client on hemodialysis whose potassium and phosphorus run high. Which snack choice shows understanding?",
 ["A banana with a small dark cola || Banana is high in potassium; cola is high in phosphorus.",
  "Plain crackers with a dark cola || Dark sodas are high in phosphorus.",
  "*Plain crackers with apple slices",
  "A banana with a glass of water || Bananas are high in potassium."],
 "Dialysis clients limit potassium and phosphorus; avoid bananas (high potassium) and dark sodas (high phosphorus).")

q("ckdcare", "A client with CKD on a fluid restriction says, 'Soup and ice pops don't count toward my fluid limit.' Which response by the nurse is best?",
 ["*'Soup and ice pops count toward your fluid limit.'",
  "'That's right; only plain water counts.' || Fluid-containing foods count.",
  "'You don't need a fluid limit until dialysis starts.' || Restriction is as prescribed.",
  "'Dark sodas are a better choice than soup.' || Dark sodas are high in phosphorus."],
 "The renal diet limits sodium, potassium and phosphorus, with a fluid restriction that counts fluid-containing foods.")

q("ckdmed", "A client with CKD has several new orders. Which order should the nurse question?",
 ["*Magnesium hydroxide antacid as needed",
  "Dapagliflozin to slow progression || Appropriate; SGLT2 inhibitor.",
  "Epoetin alfa for anemia || Appropriate; stimulates RBC production.",
  "An ACE inhibitor to lower glomerular pressure || Appropriate; protects the kidney."],
 "Avoid magnesium-containing antacids in kidney failure; epoetin alfa treats anemia, dapagliflozin slows CKD and ACEI/ARBs reduce intraglomerular pressure.")

q("hd", "A client has a right-arm AV fistula. Which action by assistive personnel requires the nurse to intervene?",
 ["Taking the BP on the left arm || Appropriate; avoids the access arm.",
  "*Taking the BP on the right arm",
  "Weighing the client before dialysis || Pre-dialysis weight is appropriate.",
  "Reporting bleeding at the access site || Appropriate to report."],
 "The access is a lifeline: no BP readings, needles or IVs in the access arm.")

q("hd", "Two hours into hemodialysis, a 66-year-old client becomes lightheaded and reports leg cramps. Which complication should the nurse suspect?",
 ["Peritonitis || That is a PD complication.",
  "Hypertensive crisis || BP more often drops during HD.",
  "*Hypotension",
  "Bowel perforation || That is a PD complication."],
 "Hypotension is the most common complication during or after hemodialysis; cramps, headache and nausea/vomiting can also occur.")

q("pd", "A client on CAPD asks to skip tonight's exchange to attend a family dinner. Which response by the nurse is best?",
 ["'Skipping one exchange is fine if you feel well.' || Exchanges must not be skipped.",
  "'You can do two exchanges tomorrow instead.' || PD follows a strict schedule.",
  "'PD has no schedule, so do it when convenient.' || PD requires a strict schedule.",
  "*'Exchanges can't be skipped; let's plan around dinner.'"],
 "PD offers fewer diet and fluid restrictions than HD, but it follows a strict exchange schedule and exchanges must not be skipped.")

q("wilms", "The parent of a 4-year-old with Wilms tumor asks whether the child will need radiation. Which response by the nurse is accurate?",
 ["'Every child gets radiation before the surgery.' || Radiation isn't routine for all.",
  "*'Only for inoperable or too-large tumors, not young children.'",
  "'Radiation replaces the need for surgery here.' || Nephrectomy is the usual treatment.",
  "'Radiation is never used for this kind of kidney tumor.' || It may be used in selected cases."],
 "Wilms treatment: chemotherapy and nephrectomy; radiation for inoperable or too-large tumors, avoided in young children.")

q("wilms", "A nurse is assessing a 3-year-old with suspected Wilms tumor. Which findings are consistent with this diagnosis? " + SATA,
 ["*Hematuria",
  "*Hypertension",
  "Painless jaundice || Not a Wilms finding.",
  "*Fever and poor appetite",
  "Low blood pressure || Wilms is linked to hypertension."],
 "Wilms tumor: abdominal mass, pain, hematuria, hypertension, fever, poor appetite and weight loss; lung spread causes cough or dyspnea.")

q("rcc", "A client is being evaluated for renal cell carcinoma. Which lab findings may occur? " + SATA,
 ["*Low hemoglobin and hematocrit",
  "High hemoglobin and hematocrit || H&H tends to be low.",
  "*Elevated ESR",
  "*Elevated renin or PTH",
  "Low ESR || ESR tends to be elevated."],
 "RCC labs: low H&H and elevated ESR; ACTH, hCG, cortisol, renin and PTH may be elevated.")

q("rcc", "Which presentation points to renal cell carcinoma rather than bladder cancer?",
 ["Painless blood in the urine of an older smoker || Classic for bladder cancer.",
  "Urine draining from an ileal conduit stoma || Relates to bladder cancer surgery.",
  "*Hematuria with flank pain and an abdominal mass",
  "Recurrent UTIs with diesel exposure || These are bladder cancer risks."],
 "RCC classically presents with hematuria, flank pain and an abdominal mass; painless hematuria suggests bladder cancer.")

q("bladder", "A 71-year-old client with painless hematuria is suspected of having bladder cancer. Which test should the nurse prepare the client for to diagnose it?",
 ["*Cystoscopy with biopsy",
  "Bone density scan only || Not used to diagnose bladder cancer.",
  "A fasting lipid panel || Not used to diagnose bladder cancer.",
  "Chest x-ray only || Not the diagnostic test."],
 "Bladder cancer is diagnosed with urinalysis, cystoscopy with biopsy and imaging.")
