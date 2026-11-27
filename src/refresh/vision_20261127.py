T = "vision"; SET = "20261127"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("sensory", "A nursing student reviews types of sensory alteration with the nurse. Which student statement needs correction?", [
  "'Overload is being unable to process excess stimuli.' || This is accurate; overload is the inability to process excessive or multiple stimuli",
  "'A deficit means part of a sense is impaired.' || This is accurate; low vision is an example of a deficit",
  "*'Deprivation means a sense is only partly impaired.'",
  "'Overload is sometimes called ICU psychosis.' || This is accurate; overload in the ICU is sometimes called ICU psychosis"],
  "Sensory deprivation is the absence of a sense, such as total blindness. A deficit is partial impairment, such as low vision, and overload is the inability to process excessive or multiple stimuli (sometimes called ICU psychosis).")

q("history", "A 52-year-old bus driver with diabetes comes to the clinic for a foot check and reports no vision problems. Which action reflects the nurse's role?", [
  "Skip eye follow-up since there are no vision complaints || Diabetes places the client at risk even without symptoms",
  "*Identify the client as at risk and refer to an eye-care specialist",
  "Prescribe a new pair of glasses for night driving || Prescribing glasses is not part of the nurse's role",
  "Perform a laser iridotomy to prevent glaucoma || A procedure like this is not part of the nurse's role"],
  "The nurse's role includes obtaining an ocular history, identifying at-risk clients (such as those with diabetes or hypertension) and referring them, preventing further vision loss, and helping clients adapt.")

q("external", "During an admission assessment of a 79-year-old, the nurse notes the client's eyelashes are turned inward toward the eye. Which term should the nurse document?", [
  "Ectropion || Ectropion is the lower lid turning outward",
  "Ptosis || Ptosis is drooping of the upper eyelid",
  "*Trichiasis",
  "Nystagmus || Nystagmus is involuntary rhythmic oscillation of the eyes"],
  "Trichiasis is eyelashes turning inward. Ectropion is the lower lid turning outward, ptosis is a drooping upper eyelid, and nystagmus is involuntary rhythmic oscillation of the eyeballs.")

q("acuity", "A new nurse is testing a client's near vision. Which action by the new nurse needs correction?", [
  "Holding the reading card 14 inches from the client || Near vision is correctly tested at 14 inches",
  "*Testing both eyes together to save time",
  "Using a number card for a client who can't read English || Numbers or pictures are correct for this client",
  "Explaining that the test checks the optic nerve || Visual acuity does evaluate cranial nerve II (optic)"],
  "Near vision is tested at 14 inches and distance vision at 20 feet with a Snellen chart. Each eye is tested separately. Use pictures or numbers if the client can't read English. Acuity evaluates cranial nerve II (optic).")

q("color", "A father asks why his son has red-green color deficiency but his daughter does not. Which statement by the nurse is accurate?", [
  "*'Inherited red-green deficiency affects about 8% of men and 0.5% of women.'",
  "'Red-green deficiency is caused by taking digoxin in childhood.' || Digoxin causes acquired, not inherited, color loss",
  "'It affects women far more often than men.' || It is far more common in men (8%) than women (0.5%)",
  "'It is screened using an Amsler grid at home.' || Color vision is screened with Ishihara polychromatic plates"],
  "Inherited red-green color deficiency affects about 8% of men versus 0.5% of women. Digitalis/digoxin and cataracts can cause acquired color loss. Ishihara polychromatic plates screen for color-vision deficiency.")

q("amsler", "A 69-year-old retired teacher asks what the Amsler grid looks like. Which description by the nurse is accurate?", [
  "'A booklet of colored plates with hidden numbers.' || This describes Ishihara plates for color vision",
  "'A chart of letters you read from 20 feet away.' || This describes the Snellen chart for distance acuity",
  "*'A grid of identical squares with a center point to focus on.'",
  "'A lighted scope with rotating lenses.' || This describes the direct ophthalmoscope"],
  "The Amsler grid is a geometric grid of identical squares with a central fixation point. It detects macular changes early; faded squares or wavy lines are abnormal.")

q("scopes", "A 58-year-old with diabetes has a direct ophthalmoscopy exam. Which finding may be linked to the client's diabetes?", [
  "Flame-shaped hemorrhages || Flame-shaped hemorrhages are linked to hypertension",
  "*Yellow lipid deposits on the retina",
  "Purulent discharge with crusting || This is an external finding of bacterial conjunctivitis",
  "Faded squares on the Amsler grid || This is a home grid finding, not an ophthalmoscopy finding"],
  "Direct ophthalmoscopy, done in a darkened room, looks for intraretinal hemorrhages (flame-shaped with hypertension), yellow lipid deposits (linked to high cholesterol or diabetes) and drusen (macular degeneration).")

q("tono", "A client with glaucoma has intraocular pressure measured at each clinic visit. Why does the nurse follow these results over time?", [
  "Results never change once glaucoma is diagnosed || Results can change with progression or therapy",
  "*Trends can show disease progression or response to therapy",
  "A single reading is enough to stop treatment || Following trends, not one reading, guides care",
  "Trends show the client's color-vision changes || Tonometry measures intraocular pressure, not color vision"],
  "Tonometry measures IOP (intraocular pressure) and determines glaucoma risk. The nurse follows result trends over time, which can show disease progression or response to therapy.")

q("cataract", "A 50-year-old accountant asks the nurse about cataracts. Which statement by the nurse is accurate?", [
  "*'About half of people have a cataract by age 75.'",
  "'Cataracts usually appear suddenly overnight.' || Cataracts develop slowly",
  "'A cataract can only form in one eye.' || Cataracts develop in one or both eyes",
  "'Cataracts are caused by high eye pressure.' || Elevated IOP describes glaucoma, not cataract"],
  "A cataract is clouding of the eye's lens that makes vision blurry, hazy or less colorful. Cataracts develop slowly in one or both eyes, and about half of people have one by age 75.")

q("cataract", "The nurse reviews health histories at a clinic. Which clients have a risk factor for cataracts? " + SATA, [
  "*A 60-year-old who had radiation treatment",
  "*A former boxer with a past eye injury",
  "*A 55-year-old with diabetes mellitus",
  "A healthy 24-year-old runner || Young age with no chronic disease, trauma or radiation is not a listed risk",
  "*An 81-year-old retired farmer"],
  "Cataract risk factors include eye trauma, diabetes or other chronic disease, older age and radiation.")

q("catcare", "Mydriatic drops are ordered before a client's cataract surgery. Which description of these drops is accurate?", [
  "Beta blocker drops that lower eye pressure || This describes timolol, not a mydriatic",
  "Antibiotic drops that treat infection || This describes moxifloxacin, not a mydriatic",
  "*Anticholinergic drops that dilate the pupil",
  "Lubricant drops that moisten the eye || This describes an ocular lubricant, not a mydriatic"],
  "Mydriatics are anticholinergic drops that dilate the pupil before cataract surgery. The nurse dims the lights afterward.")

q("catcare", "A 73-year-old returns to the unit after cataract surgery. Which nursing actions are appropriate? " + SATA, [
  "*Assess placement of the eye patch",
  "*Assist the client with ambulation and toileting",
  "*Give analgesics as needed for eye pain",
  "Keep the client flat in bed for the first day || The HOB is raised 30-40 degrees, not flat",
  "Encourage deep coughing every hour || Coughing raises IOP and should be avoided"],
  "After cataract surgery: HOB 30-40 degrees off the operative side, give analgesics as needed, assess eye-patch placement, assist with ambulation and toileting, and avoid bending, coughing and lifting over 5 lb.")

q("blind", "A 45-year-old electrician who recently became blind after an injury is quiet and tearful. Which nursing action best promotes coping?", [
  "Insist the client begin Braille lessons today || The client needs time to process the loss first",
  "*Allow time and support for processing and acceptance",
  "Avoid any discussion of the vision loss || Support for processing the loss promotes coping",
  "Request a psychiatric consult for the tears || Grieving is an expected response to a major loss"],
  "New blindness is a major loss, and the client may move through grieving. The nurse promotes coping by allowing time and support for processing, acceptance and rehabilitation.")

q("blindcare", "A client who is blind is choosing lunch from the hospital menu. Which action by the nurse is best?", [
  "Choose a meal for the client to save time || This removes the client's choice",
  "Speak to the visiting daughter instead || Speak directly to the client as with anyone",
  "*Offer to read the menu choices aloud",
  "Avoid words like 'look' while talking || Words like 'see' and 'look' are fine to use"],
  "For a client with vision loss, offer to read written material such as menus, speak honestly and respectfully as with anyone, and keep the environment free of fall hazards.")

q("blindcare", "The nurse observes a nursing assistant caring for a client who is blind. Which action needs correction?", [
  "Saying 'I'm leaving now' before walking out || Stating when you leave is correct",
  "Describing the water cup as being at 3 o'clock || The clock method is correct",
  "*Touching the client's arm before saying her name",
  "Keeping the call light within the client's reach || Keeping devices nearby is correct"],
  "When caring for a blind client, introduce yourself before touching the client, state when you are leaving, describe item locations or use the clock method, and keep devices nearby.")

q("glauc", "Which explanation of what causes primary angle-closure glaucoma is accurate?", [
  "Drusen increase in size and number || This describes dry macular degeneration",
  "*Pupil dilation or a bulging lens",
  "Clouding of the lens over many years || This describes a cataract",
  "Bacteria on the exposed conjunctiva || This describes bacterial conjunctivitis"],
  "Primary angle-closure (narrow-angle) glaucoma is a medical emergency caused by pupil dilation or a bulging lens. It presents with sudden severe eye pain, nausea and vomiting, blurred vision and colored halos.")

q("glauc", "A nursing student explains glaucoma to a peer. Which statement needs correction?", [
  "'It's a problem with draining the fluid the eye makes.' || This is accurate; poor drainage lets pressure build",
  "'Open-angle glaucoma is called the silent thief of sight.' || This is accurate; it usually has no symptoms early",
  "*'Vision lost to glaucoma can be restored with treatment.'",
  "'The slides also call glaucoma ocular hypertension.' || This is accurate per the slides"],
  "Glaucoma is a group of conditions with elevated IOP caused by a problem with drainage of the fluid the eye produces. Vision loss is irreversible, so early detection matters. Open-angle glaucoma is the 'silent thief of sight.'")

q("glaucare", "The nurse checks on four clients after laser iridotomy. Which client is following post-procedure instructions?", [
  "A client bending to pick up a laundry basket || Bending raises IOP and should be avoided",
  "A client carrying a 10-lb bag of groceries || Lifting over 5 lb should be avoided",
  "*A client resting with the HOB at 35 degrees",
  "A client lying flat on the operative side || The client stays off the operative side and not flat"],
  "After laser iridotomy, use the same precautions as cataract surgery: HOB 30-40 degrees, off the operative side, analgesics as needed, and avoid bending, coughing or lifting over 5 lb.")

q("glaucare", "A 61-year-old librarian with open-angle glaucoma asks which changes to report to the provider. Which should the nurse include? " + SATA, [
  "*Eye redness",
  "*Drainage from the eye",
  "*Sudden floaters",
  "*Flashes of light",
  "Needing sunglasses outdoors || Sunglasses are recommended to prevent photophobia"],
  "Open-angle glaucoma teaching: take IOP-lowering drops as prescribed, wear sunglasses to prevent photophobia, avoid bending and coughing, and report redness, drainage, floaters or flashes of light.")

q("glaumed", "The nurse reviews a client's eye medications. Which drop is an ophthalmic beta blocker?", [
  "Brinzolamide || Brinzolamide works by reducing aqueous-humor formation",
  "Moxifloxacin || Moxifloxacin is an antibiotic for bacterial conjunctivitis",
  "*Timolol",
  "Ocular lubricant || A lubricant moistens the eye"],
  "Timolol is an ophthalmic beta blocker given 1 drop twice daily for open-angle glaucoma and ocular hypertension. Brinzolamide reduces aqueous-humor formation and is indicated for both open- and angle-closure glaucoma.")

q("drops", "Right after the nurse instills an eye drop, the client blinks hard and tears. The nurse understands that:", [
  "Blinking helps the eye absorb more medication || Blinking can expel the drop",
  "*Tearing and blinking can dilute or expel the drop",
  "Tearing shows the wrong drop was given || Tearing does not mean a wrong medication",
  "The eye holds several drops, so it doesn't matter || The sac holds only about 50 mcL"],
  "The conjunctival sac holds about 50 mcL and one drop is 20-35 mcL. Tearing, blinking and drainage can dilute or expel a drop, so technique matters.")

q("drops", "A 45-year-old teacher who wears contact lenses has eye drops ordered. Which action should the nurse take before instilling the drop?", [
  "Rest the bottle tip on the lower lid to steady it || The tip should never touch the eye",
  "Have the client look down at the floor || The client tilts the head back and looks up",
  "*Have the client remove the contact lenses",
  "Lift the upper lid to form a pocket || The lower lid is pulled down to form the pocket"],
  "Eye-drop steps: hand hygiene, remove contact lenses, tilt the head back and look up, pull down the lower lid to form a pocket, don't touch the tip, and recap.")

q("md", "A family member asks the nurse about macular degeneration. Which statement by the nurse is accurate?", [
  "*'It's the leading cause of irreversible blindness worldwide.'",
  "'It can be cured with surgery if found early.' || Macular degeneration isn't curable",
  "'It takes away side vision before central vision.' || It causes central vision loss",
  "'It's caused by bacteria on the conjunctiva.' || The macula is the central part of the retina"],
  "The macula is the central part of the retina. Macular degeneration causes central vision loss, may leave peripheral vision intact, is the leading cause of irreversible blindness worldwide and isn't curable.")

q("md", "The nurse reviews four clients' histories. Which client has the MOST risk factors for macular degeneration?", [
  "A 25-year-old nonsmoker with no family history || Young age without other listed risks",
  "A 40-year-old nonsmoker with seasonal allergies || Allergies are not a listed risk factor",
  "*An 80-year-old white smoker with heart disease",
  "A 30-year-old with a past eye infection || Infection is not a listed risk factor"],
  "Macular degeneration risk factors include increasing age, genetics/family history, white ethnicity, cardiovascular disease, and smoking or secondhand smoke.")

q("mdtypes", "A 74-year-old with DRY macular degeneration asks about the treatment plan. Which response is accurate?", [
  "'You'll get an eye injection every 4-6 weeks.' || Injections are used for wet macular degeneration",
  "'A laser will make a hole in your iris.' || Iridotomy is for angle-closure glaucoma",
  "*'The focus is on visual aids and monitoring.'",
  "'Antibiotic drops will stop the drusen.' || Antibiotic drops treat bacterial conjunctivitis"],
  "Dry macular degeneration is the most common type; drusen increase in size and number (atrophy). It has no treatment or cure, so the goal is visual aids and monitoring.")

q("conj", "A 19-year-old college student has red eyes with drainage and says the main problem is intense itching. Which type of conjunctivitis is most likely?", [
  "Bacterial || Bacterial is marked by purulent discharge that may crust",
  "Viral || Viral is marked by serous, watery drainage",
  "*Allergic",
  "Angle-closure || Angle-closure is a glaucoma emergency, not conjunctivitis"],
  "Allergic conjunctivitis drainage ranges from watery to thick, and itching is the defining feature. Bacterial is purulent and may crust; viral is serous or watery.")

q("conj", "A client with bacterial conjunctivitis asks to use an ocular lubricant instead of the prescribed antibiotic drops. Which response is best?", [
  "'Yes, the lubricant treats the infection just as well.' || A lubricant does not treat bacterial infection",
  "*'A lubricant moistens the eye but won't treat the infection.'",
  "'Use the lubricant and stop the antibiotic early.' || The antibiotic is used as prescribed",
  "'Lubricants are only used for glaucoma.' || Lubricants ease viral or allergic symptoms"],
  "Bacterial conjunctivitis is treated with moxifloxacin antibiotic drops, 1 drop 3 times a day for 7 days. An ocular lubricant moistens the eye and eases dryness and irritation but doesn't treat bacterial infection.")

q("conjteach", "A daycare worker with conjunctivitis asks what can ease eye discomfort. Which response by the nurse is appropriate?", [
  "'Patch the eye for a week.' || Patching is not a listed intervention",
  "'Keep wearing contacts to protect the eye.' || Contact lenses are stopped until it clears",
  "*'Apply cold or warm compresses for comfort.'",
  "'Rub your eyes gently with a family towel.' || Washcloths and towels should not be shared"],
  "Priority conjunctivitis interventions: give prescribed eye drops, maintain strict infection control, and apply cold or warm compresses. Teaching includes not sharing towels and stopping contacts until it clears.")

q("promo", "At a health fair, a 38-year-old asks how often she needs an eye exam. Which response by the nurse is accurate?", [
  "'Everyone needs one exactly every 10 years.' || Frequency is individualized, not one fixed interval",
  "'Only when you notice a vision change.' || Routine exams are part of health promotion",
  "'Only children need routine eye exams.' || Eye checks are a concern across the lifespan",
  "*'It depends on your age, race/ethnicity and health.'"],
  "Eye exam frequency depends on race/ethnicity, age and health conditions. Health promotion also includes eye protection, avoiding smoking and vaping, managing chronic disease and asking about family history.")
