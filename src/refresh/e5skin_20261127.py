T = "e5skin"; SET = "20261127"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("patho", "During teaching about the layers of the skin, a 52-year-old hair stylist asks what melanocytes do. Which response by the nurse is accurate?",
  ["*'They are epidermal cells that make melanin.'",
   "'They form the blood and lymph vessels of the dermis.' || Blood and lymph vessels are in the dermis; melanocytes are epidermal cells",
   "'They are bone-forming cells that lie under the skin.' || Bone-forming cells (osteoblasts) are not skin cells",
   "'They are the outer layer of cells that is called squamous.' || Squamous cells form the outer layer; melanocytes make melanin"],
  "The epidermis contains squamous cells (outer layer), basal cells (lower epidermis) and melanocytes, which make melanin. Skin cancer is abnormal growth of these epidermal cells.")

q("uv", "The nurse is making a poster that compares the two types of ultraviolet light. Which pairing should the nurse include?",
  ["UVA (ultraviolet A): the shorter wave that causes sunburn || UVB (ultraviolet B) is the shorter wave that causes sunburn",
   "*UVA: penetrates deeper and is present all year",
   "UVB: the main type of ray used in tanning beds || Tanning beds mainly use UVA",
   "UVB: the only type that contributes to skin cancer || Both UVA and UVB contribute to skin cancer"],
  "UVB is shorter and causes sunburn; UVA penetrates deeper and is present all year. Both contribute to skin cancer, and tanning beds mainly use UVA.")

q("risk", "The nurse discusses skin cancer risk with clients at a health fair. Which client statement indicates a need for more teaching?",
  ["'My transplant medications can raise my risk.' || Accurate; immunosuppression from transplant medications is a major risk factor",
   "'Smoking adds to my risk for skin cancer.' || Accurate; smoking is a listed risk factor",
   "*'I'm only 25, so skin cancer isn't a worry yet.'",
   "'My history of bad sunburns raises my risk.' || Accurate; a history of severe sunburn adds risk"],
  "Skin cancer is very common and increasingly seen in younger adults; don't assume only older clients get it. Risk factors include immunosuppression such as transplant medications, smoking and a history of severe sunburn.")

q("precan", "A 66-year-old retired golfer is diagnosed with actinic keratosis on the ears and asks why the provider wants to treat it. Which response by the nurse is accurate?",
  ["'Because it is already a melanoma that is spreading.' || Actinic keratosis is precancerous, not melanoma",
   "*'Because it can progress to squamous cell carcinoma.'",
   "'Because it is a bacterial infection that can spread.' || Actinic keratosis is a precancerous lesion, not an infection",
   "'Because it will turn into basal cell carcinoma.' || Actinic keratosis can progress to squamous cell carcinoma"],
  "Actinic (solar) keratosis is rough, scaly, red-brown patches on sun-exposed skin such as the ears and scalp. It is precancerous and can progress to squamous cell carcinoma.")
q("precan", "Which pairings of a precancerous condition and its description are correct? " + SATA,
  ["*Actinic keratosis: rough, scaly, red-brown patches on sun-exposed skin",
   "*Dysplastic nevi syndrome: many atypical moles that often run in families",
   "Actinic keratosis: a lesion that progresses to basal cell carcinoma || It can progress to squamous cell carcinoma",
   "*Ugly duckling sign: a mole that looks different from the client's others",
   "Dysplastic nevi syndrome: having more moles lowers the concern || More moles raise concern"],
  "Actinic keratosis is rough, scaly, red-brown patches on sun-exposed skin and can progress to squamous cell carcinoma. Dysplastic nevi syndrome is many atypical moles, often familial; more moles raise concern. Teach the ugly duckling sign.")

q("bcc", "During a telehealth visit, a 55-year-old teacher describes a spot on her nose. Which description by the client suggests basal cell carcinoma?",
  ["'It's a rough, scaly, red-brown patch like the ones on my scalp.' || This describes actinic keratosis",
   "'It's red, thick and scaly, and it hurts when I touch it.' || This describes squamous cell carcinoma",
   "*'It's a shiny pink bump, and I can see tiny blood vessels in it.'",
   "'It's a mole with several colors and edges that look jagged.' || Color variation and border irregularity are ABCDE melanoma signs"],
  "Basal cell carcinoma is a smooth, raised, shiny/waxy pink lesion with visible small vessels. It may have a central depression and is often a 'sore that doesn't heal.'")
q("bcc", "A 68-year-old client has biopsy-confirmed basal cell carcinoma. Which treatments might the nurse expect the provider to discuss? " + SATA,
  ["*Curettage and electrodesiccation",
   "*Mohs micrographic surgery",
   "*Topical fluorouracil for a superficial basal lesion",
   "Standard chemotherapy as the first treatment || Standard chemotherapy is for cancers that don't respond to other therapies",
   "A bulky pressure dressing alone as the cure || Pressure dressings are graft-site care, not cancer treatment"],
  "Curettage and electrodesiccation is used for basal or squamous cell lesions, Mohs removes thin layers until no cancer cells remain, and topical fluorouracil treats actinic keratosis or superficial basal lesions. Standard chemotherapy is for cancers that don't respond to other therapies.")

q("scc", "A 75-year-old retired welder who smokes has a red, thick, scaly lesion on the ear that has started to bleed. Which statement by the nurse is best?",
  ["'This looks like basal cell carcinoma, which rarely spreads, so we can watch it.' || The description fits SCC (squamous cell carcinoma), and lesions need evaluation",
   "*'A dermatologist should check this, and a biopsy will show what type it is.'",
   "'This is a normal actinic keratosis, so no follow-up is needed for it.' || Actinic keratosis is precancerous, and this lesion is bleeding",
   "'Bleeding means it is melanoma, which is the least aggressive kind.' || Melanoma is the most dangerous skin cancer"],
  "Squamous cell carcinoma is a red, thick, scaly lesion that may ulcerate, hurt and bleed; it is common on the lips, ears and nose and is more aggressive than BCC (basal cell carcinoma). Refer for dermatologic evaluation; biopsy determines the lesion type.")
q("scc", "The nurse reviews skin findings for several clients. Which findings should make the nurse suspect squamous cell carcinoma? " + SATA,
  ["*A painful, red, thick, scaly lesion on the lower lip",
   "*An untreated actinic keratosis on the nose that has thickened and ulcerated",
   "A smooth, pearly pink bump with small visible vessels || This describes basal cell carcinoma",
   "*A red, scaly lesion on the ear that bleeds easily",
   "One mole that looks unlike the client's other moles || This is the ugly duckling sign for atypical moles"],
  "Squamous cell carcinoma is a red, thick, scaly lesion that may ulcerate, hurt and bleed. It is common on the lips, ears and nose and can arise from untreated actinic keratosis.")

q("mel", "A 49-year-old client's malignant melanoma has spread to the lymph nodes. Which treatment should the nurse expect the provider to discuss?",
  ["Cryosurgery with liquid nitrogen || Cryosurgery freezes a local lesion",
   "Topical fluorouracil cream || Used for actinic keratosis or superficial basal lesions",
   "*Immunotherapy or targeted therapy",
   "Curettage and electrodesiccation || Used for basal or squamous cell lesions"],
  "Melanoma is the most dangerous and highly metastatic skin cancer. Immunotherapy and targeted therapy are used for advanced or metastatic disease.")
q("mel", "A 30-year-old software developer who rarely goes outside says, 'I can't get melanoma because I'm never in the sun.' Which response by the nurse is best?",
  ["'That's right; melanoma only forms on skin that gets a lot of sun.' || Melanoma can occur anywhere, not just sun-exposed skin",
   "'You're correct, so you only need to check your scalp for it.' || The entire skin surface is assessed",
   "'Melanoma is the least aggressive kind, so it is not a concern.' || Melanoma is the most dangerous skin cancer",
   "*'Melanoma can occur anywhere, even in the eyes or inside the mouth.'"],
  "Melanoma can occur anywhere, including the eyes and mucosal surfaces, not just sun-exposed skin, so assess the entire skin surface. It is the most dangerous and highly metastatic skin cancer.")

q("abcde", "The nurse asks clients about changes in their moles. Which client report reflects the E in the ABCDE guide?",
  ["'It measures about 8 mm across.' || This reflects D, diameter over 6 mm",
   "'The two halves of it don't match.' || This reflects A, asymmetry",
   "*'It used to be flat, but now it's raised.'",
   "'It has brown and black areas in it.' || This reflects C, color variation"],
  "E stands for Evolving: changing size, shape, color or appearance. A = asymmetry, B = border irregularity, C = color variation, D = diameter over 6 mm.")
q("abcde", "The nurse finds a 7 mm mole with an irregular border on a 50-year-old truck driver's shoulder. He asks, 'Can you tell if this is cancer?' Which response by the nurse is best?",
  ["'Yes, the uneven border tells me that it is a melanoma.' || The type cannot be known by looking; biopsy determines it",
   "*'A dermatologist should see it; a biopsy will show what it is.'",
   "'Only the color of a mole matters, so this one is fine.' || Border and diameter are also ABCDE warning signs",
   "'A mole that is smaller than 10 mm is never a concern.' || A diameter over 6 mm is a warning sign"],
  "A diameter over 6 mm and border irregularity are ABCDE warning signs. Refer for dermatologic evaluation; biopsy determines the type. Assess the whole skin, including the ugly duckling.")

q("biopsy", "A nursing student reviews biopsy types with the nurse. Which statement by the student needs correction?",
  ["'A punch biopsy takes a cylinder of tissue to a set depth.' || Accurate description of a punch biopsy",
   "*'An excisional biopsy removes only the surface of the lesion.'",
   "'An incisional biopsy removes part of a larger lesion.' || Accurate description of an incisional biopsy",
   "'A shave biopsy removes the superficial tissue only.' || Accurate description of a shave biopsy"],
  "Excisional biopsy removes the whole lesion plus a margin of healthy tissue and is preferred for suspected melanoma when size permits. Shave is superficial, punch is a cylindrical sample to a set depth, and incisional removes part of a larger lesion.")

q("local", "A 62-year-old client had photodynamic therapy for a skin lesion. Which statements by the client show understanding? " + SATA,
  ["*'A light-sensitizing drug was activated with blue light.'",
   "*'I'll stay out of the sunlight for about 48 hours.'",
   "*'Some redness, pain and swelling may happen.'",
   "'Sun on the area will help the treatment work.' || Avoid sunlight for about 48 hours",
   "'The lesion was frozen with liquid nitrogen.' || Freezing with liquid nitrogen is cryosurgery"],
  "Photodynamic therapy uses a light-sensitizing agent activated with blue light. Avoid sunlight for about 48 hours; redness, pain and swelling can occur.")

q("surg", "A 71-year-old client is scheduled for curettage and electrodesiccation. Which statement by the client indicates a need for more teaching?",
  ["'The lesion will be scraped away first.' || Accurate; the lesion is scraped",
   "'Heat will destroy any tissue that's left.' || Accurate; electrodesiccation destroys remaining tissue with heat",
   "'It's used for basal or squamous lesions.' || Accurate; it is used for basal or squamous cell lesions",
   "*'Thin layers will be checked under a microscope.'"],
  "Curettage and electrodesiccation scrapes the lesion and destroys remaining tissue with heat; it is used for basal or squamous cell lesions. Checking thin layers under a microscope describes Mohs surgery.")
q("surg", "A 44-year-old client with melanoma is scheduled for a wide excision and a sentinel lymph node biopsy. Which statements by the nurse are accurate? " + SATA,
  ["*'The wide excision removes the lesion and surrounding tissue.'",
   "*'A tracer or dye will find the first node the tumor drains to.'",
   "'The sentinel node biopsy freezes the nodes with liquid nitrogen.' || Freezing with liquid nitrogen is cryosurgery",
   "'The wide excision takes off one thin layer at a time.' || Layer-by-layer removal is Mohs surgery",
   "*'A flap or skin graft may be needed to close the wound.'"],
  "Wide excision removes the lesion plus surrounding tissue and may need a flap or skin graft to close. Sentinel lymph node biopsy uses a tracer or dye near the tumor to find the first draining node.")

q("graft", "A 50-year-old client asks why the surgeon chose a split-thickness skin graft to cover a large wound. Which response by the nurse is accurate?",
  ["'It includes the full dermis, so it is stitched in place.' || This describes a full-thickness graft",
   "'The skin comes from a cadaver instead of your own body.' || An autograft uses the client's own healthy skin",
   "*'It can be meshed to stretch over a larger area.'",
   "'Its donor site will lose all of its sweat glands.' || The donor site keeps follicles and sweat glands"],
  "A split-thickness graft is epidermis plus superficial dermis and can be meshed to cover a larger area. The donor site keeps follicles and sweat glands. A full-thickness graft includes the entire epidermis and dermis and is stitched into position.")

q("donor", "The nurse teaches a 37-year-old client about home care of a thigh donor site. Which statement by the client needs correction?",
  ["'Wet drainage for a few days is expected.' || Accurate; weeping for about 3-5 days, then a dry phase",
   "*'I'll peel off the dressing each morning to check it.'",
   "'The site may look discolored as it heals.' || Accurate; discoloration is expected",
   "'I'll protect the site from the sun for about a year.' || Accurate; teach sun protection for about a year"],
  "Donor site: wet, weeping drainage for about 3-5 days, then a dry phase; discoloration is expected; the nonadherent dressing stays in place until it lifts off as it heals; teach sun protection for about a year.")
q("donor", "The nurse is caring for a client 36 hours after a skin graft to the hand. Which statement about the graft site is accurate?",
  ["The bulky dressing is removed daily to inspect the graft || The bulky pressure dressing stays about 3-5 days",
   "*Vascularization of the graft may begin within about 36 hours",
   "Weeping drainage that turns dry is the expected graft course || This is the expected course of the donor site",
   "Fluid collecting under the graft helps it adhere to the bed || Trapped fluid keeps the graft from adhering"],
  "Graft site care: bulky pressure dressing for about 3-5 days, immobilize and elevate, monitor color, vascularization and adherence, and watch for trapped blood or fluid. Vascularization may begin within about 36 hours.")

q("systemic", "A 58-year-old client with metastatic melanoma is starting immunotherapy. Which statement by the client indicates a need for more teaching?",
  ["'It helps my body recognize and attack the cancer.' || Accurate description of immunotherapy",
   "'It can help my body build immune memory.' || Accurate; immunotherapy builds immune memory",
   "*'It works by freezing the tumor cells off.'",
   "'It is being used because the cancer has spread.' || Accurate; it is used for advanced or metastatic disease"],
  "Immunotherapy helps the body recognize and attack malignant cells and build immune memory. It and targeted therapy are used for advanced or metastatic disease. Freezing with liquid nitrogen is cryosurgery.")

q("promo", "The nurse teaches sun protection to a 38-year-old landscape gardener. Which statement by the client needs correction?",
  ["'I'll wear a wide-brimmed hat and sunglasses.' || Accurate sun-protection teaching",
   "'I'll try to work before 11 a.m. or after 3 p.m.' || Accurate; avoid peak sun, about 11 a.m. to 3 p.m.",
   "*'SPF (sun protection factor) 4 is enough for a short day outside.'",
   "'I'll put sunscreen on 30 minutes before I go out.' || Accurate; apply about 30 minutes before going out"],
  "Sun protection: avoid peak sun (about 11 a.m. to 3 p.m.), wear long sleeves, a wide-brimmed hat and sunglasses, and apply SPF 15-30 sunscreen about 30 minutes before going out.")
q("promo", "A 44-year-old pharmacist asks the nurse how to do a monthly skin self-exam. Which instruction by the nurse is best?",
  ["'Do it before bed in a dim room so moles stand out.' || The exam is done in a well-lit room",
   "'Check just your face, since it gets the most sun.' || The whole skin surface is checked",
   "*'Do it after a shower in a well-lit room with mirrors.'",
   "'A self-exam replaces the yearly professional check.' || 'Check your birthday suit on your birthday' means an annual professional exam"],
  "Do the self-exam after a bath or shower in a well-lit room using full-length and handheld mirrors. Know your usual moles, use ABCDE, and get an annual professional skin check.")
