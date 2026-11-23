# Week 14.1 Immunity: Ulcerative Colitis & Crohn Disease — lecture PowerPoint (main) + updated notes after the 11/23 lecture.
EXAM = "e5"
T = "e5ibd"
CONCEPTS = {
 "overview":"IBS vs IBD",
 "immune":"Immunity, autoimmune triggers & interrelated concepts",
 "compare":"UC vs Crohn's: the differences",
 "ucassess":"UC findings",
 "megacolon":"UC complications & toxic megacolon",
 "cdassess":"Crohn's findings & complications",
 "dx":"Diagnostics",
 "fe":"Fluid & electrolyte losses",
 "nursing":"Acute flare: nursing priorities",
 "steroid":"Corticosteroids for acute flares",
 "asa":"5-ASA maintenance drugs",
 "immuno":"Immunomodulators vs biologics",
 "bio":"Biologics",
 "nutri":"Diet: remission vs flare",
 "tpn":"Total parenteral nutrition (TPN)",
 "surg":"Surgery: Crohn's vs UC",
 "health":"Health promotion, cancer screening & psychosocial support",
}
HI = ["compare","megacolon","cdassess","ucassess","surg","asa","nursing","bio","tpn","nutri"]
# Updated lecture leaves these out. Don't write questions on them:
NOT_TESTED = ["'lead-pipe' colon / haustra", "stool-count severity grading (mild vs severe UC)", "vitamin B12 / bile salt absorption",
 "smoking lowering UC risk", "drugs not on the lecture slide (balsalazide, olsalazine, budesonide, infliximab for IBD, certolizumab, golimumab, natalizumab, tofacitinib, antibiotics)",
 "strictureplasty, continent ileostomy", "lifespan (teens, older adults, pregnancy)"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- IBS vs IBD ----------
q("overview","Which statements correctly compare irritable bowel syndrome (IBS) and inflammatory bowel disease (IBD)? "+SATA,
 ["*IBS is a functional GI disorder; IBD is an autoimmune disease","*IBS shows no abnormalities when the colon is examined; IBD causes permanent structural changes","*IBD increases colon cancer risk; IBS does not","IBS increases colon cancer risk; IBD does not || Reversed.","Both cause permanent bowel damage || Only IBD does."],
 "IBS = symptoms without structural damage. IBD = chronic inflammation with tissue injury.")
q("overview","A client with IBS asks whether they will need frequent hospital stays like their cousin with Crohn's. Best response?",
 ["*'IBS treatment is symptom management; IBD more often leads to hospital admissions.'","'Yes, IBS damages the bowel the same way.' || IBS causes no structural damage.","'IBS always turns into Crohn's.' || Not true.","'IBS needs biologics for life.' || Symptom management."],
 "IBD treatment aims to maintain remission and limit exacerbations.")
q("overview","Which symptoms fit IBS rather than IBD?",
 ["*Episodes of diarrhea and/or constipation with pain, gas and distention","Bloody stools with nutritional deficits || IBD.","Fistulas and strictures || Crohn's.","Toxic megacolon || UC."],
 "IBS-D = diarrhea type; IBS-C = constipation type.")

# ---------- immunity ----------
q("immune","Why is IBD classified as an autoimmune disease?",
 ["*The immune system can't tell 'self' from 'non-self' and attacks the bowel","The immune response is too weak || That's immunosuppression.","A bacteria permanently infects the bowel || Not the definition.","It's caused only by diet || Not the definition."],
 "Too little response = immunosuppressed; too much = autoimmune.")
q("immune","Which factors can contribute to developing an autoimmune disease like IBD? "+SATA,
 ["*Genetic or family predisposition","*An existing autoimmune condition","*Female gender","*Environmental triggers such as smoking, stress, infection or chemical exposure","Regular exercise || Not a listed trigger."],
 "Viral and bacterial infections can overstimulate the immune system.")
q("immune","Which interrelated concepts does the lecture link to UC and Crohn's? "+SATA,
 ["*Inflammation","*Fluid and electrolytes","*Nutrition","*Teamwork and collaboration","*Health promotion","Mobility || Not on the concept map."],
 "Immunity is the central concept.")

# ---------- compare ----------
q("compare","Which pairings correctly compare UC and Crohn's? "+SATA,
 ["*UC: continuous; Crohn's: patchy skip lesions","*UC: mucosal layer; Crohn's: all layers (transmural)","*UC: rectum to colon only; Crohn's: entire GI tract ('gum to bum')","*UC: ulcerative appearance; Crohn's: cobblestone appearance","UC: right lower abdominal pain; Crohn's: left lower || Reversed."],
 "Both usually start between ages 15 and 35.")
q("compare","A client has frequent stools with blood and mucus, urgency and left lower abdominal cramping. Which condition fits best?",
 ["*Ulcerative colitis","Crohn's disease || Loose, watery, greasy stools; right lower pain.","Irritable bowel syndrome || No bleeding or inflammation.","Bowel obstruction || Distention and vomiting."],
 "UC = continuous colon/rectum mucosal disease with bloody stools.")
q("compare","A client has loose, watery, greasy stools, right lower abdominal pain, weight loss and a fistula. Which condition fits best?",
 ["*Crohn's disease","Ulcerative colitis || Bloody mucus stools; no fistulas.","Irritable bowel syndrome || No fistulas.","Toxic megacolon || UC complication."],
 "Crohn's = strictures, fistulas, abscesses.")
q("compare","Which features do UC and Crohn's SHARE? "+SATA,
 ["*Nutritional deficits, anemia and weight loss","*Increased colon cancer risk","*Systemic complications","*Typical onset around ages 15–35","Continuous distribution || UC only."],
 "Same immune cause, different pattern and depth.")

# ---------- UC findings ----------
q("ucassess","Which findings are typical of ulcerative colitis? "+SATA,
 ["*Frequent stools with blood and mucus","*Abdominal cramps and urgency","*Left lower abdominal pain","*Anemia and weight loss","Fistula draining to the skin || Crohn's."],
 "Inflammation is in the mucosal layer of the rectum and colon.")
q("ucassess","Where does ulcerative colitis begin and how does it spread?",
 ["*It begins in the rectum and spreads continuously through the colon","It starts in the mouth and skips areas || Crohn's.","It affects only the small intestine || Not UC.","It forms patches anywhere in the GI tract || Crohn's."],
 "UC = rectum to colon only.")

# ---------- UC complications ----------
q("megacolon","Which are complications of ulcerative colitis? "+SATA,
 ["*Hemorrhage","*Perforation","*Toxic megacolon","*Colorectal cancer","Fistulas and abscesses || Crohn's."],
 "Keep colorectal cancer screening on schedule.")
q("megacolon","A client with a severe UC flare suddenly develops marked abdominal distention, fever and tachycardia. Which action is the priority?",
 ["*Report it immediately as possible toxic megacolon/perforation","Give an antidiarrheal and recheck in 4 hours || Antidiarrheals can worsen it.","Encourage a high-fiber meal || Not during a flare.","Document as an expected flare || It's an emergency."],
 "Report gross bleeding, severe pain or distention, fever or signs of shock.")
q("megacolon","Why does the lecture say to use CAUTION with antidiarrheal medication in IBD?",
 ["*They can be dangerous in severe UC or suspected toxic megacolon","They cure the disease too quickly || Not true.","They cause bloody stools || Not the reason.","They interact with all foods || Not the reason."],
 "New distention or constipation may signal obstruction.")

# ---------- Crohn's findings ----------
q("cdassess","Which findings are typical of Crohn's disease? "+SATA,
 ["*Loose, watery or greasy stools","*Abdominal pain, often right lower","*Patchy skip lesions anywhere in the GI tract","*Malabsorption and weight loss","Continuous inflammation starting at the rectum || UC."],
 "Blood is less typical than in UC.")
q("cdassess","Which are complications of Crohn's disease? "+SATA,
 ["*Strictures","*Obstruction","*Fistulas","*Abscesses","Toxic megacolon || UC."],
 "Transmural inflammation affects every layer of the bowel wall.")
q("cdassess","Why can Crohn's disease cause fistulas and strictures while UC usually doesn't?",
 ["*Crohn's inflammation goes through all layers of the bowel wall","Crohn's only affects the mucosa || That's UC.","Crohn's is limited to the rectum || Not true.","Crohn's is a functional disorder || That's IBS."],
 "Transmural = full thickness.")
q("cdassess","A client with Crohn's reports cramping, vomiting and new abdominal distention with no stool. What should the nurse suspect?",
 ["*Bowel obstruction from a stricture","Expected remission || Not remission.","Toxic megacolon || UC complication.","IBS flare || Not this picture."],
 "Report new distention or constipation.")

# ---------- diagnostics ----------
q("dx","Which tests are used to evaluate UC and Crohn's? "+SATA,
 ["*Endoscopy with biopsy","*CT scan or MRI of the bowel and bowel wall","*Stool culture","*CBC and ESR","Anti-CCP || RA test."],
 "Also electrolytes and albumin.")
q("dx","Match the test with what it shows in IBD. Which pairing is correct?",
 ["*Albumin — malnutrition","Stool culture — inflammation level || It rules out infection.","ESR — anemia || ESR is an inflammatory marker.","Electrolytes — bowel wall thickness || CT/MRI shows that."],
 "CBC/WBC: anemia, infection, inflammation.")
q("dx","Why is a stool culture ordered for a client with a suspected IBD flare?",
 ["*To rule out an intestinal infection as the cause of diarrhea","To confirm Crohn's || Biopsy does.","To check albumin || A blood test.","To measure ESR || A blood test."],
 "Endoscopy with biopsy confirms the mucosal changes.")

# ---------- fluid & electrolytes ----------
q("fe","Which imbalances can frequent diarrhea in IBD cause? "+SATA,
 ["*Hyponatremia","*Hypokalemia","*Hypomagnesemia","*Metabolic acidosis","Metabolic alkalosis || Diarrhea causes acidosis."],
 "Also chloride loss, calcium deficiency and dehydration.")
q("fe","Why is a client with long-standing IBD at risk for osteoporosis?",
 ["*Calcium deficiency","Too much potassium || Not the link.","High sodium || Not the link.","Metabolic alkalosis || Not the link."],
 "Calcium-rich foods are part of the remission diet.")
q("fe","Which findings suggest dehydration in a client with an IBD flare? "+SATA,
 ["*Tachycardia","*Orthostatic blood pressure changes","*Decreased urine output","*Rapid weight loss","Bounding pulses || Fluid overload."],
 "Track stool frequency, weight and intake and output.")

# ---------- nursing ----------
q("nursing","During a severe IBD flare, which interventions does the nurse expect? "+SATA,
 ["*NPO bowel rest with IV fluids as ordered","*Prescribed corticosteroids","*Nutrition support such as parenteral nutrition","*Perianal skin protection","Large high-fiber meals || Low fiber during flares."],
 "Monitor vital signs, weight, I&O and stool output.")
q("nursing","Which findings in a client with IBD must be reported immediately? "+SATA,
 ["*Gross bleeding","*Severe abdominal pain or distention","*Fever","*Signs of shock","Mild cramping relieved after a stool || Expected."],
 "These can signal hemorrhage or perforation.")
q("nursing","Which findings should the nurse record for a client with an IBD flare? "+SATA,
 ["*Stool frequency and blood or mucus","*Pain","*Vital signs and weight","*Intake and output","Peak flow || Not related."],
 "Frequent diarrhea and bleeding can cause hypovolemia and anemia.")

# ---------- steroids ----------
q("steroid","What is the role of corticosteroids in IBD?",
 ["*Short-term control of acute exacerbations","Lifelong maintenance || Not the role.","Cure the disease || No cure.","Replace 5-ASA for maintenance || Maintenance uses other classes."],
 "Monitor for adverse effects.")
q("steroid","Which corticosteroids are on the IBD slide and by which routes? "+SATA,
 ["*Methylprednisolone by mouth, rectally or IV","*Prednisone by mouth","Mesalamine IV for flares || A 5-ASA, not a steroid.","Adalimumab by mouth || A biologic injection."],
 "Steroids = acute flare; the rest = maintenance.")

# ---------- 5-ASA ----------
q("asa","Which drugs are 5-ASA (5-aminosalicylic acid) anti-inflammatories for IBD maintenance? "+SATA,
 ["*Sulfasalazine","*Mesalamine","Azathioprine || Immunomodulator.","Vedolizumab || Biologic."],
 "Mesalamine comes in oral and rectal forms.")
q("asa","Which teaching is specific to sulfasalazine? "+SATA,
 ["*Take folic acid supplementation","*Avoid sun exposure","Get TB screening before each dose || Biologics.","Inject under the skin || It's oral."],
 "It's taken by mouth for maintenance.")
q("asa","A client asks why they still take mesalamine when they have no symptoms. Best response?",
 ["*'It's a maintenance drug that keeps the inflammation controlled.'","'It's only for acute flares.' || That's steroids.","'You can stop once you feel better.' || Maintenance continues.","'It cures UC.' || No cure."],
 "5-ASA drugs maintain remission.")

# ---------- immunomodulators ----------
q("immuno","Which drugs are immunomodulators for IBD? "+SATA,
 ["*Azathioprine","*Methotrexate","*Mercaptopurine","Ustekinumab || Biologic.","Prednisone || Corticosteroid."],
 "Monitor CBC and liver function.")
q("immuno","Which statements compare immunomodulators and biologics correctly? "+SATA,
 ["*Immunomodulators broadly suppress immunity; biologics target specific immune proteins","*Immunomodulators are taken by mouth daily; biologics are self-injected or given by IV infusion","*Immunomodulators take weeks to months to work; biologics work in a few weeks","*Immunomodulators are inexpensive; biologics are very expensive","Biologics are cheaper and work slower || Reversed."],
 "Both are maintenance therapy.")
q("immuno","Which labs does the nurse monitor for a client on azathioprine for Crohn's?",
 ["*CBC and liver function","Hemoglobin A1C only || Not the focus.","Thyroid levels || Not listed.","Lipase only || Not listed."],
 "Infection precautions apply too.")

# ---------- biologics ----------
q("bio","Which drugs are biologics on the IBD slide? "+SATA,
 ["*Ustekinumab","*Adalimumab","*Risankizumab","*Vedolizumab","Mercaptopurine || Immunomodulator."],
 "Given by IV infusion or subcutaneous injection.")
q("bio","Before a client starts vedolizumab, what must be done?",
 ["*Screen for infection and tuberculosis","Start folic acid || Sulfasalazine.","Check a sweat chloride test || Not related.","Schedule a colonoscopy every month || Not required."],
 "Biologics suppress immunity.")
q("bio","A client on adalimumab for UC has a fever and cough. What should the nurse do?",
 ["*Report it promptly; biologics raise infection risk","Tell them it's an expected flare || Infection must be ruled out.","Double the next dose || Never.","Recommend an antidiarrheal || Not related."],
 "Monitor during injections and infusions.")

# ---------- nutrition ----------
q("nutri","Which foods fit the diet DURING A FLARE? "+SATA,
 ["*Soft, bland, low-fiber foods","*Bananas","*Fully cooked, skinless vegetables","*Lean protein","Raw vegetables and whole grains || High fiber."],
 "Hydrate with 8–10 glasses a day.")
q("nutri","Which foods fit the diet DURING REMISSION? "+SATA,
 ["*Fiber-rich whole foods","*Lean protein","*Calcium-rich foods","*Avoiding processed foods","Only clear liquids || Not in remission."],
 "Keep a food journal and avoid trigger foods.")
q("nutri","Which teaching applies to IBD in BOTH remission and flare? "+SATA,
 ["*Drink 8–10 glasses of fluid a day","*Eat small, frequent meals","*Keep a food journal","*Avoid trigger foods","Eat high fiber at all times || Low fiber during flares."],
 "Supplements and probiotics may be added.")
q("nutri","Which statement by a client in an acute flare needs more teaching?",
 ["*'I'll eat a big raw salad with nuts tonight.'","'I'll have a banana and cooked carrots.' || Correct flare choice.","'I'll eat small meals.' || Correct.","'I'll write down what I eat.' || Correct."],
 "Flare = soft, bland, low fiber.")

# ---------- TPN ----------
q("tpn","Which nursing actions apply to TPN? "+SATA,
 ["*Run it on an infusion pump","*Check the label for accuracy","*Check fingerstick glucose every 6 hours","*Change tubing every 24 hours with a micron filter","Piggyback other IV medications into the line || No other medications."],
 "Also monitor labs, weight and I&O.")
q("tpn","How often is the central line dressing changed for TPN per the lecture?",
 ["*Every 7 days","Every hour || Too often.","Only when it falls off || Scheduled.","Every 24 hours like the tubing || Tubing is every 24 hours."],
 "Maintain sterility of all ports.")
q("tpn","What does TPN contain? "+SATA,
 ["*Protein, carbohydrates and lipids","*Electrolytes","*Vitamins and minerals","Whole blood || Not TPN."],
 "Macronutrients plus micronutrients.")
q("tpn","Which is the PRIORITY risk the nurse prevents with TPN?",
 ["*Central line infection","Constipation || Not the priority.","Hair loss || Not the priority.","Low fiber intake || Not the priority."],
 "Sterile technique, dedicated line, monitor glucose and fluid balance.")

# ---------- surgery ----------
q("surg","Which surgeries match the disease? "+SATA,
 ["*Bowel resection: Crohn's","*J-pouch: UC","*Proctocolectomy with permanent ileostomy: UC","J-pouch: Crohn's || UC."],
 "The J-pouch is built after the colon and rectum are removed.")
q("surg","A client with Crohn's asks if a bowel resection will cure the disease. Best response?",
 ["*'It treats complications, but Crohn's can come back.'","'Yes, it's curative.' || Crohn's can recur.","'Surgery is never done for Crohn's.' || Resection is.","'Only a J-pouch can cure Crohn's.' || J-pouch is for UC."],
 "UC surgery that removes the colon can be definitive.")
q("surg","What is a J-pouch?",
 ["*An internal reservoir made from the end of the small intestine after the colon and rectum are removed","A permanent colostomy || Not a J-pouch.","A feeding tube || Not a J-pouch.","A stent in the colon || Not a J-pouch."],
 "Also called ileal pouch–anal anastomosis (IPAA).")

# ---------- health promotion ----------
q("health","When does colorectal cancer screening start for a client with IBD per the lecture?",
 ["*About 8 years after diagnosis or symptom onset, then every 1–3 years","At age 75 only || Too late.","Every month after diagnosis || Not the schedule.","Never, IBD doesn't raise risk || It does."],
 "Individualized to risk.")
q("health","Which health promotion teaching helps PREVENT IBD exacerbations? "+SATA,
 ["*Avoid trigger foods","*Stress reduction","*Hydration","Stop maintenance medicine when well || Keep taking it."],
 "Managing a flare = soft, bland, low fiber plus hydration.")
q("health","Which psychosocial support fits a client with IBD? "+SATA,
 ["*Refer to the Crohn's & Colitis Foundation","*Address body image and ostomy adjustment","*Support stress management","Tell them symptoms are all in their head || Not therapeutic."],
 "Chronic symptoms affect daily life.")
