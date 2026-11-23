T = "e5ibd"; SET = "20261123"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("overview","A client with abdominal pain, gas and alternating diarrhea and constipation has a normal colonoscopy. Which condition does this fit?",
 ["*Irritable bowel syndrome (IBS)","Ulcerative colitis || Would show mucosal inflammation.","Crohn's disease || Would show skip lesions.","Toxic megacolon || An emergency with dilation."],
 "IBS = functional disorder with no abnormalities on exam.")
q("immune","Which statement best describes the immune response in IBD?",
 ["*It's an exaggerated response: the body attacks its own bowel tissue","It's a suppressed response that can't fight infection || That's immunosuppression.","It's a normal response at homeostasis || Not IBD.","It's an allergic reaction to fiber || Not the cause."],
 "Too much response = autoimmune.")
q("compare","Which description fits CROHN'S disease rather than UC?",
 ["*Cobblestone appearance with inflammation through all layers of the bowel wall","Continuous inflammation starting at the rectum || UC.","Mucosal layer only || UC.","Limited to the colon and rectum || UC."],
 "Crohn's = patchy, transmural, anywhere 'gum to bum'.")
q("compare","A nurse is comparing UC and Crohn's. Which statement is correct?",
 ["*UC stays in the rectum and colon; Crohn's can occur anywhere in the GI tract","UC causes fistulas; Crohn's causes toxic megacolon || Reversed.","Only Crohn's raises colon cancer risk || Both do.","Only UC causes anemia and weight loss || Both do."],
 "Both carry nutritional deficits and colon cancer risk.")
q("ucassess","Which stool pattern is the nurse most likely to document for a client with UC?",
 ["*Frequent stools with blood and mucus, with urgency","Greasy, loose stools without blood || Crohn's.","Hard stools every 4 days || Constipation.","Clay-colored stools || Not IBD."],
 "UC = abdominal cramps and urgency.")
q("ucassess","Which client statement suggests ulcerative colitis?",
 ["*'I have cramping in my lower left side and have to rush to the bathroom.'","'My pain is mostly on the lower right, with greasy stools.' || Crohn's.","'Stool is coming out near my rectum through a new opening.' || Fistula, Crohn's.","'I'm only constipated, with no blood.' || Not UC."],
 "UC pain is often left lower abdomen.")
q("megacolon","A client with UC asks for an over-the-counter antidiarrheal during a severe flare. Best response?",
 ["*'Let's check with your provider first; antidiarrheals need caution in severe UC.'","'Take double the usual dose.' || Unsafe.","'Antidiarrheals cure UC.' || They don't.","'They're always safe with UC.' || Not in severe UC."],
 "They can contribute to toxic megacolon.")
q("megacolon","Which complication is MOST associated with ulcerative colitis?",
 ["*Toxic megacolon","Fistula formation || Crohn's.","Strictures from transmural fibrosis || Crohn's.","Abscesses || Crohn's."],
 "UC also causes hemorrhage and perforation.")
q("cdassess","A client with Crohn's disease has weight loss and low albumin despite eating. What explains this?",
 ["*Malabsorption from inflamed bowel","Overeating || Not the cause.","Toxic megacolon || UC.","Normal aging || Not the cause."],
 "Nutritional deficits and anemia are common.")
q("cdassess","Which finding should the nurse expect in a client with Crohn's disease?",
 ["*Patchy areas of inflammation separated by healthy bowel","One continuous area of inflammation from the rectum || UC.","Inflammation in the mucosa only || UC.","No structural change || IBS."],
 "Skip lesions are classic for Crohn's.")
q("dx","Which test gives information about the bowel and bowel wall in IBD?",
 ["*CT scan or MRI","Stool culture || Rules out infection.","ESR || Inflammatory marker.","Albumin || Malnutrition."],
 "Endoscopy with biopsy confirms the diagnosis.")
q("fe","A client with an IBD flare has had 10 watery stools today. Which lab results does the nurse anticipate? "+SATA,
 ["*Low potassium","*Low sodium","*Low magnesium","*Chloride loss","High potassium || Diarrhea lowers potassium."],
 "Metabolic acidosis and dehydration can follow.")
q("nursing","A client in a severe UC flare is placed on bowel rest. What does the nurse expect?",
 ["*NPO with IV fluids, and parenteral nutrition if needed","A high-fiber diet || Not during a flare.","Unrestricted oral intake || Not bowel rest.","Antidiarrheals every hour || Caution."],
 "Monitor I&O and weight.")
q("nursing","Which finding in a client with Crohn's should be reported right away?",
 ["*Sudden severe abdominal pain with a rigid, distended abdomen","Two loose stools today || Monitor.","Mild fatigue || Monitor.","Asking about the Crohn's & Colitis Foundation || Not urgent."],
 "This may signal perforation or obstruction.")
q("steroid","A client in an acute UC flare is started on IV methylprednisolone. The client asks how long they'll take it. Best response?",
 ["*'Steroids are for the acute flare, short term; other drugs maintain remission.'","'For the rest of your life.' || Not maintenance.","'Only until your colonoscopy.' || Not the reason.","'Steroids cure UC.' || No cure."],
 "Prednisone by mouth is the other listed steroid.")
q("asa","Which teaching should the nurse give a client starting sulfasalazine?",
 ["*'Take your folic acid supplement and protect yourself from the sun.'","'Get a TB test before each dose.' || Biologics.","'Inject this under the skin.' || Oral.","'This is only for acute flares.' || Maintenance."],
 "Sulfasalazine is a 5-ASA for maintenance.")
q("asa","Which routes are listed for mesalamine?",
 ["*Oral or rectal","IV only || Not listed.","Subcutaneous injection || Biologics.","Inhaled || Not listed."],
 "Mesalamine is a 5-ASA maintenance drug.")
q("immuno","A client asks why their provider chose methotrexate instead of a biologic. Which difference is accurate?",
 ["*Immunomodulators are inexpensive oral drugs but take weeks to months to work","Immunomodulators work faster than biologics || Slower.","Immunomodulators target one specific immune protein || Biologics do.","Immunomodulators are self-injected || Oral."],
 "Biologics are very expensive but faster.")
q("bio","Which statement by a client starting ustekinumab shows correct understanding?",
 ["*'I needed a TB screening before my first dose.'","'This is a pill I take daily.' || IV or SQ.","'It's for acute flares only.' || Maintenance.","'It doesn't affect my immune system.' || It suppresses it."],
 "Biologics are maintenance drugs.")
q("bio","Which IBD drugs are biologics given by IV infusion or SQ injection? "+SATA,
 ["*Adalimumab","*Risankizumab","*Vedolizumab","Azathioprine || Oral immunomodulator.","Mesalamine || 5-ASA."],
 "Screen for infection and TB first.")
q("nutri","A client in remission from Crohn's asks what to eat. Which choices fit? "+SATA,
 ["*Fiber-rich whole foods","*Lean protein","*Calcium-rich foods","Mostly processed snacks || Whole foods.","Only clear liquids || Not in remission."],
 "Stay hydrated: 8–10 glasses a day.")
q("nutri","Which meal is BEST for a client during a UC flare?",
 ["*Baked chicken, a ripe banana and well-cooked, skinless carrots","Raw salad with nuts and seeds || High fiber.","Whole-grain bran cereal || High fiber.","Fried fast food || Not bland."],
 "Flare = soft, bland, low fiber.")
q("tpn","A client on TPN needs an IV antibiotic. What should the nurse do?",
 ["*Use a different line; give no other medications through the TPN line","Piggyback it into the TPN line || No other medications.","Stop TPN for the day || Not needed.","Mix it into the TPN bag || Never."],
 "Keep all ports sterile.")
q("tpn","Which TPN checks are on schedule? "+SATA,
 ["*Fingerstick glucose every 6 hours","*Tubing change every 24 hours with a micron filter","*Central dressing change every 7 days","Tubing change every 7 days || Every 24 hours."],
 "Monitor labs, weight and I&O.")
q("surg","Which surgery for UC leaves the client with a permanent stoma?",
 ["*Proctocolectomy with permanent ileostomy","J-pouch || Internal reservoir.","Bowel resection || Crohn's.","Appendectomy || Not IBD surgery."],
 "Surgery can be definitive for UC.")
q("surg","A client is having a J-pouch created. Which condition does the client most likely have?",
 ["*Ulcerative colitis","Crohn's disease || Bowel resection.","IBS || Not surgical.","Appendicitis || Not this surgery."],
 "Built from the end of the small intestine after the colon and rectum are removed.")
q("health","A client was diagnosed with UC 8 years ago. Which teaching is a priority?",
 ["*Start colorectal cancer screening now, then every 1–3 years","Screening isn't needed with IBD || Risk is increased.","Screen only if symptoms change || Scheduled.","Screen once at age 75 || Too late."],
 "Screening begins about 8 years after diagnosis or symptom onset.")
