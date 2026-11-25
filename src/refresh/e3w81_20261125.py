T = "e3w81"; SET = "20261125"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("hydro", "An ultrasound confirms hydronephrosis from a ureteral stricture. Which actions belong in the plan of care? " + SATA,
  ["*Relieve the obstruction",
   "*Control the client's pain",
   "Restrict fluids to rest the kidney || Not part of hydronephrosis care",
   "*Give antibiotics if infection is present",
   "*Monitor BUN and creatinine"],
  "Hydronephrosis care: identify and relieve the obstruction, pain control, antibiotics if infected, and monitor kidney function.")

q("stones", "A client's passed stone is analyzed and found to be struvite. Which history does the nurse expect?",
  ["Gout with high uric acid || Gout is linked to uric acid stones",
   "*Recurrent urinary tract infections",
   "An inherited condition called cystinuria || Cystinuria causes cystine stones",
   "A diet high in oxalate-rich foods || Oxalate is linked to calcium oxalate stones"],
  "Calcium ~80% (oxalate/diet). Struvite ~10% (UTI). Uric acid ~9% (gout). Cystine ~1% (inherited cystinuria).")

q("stoneloc", "A client arrives with suspected renal colic. Which imaging studies does the nurse anticipate for a kidney stone? " + SATA,
  ["*CT without contrast",
   "*Ultrasound",
   "Bone scan || Used to evaluate prostate cancer spread",
   "*KUB x-ray",
   "Contrast IVP || Not a listed stone study"],
  "Imaging for stones: CT without contrast, ultrasound and KUB.")

q("stonetx", "A client with a small ureteral stone is managed conservatively. Which order should the nurse question?",
  ["Strain all urine and save any stone || Expected conservative care",
   "Tamsulosin to aid stone passage || Expected conservative care",
   "*Restrict fluids to 500 mL per day",
   "NSAIDs or opioids for pain || Expected conservative care"],
  "Conservative stone care: hydrate as ordered (slides: 2-3 L/day), analgesics, tamsulosin, strain all urine and save the stone.")

q("stonetx", "A client returns from percutaneous nephrolithotomy for a large, complex stone. What should the nurse monitor closely?",
  ["Cardiac rhythm for shock-wave dysrhythmias || Cardiac monitoring is emphasized during ESWL",
   "Continuous bladder irrigation color || CBI is used after TURP",
   "*The tube and signs of bleeding",
   "Stoma color and shape || PCNL monitoring is the tube and bleeding"],
  "PCNL uses a small back incision for large or complex stones; monitor the tube and bleeding.")

q("stoneteach", "A client recovering from a kidney stone reviews prevention teaching. Which statement needs MORE teaching?",
  ["'I'll cut back on soda and excessive red meat.' || Correct professor teaching",
   "'My diet changes will depend on my stone type.' || Correct; diet is adjusted by stone type",
   "'I'll drink the fluids my provider recommends.' || Correct; hydration prevents stones",
   "*'Once I pass this stone, I won't need any follow-up.'"],
  "Prevention: hydration, diet by stone type, avoid excess salt, oxalate guidance for calcium oxalate stones, and keep follow-up.")

q("bph", "During a digital rectal exam on a client with urinary symptoms, the provider feels a hard nodule on the prostate. How should the nurse interpret this?",
  ["*It suggests prostate cancer and needs further evaluation",
   "It is the typical finding of BPH || BPH feels smooth and enlarged",
   "It confirms a urinary tract infection || DRE does not diagnose infection",
   "It means the prostate is shrinking from medication || Nodules suggest cancer"],
  "BPH: smooth, enlarged prostate. Nodules or hard areas suggest prostate cancer; PSA assesses for cancer and biopsy confirms.")

q("bph", "A 68-year-old client with BPH reports getting up 3 times a night to void and sudden strong urges during the day. How does the nurse classify these symptoms?",
  ["Obstructive symptoms || Obstructive: hesitancy, weak stream, straining, dribbling, incomplete emptying",
   "Signs of prostate cancer spread || New back or pelvic pain suggests spread",
   "*Irritative symptoms",
   "Signs of hydronephrosis || Hydronephrosis causes flank pain and reduced urine output"],
  "BPH irritative symptoms: urgency, frequency, nocturia. Obstructive: hesitancy, weak stream, straining, dribbling, incomplete emptying.")

q("bphmed", "Which pairing of BPH medication and action is correct?",
  ["Terazosin — shrinks the prostate over months || Terazosin is an alpha blocker that relaxes",
   "*Dutasteride — shrinks the prostate over time",
   "Finasteride — relaxes smooth muscle for fast relief || Finasteride shrinks the prostate slowly",
   "Tamsulosin — a 5-alpha reductase inhibitor || Tamsulosin is an alpha blocker"],
  "Alpha blockers (tamsulosin, terazosin) RELAX. 5-alpha reductase inhibitors (finasteride, dutasteride) SHRINK the prostate over time.")

q("turp", "A client is on continuous bladder irrigation after TURP. The drainage is light pink with no clots. What should the nurse do?",
  ["Increase the irrigation rate per protocol || Increase for darker drainage or small clots",
   "Stop the irrigation since bleeding has ended || Continuous flow prevents clots and keeps the catheter patent",
   "*Keep the current rate and continue monitoring",
   "Notify the provider of active bleeding || Light pink is at the goal"],
  "CBI goal: light pink to clear. Darker drainage or small clots: increase irrigation per protocol. Persistent bright red or large clots: assess and notify.")

q("turp", "The nurse gives discharge teaching to a client after TURP. Which instructions are correct? " + SATA,
  ["*Avoid straining",
   "*Avoid heavy lifting",
   "Resume weightlifting the next day || Avoid strenuous exercise per instructions",
   "*Avoid NSAIDs unless approved",
   "*Watch for bleeding or infection"],
  "After TURP: avoid straining, heavy lifting and strenuous exercise; avoid NSAIDs unless approved due to bleeding risk; monitor bleeding and infection.")

q("pca", "A client's PSA level comes back elevated. He asks, 'Does this mean I have prostate cancer?' Which response is best?",
  ["'Yes, an elevated PSA confirms prostate cancer.' || PSA may be elevated but doesn't confirm",
   "'No, a urinalysis is what confirms the diagnosis.' || Biopsy confirms cancer",
   "'Yes, and a Gleason score will show how far it spread.' || Stage describes spread; Gleason describes aggressiveness",
   "*'A biopsy is needed to confirm whether cancer is present.'"],
  "DRE may find nodules; PSA may be elevated; biopsy confirms prostate cancer. MRI/CT/bone scan evaluate spread.")
