T = "e5ibd"; SET = "20261123"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# overview
q("overview", "A 22-year-old client newly diagnosed with IBD (inflammatory bowel disease) asks, 'What did I do to cause this, and how could I have prevented it?' Which response by the nurse is accurate?",
  ["'It was caused by eating too much fiber over many years.' || A high-fiber diet is not the cause",
   "'Stress alone caused your disease, so avoiding stress prevents it.' || Stress alone is not the cause",
   "*'The cause is unknown, and there's no established prevention.'",
   "'A single virus caused it, and antibiotics will cure it.' || IBD is not one virus and is not cured by antibiotics"],
  "The cause of IBD is unknown; genetic, immune, environmental and possibly infectious factors are involved, and there is no established way to prevent it. IBD is chronic and relapsing.")

# risk
q("risk", "A 26-year-old client with Crohn's disease smokes and says, 'My cousin with ulcerative colitis was told smoking might lower UC risk, so it's fine for me.' Which response by the nurse is best?",
  ["'You're right; smoking protects against all forms of IBD, including Crohn's.' || Smoking increases Crohn's risk",
   "*'Smoking increases Crohn's risk and is never recommended.'",
   "'Smoking has no relationship to either Crohn's disease or UC.' || The textbook links smoking to IBD risk",
   "'Smoking helps UC, so it should be recommended for your Crohn's too.' || Smoking is never recommended"],
  "Smoking increases Crohn's risk. It is linked to lower UC (ulcerative colitis) risk, but that is never a reason to recommend smoking.")

# ucpatho
q("ucpatho", "A nurse is reviewing a colonoscopy report for a 34-year-old client with ulcerative colitis. Which description fits UC (ulcerative colitis)?",
  ["Patchy skip lesions scattered through the terminal ileum || Skip lesions in the ileum fit Crohn's",
   "Transmural inflammation with a cobblestone appearance || That describes Crohn's",
   "Inflammation limited to the lining of the stomach || UC affects the colon and rectum",
   "*Continuous mucosal inflammation that starts in the rectum"],
  "UC involves the mucosa of the colon and rectum, starting in the rectum and spreading continuously. Fragile, ulcerated mucosa bleeds easily.")

# cdpatho
q("cdpatho", "A 30-year-old client with Crohn's disease reports cramping, distention and vomiting. The nurse suspects bowel obstruction. Which explanation of the cause is correct?",
  ["*Transmural thickening and fibrosis have formed a stricture",
   "Inflammation is limited to the mucosa, which blocks the lumen || Crohn's is transmural, not mucosa-only",
   "Loss of haustra has created a smooth lead-pipe colon || Lead-pipe colon is a UC finding",
   "Excess peristalsis alone has blocked the small bowel || Not the mechanism of Crohn's obstruction"],
  "In Crohn's, transmural inflammation causes thickening and fibrosis, which form strictures that narrow the bowel and can cause obstruction.")

# compare (HI x2)
q("compare", "A 19-year-old client reports 8 weeks of non-bloody diarrhea, steady RLQ (right lower quadrant) pain and weight loss. A perianal abscess is found. Which condition does the nurse expect?",
  ["Ulcerative colitis || UC usually causes bloody mucus diarrhea with LLQ cramps",
   "Toxic megacolon || That is an acute UC complication with distention",
   "*Crohn's disease",
   "Hemorrhoids || Hemorrhoids don't explain weight loss and RLQ pain"],
  "Crohn's typically causes non-bloody diarrhea, RLQ pain and weight loss, with complications such as fistulas, abscesses and strictures.")
q("compare", "A nurse is teaching a study group how UC (ulcerative colitis) differs from Crohn's disease. Which statements are correct? " + SATA,
  ["*UC is continuous; Crohn's has skip lesions",
   "*UC involves the mucosa only; Crohn's is transmural",
   "UC typically causes RLQ (right lower quadrant) pain; Crohn's causes LLQ (left lower quadrant) pain || Reversed: UC is LLQ; Crohn's is RLQ",
   "*Toxic megacolon is a UC complication; fistulas and strictures fit Crohn's",
   "Colectomy cures both UC and Crohn's || Crohn's can recur after resection"],
  "UC is continuous and mucosal, in the colon and rectum, and risks toxic megacolon. Crohn's is transmural with skip lesions anywhere from mouth to anus and causes fistulas and strictures.")

# ucassess (HI x2)
q("ucassess", "A nurse is assessing four clients with ulcerative colitis. Which client has SEVERE disease?",
  ["A client with 3 soft, non-bloody stools a day and mild cramps || That fits mild disease",
   "A client with 4 stools a day, no fever and a normal heart rate || Four or fewer stools a day is mild",
   "A client with 1 formed stool a day and no abdominal pain || That is not severe",
   "*A client with 7 bloody stools a day, fever and anemia"],
  "Severe UC is six or more bloody stools a day with fever, tachycardia and anemia; mild UC is four or fewer stools a day.")
q("ucassess", "A 28-year-old client with UC (ulcerative colitis) is admitted during a flare. Which findings should the nurse expect? " + SATA,
  ["*Urgency to defecate",
   "*Bloody diarrhea containing mucus",
   "A fistula draining to the skin || Fistulas fit Crohn's",
   "*LLQ (left lower quadrant) cramping relieved by defecation",
   "*Dehydration and weight loss"],
  "UC typically causes frequent bloody, mucus-containing diarrhea, urgency, LLQ cramping relieved by defecation, and anemia, dehydration and weight loss.")

# megacolon (HI x2)
q("megacolon", "A 40-year-old client with severe UC (ulcerative colitis) asks for an antidiarrheal to slow her stools. Which response by the nurse is best?",
  ["'Sure, antidiarrheals are the main treatment for severe UC flares.' || They are generally avoided in severe acute UC",
   "*'Antidiarrheals can contribute to toxic megacolon, so they're avoided.'",
   "'You can take it freely, as long as you also take an opiate.' || Opiates also contribute to toxic megacolon",
   "'Antidiarrheals will rest the colon and help prevent perforation.' || They raise the risk of a complication that causes perforation"],
  "Antidiarrheals, opiates and certain antidepressants can contribute to toxic megacolon, so antidiarrheals are generally avoided in severe acute UC.")
q("megacolon", "A client with severe ulcerative colitis suddenly develops marked abdominal distention, a temperature of 102°F (38.9°C) and a heart rate of 128. What is the nurse's priority action?",
  ["Give a prescribed antidiarrheal to reduce stool output || Antidiarrheals can worsen toxic megacolon",
   "Encourage the client to walk to relieve gas || Delays urgent evaluation",
   "Document the findings as an expected flare || These are not expected flare signs",
   "*Report the findings urgently as possible toxic megacolon"],
  "Sudden distention, fever and tachycardia in severe UC suggest toxic megacolon: severe colonic dilation with paralysis that risks perforation and needs urgent evaluation.")

# cdassess (HI x2)
q("cdassess", "A 32-year-old client with Crohn's disease of the terminal ileum has fatigue and anemia. The nurse anticipates a deficiency of which nutrient, and why?",
  ["*Vitamin B12, because the terminal ileum absorbs it",
   "Vitamin B12, because the colon normally makes most of it || The colon does not make B12",
   "Vitamin B12, because ileal Crohn's causes bleeding only || Deficiency is from malabsorption, not bleeding",
   "Vitamin B12, because steroid treatment destroys it in the gut || Not the mechanism"],
  "The terminal ileum absorbs vitamin B12 and bile salts, so ileal Crohn's causes B12 deficiency; malabsorption contributes to anemia and nutrition deficits.")
q("cdassess", "A 45-year-old client with Crohn's disease reports recurrent urinary infections and air bubbles in the urine. Which complication should the nurse suspect?",
  ["Toxic megacolon from colonic dilation || That presents with distention, fever and tachycardia",
   "Lead-pipe colon from loss of haustra || That is a UC finding",
   "*A bowel-to-bladder fistula",
   "A normal, expected finding in Crohn's disease || Gas in the urine is never normal"],
  "Fistulas in Crohn's can connect the bowel to the bladder or skin; passing gas or stool in the urine suggests a bowel-to-bladder fistula.")

# dx
q("dx", "A 25-year-old client is admitted with an IBD (inflammatory bowel disease) flare. The provider orders stool tests. The client asks why. Which response by the nurse is correct?",
  ["'To measure how much vitamin B12 you are absorbing.' || B12 is a blood test",
   "*'To check for blood and mucus and rule out infection.'",
   "'To check whether you also have RA (rheumatoid arthritis).' || Unrelated",
   "'To check your CD4 (cluster of differentiation 4) count.' || Unrelated"],
  "Stool tests check for blood and mucus and rule out infectious diarrhea. Colonoscopy, CBC, ESR and CRP also help evaluate IBD.")

# asa (HI x2)
q("asa", "A 36-year-old client with UC (ulcerative colitis) is prescribed sulfasalazine. Which assessment finding should the nurse report to the provider before the first dose?",
  ["A shellfish allergy with hives || Not related to sulfasalazine",
   "A latex allergy from surgical gloves || Not related to sulfasalazine",
   "*A sulfonamide allergy",
   "An egg allergy since childhood || Not related to sulfasalazine"],
  "Before sulfasalazine, ask about sulfonamide or salicylate allergy. Monitor kidney and liver function and CBC, and watch for headache, dizziness or rash.")
q("asa", "A nurse is reviewing a medication list for a client with IBD (inflammatory bowel disease). Which drugs are 5-ASA (5-aminosalicylic acid) derivatives? " + SATA,
  ["*Balsalazide",
   "Adalimumab || A TNF (tumor necrosis factor) inhibitor",
   "*Mesalamine",
   "*Olsalazine",
   "Budesonide || A corticosteroid"],
  "5-ASA derivatives include mesalamine, sulfasalazine, balsalazide and olsalazine. They reduce intestinal inflammation and come in oral and/or rectal forms.")

# steroid
q("steroid", "A 29-year-old client with Crohn's disease has been on prednisone for a flare and now feels much better. Which statement by the client indicates a need for further teaching?",
  ["'This medicine is meant to control my acute flare.' || Correct; steroids control acute flares",
   "*'I feel better, so I'll stop the prednisone today.'",
   "'I'll taper the dose slowly, the way I was instructed.' || Correct; taper as instructed",
   "'I'll watch for signs of infection while I take it.' || Correct; monitor for infection"],
  "Corticosteroids control acute IBD flares but aren't the main long-term maintenance strategy. They must be tapered as instructed, not stopped abruptly.")

# bio (HI x2)
q("bio", "A 33-year-old client with Crohn's disease is starting infliximab. Which instruction by the nurse is the priority?",
  ["'Take extra antidiarrheals whenever you have a severe flare.' || Not biologic teaching; antidiarrheals are avoided in severe acute UC",
   "'Stop the drug once your symptoms are better controlled.' || Treatment should not be stopped on one's own",
   "*'Report any fever and review your vaccines with the provider.'",
   "'Expect to gain weight; that's the main side effect.' || Not the priority teaching"],
  "Infliximab is a TNF (tumor necrosis factor) inhibitor; biologics suppress immunity, so infection vigilance and vaccine review are the priority.")
q("bio", "A client with Crohn's disease has developed a perianal fistula with an abscess. Which statement about drug therapy is correct?",
  ["Antibiotics are given for every IBD flare || They are used when fistulas or abscesses complicate disease",
   "Tofacitinib is a TNF (tumor necrosis factor) inhibitor || Tofacitinib is an oral JAK inhibitor",
   "Vedolizumab is a corticosteroid || Vedolizumab is an integrin antagonist",
   "*Antibiotics are indicated for this complication"],
  "Antibiotics are used in IBD when fistulas or abscesses complicate the disease. Vedolizumab is an integrin antagonist, ustekinumab an interleukin-12/23 inhibitor and tofacitinib an oral JAK (Janus-associated kinase) inhibitor.")

# nutri
q("nutri", "A 21-year-old client with IBD (inflammatory bowel disease) who is lactose intolerant asks what to eat between flares. Which meal plan should the nurse reinforce?",
  ["A high-fat, low-protein diet eaten in three large meals || The diet should be lower fat and high protein",
   "Clear liquids only, continued for the rest of life || Not a long-term diet",
   "Unlimited milk and dairy products for extra calcium || Lactose should be limited if intolerant",
   "*A high-protein, high-calorie, lower-fat, low-lactose diet"],
  "The textbook suggests a high-calorie, high-protein, lower-fat diet, limiting lactose if intolerant, individualized with a dietitian.")

# surg (HI x2)
q("surg", "A 38-year-old client with Crohn's disease asks whether surgery will cure his disease. Which response by the nurse is accurate?",
  ["'Yes, removing the affected section of bowel cures Crohn's.' || Crohn's can recur after resection",
   "*'Surgery treats complications, but Crohn's can recur afterward.'",
   "'Surgery is the first-line treatment for mild Crohn's.' || It is not first line or for mild disease",
   "'Surgery is never used for Crohn's, even for complications.' || Surgery is used for complications"],
  "Surgery for Crohn's is for complications or failure of conservative care, and the disease can recur after resection. Strictureplasty relieves obstruction without removing bowel.")
q("surg", "A nurse is comparing surgical outcomes for UC (ulcerative colitis) and Crohn's disease. Which statement is correct?",
  ["*Colectomy can treat colonic UC definitively",
   "Colectomy cures both UC and Crohn's disease permanently || Crohn's can recur anywhere in the GI tract",
   "UC can never be treated surgically, only with medication || Colectomy can treat UC definitively",
   "Strictureplasty removes the entire colon and rectum || It relieves obstruction without removing bowel"],
  "UC is limited to the colon and rectum, so colectomy can treat colonic UC definitively; Crohn's can recur after resection.")

# ostomy
q("ostomy", "A 27-year-old client had a total colectomy with a new ileostomy for UC (ulcerative colitis). Which assessments should the nurse include in the plan of care? " + SATA,
  ["*Ileostomy output volume",
   "*Hydration status",
   "Expect formed, solid stool in the pouch || Ileostomy output is not formed, solid stool",
   "*Peristomal skin integrity",
   "*Pouch fit and the client's self-care teaching"],
  "After a new ileostomy, monitor output volume, hydration, peristomal skin integrity, and pouch fit and teaching.")

# nursing (HI x2)
q("nursing", "A 31-year-old client with an IBD (inflammatory bowel disease) flare has frequent liquid stools. Which findings suggest hypovolemia? " + SATA,
  ["*Heart rate of 118",
   "*Dry mucous membranes",
   "Bounding peripheral pulses || Bounding pulses suggest fluid excess",
   "*Poor skin turgor",
   "*Thirst and weakness"],
  "Hypovolemia in an IBD flare shows as tachycardia, dry mucous membranes, poor skin turgor, thirst and weakness. Record stool output, I&O (intake and output), vitals and daily weights.")
q("nursing", "A nurse is caring for four clients with IBD (inflammatory bowel disease). Which client should the nurse report to the provider FIRST?",
  ["A client with mild cramping relieved by a bowel movement || An expected finding",
   "A client asking which lactose-free foods are high in protein || A teaching need, not urgent",
   "A client needing perianal skin care after a liquid stool || Routine care",
   "*A client with increasing abdominal distention and hypotension"],
  "Increasing distention and hypotension must be reported promptly; perforation and hemorrhage can be emergencies.")

# life
q("life", "A nurse is planning care for a 15-year-old with Crohn's disease. Which action is most appropriate?",
  ["Restrict the teen from all school activities during treatment || Not recommended; address school impact instead",
   "Discuss the diagnosis only with the parents, not the teen || Privacy should be respected while involving family",
   "*Monitor growth and nutrition and address school impact",
   "Assume psychosocial needs are minimal at this age || Coping and body image are common needs"],
  "For a teen with Crohn's, monitor growth and nutrition, address school and social impact, and involve family while respecting privacy.")
