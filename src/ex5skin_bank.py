# Week 13.2 Cellular Dysregulation: Skin Cancer — lesson plan, lecture transcript (via notes), notes.
EXAM = "e5"
T = "e5skin"
CONCEPTS = {
 "patho":"Epidermis, melanocytes & UV damage",
 "uv":"UVA vs UVB",
 "risk":"Risk factors",
 "precan":"Actinic keratosis & atypical moles",
 "bcc":"Basal cell carcinoma",
 "scc":"Squamous cell carcinoma",
 "mel":"Malignant melanoma",
 "abcde":"ABCDE assessment",
 "biopsy":"Biopsy types",
 "local":"Cryosurgery, laser, photodynamic & topical treatment",
 "surg":"Curettage, Mohs, wide excision & sentinel node",
 "graft":"Split- vs full-thickness grafts",
 "donor":"Donor site vs graft site care",
 "systemic":"Immunotherapy & targeted therapy",
 "promo":"Sun protection & self-exam",
}
HI = ["bcc","scc","mel","abcde","donor","precan","promo","surg"]

SATA = "Select all that apply."
Q = []
def q(c, stem, opts, r): Q.append((c, stem, opts, r))

# ---------- patho ----------
q("patho","Which cells live in the epidermis? "+SATA,
 ["*Squamous cells (outer layer)","*Basal cells (lower epidermis)","*Melanocytes (make melanin)","Osteoblasts || Bone cells."],
 "Skin cancer is abnormal growth of epidermal cells.")
q("patho","How does UV exposure cause skin cancer?",
 ["*It damages DNA, suppresses cellular immunity and promotes uncontrolled growth","It only causes a tan || It damages DNA.","It thickens the dermis harmlessly || Not the mechanism.","It infects the skin with a virus || Not the mechanism."],
 "Cancer invading the dermis can reach blood and lymph vessels and metastasize.")
q("patho","Why can skin cancer spread once it invades the dermis?",
 ["*The dermis contains blood and lymph vessels","The dermis has no cells || It does.","The epidermis has the vessels || The dermis does.","It can't spread || It can metastasize."],
 "Melanoma is the most likely to metastasize.")

# ---------- UV ----------
q("uv","Which statement correctly compares UVA and UVB?",
 ["*UVB is shorter and causes sunburn; UVA penetrates deeper and is present all year","UVA causes sunburn; UVB penetrates deeper || Reversed.","Only UVB causes skin cancer || Both do.","Tanning beds use mainly UVB || Mainly UVA."],
 "Both contribute to skin cancer.")
q("uv","A client says tanning beds are safer than the sun. Best response?",
 ["*'Tanning beds mainly use UVA, which penetrates deeply and causes skin cancer too.'","'Yes, they're safe.' || They raise cancer risk.","'Only if you use them in winter.' || Still harmful.","'They only cause freckles.' || They cause cancer."],
 "Tanning beds are a major risk factor.")

# ---------- risk ----------
q("risk","Which are MAJOR risk factors for skin cancer? "+SATA,
 ["*Cumulative sun or UV exposure","*Tanning beds","*Immunosuppression, such as HIV or transplant medications","*Personal or family history of skin cancer","Dark skin with lots of melanin || More melanin is protective."],
 "Also chemical exposure and smoking.")
q("risk","Which clients have additional risk for skin cancer? "+SATA,
 ["*Fair, freckled skin with red or blond hair","*Blue or green eyes","*History of severe sunburn","*Many or atypical moles","Brown eyes and dark skin || Lower risk."],
 "Also albinism and outdoor activities.")
q("risk","What did the professor stress about the age of clients with skin cancer?",
 ["*It's increasingly seen in younger adults; don't assume only older clients get it","It only affects people over 70 || Not true.","Children can't get it || Not the point.","It never affects young adults || It does."],
 "Skin cancer is very common.")

# ---------- precancerous ----------
q("precan","A client has rough, scaly, red-brown patches on the ears and scalp. What is this, and why does it matter?",
 ["*Actinic keratosis; it can progress to squamous cell carcinoma","Basal cell carcinoma; it metastasizes widely || Not this lesion.","Melanoma; it's the most dangerous || Not this lesion.","A normal age spot; no concern || It's precancerous."],
 "Actinic (solar) keratosis appears on sun-exposed skin.")
q("precan","What is the 'ugly duckling' sign?",
 ["*A mole that looks different from the person's other moles","A mole that's very small || Not the sign.","A freckle that fades in winter || Not the sign.","A scar after biopsy || Not the sign."],
 "It's taught for dysplastic nevi syndrome (many atypical moles, often familial).")
q("precan","Which statement about dysplastic nevi syndrome is correct?",
 ["*Many atypical moles, often familial; more moles raise concern","It's a single harmless mole || Many moles.","It's a bacterial infection || Not infectious.","It never needs monitoring || Needs monitoring."],
 "Teach the ugly duckling sign.")

# ---------- BCC ----------
q("bcc","Which lesion is typical of basal cell carcinoma?",
 ["*Smooth, raised, shiny/waxy pink lesion with visible small vessels","Red, thick, scaly lesion that bleeds || SCC.","Irregular lesion with mixed colors || Melanoma.","Rough, scaly patches that are precancerous || Actinic keratosis."],
 "It may have a central depression and is often a 'sore that doesn't heal.'")
q("bcc","Which statement about basal cell carcinoma is correct?",
 ["*It's the most common and least aggressive skin cancer; metastasis is rare","It's the most dangerous || That's melanoma.","It spreads quickly through lymph || Rare metastasis.","It only appears on the feet || Usually face, forehead and ears."],
 "BCC = pearly/waxy + nonhealing sore + least aggressive.")
q("bcc","A client says a sore on his forehead won't heal and has a waxy edge. What should the nurse suspect?",
 ["*Basal cell carcinoma","Actinic keratosis || Scaly patch.","Shingles || Vesicles in a dermatome.","A normal mole || Not with these findings."],
 "Refer for dermatologic evaluation and biopsy.")

# ---------- SCC ----------
q("scc","Which lesion is typical of squamous cell carcinoma?",
 ["*Red, thick, scaly lesion that may ulcerate, hurt and bleed","Shiny, waxy, pink bump || BCC.","Irregular, multicolored mole || Melanoma.","Flat freckle || Not cancer."],
 "Common on the lips, ears and nose.")
q("scc","How does SCC compare with BCC?",
 ["*SCC is more aggressive and more likely to metastasize","SCC is less aggressive || More aggressive.","They're identical || Different lesions.","SCC never invades tissue || It invades nearby tissue."],
 "SCC can arise from untreated actinic keratosis.")

# ---------- melanoma ----------
q("mel","Which skin cancer is the most dangerous and highly metastatic?",
 ["*Malignant melanoma","Basal cell carcinoma || Least aggressive.","Squamous cell carcinoma || More aggressive than BCC, but less than melanoma.","Actinic keratosis || Precancerous."],
 "Early detection and treatment are critical.")
q("mel","Where can melanoma occur?",
 ["*Anywhere, including the eyes and mucosal surfaces, not just sun-exposed skin","Only on sun-exposed skin || Can be anywhere.","Only on the scalp || Anywhere.","Only on the palms || Anywhere."],
 "Assess the entire skin surface.")
q("mel","Which procedure checks whether melanoma has spread to the lymph nodes?",
 ["*Sentinel lymph node biopsy","Mohs surgery || Removes skin cancer layer by layer.","Cryosurgery || Freezes lesions.","Photodynamic therapy || Treats broad superficial areas."],
 "A tracer or dye near the tumor finds the first draining node.")

# ---------- ABCDE ----------
q("abcde","What does each letter of ABCDE stand for? "+SATA,
 ["*A — Asymmetry","*B — Border irregularity","*C — Color variation","*D — Diameter over 6 mm","*E — Evolving","D — Darkness || D is diameter."],
 "Six millimeters is about the size of a pencil eraser.")
q("abcde","A mole has been getting larger and changing color over 3 months. Which ABCDE letter does this describe?",
 ["*E — Evolving","A — Asymmetry || One half differs.","B — Border || Edges.","D — Diameter || Size over 6 mm only."],
 "Evolving = changing size, shape, color or appearance.")
q("abcde","What is the nurse's priority after finding a new, changing lesion?",
 ["*Refer it for dermatologic evaluation; biopsy determines the type","Reassure the client that moles are normal || A changing lesion needs evaluation.","Remove it with cryotherapy at the bedside || Not the nurse's role.","Wait a year and recheck || Delays diagnosis."],
 "Assess the whole skin, including the ugly duckling.")

# ---------- biopsy ----------
q("biopsy","Which biopsy removes the whole lesion plus a margin of healthy tissue and is preferred for suspected melanoma?",
 ["*Excisional","Shave || Superficial only.","Punch || A cylindrical sample.","Incisional || Only part of a larger lesion."],
 "The professor emphasized excisional biopsy when size permits.")
q("biopsy","Match each biopsy type. "+SATA,
 ["*Shave — removes superficial tissue","*Punch — cylindrical sample to a set depth","*Incisional — removes part of a larger lesion","Excisional — removes only the surface || Excisional removes the whole lesion plus a margin."],
 "Biopsy determines lesion type.")

# ---------- local treatment ----------
q("local","After photodynamic therapy, what is the key teaching?",
 ["*Avoid sunlight for about 48 hours","Get extra sun to activate healing || Avoid sun.","Apply heat packs || Not the teaching.","No restrictions || Sun avoidance is needed."],
 "A light-sensitizing agent is activated with blue light; redness, pain and swelling can occur.")
q("local","A client using topical fluorouracil says the area looks worse. Best response?",
 ["*'It's expected to look irritated or crusted before it heals.'","'Stop it; you're allergic.' || Expected reaction.","'That means the cancer spread.' || Not the meaning.","'Apply it twice as often.' || Don't change the dose."],
 "Topical fluorouracil or retinoids treat actinic keratosis or superficial basal lesions.")
q("local","Which effects are expected after cryosurgery? "+SATA,
 ["*Redness and swelling","*A pale/white scar","*The treatment may need repeating","Bleeding that won't stop || Not expected."],
 "Liquid nitrogen freezes the lesion.")
q("local","When are laser or radiation used for skin cancer?",
 ["*For lesions in hard-to-remove areas, such as around the eyelids, nose or facial nerves","For every mole || Not the use.","Only for melanoma spread to the brain || Not the lecture use.","To harvest graft skin || That's a dermatome."],
 "These spare delicate structures.")

# ---------- surgery ----------
q("surg","How is Mohs micrographic surgery done?",
 ["*One thin layer is removed and checked under a microscope, repeated until no cancer cells remain","The whole area is frozen at once || Cryosurgery.","A dye finds the first lymph node || Sentinel node biopsy.","The lesion is scraped and burned || Curettage and electrodesiccation."],
 "The professor stressed the layer-by-layer process.")
q("surg","What is curettage and electrodesiccation?",
 ["*Scraping the lesion and destroying remaining tissue with heat","Removing layers one by one with microscopy || Mohs.","Freezing with liquid nitrogen || Cryosurgery.","Activating a topical drug with light || Photodynamic therapy."],
 "Used for basal or squamous cell lesions.")
q("surg","After a wide excision of a large lesion, what may be needed to close the wound?",
 ["*A flap or skin graft","Nothing; it always closes by itself || Large defects may need a graft.","A cast || Not for skin.","Sentinel node biopsy || That checks spread."],
 "Wide excision removes the lesion plus surrounding tissue.")

# ---------- grafts ----------
q("graft","Which statement describes a split-thickness skin graft?",
 ["*Epidermis plus superficial dermis; it can be meshed to cover a larger area","The entire epidermis and dermis || That's full-thickness.","Skin from a donor cadaver only || Autografts come from the client.","A synthetic patch || Not the definition."],
 "The donor site keeps follicles and sweat glands; thigh and buttock are common donor areas.")
q("graft","What is an autograft?",
 ["*Skin taken from the client's own healthy skin","Skin from another person || Not an autograft.","Skin from an animal || Not an autograft.","A bandage || Not a graft."],
 "A dermatome harvests thin donor skin.")
q("graft","Which statement describes a full-thickness graft?",
 ["*It includes the entire epidermis and dermis and is stitched into position","It's only the epidermis || Not full-thickness.","It's meshed to stretch || That's split-thickness.","It's taken from the client's scalp only || Not specified."],
 "Full-thickness grafts are placed over the defect and sutured.")

# ---------- donor vs graft ----------
q("donor","A client says the donor site hurts more than the graft site. How should the nurse respond?",
 ["*'That's common; the donor site is often more painful.'","'That means the graft failed.' || Not the meaning.","'The donor site never hurts.' || It often hurts more.","'You must have an infection.' || Not necessarily."],
 "Treat pain and keep the nonadherent dressing in place until healed.")
q("donor","Which findings are expected at a DONOR site? "+SATA,
 ["*Wet, weeping drainage for about 3–5 days, then a dry phase","*A nonadherent dressing that lifts off as it heals","*Discoloration","Bulky pressure dressing to keep contact with a wound bed || That's the graft site."],
 "Teach sun protection (the professor discussed about a year).")
q("donor","Which care is needed at the GRAFT site? "+SATA,
 ["*Bulky pressure dressing for about 3–5 days","*Immobilize and elevate the area","*Monitor color, vascularization and adherence","*Watch for blood or fluid trapped under the graft","Remove the dressing daily to look || Movement disrupts adherence."],
 "Vascularization may begin within about 36 hours.")
q("donor","Why is fluid trapped under a skin graft a concern?",
 ["*It keeps the graft from adhering to the wound bed","It speeds healing || It prevents adherence.","It's expected and harmless || It can cause graft failure.","It numbs the area || Not the concern."],
 "Preserve graft–wound contact.")

# ---------- systemic ----------
q("systemic","How does immunotherapy treat advanced skin cancer?",
 ["*It helps the body recognize and attack malignant cells and build immune memory","It freezes the tumor || Cryosurgery.","It blocks the tumor's blood supply only || Targeted therapy can.","It removes the tumor layer by layer || Mohs."],
 "Targeted therapy blocks growth signals and/or tumor blood-vessel formation.")
q("systemic","When is standard chemotherapy discussed for skin cancer?",
 ["*For cancers that don't respond to other therapies","For every actinic keratosis || Not the use.","Instead of sunscreen || Not prevention.","Only before a biopsy || Not the use."],
 "Immunotherapy and targeted therapy are used for advanced or metastatic disease.")

# ---------- promotion ----------
q("promo","Which sun-protection teaching is correct? "+SATA,
 ["*Avoid peak sun, about 11 a.m. to 3 p.m.","*Wear long sleeves, a wide-brimmed hat and sunglasses","*Avoid tanning booths","*Apply sunscreen about 30 minutes before going out","Reapply sunscreen once a day only || Every 2 hours."],
 "Reapply every 2 hours and more often when swimming or sweating.")
q("promo","Which SPF does the lecture recommend?",
 ["*SPF 15–30","SPF 4 || Too low.","SPF 100 only || Not the lecture range.","No sunscreen is needed with a tan || Always protect."],
 "Sunscreen has a shelf life; check expiration.")
q("promo","How should a client do a skin self-exam?",
 ["*After a bath or shower, in a well-lit room, using full-length and handheld mirrors","Only in dim light || Use bright light.","Only on the face || The whole body.","Only once every 10 years || More often, plus annual checks."],
 "'Check your birthday suit on your birthday' for an annual professional exam.")
q("promo","Which teaching fits the professor's saying, 'Check your birthday suit on your birthday'?",
 ["*Get an annual professional skin check","Only check your skin on your birthday, never otherwise || Self-exams are also taught.","Buy new sunscreen yearly only || Not the meaning.","Get a tan on your birthday || Opposite."],
 "Know your usual moles and use ABCDE.")
