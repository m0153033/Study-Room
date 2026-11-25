T = "e3w62"; SET = "20261125"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("perf", "The nurse checks capillary refill on a client with an aortic aneurysm. Which part of perfusion does this finding reflect?",
 ["Renal perfusion || Urine output reflects the kidneys.",
  "Cerebral perfusion || Mentation reflects the brain.",
  "*Peripheral perfusion",
  "Cardiac output alone || Cardiac output = heart rate × stroke volume."],
 "Cap refill under 3 seconds = peripheral perfusion; urine output = renal; mentation = cerebral.")

q("types", "Which vascular finding is an acute, highly lethal emergency?",
 ["A stable 4.0 cm fusiform AAA on surveillance || Watchful waiting.",
  "*An intimal tear with blood forming a false lumen",
  "A popliteal aneurysm with a strong pedal pulse || Expected finding.",
  "A pulsatile groin mass after femoral line removal || Pseudoaneurysm contained by tissue."],
 "Dissection = intimal tear + false lumen; an acute, highly lethal emergency. Aneurysm = dilation.")

q("laplace", "A client with a 5.0 cm AAA asks why the nurse keeps checking and treating the blood pressure. Best response?",
 ["'Lower pressure will shrink the aneurysm back to normal.' || It lowers tension, not size.",
  "'Blood pressure doesn't affect the aneurysm wall.' || Pressure raises wall tension.",
  "'Higher pressure makes the wall stronger.' || Higher pressure raises rupture risk.",
  "*'Higher pressure raises tension on the aneurysm wall.'"],
 "Laplace: wall tension = pressure × radius. Lowering pressure lowers wall tension, slowing growth and rupture risk.")

q("risk", "A 58-year-old woman with Ehlers-Danlos syndrome and a family history of aneurysm is obese, inactive and uses methamphetamine. Which risk factors are modifiable? " + SATA,
 ["*Methamphetamine use",
  "Ehlers-Danlos syndrome || Connective tissue disease is non-modifiable.",
  "*Obesity",
  "Family history of aneurysm || Non-modifiable.",
  "*Sedentary lifestyle"],
 "Modifiable: smoking, HTN, hyperlipidemia, stimulants, obesity, inactivity. Non-modifiable: age, sex, family history, connective tissue disease.")

q("aaa", "A nursing student prepares to palpate deeply to measure the width of a client's known AAA. What should the nurse say?",
 ["'Go ahead; it helps track the size.' || Imaging tracks size.",
  "*'Stop; deep palpation can cause the aneurysm to rupture.'",
  "'Press harder so you can feel the edges.' || Never palpate deeply.",
  "'Palpate it every shift to watch for growth.' || Avoid repeated palpation."],
 "Do NOT deeply or repeatedly palpate a suspected or known AAA; it can precipitate rupture.")

q("taa", "A client with a thoracic aortic aneurysm reports new shortness of breath. Which explanation is most likely?",
 ["The aneurysm is compressing the laryngeal nerve || That causes hoarseness.",
  "The aneurysm is compressing the esophagus || That causes dysphagia.",
  "*The aneurysm is pressing on the airway",
  "A popliteal aneurysm has formed || Unrelated to breathing."],
 "TAA compression: hoarseness (laryngeal nerve), dysphagia (esophagus), dyspnea (airway).")

q("pop", "The nurse assesses the limb below a client's popliteal aneurysm. Which assessments are appropriate? " + SATA,
 ["*Pedal pulses",
  "*Skin color and temperature",
  "Blood pressure in both arms || Used for thoracic aneurysm/dissection.",
  "*Capillary refill and sensation",
  "Bowel sounds in four quadrants || Not downstream of the knee."],
 "Think downstream perfusion: color, temperature, cap refill, sensation and pulses distal to the aneurysm.")

q("pop", "A nurse cares for four clients with popliteal aneurysms. Which client should the nurse see FIRST?",
 ["Client with pulsatile masses behind both knees || Expected; often bilateral.",
  "Client with lower-leg edema and a strong pedal pulse || Vein compression; less urgent.",
  "*Client with a suddenly pale, cool foot and no pedal pulse",
  "Client with foot numbness and a strong pedal pulse || Nerve compression; less urgent."],
 "Mural thrombus can cause arterial occlusion: pain, pallor, absent pulse and limb ischemia. Emergency; risk of limb loss.")

q("dx", "A client asks why ultrasound, not CT angiography, is used to follow a small AAA. Best response?",
 ["'Ultrasound is the gold standard for surgical planning.' || That is CT angiography.",
  "'Ultrasound requires contrast dye.' || No contrast is used.",
  "'Ultrasound needs you to be NPO and sedated.' || That describes TEE.",
  "*'Ultrasound is noninvasive, uses no contrast and is used for follow-up.'"],
 "Abdominal ultrasound: noninvasive, no contrast, used for screening and surveillance. CT angiography is the gold standard for size, shape and surgical planning.")

q("rupture", "A client with a known AAA had BP 134/78 an hour ago. Now BP is 92/76, pulse pressure is narrow, urine output has dropped and the client is confused. Which stage of shock does this suggest?",
 ["Early compensated shock || Early shock has a normal BP.",
  "*Progressive shock",
  "Irreversible shock || Profound hypotension, anuria and multi-organ failure.",
  "No shock; this is anxiety || Falling BP and confusion signal shock."],
 "Progressive: hypotension, narrow pulse pressure, oliguria, confusion. Early: restlessness, tachycardia, normal BP. Irreversible: anuria, MODS.")

q("rupture", "Which finding would the nurse expect in a client whose aneurysm is still INTACT rather than ruptured?",
 ["*Warm, dry skin with alert mentation",
  "Cool, pale, diaphoretic skin || Suggests rupture.",
  "Flank ecchymosis || Suggests retroperitoneal bleeding.",
  "Thready pulse with narrowing pulse pressure || Suggests hemorrhagic shock."],
 "Intact: warm/dry, alert, often hypertensive. Ruptured: tearing pain, hypotension, narrow pulse pressure, tachycardia, cool/pale/diaphoretic skin.")

q("medmgmt", "A client with a stable 4.5 cm AAA takes labetalol. Today's SBP is 112 and HR is 66. How does the nurse interpret these values?",
 ["SBP should be lowered to 80–90 || That permissive range is for rupture.",
  "HR is too low and the drug should be stopped || Don't stop a beta blocker abruptly.",
  "*Both values are within the course targets",
  "SBP should be raised above 140 || Target is about 100–120."],
 "Stable aneurysm targets: SBP about 100–120 and HR 60–70 with beta blockers first line.")

q("repair", "Which statement by a client 2 days after EVAR shows understanding of follow-up care?",
 ["'Once I go home, I won't need more scans.' || Surveillance is lifelong.",
  "*'I'll need imaging for life to check for an endoleak.'",
  "'My main risk is ischemia from the aortic cross-clamp.' || That is open repair.",
  "'My incision runs down my abdomen.' || EVAR uses the femoral artery."],
 "EVAR: stent graft through the femoral artery; endoleak (persistent flow into the sac) requires lifelong surveillance imaging.")

q("repair", "A client's vessel anatomy is not suitable for EVAR, so open repair is planned. What should the nurse watch MORE closely after this surgery?",
 ["Endoleak only || That is the EVAR complication.",
  "Hoarseness only || Not the focus after open repair.",
  "Nothing extra; care is the same as EVAR || Open repair is more invasive.",
  "*Organ ischemia and significant blood loss"],
 "Open repair: aorta cross-clamped, more blood loss, longer ICU stay; watch kidney, bowel and spinal cord ischemia.")

q("preop", "A client with a symptomatic AAA awaiting repair is in acute pain and wants to walk to the bathroom. Which response is best?",
 ["'Walking will help ease the pain.' || Bed rest during acute pain.",
  "'Bear down hard if you need to have a bowel movement.' || Avoid Valsalva.",
  "*'Please stay in bed for now; I'll bring what you need.'",
  "'You can walk once I check your BP.' || Bed rest during acute pain."],
 "Pre-op: keep the client calm, bed rest during acute pain, treat pain and anxiety and avoid Valsalva.")

q("postop", "After aneurysm repair, the client's BP is 84/50, below the ordered window. Why is this a concern for the graft?",
 ["*Hypotension risks graft thrombosis",
  "Hypotension stresses the suture lines || High BP stresses the graft.",
  "Low BP causes an endoleak || Endoleak is flow into the sac after EVAR.",
  "Low BP is the post-op goal || Keep BP within the ordered window."],
 "Keep BP in the ordered window: hypertension stresses the graft; hypotension risks graft thrombosis.")

q("postop", "Which post-op findings after aneurysm repair suggest bleeding? " + SATA,
 ["*Increasing abdominal girth",
  "Strong, equal pedal pulses || Normal finding.",
  "*Downward hemoglobin trend",
  "*New back or groin pain",
  "Using the incentive spirometer well || Expected pulmonary care."],
 "Watch dressings, drains, girth, back/groin pain and the Hgb trend for bleeding.")

q("teach", "A client being discharged after aneurysm repair makes four statements. Which needs correction?",
 ["'I'll keep a BP log and bring it to visits.' || Correct teaching.",
  "'I won't lift more than 10–15 pounds for a while.' || Correct teaching.",
  "'I'll keep every surveillance imaging appointment.' || Correct teaching.",
  "*'If I faint, I'll rest and call my doctor next week.'"],
 "Call 911 for sudden severe tearing pain, fainting or a new pulsating sensation.")
