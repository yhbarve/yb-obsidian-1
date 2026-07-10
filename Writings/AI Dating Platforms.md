---

---

## Introduction
Most people are terrible at writing about themselves. Dating profiles are a perfect example — users either undersell themselves with a vague three-liner, or overcorrect with something that sounds like a LinkedIn bio. What if a Large Language Model (LLM) could help bridge that gap?

This post explores a hypothetical (but grounded) product concept: an AI-powered **Profile Enhancement Assistant (PEA)** for an online matchmaking platform. We'll walk through the problem it solves, how we designed prompts for it, how three leading LLMs — GPT-4o, Claude Sonnet 4.0, and Gemini 2.5 Pro — performed on the task, and what responsible deployment of such a system would look like.
## The Problem: Profile Quality at Scale
Imagine you're running a matchmaking platform — let's call it Make-A-Date.com. You have tens of thousands of users, and a significant chunk of their bios look something like this:

> *"idk what to write here. i'm just vibing, life's weird. talk to me if you want lol"*

This isn't a bad person. It's just a bad bio — vague, low-effort, and unlikely to attract the right matches. Multiply this across thousands of profiles and you have a platform-wide quality problem that manual moderation can't realistically solve.

The stakes are real: poor profile quality leads to lower match rates, lower user satisfaction, and higher churn. It also increases the moderation burden when low-effort bios shade into inappropriate or off-brand content.

An LLM-powered assistant that can take a rough draft and transform it into something polished — without stripping out the user's personality — is a compelling solution.
## The Proposed System: Profile Enhancement Assistant (PEA)
The PEA works during the onboarding flow. Users provide:
- A rough draft of their bio (optional but encouraged)
- Their preferred **tone** (e.g., sincere, humorous, flirty, confident, quirky)
- A list of **interests** (e.g., hiking, board games, live music)
- Their **values** (e.g., honesty, ambition, spontaneity)
- Basic **demographic context** (age, gender identity, location)
This structured input is compiled into a prompt, the LLM generates a revised bio, and the user can accept, edit, or reject the result. If a bio is flagged for low quality or inappropriate content, the system can also generate an alternative before it ever reaches a human moderator.
The dual value here is clear: better user experience through personalized, engaging profiles, and lower operational cost through reduced manual moderation.
## Prompt Design
Good prompt engineering is the difference between a useful AI tool and a generic one. For the PEA, we used the following prompt template across all three models:

> You are an assistant helping users create standout dating profiles. Take the information below and craft a bio that feels natural, emotionally resonant, and aligned with the user's tone and personality. Feel free to reframe the content creatively — while staying true to the user's preferences, interests, and values. Avoid sounding generic or templated. Keep the writing concise, expressive, and engaging.
> 
> Important: Match the user's formatting style. If the original bio is a paragraph, the output should be a paragraph. If it includes emojis, lists, or line breaks, reflect that in the output. Preserve the user's stylistic intent while improving quality.

The instruction to match formatting style turned out to be critical — without it, models tend to normalize everything into uniform paragraphs, erasing the personality signals embedded in how someone originally wrote their bio.
## Comparing Three LLMs
We tested GPT-4o, Claude Sonnet 4.0, and Gemini 2.5 Pro on five synthetic user profiles, each varying in tone, input quality, and demographic context. Here's a snapshot of one input and how the models handled it:

**Input:**
> *"idk what to write here. i'm just vibing, life's weird. talk to me if you want lol"*
> *Tone: Playful | Interests: Music, memes | Values: Humor | Age: 22 | Male | Toronto*

**GPT-4o output:**
> *Somewhere between "figuring it out" and "fully vibing" — that's me. I'm into music that hits different at 2am, memes that make you question reality, and conversations that go nowhere but somehow feel meaningful. Life's weird. Let's be weird together.*

**Claude Sonnet 4.0 output:**
> *cozy nights in with terrible reality TV 🛋️*
> *my spotify wrapped is genuinely embarrassing 🎶*
> *3am conversations about everything and nothing ☕🌙*
> *let's debate whether pineapple belongs on pizza*

**Gemini 2.5 Pro output:**
> *Connoisseur of cozy nights in 🛋️*
> *Fueled by strong coffee ☕ and playlists that give you musical whiplash 🎶*
> *Let's trade weird facts and song recs until we forget what time it is 🌙*
> *All three are better than the original. But they're better in meaningfully different ways.*
## Evaluation: How Did the Models Stack Up?
We evaluated each model across five criteria: tone alignment, clarity and readability, personalization, creativity and engagement, and authenticity.

| Criterion               | GPT-4o    | Claude Sonnet 4.0 | Gemini 2.5 Pro |
| ----------------------- | --------- | ----------------- | -------------- |
| Tone Alignment          | Excellent | Very Good         | Good           |
| Clarity & Readability   | Very Good | Excellent         | Good           |
| Personalization         | Excellent | Good              | Moderate       |
| Creativity & Engagement | Very Good | Excellent         | Moderate       |
| Authenticity            | Excellent | Good              | Moderate       |

**GPT-4o** offered the most balanced performance overall. It was consistently the strongest at weaving user-specific details — interests, values, personal quirks — into outputs that felt genuinely human. When a user had an unusual anecdote or a distinctive voice, GPT-4o preserved and amplified it rather than smoothing it away.
**Claude Sonnet 4.0** stood out on creativity and humor. For profiles with a playful or quirky tone, its outputs were often the most memorable and distinctive. It occasionally leaned on wit at the expense of directly incorporating user values, but for engagement-focused bios, it frequently produced the most "swipe-worthy" results.
**Gemini 2.5 Pro** was the most reliable and cautious. Its outputs were consistently clear and well-structured, but tended toward safer, more neutral phrasing. For users who wanted a calm or sincere tone, it performed well. For edgier or more distinctive tones, it felt comparatively flat.

No single model dominated every use case — which actually suggests a smart product strategy: route tone preferences to the model best suited for them, or run multiple models in parallel and let users choose.
## Measuring Real-World Effectiveness
Controlled testing is a starting point, but it doesn't tell you if the tool actually improves the product. In a real deployment, the key metrics would be:
- **Bio adoption rate** — how often do users accept the LLM-generated version over their own draft?
- **Match engagement rate** — do users with enhanced bios receive more meaningful interactions (likes, messages, conversations)?
- **Moderator intervention rate** — does the LLM reduce the number of profiles that require manual review?
- **A/B testing** — comparing user satisfaction and match outcomes before and after LLM deployment
A combination of these metrics, surfaced in a stakeholder dashboard, would provide a clear picture of whether the investment is paying off — and where the system needs refinement.
## Responsible AI Considerations
Deploying an LLM on something as personal as a dating profile requires careful thought. A few non-negotiable principles:
1. **Transparency.** Users should always know when their bio has been AI-assisted. In a context built on authenticity and personal connection, concealing AI involvement would undermine the platform's core value proposition.
2. **User control.** Accept, edit, or reject — the LLM should be a suggestion engine, not an auto-publish tool. Users should always have the final word on how they present themselves.
3. **Data privacy.** The inputs used to generate a bio — tone, values, demographic context — are personal. They should be used only for the stated purpose, stored securely, and never repurposed for advertising or secondary profiling without explicit consent.
4. **Bias and safety.** LLMs can reflect the biases present in their training data. For a matchmaking platform, this is especially sensitive — outputs should be filtered for stereotypes, inappropriate framing, or language that violates community standards. Human moderators should remain in the loop, even if their workload decreases.
5. **Avoiding homogenization.** If every bio on the platform starts sounding like it was written by the same AI, the platform loses its diversity and authenticity. Encouraging users to edit outputs, offering multiple variations, and prompting reflection ("does this sound like you?") can help keep profiles genuinely individual.
## The Bigger Picture
LLMs are not here to replace self-expression — they're here to lower the activation energy required to do it well. Most people know roughly who they are and what they're looking for; they just struggle to articulate it in a 150-word bio under pressure.

A well-designed PEA gives those users a starting point. It takes the raw material of who someone is and helps them shape it into something that communicates clearly and attractively. The best version of this tool is invisible — users don't think "the AI wrote this," they think "oh, that actually sounds like me."

That's the standard worth aiming for.