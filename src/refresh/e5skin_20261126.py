T = "e5skin"; SET = "20261126"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("patho", "A 46-year-old accountant newly diagnosed with skin cancer asks the nurse where skin cancer starts. Which response by the nurse is accurate?",
  ["'It starts in the blood and lymph vessels of the dermis.' || It starts in the epidermis and can reach dermal vessels later",
   "*'It starts as abnormal growth of cells in the epidermis.'",
   "'It starts only in melanocytes, the cells that make melanin.' || Squamous and basal cells can also become cancer",
   "'It starts in bone-forming cells that lie under the skin.' || Osteoblasts are not epidermal cells"],
  "Skin cancer is abnormal growth of epidermal cells: squamous cells, basal cells and melanocytes. Once it invades the dermis it can reach blood and lymph vessels and metastasize.")

q("uv", "The nurse teaches a 31-year-old delivery driver about ultraviolet light. Which statement by the client shows understanding?",
  ["'UVA (ultraviolet A) is the shorter wave that gives me sunburns.' || UVB (ultraviolet B) is shorter and causes sunburn",
   "'UVB is around all year, but UVA only shows up in the summer.' || UVA is the one present all year",
   "'Tanning beds use UVB, so the deeper UVA rays aren't an issue.' || Tanning beds mainly use UVA",
   "*'Both UVA and UVB rays contribute to skin cancer.'"],
  "UVB is shorter and causes sunburn; UVA penetrates deeper and is present all year. Both contribute to skin cancer, and tanning beds mainly use UVA.")

q("risk", "The nurse takes a health history from a 33-year-old warehouse worker. Which findings are risk factors for skin cancer? " + SATA,
  ["*Handles industrial chemicals at work",
   "*Smokes cigarettes daily",
   "Has dark skin with lots of melanin || Dark skin with lots of melanin is not a listed risk factor",
   "*Has HIV (human immunodeficiency virus)",
   "*Mother was treated for skin cancer"],
  "Major risk factors include cumulative UV (ultraviolet) exposure, tanning beds, immunosuppression such as HIV or transplant medications, personal or family history of skin cancer, chemical exposure and smoking.")

q("precan", "A 76-year-old retired mail carrier has rough, scaly, red-brown patches on his scalp. After teaching, which statement by the client shows understanding?",
  ["'These are the most dangerous kind of skin cancer there is.' || Melanoma is the most dangerous",
   "'These patches will turn into basal cell carcinoma over time.' || Actinic keratosis can progress to squamous cell carcinoma",
   "*'These are precancerous and could turn into squamous cell cancer.'",
   "'These only show up on skin that never gets any sun exposure.' || Actinic keratosis appears on sun-exposed skin"],
  "Actinic (solar) keratosis is rough, scaly, red-brown patches on sun-exposed skin such as the ears and scalp. It is precancerous and can progress to squamous cell carcinoma.")
q("precan", "The nurse teaches a 25-year-old client with dysplastic nevi syndrome. Which statement by the client indicates a need for more teaching?",
  ["'This condition often runs in families.' || Accurate; dysplastic nevi syndrome is often familial",
   "'I should look for a mole that looks unlike my others.' || Accurate; this is the ugly duckling sign",
   "'It means I have many atypical moles.' || Accurate description of the syndrome",
   "*'I have so many moles that one more won't matter.'"],
  "Dysplastic nevi syndrome is many atypical moles, often familial; more moles raise concern. Teach the ugly duckling sign: a mole that looks different from the person's other moles.")

q("bcc", "A 67-year-old retired fisherman shows the nurse a lesion on his temple. Which feature points most to basal cell carcinoma?",
  ["*A pearly, raised edge with a dip in the center",
   "A red, thick, scaly surface that hurts and bleeds || This describes squamous cell carcinoma",
   "A rough, red-brown scaly patch on the scalp || This describes actinic keratosis",
   "Several colors with a notched, uneven border || These are ABCDE melanoma warning signs"],
  "Basal cell carcinoma is a smooth, raised, shiny/waxy pink lesion with visible small vessels. It may have a central depression and is often a 'sore that doesn't heal.'")
q("bcc", "Which statements correctly compare basal cell carcinoma (BCC) with other skin cancers? " + SATA,
  ["BCC is more likely to spread than squamous cell carcinoma || SCC (squamous cell carcinoma) is more likely to metastasize",
   "*BCC is more common than squamous cell carcinoma",
   "*BCC is less aggressive than squamous cell carcinoma",
   "BCC is the type that arises from untreated actinic keratosis || SCC can arise from untreated actinic keratosis",
   "*BCC metastasizes less often than malignant melanoma"],
  "BCC is the most common and least aggressive skin cancer, and metastasis is rare. SCC is more aggressive, can arise from actinic keratosis, and melanoma is the most metastatic.")

q("scc", "A 70-year-old client has two biopsy-confirmed lesions: a basal cell carcinoma on the cheek and a squamous cell carcinoma on the lip. Which statement by the nurse is accurate?",
  ["'The cheek lesion is the one more likely to spread.' || Basal cell carcinoma rarely metastasizes",
   "'Both lesions carry the very same risk of spreading.' || SCC (squamous cell carcinoma) is more likely to metastasize",
   "'The lip lesion never invades the deeper tissues.' || SCC is more aggressive and can invade and spread",
   "*'The lip lesion is the more aggressive of the two.'"],
  "SCC is more aggressive and more likely to metastasize than BCC (basal cell carcinoma). SCC is common on the lips, ears and nose.")
q("scc", "Which statements about squamous cell carcinoma are accurate? " + SATA,
  ["*It can develop from an untreated actinic keratosis",
   "It is the most common type of skin cancer || Basal cell carcinoma is the most common",
   "*It may ulcerate and bleed",
   "*It can be painful",
   "It is less aggressive than basal cell carcinoma || SCC is more aggressive than BCC (basal cell carcinoma)"],
  "Squamous cell carcinoma is a red, thick, scaly lesion that may ulcerate, hurt and bleed. It is more aggressive than BCC and can arise from untreated actinic keratosis.")

q("mel", "The nurse is reviewing facts about malignant melanoma before a skin screening event. Which statement is accurate?",
  ["It rarely spreads to the lymph nodes || Melanoma is highly metastatic",
   "*It can occur in the eyes",
   "It is the most common type of skin cancer || Basal cell carcinoma is the most common",
   "It occurs only on sun-exposed skin || Melanoma can occur anywhere, including mucosal surfaces"],
  "Malignant melanoma is the most dangerous and highly metastatic skin cancer. It can occur anywhere, including the eyes and mucosal surfaces, so assess the entire skin surface.")
q("mel", "A 52-year-old office manager with melanoma on the back is scheduled for a sentinel lymph node biopsy. Which statement by the client shows understanding?",
  ["'They will freeze my lymph nodes with liquid nitrogen.' || Freezing with liquid nitrogen is cryosurgery",
   "'This test takes the melanoma off one thin layer at a time.' || Layer-by-layer removal is Mohs surgery",
   "*'A tracer or dye shows the first node the tumor drains to.'",
   "'This test is done because melanoma almost never spreads.' || Melanoma is the most likely skin cancer to spread"],
  "Sentinel lymph node biopsy uses a tracer or dye near the tumor to find the first draining node and check whether melanoma has spread. Early detection and treatment are critical.")

q("abcde", "A 37-year-old client says, 'If I folded a picture of my mole in half, the two sides wouldn't line up.' Which ABCDE letter does this describe?",
  ["*A — Asymmetry",
   "B — Border irregularity || Border refers to ragged, notched or blurry edges",
   "C — Color variation || Color refers to several shades in one mole",
   "E — Evolving || Evolving means changing size, shape, color or appearance"],
  "ABCDE: Asymmetry (one half doesn't match the other), Border irregularity, Color variation, Diameter over 6 mm, Evolving.")
q("abcde", "The nurse documents several clients' moles at a community clinic. Which moles show at least one ABCDE warning sign? " + SATA,
  ["*A mole that measures 8 mm across",
   "A round, 4 mm mole that is one even brown color || It has no ABCDE warning signs",
   "*A mole that has grown larger over two months",
   "*A mole with black and red areas",
   "A 3 mm mole with smooth edges and matching halves || It has no ABCDE warning signs"],
  "ABCDE: Asymmetry, Border irregularity, Color variation, Diameter over 6 mm (about a pencil eraser), Evolving (changing size, shape, color or appearance).")

q("biopsy", "A 39-year-old client is scheduled for a shave biopsy of a skin lesion. Which description should the nurse give?",
  ["'The whole lesion is removed along with a margin of healthy skin.' || This is an excisional biopsy",
   "'A cylinder-shaped sample is taken down to a set depth.' || This is a punch biopsy",
   "*'Only the superficial tissue of the lesion is removed.'",
   "'Just one part of a large lesion is cut out for testing.' || This is an incisional biopsy"],
  "Shave biopsy removes superficial tissue. Punch is a cylindrical sample to a set depth, incisional removes part of a larger lesion, and excisional removes the whole lesion plus a margin.")

q("local", "A 60-year-old client with actinic keratosis on the forearm is starting topical fluorouracil. Which statement by the client shows understanding?",
  ["'If it turns red, that means the cancer is spreading.' || Irritation is expected and does not mean spread",
   "'I'll use it twice as often if the area looks irritated.' || Using it more often is not the correct response",
   "*'The area may look irritated or crusted before it heals.'",
   "'Irritation means I'm allergic, so I'll stop using it.' || Irritation and crusting are expected effects"],
  "Topical fluorouracil or retinoids treat actinic keratosis or superficial basal lesions. The area is expected to look irritated or crusted before it heals.")

q("surg", "A 64-year-old client is scheduled for Mohs micrographic surgery. Which statement by the client shows understanding?",
  ["'The lesion and tissue around it come out in one piece.' || This describes wide excision",
   "*'Thin layers come off until the microscope shows no cancer.'",
   "'A light-activated drug will be used to destroy the lesion.' || This describes photodynamic therapy",
   "'Only part of the lesion is removed so it can be diagnosed.' || This describes an incisional biopsy"],
  "Mohs surgery removes one thin layer at a time and checks it under a microscope, repeating until no cancer cells remain.")
q("surg", "A 58-year-old client had a wide excision of a large lesion on the back. Which statements by the nurse are accurate? " + SATA,
  ["*'The lesion was removed along with surrounding tissue.'",
   "'The wound will always close by itself without help.' || A flap or skin graft may be needed",
   "*'A flap may be needed to close the wound.'",
   "'Thin layers were checked one at a time under a microscope.' || This describes Mohs surgery",
   "*'A skin graft may be needed to close the wound.'"],
  "Wide excision removes the lesion plus surrounding tissue, and a flap or skin graft may be needed to close the wound.")

q("graft", "The nurse teaches a 49-year-old client about an upcoming split-thickness skin graft. Which statement by the client needs correction?",
  ["'The graft can be meshed to cover a larger area.' || Accurate; split-thickness grafts can be meshed",
   "*'My donor site will lose its hair follicles and sweat glands.'",
   "'A dermatome will be used to take the thin donor skin.' || Accurate; a dermatome harvests the donor skin",
   "'The skin may come from my thigh or my buttock.' || Accurate; these are common donor areas"],
  "A split-thickness graft is epidermis plus superficial dermis and can be meshed. The donor site keeps its follicles and sweat glands; thigh and buttock are common donor areas.")

q("donor", "On day 6 after a split-thickness graft, a client's buttock donor site has moved from weeping to dry, and the edges of the nonadherent dressing are lifting. Which action by the nurse is best?",
  ["Peel the dressing off now to inspect the healing site || The dressing stays until it lifts off on its own",
   "Apply a bulky pressure dressing over the donor site || A bulky pressure dressing is used on the graft site",
   "Report that the lifting dressing means the graft failed || Lifting is expected as the donor site heals",
   "*Leave the dressing in place to lift off as the site heals"],
  "Donor site: wet, weeping drainage for about 3-5 days, then a dry phase. The nonadherent dressing stays in place until it lifts off as the site heals.")
q("donor", "A client asks why the nurse keeps the newly grafted leg elevated and still under its bulky dressing. Which response is best?",
  ["'It helps the donor site on your thigh stop weeping.' || Immobilizing the graft does not treat the donor site",
   "*'It helps the graft stay in contact with the wound bed.'",
   "'It keeps the dressing from lifting off before it heals.' || A dressing that lifts off as it heals is the donor site",
   "'It is only needed for the first 12 hours after surgery.' || The bulky graft dressing stays about 3-5 days"],
  "Graft site care: bulky pressure dressing for about 3-5 days, immobilize and elevate, and watch for trapped blood or fluid that keeps the graft from adhering. Preserve graft-wound contact.")

q("systemic", "Which statements about systemic treatment for advanced skin cancer are accurate? " + SATA,
  ["*Immunotherapy helps the body build immune memory",
   "Immunotherapy works by freezing the tumor || Freezing with liquid nitrogen is cryosurgery",
   "*Targeted therapy can block tumor blood-vessel formation",
   "Targeted therapy is used for every actinic keratosis || It is used for advanced or metastatic disease",
   "*Standard chemotherapy is for cancers not helped by other therapies"],
  "Immunotherapy helps the body recognize and attack malignant cells and build immune memory. Targeted therapy blocks growth signals and/or tumor blood-vessel formation. Standard chemotherapy is for cancers that don't respond to other therapies.")

q("promo", "A 45-year-old roofer asks how often to reapply sunscreen on a hot workday. Which response by the nurse is best?",
  ["'Once in the morning is enough for the whole day.' || Reapply every 2 hours",
   "'Reapply only when you start to see a sunburn.' || Reapply on a schedule, not after burning",
   "'Every 6 hours is fine if the bottle says SPF (sun protection factor) 30.' || Reapply every 2 hours",
   "*'Every 2 hours, and more often since you'll be sweating.'"],
  "Apply SPF 15-30 sunscreen about 30 minutes before going out, reapply every 2 hours and more often when swimming or sweating, and check the expiration date.")
q("promo", "The nurse teaches skin self-examination to a 32-year-old barista. Which statements by the client show understanding? " + SATA,
  ["*'I'll do the exam in a well-lit room.'",
   "'I'll check only my face and arms each time.' || The whole skin surface is checked",
   "*'I'll use a full-length mirror and a handheld mirror.'",
   "'Since I check myself, I can skip the yearly professional exam.' || 'Check your birthday suit on your birthday' means an annual professional exam",
   "*'I'll learn what my usual moles look like.'"],
  "Do the self-exam after a bath or shower in a well-lit room using full-length and handheld mirrors. Know your usual moles, use ABCDE, and get an annual professional skin check.")
