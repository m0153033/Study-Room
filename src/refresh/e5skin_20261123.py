T = "e5skin"; SET = "20261123"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("patho", "A 58-year-old client with a newly diagnosed skin cancer asks why the dermatologist is worried about whether the tumor has reached the dermis. Which response by the nurse is best?",
  ["The dermis is the layer where squamous cells, basal cells and melanocytes live || These cells live in the epidermis, not the dermis",
   "*The dermis contains blood and lymph vessels, so cancer there can spread to other areas",
   "Once cancer reaches the dermis it stops growing because there are no cells there || The dermis has tissue and vessels; invasion allows spread",
   "The dermis is only a concern because it causes the skin to tan || Tanning is not the concern; vessel access and metastasis are"],
  "Skin cancer begins as abnormal growth of epidermal cells. Once it invades the dermis it can reach blood and lymph vessels and metastasize.")

q("uv", "A 22-year-old lifeguard asks the nurse how the two types of ultraviolet light differ. Which statement by the nurse is accurate?",
  ["UVA is the shorter wave that causes sunburn, and it is present only in the summer months || UVB causes sunburn; UVA is present all year",
   "Only UVA contributes to skin cancer, so a client never needs to block UVB rays || Both UVA and UVB contribute to skin cancer",
   "*UVB is shorter and causes sunburn; UVA goes deeper and is present all year",
   "UVB penetrates the deepest into the skin and is the main type used in tanning beds || UVA penetrates deeper and is the main type in tanning beds"],
  "UVB is shorter and causes sunburn; UVA penetrates deeper and is present year-round. Both contribute to skin cancer, and tanning beds mainly use UVA.")

q("risk", "The nurse in a dermatology clinic reviews the health histories of several clients. Which clients have an increased risk for skin cancer? " + SATA,
  ["*A 45-year-old kidney transplant recipient taking transplant medications",
   "*A 30-year-old with red hair, freckles and blue eyes",
   "*A 26-year-old who uses a tanning bed every week",
   "*A 52-year-old roofer who smokes and has had several severe sunburns",
   "A 40-year-old with dark skin, lots of melanin and brown eyes || Dark skin with lots of melanin is not listed as a risk factor"],
  "Major risk factors include cumulative sun/UV exposure, tanning beds, immunosuppression (such as transplant medications), smoking and chemical exposure. Fair, freckled skin with red or blond hair, blue/green eyes and severe sunburn history add risk. Skin cancer is increasingly seen in younger adults.")

q("precan", "A 68-year-old farmer has rough, scaly, red-brown patches on the tops of his ears and scalp. Which teaching by the nurse is most important?",
  ["'These are normal age spots from getting older and do not need any follow-up.' || Actinic keratosis is precancerous and needs follow-up",
   "'These are melanoma, which is the most dangerous and fastest-spreading skin cancer.' || The description fits actinic keratosis, not melanoma",
   "*'This may be actinic keratosis, which can progress to squamous cell carcinoma.'",
   "'These are basal cell carcinoma and will spread widely through your body.' || This is actinic keratosis; BCC rarely metastasizes"],
  "Actinic (solar) keratosis appears as rough, scaly, red-brown patches on sun-exposed skin and can progress to squamous cell carcinoma.")

q("precan", "A 34-year-old client has dysplastic nevi syndrome, like her mother. Which instruction should the nurse include in her teaching?",
  ["*'Watch for an ugly duckling: a mole that looks unlike your others.'",
   "'Since this is a single harmless mole, you don't need to check it.' || Dysplastic nevi syndrome means many atypical moles needing monitoring",
   "'This is a bacterial infection, so finish your antibiotics.' || It is not an infection; it is many atypical moles, often familial",
   "'Having more moles actually lowers your concern for skin cancer.' || More moles raise concern, not lower it"],
  "Dysplastic nevi syndrome is many atypical moles, often familial; more moles raise concern. The ugly duckling sign (a mole that looks different from the rest) is taught for monitoring.")

q("bcc", "A 62-year-old client has a lesion on the side of the nose. Which description would lead the nurse to suspect basal cell carcinoma?",
  ["Rough, scaly, red-brown patch on sun-exposed skin || This describes actinic keratosis",
   "Mole with mixed colors, asymmetry and irregular borders || This suggests melanoma (ABCDE findings)",
   "Red, thick, scaly lesion that is painful and bleeds || This describes squamous cell carcinoma",
   "*Shiny, pearly pink bump with tiny visible vessels"],
  "Basal cell carcinoma is a smooth, raised, shiny/waxy pink lesion with visible small vessels; it may have a central depression and is often a 'sore that doesn't heal.'")

q("bcc", "A 71-year-old client just diagnosed with basal cell carcinoma on the forehead asks, 'Is this going to spread all through my body?' Which response by the nurse is accurate?",
  ["'Yes, it is the most dangerous skin cancer and it spreads very quickly.' || Melanoma is the most dangerous; BCC is least aggressive",
   "*'It is the most common, least aggressive type, and spread is rare.'",
   "'It spreads rapidly through the lymph system, so you need a sentinel node biopsy.' || BCC rarely metastasizes; sentinel node biopsy is for melanoma",
   "'It only becomes a problem if it shows up on the soles of your feet.' || BCC is not limited to the feet"],
  "BCC is the most common and least aggressive skin cancer; metastasis is rare. It still needs dermatologic evaluation, biopsy and treatment.")

q("scc", "A 70-year-old client who smoked for years has a red, thick, scaly lesion on the lower lip that is sore and bleeds easily. Which skin cancer should the nurse suspect?",
  ["Basal cell carcinoma || BCC is shiny, waxy and pink, not thick, scaly and bleeding",
   "Actinic keratosis || AK is a rough, scaly precancerous patch, not an ulcerating painful lesion",
   "*Squamous cell carcinoma",
   "A dysplastic nevus || Dysplastic nevi are atypical moles, not thick scaly bleeding lesions"],
  "Squamous cell carcinoma is a red, thick, scaly lesion that may ulcerate, hurt and bleed. It is common on the lips, ears and nose.")

q("scc", "The nurse is preparing a teaching session on squamous cell carcinoma (SCC). Which statements should the nurse include? " + SATA,
  ["*It is more aggressive than basal cell carcinoma",
   "*It is more likely to metastasize than basal cell carcinoma",
   "*It can arise from untreated actinic keratosis",
   "*It commonly appears on the lips, ears and nose",
   "It typically looks like a shiny, waxy, pink bump || That describes basal cell carcinoma"],
  "SCC is more aggressive and more likely to metastasize than BCC, can arise from untreated actinic keratosis, and is common on the lips, ears and nose.")

q("mel", "During a full skin assessment, a 35-year-old client asks why the nurse is checking between the toes and inside the mouth. Which response is best?",
  ["'Melanoma only appears on the scalp, so I'm being extra careful.' || Melanoma is not limited to the scalp",
   "'I'm looking for sunburn, since melanoma only occurs on sun-exposed skin.' || Melanoma can occur on non-sun-exposed areas too",
   "'This is routine, but skin cancer never occurs in those places.' || Melanoma can occur in mucosal surfaces",
   "*'Melanoma can occur anywhere, including eyes and mucosal surfaces.'"],
  "Melanoma can occur anywhere, including the eyes and mucosal surfaces, not just sun-exposed skin, so the entire skin surface is assessed. It is the most dangerous and highly metastatic skin cancer.")

q("mel", "A 47-year-old client with a confirmed malignant melanoma is scheduled for a sentinel lymph node biopsy and asks what it is for. Which explanation is correct?",
  ["*'A tracer or dye finds the first draining node to check for spread.'",
   "'Thin layers of skin are removed and checked under a microscope one at a time.' || That describes Mohs surgery",
   "'The lesion is frozen with liquid nitrogen to destroy it.' || That describes cryosurgery",
   "'A light-sensitizing drug is applied and activated with blue light.' || That describes photodynamic therapy"],
  "Melanoma is the most likely skin cancer to metastasize. Sentinel lymph node biopsy uses a tracer or dye near the tumor to find the first draining node and check for spread.")

q("abcde", "The nurse assesses a mole on a 41-year-old client's back. Which findings are concerning using the ABCDE guide? " + SATA,
  ["*One half of the mole does not match the other half",
   "*The edges are ragged and irregular",
   "*It has shades of brown, black and red",
   "*It is larger than a pencil eraser",
   "It is round, 3 mm, and one even tan color || Symmetric, small, single-color moles are not ABCDE warning signs"],
  "ABCDE: Asymmetry, Border irregularity, Color variation, Diameter over 6 mm (about a pencil eraser), Evolving.")

q("abcde", "The nurse teaches a client about the ABCDE guide for moles. Which statement by the client indicates a need for more teaching?",
  ["'A means one half of the mole doesn't match the other half.' || Correct; A is asymmetry",
   "'E means I should report a mole that is changing in size, shape or color.' || Correct; E is evolving",
   "*'D means I should worry if the mole is darker than my other moles.'",
   "'Six millimeters is about the size of a pencil eraser.' || Correct; this is the diameter guide"],
  "D stands for diameter over 6 mm (about a pencil eraser), not darkness. A = asymmetry, B = border, C = color, E = evolving (changing size, shape, color or appearance).")

q("biopsy", "A 55-year-old client has a large lesion on the back, and the provider plans to remove only a portion of it for diagnosis. Which type of biopsy does the nurse expect?",
  ["Excisional || Excisional removes the whole lesion plus a margin",
   "Shave || Shave removes only superficial tissue",
   "*Incisional",
   "Punch || Punch takes a cylindrical sample to a set depth"],
  "Incisional biopsy removes part of a larger lesion. Excisional removes the whole lesion plus a margin (preferred for suspected melanoma when size permits); shave is superficial; punch is a cylindrical sample.")

q("local", "A 66-year-old client calls the clinic the day after cryosurgery for a skin lesion and reports redness and swelling at the site. Which response by the nurse is best?",
  ["'Redness means the treatment failed and you need a wide excision.' || Redness and swelling are expected after cryosurgery",
   "*'Redness and swelling are expected, and it may leave a pale scar.'",
   "'Bleeding that won't stop is also normal, so don't worry about it.' || Uncontrolled bleeding is not an expected effect",
   "'Put a heat pack on it to help the frozen tissue thaw out faster.' || Heat is not part of the teaching for cryosurgery"],
  "Cryosurgery uses liquid nitrogen to freeze the lesion. Expected effects include redness, swelling and a pale/white scar, and treatment may need repeating.")

q("surg", "A 64-year-old client with a basal cell carcinoma near the eyelid is scheduled for Mohs micrographic surgery and asks why it may take several hours. Which explanation is correct?",
  ["'The lesion is scraped off and the base is burned with heat.' || That is curettage and electrodesiccation",
   "'A dye is injected near the tumor to find the first lymph node.' || That is sentinel lymph node biopsy",
   "'The entire lesion is frozen at once with liquid nitrogen to destroy it.' || That is cryosurgery",
   "*'Thin layers are removed and checked under a microscope until clear.'"],
  "Mohs surgery removes one thin layer at a time and checks it under a microscope, repeating until no cancer cells remain.")

q("surg", "Which pairings of skin cancer surgery and description are correct? " + SATA,
  ["*Curettage and electrodesiccation: scraping the lesion, then destroying remaining tissue with heat",
   "*Wide excision: removing the lesion plus surrounding tissue, sometimes closed with a flap or graft",
   "*Sentinel lymph node biopsy: a tracer or dye finds the first draining node",
   "Mohs surgery: freezing the whole lesion at once || Mohs removes thin layers checked under a microscope",
   "Curettage and electrodesiccation: activating a topical drug with light || That describes photodynamic therapy"],
  "Curettage and electrodesiccation scrapes and burns basal or squamous lesions. Wide excision removes the lesion plus surrounding tissue and may need a flap or skin graft. Sentinel node biopsy uses a tracer or dye. Mohs is layer-by-layer with microscopy.")

q("graft", "A 57-year-old client will have a split-thickness skin graft taken from the thigh after a wide excision. Which statement by the nurse is accurate?",
  ["'The graft includes your entire epidermis and dermis and is stitched in place.' || That describes a full-thickness graft",
   "'The skin will come from a cadaver donor instead of your own body.' || An autograft comes from the client's own healthy skin",
   "*'It is epidermis plus a thin layer of dermis and can be meshed.'",
   "'The donor site will lose all its hair follicles and sweat glands.' || The split-thickness donor site keeps follicles and sweat glands"],
  "A split-thickness graft is epidermis plus superficial dermis and can be meshed to cover a larger area. The donor site keeps follicles and sweat glands; thigh and buttock are common donor areas. A dermatome harvests the thin donor skin.")

q("donor", "On day 2 after a skin graft to the lower leg, a 60-year-old client asks the nurse to take off the bulky dressing so he can see the graft. Which response is best?",
  ["'Sure, we change it every day so we can look closely at the graft.' || Daily removal disrupts graft contact; the pressure dressing stays about 3-5 days",
   "*'It stays on about 3 to 5 days, with the leg kept still and raised.'",
   "'We can take it off, but please walk on it to boost circulation.' || The graft site is immobilized and elevated",
   "'The dressing is only there to absorb weeping drainage from the graft.' || Weeping drainage is a donor site finding; graft dressing maintains pressure"],
  "Graft site care: bulky pressure dressing for about 3-5 days, immobilize and elevate, monitor color, vascularization and adherence, and watch for blood or fluid trapped under the graft that keeps it from adhering.")

q("donor", "The nurse is teaching a client how to care for a split-thickness donor site on the thigh. Which statements should the nurse include? " + SATA,
  ["*'Leave the nonadherent dressing in place; it will lift off as the site heals.'",
   "*'The donor site is often more painful than the graft site, so ask for pain medicine.'",
   "*'Expect wet, weeping drainage for a few days before it dries.'",
   "*'Protect the site from the sun for about a year.'",
   "'Peel the dressing off each day to check for healing.' || The nonadherent dressing stays until it lifts off on its own"],
  "Donor site: wet, weeping drainage for about 3-5 days, then a dry phase; the nonadherent dressing stays until it lifts off as it heals; discoloration is expected; the donor site is often more painful than the graft site; teach sun protection for about a year.")

q("systemic", "A 60-year-old client with metastatic melanoma is starting immunotherapy and asks how it works. Which explanation by the nurse is correct?",
  ["'It freezes the tumor with liquid nitrogen so it can be removed.' || That describes cryosurgery",
   "'It removes the tumor one thin layer at a time under a microscope.' || That describes Mohs surgery",
   "'It is a cream that is activated by blue light on the skin.' || That describes photodynamic therapy",
   "*'It helps your immune system recognize and attack the cancer cells.'"],
  "Immunotherapy helps the body recognize and attack malignant cells and build immune memory. It and targeted therapy are used for advanced or metastatic skin cancer; standard chemotherapy is for cancers that don't respond to other therapies.")

q("promo", "A family is planning a beach vacation. Which sun-protection teaching should the nurse include? " + SATA,
  ["*Apply sunscreen about 30 minutes before going outside",
   "*Reapply sunscreen every 2 hours, and more often when swimming or sweating",
   "*Use a sunscreen with SPF 15-30 and check the expiration date",
   "*Wear a wide-brimmed hat, long sleeves and sunglasses",
   "Plan beach time between 11 a.m. and 3 p.m. || These are peak sun hours to avoid"],
  "Sun protection: avoid peak sun (about 11 a.m. to 3 p.m.), wear protective clothing, hat and sunglasses, avoid tanning booths, apply SPF 15-30 sunscreen about 30 minutes before going out, reapply every 2 hours and more often when swimming or sweating, and check expiration.")

q("promo", "The nurse teaches a 29-year-old client about skin self-examination. Which statement by the client indicates a need for more teaching?",
  ["'I'll check my skin after a shower using a full-length and handheld mirror.' || Correct self-exam technique",
   "'I'll get a professional skin check every year around my birthday.' || Correct; 'check your birthday suit on your birthday'",
   "'I'll learn what my usual moles look like and use ABCDE.' || Correct; know your usual moles",
   "*'I'll do my self-exam in a dimly lit room so the moles stand out.'"],
  "Self-exam is done after a bath or shower in a well-lit room with full-length and handheld mirrors. 'Check your birthday suit on your birthday' means an annual professional exam. Know your usual moles and use ABCDE.")
