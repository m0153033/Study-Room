T = "resp"; SET = "20261123"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("anat", "A 30-year-old client has seasonal hay fever with sneezing and a stuffy nose. Which part of the respiratory tract is affected?",
  ["The alveoli, located in the lower respiratory tract || Alveoli are lower-tract structures, affected in diseases such as COPD",
   "*The upper tract, including the nasal lining",
   "The bronchioles, located in the lower tract || Bronchioles are lower-tract structures involved in asthma",
   "The lungs and bronchi of the lower tract || These are lower-tract structures"],
  "Upper tract: nose, sinuses, pharynx, larynx, trachea; disorders include hay fever, rhinitis and cold/flu. Lower tract: lungs, bronchi, bronchioles, alveoli; disorders include asthma and COPD.")

q("copd", "A nurse is teaching a 67-year-old client newly diagnosed with COPD (chronic obstructive pulmonary disease). Which statements are accurate? " + SATA,
  ["*COPD is progressive and irreversible",
   "*COPD makes exhalation difficult",
   "*Emphysema involves damage to the alveoli",
   "*Chronic bronchitis involves damage to the airways",
   "COPD airway obstruction fully reverses with treatment || Reversible obstruction describes asthma"],
  "Asthma airway obstruction is reversible; COPD is progressive and irreversible and makes exhalation difficult. Emphysema = alveolar damage; chronic bronchitis = airway damage.")

q("mast", "A client with allergies is exposed to pollen and develops airway narrowing with mucus. Which process explains this?",
  ["Red blood cells release acetylcholine that narrows the airway || Mast cells, not red cells, drive this response",
   "Platelets release insulin that causes swelling in the airway || Neither platelets nor insulin cause this response",
   "*Mast cells release histamine, leukotrienes and prostaglandins",
   "Osteoblasts release messengers that trigger bronchodilation || Osteoblasts are bone cells and are not involved"],
  "Mast cells respond to allergens or antigens by releasing histamine, leukotrienes and prostaglandins, causing inflammation, edema and mucus that narrow the airway.")

q("ns", "A drug binds to beta-2 receptors in the lungs and activates them, causing bronchodilation. How should the nurse classify this drug?",
  ["An antagonist, because it binds to the receptor in the lungs || An antagonist binds and blocks a response",
   "*An agonist, because it binds and causes a response",
   "A somatic nervous system drug that acts on voluntary muscle || The somatic system controls voluntary functions such as walking",
   "A drug that works without acting on any receptors at all || It binds beta-2 receptors"],
  "An agonist binds a receptor and causes a response; an antagonist binds and blocks a response.")

q("symp", "A client is frightened and the sympathetic (fight or flight) system is activated. Which effects should the nurse expect? " + SATA,
  ["*Bronchodilation",
   "*Decreased airway secretions",
   "*Increased HR (heart rate)",
   "Bronchoconstriction || Bronchoconstriction is a parasympathetic effect",
   "Increased airway secretions || Increased secretions are a parasympathetic effect"],
  "Sympathetic = fight or flight = adrenergic: bronchodilation, decreased secretions and increased HR.")

q("symp", "A drug stimulates the parasympathetic (rest and digest) nervous system. Which term describes this drug?",
  ["Sympathomimetic agent || Sympathomimetics are adrenergic drugs that stimulate the sympathetic system",
   "Anticholinergic agent || Anticholinergics block the parasympathetic response",
   "*Parasympathomimetic",
   "Adrenergic agonist || Adrenergic refers to the sympathetic system"],
  "Parasympathetic = rest and digest = cholinergic; drugs that stimulate it are parasympathomimetics. Adrenergic drugs are sympathomimetics.")

q("predict", "A client receives a drug with cholinergic effects. Which finding should the nurse anticipate?",
  ["Dilated pupils || Cholinergic stimulation constricts the pupils",
   "Urinary retention || Cholinergic stimulation contracts the bladder and relaxes the sphincter",
   "Decreased peristalsis || Cholinergic stimulation increases peristalsis",
   "*A slower heart rate"],
  "Cholinergic effects: pupil and bronchial constriction, increased secretions, decreased HR, increased peristalsis, bladder contracts and sphincter relaxes.")

q("predict", "A client is taking an adrenergic blocker. Which finding is expected?",
  ["Bronchodilation in the small airways || Adrenergic blockers cause bronchial constriction",
   "*Lower BP (blood pressure) via vasodilation",
   "Increased HR (heart rate) and palpitations || Adrenergic blockers decrease HR",
   "Decreased secretions in the airway || Adrenergic blockers increase secretions"],
  "Adrenergic blocker effects: pupil and bronchial constriction, increased secretions, decreased HR, and decreased BP through vasodilation.")

q("beta2", "A client with asthma used albuterol for acute wheezing. Which finding BEST shows the drug was effective?",
  ["HR (heart rate) increased from baseline || Increased HR is an adverse adrenergic effect, not a sign of effectiveness",
   "The client reports feeling shaky || Tremor is an adverse effect",
   "*Breath sounds improved with less wheezing",
   "Secretions increased || Beta-2 agonists decrease secretions"],
  "A SABA (short-acting beta-2 agonist) such as albuterol is evaluated by improved breath sounds and less wheezing. A LABA is evaluated by long-term stability and less rescue use.")

q("beta2", "A client with persistent asthma has been prescribed salmeterol and albuterol. Which client statement indicates a need for MORE teaching?",
  ["'I take salmeterol on a fixed daily schedule.' || Correct; LABAs are scheduled maintenance",
   "'I keep albuterol with me for asthma attacks.' || Correct; albuterol is the rescue drug",
   "'My heart may race a bit after I use albuterol.' || Correct; increased HR is an expected adrenergic effect",
   "*'When I start wheezing, I'll use my salmeterol.'"],
  "A LABA (long-acting beta-2 agonist) such as salmeterol is never used alone for acute attacks; it is fixed daily maintenance. Albuterol (SABA) is the rescue drug.")

q("anticho", "A 68-year-old client with COPD (chronic obstructive pulmonary disease) is prescribed umeclidinium. Which statement about this drug is correct?",
  ["It is a short-acting beta-2 agonist used for rescue || That describes albuterol",
   "It stabilizes mast cells to prevent histamine release || That describes cromolyn",
   "*It is a long-acting anticholinergic bronchodilator",
   "It blocks phosphodiesterase to keep more cAMP available || That describes theophylline"],
  "Ipratropium is the short-acting and umeclidinium the long-acting anticholinergic. They block acetylcholine, which causes bronchoconstriction and mucus, producing bronchodilation and decreased secretions.")

q("anticho", "A client begins inhaled ipratropium. Which effects should the nurse expect or monitor for? " + SATA,
  ["*Bronchodilation",
   "*Decreased secretions",
   "*Urinary retention",
   "Increased mucus production || Blocking acetylcholine decreases mucus",
   "Pupil constriction || Anticholinergics dilate the pupil"],
  "Anticholinergics block the parasympathetic response: bronchodilation and decreased secretions. They relax the bladder and contract the sphincter (retention) and dilate the pupil, which can raise IOP in glaucoma.")

q("theo", "A client taking theophylline says they drink six cups of coffee a day. Which response by the nurse is best?",
  ["'Coffee will help the medicine open your airways even better.' || Caffeine is also a methylxanthine; the client should limit it",
   "*'Try to limit caffeine; it is a methylxanthine like your drug.'",
   "'Switch to eating chocolate instead of drinking coffee.' || Chocolate also contains methylxanthines",
   "'Caffeine has no effect on this medication, so keep drinking it.' || Limiting caffeine is specific teaching for theophylline"],
  "Methylxanthines are naturally found in caffeine and chocolate, so clients on theophylline should limit caffeine.")

q("theo", "Which statements about theophylline are accurate? " + SATA,
  ["*It blocks phosphodiesterase",
   "*It keeps more cAMP (cyclic adenosine monophosphate) available to relax smooth muscle",
   "*It can cause insomnia and nervousness",
   "It blocks acetylcholine to dilate the airway || That is how anticholinergics work",
   "It works by mimicking cortisol || That describes glucocorticoids"],
  "Phosphodiesterase breaks down cAMP, leading to constriction; theophylline blocks it so cAMP stays and the airway dilates. It is a CNS (central nervous system) stimulant, causing insomnia and nervousness.")

q("gluco", "A client on long-term prednisone has a blood glucose level above their usual range. How should the nurse interpret this?",
  ["Proof that the prednisone is no longer controlling inflammation || Glucose level doesn't measure drug effectiveness",
   "*A known glucocorticoid adverse effect to monitor and report",
   "A reason to stop the prednisone today without tapering || Glucocorticoids must be tapered, not stopped abruptly",
   "A finding unrelated to the medication that needs no follow-up || Hyperglycemia is a known glucocorticoid effect"],
  "Long-term glucocorticoids cause hyperglycemia, immunosuppression, muscle wasting, bone loss and fluid retention/weight gain, so blood glucose is monitored.")

q("gluco", "The nurse teaches a client about long-term prednisone. Which client statement indicates a need for MORE teaching?",
  ["'I'll watch for signs of infection, since my immunity is lower.' || Correct; glucocorticoids suppress the immune system",
   "*'I can stop prednisone on my own once I breathe better.'",
   "'I may gain some weight because my body retains fluid.' || Correct; fluid retention and weight gain occur",
   "'My bones can weaken over time while I'm on this drug.' || Correct; bone demineralization occurs"],
  "Glucocorticoids must not be stopped abruptly; they are tapered because they suppress the adrenal gland's own production, and stopping suddenly risks adrenal crisis.")

q("mastmed", "A client asks how cromolyn and montelukast compare. Which statement by the nurse is correct?",
  ["'Both are rescue bronchodilators to use during an asthma attack.' || Neither is a rescue bronchodilator",
   "'Cromolyn suppresses only leukotrienes, not histamine.' || Cromolyn prevents both leukotriene and histamine release",
   "'Montelukast works by stabilizing mast cells in the airway.' || Cromolyn is the mast-cell stabilizer",
   "*'Both reduce inflammation and edema, by different routes.'"],
  "Cromolyn stabilizes mast cells, preventing release of leukotrienes and histamine; montelukast suppresses leukotrienes. Both decrease inflammation and edema.")

q("antihist", "A 35-year-old delivery driver needs an allergy medication to take during the workday. Which choice is best and why?",
  ["Diphenhydramine, because it is non-sedating || Diphenhydramine causes drowsiness",
   "*Cetirizine, because it doesn't cross the blood-brain barrier",
   "Diphenhydramine, because it lacks anticholinergic effects || It has anticholinergic properties",
   "Cetirizine, because it is a stimulant || Cetirizine is not a stimulant"],
  "Second-generation cetirizine is non-sedating because it doesn't cross the BBB (blood-brain barrier). First-generation diphenhydramine crosses it, causing drowsiness, and has anticholinergic effects.")

q("phenyl", "A 64-year-old client with hypertension asks about using nasal phenylephrine for congestion. Which response is best?",
  ["'It's safe for anyone with high blood pressure because it only acts in the nose.' || Vasoconstriction can worsen hypertension",
   "'It works by blocking histamine, so blood pressure isn't affected.' || Phenylephrine is a sympathomimetic, not an antihistamine",
   "*'Ask your provider first; its vasoconstriction can worsen hypertension.'",
   "'It works by thinning mucus, so it won't affect your heart or blood pressure.' || Phenylephrine doesn't thin mucus"],
  "Phenylephrine is a nasal sympathomimetic that stimulates adrenergic receptors, causing vasoconstriction; use caution with hypertension or cardiac disease.")

q("cough", "A client with a productive cough and thick mucus has been taking dextromethorphan. Which response by the nurse is best?",
  ["'Add codeine so the cough is suppressed even more strongly at night.' || Codeine is also an antitussive; a productive cough shouldn't be suppressed",
   "*'A productive cough needs mucus thinned or moved, as with guaifenesin.'",
   "'Keep taking dextromethorphan; it is the right drug for thick mucus.' || Antitussives are for dry cough",
   "'Switch to a leukotriene modifier, which will clear the thick mucus.' || Leukotriene modifiers reduce inflammation; they don't move or thin mucus"],
  "Dry cough is suppressed with an antitussive (codeine, dextromethorphan). Productive cough needs mucus moved or thinned: expectorant (guaifenesin) or mucolytic (acetylcysteine).")

q("cough", "Which pairings of cough medicine and drug class are correct? " + SATA,
  ["*Acetylcysteine: mucolytic",
   "*Dextromethorphan: non-opioid antitussive",
   "*Codeine: opioid antitussive",
   "Guaifenesin: antitussive || Guaifenesin is an expectorant",
   "Acetylcysteine: antitussive || Acetylcysteine is a mucolytic"],
  "Antitussives (dry cough): codeine (opioid) and dextromethorphan (non-opioid). Productive cough: guaifenesin (expectorant) and acetylcysteine (mucolytic).")

q("nursing", "A client says the prescribed inhaler 'doesn't seem to help.' Which action should the nurse take FIRST?",
  ["*Observe the client using the inhaler to check technique",
   "Tell the client to double each dose || Doubling doses is unsafe",
   "Count the doses left in the canister || This doesn't show whether the drug reaches the lungs",
   "Tell the client inhalers don't need a specific technique || Technique determines whether the drug reaches the bronchioles"],
  "The nurse checks inhaler technique to be sure the drug reaches the bronchioles, not just the back of the throat. Teaching covers purpose, timing, rescue vs maintenance, technique, expected effects and safety.")
