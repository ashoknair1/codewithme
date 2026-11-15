# Ep 6 (Expert) — From Vibe Code to Production: Ship It Safely

**What you build:** nothing new — you take the Ep 1 app and make it *shippable*: tests, a review pass, secrets out of the code, an error page that doesn't leak, and a one-command start.

**The one key idea:** prototypes are easy; production is a checklist, not a vibe. The gap between "it works on my screen" and "strangers can use it" is a finite list of unglamorous checks — work the list.

**Worth knowing:**
- Let the agent write the tests, then *you* read them. Generated tests that only assert what the code already does are decoration.
- Run the Ep 3 code-review Skill on the final diff — fresh "eyes" catch what the building session rationalized away.
- Secrets and debug mode are the two classic vibe-code leaks. Check them by name, every release.

**Try this:** run `production_checklist.md` against any app you've built this series and count how many boxes you honestly tick. Hint: most first apps score under half — that's normal, and it's exactly the list to work.
