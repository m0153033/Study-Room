T = "vision"; SET = "20261123"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("sensory", "The nurse is caring for four clients on a medical unit. Which client is experiencing sensory DEPRIVATION?", [
  "A client with blurred vision from a cataract || Part of the sense is impaired, which is a deficit",
  "A client with low vision who needs glasses || Partial impairment is a sensory deficit",
  "*A client who is totally blind",
  "An ICU client confused by constant alarms and lights || Inability to process excess stimuli is overload"],
  "Sensory deprivation is the absence of a sense, such as total blindness. A deficit is partial impairment (low vision), and overload is the inability to process excessive or multiple stimuli.")

q("history", "A 66-year-old reports blurry vision in the right eye. Which questions belong in the ocular history? " + SATA, [
  "*When did you first notice the change?",
  "*Have you tried treating it yourself?",
  "*How is it affecting your daily activities?",
  "*Have you ever had eye surgery?",
  "Which style of glasses frame do you prefer? || Frame preference is not part of the ocular history"],
  "The ocular history covers the client's view of the problem, acuity changes, pain, whether both eyes are affected, discharge, onset, self-treatment, ADLs, other conditions, eye surgery and family members with similar symptoms.")

q("external", "A nursing student documents external eye findings. Which term-definition pairing is correct?", [
  "Ectropion - eyelashes turning inward || Ectropion is the lower lid turning outward",
  "*Ptosis - drooping of the upper eyelid",
  "Nystagmus - drooping of the upper eyelid || Nystagmus is involuntary rhythmic eye oscillation",
  "Trichiasis - lower lid turning outward || Trichiasis is lashes turning inward"],
  "Ptosis is a drooping upper eyelid. Ectropion is the lower lid turning outward, trichiasis is lashes turning inward, and nystagmus is involuntary rhythmic oscillation of the eyes.")

q("acuity", "The nurse is preparing to test a 40-year-old's distance vision. Which action is correct?", [
  "Have the client stand 14 feet from the Snellen chart || Distance vision is tested at 20 feet",
  "Test both eyes together only, 20 feet from the chart || Each eye is tested separately",
  "Hold the Snellen chart 14 inches from the client's face || 14 inches is for near vision",
  "*Test each eye separately, 20 feet from a Snellen chart"],
  "Distance vision is tested at 20 feet with a standardized Snellen chart, and near vision at 14 inches. Each eye is tested separately. Acuity tests cranial nerve II (optic).")

q("color", "A 74-year-old taking digoxin says colors have started to look different. Which response by the nurse reflects the lecture?", [
  "*Digoxin can cause acquired color loss; screening uses Ishihara plates",
  "Red-green deficiency is inherited, so a new change is expected now || A new change suggests an acquired cause",
  "This points to open-angle glaucoma, a central vision problem || Glaucoma affects peripheral vision",
  "Color vision is screened with a Snellen chart at 20 feet || Ishihara plates screen color vision"],
  "Digitalis/digoxin and cataracts can cause acquired color-vision loss. Ishihara polychromatic plates screen for color-vision deficiency.")

q("amsler", "Which statement by a client with macular degeneration shows correct understanding of the home Amsler grid?", [
  "'I'll check it once a year before my eye exam.' || The grid is used daily",
  "'It tells me what my eye pressure is.' || Tonometry measures eye pressure",
  "*'I'll look at it every day and call if lines look wavy.'",
  "'Wavy lines are normal as long as I can see the center.' || Wavy lines or faded squares are abnormal"],
  "The Amsler grid detects macular changes early. It should be used daily at home, and faded squares or wavy lines are reported.")

q("scopes", "A 62-year-old with long-standing hypertension has a direct ophthalmoscopy exam. Which finding is linked to the client's hypertension?", [
  "Colored halos around lights || Halos are a symptom of angle-closure glaucoma, not a scope finding",
  "*Flame-shaped hemorrhages",
  "Small yellow globular drusen || Drusen are linked to macular degeneration",
  "Purulent crusted discharge || This is a bacterial conjunctivitis finding"],
  "Direct ophthalmoscopy, done in a darkened room, looks for intraretinal hemorrhages (flame-shaped with hypertension), lipid deposits and drusen.")

q("tono", "A 60-year-old with a family history of glaucoma is scheduled for tonometry. Which explanation is accurate?", [
  "'You'll check a grid of squares at home each day for it.' || That describes the Amsler grid",
  "'You'll read letters on a chart from 20 feet away, one eye at a time.' || That is a Snellen acuity test",
  "'You'll name numbers hidden in colored plates.' || That is Ishihara color testing",
  "*'Numbing drops go in; then the cornea is gently flattened.'"],
  "Tonometry is the most common and reliable way to measure IOP. It is painless: numbing drops are placed, the client sits at the slit lamp, and the provider gently flattens a small area of cornea.")

q("cataract", "A 76-year-old with diabetes reports vision that has slowly become hazy and glare from headlights when driving at night. What is the most likely cause?", [
  "*Cataract, a clouding of the eye's lens",
  "Angle-closure glaucoma, an eye emergency || Angle-closure is sudden with severe pain and vomiting",
  "Macular degeneration, loss of the macula || MD causes central vision loss, not lens clouding",
  "Conjunctivitis, inflammation of the conjunctiva || Conjunctivitis doesn't cause night glare"],
  "A cataract is clouding of the lens that makes vision blurry, hazy or less colorful; it develops slowly. Risks include older age and diabetes. Glare with night driving is a classic symptom.")

q("cataract", "Which client statements are consistent with cataracts? " + SATA, [
  "*'Everything looks blurry and hazy.'",
  "*'Colors don't look as bright as they used to.'",
  "*'Sometimes I see double.'",
  "'My eyes are itchy and watery.' || Itching points to allergic conjunctivitis",
  "'I suddenly lost the center of my vision.' || Central vision loss points to macular degeneration"],
  "Cataract findings include decreased or blurred vision (the priority finding), abnormal color perception, glare when driving at night, and diplopia.")

q("catcare", "Two hours after cataract surgery, a client asks to lie flat on the operative side to sleep. Which response is best?", [
  "'That's fine; lying on that side helps protect the new eye.' || The client stays off the operative side",
  "*'Keep the bed raised 30-40 degrees, off the operative side.'",
  "'Lie flat on your back for the first day.' || The client should not be flat",
  "'Lower your head below your feet to rest.' || Trendelenburg is not used"],
  "After cataract surgery, position the client with the HOB at 30-40 degrees and off the operative side, not flat.")

q("catcare", "The nurse reviews discharge teaching after cataract surgery. Which statement by the client needs more teaching?", [
  "'I'll wear sunglasses to help with light sensitivity.' || Correct; sunglasses reduce photophobia",
  "'I'll call for cough medicine if I start coughing.' || Correct; coughing raises IOP",
  "*'I'll bend over at the waist to put my shoes on.'",
  "'I won't lift anything heavier than 5 pounds.' || Correct; lifting over 5 lb raises IOP"],
  "To prevent a rise in IOP after cataract surgery, avoid bending at the waist, coughing and lifting over 5 lb. Sunglasses reduce photophobia.")

q("blind", "A 70-year-old applying for disability help asks what counts as legal blindness. Which eye exam result would qualify?", [
  "20/200 in the right eye and 20/20 in the left || Legal blindness is based on the better eye",
  "Best-corrected acuity of 20/100 in the better eye || This is better than 20/200",
  "*Widest visual field of 18 degrees with 20/40 acuity",
  "A visual field of 60 degrees in both eyes || The field must be 20 degrees or less"],
  "Legal blindness is best-corrected acuity of 20/200 or worse in the better eye, OR a widest visual field of 20 degrees or less. About half of legally blind clients are 65 or older.")

q("blindcare", "The nurse enters the room of a 70-year-old who is blind to deliver a lunch tray. Which actions are appropriate? " + SATA, [
  "*State your name before touching the client",
  "*Describe the tray using the clock method",
  "*Tell the client when you are leaving the room",
  "*Ask, 'How can I help you?'",
  "Move the client's belongings to tidy the room || Items should stay where the client can find them"],
  "Introduce yourself, state when you leave, describe item locations (or use the clock method), keep devices nearby and ask 'How can I help you?'")

q("blindcare", "The nurse observes an assistive staff member walking with a client who is blind. Which action needs correction?", [
  "Letting the client hold the staff member's arm || This is correct technique",
  "Walking a half step ahead of the client || The client walks a half step behind, so this is correct",
  "Moving a cord out of the hallway path || Removing fall hazards is correct",
  "*Holding the client's wrist and pulling forward"],
  "When guiding a blind client, the client holds the nurse's arm and walks one-half step behind. Keep the environment free of fall hazards such as cords.")

q("glauc", "A 64-year-old has elevated eye pressure on a routine exam and says, 'But my vision seems fine.' Which response by the nurse is accurate?", [
  "'Glaucoma always causes pain early, so you're fine.' || Open-angle glaucoma is usually painless",
  "*'It's often silent, and lost vision can't be restored.'",
  "'Glaucoma is cured with a new pair of glasses.' || Glasses don't cure glaucoma",
  "'Glaucoma takes away your central vision first.' || Open-angle glaucoma causes peripheral loss"],
  "Primary open-angle glaucoma is the most common type; pressure builds slowly with gradual peripheral loss and usually no other symptoms ('silent thief of sight'). Vision loss is irreversible, so early detection matters.")

q("glauc", "The eye clinic nurse receives four phone calls. Which client should the nurse treat as an emergency?", [
  "A client with itchy, watery eyes after gardening || Itching suggests allergic conjunctivitis",
  "A client with gradual glare when driving at night || This suggests a cataract",
  "A client with peripheral vision slowly narrowing over a year || This is gradual open-angle loss",
  "*A client with sudden severe eye pain, vomiting and colored halos"],
  "Sudden severe eye pain, nausea and vomiting, blurred vision and colored halos point to primary angle-closure glaucoma, a medical emergency.")

q("glaucare", "The nurse reviews teaching after a laser iridotomy. Which client statement needs more teaching?", [
  "'I'll keep the head of my bed raised.' || Correct; HOB 30-40 degrees",
  "*'I'll lie flat for the first 24 hours.'",
  "'I won't lift more than 5 pounds.' || Correct; avoid lifting over 5 lb",
  "'I'll take my pain medicine as needed.' || Correct; analgesics as needed"],
  "Laser iridotomy creates a hole in the iris so aqueous humor can flow out. Afterward: HOB 30-40 degrees, off the operative side, analgesics as needed, and avoid bending, coughing or lifting over 5 lb. The client is not kept flat.")

q("glaucare", "A client with open-angle glaucoma says, 'My vision feels normal, so I stopped my eye drops.' Which response is best?", [
  "*'Keep using them as prescribed; they lower eye pressure.'",
  "'That's fine once your vision feels normal again.' || Drops are not stopped when vision feels normal",
  "'Use them only on days when your eyes hurt or feel tired.' || Drops are taken as prescribed, not for pain",
  "'Double the dose when you restart them next week.' || Dosing is not changed by the client"],
  "Open-angle glaucoma teaching: take IOP-lowering drops as prescribed, wear sunglasses, avoid bending and coughing, and report redness, drainage, floaters or flashes of light.")

q("glaumed", "A client with open-angle glaucoma is prescribed timolol eye drops. Which instruction matches this medication?", [
  "'Use 1 drop 3 times a day for 7 days only.' || That is the moxifloxacin regimen",
  "'Use it as needed for dryness.' || That describes an ocular lubricant",
  "*'Use 1 drop twice a day, such as 10 AM and 10 PM.'",
  "'It's injected into the eye every 4-6 weeks.' || That is the wet MD injection"],
  "Timolol is an ophthalmic beta blocker given as 1 drop twice daily (for example 10 AM and 10 PM) for open-angle glaucoma and ocular hypertension.")

q("drops", "A nursing student asks why only one eye drop is instilled at a time. Which explanation is accurate?", [
  "'One drop is about 100 mcL, so it fills the eye.' || One drop is 20-35 mcL",
  "'Extra drops absorb through the skin.' || Eye drops are not absorbed through the skin",
  "*'The sac holds about 50 mcL, and one drop is 20-35 mcL.'",
  "'The eye holds several drops at once, so one is enough.' || The sac holds only about 50 mcL"],
  "The conjunctival sac holds about 50 mcL and one drop is 20-35 mcL. Tearing, blinking and drainage can dilute or expel a drop, so technique matters.")

q("drops", "The nurse watches a 68-year-old instill two prescribed eye drops at home. Which actions are correct? " + SATA, [
  "*Washes hands before starting",
  "*Tilts the head back and looks up",
  "*Waits 5 minutes before the second drop",
  "Touches the tip to the eyelid to aim || The tip should never touch the eye",
  "*Recaps the bottle after use"],
  "Correct technique: hand hygiene, remove contacts, head back and look up, pull down the lower lid to form a pocket, don't touch the tip, recap. Wait 5 minutes between different drops.")

q("md", "An 82-year-old with macular degeneration says, 'I can see the edges of the room but not the face in front of me.' The nurse understands that:", [
  "Macular degeneration takes peripheral vision first || Peripheral vision may stay intact",
  "*This fits central loss with intact peripheral vision",
  "This is curable with laser surgery || MD isn't curable",
  "Only night vision is affected in this disease || Central vision is lost"],
  "The macula is the central part of the retina. MD causes central vision loss while peripheral vision may stay intact. It is the leading cause of irreversible blindness worldwide and isn't curable.")

q("md", "A 77-year-old who smokes has macular degeneration. Which teaching is appropriate? " + SATA, [
  "*Stop smoking and avoid secondhand smoke",
  "*Use a handheld electronic magnifier or e-reader",
  "*Check an Amsler grid at home daily",
  "Wear an eye patch at night || Patching is not part of MD teaching",
  "Expect surgery to cure the disease || MD isn't curable"],
  "MD teaching includes visual aids such as handheld electronic magnifiers or e-readers, daily Amsler grid checks, and smoking cessation. Smoking and secondhand smoke are risk factors.")

q("mdtypes", "A client with wet macular degeneration asks why she needs an eye injection every 4-6 weeks. Which response is accurate?", [
  "'It creates a hole in the iris for fluid to drain.' || That is laser iridotomy",
  "'It replaces the cloudy lens.' || That is cataract surgery",
  "'It cures the disease after a few doses.' || It slows vision loss; it doesn't cure",
  "*'It inhibits a growth factor to slow vision loss.'"],
  "In wet MD, abnormal vessels leak fluid and blood and scar. A prescribed inhibitor of endothelial growth factor given by intravitreal injection every 4-6 weeks slows vision loss. Dry MD has no treatment.")

q("conj", "A 28-year-old has red eyes with thin, watery discharge and no itching. Which type and treatment fit best?", [
  "Bacterial; moxifloxacin drops are needed || Bacterial drainage is purulent and may crust",
  "*Viral; a lubricant can ease irritation",
  "Allergic; itching is the main feature || The client has no itching",
  "Viral; antibiotic drops will cure it || Antibiotics treat bacterial, not viral, infection"],
  "Viral conjunctivitis has serous/watery drainage; bacterial is purulent and may crust; allergic is defined by itching. An ocular lubricant eases dryness and irritation but doesn't treat bacterial infection.")

q("conj", "A client with purulent, crusted eye discharge is prescribed moxifloxacin drops. Which instruction matches the slides?", [
  "*'Use 1 drop 3 times a day for 7 days.'",
  "'Use 1 drop twice a day long term.' || That is the timolol regimen",
  "'Use it only as needed for dryness.' || That describes an ocular lubricant",
  "'It's injected every 4-6 weeks.' || That is the wet MD treatment"],
  "Purulent, crusting discharge suggests bacterial conjunctivitis. The slides list moxifloxacin antibiotic drops, 1 drop 3 times a day for 7 days.")

q("conjteach", "A 22-year-old with conjunctivitis wears contact lenses and mascara. Which teaching is correct? " + SATA, [
  "*Throw away your current mascara",
  "*Stop wearing contacts until it clears",
  "*Use your own washcloths and towels",
  "Share your eye drops with your roommate if her eyes get red || Eye drops are never shared",
  "*Don't touch your eye with the dropper"],
  "Conjunctivitis teaching: discard eye makeup (especially mascara), don't share washcloths or towels, stop contact lenses until it clears, meticulous hand hygiene, and don't touch the eye with the dropper.")

q("promo", "The nurse teaches a community group about nutrition and eye health. Which statement is accurate?", [
  "'Vitamin A causes cataracts.' || Vitamin A deficiency causes dryness; it doesn't cause cataracts",
  "'Caffeine improves night vision and eye health.' || This is not supported",
  "'Vitamin A deficiency increases tear production.' || Deficiency causes eye dryness",
  "*'Lutein and beta-carotene support retinal function.'"],
  "Vitamin A deficiency can cause eye dryness, and lutein and beta-carotene help maintain retinal function.")
