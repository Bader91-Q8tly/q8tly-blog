<!--
AR twin body for the WPML twin of EN guide_article 5430 (Solange Maison, Salhia Complex).
Bader-authored Kuwaiti Arabic, pasted 2026-08-13 — D-145 human translation. FAITHFUL INJECT:
his wording is reproduced verbatim. Only mechanical changes:

  1. STRIPPED the title line and the byline "بقلم فريق تحرير Q8tly · ١٣ أغسطس ٢٠٢٦" — the
     template renders title / deck / byline. Leaving them in the body double-renders.
     His deck sentence is carried in `deck:` below, verbatim.
  2. Inserted [[image:...]] markers under headings 2/3/4, mirroring the EN exactly
     (inline-1 under الصالة, inline-2 under السقف, inline-3 under الأكل). No captions,
     empty hero_caption — the four-H2 mirror shape.

⚠ ONE CALL FOR BADER — the TITLE. He wrote «سولانج ميزون» (Arabic transliteration) as the
heading, but his own standing rule is "business names stay in the business's own script",
and his body text uses the Latin "Solange Maison" throughout. Cure's AR twin is titled "Cure"
(Latin) for the same reason. So this ships as **"Solange Maison"**. One-line change if he
wants the transliteration instead.

STRUCTURE ✓ mirrors EN 5430 exactly: four H2s (من أول المصعد / الصالة / السقف / الأكل) +
معلومات سريعة, 7-row facts table, [[place]]. This pair is the first fully-mirrored EN/AR guide.
⚠ Cure EN still has zero body H2s — Advisor note 2026-08-13.

⚠ FENCE: populate_ar_twin.py hardcodes rank_math_robots=['noindex'] (pre-flip rail #4).
Every twin on prod is UNFENCED — clear the fence after the run.
⚠ ALT: kit does `alt = cap or title`, so captionless inline images get alt="Solange Maison".
Known live defect, fix owed in the kit (not hand-patched here).

Media reused from the EN guide: hero=5426, inline-1=5427, inline-2=5428, inline-3=5429.
-->
---
title: "Solange Maison"
slug: solange-maison-kuwait-city
lang: ar
deck: "مطعم صيني راقٍ في الميزانين داخل مجمع الصالحية بمدينة الكويت — أجواؤه غامقة ومسرحية، سقفه مرسوم بتفاصيل لافتة، وعنده ساحة داخلية تعطيك إحساس الجلسة الخارجية، لكنها فعلياً داخل المجمع."
topic: food-drink
article_type: guide
place_id: 4025
map_ids: []
word_count: auto
# SEO ADDED 2026-08-13 (Bader approved). The twin shipped with NO rank_math_title and NO
# rank_math_description — the AR <title> was the bare "Solange Maison" and there was no
# description at all, while the EN twin had both. Separately, «سولانج ميزون» appeared ZERO
# times on the AR page, so an Arabic-script brand query had nothing to match.
# Fix: carry BOTH name forms in the SEO title. The H1/post_title stays LATIN for entity
# consistency (their domain solangemaison.com, @solange.maison, the listing, the EN twin,
# hreflang) — the Arabic form earns its keep in the title tag instead.
# Arabic in these fields is safe here: populate_ar_twin.py uses ensure_ascii=False
# (charset-safe). Do NOT copy this into a publish_guide.py drop — that path mojibakes.
# NOT DONE (needs Bader's separate word — it edits his D-145 copy): working «سولانج ميزون»
# into the opening body sentence. Offered, declined-by-omission, still open.
seo_title: "سولانج ميزون Solange Maison | مطعم صيني راقٍ في الصالحية"
meta_description: "مطعم صيني راقٍ في الميزانين داخل مجمع الصالحية بمدينة الكويت — يفتح من ١ ظهراً إلى ١١ مساءً يومياً، بأجواء غامقة وسقف مرسوم وساحة داخلية."
hero_alt: "المصعد الكهربائي الصاعد إلى Solange Maison في الميزانين داخل مجمع الصالحية بمدينة الكويت — ممر غامق واسم المطعم مكتوب بالذهبي على الجدار."
hero_caption: ""
status: publish
---

## من أول المصعد

Solange Maison موجود في الميزانين داخل مجمع الصالحية، ووصولك له يكون عن طريق مصعد كهربائي ضيّق وإضاءته غامقة، واسم المطعم مكتوب قدامك بالذهبي. من البداية واضح إن الدخول نفسه جزء من التجربة.

أول ما توصل فوق، تستقبلك بوابة حمراء لامعة، وعلى الجانبين لوحات مرسومة يدوياً بالأزرق والأبيض، ومعها ستاير ثقيلة مفتوحة على المطعم من الداخل.

## الصالة

[[image:inline-1||صالة مطعم Solange Maison في مجمع الصالحية — طاولات دائرية بمفارش بيضاء ولمبات نحاسية صغيرة، والقماش متجمع على السقف.]]

من داخل، المكان غامق، أحمر، ومليان تفاصيل — وبشكل مقصود. القماش متجمع على السقف بطريقة تذكرك بالخيام، والطاولات الدائرية عليها مفارش بيضا، وكل طاولة عليها لمبة نحاسية صغيرة بإضاءة هادية. على الجدران رسومات جبال وغيوم، وفي آخر الصالة تركيب زهور بإضاءة وردية يعطي المكان بعد أكثر.

هذا مكان يناسب العشا أكثر بكثير من الغدا. الإضاءة خافتة لدرجة إن لمبات الطاولات الصغيرة تسوي جزء كبير من الشغل — الجو حلو وراقي، لكن بنفس الوقت توقّع إنك تقرأ المنيو على إضاءة هادية.

المطعم مسجل عندنا كخيار مناسب للـ date nights، وهذا يمكن أوضح استخدام له، لكن الطاولات الدائرية تستوعب قروب من ستة أشخاص بدون مشكلة، ومناسب أيضاً للمناسبات الرسمية وعشا القروبات.

## السقف

[[image:inline-2||السقف المرسوم في Solange Maison — دائرة كبيرة فيها زهور وأمواج وطيور بدرجات الكورال والأحمر والأزرق الغامق، وحولها قماش أحمر متجمع.]]

أكثر شيء الناس ترفع راسها وتصوره هو الدائرة الكبيرة المرسومة في نص السقف — فيها زهور peony، أمواج وطيور cranes بدرجات الكورال والأحمر والأزرق الغامق، وحولها القماش المتجمع وتتقاطع فوقها خطوط سوداء رفيعة.

يمكن هذا أكثر تفصيل يلخص Solange Maison: الديكور جزء أساسي من التجربة وجزء من اللي قاعد تدفع عليه. إذا هالنوع من الأماكن ما يفرق معاك، الأفضل تعرف هالشي قبل ما تحجز، مو بعد ما تقعد.

## الأكل

[[image:inline-3||طاولة أطباق في Solange Maison — دجاج مقلي وسلطة ومشروبات مثلجة على مفرش أبيض، وخلفها إضاءة وردية من تركيب الزهور.]]

المطبخ صيني. وأكثر من جذي ما راح نبالغ، لأن ما عندنا طبق مسجل كـ signature dish، وما نبي نخترع لك واحد.

الشي المفيد إن المنيو كاملة موجودة أونلاين، ومع مستوى الأسعار هنا، الأفضل تطلع عليها قبل لا تروح بدل ما تعرف الأسعار بعد ما تقعد على الطاولة.

من ناحية السعر، Solange Maison عندنا $$$$ — أعلى فئة سعرية في Q8tly، وهذه أهم معلومة لازم تعرفها من البداية. ما عندنا متوسط سعر للشخص منشور، فالأفضل تشيك المنيو قبل الحجز. الحجز متوفر من خلال رابط الحجز، وموجود رقم تلفون إذا تفضل تسألهم مباشرة.

**وشغلة لازم تعرفها.** عندنا في البيانات إن المطعم فيه جلسات داخلية وخارجية، لكن كلمة «خارجية» هنا ممكن تعطي فكرة غلط.

الجلسة عبارة عن ساحة داخل مجمع الصالحية، مصممة كأنها شارع: أعمدة إنارة سوداء، ممشى أحمر وزرع حقيقي. شكلها فعلاً جميل، لكنها مسقوفة، مكيفة، وما فيها سما مفتوحة. يعني لا تحجزها على أساس إنها تراس أو جلسة هواء طلق.

ونفس الشي بالنسبة للموسيقى الحية: مذكور إنها موجودة أحياناً، لكن ما عندنا جدول ثابت لها. إذا صادفتها تكون إضافة حلوة، لكن لا تخليها السبب الرئيسي لزيارتك.

## معلومات سريعة

| | |
|---|---|
| **المطبخ** | صيني |
| **ساعات العمل** | ١:٠٠ ظهراً – ١١:٠٠ مساءً، يومياً |
| **السعر** | $$$$ |
| **الموقع** | مجمع الصالحية – الميزانين، شارع الشهداء، مدينة الكويت |
| **الجلسات** | داخلية وجلسة ساحة داخل المجمع · تكييف قوي |
| **الحجز** | متوفر |
| **مناسب لـ** | ديت نايت · مناسبات رسمية · عشا قروبات |

[[place]]
