T = "e5skin"; SET = "20261125"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("patho", "A nursing student explains how skin cancer develops during a clinical huddle. Which statement by the student needs correction?",
  ["'Melanocytes in the epidermis are the cells that make melanin.' || Accurate; melanocytes make melanin",
   "'UV exposure damages DNA and suppresses cellular immunity.' || Accurate; this is how UV promotes cancer",
   "*'Skin cancer begins as abnormal growth of cells in the dermis.'",
   "'Basal cells are found in the lower layer of the epidermis.' || Accurate; basal cells are in the lower epidermis"],
  "Skin cancer is abnormal growth of epidermal cells (squamous cells, basal cells and melanocytes); once it invades the dermis it can reach blood and lymph vessels.")

q("uv", "A 33-year-old who skis every winter asks the nurse about ultraviolet light. Which statements by the nurse are accurate? " + SATA,
  ["*'UVA is present all year, including winter.'",
   "'Only UVB contributes to skin cancer.' || Both UVA and UVB contribute to skin cancer",
   "*'UVB is the shorter wave that causes sunburn.'",
   "'Tanning beds mainly use UVB rays.' || Tanning beds mainly use UVA",
   "*'UVA penetrates deeper into the skin than UVB.'"],
  "UVB is shorter and causes sunburn; UVA penetrates deeper and is present all year. Both contribute to skin cancer.")

q("risk", "The nurse reviews intake forms at a skin screening event. Which client has the most risk factors for skin cancer?",
  ["A 36-year-old office worker with dark skin and brown eyes || Dark skin and brown eyes are not listed risk factors",
   "*A 38-year-old with albinism who spends weekends hiking outdoors",
   "A 42-year-old with lots of melanin who rarely goes outside || Melanin-rich skin and little sun do not add risk",
   "A 30-year-old with brown eyes who has never had a sunburn || No listed risk factors are present"],
  "Additional risk factors include albinism and outdoor activities, along with fair skin, light eyes, severe sunburns and many or atypical moles.")

q("precan", "Which statement correctly compares actinic keratosis with squamous cell carcinoma?",
  ["Actinic keratosis is more aggressive than squamous cell carcinoma || AK is precancerous; SCC is the cancer",
   "Both appear as shiny, waxy pink bumps with tiny vessels || That describes basal cell carcinoma",
   "*Actinic keratosis is a precancerous patch that can progress to SCC",
   "Squamous cell carcinoma progresses into actinic keratosis || The progression goes from AK to SCC"],
  "Actinic (solar) keratosis is rough, scaly, red-brown patches on sun-exposed skin; it is precancerous and can progress to squamous cell carcinoma.")

q("precan", "A 27-year-old with dysplastic nevi syndrome does a monthly skin self-exam. Which finding should she report?",
  ["A freckle on her arm that fades every winter || Fading freckles are not the ugly duckling sign",
   "A healed biopsy scar on her upper back || A biopsy scar is not a mole warning sign",
   "Several moles on her legs that all look alike || Moles that match each other are not the ugly duckling",
   "*A mole on her shoulder that looks unlike her other moles"],
  "Dysplastic nevi syndrome is many atypical moles, often familial. Teach the ugly duckling sign: a mole that looks different from the person's other moles.")

q("bcc", "The nurse teaches a 70-year-old client newly diagnosed with basal cell carcinoma. Which statement by the client indicates a need for more teaching?",
  ["'This is the most common type of skin cancer.' || Accurate; BCC is the most common",
   "*'Since it rarely spreads, I can skip the treatment.'",
   "'It can look like a sore that won't heal.' || Accurate; BCC is often a sore that doesn't heal",
   "'It is the least aggressive of the skin cancers.' || Accurate; BCC is least aggressive"],
  "BCC is the most common and least aggressive skin cancer and metastasis is rare, but it still needs dermatologic evaluation, biopsy and treatment.")

q("bcc", "A 65-year-old has a smooth, waxy pink lesion with a central depression on the temple. Which findings in the record support basal cell carcinoma? " + SATA,
  ["*Small visible vessels on the surface of the lesion",
   "*The client says the sore has not healed for months",
   "Rough, scaly, red-brown patches on the scalp || This describes actinic keratosis",
   "*The lesion is raised and has a shiny, pearly look",
   "Mixed colors with an irregular, notched border || These are ABCDE signs of melanoma"],
  "Basal cell carcinoma is a smooth, raised, shiny/waxy pink lesion with visible small vessels; it may have a central depression and is often a sore that doesn't heal.")

q("scc", "The nurse compares two lesions on a 72-year-old client. Which findings point to squamous cell carcinoma rather than basal cell carcinoma? " + SATA,
  ["*The lesion is red, thick and scaly",
   "Shiny, pearly surface with tiny visible vessels || This points to basal cell carcinoma",
   "*The lesion has ulcerated and bleeds easily",
   "*The client says the lesion is painful",
   "It is the least likely of the two to metastasize || BCC is less likely to spread; SCC is more aggressive"],
  "Squamous cell carcinoma is a red, thick, scaly lesion that may ulcerate, hurt and bleed. It is more aggressive and more likely to metastasize than BCC.")

q("scc", "The nurse reviews four clients' skin histories. Which client is at greatest risk for developing squamous cell carcinoma?",
  ["A client with one round, 3 mm, evenly tan mole || A small, symmetric, one-color mole is not a warning sign",
   "*A client with an untreated actinic keratosis on the ear",
   "A client with a pale scar after cryosurgery || A pale scar is an expected effect of cryosurgery",
   "A client with dark skin, lots of melanin and brown eyes || These are not listed risk factors"],
  "SCC can arise from untreated actinic keratosis and is common on the lips, ears and nose.")

q("mel", "The dermatology nurse reviews four new biopsy results. Which client's diagnosis carries the greatest risk of metastasis?",
  ["Basal cell carcinoma on the forehead || BCC is the least aggressive; metastasis is rare",
   "Actinic keratosis on the scalp || AK is precancerous, not a cancer that spreads",
   "Squamous cell carcinoma on the lip || SCC is more aggressive than BCC, but melanoma spreads most",
   "*Malignant melanoma on the upper back"],
  "Malignant melanoma is the most dangerous and highly metastatic skin cancer; early detection and treatment are critical.")

q("mel", "Which statements about the care of a client with malignant melanoma are accurate? " + SATA,
  ["*The entire skin surface, including mucosal areas, is assessed",
   "Melanoma rarely spreads, so lymph nodes are not checked || Melanoma is the most likely to metastasize",
   "*A tracer or dye near the tumor finds the first draining lymph node",
   "Cryosurgery is the main treatment for metastatic melanoma || Advanced disease uses immunotherapy or targeted therapy",
   "*Immunotherapy may be used if the melanoma has metastasized"],
  "Melanoma can occur anywhere, including the eyes and mucosal surfaces. Sentinel lymph node biopsy checks for spread, and immunotherapy and targeted therapy are used for advanced or metastatic disease.")

q("abcde", "A client asks the nurse how to judge whether a mole's size is a warning sign. Which response is accurate?",
  ["'Any mole larger than 1 mm should be seen right away.' || The cutoff is over 6 mm",
   "'Size doesn't matter; only the color of the mole counts.' || Diameter is one of the ABCDE signs",
   "*'A mole over 6 mm, about a pencil eraser, is a warning sign.'",
   "'Only moles larger than a quarter are any concern at all.' || The cutoff is over 6 mm, about a pencil eraser"],
  "D in ABCDE is diameter over 6 mm, about the size of a pencil eraser.")

q("abcde", "During a telehealth visit, clients describe their moles. Which reports match ABCDE warning signs? " + SATA,
  ["*'It used to be tan, and now it's tan, black and red.'",
   "'It's the same small, round tan spot it has always been.' || A stable, round, one-color mole is not a warning sign",
   "*'The edges used to be smooth, but now they look jagged.'",
   "*'It has changed shape over the last few months.'",
   "'It's 3 mm across and both halves match.' || Small and symmetric are not warning signs"],
  "ABCDE: Asymmetry, Border irregularity, Color variation, Diameter over 6 mm, Evolving (changing size, shape, color or appearance).")

q("biopsy", "A 48-year-old is scheduled for a punch biopsy of a skin lesion. Which description should the nurse give?",
  ["'The whole lesion is removed with a margin of healthy skin.' || That describes an excisional biopsy",
   "*'A cylinder-shaped sample is taken down to a set depth.'",
   "'Only the top, superficial layer of the lesion is removed.' || That describes a shave biopsy",
   "'Just one part of a large lesion is cut out for testing.' || That describes an incisional biopsy"],
  "Punch biopsy takes a cylindrical sample to a set depth. Shave removes superficial tissue, incisional removes part of a larger lesion, and excisional removes the whole lesion plus a margin.")

q("local", "A 58-year-old had photodynamic therapy for a skin lesion this morning and plans to spend tomorrow afternoon gardening. Which response by the nurse is best?",
  ["'Sun on the area will help activate the medicine and speed healing.' || Sun exposure should be avoided after photodynamic therapy",
   "'Gardening is fine as long as you put a heat pack on the area first.' || Heat packs are not part of photodynamic therapy teaching",
   "'There are no restrictions after this treatment, so enjoy the garden.' || The key teaching is avoiding sunlight for about 48 hours",
   "*'Stay out of the sunlight for about 48 hours after this treatment.'"],
  "Photodynamic therapy uses a light-sensitizing agent activated with blue light; avoid sunlight for about 48 hours. Redness, pain and swelling can occur.")

q("surg", "Which statement correctly compares Mohs micrographic surgery with wide excision?",
  ["*Mohs removes thin layers checked by microscope; wide excision takes the lesion and surrounding tissue",
   "Mohs freezes the lesion at once; wide excision scrapes and burns the base || Freezing is cryosurgery; scrape and burn is curettage",
   "Mohs finds the first lymph node; wide excision uses a light-activated drug || Those are sentinel node biopsy and photodynamic therapy",
   "Mohs always needs a skin graft; wide excision never needs one || Wide excision may need a flap or graft to close"],
  "Mohs removes one thin layer at a time and checks it under a microscope until no cancer cells remain. Wide excision removes the lesion plus surrounding tissue and may need a flap or skin graft.")

q("surg", "A 73-year-old asks which kinds of skin lesions curettage and electrodesiccation is used for. Which response by the nurse is accurate?",
  ["'It is used only for melanoma that has spread to the lymph nodes.' || Curettage is used for basal or squamous lesions",
   "'It is used to collect healthy skin for a graft on another area.' || A dermatome harvests graft skin",
   "*'It is used for basal cell or squamous cell skin lesions.'",
   "'It is used to find the first lymph node that drains the tumor.' || That is sentinel lymph node biopsy"],
  "Curettage and electrodesiccation scrapes the lesion and destroys remaining tissue with heat; it is used for basal or squamous cell lesions.")

q("graft", "A 54-year-old scheduled for an autograft asks where the skin will come from and how it is taken. Which response by the nurse is accurate?",
  ["'A scalpel removes the full dermis from a cadaver donor.' || An autograft uses the client's own skin",
   "'The skin comes from another person and is meshed to fit.' || Skin from another person is not an autograft",
   "'The skin is taken from your scalp only with a punch tool.' || Thigh and buttock are common donor areas",
   "*'A dermatome takes thin skin from your own thigh or buttock.'"],
  "An autograft is skin taken from the client's own healthy skin. A dermatome harvests thin donor skin; thigh and buttock are common donor areas.")

q("donor", "On day 3 after a split-thickness graft, the nurse assesses the client's thigh donor site. Which findings are expected? " + SATA,
  ["*Wet, weeping drainage under the dressing",
   "*Discoloration of the skin at the site",
   "Blood trapped under the edge of the graft || This is a graft site concern that keeps it from adhering",
   "*The client rates donor pain higher than graft pain",
   "A bulky pressure dressing pressed to a wound bed || A bulky pressure dressing is graft site care"],
  "Donor site: wet, weeping drainage for about 3-5 days, then a dry phase; discoloration; it is often more painful than the graft site; the nonadherent dressing stays until it lifts off.")

q("donor", "A 46-year-old had a skin graft to the forearm 12 hours ago. Which nursing action is the priority for the graft site?",
  ["Remove the dressing each shift to look at the graft || The bulky pressure dressing stays about 3-5 days",
   "*Keep the arm immobilized and elevated under the dressing",
   "Encourage active exercise of the grafted arm hourly || The graft site is immobilized",
   "Leave a nonadherent dressing until it lifts off alone || That is donor site care"],
  "Graft site care: bulky pressure dressing for about 3-5 days, immobilize and elevate, monitor color, vascularization and adherence, and watch for trapped blood or fluid.")

q("systemic", "A 63-year-old with advanced skin cancer asks when standard chemotherapy would be used. Which response by the nurse is accurate?",
  ["'It is the first treatment for every basal cell carcinoma.' || BCC is treated locally; it is least aggressive",
   "'It is used to treat each actinic keratosis on the skin.' || AK is treated with topical drugs or other local methods",
   "*'It is for cancers that don't respond to other therapies.'",
   "'It is given before every biopsy to shrink the lesion.' || Biopsy determines lesion type; chemotherapy is not given first"],
  "Standard chemotherapy is discussed for cancers that don't respond to other therapies; immunotherapy and targeted therapy are used for advanced or metastatic disease.")

q("promo", "A parent is scheduling a child's summer soccer practices. Which practice time best fits sun-protection teaching?",
  ["Noon, when the sun is high || This is within peak sun hours",
   "*8 a.m., before peak sun hours",
   "1 p.m., right after lunch || This is within peak sun hours",
   "2:30 p.m., after the noon heat || This is still within peak sun hours"],
  "Avoid peak sun, about 11 a.m. to 3 p.m.; wear protective clothing and apply SPF 15-30 sunscreen about 30 minutes before going out.")

q("promo", "The nurse teaches skin cancer prevention to a 40-year-old mail carrier. Which statements by the client show understanding? " + SATA,
  ["*'I'll reapply sunscreen more often on days I sweat a lot.'",
   "'I'll put sunscreen on right as I walk out the door.' || Apply it about 30 minutes before going out",
   "*'I'll check the expiration date on my sunscreen.'",
   "'SPF 4 is plenty once I have a base tan.' || SPF 15-30 is recommended; a tan doesn't replace sunscreen",
   "*'I'll get a professional skin check every year.'"],
  "Reapply sunscreen every 2 hours and more often when swimming or sweating, check expiration, use SPF 15-30 about 30 minutes before going out, and 'check your birthday suit on your birthday.'")
