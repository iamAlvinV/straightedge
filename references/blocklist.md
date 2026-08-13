# Blocklist

<!-- scan:allow-folklore -->

Claims that are false, misattributed, untraceable, or inverted from what the source says. None of these enter the work, the rationale, a deck, a pitch, a caption, or a client email. If a stat has no traceable primary source, it does not ship.

`scripts/scan.py` catches the string-matchable ones. The rest are on judgment.

---

## Color

- "Color boosts brand recognition by 80%." Untraceable. Came from a Xerox marketing leaflet. The original figure, where one exists, was about color aiding document and graph processing, not brand recognition.
- "62 to 90% of judgment happens in 90 seconds and it is mostly color." Uncited. Traces to the Institute for Color Research, restated without an experiment.
- "85% of purchase decisions are color."
- "Red makes people more attractive or smarter." Failed multiple large replications.
- Fixed color-emotion equations stated as law. Blue equals trust, red equals energy. Weak, cultural, context-dependent, not deterministic.
- "Complementary colors give maximum visual contrast." Conflates hue contrast with luminance contrast. True for hue only. Says nothing about readability.
- "There is a universal best button color." False. The winner is whatever contrasts with its surroundings on that page. It flips by context.
- Precise "color X means emotion Y in culture Z" charts. Folklore. Verify the target market. Perception is universal, meaning is not.

## Layout, grid, and geometry

- "The 8px grid is an official standard." It is a convention, formalized only inside Material Design.
- "Most screen sizes divide by 8, so the grid is mathematically required." Engineering folklore.
- "There are standard responsive breakpoints." There are not. Frameworks disagree. Choose by content.
- "The golden ratio makes a layout objectively more beautiful or higher-converting." Weak and contested. Near-zero support for abstract UI geometry.
- "The golden ratio is the correct type-scale ratio." One option among many, and a poor default for body-text work. The nature-and-art story was formally challenged (Markowsky, 1992) on cherry-picked measurements.
- Golden ratio or Fibonacci construction of famous logos. Retrofitted. Overlays fit almost any shape. Not a construction method.
- "The rule of thirds improves UI usability." No UI evidence.
- "Optimal line length is 600 to 700 pixels." Font-size dependent. The real target is 50 to 75 characters set in ch or em.
- "45 to 75 characters is proven best for screens." That range is a print guideline. Screen research is mixed.

## Attention and scanning

- "Design toward the F-pattern." Inverts the source. The F-pattern is a symptom of weak formatting that the research says to prevent.
- "The Z-pattern is eye-tracking validated like the F-pattern." False. Z-pattern is craft lore from the Gutenberg Diagram, 1950s. Only the F-pattern has the eye-tracking evidence.
- "The eye always enters top-left." Only for left-to-right readers. It is reading direction, not human vision.
- "Centering traps the eye." Wrong. Center bias is real. The center is usually the easiest thing to see.
- "Users decide in 50 milliseconds whether to stay or leave." Misstates the study. It measured visual appeal only.
- "You have two seconds to make an impression." False as impression latency. The verdict forms in about 50 to 100ms. If two seconds is meant as dwell time, label it as dwell time.
- "The 8-second attention span" or the goldfish comparison. Fabricated. Traced to a marketing figure. Attention capacity is stable across decades.
- "More visual paths keep people looking longer." Unproven. More time can mean confusion.
- "Right-to-left motion damages brand trust." One advertising paper amplified by neuromarketing blogs. Magnitude unproven.

## Whitespace and hierarchy

- "White space increases comprehension by 20% (Lin, 2004)." Mis-cited. The study was about older adults reading Chinese hypertext topology. The author confirmed it has nothing to do with whitespace.
- "Change weight by 100 to 200 units between roles." Arbitrary. No standards body sets this. Aim for clear distinction.
- "80/20 of visual logic" as a measured law. Rhetorical framing, not a finding.
- "A distinctive element is more likely to be clicked (von Restorff)." Misapplied. The isolation effect is about memory and recall, mainly free recall, not click likelihood.
- "Contrast on a CTA creates an addictive response." False. Addiction comes from variable reward schedules. Contrast affects attention, not compulsion.
- "The larger sign-up option gets clicked simply because of contrast." Oversimplified. Framing, defaults, decoy pricing, and social proof do most of the work.

## Type and text

- "Headers are 1:1 and body is 1:1.5, always." Half true. Body at 1.5 is the accessibility anchor. Header leading is 1.1 to 1.2, not a literal 1.0.
- "Set letter spacing to -1 to -3 pixels for display." Right direction, wrong unit. Use em.
- "Nielsen found users check out the second they see a big block of text." Misattributed drama.
- "Lists get 308% more attention." Untraceable.
- "Bullet points give the brain a dopamine hit." Pop neuroscience. Bullets aid scanning. That is the whole claim.
- Typeface spelling: it is **Mulish**, not "mullish."

## Logo and identity

- "You must be able to draw it from memory" as an absolute law. A heuristic. Clarity is the target, not minimalism.
- The FedEx-arrow claim that hidden meaning is processed subliminally. Not supported. Only about 4 to 20% notice the arrow at all.
- Any single universal minimum-size number. Minimum size is per medium and per reproduction.
- Any fixed pixel clear-space value. Clear space must be proportional.
- "Living or modular identity is a 2026 novelty." The practice is 15 or more years old. MIT Media Lab, Google 2015, responsive logos 2014.
- "3D and depth systems are a 2026 invention." Elevation systems have been formalized since 2014.

## Conversion and business

- Bare "40% more conversions" as a design law. Untraceable as a generic claim. The only real figure near it is one 2008 political-campaign landing-page A/B test, roughly a 40.6% signup lift. One experiment, not a rule.
- Loose CRO percentages generally: "good UX boosts conversions up to 400%," "personalized CTAs convert 202% better." Vendor numbers recirculated without primary studies.
- "This is the difference between a $500 and a $5,000 website." Rhetoric, not a benchmark.
- "Human-made design commands a 10 to 50 times pricing premium." Unsourced.
- "Heavy orange is the 2026 color strategy." Unsupported.

## AI claims

- "AI cannot keep a character consistent." Outdated. Single-subject consistency is productized. The accurate version: AI struggles with full brand-system consistency across formats.
- Any hard AI consistency percentage, "90 to 95 percent consistent." Untraceable marketing numbers.
- Vendor phrases repeated as fact: "perfectly consistent," "brand-compliant," "shot to shot identical."
- "Creativity is trainable, not innate." Overstated. Substantially trainable but multi-determined.
- "AI produces probable outputs, creativity is improbable combinations." A metaphor, not a technical fact. Fine as illustration, not as a defended claim.
- The "22 times more likely" polymath statistic. Comes from a narrow set of specific hobbies, not arts study in general.
- Any neuroscience claim that brains register or detect perfection as manufactured. Practitioner assertion, no primary research.

## Design philosophy overreach

- "More shock equals more memory." False. Inverted U. Extreme incongruity underperforms.
- "A memorable design is a successful design." Incomplete. If the surprise is memorable but the brand is forgotten, the job failed.
- "Iconic work is iconic because it is not perfect." Overcorrection. Much iconic work is technically masterful. The point is the single idea.
- "Design for results applies to all design." Overstated. Holds for commercial and UX work, not for brand, editorial, or cultural work judged on resonance.
- "Removing elements always makes a design better." Overgeneralized. Reduction has limits and can mask real problems.
- "Emotion always comes before cognition, and that is proven." Contested. Affective primacy was debated and never settled. Working assumption, not a law.
- "99% of designers don't consider [X]." Invented stat pattern. Drop on sight.
- Loose Jobs or Ive one-liners from quote-aggregator sites presented as a documented Apple process.
- Unverifiable case studies: "the Elseworld project won at AGDA," "the Aqua logo by Six Inc." Neither confirms. Pull a verified winner from the official archive instead.

---

## Claims that ARE safe to use

- Users scan rather than read. About 79% scan, roughly 16% read word for word.
- Users read about 20 to 28% of the words on a page. Traces to Nielsen Norman Group.
- NN/g eye tracking found users spend about 80% of viewing time on the left half of a page. A real finding about horizontal attention, not about design principles.
- Low-contrast text is the single most common accessibility failure on the web.
- Roughly 1 in 12 men have a color vision deficiency, red-green most common.

---

Designed by IamAlvinV
