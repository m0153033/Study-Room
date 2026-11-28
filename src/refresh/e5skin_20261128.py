T = "e5skin"; SET = "20261128"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("patho", "The nurse explains to a 44-year-old pool maintenance worker how ultraviolet exposure can lead to skin cancer. Which effects of UV exposure should the nurse describe? " + SATA,
  ["*It damages the DNA in skin cells",
   "*It suppresses cellular immunity",
   "*It promotes uncontrolled cell growth",
   "It infects the skin cells with a virus || UV exposure is not an infection",
   "It thickens the dermis in a harmless way || UV damage is not harmless; it leads to cancer"],
  "UV exposure damages DNA, suppresses cellular immunity and promotes uncontrolled growth of epidermal cells. Cancer that invades the dermis can reach blood and lymph vessels and metastasize.")

q("uv", "A 28-year-old cyclist says, 'I never burn, so the sun can't be giving me skin cancer.' Which response by the nurse is best?",
  ["'That's true; skin cancer only comes from the rays that burn.' || Both UVA and UVB contribute to skin cancer",
   "*'UVA rays don't burn, but they go deep and add to cancer risk.'",
   "'UVB rays go the deepest, so not burning means you're safe.' || UVA penetrates deeper; UVB causes sunburn",
   "'You only need to worry about UV rays during the summer.' || UVA is present all year"],
  "UVB is shorter and causes sunburn; UVA penetrates deeper and is present all year. Both contribute to skin cancer.")

q("risk", "The nurse is scheduling skin screenings at a community clinic. Which client has the greatest risk for skin cancer?",
  ["A 29-year-old with dark skin and brown eyes who works indoors || Dark skin, brown eyes and indoor work are not listed risks",
   "*A 45-year-old with green eyes, many atypical moles and a past skin cancer",
   "A 50-year-old with lots of melanin who has never had a sunburn || Melanin-rich skin without sunburn history is lower risk",
   "A 35-year-old with brown eyes who has never used a tanning bed || No listed risk factors are present"],
  "Major risk factors include cumulative UV exposure, tanning beds, immunosuppression, personal or family history of skin cancer, chemical exposure and smoking. Additional risks include fair skin, blue or green eyes, severe sunburns, many or atypical moles, albinism and outdoor activities.")

q("precan", "The nurse performs a skin assessment on a 72-year-old retired roofer. Where is the nurse most likely to find actinic keratosis?",
  ["*On the ears and scalp",
   "On skin that is always covered by clothing || Actinic keratosis appears on sun-exposed skin",
   "Only on the inside of the mouth || Actinic keratosis appears on sun-exposed skin such as the ears and scalp",
   "Only on the palms of the hands || Actinic keratosis appears on sun-exposed skin such as the ears and scalp"],
  "Actinic (solar) keratosis is rough, scaly, red-brown patches on sun-exposed skin such as the ears and scalp. It is precancerous and can progress to squamous cell carcinoma.")
q("precan", "A client's chart lists both actinic keratosis and dysplastic nevi syndrome. After teaching, which statement by the client shows understanding?",
  ["'Both are skin infections that clear up with antibiotics.' || Neither is an infection; both are precancerous concerns",
   "*'One is scaly sun patches; the other is many atypical moles.'",
   "'The moles mean less worry the more of them I have.' || More moles raise concern in dysplastic nevi syndrome",
   "'The scaly patches can turn into basal cell carcinoma.' || Actinic keratosis can progress to squamous cell carcinoma"],
  "Actinic keratosis is rough, scaly, red-brown patches on sun-exposed skin that can progress to squamous cell carcinoma. Dysplastic nevi syndrome is many atypical moles, often familial; more moles raise concern, and the ugly duckling sign is taught.")

q("bcc", "The nurse reviews biopsy results for four clients. Which client's skin cancer is least likely to metastasize?",
  ["Malignant melanoma on the lower leg || Melanoma is the most dangerous and highly metastatic",
   "Squamous cell carcinoma on the lower lip || SCC is more aggressive and more likely to metastasize than BCC",
   "*Basal cell carcinoma on the side of the nose",
   "Squamous cell carcinoma arising on the ear || SCC is more aggressive than BCC"],
  "BCC (basal cell carcinoma) is the most common and least aggressive skin cancer; metastasis is rare. SCC is more aggressive and more likely to metastasize, and melanoma is the most dangerous and highly metastatic.")
q("bcc", "A 66-year-old client is newly diagnosed with basal cell carcinoma. Which statements by the client show understanding? " + SATA,
  ["*'This is the most common kind of skin cancer.'",
   "*'It rarely spreads, but it still needs to be treated.'",
   "*'It can look like a shiny pink bump with tiny vessels.'",
   "'It is more aggressive than squamous cell cancer.' || BCC is the least aggressive; SCC is more aggressive",
   "'It grew out of an untreated actinic keratosis.' || Untreated actinic keratosis can progress to SCC, not BCC"],
  "BCC is the most common and least aggressive skin cancer and metastasis is rare, but it still needs dermatologic evaluation, biopsy and treatment. It is a smooth, raised, shiny/waxy pink lesion with visible small vessels.")

q("scc", "The nurse teaches a 63-year-old client with a history of squamous cell carcinoma to check his skin. Which areas should the nurse point out as common sites for this cancer?",
  ["*The lips, ears and nose",
   "The palms, soles and nail beds || SCC is common on the lips, ears and nose",
   "Only skin that is covered by clothing || SCC is common on the lips, ears and nose",
   "The eyes and inside of the mouth only || SCC is common on the lips, ears and nose"],
  "Squamous cell carcinoma is a red, thick, scaly lesion that may ulcerate, hurt and bleed. It is common on the lips, ears and nose and can arise from untreated actinic keratosis.")
q("scc", "A 69-year-old client with actinic keratosis on the nose says, 'It's just a rough patch, so I'll skip my follow-up.' Which response by the nurse is best?",
  ["'You're right; these patches never change into anything else.' || Untreated actinic keratosis can become SCC",
   "'It can turn into basal cell cancer, which spreads very fast.' || AK progresses to SCC; BCC rarely spreads",
   "*'Untreated, it can become squamous cell cancer, which can spread.'",
   "'It can only become a melanoma, so watch it for color changes.' || Actinic keratosis can progress to squamous cell carcinoma"],
  "SCC (squamous cell carcinoma) can arise from untreated actinic keratosis. SCC is more aggressive and more likely to metastasize than BCC (basal cell carcinoma).")

q("mel", "The nurse performs a full skin assessment on a 42-year-old client with a history of malignant melanoma. Which areas should the nurse include? " + SATA,
  ["*The eyes",
   "*Mucosal surfaces such as the inside of the mouth",
   "*Skin that is usually covered from the sun",
   "Only the sun-exposed skin of the face and arms || Melanoma can occur anywhere; assess the entire skin surface",
   "Only the scalp, since melanoma starts there || Melanoma can occur anywhere, not just the scalp"],
  "Melanoma can occur anywhere, including the eyes and mucosal surfaces, not just sun-exposed skin, so the entire skin surface is assessed. It is the most dangerous and highly metastatic skin cancer.")
q("mel", "Which statement correctly compares malignant melanoma with basal cell carcinoma?",
  ["Both are equally likely to spread to other parts of the body || Melanoma is highly metastatic; BCC rarely metastasizes",
   "*Melanoma is highly metastatic; basal cell carcinoma rarely spreads",
   "Melanoma is the most common; basal cell carcinoma is the most dangerous || BCC is the most common; melanoma is the most dangerous",
   "Melanoma occurs only on sun-exposed skin; basal cell occurs anywhere || Melanoma can occur anywhere, including eyes and mucosa"],
  "Malignant melanoma is the most dangerous and highly metastatic skin cancer; early detection and treatment are critical. BCC is the most common and least aggressive skin cancer, and metastasis is rare.")

q("abcde", "A 39-year-old client points to a mole and says, 'This one has red, white and black areas in it.' Which ABCDE letter does this finding represent?",
  ["A: Asymmetry || Asymmetry means one half does not match the other",
   "B: Border irregularity || Border refers to ragged, notched or blurred edges",
   "*C: Color variation",
   "D: Diameter over 6 mm || Diameter refers to size larger than a pencil eraser"],
  "ABCDE: Asymmetry, Border irregularity, Color variation, Diameter over 6 mm (about a pencil eraser), Evolving (changing size, shape, color or appearance).")
q("abcde", "The nurse checks four moles on a 54-year-old client. Which mole is most concerning?",
  ["A 4 mm round mole that is one even tan color || No ABCDE warning signs are present",
   "A 3 mm mole, unchanged for years, with matching halves || No ABCDE warning signs are present",
   "*A 7 mm mole whose edges have recently become ragged",
   "A 5 mm mole with smooth edges and a single brown color || No ABCDE warning signs are present"],
  "A diameter over 6 mm, border irregularity and evolving (change) are ABCDE warning signs. Refer for dermatologic evaluation; biopsy determines the lesion type.")

q("biopsy", "The provider plans to take a cylinder-shaped tissue sample down to a set depth from a client's lesion. Which type of biopsy should the nurse prepare for?",
  ["Shave biopsy || A shave biopsy removes superficial tissue only",
   "*Punch biopsy",
   "Incisional biopsy || An incisional biopsy removes part of a larger lesion",
   "Excisional biopsy || An excisional biopsy removes the whole lesion plus a margin"],
  "Punch biopsy takes a cylindrical sample to a set depth. Shave removes superficial tissue, incisional removes part of a larger lesion, and excisional removes the whole lesion plus a margin (preferred for suspected melanoma when size permits).")

q("local", "Two weeks after cryosurgery for a skin lesion, a client asks why the provider has scheduled a second session. Which response by the nurse is accurate?",
  ["'A second session means the cancer has spread to the lymph nodes.' || Cryosurgery may simply need repeating",
   "'The first treatment caused bleeding that would not stop.' || Bleeding that won't stop is not an expected effect",
   "*'Cryosurgery sometimes needs to be repeated to treat the lesion.'",
   "'The second session will activate the drug with blue light.' || Blue light activation is photodynamic therapy"],
  "Cryosurgery uses liquid nitrogen to freeze the lesion. Expected effects include redness, swelling and a pale/white scar, and the treatment may need repeating.")

q("surg", "A client is scheduled for a procedure in which the lesion is scraped away and the remaining tissue is destroyed with heat. Which procedure should the nurse expect?",
  ["Mohs micrographic surgery || Mohs removes thin layers checked under a microscope",
   "Sentinel lymph node biopsy || This uses a tracer or dye to find the first draining node",
   "*Curettage and electrodesiccation",
   "Wide excision || Wide excision removes the lesion plus surrounding tissue"],
  "Curettage and electrodesiccation scrapes the lesion and destroys remaining tissue with heat; it is used for basal or squamous cell lesions.")
q("surg", "A nursing student reviews skin cancer surgeries with the nurse. Which statement by the student needs correction?",
  ["'Wide excision removes the lesion plus the tissue around it.' || Accurate; it may need a flap or graft to close",
   "*'Mohs takes out the whole lesion in one large piece.'",
   "'A sentinel node biopsy uses a tracer or dye near the tumor.' || Accurate; it finds the first draining node",
   "'Curettage and electrodesiccation is used for basal lesions.' || Accurate; it is used for basal or squamous lesions"],
  "Mohs micrographic surgery removes one thin layer at a time and checks it under a microscope until no cancer cells remain. Wide excision removes the lesion plus surrounding tissue and may need a flap or skin graft.")

q("graft", "A split-thickness skin graft is harvested with a dermatome from the client's own buttock. Which term should the nurse use for this graft?",
  ["*Autograft",
   "Cadaver graft || A cadaver graft is from another person, not the client",
   "Synthetic patch || The skin came from the client's own body",
   "Full-thickness graft || A dermatome harvests thin split-thickness skin"],
  "An autograft is skin taken from the client's own healthy skin. A dermatome harvests thin donor skin; thigh and buttock are common donor areas. A split-thickness graft is epidermis plus superficial dermis and can be meshed.")

q("donor", "A 52-year-old client being discharged after a skin graft asks how long to protect the thigh donor site from the sun. Which response by the nurse is accurate?",
  ["'For about 48 hours after the surgery.' || 48 hours of sun avoidance is photodynamic therapy teaching",
   "'Until the dressing comes off, about 3 to 5 days.' || Sun protection for the donor site lasts about a year",
   "*'For about a year after the graft.'",
   "'Only until the wet drainage stops.' || Sun protection for the donor site lasts about a year"],
  "Donor site care: wet, weeping drainage for about 3-5 days, then a dry phase; the nonadherent dressing stays until it lifts off; discoloration is expected; teach sun protection for about a year.")
q("donor", "The nurse supervises an assistive staff member caring for a client 1 day after a skin graft to the lower leg. Which action by the staff member requires the nurse to intervene?",
  ["Keeping the grafted leg raised on pillows || Elevation is correct graft-site care",
   "Leaving the bulky pressure dressing in place || The bulky dressing stays on about 3-5 days",
   "*Helping the client walk to loosen the stiff leg",
   "Reporting blood seen under the edge of the graft || Trapped blood keeps the graft from adhering and should be reported"],
  "Graft site care: bulky pressure dressing for about 3-5 days, immobilize and elevate, monitor color, vascularization and adherence, and watch for blood or fluid trapped under the graft.")

q("systemic", "Which statement correctly compares immunotherapy and targeted therapy for metastatic skin cancer?",
  ["*Immunotherapy helps the body attack the cells; targeted therapy blocks growth signals",
   "Immunotherapy freezes the tumor; targeted therapy removes it layer by layer || These describe cryosurgery and Mohs",
   "Immunotherapy is for actinic keratosis; targeted therapy is used before biopsy || Both are for advanced or metastatic disease",
   "Immunotherapy blocks tumor blood vessels; targeted therapy builds immune memory || The two mechanisms are reversed"],
  "Immunotherapy helps the body recognize and attack malignant cells and build immune memory. Targeted therapy blocks growth signals and/or tumor blood-vessel formation. Both are used for advanced or metastatic disease.")

q("promo", "A 30-year-old client at a pharmacy asks the nurse which sunscreen to buy. Which choice best fits sun-protection teaching?",
  ["A tanning oil with SPF 4 || The lecture recommends SPF 15-30",
   "*An unexpired sunscreen with SPF 15-30",
   "An SPF 30 bottle that expired last year || Sunscreen has a shelf life; check expiration",
   "No sunscreen if a base tan is present || A tan does not replace sunscreen"],
  "Use SPF 15-30 sunscreen, check the expiration date, apply about 30 minutes before going out, and reapply every 2 hours and more often when swimming or sweating.")
q("promo", "A family is planning an afternoon at an outdoor fair. Which outfit choice best fits sun-protection teaching?",
  ["A tank top, shorts and a baseball cap || Long sleeves and a wide-brimmed hat give more protection",
   "*Long sleeves, a wide-brimmed hat and sunglasses",
   "A short-sleeved shirt and no hat or glasses || Long sleeves, a wide-brimmed hat and sunglasses are taught",
   "A swimsuit with sunglasses and a visor only || Long sleeves and a wide-brimmed hat are taught"],
  "Sun protection: avoid peak sun (about 11 a.m. to 3 p.m.), wear long sleeves, a wide-brimmed hat and sunglasses, avoid tanning booths, and apply SPF 15-30 sunscreen about 30 minutes before going out.")
