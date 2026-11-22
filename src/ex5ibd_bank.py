# Week 14.1 Immunity: Ulcerative Colitis & Crohn's — lesson plan and Pearson textbook excerpt (pp. 735–747), via notes.
EXAM = "e5"
T = "e5ibd"
CONCEPTS = {
 "overview":"IBD overview & cause",
 "risk":"Onset age & risk factors",
 "ucpatho":"UC pathophysiology",
 "cdpatho":"Crohn's pathophysiology",
 "compare":"UC vs Crohn's: the differences",
 "ucassess":"UC findings & severity",
 "megacolon":"Toxic megacolon & UC complications",
 "cdassess":"Crohn's findings & complications",
 "dx":"Diagnostics & monitoring",
 "asa":"5-ASA drugs",
 "steroid":"Corticosteroids for flares",
 "bio":"Biologics, JAK inhibitor & antibiotics",
 "nutri":"Nutrition, bowel rest & TPN",
 "surg":"Surgery: UC vs Crohn's",
 "ostomy":"Ileostomy & IPAA",
 "nursing":"Nursing priorities: fluids, skin, alerts",
 "life":"Lifespan & psychosocial care",
}
HI = ["compare","megacolon","cdassess","ucassess","surg","asa","nursing","bio"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- overview ----------
q("overview","Which statement about inflammatory bowel disease (IBD) is correct?",
 ["*It's chronic, relapsing intestinal inflammation with flare-ups and remissions","It's a single acute infection || Chronic and relapsing.","It's cured by antibiotics || No cure.","It only affects older adults || Peak onset 15–30."],
 "IBD includes ulcerative colitis (UC) and Crohn's disease.")
q("overview","What causes IBD?",
 ["*The cause is unknown; genetic, immune, environmental and possibly infectious factors are involved","A high-fiber diet || Not the cause.","Only stress || Not the cause.","A single virus || Not established."],
 "There's no established way to prevent it.")

# ---------- risk ----------
q("risk","When does IBD onset typically peak?",
 ["*Around ages 15–30, with another onset period later in life","Only after 70 || Not the peak.","Only in infancy || Not the peak.","Only during pregnancy || Not the pattern."],
 "Family history contributes.")
q("risk","How does smoking relate to IBD in the textbook?",
 ["*It increases Crohn's risk; it's linked to lower UC risk, but that's never a reason to recommend smoking","It prevents Crohn's || It increases Crohn's risk.","It has no relationship || There is one.","It should be recommended for UC || Never."],
 "Lack of physical activity may also raise Crohn's risk.")

# ---------- UC patho ----------
q("ucpatho","Where does ulcerative colitis occur?",
 ["*The mucosa of the colon and rectum, starting in the rectum and spreading continuously","Anywhere from mouth to anus in patches || Crohn's.","The entire bowel wall in patches || Crohn's.","The stomach only || Not UC."],
 "Fragile, ulcerated mucosa bleeds easily.")
q("ucpatho","What does a 'lead-pipe' colon mean in long-standing UC?",
 ["*Loss of haustra gives the colon a smooth appearance","A cobblestone pattern || Crohn's.","A twisted bowel || Volvulus.","A bowel full of stool || Not the meaning."],
 "Chronic inflammation changes the colon's shape.")

# ---------- Crohn's patho ----------
q("cdpatho","Which features describe Crohn's disease? "+SATA,
 ["*Can affect any part of the GI tract, often the terminal ileum","*Transmural inflammation through the whole bowel wall","*Patchy skip lesions","*Cobblestone appearance with deep ulcers and fissures","Continuous inflammation starting in the rectum || UC."],
 "Thickening and fibrosis cause strictures; fistulas and abscesses can form.")
q("cdpatho","Why can Crohn's disease cause bowel obstruction?",
 ["*Transmural thickening and fibrosis create strictures","Only mucosa is involved || That's UC.","It causes too much peristalsis only || Not the mechanism.","It removes the haustra || That's UC."],
 "Strictures narrow the bowel.")

# ---------- compare ----------
q("compare","Which pairings correctly compare UC and Crohn's? "+SATA,
 ["*UC — continuous; Crohn's — skip lesions","*UC — mucosa only; Crohn's — transmural","*UC — colon and rectum; Crohn's — mouth to anus, often terminal ileum","*UC — toxic megacolon; Crohn's — fistulas and strictures","UC — RLQ pain; Crohn's — LLQ pain || Reversed."],
 "Lock these in for Exam 5.")
q("compare","A client has bloody diarrhea with mucus and LLQ cramping relieved by defecation. Which condition fits best?",
 ["*Ulcerative colitis","Crohn's disease || Usually less bloody with RLQ pain.","Small bowel obstruction || Vomiting and distention.","Appendicitis || Not this pattern."],
 "UC = bloody mucus diarrhea and LLQ cramps.")
q("compare","A client has persistent non-bloody diarrhea, RLQ pain, weight loss and a fistula. Which condition fits best?",
 ["*Crohn's disease","Ulcerative colitis || Bloody stools, LLQ, no fistulas.","Rotavirus || Acute viral illness.","Hemorrhoids || Not this pattern."],
 "Crohn's = fistulas, abscesses, strictures, malabsorption.")
q("compare","Which surgical statement is correct?",
 ["*Colectomy can treat colonic UC definitively; Crohn's can recur after resection","Surgery cures Crohn's || It can recur.","UC can never be treated with surgery || Colectomy treats it.","Both are cured by appendectomy || Not true."],
 "Surgery for Crohn's is for complications or failed conservative care.")

# ---------- UC assessment ----------
q("ucassess","Which findings are typical of UC? "+SATA,
 ["*Frequent bloody, mucus-containing diarrhea","*Urgency","*LLQ cramping relieved by defecation","*Anemia, dehydration and weight loss","Fistula draining to the skin || Crohn's."],
 "Severity ranges from mild to severe.")
q("ucassess","Which client has SEVERE ulcerative colitis?",
 ["*Six or more bloody stools a day with fever, tachycardia and anemia","Three soft stools a day without blood || Mild at most.","Four or fewer stools a day || Mild.","One formed stool a day || Normal."],
 "Mild = four or fewer stools a day.")

# ---------- megacolon ----------
q("megacolon","A client with severe UC has sudden marked abdominal distention, fever and tachycardia. What does the nurse suspect?",
 ["*Toxic megacolon","Expected flare symptoms || This is an emergency.","Constipation || Not this picture.","Shingles || Not related."],
 "Severe colonic dilation with paralysis risks perforation; get urgent evaluation.")
q("megacolon","Which medications can contribute to toxic megacolon? "+SATA,
 ["*Antidiarrheals","*Opiates","*Certain antidepressants","Mesalamine || A 5-ASA used to treat UC."],
 "Antidiarrheals are generally avoided in severe acute UC.")
q("megacolon","Which are major complications of UC? "+SATA,
 ["*Hemorrhage","*Perforation","*Toxic megacolon","*Increased long-term colorectal cancer risk","Fistulas to the bladder || More typical of Crohn's."],
 "Keep recommended colorectal surveillance.")

# ---------- Crohn's assessment ----------
q("cdassess","Which findings are typical of Crohn's disease? "+SATA,
 ["*Persistent diarrhea, often without visible blood","*Steady RLQ or periumbilical pain","*Weight loss, fever and fatigue","*Malnutrition","LLQ cramps with bloody mucus || UC."],
 "Nausea and vomiting can occur with upper-tract involvement.")
q("cdassess","Why does Crohn's of the terminal ileum cause vitamin B12 deficiency?",
 ["*The terminal ileum absorbs vitamin B12 and bile salts","The colon makes B12 || Not the reason.","Steroids destroy B12 || Not the reason.","It causes bleeding only || Not the reason."],
 "Malabsorption contributes to anemia and nutrition deficits.")
q("cdassess","A client with Crohn's reports passing gas and stool in the urine. What does this suggest?",
 ["*A bowel-to-bladder fistula","A UTI only || A fistula is suspected.","Toxic megacolon || UC.","Normal finding || Not normal."],
 "Fistulas can connect bowel to bladder or skin.")
q("cdassess","Which are complications of Crohn's disease? "+SATA,
 ["*Strictures and obstruction","*Fistulas and abscesses","*Perianal disease","*Malabsorption","Lead-pipe colon || UC."],
 "Also perforation and increased colon cancer risk.")

# ---------- diagnostics ----------
q("dx","Which tests evaluate IBD? "+SATA,
 ["*Colonoscopy or sigmoidoscopy","*Stool tests to rule out infection","*CBC for anemia and WBC","*ESR and CRP","Anti-CCP || RA."],
 "Also monitor albumin, electrolytes, vitamins and liver tests.")
q("dx","Why are stool tests done for a client with an IBD flare?",
 ["*To check for blood and mucus and rule out infectious diarrhea","To diagnose RA || Not related.","To measure B12 || Not the test.","To check CD4 || Not related."],
 "An elevated WBC may suggest inflammation or an abscess.")

# ---------- 5-ASA ----------
q("asa","Which drugs are 5-ASA derivatives? "+SATA,
 ["*Mesalamine","*Sulfasalazine","*Balsalazide","*Olsalazine","Infliximab || A TNF inhibitor."],
 "They reduce intestinal inflammation; oral and/or rectal forms.")
q("asa","Before sulfasalazine, which allergy should the nurse ask about?",
 ["*Sulfonamide or salicylate allergy","Shellfish allergy || Not related.","Latex allergy || Not related.","Egg allergy || Not related."],
 "Monitor kidney and liver function and CBC; watch for headache, dizziness or rash.")

# ---------- steroids ----------
q("steroid","What is the role of corticosteroids in IBD?",
 ["*Control acute flares; they aren't the main long-term maintenance strategy","Daily lifelong maintenance for everyone || Not the main strategy.","Cure the disease || Not curative.","Prevent colon cancer || Not their role."],
 "Taper as instructed; don't stop abruptly.")
q("steroid","Which corticosteroids are listed for IBD? "+SATA,
 ["*Prednisone","*Prednisolone","*Budesonide","*Hydrocortisone","Mesalamine || A 5-ASA."],
 "Monitor infection and adverse effects.")

# ---------- biologics ----------
q("bio","Which drugs are TNF inhibitors used for IBD? "+SATA,
 ["*Infliximab","*Adalimumab","*Certolizumab","*Golimumab","Vedolizumab || Integrin antagonist."],
 "Assess for infection.")
q("bio","Which statement matches the IBD drug to its class?",
 ["*Vedolizumab — integrin antagonist; ustekinumab — interleukin-12/23 inhibitor; tofacitinib — oral JAK inhibitor","Tofacitinib — TNF inhibitor || It's a JAK inhibitor.","Ustekinumab — 5-ASA || IL-12/23 inhibitor.","Vedolizumab — corticosteroid || Integrin antagonist."],
 "Natalizumab is also an integrin antagonist.")
q("bio","What is the priority teaching for a client on a biologic or tofacitinib?",
 ["*Report fever or other infection signs; review vaccines with the provider","Take extra antidiarrheals during flares || Can worsen severe UC.","Stop when feeling better || Take as prescribed.","Expect weight gain only || Not the priority."],
 "Immunosuppression requires infection vigilance.")
q("bio","When are antibiotics used in IBD?",
 ["*When fistulas or abscesses complicate the disease","For every flare || Not routine.","To prevent toxic megacolon || Not the indication.","To replace 5-ASA drugs || Not a replacement."],
 "Antidiarrheals are avoided in severe acute UC.")

# ---------- nutrition ----------
q("nutri","Which diet does the textbook suggest for IBD?",
 ["*High-calorie, high-protein, lower-fat, limiting lactose if intolerant","High-fat, low-protein || Opposite.","Unlimited dairy for calcium || Limit lactose if intolerant.","Clear liquids for life || Not the plan."],
 "Collaborate with a dietitian; individualize to tolerance.")
q("nutri","During a severe IBD flare, what may be ordered for bowel rest?",
 ["*NPO, with enteral nutrition preferred when feasible and TPN if needed","A large high-fiber meal || Not during a severe flare.","Only coffee and juice || Not the plan.","Nothing; diet doesn't matter || It does."],
 "TPN carries more complications than enteral feeding.")
q("nutri","Which monitoring supports nutrition in IBD? "+SATA,
 ["*Weight trends","*Fluid balance","*Protein status and albumin","*Micronutrients such as B12","Peak flow || Not related."],
 "Malabsorption is especially common in Crohn's.")

# ---------- surgery ----------
q("surg","When is surgery generally done for Crohn's disease?",
 ["*For complications or failure of conservative care","As a first-line cure || It doesn't cure Crohn's.","Only for mild disease || Not the indication.","Never || Resection or strictureplasty can help."],
 "Strictureplasty relieves obstruction without removing bowel.")
q("surg","A client asks whether a total colectomy will cure their UC. Best response?",
 ["*'Removing the diseased colon can eliminate colonic UC.'","'No surgery helps UC.' || Colectomy can.","'It will cure Crohn's too.' || Crohn's can recur.","'It only treats the rectum.' || Total colectomy removes the colon."],
 "UC is limited to the colon and rectum.")

# ---------- ostomy ----------
q("ostomy","What is an IPAA (ileal pouch–anal anastomosis)?",
 ["*A pouch made from the terminal ileum connected to the anal canal, often with a temporary loop ileostomy","A permanent colostomy || Not IPAA.","A stent in the colon || Not IPAA.","A feeding tube || Not IPAA."],
 "Used after total colectomy for UC.")
q("ostomy","What should the nurse monitor for a client with a new ileostomy? "+SATA,
 ["*Output volume","*Hydration","*Peristomal skin integrity","*Pouch fit and teaching","Formed, solid stool || Ileostomy output is liquid."],
 "A continent ileostomy has an internal reservoir drained with a catheter.")

# ---------- nursing ----------
q("nursing","Which findings suggest hypovolemia in a client with an IBD flare? "+SATA,
 ["*Tachycardia","*Dry mucous membranes","*Poor skin turgor","*Thirst and weakness","Bounding pulses || Not hypovolemia."],
 "Record liquid stool output and I&O, vitals and daily weights.")
q("nursing","Which findings in a client with IBD must be reported promptly? "+SATA,
 ["*Grossly bloody stools","*Increasing abdominal distention","*Severe pain or fever","*Hypotension","Mild cramping relieved by a bowel movement || Expected in UC."],
 "Perforation and hemorrhage can be emergencies.")
q("nursing","How should the nurse protect perianal skin in a client with frequent diarrhea?",
 ["*Cleanse after each stool and apply prescribed barrier products","Leave the skin moist to soothe it || Causes breakdown.","Use harsh soap scrubs || Damages skin.","Apply heat packs || Not the care."],
 "Monitor for breakdown.")
q("nursing","Which teaching applies to IBD? "+SATA,
 ["*Take medications as prescribed","*Recognize flare symptoms","*Keep colorectal surveillance and follow-up visits","*Monitor hydration and nutrition","Take antidiarrheals freely during severe flares || Avoid in severe UC."],
 "Teach central line/TPN care when relevant.")

# ---------- lifespan ----------
q("life","Which considerations apply to a teen with Crohn's disease? "+SATA,
 ["*Monitor growth and nutrition","*Address school and social impact","*Involve family while respecting privacy","Limit all school activities || Not the goal."],
 "Older adults may have less pronounced symptoms and more comorbidities.")
q("life","Which psychosocial needs are common in IBD? "+SATA,
 ["*Stress management and coping","*Body image","*Privacy and social functioning","*Adjustment to an ostomy","None; IBD is purely physical || Psychosocial care matters."],
 "Pregnancy planning involves GI and maternal-fetal clinicians.")
