# English study site, built with the studynow kit: python3 build.py course.py OUT
import json, os
D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "deck.json")))
SECS = []
for s in D["sections"]:
    s = dict(s); s.pop("quizlet", None)
    if not s.get("cards"): s["steps"] = [0, 1, 4, 5]
    SECS.append(s)
COURSE = {
 "name": "Representations of Social Conflict, 10th grade",
 "eyebrow": "The Clinton School, 2026 to 2027",
 "intro": "Study loops for the quiz on \"Interpreter of Maladies\" by Jhumpa Lahiri: the characters, what happens, the symbols, the themes and the quotes to know.",
 "img": "img", "breakMinutes": 5, "dumpMinutes": 7,
 "extras": [{"eyebrow": "Quiz Mon, Nov 2", "title": "Written practice", "text": "Pick 2 likely questions, answer them on the clock, then check each answer and compare with a model outline.", "href": "practice/"}],
 "units": [{"label": "Story", "name": "Interpreter of Maladies", "title": "Interpreter of Maladies",
   "chip": "Quiz Mon, Nov 2",
   "topics": "Mr. Kapasi and the Das family, the trip to the Sun Temple, the confession, the monkeys, the address slip, miscommunication, loneliness, cultural identity",
   "source": D.get("source", ""), "sections": SECS,
   "review": {"must": ["Mr. Kapasi interprets for a doctor and gives tours on Fridays and Saturdays",
                       "Mrs. Das tells him Bobby is not Raj's son",
                       "\"Is it really pain you feel, Mrs. Das, or is it guilt?\"",
                       "The address slip blows away, so the letters he dreamed of will never come",
                       "Title: he interprets illness for patients but can't interpret or heal her"], "secs": {}}}]}
