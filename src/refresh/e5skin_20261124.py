T = "e5skin"; SET = "20261124"
SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

q("patho", "The nurse explains to a 40-year-old landscaper how ultraviolet exposure leads to skin cancer. Which statement by the client shows understanding?",
  ["'UV only gives me a tan, and the tan protects my skin.' || UV damages DNA; it does more than cause a tan",
   "'UV is a virus that infects the outer layer of my skin.' || UV is not an infection; it damages DNA",
   "*'UV damages DNA and weakens cell immunity, so cells grow out of control.'",
   "'UV thickens my dermis, which is harmless and never leads to cancer.' || UV promotes uncontrolled cell growth, not harmless thickening"],
  "UV exposure damages DNA, suppresses cellular immunity and promotes uncontrolled growth of epidermal cells. Cancer that invades the dermis can reach blood and lymph vessels and metastasize.")

q("uv", "A 50-year-old office worker says she only needs sun protection in the summer because she never burns in winter. Which response by the nurse is best?",
  ["'You're right; UV damage only happens when you get a sunburn.' || UVA causes damage without a burn and is present all year",
   "*'UVA is present all year and goes deep, so protect your skin year-round.'",
   "'Only UVB causes skin cancer, and it is absent during the winter.' || Both UVA and UVB contribute to skin cancer",
   "'Winter sun is mostly UVB, which penetrates the deepest of the two.' || UVA, not UVB, penetrates deeper"],
  "UVB is shorter and causes sunburn; UVA penetrates deeper and is present all year. Both contribute to skin cancer.")

q("risk", "A 24-year-old graduate student tells the clinic nurse, 'Skin cancer is something only old people get.' Which response by the nurse is best?",
  ["'That's true; it rarely shows up before about age 70.' || Skin cancer is increasingly seen in younger adults",
   "'Young adults only get it if they have dark skin and brown eyes.' || Dark skin is not a risk factor; fair skin and light eyes are",
   "'You're correct, so you can wait to start skin checks until later.' || Younger adults also get skin cancer and need monitoring",
   "*'It's increasingly seen in younger adults, so it matters for you too.'"],
  "Skin cancer is very common and increasingly seen in younger adults; don't assume only older clients get it. Risk factors include cumulative UV exposure, tanning beds, immunosuppression, family or personal history, fair skin and severe sunburns.")

q("precan", "The nurse is screening clients at a county fair. Which finding should the nurse recognize as a precancerous lesion?",
  ["Shiny, pearly pink bump with tiny vessels on the nose || This describes basal cell carcinoma",
   "*Rough, scaly, red-brown patches on a farmer's scalp",
   "Red, thick, scaly lesion that ulcerates on the lip || This describes squamous cell carcinoma",
   "Mole with mixed colors and an uneven border on the back || These are ABCDE warning signs of melanoma"],
  "Actinic (solar) keratosis appears as rough, scaly, red-brown patches on sun-exposed skin such as the ears and scalp. It is precancerous and can progress to squamous cell carcinoma.")

q("precan", "A 19-year-old college student whose father has dysplastic nevi syndrome asks the nurse about the condition. Which statements by the nurse are accurate? " + SATA,
  ["*'It involves many atypical moles.'",
   "'It is caused by a bacterial infection of the moles.' || It is not an infection; it is many atypical moles",
   "*'It often runs in families.'",
   "'Having more moles lowers your concern for skin cancer.' || More moles raise concern",
   "*'Watch for a mole that looks different from your others.'"],
  "Dysplastic nevi syndrome is many atypical moles, often familial; more moles raise concern. Teach the ugly duckling sign: a mole that looks different from the person's other moles.")

q("bcc", "A 59-year-old construction worker has a spot on his cheek that has bled and scabbed for months without healing. It has a pearly edge and a central dip. Which action by the nurse is the priority?",
  ["Reassure him that this is a harmless pimple that will clear || A nonhealing pearly lesion suggests basal cell carcinoma",
   "Advise him to wait six months and then recheck the spot || The lesion needs evaluation now, not delayed follow-up",
   "*Refer him for dermatologic evaluation and a biopsy",
   "Tell him it will spread fast and he needs chemotherapy || BCC is least aggressive; chemotherapy is for nonresponsive cancers"],
  "Basal cell carcinoma is a smooth, raised, shiny/waxy pink lesion with visible small vessels that may have a central depression and is often a 'sore that doesn't heal.' Refer for dermatologic evaluation and biopsy.")

q("bcc", "The nurse is reviewing basal cell carcinoma with a group of nursing students. Which features are characteristic of basal cell carcinoma? " + SATA,
  ["*It is the most common type of skin cancer",
   "It is the skin cancer most likely to metastasize || Melanoma is most likely to spread; BCC metastasis is rare",
   "*It is often described as a sore that doesn't heal",
   "*It looks shiny or waxy pink with small visible vessels",
   "It is a red, thick, scaly lesion that ulcerates || This describes squamous cell carcinoma"],
  "BCC is the most common and least aggressive skin cancer; metastasis is rare. It appears as a smooth, raised, shiny/waxy pink lesion with visible small vessels, may have a central depression and is often a sore that doesn't heal.")

q("scc", "A 74-year-old client had an untreated actinic keratosis on the ear. That area is now thick, red and scaly and has started to ulcerate. Which interpretation by the nurse is best?",
  ["*It may have progressed to squamous cell carcinoma",
   "It is a basal cell carcinoma, which rarely spreads || BCC is shiny, waxy and pink, not thick and ulcerating",
   "This is the expected course of actinic keratosis || Change to an ulcerating lesion is not expected; it suggests SCC",
   "It is an ugly duckling mole from dysplastic nevi || The ugly duckling sign refers to a mole unlike the others"],
  "SCC can arise from untreated actinic keratosis. It is a red, thick, scaly lesion that may ulcerate, hurt and bleed, and is common on the lips, ears and nose.")

q("scc", "A client newly diagnosed with squamous cell carcinoma says his brother had basal cell carcinoma. Which statement by the client shows correct understanding?",
  ["'Mine is the less aggressive of the two types.' || SCC is more aggressive than BCC",
   "'They are the same cancer with different names.' || SCC and BCC differ in appearance and behavior",
   "'Squamous cell never invades deeper tissue.' || SCC can invade tissue and metastasize",
   "*'Mine is more aggressive and more likely to spread.'"],
  "SCC is more aggressive and more likely to metastasize than BCC. It can arise from untreated actinic keratosis and is common on the lips, ears and nose.")

q("mel", "A 28-year-old client was just diagnosed with malignant melanoma. Which statement by the nurse reflects the priority teaching?",
  ["'Melanoma is the least aggressive skin cancer, so treatment can wait.' || Melanoma is the most dangerous skin cancer",
   "*'Early detection and treatment matter because melanoma spreads easily.'",
   "'Melanoma rarely metastasizes, much like basal cell carcinoma does.' || Melanoma is highly metastatic",
   "'From now on, you only need to check skin that gets sun exposure.' || Melanoma can occur anywhere, so check all skin"],
  "Malignant melanoma is the most dangerous and highly metastatic skin cancer; early detection and treatment are critical. It can occur anywhere, so the entire skin surface is assessed.")

q("mel", "The nurse is preparing a teaching sheet on malignant melanoma. Which statements should the nurse include? " + SATA,
  ["*It is the most dangerous type of skin cancer",
   "It only develops on skin exposed to the sun || Melanoma can occur anywhere, including mucosal surfaces",
   "*It can occur in the eyes",
   "*Sentinel lymph node biopsy checks for spread",
   "It is the least likely type to metastasize || Melanoma is the most likely to metastasize"],
  "Melanoma is the most dangerous and highly metastatic skin cancer. It can occur anywhere, including the eyes and mucosal surfaces. Sentinel lymph node biopsy uses a tracer or dye near the tumor to find the first draining node.")

q("abcde", "A 45-year-old client reports that a mole on his forearm now has notched, blurry edges. Which ABCDE letter does this finding represent?",
  ["A — Asymmetry || Asymmetry means one half does not match the other",
   "C — Color variation || Color variation means mixed shades",
   "*B — Border irregularity",
   "D — Diameter || Diameter refers to size over 6 mm"],
  "ABCDE: Asymmetry, Border irregularity, Color variation, Diameter over 6 mm (about a pencil eraser), Evolving (changing size, shape, color or appearance).")

q("abcde", "During a home visit, the nurse notes a 9 mm mole with several shades of brown and black on a 63-year-old client's calf. The client says, 'It's been there for years.' Which action by the nurse is best?",
  ["Reassure her that a mole she has had for years is not a concern || Its size and color variation are ABCDE warning signs",
   "Remove the mole with cryotherapy during the home visit || The lesion needs evaluation and biopsy, not bedside removal",
   "Tell her to recheck it in a year and call if it gets bigger || Waiting delays diagnosis of a concerning lesion",
   "*Recommend dermatologic evaluation, since biopsy shows its type"],
  "A diameter over 6 mm (larger than a pencil eraser) and color variation are ABCDE warning signs. Refer for dermatologic evaluation; biopsy determines the lesion type.")

q("biopsy", "A 36-year-old client asks why the provider plans to remove an entire suspicious mole plus some healthy skin around it. Which response by the nurse is accurate?",
  ["'A shave biopsy is planned, and it reaches the deepest tissue.' || A shave biopsy removes only superficial tissue",
   "*'Excisional biopsy is preferred for suspected melanoma if size permits.'",
   "'A punch biopsy removes just part of a large lesion like this.' || Punch is a cylindrical sample; incisional removes part",
   "'The biopsy is mainly done to improve how the area looks.' || Biopsy is done to determine the lesion type"],
  "Excisional biopsy removes the whole lesion plus a margin of healthy tissue and is preferred for suspected melanoma when size permits. Shave is superficial, punch is a cylindrical sample to a set depth, and incisional removes part of a larger lesion.")

q("local", "Which pairings of local skin cancer treatment and description are correct? " + SATA,
  ["*Cryosurgery: liquid nitrogen freezes the lesion",
   "*Photodynamic therapy: a light-sensitizing agent activated with blue light",
   "*Topical fluorouracil: treats actinic keratosis or superficial basal lesions",
   "Photodynamic therapy: extra sun exposure afterward speeds healing || Avoid sunlight for about 48 hours after",
   "*Laser or radiation: for hard-to-remove areas such as the eyelids or nose"],
  "Cryosurgery freezes the lesion with liquid nitrogen. Photodynamic therapy uses a light-sensitizing agent activated with blue light; avoid sunlight for about 48 hours. Topical fluorouracil or retinoids treat actinic keratosis or superficial basal lesions. Laser or radiation spare delicate structures around the eyelids, nose or facial nerves.")

q("surg", "A 69-year-old client with a small squamous cell lesion on the hand is scheduled for curettage and electrodesiccation. Which description of the procedure should the nurse give?",
  ["'Thin layers are removed and checked under a microscope.' || That is Mohs micrographic surgery",
   "'A dye is injected to locate the first draining lymph node.' || That is sentinel lymph node biopsy",
   "*'The lesion is scraped away and remaining tissue is destroyed with heat.'",
   "'The whole lesion is frozen at once using liquid nitrogen.' || That is cryosurgery"],
  "Curettage and electrodesiccation scrapes the lesion and destroys remaining tissue with heat. It is used for basal or squamous cell lesions.")

q("surg", "A 61-year-old client is having a wide excision of a large lesion on the scalp and asks why the consent form mentions a skin graft. Which response by the nurse is best?",
  ["*'Removing the lesion and the tissue around it may need a flap or graft to close.'",
   "'The wound always closes by itself, so the graft is only a formality.' || A large wide excision may need a flap or graft",
   "'The graft is placed to help locate the first draining lymph node.' || A tracer or dye, not a graft, finds the sentinel node",
   "'A graft is needed because the scalp lesion will be frozen first.' || Freezing is cryosurgery, not wide excision"],
  "Wide excision removes the lesion plus surrounding tissue, and a flap or skin graft may be needed to close the wound.")

q("graft", "Which statement correctly distinguishes a full-thickness skin graft from a split-thickness skin graft?",
  ["Full-thickness grafts are meshed to stretch over a larger area || Meshing is done with split-thickness grafts",
   "Split-thickness grafts include the entire epidermis and dermis || Split-thickness is epidermis plus superficial dermis",
   "Split-thickness skin comes only from a cadaver donor || An autograft is taken from the client's own healthy skin",
   "*Full-thickness grafts include all of the dermis and are sutured"],
  "A full-thickness graft includes the entire epidermis and dermis and is stitched into position. A split-thickness graft is epidermis plus superficial dermis, harvested with a dermatome, and can be meshed; its donor site keeps follicles and sweat glands.")

q("donor", "The nurse is caring for a 44-year-old client 1 day after a split-thickness skin graft to the arm, with the donor site on the thigh. Which finding requires follow-up?",
  ["Wet, weeping drainage from the thigh donor site || Weeping drainage for about 3-5 days is expected at the donor site",
   "*Blood collecting under one edge of the arm graft",
   "Discoloration of the skin at the thigh donor site || Discoloration is an expected donor site finding",
   "Client reports the donor site hurts more than the graft || The donor site is often more painful; treat the pain"],
  "Blood or fluid trapped under a graft keeps it from adhering to the wound bed and must be watched for and reported. Weeping drainage, discoloration and greater pain at the donor site are expected.")

q("donor", "Which interventions are part of care for the GRAFT site rather than the donor site? " + SATA,
  ["*Keep a bulky pressure dressing on for about 3-5 days",
   "Leave a nonadherent dressing until it lifts off || This is donor site care",
   "*Immobilize and elevate the grafted area",
   "Expect wet, weeping drainage, then a dry phase || This is a donor site finding",
   "*Monitor color, vascularization and adherence"],
  "Graft site: bulky pressure dressing for about 3-5 days, immobilize and elevate, monitor color, vascularization and adherence, and watch for trapped blood or fluid; vascularization may begin within about 36 hours. Donor site: nonadherent dressing until it lifts off, weeping drainage then a dry phase, discoloration, sun protection.")

q("systemic", "A 56-year-old client with metastatic melanoma will start targeted therapy and asks how it differs from other treatments. Which explanation by the nurse is correct?",
  ["'It helps your immune system build memory to attack the cancer.' || That describes immunotherapy",
   "*'It blocks the signals the tumor uses to grow or form blood vessels.'",
   "'It freezes the tumor with liquid nitrogen so it can be removed.' || That describes cryosurgery",
   "'It removes the tumor one layer at a time under a microscope.' || That describes Mohs surgery"],
  "Targeted therapy blocks growth signals and/or tumor blood-vessel formation. Immunotherapy helps the body recognize and attack malignant cells and build immune memory. Both are used for advanced or metastatic disease.")

q("promo", "A 17-year-old client plans to use a tanning booth several times before a school dance. Which teaching by the nurse is most important?",
  ["'Booths are safe as long as you only go in the winter months.' || Tanning beds are a major risk factor in any season",
   "'A tan protects you, so you won't need sunscreen afterward.' || A tan does not replace sunscreen",
   "*'Avoid tanning booths; they are a major risk for skin cancer.'",
   "'Booths are fine if you wear a sunscreen with SPF 4 inside.' || Tanning booths should be avoided; SPF 15-30 is advised"],
  "Avoiding tanning booths is part of sun-protection teaching; tanning beds are a major risk factor for skin cancer. No sunscreen substitute makes them safe.")

q("promo", "The nurse teaches sunscreen use to a 35-year-old summer camp counselor. Which statement by the client shows correct understanding?",
  ["'One coat in the morning lasts all day, even when I swim.' || Reapply every 2 hours and more often when swimming",
   "'I can keep using the same bottle for years past its date.' || Sunscreen has a shelf life; check the expiration",
   "'Only SPF 100 works, so anything lower is a waste of money.' || SPF 15-30 is recommended",
   "*'I'll apply it 30 minutes before going out and reapply every 2 hours.'"],
  "Apply SPF 15-30 sunscreen about 30 minutes before going out, reapply every 2 hours and more often when swimming or sweating, and check the expiration date.")
