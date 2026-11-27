T = "resp"; SET = "20261127"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("anat", "A nurse at a community clinic reviews the charts of four clients. Which client has a disorder of the LOWER respiratory tract?",
  ["A 22-year-old college student with rhinitis || Rhinitis is inflammation of the nasal lining, an upper-tract disorder",
   "A 41-year-old cashier with a cold || Cold and flu are upper-tract disorders",
   "*A 58-year-old retired welder with emphysema",
   "A 16-year-old athlete with hay fever || Hay fever is an upper-tract disorder"],
  "Upper tract: nose, sinuses, pharynx, larynx, trachea; disorders include hay fever, rhinitis and cold/flu. Lower tract: lungs, bronchi, bronchioles, alveoli; disorders include asthma and COPD. Emphysema, a form of COPD, is damage to the alveoli.")

q("copd", "A 72-year-old retired miner with emphysema asks whether his lung damage will go away with inhalers. Which response by the nurse is accurate?",
  ["'Yes, like asthma, the narrowing fully reverses with treatment.' || COPD is progressive and irreversible; asthma is the reversible one",
   "*'COPD is progressive and irreversible; emphysema damages alveoli.'",
   "'Emphysema is airway damage that heals once the cough clears.' || Emphysema is alveolar damage; chronic bronchitis is airway damage, and COPD is irreversible",
   "'Your main problem with COPD is breathing in, not breathing out.' || COPD makes exhalation difficult"],
  "Asthma airway obstruction is reversible; COPD is progressive and irreversible and makes exhalation difficult. Emphysema = alveolar damage; chronic bronchitis = airway damage.")

q("mast", "A 9-year-old with a known cat allergy visits a friend's home and develops airway swelling and mucus. Which sequence best explains these findings?",
  ["Mast cells release acetylcholine and insulin, narrowing the airway || Mast cells release histamine, leukotrienes and prostaglandins",
   "*Mast cells release histamine, leukotrienes and prostaglandins",
   "Platelets release prostaglandins that dilate and dry the airway || Mast cells, not platelets, respond to allergens, and the result is narrowing",
   "Red blood cells release histamine that dries out the airway || Mast cells are the responding cell, and the result is more mucus"],
  "Mast cells respond to allergens (noninfectious) or antigens (infectious) by releasing histamine, leukotrienes and prostaglandins, which cause inflammation, edema and mucus that narrow the airway.")

q("ns", "A nursing student states, 'An antagonist drug binds to a receptor and turns the response on.' How should the instructor correct this statement?",
  ["'Antagonists never bind to receptors; they act some other way.' || An antagonist does bind a receptor; it blocks the response",
   "'That statement describes the somatic nervous system instead.' || Agonist and antagonist describe drug action at receptors, not a division of the nervous system",
   "*'An antagonist binds and blocks; an agonist binds and activates.'",
   "'Agonists and antagonists both turn the same response on.' || Agonists activate and antagonists block"],
  "An agonist binds a receptor and causes a response; an antagonist binds and blocks a response.")

q("symp", "A 27-year-old firefighter enters a burning building and the sympathetic nervous system activates. Which airway change should the nurse expect?",
  ["Bronchoconstriction with increased secretions || These are parasympathetic (cholinergic) effects",
   "*Bronchodilation with decreased secretions",
   "Bronchoconstriction with a slower heart rate || These are parasympathetic effects",
   "No change, because the airway is controlled voluntarily || Airway tone is autonomic (involuntary), and sympathetic stimulation dilates it"],
  "Sympathetic = fight or flight = adrenergic: bronchodilation, decreased secretions and increased HR (heart rate). Parasympathetic = rest and digest = cholinergic: bronchoconstriction, increased secretions, decreased HR.")

q("symp", "Which pairings of nervous system division and descriptive term are correct? " + SATA,
  ["*Sympathetic: adrenergic",
   "*Parasympathetic: rest and digest",
   "*Drugs that stimulate the parasympathetic system: parasympathomimetics",
   "Sympathetic: cholinergic || Sympathetic is adrenergic; cholinergic matches parasympathetic",
   "Adrenergic drugs: parasympathomimetics || Adrenergic drugs are sympathomimetics"],
  "Sympathetic = fight or flight = adrenergic; adrenergic drugs = sympathomimetics. Parasympathetic = rest and digest = cholinergic; drugs that stimulate it are parasympathomimetics.")

q("predict", "A client receiving an anticholinergic drug reports trouble passing urine. Which explanation should the nurse give?",
  ["'The drug makes your bladder contract and the sphincter relax.' || That is the cholinergic effect, which empties the bladder",
   "*'The drug relaxes your bladder and contracts the sphincter.'",
   "'The drug increases secretions that block the urethra.' || Anticholinergics decrease secretions",
   "'The drug speeds up peristalsis, which presses on the bladder.' || Anticholinergics decrease peristalsis"],
  "Anticholinergic effects: pupil and bronchial dilation, decreased secretions, increased HR (heart rate), decreased peristalsis, and the bladder relaxes while the sphincter contracts, causing retention.")

q("predict", "A client is given a drug with adrenergic (sympathomimetic) effects. Which findings should the nurse anticipate? " + SATA,
  ["*Increased heart rate",
   "*Increased blood pressure from vasoconstriction",
   "*Decreased peristalsis",
   "Pupil and bronchial constriction || These are cholinergic or adrenergic-blocker effects",
   "Lower blood pressure from vasodilation || This is an adrenergic-blocker effect"],
  "Adrenergic stimulation: increased HR (heart rate), increased BP (blood pressure) via vasoconstriction, decreased peristalsis. Adrenergic blockers cause pupil and bronchial constriction, increased secretions, decreased HR and decreased BP via vasodilation.")

q("beta2", "A 19-year-old college student with asthma has a new prescription for albuterol and salmeterol. Which instruction is correct?",
  ["'Use salmeterol whenever you feel wheezy and albuterol every day.' || The roles are reversed: salmeterol is maintenance, albuterol is rescue",
   "*'Take salmeterol daily on schedule; use albuterol for wheezing.'",
   "'Either inhaler can be used alone during an asthma attack.' || A LABA is never used alone for an acute attack",
   "'Stop salmeterol once your breathing improves for a day.' || Salmeterol is fixed daily maintenance, judged by long-term stability"],
  "Albuterol is a short-acting beta-2 agonist (SABA) for acute symptoms. Salmeterol is a long-acting beta-2 agonist (LABA) used as fixed daily maintenance and is never used alone for acute attacks.")

q("beta2", "After using albuterol, a 45-year-old teacher with asthma reports feeling nervous and shaky. Which action by the nurse is most appropriate?",
  ["Hold all future doses because this is an allergic reaction || Tremor and nervousness are expected adrenergic effects, not allergy",
   "Tell the client the drug did not reach the lungs properly || These effects reflect sympathetic stimulation, not failure of the drug",
   "*Explain these are expected and monitor the heart rate",
   "Check blood glucose because this suggests a low reading || The source links these effects to sympathetic stimulation, not glucose"],
  "Beta-2 agonists stimulate the sympathetic system, causing increased HR (heart rate), tremors and nervousness. The nurse monitors for tachycardia and palpitations.")

q("anticho", "Which clients have a condition that requires the nurse to use caution before giving an inhaled anticholinergic such as ipratropium? " + SATA,
  ["*A 70-year-old with glaucoma",
   "*A 66-year-old who already has urinary retention",
   "A 50-year-old with frequent diarrhea || Anticholinergics decrease peristalsis; diarrhea is not a caution listed",
   "A 59-year-old with a slow heart rate || Anticholinergics increase HR; a slow rate is not the listed concern",
   "A 48-year-old with excess airway mucus || Anticholinergics decrease secretions, which is a desired effect"],
  "Anticholinergics dilate the pupil and can obstruct drainage, raising IOP (intraocular pressure) in glaucoma. They relax the bladder and contract the sphincter, causing urinary retention.")

q("anticho", "A nurse compares ipratropium and umeclidinium for a 63-year-old client with COPD (chronic obstructive pulmonary disease). Which statement is accurate?",
  ["Ipratropium is the long-acting one; umeclidinium is short-acting || The opposite: ipratropium is short-acting, umeclidinium long-acting",
   "Both stimulate beta-2 receptors to dilate the airway quickly || They are anticholinergics that block acetylcholine",
   "*Both block acetylcholine; ipratropium is the short-acting one",
   "Both increase airway secretions to help loosen thick mucus || Blocking acetylcholine decreases secretions"],
  "Inhaled anticholinergics block acetylcholine, which causes bronchoconstriction and mucus, producing bronchodilation and decreased secretions. Ipratropium = short-acting; umeclidinium = long-acting.")

q("theo", "A 52-year-old office worker starts theophylline. Which client statement shows understanding of the teaching?",
  ["'I'll drink extra coffee to help the medicine work.' || Caffeine is a methylxanthine; caffeine should be limited",
   "'This drug blocks acetylcholine to open my airways.' || Theophylline blocks phosphodiesterase, not acetylcholine",
   "'This drug should make me feel calm and sleepy.' || Theophylline is a CNS stimulant causing insomnia and nervousness",
   "*'I should cut back on caffeine while taking this.'"],
  "Methylxanthines are naturally found in caffeine and chocolate, so clients limit caffeine. Theophylline is a CNS (central nervous system) stimulant causing insomnia and nervousness, and it blocks phosphodiesterase.")

q("theo", "Which sequence correctly describes how theophylline relaxes airway smooth muscle?",
  ["It stimulates phosphodiesterase, which builds up cAMP (cyclic adenosine monophosphate) || Theophylline blocks phosphodiesterase; phosphodiesterase breaks down cAMP",
   "*It blocks phosphodiesterase, so more cAMP (cyclic adenosine monophosphate) remains",
   "It blocks cAMP (cyclic adenosine monophosphate), so phosphodiesterase can act || Theophylline keeps cAMP available by blocking phosphodiesterase",
   "It stabilizes mast cells, so less cAMP (cyclic adenosine monophosphate) is needed || Mast-cell stabilization is how cromolyn works"],
  "Phosphodiesterase breaks down cAMP, leading to constriction. Theophylline blocks phosphodiesterase, so cAMP stays and relaxes smooth muscle, causing dilation.")

q("gluco", "A 60-year-old client has taken prednisone for several months. Which findings should the nurse recognize as adverse effects of long-term use? " + SATA,
  ["*Elevated blood glucose",
   "*Weight gain from fluid retention",
   "*Muscle wasting",
   "Bone strengthening || Long-term glucocorticoids cause bone demineralization",
   "Improved resistance to infection || Glucocorticoids suppress the immune system"],
  "Long-term glucocorticoid effects: hyperglycemia, immunosuppression, muscle wasting, bone demineralization, and fluid retention with weight gain.")

q("gluco", "A 34-year-old chef taking prednisone for several weeks says, 'I feel better, so I'm stopping it tomorrow.' Which is the nurse's priority concern?",
  ["Rebound histamine release causing hay fever || The source names adrenal crisis as the risk of abrupt stopping",
   "*Adrenal crisis from suppressed adrenal production",
   "Sudden hypoglycemia from the drug leaving the body || The source does not list this; long-term use raises glucose",
   "Immediate bronchoconstriction from acetylcholine release || The risk of abrupt stopping is adrenal crisis"],
  "Glucocorticoids suppress the adrenal gland's own production, and the gland needs time to recover, so they must be tapered rather than stopped abruptly to prevent adrenal crisis.")

q("mastmed", "A client with allergic asthma is prescribed montelukast. Which statement by the nurse describes how this drug works?",
  ["'It stabilizes mast cells so they release no histamine.' || That describes cromolyn",
   "'It blocks phosphodiesterase to keep cAMP (cyclic adenosine monophosphate) available.' || That describes theophylline",
   "*'It suppresses leukotrienes to reduce inflammation and edema.'",
   "'It stimulates beta-2 receptors to open the airway quickly.' || That describes beta-2 agonists such as albuterol"],
  "Montelukast is a leukotriene modifier that suppresses leukotrienes, decreasing inflammation and edema. Cromolyn stabilizes mast cells, preventing release of leukotrienes and histamine.")

q("antihist", "An 80-year-old client in assisted living takes diphenhydramine at bedtime for allergies. Which findings should the nurse monitor for? " + SATA,
  ["*Drowsiness",
   "*Constipation",
   "*Urinary retention",
   "Increased saliva production || Anticholinergic properties cause dry mouth",
   "Insomnia and jitteriness || Diphenhydramine crosses the blood-brain barrier and causes drowsiness"],
  "First-generation diphenhydramine crosses the blood-brain barrier (drowsiness) and has anticholinergic properties: dry mouth, urinary retention and constipation. Second-generation cetirizine is non-sedating.")

q("phenyl", "A 47-year-old client with a cold uses nasal phenylephrine. Which history would the nurse report to the provider as a caution?",
  ["A dry, nonproductive cough || A dry cough is not a listed caution for phenylephrine",
   "Seasonal allergic itchy eyes || This is not a listed caution for phenylephrine",
   "*Known cardiac disease",
   "Recent sneezing and runny nose || These are cold symptoms, not a caution"],
  "Phenylephrine is a nasal sympathomimetic that stimulates adrenergic receptors, causing vasoconstriction in the nasal passages. Vasoconstriction can worsen cardiac disease or HTN (hypertension).")

q("cough", "A 38-year-old radio host has a dry, nonproductive cough. Which medications match this cough type? " + SATA,
  ["*Codeine",
   "*Dextromethorphan",
   "Guaifenesin || An expectorant moves mucus in a productive cough",
   "Acetylcysteine || A mucolytic thins mucus in a productive cough"],
  "Dry cough is suppressed with an antitussive: codeine (opioid) or dextromethorphan (non-opioid). Productive cough needs mucus moved or thinned: guaifenesin (expectorant) or acetylcysteine (mucolytic).")

q("cough", "A client with a wet cough producing thick mucus asks for something to help. Which statement by the nurse needs correction?",
  ["'Acetylcysteine is a mucolytic that thins mucus.' || Accurate: acetylcysteine is a mucolytic for productive cough",
   "'Guaifenesin is an expectorant that helps move mucus.' || Accurate: guaifenesin is an expectorant",
   "*'Dextromethorphan is best for thick mucus.'",
   "'Codeine is an opioid that suppresses coughing.' || Accurate: codeine is an opioid antitussive"],
  "Productive cough needs mucus moved or thinned: expectorant (guaifenesin) or mucolytic (acetylcysteine). Antitussives (codeine, dextromethorphan) suppress a dry cough.")

q("nursing", "A nurse is teaching a client who has a rescue and a maintenance inhaler. Which topics should the teaching include? " + SATA,
  ["*Proper inhaler technique",
   "*Which inhaler is for rescue and which is maintenance",
   "*Expected effects of each drug",
   "Doubling doses when relief is slow || Doubling doses is not taught; check technique instead",
   "Stopping a glucocorticoid once breathing is easier || Glucocorticoids must not be stopped abruptly"],
  "Teach purpose, timing, rescue vs maintenance, technique, expected effects and safety. Safety rules: don't use a LABA (long-acting beta-2 agonist) alone for acute rescue, and don't stop glucocorticoids abruptly.")
