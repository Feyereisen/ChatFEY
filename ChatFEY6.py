import random
import math

# Person List
person = ["boy", "girl", "man", "woman", "policeman", "firefighter", "doctor", "teacher", "student", "nurse", 
"engineer", "artist", "musician", "chef", "scientist", "athlete", "writer", "veterinarian", "waiter", 
"businessperson", "politician", "lawyer", "mechanic", "entrepreneur", "pharmacist", "surgeon", "architect", 
"electrician", "plumber"
]

# Object List
object = ["chair", "book", "table", "car", "phone", "plant", "lamp", "watch", "pen", "bag", 
"guitar", "shoe", "camera", "hat", "laptop", "bicycle", "ring", "necklace", 
"painting", "key", "wallet", "clock", "headphone", "bracelet", "perfume", "suitcase", "scarf"
]

a_person = ["engineer", "artist", "athlete", "entrepreneur", "architect", 
"electrician", "elegant", "joyful", "exquisite", "innovative", "optimistic", "adventurous",
"affectionate", "inspiring", "exuberant", "evocative", "eloquent", "intriguing",
    "expressive", "elegant", "enchanting", "eloquent", "effervescent", 
    "articulate", "enigmatic", "airport", "office", "island", "university"]

# Location List
location = ["park", "beach", "school", "restaurant", "library", "hospital", "stadium", "museum", "airport", "cafe", 
"mountain", "lake", "river", "hotel", "office", "farm", "theater", "market", "street", "garden", 
"island", "zoo", "bridge", "castle", "gym", "temple", "church", "mosque", "mall", "university"
]

nouns = [
"boy", "girl", "man", "woman", "policeman", "firefighter", "doctor", "teacher", "student", "nurse", 
"engineer", "artist", "musician", "chef", "scientist", "athlete", "writer", "veterinarian", "waiter", 
"businessperson", "politician", "lawyer", "mechanic", "entrepreneur", "pharmacist", "surgeon", "architect", 
"electrician", "plumber", "chair", "book", "table", "car", "phone", "plant", "lamp", "watch", "pen", "bag", 
"guitar", "shoe", "camera", "hat", "laptop", "bicycle", "ring", "necklace", 
"painting", "key", "wallet", "clock", "umbrella", "headphone", "bracelet", "perfume", "suitcase", 
 "scarf"
]
# Verbs
verbs = [
   "runs to", "sings about", "danced with", "writes to", "swims to",
   "read about", "jumped at", "paints on", "played near", "talks about",
   "drived to", "flyed away from", "climbs towards to", "sleeps with",
   "worked with", "is studying", "laughed about", "travels to", "created", "is created by", "moves toward", "rotates in the dirction of", "was broken by", "was seen by", "produced", "is produced by", "changed", 
"breakes", "bended", "floats next to", "attracted"
]

o_verbs = ["moves toward", "was rotated in the dirction of", "is produced by", "is changed by", 
"vanished in front of", "levitated next to", "attracted", "was seen by", "was broken by", "is created by"
]

p_p_verbs = ["runs to", "sings about", "danced with", "writes to", "swims to",
   "read about", "jumped at","talks about",
   "drived to", "flyed away from", "climbs towards to", "sleeps with",
   "worked with", "laughed about", "travels to", "was seen by", "moves toward"]


p_verbs = [
   "runs to", "sings about", "danced with", "writes to", "swims to",
   "read about", "jumped at", "paints on", "played near", "talks about",
   "drived to", "flyed away from", "climbs towards to", "sleeps with",
   "worked with", "is studying", "laughed about", "travels to", "created", "breakes", "bended", "produced",
]

a_verbs = ["paints on", "is studying", "created", "breakes", "produced", "bended", "read about", "sings about"]
b_verbs = ["is produced by", "sleeps with",
   "worked with", "danced with", "was broken by", "is created by", "writes to"]
# Adjectives
adjs = [
   "happy", "friendly", "creative", "curious", "elegant",
    "playful", "charming", "joyful",
    "captivating", "exquisite", "tender", "innovative",
    "kind-hearted", "optimistic", "gracious", "spontaneous", "adventurous",
    "affectionate", "witty", "compassionate", "inspiring", "resilient", "beautiful", "green", "quiet", "bright", "warm",
    "colorful", "peaceful", "vibrant", "mysterious",
    "brilliant", "lively", "majestic",
    "whimsical", "tranquil", "dynamic", "picturesque",
    "splendid", "refreshing", "radiant", "scenic",
    "sophisticated", "exuberant", "thriving", "splendid", "vivid", "nuanced", "evocative", "eloquent", "intriguing",
    "expressive", "captivating", "poignant", "mellifluous", "profound",
    "whimsical", "nuanced", "elegant", "enchanting", "meticulous",
    "resonant", "dynamic", "eloquent", "effervescent", 
    "articulate", "persuasive", "enigmatic", "alluring", "harmonious"
]

adjs_p = [
    "beautiful", "happy", "friendly", "creative", "curious", "elegant",
    "playful", "charming", "joyful",
    "captivating", "exquisite", "tender", "innovative",
    "kind-hearted", "optimistic", "gracious", "spontaneous", "adventurous",
    "affectionate", "witty", "compassionate", "inspiring", "resilient"
]

adjs_o = [
    "beautiful", "green", "quiet", "bright", "warm",
    "colorful", "peaceful", "vibrant", "mysterious",
    "brilliant", "lively", "majestic",
    "whimsical", "tranquil", "dynamic", "picturesque",
    "splendid", "refreshing", "radiant", "scenic",
    "sophisticated", "exuberant", "thriving", "splendid"
]

adjs_l = [
    "vivid", "nuanced", "evocative", "eloquent", "intriguing",
    "expressive", "captivating", "poignant", "mellifluous", "profound",
    "whimsical", "nuanced", "elegant", "enchanting", "meticulous",
    "resonant", "dynamic", "eloquent", "effervescent", "persuasive", "enigmatic", "alluring", "harmonious"
]


# Connectors
connect = [
   "and", "but", "or", "because", "although",
   "since", "while", "when", "if", "unless",
   "however", "therefore", "meanwhile", "moreover",
   "nevertheless", "otherwise", "furthermore", "thus",
   "consequently", "notwithstanding", "in addition", "on the other hand",
   "as a result", "in contrast", "for instance"
]
def create_sentences0(nouns,verbs,adjs,connect,location,Mnoun,Snoun):
   sentences = []
   for _ in range(1):
       noun1 = random.choice(nouns)
       lp = 0
       if Mnoun in person:
          verb = random.choice(p_verbs)
       else:
          verb = random.choice(o_verbs)
       if verb in a_verbs:
          noun2 = random.choice(object)
       elif verb in b_verbs:
          noun2 = random.choice(person)
       else:
          noun2 = random.choice(nouns)
       if lp == 2:
         adj = random.choice(adjs_p)
       elif noun2 in object:
         adj = random.choice(adjs_o)
       elif noun2 in person:
         adj = random.choice(adjs_p)
       else:
         adj = random.choice(adjs_l)
       if Snoun == 0:
         if verb in ["runs to", "swims to", "played near", "drived to", "flyed away from", "climbs towards to", "travels to","moves toward", "rotates in the dirction of", "floats next to"]:
            lp = random.randint(1, 2)
            loc = random.choice(location)
            per = random.choice(person)
            if (lp == 1):
               sentence = f'Our {Mnoun} {verb} the {adj} {loc}'
               
            else:
               sentence = f'Our {Mnoun} {verb} the {adj} {per}'
         else:
            sentence = f'Our {Mnoun} {verb} your {adj} {noun2}'
       else:
          if lp == 2:
            adj = random.choice(adjs_p)
          elif Snoun in person:
            adj = random.choice(adjs_p)
          else:
            adj = random.choice(adjs_l)
          if verb in ["runs to", "swims to", "played near", "drived to", "flyed away from", "climbs towards to", "travels to","moves toward", "rotates in the dirction of", "floats next to"]:
            lp = random.randint(1, 2)
            loc = random.choice(location)
            per = random.choice(person)
            if (lp == 1):
               sentence = f'Our {Mnoun} {verb} the {adj} {loc}'
            else:
               sentence = f'Our {Mnoun} {verb} the {adj} {per}'
          else:
            verb = random.choice(a_verbs)
            sentence = f'Our {Mnoun} {verb} your {adj} {Snoun}'
       sentences.append(sentence)
   return sentences

def create_sentences00(nouns,verbs,adjs,connect,location,Mnoun,Snoun,Fnoun):
   sentences = []
   for _ in range(1):
       noun1 = Mnoun
       lp = 0
       if noun1 in person:
          verb = random.choice(p_verbs)
       else:
          verb = random.choice(o_verbs)
       if noun1 in a_person:
          aes = "an"
       else:
          aes = "a"
       if verb in a_verbs:
          noun2 = random.choice(object)
       elif verb in b_verbs:
          noun2 = random.choice(person)
       else:
          noun2 = random.choice(nouns)
       if Fnoun in person:
          verb1 = random.choice(p_verbs)
       else:
          verb1 = random.choice(o_verbs)
       if verb1 in a_verbs:
          noun3 = random.choice(object)
       elif verb1 in b_verbs:
          noun3 = random.choice(person)
       else:
          noun3 = random.choice(nouns)
       if lp == 2:
         adj = random.choice(adjs_p)
       elif Fnoun in object:
         adj = random.choice(adjs_o)
       elif Fnoun in person:
         adj = random.choice(adjs_p)
       else:
         adj = random.choice(adjs_l)
       if lp == 2:
         adj1 = random.choice(adjs_p)
       elif Fnoun in object:
         adj1 = random.choice(adjs_o)
       elif Fnoun in person:
         adj1 = random.choice(adjs_p)
       else:
         adj1 = random.choice(adjs_l)
       if adj in a_person:
          aes1 = "an"
       else:
          aes1 = "a"
       connect0 = random.choice(connect)
       if Snoun == 0:
         if verb in ["runs to", "swims to", "played near", "drived to", "flyed away from", "climbs towards to", "travels to","moves toward", "rotates in the dirction of", "floats next to"]:
            lp = random.randint(1, 2)
            loc = random.choice(location)
            per = random.choice(person)
            if verb1 in ["runs to", "swims to", "played near", "drived to", "flyed away from", "climbs towards to", "travels to","moves toward", "rotates in the dirction of", "floats next to"]:
               if (lp == 1):
                  sentence = f'{aes} {Mnoun} {verb} {aes1} {adj} {loc} {connect0} the {adj1} {Fnoun} {verb1} the {loc}'
               else:
                  sentence = f'{aes} {Mnoun} {verb} {aes1} {adj} {per} {connect0} the {adj1} {Fnoun} {verb1} the {per}'
            else:
               verb1 = random.choice(p_p_verbs)
               if (lp == 1):
                  sentence = f'{aes} {Mnoun} {verb} {aes1} {adj} {loc} {connect0} the {adj1} {Fnoun} {verb1} the {Mnoun}'
               else:
                  sentence = f'{aes} {Mnoun} {verb} {aes1} {adj} {per} {connect0} the {adj1} {Fnoun} {verb1} the {Mnoun}'
         else:
            noun1 = Fnoun
            if noun1 in person:
               verb = random.choice(p_verbs)
            else:
               verb = random.choice(o_verbs)
            if noun1 in a_person:
               aes = "an"
            else:
               aes = "a"
            if Mnoun in person:
               verb1 = random.choice(b_verbs)
            else:
               verb1 = random.choice(a_verbs)
            if verb1 in p_verbs:
               noun2 = random.choice(person)
            else:
               noun2 = random.choice(object)
            if Mnoun in object:
               adj = random.choice(adjs_o)
            elif Mnoun in person:
               adj = random.choice(adjs_p)
            else:
               adj = random.choice(adjs_l)
            if noun2 in object:
               adj1 = random.choice(adjs_o)
            elif noun2 in person:
               adj1 = random.choice(adjs_p)
            else:
               adj1 = random.choice(adjs_l)
            if adj in a_person:
               aes1 = "an"
            else:
               aes1 = "a"
            verb = random.choice(p_p_verbs)
            sentence = f'{aes} {Fnoun} {verb} {aes1} {adj} {Mnoun} {connect0} the {adj1} {noun2} {verb1} the {Mnoun}'
       else:
         if verb in ["runs to", "swims to", "played near", "drived to", "flyed away from", "climbs towards to", "travels to","moves toward", "rotates in the dirction of", "floats next to"]:
            noun1 = Fnoun
            if noun1 in a_person:
               aes = "an"
            else:
               aes = "a"
            if Mnoun in person:
               verb1 = random.choice(b_verbs)
            else:
               verb1 = random.choice(a_verbs)
            if verb1 in p_verbs:
               noun1 = random.choice(person)
            else:
               noun1 = random.choice(object)
            if Mnoun in object:
               adj = random.choice(adjs_o)
            elif Mnoun in person:
               adj = random.choice(adjs_p)
            else:
               adj = random.choice(adjs_l)
            if noun1 in object:
               adj1 = random.choice(adjs_o)
            elif noun1 in person:
               adj1 = random.choice(adjs_p)
            else:
               adj1 = random.choice(adjs_l)
            if adj in a_person:
               aes1 = "an"
            else:
               aes1 = "a"
            lp = random.randint(1, 2)
            loc = random.choice(location)
            per = random.choice(person)
            if verb1 in ["runs to", "swims to", "played near", "drived to", "flyed away from", "climbs towards to", "travels to","moves toward", "rotates in the dirction of", "floats next to"]:
               if (lp == 1):
                  sentence = f'{aes} {Fnoun} {verb} {aes1} {adj} {loc} {connect0} the {adj1} {Fnoun} {verb1} the {loc}'
               else:
                  sentence = f'{aes} {Fnoun} {verb} {aes1} {adj} {per} {connect0} the {adj1} {Fnoun} {verb1} the {per}'
            else:
               verb1 = random.choice(p_p_verbs)
               if (lp == 1):
                  sentence = f'{aes} {Fnoun} {verb} {aes1} {adj} {loc} {connect0} the {adj1} {Fnoun} {verb1} the {Mnoun}'
               else:
                  sentence = f'{aes} {Fnoun} {verb} {aes1} {adj} {per} {connect0} the {adj1} {Fnoun} {verb1} the {Mnoun}'
         else:
            noun1 = Mnoun
            if noun1 in person:
               verb = random.choice(p_verbs)
            else:
               verb = random.choice(o_verbs)
            if noun1 in a_person:
               aes = "an"
            else:
               aes = "a"
            if Fnoun in person:
               verb1 = random.choice(b_verbs)
            else:
               verb1 = random.choice(a_verbs)
            if verb1 in p_verbs:
               noun2 = random.choice(person)
            else:
               noun2 = random.choice(object)
            if Snoun in object:
               adj = random.choice(adjs_o)
            elif Snoun in person:
               adj = random.choice(adjs_p)
            else:
               adj = random.choice(adjs_l)
            if noun2 in object:
               adj1 = random.choice(adjs_o)
            elif noun2 in person:
               adj1 = random.choice(adjs_p)
            else:
               adj1 = random.choice(adjs_l)
            verb = random.choice(a_verbs)
            sentence = f'{aes} {Mnoun} {verb} {aes1} {adj} {Snoun} {connect0} the {adj1} {noun2} {verb1} the {Fnoun}'
       sentences.append(sentence)
   return sentences
def create_sentences1(nouns,verbs,adjs,connect,location,Mnoun):
   sentences = []
   for _ in range(1):
       noun1 = random.choice(nouns)
       if noun1 in person:
          verb = random.choice(p_verbs)
       else:
          verb = random.choice(o_verbs)
       if verb in a_verbs:
          noun2 = random.choice(object)
       elif verb in b_verbs:
          noun2 = random.choice(person)
       else:
          noun2 = random.choice(nouns)
       if noun1 in object:
         adj = random.choice(adjs_o)
       elif noun1 in person:
         adj = random.choice(adjs_p)
       else:
         adj = random.choice(adjs_l)
       if adj in a_person:
          aes = "an"
       else:
          aes = "a"
       if verb in ["runs to", "swims to", "played near", "drived to", "flyed away from", "climbs towards to", "travels to","moves toward", "rotates in the dirction of", "floats next to"]:
          if Mnoun in person:
            verb = random.choice(p_verbs)
          else:
            verb = random.choice(o_verbs)
          lp = random.randint(1, 2)
          loc = random.choice(location)
          per = random.choice(person)
          if (lp == 1):
            sentence = f'{aes} {adj} {Mnoun} {verb} that {loc}'
          else:
            sentence = f'{aes} {adj} {Mnoun} {verb} that {per}'
       else:
          if Mnoun in person:
            verb = random.choice(b_verbs)
          else:
            verb = random.choice(a_verbs)
          if verb in p_verbs:
            noun1 = random.choice(person)
          else:
            noun1 = random.choice(object)
          sentence = f'{aes} {adj} {noun1} {verb} that {Mnoun}'

       sentences.append(sentence)
   return sentences
def create_sentences10(nouns,verbs,adjs,connect,location,Mnoun,Snoun,Fnoun):
   sentences = []
   for _ in range(1):
       noun1 = random.choice(nouns)
       lp = 0
       if noun1 in person:
          verb = random.choice(p_verbs)
          verb1 = random.choice(p_verbs)
       else:
          verb = random.choice(o_verbs)
          verb1 = random.choice(o_verbs)
       if verb in a_verbs:
          noun2 = random.choice(object)
       elif verb in b_verbs:
          noun2 = random.choice(person)
       else:
          noun2 = random.choice(nouns)
       if lp == 1:
          if loc in a_person:
             aes = "an"
          else:
             aes = "a"
       elif lp == 2:
          if per in a_person:
             aes = "an"
          else:
             aes = "a"
       elif noun2 in a_person:
          aes = "an"
       else:
          aes = "a"
       if verb1 in a_verbs:
          noun3 = random.choice(object)
       elif verb1 in b_verbs:
          noun3 = random.choice(person)
       else:
          noun3 = random.choice(nouns) 
       if noun1 in object:
         adj = random.choice(adjs_o)
       elif noun1 in person:
         adj = random.choice(adjs_p)
       else:
         adj = random.choice(adjs_l)
       if lp == 2:
         adj1 = random.choice(adjs_p)
       elif noun3 in object:
         adj1 = random.choice(adjs_o)
       elif noun3 in person:
         adj1 = random.choice(adjs_p)
       else:
         adj1 = random.choice(adjs_l)
       connect0 = random.choice(connect)
       if Mnoun == 0:
         if verb in ["runs to", "swims to", "played near", "drived to", "flyed away from", "climbs towards to", "travels to","moves toward", "rotates in the dirction of", "floats next to"]:
            lp = random.randint(1, 2)
            loc = random.choice(location)
            per = random.choice(person)
            if verb1 in ["runs to", "swims to", "played near", "drived to", "flyed away from", "climbs towards to", "travels to","moves toward", "rotates in the dirction of", "floats next to"]:
               if (lp == 1):
                  sentence = f'The {adj} {Fnoun} {verb} {aes} {loc} {connect0} that {Fnoun} {verb1} this {adj1} {loc}'
               else:
                  sentence = f'The {adj} {Snoun} {verb} {aes} {per} {connect0} that {Snoun} {verb1} this {adj1} {per}'
            else:
               if (lp == 1):
                  verb1 = random.choice(a_verbs)
                  sentence = f'The {adj} {Fnoun} {verb} {aes} {loc} {connect0} that {Fnoun} {verb1} this {adj1} {Snoun}'
               else:
                  verb1 = random.choice(b_verbs)
                  verb = "is located near"
                  sentence = f'The {adj} {Snoun} {verb} {aes} {per} {connect0} that {Snoun} {verb1} this {adj1} {Fnoun}'

         else:
            verb1 = random.choice(a_verbs)
            sentence = f'The {adj} {Fnoun} {verb} {aes} {noun2} {connect0} that {Fnoun} {verb1} this {adj1} {Snoun}'
       else:
         if verb in ["runs to", "swims to", "played near", "drived to", "flyed away from", "climbs towards to", "travels to","moves toward", "rotates in the dirction of", "floats next to"]:
            lp = random.randint(1, 2)
            loc = random.choice(location)
            per = random.choice(person)
            if verb1 in ["runs to", "swims to", "played near", "drived to", "flyed away from", "climbs towards to", "travels to","moves toward", "rotates in the dirction of", "floats next to"]:
               if (lp == 1):
                  sentence = f'The {adj} {Fnoun} {verb} {aes} {loc} {connect0} that {Snoun} {verb1} this {adj1} {loc}'
               else:
                  sentence = f'The {adj} {Mnoun} {verb} {aes} {per} {connect0} that {Fnoun} {verb1} this {adj1} {per}'
            else:
               if (lp == 1):
                  verb1 = random.choice(p_p_verbs)
                  sentence = f'The {adj} {Snoun} {verb} {aes} {loc} {connect0} that {Mnoun} {verb1} this {adj1} {Fnoun}'
               else:
                  sentence = f'The {adj} {noun1} {verb} {aes} {per} {connect0} that {Fnoun} {verb1} this {adj1} {noun3}'

         else:
            verb = random.choice(a_verbs)
            sentence = f'The {adj} {Mnoun} {verb} {aes} {Snoun} {connect0} that {noun1} {verb1} this {adj1} {Fnoun}'

       sentences.append(sentence)
   return sentences


#  topic SCHOOL
S_nouns = [
    "principal", "custodian", "librarian", "coach", "nurse",
    "janitor", "bus driver", "security guard", "parent", "tutor",
    "guidance counselor", "receptionist", "substitute teacher", "classmate", "volunteer",
    "lunch lady", "crossing guard", "school nurse", "teacher's assistant", "coach", "whiteboard", "calculator", "backpack", "computer", "projector",
    "microscope", "globe", "textbook", "map", "laptop",
    "highlighter", "eraser", "scissors", "ruler", "pen",
    "chair", "desk lamp", "dictionary", "notebook", "protractor"
]

S_verbs = [
    "teaches", "learns", "studies", "reads", "writes",
    "solves", "listens", "discuss", "presents", "questions",
    "grades", "attends", "participates", "prepares", "explains",
    "researches", "collaborates", "reviewes", "analyzes", "discoveres"
]

S_verbs1 = [
    "teaching", "learning", "studying", "reading", "writing",
    "solving", "listening", "discussv", "presenting", "questioning",
    "participating", "prepareîng", "explaining",
    "researching", "reviewing", "analyzing", "discovering"
]

S_locations = [
    "school", "classroom", "library", "cafeteria", "playground",
    "office", "gymnasium", "auditorium", "laboratory", "hallway"
]

S_adjectives = [
    "knowledgeable", "curious", "enthusiastic", "creative", "disciplined",
    "organized", "interactive", "inspiring", "challenging", "educational",
    "motivated", "friendly", "supportive", "innovative", "collaborative"
]

S_connections = [
    "after that", "then", "surprisingly", "meanwhile", "eventually",
    "subsequently", "simultaneously", "consequently", "nevertheless", "however",
    "furthermore", "moreover", "in addition", "in contrast", "hence",
    "as a result", "for instance", "on the other hand", "in conclusion", "to sum up"
]

S_objects = [
    "whiteboard", "calculator", "backpack", "computer", "projector",
    "microscope", "globe", "textbook", "map", "laptop",
    "highlighter", "eraser", "scissors", "ruler", "pen",
    "chair", "desk lamp", "dictionary", "notebook", "protractor"
]

S_persons = [
    "principal", "custodian", "librarian", "coach", "nurse",
    "janitor", "bus driver", "security guard", "parent", "tutor",
    "guidance counselor", "receptionist", "substitute teacher", "classmate", "volunteer",
    "lunch lady", "crossing guard", "school nurse", "teacher's assistant", "coach"
]

S_subjects = [
    "mathematics", "science", "history", "english", "art",
    "physical education", "music", "geography", "chemistry", "biology",
    "literature", "algebra", "physics", "social studies", "foreign language",
    "computer science", "economics", "psychology", "sociology", "philosophy"
]

S_names = [
    "Emily", "Alex", "Ryan", "Olivia", "Ethan",
    "Sophia", "Jacob", "Ava", "Matthew", "Isabella",
    "Daniel", "Mia", "Christopher", "Emma", "Andrew",
    "Madison", "Joshua", "Abigail", "Nathan", "Chloe"
]

S_weeknames = [
    "monday", "tuesday", "wednesday", "thursday", "friday"
]

S_responds = [
    "Of course!", "You are right!", "No response...", "Go away!!", "No, leave me alone!"
]

S_questions = [
    "Have you ever been a class representative?",
    "Do you enjoy participating in school sports?",
    "Have you ever won an award for your academic achievements?",
    "Is science your favorite subject?",
    "Have you ever been part of a school play or performance?",
    "Are you involved in any after-school clubs?",
    "Do you prefer studying alone?",
    "Have you ever been elected as a student council member?",
    "Is your favorite part of school the social aspect?",
    "Have you ever volunteered for a school event or project?"
]

def create_introduction(nouns, adjs, connect, location, MMnoun, Mnoun,Snoun, Fnoun):
    introduction = []
    coin = random.randint(1, 11)
    if coin == 1:
      for _ in range(1):
         per = random.choice(S_persons)
         adj = random.choice(adjs_p)
         loc = random.choice(location)
         sentence = f'I am a {Mnoun} and currently I am very {adj}. I know {Snoun}, the {per}, very well. {Snoun} said: - {MMnoun}!'
         introduction.append(sentence)
    elif coin == 2:
      for _ in range(1):
         per = random.choice(S_persons)
         adj = random.choice(adjs_p)
         verb = random.choice(S_verbs)
         loc = random.choice(location)
         sentence = f'As an {Mnoun}, my curiosity knows no bounds. My close companion, {Snoun}, the {per}, often {verb} intriguing stories. {Snoun} once remarked: - {MMnoun}!'
         introduction.append(sentence)
    elif coin == 3:
      for _ in range(1):
         per = random.choice(S_persons)
         adj = random.choice(adjs_p)
         loc = random.choice(location)
         sentence = f'Engrossed in {loc}, I, an avid {Mnoun}, seek answers. A {adj}, {Snoun}, the {per}, often divulges fascinating facts. {Snoun} once disclosed: - {MMnoun}!'
         introduction.append(sentence)
    elif coin == 4:
      for _ in range(1):
         per = random.choice(S_persons)
         adj = random.choice(adjs_p)
         loc = random.choice(location)
         sentence = f'Within the scholarly domain, my passion ignites. I as a {Mnoun} have a confederate, {Snoun}, the {per}, frequently unveils groundbreaking discoveries. {Snoun} once conveyed: - {MMnoun}!'
         introduction.append(sentence)
    elif coin == 5:
      for _ in range(1):
         per = random.choice(S_persons)
         adj = random.choice(adjs_p)
         loc = random.choice(location)
         sentence = f'Dedicated to intellectual endeavors, I as a {Mnoun}, am a seeker of insights. A dear friend, {Snoun}, the {per}, often shares captivating anecdotes. {Snoun} once narrated: - {MMnoun}!'
         introduction.append(sentence)
    elif coin == 6:
      for _ in range(1):
         per = random.choice(S_persons)
         adj = random.choice(adjs_p)
         loc = random.choice(location)
         sentence = f'Immersed in the world of academia, my inquisitiveness knows no bounds. I think therefore I am a {Mnoun}. My comrade, {Snoun}, the {per}, often imparts celestial revelations. {Snoun} once uttered: - {MMnoun}!'
         introduction.append(sentence)
    elif coin == 7:
      for _ in range(1):
         per = random.choice(S_persons)
         adj = random.choice(adjs_p)
         loc = random.choice(location)
         sentence = f'In the pursuit of knowledge, I as a {Mnoun},stand resolute. My companion, {Snoun}, the {per}, frequently chronicles riveting tales. {Snoun} once stated: - {MMnoun}!'
         introduction.append(sentence)
    elif coin == 8:
      for _ in range(1):
         per = random.choice(S_persons)
         adj = random.choice(adjs_p)
         loc = random.choice(location)
         sentence = f'Within the scholarly sphere, my enthusiasm propels me forward. I know as a {Mnoun} know a colleague, {Snoun}, the {per}, who often unfolds the wonders of nature. {Snoun} once voiced: - {MMnoun}!'
         introduction.append(sentence)
    elif coin == 9:
      for _ in range(1):
         per = random.choice(S_persons)
         adj = random.choice(adjs_p)
         loc = random.choice(location)
         sentence = f'Embracing the quest for wisdom, I as a {Mnoun},navigate the academic landscape. A close friend, {Snoun}, the {per}, shares profound scientific insights. {Snoun} once expressed: - {MMnoun}!'
         introduction.append(sentence)
    elif coin == 10:
      for _ in range(1):
         per = random.choice(S_persons)
         adj = random.choice(adjs_p)
         loc = random.choice(location)
         sentence = f'As a {adj} {Mnoun}, my intellectual fervor guides my journey. A friend, {Snoun}, the {per}, unveils ancient mysteries. {Snoun} once shared: - {MMnoun}!'
         introduction.append(sentence) 
    else:
       for _ in range(1):
         per = random.choice(S_persons)
         adj = random.choice(adjs_o)
         loc = random.choice(location)
         day = random.choice(S_weeknames).capitalize()
         sentence = f'Today is {day}, my name is {MMnoun} and I am working as a {Mnoun}, one day I discovered the {adj} {per} in the {loc}. I said: - {Snoun}!'
         introduction.append(sentence)
    return introduction

def create_conflict(nouns, verbs, adjs, connect, location, MMnoun, Mnoun,Snoun, Fnoun):
    conflict = []
    coin = random.randint(1, 4)
    if coin == 1:
      for _ in range(1):
         verb = random.choice(S_verbs1)
         sub = random.choice(S_subjects)
         adj = random.choice(adjs_o)
         res = random.choice(S_responds)
         sentence = f'I am {verb} something... But did you knew the {adj} {Fnoun} is secretly teaching {sub} - {res} '
         conflict.append(sentence)
    elif coin == 2 or coin == 3:
      for _ in range(1):
         verb = random.choice(S_verbs1)
         sub = random.choice(S_subjects)
         adj = random.choice(adjs_o)
         res = random.choice(S_responds)
         ques = random.choice(S_questions)
         sentence = f'The {adj} {Fnoun} {verb} {sub}. Who cares, right? {ques} - {res} '
         conflict.append(sentence)
    else:
       for _ in range(1):
         verb = random.choice(S_verbs1)
         sub = random.choice(S_subjects)
         adj = random.choice(adjs_o)
         per = random.choice(S_persons)
         res = random.choice(S_responds)
         sentence = f'We are {verb} something new everyday. As also a {per}, I observed that you and that {adj} {Fnoun} are hiding something behind my back! - {res} '
         conflict.append(sentence)
    return conflict


def create_norm(nouns, verbs, adjs, connect, location, MMnoun, Mnoun,Snoun, Fnoun):
    norm = []
    r=1
    s = random.randint(4, 8)
    for _ in range(s):
       coin = random.randint(1, 4)
       lp = random.randint(1, 2)
       if coin == 1:
         for _ in range(r):
            if Mnoun in person:
               verb = random.choice(p_verbs)
            else:
               verb = random.choice(o_verbs)
            if verb in a_verbs:
               noun2 = random.choice(S_objects)
            elif verb in b_verbs:
               noun2 = random.choice(person)
            else:
               noun2 = random.choice(nouns)
            if lp == 2:
               adj = random.choice(adjs_p)
            elif noun2 in object:
               adj = random.choice(adjs_o)
            elif noun2 in person:
               adj = random.choice(adjs_p)
            else:
               adj = random.choice(adjs_l)
            if lp == 1:
               sentence = f'Our {MMnoun} {verb} your {adj} {noun2}.'
            else:
               sentence = f'Our {MMnoun} {verb} your {adj} {Snoun}.'
         norm.append(sentence)
       elif coin == 2:
         for _ in range(r):
            verb = random.choice(S_verbs)
            sub = random.choice(S_subjects)
            adj = random.choice(adjs_p)
            noun2 = random.choice(S_nouns)
            if noun2 in S_objects:
               adj1 = random.choice(adjs_o)
               verb1 = random.choice(b_verbs)
            else:
               adj1 = random.choice(adjs_p)
               verb1 = random.choice(p_p_verbs)
            res = random.choice(S_responds)
            connect0 = random.choice(connect)
            sentence = f'{MMnoun} {verb} {adj} {Snoun} {connect0} the {adj1} {noun2} {verb1} the {Fnoun}.'
            norm.append(sentence)
       elif coin == 10:
         for _ in range(r):
            sentence = f'ERRROROROROORORORO.'
            norm.append(sentence)
       else:
         for _ in range(r):
            verb = random.choice(S_verbs1)
            sub = random.choice(S_subjects)
            per = random.choice(S_persons)
            res = random.choice(S_responds)
            if MMnoun in S_names:
               verb = random.choice(b_verbs)
            else:
               verb = random.choice(a_verbs)
            if verb in p_verbs:
               noun1 = random.choice(S_persons)
               adj = random.choice(adjs_p)
            else:
               noun1 = random.choice(S_objects)
               adj = random.choice(adjs_o)
            sentence = f'A {adj} {noun1} {verb} {MMnoun}.'
            norm.append(sentence)
    return norm

def create_desc(nouns, verbs, adjs, connect, location, MMnoun, Mnoun,Snoun, Fnoun):
    desc = []
    coin = random.randint(1, 3)
    if coin == 1:
      for _ in range(1):
         verb = random.choice(S_verbs1)
         loc = random.choice(S_locations)
         o = random.choice(S_objects) 
         o1 = random.choice(S_objects)
         adj = random.choice(adjs_l)
         adj1 = random.choice(adjs_l)
         adj2 = random.choice(adjs_l)
         adj3 = random.choice(adjs_l)
         res = random.choice(S_responds)
         sentence = f'I am in a {adj} {loc}, as the {adj1} {o} was next to a {adj2} {o1}, everything seemed {adj3} in the {loc}.'
         desc.append(sentence)
    if coin == 2:
      for _ in range(1):
         verb = random.choice(b_verbs)
         loc = random.choice(S_locations)
         noun = random.choice(S_persons)
         o = random.choice(S_objects)
         o1 = random.choice(S_objects)
         adj = random.choice(adjs_l)
         adj1 = random.choice(adjs_o)
         adj2 = random.choice(adjs_l)
         adj3 = random.choice(adjs_l)
         res = random.choice(S_responds)
         sentence = f'The {adj} {loc} echoes with children"s laughter. Swings, slides, and the{adj1} {o} {verb} {noun}.'
         desc.append(sentence)
    else:
       for _ in range(1):
         verb = random.choice(S_verbs1)
         noun = random.choice(S_persons)
         o = random.choice(S_objects)
         o1 = random.choice(S_objects)
         adj = random.choice(adjs_l)
         adj1 = random.choice(adjs_o)
         adj2 = random.choice(adjs_o)
         adj3 = random.choice(adjs_o)
         loc = random.choice(S_locations)
         sentence = f'The {loc}, a {adj} haven in our school, is filled with neatly arranged shelves of {adj1} {o}. A {adj2} lighting creates a {adj3} ambiance, and the {noun} guides seekers in their quests.'
         desc.append(sentence)
    return desc
# sentence = f'as the {Mnoun} {verb} the {adj} {Snoun}, a {Fnoun} entered the scene.'
def create_ending(nouns, verbs, adjs, connect, location, MMnoun, Mnoun,Snoun, Fnoun):
    ending = []
    for _ in range(1):
        Snoun = random.choice(S_objects)
        Fnoun = random.choice(S_persons)
        adj = random.choice(adjs_p)
        adj1 = random.choice(adjs_o)
        verb = random.choice(a_verbs)
        sentence = f'In the end, the {adj} {MMnoun} and the {adj} {Fnoun} {verb} the {adj1} {Snoun}.'
        ending.append(sentence)

    return ending

def main():
    print(f'Here are potential sentences for a mystery story:')
    Mnoun = random.choice(S_persons)
    Fnoun = random.choice(S_persons)
    MMnoun = random.choice(S_names).capitalize()
    Snoun = random.choice(S_names).capitalize()
    introductions = create_introduction(nouns, adjs, connect, location, MMnoun, Mnoun,Snoun, Fnoun)
    conflicts = create_conflict(nouns, verbs, adjs, connect, location, MMnoun, Mnoun,Snoun, Fnoun)
    endings = create_ending(nouns, verbs, adjs, connect, location, MMnoun, Mnoun,Snoun, Fnoun)
    descrip = create_desc(nouns, verbs, adjs, connect, location, MMnoun, Mnoun,Snoun, Fnoun)
    nor = create_norm(nouns, verbs, adjs, connect, location, MMnoun, Mnoun,Snoun, Fnoun)
    mid_sentences = nor + descrip
    random.shuffle(mid_sentences)
    story_sentences = introductions + conflicts + mid_sentences + endings
    for sentence in story_sentences:
        print(f'{sentence} ', end='')

main()

# sentence = f'{TextStyle.M_YELLOW}{sentence.capitalize()} {TextStyle.RESET}'