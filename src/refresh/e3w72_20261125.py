T = "e3w72"; SET = "20261125"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("def", "An instructor uses the shorthand NOTICE → CONNECT → PRIORITIZE → PLAN → DO → CHECK. Which NCSBN step does CONNECT match?",
  ["Recognize cues || that matches NOTICE",
   "*Analyze cues",
   "Generate solutions || that matches PLAN",
   "Evaluate outcomes || that matches CHECK"],
  "Recognize → Analyze → Prioritize → Generate → Act → Evaluate = NOTICE → CONNECT → PRIORITIZE → PLAN → DO → CHECK.")

q("recog", "A nurse starts the shift with a 67-year-old post-op client. Which nurse statement reflects the Recognize cues step?",
  ["'That could mean fluid overload or a clot.' || linking cues to conditions = analyze",
   "'Her breathing is the most urgent problem.' || ranking problems = prioritize",
   "*'Her RR is 28 and she says she can't catch her breath.'",
   "'I'm raising the head of the bed now.' || implementing = take action"],
  "Recognize cues = collect and filter relevant data (VS, labs, history, client perspective) without connecting it to hypotheses yet.")

q("recog", "A nurse is in the Recognize cues step. Which activities would move the nurse PAST this step? " + SATA,
  ["*Linking the findings to a possible condition",
   "Noting a new lab value in the chart || collecting data is recognize",
   "*Ranking the client's problems by urgency",
   "Listening to the client's own description || client perspective is a recognize source",
   "*Choosing an intervention to carry out"],
  "Recognize = notice and filter relevant vs irrelevant data. Connecting cues (analyze), ranking (prioritize) and choosing interventions come later.")

q("analyze", "A 48-year-old client is 2 days post-op with temp 100.9°F, HR 108 and a reddened incision. The nurse thinks, 'Together these could point to a wound infection.' Which step is this?",
  ["Recognize cues || recognizing notices data without interpreting",
   "Take action || nothing has been done yet",
   "*Analyze cues",
   "Evaluate outcomes || no intervention is being checked"],
  "Analyze cues = link cues to the clinical presentation, find patterns and consider which conditions fit.")

q("analyze", "Which activities belong to the Analyze cues step? " + SATA,
  ["*Finding patterns and relationships among cues",
   "Ranking problems by urgency and risk || that's prioritize hypotheses",
   "*Comparing expected and unexpected findings",
   "*Deciding whether more information is needed",
   "Comparing the response with the outcome goal || that's evaluate outcomes"],
  "Analyze: organize and link cues, compare expected vs unexpected, consider what conditions fit and ask whether additional information is needed.")

q("prior", "A nurse identifies three possible problems for a client: internal bleeding, mild nausea and worry about the hospital bill. The nurse asks, 'Which is most likely and most serious?' Which step is this?",
  ["Analyze cues || analyze considers possible meanings",
   "Generate solutions || no outcomes or options are listed",
   "Recognize cues || the cues have already been collected",
   "*Prioritize hypotheses"],
  "Prioritize hypotheses = rank possible problems by urgency, likelihood and risk; ask which is most likely and most serious.")

q("prior", "An NGN item asks, 'Which finding requires immediate follow-up?' This wording points mainly to which step?",
  ["Evaluate outcomes || words like improved or effective point to evaluate",
   "*Prioritize hypotheses",
   "Take action || verbs like administer or teach point to action",
   "Recognize cues || words like notice or observe point to recognize"],
  "Clue words such as priority, first, most important and immediate point to prioritization.")

q("gen", "Which nurse statements are examples of Generate solutions? " + SATA,
  ["*'Goal: temp below 100.4°F within 4 hours.'",
   "'I gave the acetaminophen at 1400.' || carrying it out = take action",
   "*'With her bleeding risk, I should avoid some options.'",
   "*'Another assessment in 1 hour is one possible option.'",
   "'Her temp is now 99.1°F, so the goal is met.' || comparing to the goal = evaluate"],
  "Generate solutions = goals + options: expected outcomes, interventions, resources and what to avoid. Additional assessment can itself be a solution.")

q("gen", "A nursing student describes Generate solutions. Which statement needs correction?",
  ["'I identify the expected outcomes.' || accurate part of generate",
   "'I decide what should be avoided.' || accurate part of generate",
   "'I identify the resources I'll need.' || accurate part of generate",
   "*'Only medications count as solutions, not assessment.'"],
  "Additional assessment or data collection can itself be a possible solution in Generate solutions.")

q("act", "A 74-year-old client declines the planned walk in the hall after surgery. Following the Take action prompts, what should the nurse do?",
  ["Insist the client walk now as planned || preferences must be considered",
   "*Explore the client's preferences and adapt the plan",
   "Skip documenting the refusal || documenting is an action step",
   "Stop all care for the rest of the shift || care continues"],
  "Take action prompts: what's needed, contraindications and what to do if the client refuses; incorporate client preferences and needs.")

q("act", "While carrying out an intervention, which considerations are part of the Take action step? " + SATA,
  ["*Contraindications to the intervention",
   "Following a memorized routine no matter what || use the specific scenario",
   "*The client's preferences and needs",
   "*Monitoring the client's response",
   "Ranking which hypothesis is most serious || that's prioritize"],
  "Take action: use the specific scenario rather than a memorized routine, consider contraindications, include preferences and monitor the response.")

q("eval", "The goal was SpO2 ≥ 92% within 1 hour. After oxygen is started, the SpO2 drops from 90% to 88%. How should the nurse evaluate this?",
  ["Improving; the goal is met || SpO2 fell below 92%",
   "Unchanged; keep the plan as is || the value went down",
   "*Declining; reassess and revise the plan",
   "Met; stop monitoring the client || the goal isn't met"],
  "Evaluate = compare observed response to expected outcome: improving, declining or unchanged. If not met, reassess and revise the plan.")

q("eval", "A client rated pain 7/10 before repositioning and still rates it 7/10 an hour later. What should the nurse do next?",
  ["Document that the goal was met || pain didn't change",
   "Repeat the same step without reassessing || the plan needs review",
   "End the pain plan of care || the cycle continues",
   "*Reassess and modify the plan of care"],
  "If the outcome isn't met, the clinical judgement cycle continues: reassess, modify outcomes or actions and update the plan of care.")

q("abc", "Using ABCs, which client should the nurse see FIRST?",
  ["Client with SpO2 90% and crackles || breathing comes after airway",
   "Client with BP 84/50 after surgery || circulation comes after airway",
   "*Client who is choking and can't speak",
   "Client with a blood glucose of 65 || not an ABC threat"],
  "When life is at stake: airway first, then breathing, then circulation.")

q("maslow", "Using Maslow's hierarchy, which client need would the nurse address LAST?",
  ["Client who needs help getting oxygen || physiological, the first level",
   "Client at risk of falling at night || safety and security, level 2",
   "Client who feels lonely and wants visitors || love and belonging, level 3",
   "*Client who wants to reach a personal life goal"],
  "Order: physiological → safety & security → love & belonging → self-esteem → self-actualization (top).")

q("safety", "Which nurse statement reflects the safety and risk-reduction framework?",
  ["'Every risk on my unit deserves equal attention.' || compare risks, don't treat them equally",
   "*'Which of these findings is the greatest threat right now?'",
   "'I'll start with the chronic problem first.' || the greatest current threat comes first",
   "'I'll choose whichever option costs the least.' || cost doesn't set priority"],
  "Safety and risk reduction: ask which finding poses the greatest threat now; compare risks; combine with ABCs if several are dangerous.")

q("np", "In the RN nursing process, which step comes right after Assessment?",
  ["*Analysis",
   "Planning || analysis comes before planning",
   "Implementation || it follows planning",
   "Evaluation || it follows implementation"],
  "RN: Assessment → Analysis → Planning → Implementation → Evaluation. PN uses 4 steps.")

q("least", "A confused client keeps pulling at an IV line. Which nurse action goes against the least restrictive principle?",
  ["Providing frequent reorientation || a least restrictive option",
   "Placing a sitter at the bedside || a least restrictive option",
   "*Applying wrist restraints before trying other measures",
   "Checking on the client frequently || a least restrictive option"],
  "Choose the least restrictive or invasive intervention that still meets the need before restraints or medication.")

q("acute", "A nurse receives a morning report on four clients. Which client should the nurse see FIRST?",
  ["*Client whose HR rose from 80 to 130 this hour",
   "Client with chronic diabetic neuropathy || chronic and expected",
   "Client with a stable chronic wound || stable and chronic",
   "Client with long-standing knee pain || chronic and expected"],
  "Acute > chronic, unstable > stable, urgent > nonurgent. A new or worsening finding needs priority attention.")

q("triage", "After a bus crash, which victim does the nurse treat FIRST using mass-casualty triage?",
  ["Victim with injuries unlikely to be survived || Class IV gets comfort measures",
   "Victim with a closed fracture and stable vitals || Class II can be delayed",
   "*Victim with a life-threatening injury survivable once stabilized",
   "Victim walking with minor scrapes || Class III is minimal"],
  "Class I (Emergent/Immediate): life-threatening but survivable with stabilization; highest priority. Triage focuses on survival potential and limited resources.")
