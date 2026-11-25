T = "e3w92"; SET = "20261125"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("course", "The mother of a 22-year-old client with schizophrenia asks, 'Will he definitely relapse someday?' Which response is best?",
  ["'Yes, relapse is certain no matter what we do.' || relapse is not inevitable",
   "'No, once he's stable, relapse can't happen.' || families should plan for relapse",
   "*'Relapse isn't certain; taking medication consistently helps prevent it.'",
   "'Relapse only happens if he gets too much support.' || family support helps"],
  "Failure to take medication consistently is the major reason for relapse. Relapse is detrimental but not inevitable; families plan for it.")

q("posneg", "A nurse assesses a client with schizophrenia. Which findings are POSITIVE symptoms? " + SATA,
  ["*Hearing voices no one else hears",
   "Speaking very little || alogia is a negative symptom",
   "*A fixed belief that neighbors are spying",
   "Loss of pleasure in activities || anhedonia is a negative symptom",
   "*Disorganized, bizarre behavior"],
  "Positive = presence of something added or distorted (hallucinations, delusions, disorganized thought/behavior). Negative = loss: flat affect, alogia, avolition, anhedonia.")

q("terms", "A nurse reviews disorganized speech and behavior terms. Which pairing is correct?",
  ["Echolalia — copying another's movements || that's echopraxia",
   "*Clang association — words linked by sound or rhyme",
   "Circumstantiality — never returns to the point || that's tangentiality",
   "Neologism — a jumble of unrelated words || that's word salad"],
  "Clang association: words linked by sound or rhyme. Neologism = invented word; word salad = jumbled words; circumstantiality eventually reaches the point.")

q("ae", "A client on long-term antipsychotic therapy has repeated lip smacking and tongue movements. Which adverse effect does the nurse suspect?",
  ["Acute dystonia || painful spasms such as torticollis soon after a dose",
   "Akathisia || intense restlessness and inability to sit still",
   "*Tardive dyskinesia",
   "Pseudoparkinsonism || shuffling gait, tremor and mask-like face"],
  "Tardive dyskinesia is a late effect: involuntary lip smacking, tongue and limb/trunk movements that may persist after stopping the drug.")

q("ae", "A nurse reviews reports from four clients taking antipsychotics. Which report is the priority?",
  ["'My mouth feels dry most of the day.' || anticholinergic; manage with sugarless gum",
   "'I've been a little constipated.' || anticholinergic; manage with fiber and fluids",
   "'I get sunburned more easily now.' || photosensitivity; teach sunscreen",
   "*'I have a sore throat and a fever.'"],
  "Agranulocytosis (dangerously low neutrophils) causes infection risk; the professor called it one of the most important effects. Check the ordered CBC.")

q("nms", "Which finding best helps the nurse tell NMS apart from acute dystonia in a client on an antipsychotic?",
  ["Head twisted to one side with eyes fixed upward || that's acute dystonia",
   "*High fever with rigidity and unstable BP and HR",
   "Restlessness and constant pacing || that's akathisia",
   "Lip smacking and tongue movements || that's tardive dyskinesia"],
  "NMS: sudden high fever, severe rigidity, autonomic instability (BP changes, tachycardia, sweating) and decreased LOC; life-threatening.")

q("comm", "A client who is hallucinating asks the nurse, 'Do you hear the voices too?' Which response is best?",
  ["'Yes, I hear them, but try to ignore them.' || never agree with the hallucination",
   "'What exactly are the voices saying to you?' || this feeds the hallucination",
   "*'I don't hear them, but they seem real and scary to you.'",
   "'There's nothing there, so stop talking about it.' || arguing is avoided"],
  "Acknowledge that it seems real and frightening, present reality gently, and don't argue, agree or feed into the hallucination.")

q("comm", "A client with schizophrenia says, 'I own this hospital, and you all work for me.' Which response is best?",
  ["'You don't own anything here, and you know it.' || arguing about a delusion is avoided",
   "'Which other buildings in town do you own?' || this reinforces the delusion",
   "'Okay, boss, whatever you say today.' || ridiculing and agreeing are avoided",
   "*'Being in charge seems to matter to you. Let's talk about your plans for today.'"],
  "Don't argue, ridicule or agree with a delusion; go to the feeling tone and focus on reality-based topics.")

q("bptypes", "A nursing student compares bipolar disorders. Which statement is accurate?",
  ["*'Judgment is more intact in hypomania than in mania.'",
   "'Bipolar II requires at least one full manic episode.' || that defines bipolar I",
   "'Cyclothymic disorder lasts at least 2 weeks.' || it lasts at least 2 years",
   "'Psychosis is a typical part of hypomania.' || psychosis may occur in severe mania"],
  "Bipolar I: at least one full manic episode. Bipolar II: hypomania + major depression. Hypomania is less severe with more intact judgment.")

q("mania", "A nurse admits a client with bipolar disorder. Which finding points to the MANIC phase?",
  ["Loss of pleasure in usual activities || anhedonia is depressive",
   "*Irritable mood and easy distractibility",
   "Psychomotor slowing and fatigue || these are depressive",
   "Frequent tearfulness through the day || tearfulness is depressive"],
  "Mania: elevated/irritable mood, grandiosity, pressured speech, flight of ideas, distractibility, less sleep, impulsivity and poor judgment.")

q("manicare", "A client in acute mania has not showered in 3 days. Which approach is best?",
  ["A long explanation of why hygiene matters || keep directions brief",
   "*Brief reminders and step-by-step hygiene help",
   "Letting the client skip hygiene until calm || hygiene needs help, not skipping",
   "Debating the client until they agree || avoid power struggles"],
  "In acute mania, give brief, concise directions, remind about hygiene and help with simple steps; avoid power struggles.")

q("manicare", "A nurse reviews the care plan for a client in acute mania. Which item should the nurse question?",
  ["*Leading a competitive volleyball game",
   "Walking with staff for physical activity || a good noncompetitive outlet",
   "Using a quiet, low-stimulation room || decreases stimulation",
   "Setting consistent limits as a team || limit setting is appropriate"],
  "Provide outlets for physical activity that don't overstimulate and avoid competition; lower stimulation and keep limits consistent.")

q("schizoaff", "A nurse reviews psychotic disorders. Which pairings are accurate? " + SATA,
  ["*Schizoaffective — psychosis plus mood episodes",
   "Brief psychotic — lasts at least 6 months || it lasts 1 day to under 1 month",
   "*Schizophreniform — schizophrenia-like, under 6 months",
   "*Delusional disorder — persistent delusions",
   "Bipolar — mainly a thought disorder || bipolar is a mood disorder"],
  "Schizoaffective = psychosis + mood episodes. Brief psychotic: 1 day to <1 month. Schizophreniform: <6 months. Delusional disorder: persistent delusions.")

q("pd", "Which personality disorders belong to Cluster B (dramatic/erratic)? " + SATA,
  ["*Borderline",
   "Avoidant || Cluster C (anxious/fearful)",
   "*Antisocial",
   "Schizoid || Cluster A (odd/eccentric)",
   "*Narcissistic"],
  "Cluster B: borderline, antisocial, histrionic, narcissistic. Cluster A: paranoid, schizoid, schizotypal. Cluster C: avoidant, dependent, obsessive-compulsive.")

q("pdtx", "A client with borderline personality disorder asks, 'Is there a pill that will cure this?' Which response is best?",
  ["'Yes, lithium cures personality disorders.' || no medication treats the disorder itself",
   "'Yes, an antipsychotic will make it go away.' || meds only target symptoms",
   "*'No pill treats the disorder, but some can help certain symptoms.'",
   "'No, and you don't need any treatment at all.' || therapies such as DBT are used"],
  "No single medication treats a personality disorder; medications target specific symptoms. DBT is emphasized for borderline personality disorder.")
