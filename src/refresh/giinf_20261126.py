T = "giinf"; SET = "20261126"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("hh", "A 52-year-old warehouse worker is told his hiatal hernia is the type in which the fundus rolls up beside the esophagus. Which statement about this hernia is accurate?",
  ["It is a sliding hernia, the most common type || In a sliding hernia the stomach and GE junction move up; fundus beside the esophagus is rolling",
   "It is the type seen in about 95% of hiatal hernias || About 95% are sliding hernias, not rolling",
   "*It is a paraesophageal hernia and is more likely to strangulate",
   "It cannot strangulate because the junction stays put || The paraesophageal (rolling) type is the one more likely to strangulate"],
  "In a paraesophageal (rolling) hernia the fundus rolls up beside the esophagus, and it is more likely to strangulate. Sliding hernias (about 95%) move the stomach and GE junction up.")

q("hh", "A nurse at a prenatal clinic reviews hiatal hernia facts with a group. Which statements are accurate? " + SATA,
  ["*Pregnancy raises abdominal pressure and increases the risk",
   "*Sliding hernia symptoms are worse when lying flat",
   "*Regurgitation, fullness and belching are common symptoms",
   "Sitting upright after meals makes symptoms worse || Symptoms are worse lying flat and after big meals",
   "*Older age is a risk factor for a hiatal hernia"],
  "Anything that raises abdominal pressure or weakens the diaphragm (pregnancy, obesity, heavy lifting, older age) raises risk. Symptoms include heartburn, regurgitation, trouble swallowing, fullness and belching, and are worse lying flat and after big meals.")

q("hh2", "A 67-year-old retired teacher with a known hiatal hernia reports substernal chest pressure that started after dinner. What should the nurse do FIRST?",
  ["Give an antacid, since this is likely reflux pain || Hernia pain can look like heart pain, so the heart must be ruled out first",
   "Have the client lie flat until the pressure eases || Hernia symptoms worsen lying flat, and cardiac causes come first",
   "*Treat it as possible cardiac pain until a heart cause is ruled out",
   "Encourage a short walk to help the meal digest || This delays ruling out a cardiac cause of chest pain"],
  "Hiatal hernia pain can look like heart pain, so a cardiac cause must be ruled out first.")

q("hh2", "The nurse reviews self-care with a 46-year-old bus driver who has a hiatal hernia. Which client statement needs correction?",
  ["'I'll eat smaller meals more often during the day.' || Correct: small, frequent meals help",
   "'I'll stop wearing tight belts and waistbands.' || Correct: avoid tight waistbands",
   "'I'll raise the head of my bed at night.' || Correct: raising the head of the bed uses gravity against reflux",
   "*'I'll have my big meal right before I go to bed.'"],
  "Hiatal hernia care: small, frequent meals, raise the head of the bed, lose weight, avoid tight waistbands, avoid straining and heavy lifting, and stay upright 1 to 2 hours after eating.")

q("gerd", "A 38-year-old bartender with frequent heartburn asks what is actually going wrong in GERD. Which explanation is best?",
  ["'Bacteria called H. pylori are infecting your duodenum.' || H. pylori is the main cause of peptic ulcers, not GERD",
   "*'A weak lower esophageal sphincter lets stomach contents back up.'",
   "'Your stomach is not making enough intrinsic factor.' || Lack of intrinsic factor causes pernicious anemia",
   "'A blockage in your appendix is causing the burning.' || A blocked appendix causes appendicitis"],
  "In GERD a weak lower esophageal sphincter lets stomach contents flow back up, and the backflow burns the esophageal lining.")

q("gerd", "A 45-year-old with a chronic cough and hoarseness is being evaluated for GERD. Which history findings support this diagnosis? " + SATA,
  ["*A burning feeling behind the breastbone that is worse lying down",
   "*A sour taste in the mouth after large meals",
   "*A known hiatal hernia",
   "Pain that began at the navel and moved to the lower right || This pattern fits appendicitis",
   "*Several cups of coffee and some chocolate every day"],
  "GERD signs: heartburn, sour regurgitation, hoarseness, chronic cough and trouble swallowing, worse after meals and lying flat. Risk factors include hiatal hernia, obesity, smoking, alcohol, pregnancy, and chocolate, caffeine and fatty or spicy foods.")

q("gerd2", "A client with long-standing, poorly treated GERD asks why the provider is worried when the heartburn is mild. Which complication should the nurse mention?",
  ["Pernicious anemia from lost intrinsic factor || Pernicious anemia is not a GERD complication",
   "Dumping syndrome after meals || Dumping follows gastric surgery such as gastrectomy",
   "Diverticulitis in the lower left colon || Diverticulitis is a colon condition, not a GERD complication",
   "*Barrett's esophagus, a change in the esophageal lining"],
  "Untreated GERD can cause esophagitis, strictures, Barrett's esophagus, aspiration pneumonia, laryngitis and tooth enamel erosion.")

q("gerd2", "The nurse evaluates teaching for a 50-year-old office manager with GERD. Which statement needs correction?",
  ["'I'll raise the head of my bed about 30 degrees.' || Correct teaching for GERD",
   "*'A nap on the couch right after lunch should help.'",
   "'I'll keep taking my PPI even when the heartburn is gone.' || Correct: damage can continue without symptoms",
   "'I'll choose small, low-fat meals instead of large ones.' || Correct teaching for GERD"],
  "Clients with GERD should not lie down for 2 to 3 hours after eating. Raise the head of the bed about 30 degrees, eat small low-fat meals, quit smoking, lose weight, and keep taking medication as prescribed.")

q("meds", "A 59-year-old has taken omeprazole daily for 6 years and now has a fracture after a minor fall. Which long-term effect of this drug may have contributed?",
  ["Tardive dyskinesia || Tardive dyskinesia is linked to long-term metoclopramide",
   "*Weakened bones (osteoporosis)",
   "Higher warfarin levels || Cimetidine, not omeprazole, raises warfarin levels",
   "Rebound hypoglycemia || Rebound hypoglycemia follows stopping TPN suddenly"],
  "Long-term PPI use is linked to weak bones (osteoporosis) and low magnesium.")

q("meds", "A nurse compares acid-reducing drugs for a group of new graduates. Which statements are accurate? " + SATA,
  ["*Pantoprazole is taken 30 to 60 minutes before the first meal",
   "Pantoprazole neutralizes the acid already in the stomach || PPIs stop acid secretion; antacids neutralize acid",
   "*Famotidine can be taken with or without food",
   "*Famotidine blocks histamine receptors so less acid is made",
   "*Cimetidine can raise phenytoin levels"],
  "PPIs (-prazole) stop acid secretion and are taken 30 to 60 minutes before the first meal. H2 blockers such as famotidine block histamine receptors and can be taken with or without food. Cimetidine raises warfarin and phenytoin levels.")

q("meds2", "A 44-year-old starting sucralfate for an ulcer explains the drug to the nurse. Which statement shows correct understanding?",
  ["'It gets absorbed into my blood and lowers acid everywhere.' || Sucralfate isn't absorbed; it works locally",
   "'I should mix it with my antacid so they work together.' || Sucralfate is taken apart from other medications",
   "*'It forms a gel coating over the ulcer and works right there.'",
   "'I should take it in the middle of each meal.' || It is taken on an empty stomach before meals"],
  "Sucralfate forms a gel coating over the ulcer and isn't absorbed into the body. It is taken on an empty stomach before meals, spaced apart from other medications because it reduces their absorption.")

q("meds2", "While reviewing the medication list of a 70-year-old, the nurse notes metoclopramide has been taken for 4 months. What is the nurse's priority concern?",
  ["*Check for involuntary movements such as lip smacking or tongue thrusting",
   "Check the magnesium level for long-term depletion || Low magnesium is a long-term PPI effect",
   "Watch for bleeding from higher warfarin levels || That interaction belongs to cimetidine",
   "Arrange a bone density check for osteoporosis || Bone loss is a long-term PPI effect"],
  "Metoclopramide should not be used for more than 12 weeks because of the risk of tardive dyskinesia (lip smacking, tongue thrusting).")

q("barrett", "A 56-year-old man with years of poorly controlled GERD has Barrett's esophagus and asks why he needs repeat scopes. Which response is best?",
  ["'A yearly chest x-ray will work just as well.' || Barrett's is monitored with endoscopy and biopsy",
   "'Scopes are only needed if your heartburn gets worse.' || Monitoring is regular, not symptom-based",
   "'A stool test can replace the scope if you prefer.' || Stool tests are not used to monitor Barrett's",
   "*'Regular scopes with biopsy catch early cell changes.'"],
  "Barrett's esophagus raises the risk of esophageal adenocarcinoma, so it is monitored with regular endoscopy and biopsy to catch early dysplasia.")

q("gastritis", "Which statement correctly compares acute and chronic gastritis?",
  ["Acute gastritis leads to cancer; chronic resolves quickly || Reversed: chronic can lead to atrophy and higher cancer risk",
   "*Acute comes on suddenly from an irritant; chronic can cause atrophy",
   "Both types are caused by a weak lower esophageal sphincter || A weak sphincter causes GERD",
   "Chronic gastritis clears within days once alcohol stops || Acute, not chronic, usually resolves once the irritant is removed"],
  "Acute gastritis is sudden, caused by an irritant, and usually resolves once the irritant is removed. Chronic gastritis can lead to atrophy and higher cancer risk.")

q("gastritis", "A 34-year-old line cook takes naproxen daily for back pain and drinks heavily on weekends. She reports burning upper abdominal pain, nausea and feeling full quickly. Which condition does the nurse suspect?",
  ["Diverticulitis || Diverticulitis causes lower left abdominal pain with fever",
   "Appendicitis || Appendicitis pain starts at the navel and moves to the lower right",
   "*Gastritis",
   "Dumping syndrome || Dumping follows gastric surgery"],
  "NSAIDs and alcohol are causes of gastritis. Expected findings are burning epigastric pain, nausea and vomiting, early fullness and loss of appetite.")

q("gastritis2", "A 48-year-old with gastritis reports black, tarry stools since yesterday. What is the nurse's priority?",
  ["Encourage a bland diet and reassess tomorrow || Tarry stools mean GI bleeding, which needs prompt action",
   "Offer aspirin for the stomach discomfort || Aspirin is a cause of gastritis",
   "*Check vital signs and notify the provider of possible bleeding",
   "Document it as an expected gastritis finding || Black stools signal bleeding, not an expected finding"],
  "Coffee-ground emesis and black, tarry stools mean GI bleeding. Check vital signs and notify the provider right away.")

q("gastritis2", "A 29-year-old graduate student with gastritis reviews her plan. Which statements show correct understanding? " + SATA,
  ["*'I'll keep a food diary to see what bothers me.'",
   "*'I'll stop having a snack right before bed.'",
   "'I'll take aspirin when my stomach starts to hurt.' || Aspirin and NSAIDs cause gastritis",
   "*'I'll cut back on caffeine and quit smoking.'",
   "'Large, high-fat meals will help settle my stomach.' || Small, bland meals are recommended"],
  "Gastritis teaching: keep a food diary, eat small bland meals, avoid bedtime snacks, avoid alcohol, caffeine and smoking, lower stress, and stop the cause such as NSAIDs. Treat H. pylori if present.")

q("pud", "The nurse is sorting ulcer findings. Which findings point to a GASTRIC rather than a duodenal ulcer? " + SATA,
  ["*Pain worsens 30 to 60 minutes after eating",
   "Pain is relieved when the client eats || Food relief is typical of a duodenal ulcer",
   "Pain often wakes the client at night || Night pain is common with duodenal ulcers",
   "*Weight loss because eating causes pain",
   "Pain returns 2 to 3 hours after a meal || This pattern fits a duodenal ulcer"],
  "Gastric ulcer pain worsens 30 to 60 minutes after eating, so clients lose weight. Duodenal ulcer pain is relieved by food, returns 2 to 3 hours later, and often occurs at night.")

q("pud", "A client in the burn unit develops a peptic ulcer during recovery from extensive burns. What is this type of ulcer called?",
  ["Cushing's ulcer || Cushing's ulcers are stress ulcers after head injury",
   "Barrett's ulcer || Barrett's esophagus is a lining change from GERD",
   "Gastric ulcer from a hiatal hernia || A hiatal hernia is not a listed ulcer cause",
   "*Curling's ulcer, a type of stress ulcer"],
  "Curling's ulcers (burns) and Cushing's ulcers (head injury) are stress ulcers. Peptic ulcers form when acid outmatches the lining's defenses.")

q("pud2", "The nurse is caring for a client with peptic ulcer disease. Which findings should be reported promptly? " + SATA,
  ["*Vomiting blood",
   "*Black stools",
   "*Sudden severe pain with a hard, board-like abdomen",
   "Pain felt at McBurney's point || McBurney's point pain points to appendicitis",
   "*Signs of obstruction"],
  "PUD complications are bleeding (bloody vomit or black stools), perforation (sudden severe pain, board-like abdomen) and obstruction. Perforation is a surgical emergency.")

q("pud2", "A 37-year-old with an H. pylori ulcer asks why the treatment involves so many pills. Which response is best?",
  ["'Antacids alone will heal it, so the rest are optional.' || Antacids alone don't treat H. pylori",
   "*'Triple or quadruple therapy plus a PPI treats the infection.'",
   "'The extra pills prepare you for the surgery every ulcer needs.' || Not every ulcer needs surgery",
   "'NSAIDs are included to control the ulcer pain.' || NSAIDs are a major ulcer cause and are avoided"],
  "An H. pylori ulcer is treated with triple or quadruple therapy plus a PPI. Avoid NSAIDs, alcohol and smoking, and monitor for bleeding, perforation and obstruction.")

q("gcancer", "A 66-year-old fisherman eats salted and smoked foods daily and has had H. pylori. Which reports raise concern for gastric cancer? " + SATA,
  ["*Feeling full after only a few bites",
   "*Losing weight without trying",
   "*Months of vague indigestion",
   "*Fatigue with a low blood count (anemia)",
   "Lower left abdominal pain with fever || This fits diverticulitis"],
  "Gastric cancer signs are vague indigestion, early fullness, unplanned weight loss, anemia and epigastric pain. Risks include H. pylori, smoked, salted or preserved foods, smoking and pernicious anemia.")

q("gcancer", "Why is gastric cancer often diagnosed at a late stage?",
  ["Endoscopy with biopsy cannot detect it || Upper endoscopy with biopsy is how it is diagnosed",
   "Its first sign is usually a rigid abdomen || A rigid abdomen suggests perforation or peritonitis",
   "*Early signs are vague, such as indigestion",
   "It only causes symptoms after a gastrectomy || Symptoms occur before surgery; surgery is treatment"],
  "Early gastric cancer signs are vague, so it is often found late. Diagnosis is by upper endoscopy with biopsy, followed by CT staging.")

q("enteral", "A client with an established feeding tube is due for medications. Which nursing actions are correct? " + SATA,
  ["*Check the pH of the aspirate before use",
   "*Check the tube markings before use",
   "*Flush the tube before and after the medications",
   "Lower the head of the bed flat during the medication || Keep the head of the bed at least 30 degrees",
   "Rely on an air bolus sound as the only check || Placement checks are pH and tube markings after the first x-ray"],
  "Placement is first confirmed by x-ray; after that, check gastric pH (under 5 supports placement) and the tube markings before each use. Flush before and after feeds and meds, and keep the head of the bed at least 30 degrees.")

q("tpn", "A client receiving TPN through a central line has a new order for an IV antibiotic. What should the nurse do?",
  ["Piggyback the antibiotic into the TPN tubing || TPN needs a dedicated line",
   "Stop the TPN suddenly and use its line for the dose || Never stop TPN suddenly, and the line is dedicated",
   "Add the antibiotic directly into the TPN bag || The TPN line and bag are used for TPN only",
   "*Give the antibiotic through a separate line, not the TPN line"],
  "TPN care: strict aseptic technique, a dedicated line, regular blood glucose checks, and tapering rather than stopping suddenly.")

q("tpn", "A 33-year-old has received TPN for 2 weeks. Which complications should the nurse monitor for? " + SATA,
  ["*High blood glucose",
   "Tardive dyskinesia || This is linked to long-term metoclopramide",
   "*Low blood glucose if the infusion stops suddenly",
   "*Fever and redness at the central line site",
   "*Fluid overload"],
  "TPN complications include high or low glucose, line infection (a sepsis risk) and fluid overload. Never stop TPN suddenly because of rebound hypoglycemia.")

q("dumping", "A 58-year-old had a gastric bypass and is learning to prevent dumping syndrome. Which statement needs correction?",
  ["'I'll lie down for 20 to 30 minutes after I eat.' || Correct: lying down after eating helps",
   "'I'll wait 30 to 45 minutes between liquids and solids.' || Correct: separate liquids from solids",
   "*'I'll drink a big glass of sweet juice with each meal.'",
   "'I'll add more protein and fat to my meals.' || Correct: more protein and fat helps"],
  "Prevent dumping with small, frequent meals, avoiding sweets and simple sugars, separating liquids from solids by 30 to 45 minutes, lying down 20 to 30 minutes after eating, and more protein and fat.")

q("pernicious", "A 72-year-old who had a gastrectomy years ago has tingling feet, poor balance and a smooth, beefy red tongue. Which lab pattern does the nurse expect?",
  ["High vitamin B12 with a low MCV || Reversed: B12 is low and MCV is high",
   "High vitamin B12 with a high MCV || B12 is low in pernicious anemia",
   "*Low vitamin B12 with a high MCV",
   "Low vitamin B12 with a low MCV || MCV is high in pernicious anemia"],
  "Without intrinsic factor (autoimmune, gastrectomy, atrophic gastritis), B12 can't be absorbed. Labs show low B12 and high MCV; findings include a beefy red tongue, tingling and balance problems.")

q("gastro", "Several toddlers at a daycare develop vomiting and diarrhea from norovirus. One is admitted. Which nursing actions are appropriate? " + SATA,
  ["*Use contact precautions",
   "*Perform careful hand hygiene",
   "Use airborne precautions || Infectious gastroenteritis needs contact precautions",
   "*Monitor for dry mouth and less urine",
   "Start a high-fiber diet first || Replacing fluids and electrolytes is the priority"],
  "Infectious gastroenteritis needs contact precautions and hand hygiene. Fluid loss is the main danger, so replace fluids and electrolytes; young children and older adults are at highest risk.")

q("append", "A 19-year-old college student has nausea, no appetite, and pain that began around the navel. Where does the nurse expect the pain to settle if this is appendicitis?",
  ["In the right upper quadrant under the ribs || That area is checked for Murphy's sign (cholecystitis)",
   "In the lower left quadrant near the hip || Lower left pain fits diverticulitis",
   "Behind the breastbone after meals || Burning behind the breastbone is GERD heartburn",
   "*At McBurney's point in the right lower quadrant"],
  "Classic appendicitis pain starts at the belly button and moves to McBurney's point in the RLQ, with loss of appetite, nausea and low-grade fever.")

q("append", "A client is admitted with suspected appendicitis. Which diagnostic tests does the nurse anticipate? " + SATA,
  ["*CT scan",
   "HIDA scan || A HIDA scan is not used to diagnose appendicitis",
   "*Ultrasound",
   "ERCP || ERCP is not used to diagnose appendicitis",
   "Upper endoscopy || Upper endoscopy is not used to diagnose appendicitis"],
  "Appendicitis is diagnosed with a CT scan or ultrasound, and treatment is an appendectomy.")

q("append2", "A 27-year-old is awaiting surgery for suspected appendicitis. Which nursing actions are appropriate? " + SATA,
  ["*Keep the client NPO",
   "*Watch the pain trend for a sudden drop in pain",
   "Give a prescribed bisacodyl laxative for constipation || Laxatives can cause rupture",
   "*Report a rigid abdomen with a rising fever right away",
   "Apply a warm pack to the lower right abdomen || Heat can cause rupture"],
  "With suspected appendicitis: keep NPO, prepare for surgery and watch the pain trend. Never use heat, laxatives or enemas. Sudden pain relief suggests rupture; a rigid abdomen and rising fever suggest peritonitis.")

q("append2", "A nurse teaches a student when an inflamed appendix is most likely to rupture. Which time frame is correct?",
  ["Within the first hour of pain || The highest-risk window is 24 to 72 hours",
   "*24 to 72 hours after symptoms start",
   "Only after a full week of symptoms || The highest-risk window is 24 to 72 hours",
   "Only after an enema is given || Enemas raise rupture risk but do not define the time window"],
  "Rupture risk is highest 24 to 72 hours after symptoms start. A sudden drop in pain suggests rupture.")

q("divert", "A 61-year-old office worker is recovering from a diverticulitis flare. Which statement shows correct understanding?",
  ["'I'll eat high-fiber foods during my next flare.' || During a flare the bowel is rested (NPO or clear liquids)",
   "'I'll stay on a low-fiber diet from now on.' || High fiber prevents flares once the flare resolves",
   "*'Once I'm healed, I'll eat high fiber and avoid straining.'",
   "'Smoking and sitting all day won't affect my colon.' || Avoid smoking and a sedentary life"],
  "During a flare, rest the bowel (NPO or clear liquids) with IV antibiotics. After it resolves, a high-fiber diet prevents flares; also avoid straining, smoking and a sedentary life.")

q("perf", "A client with a peptic ulcer has sudden severe pain, a rigid abdomen, HR 122 and BP 88/50. Free air is seen under the diaphragm. What should the nurse anticipate?",
  ["Giving a PPI and rechecking in 4 hours || Perforation needs emergency surgery, not watchful waiting",
   "*Keeping the client NPO and preparing for emergency surgery",
   "Offering clear liquids to replace lost fluid || The client must stay NPO",
   "Giving a laxative to move stool along || Laxatives are not part of perforation care"],
  "Free air under the diaphragm confirms perforation, which needs emergency surgery: notify the provider, keep NPO, start IV fluids and antibiotics, insert an NG tube, and check vitals often for shock.")

q("periton", "The nurse reviews four clients. Which clients have a listed cause of peritonitis? " + SATA,
  ["*A client with an infection related to dialysis",
   "*A client with a perforated peptic ulcer",
   "A client with a sliding hiatal hernia || A hiatal hernia is not a listed peritonitis cause",
   "*A client whose appendix has ruptured",
   "A client with mild GERD || GERD alone is not a listed cause"],
  "Peritonitis causes include perforation, a ruptured appendix and dialysis infection. It can quickly become sepsis.")

q("sepsis", "A client with peritonitis has a temperature of 39 C, HR 118, RR 26 and new confusion. Sepsis orders are received. Which order of actions is correct?",
  ["Antibiotics first, then blood cultures, then fluids || Cultures are drawn before antibiotics",
   "IV fluids, then wait for culture results before antibiotics || Antibiotics are due within 1 hour, not after results",
   "*Blood cultures, then antibiotics within 1 hour, then fluids",
   "Vasopressors first, then cultures and antibiotics || The bundle starts with cultures"],
  "The 1-hour sepsis bundle: blood cultures, then antibiotics within 1 hour, then fluids.")

q("signs", "While palpating the right upper abdomen of a 44-year-old, the nurse notices the client abruptly stops breathing in. Which condition does this finding suggest?",
  ["*Cholecystitis",
   "Appendicitis || Appendicitis pain is at McBurney's point in the RLQ",
   "Pancreatitis || Cullen's sign, not Murphy's sign, relates to pancreatitis",
   "Diverticulitis || Diverticulitis causes lower left abdominal pain"],
  "A positive Murphy's sign (stopping inspiration when the RUQ is pressed) suggests cholecystitis. Murphy = upper (gallbladder).")

q("signs", "A nursing student says, 'McBurney's point is in the upper right abdomen and means gallbladder disease.' Which correction is accurate?",
  ["'Murphy's sign is in the lower right and means appendicitis.' || Murphy's sign is upper right, for cholecystitis",
   "'McBurney's point is in the lower left and means diverticulitis.' || McBurney's point is in the lower right",
   "'McBurney's point is in the upper left and means gastritis.' || McBurney's point is in the lower right",
   "*'McBurney's point is lower right, between navel and hip, for appendicitis.'"],
  "McBurney's point is in the RLQ halfway between the belly button and the hip bone (appendicitis). Murphy's sign is checked in the RUQ (cholecystitis).")
