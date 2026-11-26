T = "blood"; SET = "20261126"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("comp", "A 58-year-old retired teacher has a low white blood cell count after treatment. Which blood function should the nurse explain is most affected?",
  ["Delivering oxygen to the tissues || that is the red blood cells' job",
   "Forming clots to stop bleeding || that is the platelets' job",
   "*Fighting off infection",
   "Carrying waste and hormones || that is the plasma's job"],
  "Red blood cells carry oxygen, white blood cells fight infection, platelets form clots, and plasma carries nutrients, hormones and waste.")

q("why", "The nurse on a medical-surgical unit reviews the census. Which clients are likely candidates for a blood product? " + SATA,
  ["*A 49-year-old with a large GI (gastrointestinal) bleed",
   "*A 33-year-old with immune thrombocytopenia and a very low platelet count",
   "*A 15-year-old with hemophilia who is actively bleeding",
   "A 40-year-old with normal labs before a routine physical || nothing is missing that a blood product would replace",
   "*A 62-year-old with anemia from chemotherapy"],
  "Clients need blood products for blood loss, anemia, clotting disorders, low platelets and massive hemorrhage.")

q("prod", "A 70-year-old on warfarin needs the drug's effect reversed before emergency surgery. Which blood product does the nurse anticipate?",
  ["Packed red blood cells || these raise oxygen-carrying capacity, not clotting factors",
   "*Fresh frozen plasma",
   "Platelets || these treat a low platelet count",
   "Cryoprecipitate || this is mainly for a low fibrinogen"],
  "Plasma replaces clotting factors and is used for coagulopathy, liver disease, massive transfusion and reversing warfarin.")

q("prod", "A nursing student describes blood products to a preceptor. Which statements are accurate? " + SATA,
  ["*'Cryoprecipitate is rich in fibrinogen, factor VIII and von Willebrand factor.'",
   "*'Platelets are kept at room temperature and have a short shelf life.'",
   "'Plasma is the product given to raise a low hemoglobin.' || packed RBCs raise hemoglobin; plasma replaces clotting factors",
   "*'One unit of packed RBCs raises hemoglobin about 1 g/dL.'",
   "'Whole blood is the most common product used on every unit.' || whole blood is rarely used today, mainly in trauma"],
  "Cryo is rich in fibrinogen, factor VIII and von Willebrand factor; platelets are stored at room temperature with a short shelf life; one unit of PRBCs raises Hgb about 1 g/dL; whole blood is rarely used, mainly for trauma.")

q("choose", "A 27-year-old postpartum client is bleeding and has a fibrinogen level of 85 mg/dL. Which product should the nurse prepare to give?",
  ["Platelets || these replace platelets, not fibrinogen",
   "Packed red blood cells || these restore oxygen-carrying capacity, not fibrinogen",
   "Whole blood || this is mainly for trauma and massive hemorrhage",
   "*Cryoprecipitate"],
  "Cryoprecipitate is rich in fibrinogen and is used when fibrinogen is under 100 mg/dL.")

q("choose", "A 44-year-old on chemotherapy has a platelet count of 38,000/µL and is actively bleeding from the nose. Which statement by the nurse is accurate?",
  ["'Platelets are given only when the count is below 10,000.' || active bleeding raises the threshold to 50,000",
   "*'With active bleeding, platelets are given under 50,000.'",
   "'Fresh frozen plasma will raise the platelet count.' || plasma replaces clotting factors, not platelets",
   "'Packed red cells are the product that will stop this.' || PRBCs treat anemia and hemorrhage, not low platelets"],
  "Platelets are given under 10,000-20,000/µL, or under 50,000/µL with active bleeding.")

q("abo", "A 36-year-old warehouse worker has type A blood. Which antibody is present in the client's plasma?",
  ["Anti-A || people do not make antibodies against their own antigen",
   "Both anti-A and anti-B || this describes type O",
   "*Anti-B",
   "No ABO antibodies || this describes type AB"],
  "Antibodies target the antigens a person does not have, so type A blood carries anti-B antibodies and can receive A or O red cells.")

q("abo", "A 51-year-old with type AB blood needs packed red cells. Which statement by the nurse shows correct understanding?",
  ["'AB clients can only receive AB red cells.' || AB has no anti-A or anti-B antibodies",
   "'AB clients can receive only type O red cells.' || AB can receive any ABO type",
   "'AB clients have both anti-A and anti-B antibodies.' || that describes type O",
   "*'AB is the universal recipient and can receive any ABO type.'"],
  "Type AB has no anti-A or anti-B antibodies, so it is the universal recipient for red cells.")

q("rh", "A 23-year-old with O-positive blood needs red cells. Which donor units are compatible? " + SATA,
  ["*O positive",
   "*O negative",
   "A positive || type O has anti-A antibodies",
   "B negative || type O has anti-B antibodies",
   "AB positive || type O has both anti-A and anti-B antibodies"],
  "Type O can receive only type O red cells, and an Rh-positive client can receive Rh-positive or Rh-negative.")

q("rh", "A 29-year-old with B-negative blood needs a red cell transfusion. Which donor unit is safe?",
  ["*O negative",
   "B positive || an Rh-negative client receives only Rh-negative red cells",
   "A negative || type B has anti-A antibodies",
   "AB negative || type B has anti-A antibodies"],
  "An Rh-negative client receives only Rh-negative red cells to prevent sensitization to the D antigen; type B can receive B or O, so B negative or O negative is safe.")

q("jw", "A 46-year-old Jehovah's Witness with severe anemia asks what options might be available instead of blood. Which response by the nurse is best?",
  ["'Your family can consent to blood if you become unstable.' || the client's refusal must be respected",
   "'There are no alternatives, so blood is your only option.' || alternatives such as erythropoietin with iron exist",
   "*'Some clients accept options like erythropoietin with iron.'",
   "'All Jehovah's Witnesses accept platelets and plasma.' || these are products they always refuse"],
  "Alternatives for bloodless care include erythropoietin with iron, tranexamic acid and IV fluids; ask each client which fractions they accept.")

q("jw", "The nurse is caring for a 64-year-old Jehovah's Witness after surgery who declines all blood. Which actions are appropriate? " + SATA,
  ["*Use small pediatric tubes and cluster lab draws",
   "*Document the client's wishes clearly in the record",
   "Give whole blood if the client becomes confused || the refusal must be respected",
   "*Monitor the client closely for signs of bleeding",
   "Assume the client accepts albumin and clotting factors || acceptance of fractions is a personal choice; ask each client"],
  "Bloodless care includes clustering labs with small tubes, documenting wishes, monitoring for bleeding and giving emotional and spiritual support; ask each client which fractions they accept.")

q("labs", "A 38-year-old is being prepared for a transfusion. Which statement about pretransfusion testing is accurate?",
  ["'A crossmatch is done first, then the type and screen.' || type and screen comes first",
   "*'Type and screen is done first, then a crossmatch with the donor unit.'",
   "'A CBC (complete blood count) matches the donor unit to the client.' || the crossmatch does this",
   "'No testing is needed if the client knows the blood type.' || always follow blood bank testing"],
  "Type and screen is done first, then a crossmatch checks the donor unit against the client's blood before release.")

q("pre", "A 55-year-old accountant is about to receive a unit of packed red cells. Which equipment should the nurse have at the bedside? " + SATA,
  ["*An IV (intravenous) pump",
   "*Y-tubing with an inline filter",
   "*An 18-20 gauge IV (intravenous) catheter",
   "A bag of D5W (5% dextrose in water) to prime the line || only normal saline is used with blood",
   "A 24-gauge IV (intravenous) catheter || blood needs 18-20 gauge access"],
  "Blood is given through an 18-20 gauge IV with an IV pump and Y-tubing with an inline filter primed with normal saline.")

q("pre", "Two RNs (registered nurses) are checking a unit of blood at the bedside. The client's blood type on the bag does not match the type on the order. What should the nurse do?",
  ["Give the unit, since the client's name matches || every identifier must match",
   "Correct the type on the form and start the blood || never change labels to make them match",
   "*Hold the unit, return it and call the blood bank",
   "Start the blood slowly and watch for a reaction || an unverified unit must not be given"],
  "Two RNs verify the unit at the bedside; if anything does not match, the blood is not given and the blood bank is called.")

q("admin", "A 68-year-old is receiving packed red cells. Which nursing action reflects correct transfusion practice?",
  ["*Stay with the client during the first 15 minutes",
   "Leave the room once the pump is running || the most serious reactions usually happen early",
   "Run the unit fast for the first 15 minutes || blood is run slowly at first",
   "Take vital signs only when the unit is done || vitals are taken at 15 minutes, then hourly"],
  "The nurse stays with the client and runs blood slowly for the first 15 minutes because the most serious reactions usually happen early.")

q("admin", "The nurse is reviewing transfusion timing with a new graduate. Which statements are accurate? " + SATA,
  ["*'Start packed RBCs within 30 minutes of picking them up.'",
   "*'A unit of packed RBCs must be finished within 4 hours.'",
   "'Platelets are given slowly over 4 hours.' || platelets are usually given over 15-30 minutes",
   "*'Check vitals 15 minutes after starting, then every hour.'",
   "'Vitals are only needed if the client complains.' || vitals follow a set schedule"],
  "PRBCs start within 30 minutes of pickup and finish within 4 hours; platelets go over 15-30 minutes; vitals are taken before, at 15 minutes, then hourly.")

q("ns", "A 42-year-old has lactated Ringer's infusing when a unit of blood arrives. Which action is correct?",
  ["Piggyback the blood into the lactated Ringer's line || only normal saline is used with blood",
   "*Hang the blood on Y-tubing primed with 0.9% normal saline",
   "Add the blood to the lactated Ringer's bag to dilute it || never mix other solutions with blood",
   "Change the fluid to D5W (5% dextrose in water) first || only normal saline is used with blood"],
  "0.9% normal saline is the only fluid hung with blood; never mix medications or other solutions with blood.")

q("ns", "A client's IV (intravenous) antibiotic is due while a unit of blood is infusing. Which statement by the nurse shows understanding of blood safety?",
  ["'I'll inject the antibiotic into the blood bag.' || never mix medications with blood",
   "'I'll run the antibiotic through the blood tubing.' || never mix medications with blood",
   "*'No medication goes in with the blood; only normal saline does.'",
   "'I'll dilute the antibiotic with D5W in the Y-tubing.' || only normal saline is used with blood"],
  "Normal saline is the only fluid used with blood; never mix medications or other solutions with blood.")

q("post", "A unit of packed red cells finishes for a 61-year-old with no reaction. What should the nurse do next?",
  ["Send the bag and tubing back to the blood bank || this is done after a reaction",
   "Hang D5W (5% dextrose in water) to keep the vein open || only normal saline is used",
   "*Flush the line with normal saline and document",
   "Stop all monitoring now that the unit is done || delayed reactions can still occur"],
  "After a transfusion, flush the line with normal saline, discard the bag and tubing per policy (usually biohazard), document and watch for delayed reactions.")

q("ahtr", "A 35-year-old is 10 minutes into a unit of blood. Which finding should make the nurse suspect a serious transfusion reaction?",
  ["Blood pressure unchanged from baseline || stable vitals do not suggest a reaction",
   "*New flank pain and dark red urine",
   "A request for a pillow to sleep || this is not a reaction sign",
   "Clear, pale yellow urine || this is a normal finding"],
  "Back or flank pain, dark red urine, low blood pressure, chills, fever and sudden anxiety are signs of a serious reaction.")

q("ahtr", "A transfusion is stopped for a 47-year-old with back pain, dark urine and hypotension. Which complications should the nurse monitor for? " + SATA,
  ["*Shock",
   "*Oozing at the IV (intravenous) site from DIC (disseminated intravascular coagulation)",
   "*Kidney injury",
   "Shingles along one dermatome || this is not a transfusion complication",
   "Rising blood pressure from overload || low BP, not high, signals this reaction"],
  "A serious reaction with back pain, dark urine and low blood pressure can lead to shock, DIC with oozing at the IV site, and kidney injury.")

q("fnh", "A 59-year-old's temperature rises from 37.0°C to 38.2°C with shaking chills 40 minutes into a transfusion. What should the nurse do first?",
  ["Give acetaminophen and keep the blood running || the transfusion must be stopped first",
   "Speed up the unit so it finishes sooner || this gives more of the product",
   "*Stop the transfusion and assess the client",
   "Give epinephrine for anaphylaxis || there are no airway or breathing signs"],
  "Any temperature rise of 1°C (about 2°F) or more means stop and assess; acetaminophen may be given as ordered, and the blood restarts only if the provider approves.")

q("allergy", "A 31-year-old receiving platelets develops hives and itching on the arms with stable vitals. After the nurse stops the transfusion, which statement is accurate?",
  ["'This is minor, so I'll restart it right away.' || it restarts only if symptoms resolve and the provider approves",
   "*'It may restart only if symptoms resolve and the provider approves.'",
   "'I'll give furosemide for the hives.' || an antihistamine is given as ordered",
   "'This unit can never be restarted under any circumstances.' || it may restart with resolution and provider approval"],
  "For hives and itching, stop the transfusion, notify the provider and give an antihistamine as ordered; it may restart only if symptoms resolve and the provider approves.")

q("lung", "An 80-year-old with heart failure receiving blood develops crackles, distended neck veins and a rising blood pressure. Which action should the nurse take first?",
  ["Lay the client flat to rest || the client should sit upright",
   "Increase the rate to finish the unit || this adds more fluid",
   "Give an antihistamine as ordered || these are fluid overload signs, not allergy",
   "*Stop the transfusion"],
  "Crackles, JVD, high blood pressure and shortness of breath are fluid overload signs: stop the transfusion, sit the client upright, give oxygen and a diuretic as ordered.")

q("delayed", "A 26-year-old who received blood 10 days ago calls the clinic. Which reported symptom should the nurse recognize as a possible delayed reaction?",
  ["*New dark urine and itching",
   "Feeling well with normal energy || this is not a reaction sign",
   "A mild bruise healed at the IV site || this is not a reaction sign",
   "Good appetite since discharge || this is not a reaction sign"],
  "Reactions can appear days to weeks later and are usually milder; clients should report fever, itching or rash, dark urine and shortness of breath.")

q("steps", "A 52-year-old receiving blood suddenly reports chest pain. After stopping the transfusion and keeping the IV (intravenous) open, which action comes next?",
  ["Collect urine and blood samples || samples come after notifying the provider and blood bank",
   "Document the reaction || documentation comes later in the sequence",
   "*Notify the provider",
   "Advise the client about prevention || this is the last step"],
  "The order is stop, notify the provider, notify the blood bank, collect samples, document and advise the client.")

q("steps", "A transfusion is stopped for a suspected reaction. Which actions are correct when keeping the line open? " + SATA,
  ["*Use normal saline",
   "*Hang it through new tubing",
   "Flush saline through the blood tubing || leftover blood would go into the client",
   "*Run about 250 mL of saline as ordered",
   "Hang D5W (5% dextrose in water) instead || only normal saline is used with blood"],
  "Keep the line open with normal saline (about 250 mL) through new tubing so leftover blood does not reach the client.")
