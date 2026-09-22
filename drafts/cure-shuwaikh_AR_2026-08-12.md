<!--
AR twin body for the WPML twin of EN guide_article 5025 (Cure, Shuwaikh).
Bader-authored Kuwaiti Arabic, pasted 2026-08-12 — D-145 human translation.
FAITHFUL INJECT: his wording is reproduced verbatim. Only mechanical changes:

  1. STRIPPED the "# Cure" title line, the italic deck line, and the
     "بقلم فريق تحرير Q8tly · ١٢ أغسطس ٢٠٢٦" byline — the guide template renders
     all three (title / deck meta / byline). Leaving them in the body
     double-renders. The deck line is carried in `deck:` below instead, verbatim.
  2. The third section heading is "شورت ريبز دونبوري" — the dish's real name
     (Bader, 2026-08-12: use the dish name, drop the generic meat-dish wording).
     EN twin caption = "Short Ribs Donburi", already live on 5025.
  3. Inserted [[image:...]] markers under the matching headings.

TWO JUDGMENT CALLS — flagged to Bader, easy to reverse:
  A. His formula uses H2 HEADINGS where the EN uses photo CAPTIONS (his headings
     are the EN captions promoted). So photos here are inserted with NO caption —
     the heading already names each one, and a caption repeating the heading
     verbatim reads as a stutter.
  B. For the same reason `hero_caption` is left EMPTY: the template prints the
     hero caption directly above "## من برا Cure", which would duplicate it.
  => If he wants captions as well as headings, add them and re-run; nothing else moves.

STRUCTURAL DIVERGENCE, NEEDS HIS CALL: the live EN body has NO H2 sections
(captions only). This AR has four. EN and AR are supposed to mirror. Either the
EN gets restructured to match this formula, or the AR drops the headings.
NOT resolved unilaterally — the EN is live on prod.

⚠ FENCE: `populate_ar_twin.py` HARDCODES `rank_math_robots = noindex` (rail #4,
pre-flip). Post-flip that is WRONG — all six AR twins checked on prod (2600/2612/
2618/2808/2924/3122) have EMPTY rank_math_robots, i.e. UNFENCED and indexed.
Running the tool unmodified would make Cure the only noindexed twin. Fence must
be cleared after the run (or the tool given a --no-fence flag) — see handoff.

Media reused from the EN guide: hero=5021, inline-1=5022, inline-2=5023, inline-3=5024.
Meta ASCII where the field is ASCII-only (CHARSET.md); Arabic meta goes through
populate_ar_twin.py's ensure_ascii=False path, which is charset-safe.
-->
---
title: "Cure"
slug: cure-shuwaikh
lang: ar
deck: "مطعم ياباني–ميديتيراني راقٍ داخل Design District في الشويخ، بديكور مشرق وواضح التفاصيل، قائمة موسمية تتغيّر، وجلسات داخلية وخارجية."
topic: food-drink
article_type: guide
place_id: 3807
map_ids: []
word_count: auto
# SEO restored 2026-08-13 — these MUST live in the draft. Re-running the tool on a
# draft without them previously WIPED the live values (that is how 5032 lost its
# title+description mid-session). Tool now keeps existing values, but the draft is
# the source of truth, so they belong here. Pattern ratified under A4.
seo_title: "كيور Cure | مطعم ياباني–ميديتيراني في الشويخ"
meta_description: "مطعم ياباني–ميديتيراني راقٍ داخل Design District في الشويخ، بديكور مشرق وواضح التفاصيل، قائمة موسمية تتغيّر، وجلسات داخلية وخارجية."
hero_alt: "واجهة مطعم Cure في Design District بالشويخ — واجهة بلون خمري غامق تحت مظلة نحاسية، والاسم مكتوب بالعربي والإنجليزي."
hero_caption: ""
status: publish
---

## من برا Cure

Cure موجود داخل Design District في الشويخ، وهذا يمكن يعطيك انطباع مختلف شوي عن اللي بتلقاه لما تدخل. الوصول للمطعم يكون من داخل المجمع، مو من واجهة مباشرة على الشارع. تمر بواجهة بلون خمري غامق واسم Cure مكتوب فوق المدخل بالعربي والإنجليزي، وبعدها تدخل على مكان أهدأ وأرتب بكثير مما تتوقعه من طريق الدخول.

الأرضية تيرازو، وعلى طول أحد الجدران كنبة جلدية بلون برغندي، مع طاولات خشب فاتح وكراسي بظهر من الخيزران. وبين الأعمدة ستاير خفيفة تقسم المكان بصرياً من غير ما تحسسك إن المساحة مسكرة أو مزدحمة.

## صالة المطعم

[[image:inline-1||صالة مطعم Cure في الشويخ — طاولات خشب فاتح وكراسي خيزران على طول كنبة جلدية برغندي، وإضاءة نهارية من الواجهات الزجاجية.]]

هذا من الأماكن اللي النهار يطلعها بأفضل شكل. الواجهات الزجاجية كبيرة، وأغلب ألوان المكان فاتحة — حجر، خشب فاتح، وأقمشة كريمية — فوقت الغدا تكون الصالة فعلاً مشرقة، والنباتات الموجودة بالمكان تضيف له أكثر من الإضاءة نفسها.

بالليل يتغير الجو شوي. الإضاءة اللي تحت الكنبة تبدأ تبين أكثر وتعطي المكان دفء، لدرجة إن النهار والليل يحسون تقريباً كتجربتين مختلفتين. وإذا كان اختيارك مبني على الديكور، الغدا هو الوقت اللي تشوف فيه المكان بأوضح صورة.

أغلب الجلسات لشخصين أو أربعة على جهة الكنبة، وفي طاولات أكبر بالنص، بالإضافة إلى التراس الخارجي. المكان مناسب لموعد عشا لشخصين مثل ما يناسب طلعة مجموعة، لكن إذا تقدر تختار، جلسة الكنبة هي الأفضل — وهي اللي تستاهل تطلبها وقت الحجز.

## شورت ريبز دونبوري

[[image:inline-2||طبق شورت ريبز دونبوري في Cure — لحم قصير بصلصة لامعة فوق أرز بالفطر في صحن أسود، مزيّن بحلقة فلفل حار وبصل أخضر.]]

أساس المطبخ ياباني، ومعاه تأثيرات ميديتيرانية وأطباق فيوجن. ما في طبق واحد نقدر نقول عنه إنه الطبق الأشهر في Cure، والأفضل ما نخترع لك واحد بس علشان نعطيك توصية.

الشيء اللي فعلاً يستحق تنتبه له هو **قائمة الأطباق الموسمية**. قائمة قصيرة تنعطى لك بروحها غير المنيو الرئيسي، وتتغير من فترة إلى فترة.

وقت الزيارة اللي أخذنا فيها هالصور، كانت القائمة فيها ستة أطباق: سيزر بالسمسم، نودلز خضار مشوية، بطاطا مع دجاج بالبرتقال، روبيان بالجوز والعسل، ميسو رامن، وأرز بجوز الهند والمانجو.

اسأل عنها لما تروح. لأنها تتغير، وغالباً هي أكثر جزء بالمنيو يعطيك فكرة عن الأشياء اللي المطبخ قاعد يجربها ومهتم فيها حالياً.

## التراس

[[image:inline-3||تراس Cure الخارجي في Design District بالشويخ — طاولات وكراسي معدنية سوداء على أرضية مرصوفة بجانب واجهة المطعم الخمرية.]]

من ناحية السعر، Cure يقع ضمن فئة $$$. يعني مكان يناسب مناسبة أو طلعة مرتبة أكثر من كونه مطعم تروح له بشكل عفوي بنص الأسبوع، لكنه بنفس الوقت مو من أغلى الخيارات الموجودة بالسوق.

الحجز متوفر من خلال رابط الحجز الموجود بصفحة المطعم، والمنيو الكامل موجود أونلاين إذا تحب تشوف الخيارات والأسعار قبل ما تروح الشويخ.

**وشغلة نقولها لك بصراحة.**

الوصول للمطعم مو أقوى جزء من التجربة. ما عنده واجهة واضحة على الشارع أو مدخل يعطيك إحساس من البداية إنك وصلت للمطعم؛ تمشي داخل Design District إلى أن يطلع لك Cure في النهاية.

وبعد، المطعم ما يفتح إلا الساعة ١:٠٠ الظهر. فمع إن شكل المكان وإضاءته يخليك تتخيله مناسب لقعدة صباحية هادية، هذا الخيار مو موجود.

روح له على غدا متأخر، أو على العشا. هذولا فعلياً الوقتين اللي يناسبونه.

## معلومات سريعة

| | |
|---|---|
| **المطبخ** | ياباني · ميديتيراني · فيوجن |
| **ساعات العمل** | ١:٠٠ م – ١٠:٤٥ م، يومياً |
| **الأسعار** | $$$ |
| **الموقع** | Design District، شارع ٢٨، الشويخ |
| **الجلسات** | داخلية وخارجية |
| **الحجز** | متوفر |
| **مناسب لـ** | موعد عشا · مجموعات · غدا متأخر |

[[place]]
