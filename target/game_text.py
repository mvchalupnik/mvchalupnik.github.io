from physics_elements import Final, Question, PhysicsClass, Lab, Ending, LabScenario, Choice

"""
game_text.py
Contains text and some instantiated classes used in the game play of Becoming Physics
"""

# LabTypes
BIG_STUFF = 2
SMALL_STUFF = 1
BOTH = 0
NONE = -1

# Grades
A = 0
B = 1
C = 2
D = 3

# Texts
INTRO_TEXT = "Do you want to become physics?????\n"

REGISTER_TEXT = "There are many physics classes you can take. Unfortunately, "\
               "since you are a beginning student, you can only register for "\
               "the beginning classes. You can register for as many classes as you want, "\
               "but whichever classes you register for, you will have to take finals for at "\
               "the end of the quarter. Which classes would you like to register for?"

JOIN_TEXT = "What kind of lab do you want to join? Do you want to study Big Stuff, "\
            "like astronomy and cosmology, \nEveryday Stuff, or Small Stuff, like "\
            "particle physics and atomic physics?"

CHOOSE_CLASS_TEXT = "Which class do you want to go to?"


# Physics Lectures
COOL_PHYSICS_LECTURES = [
    {
        "lecture": "Today we're going to DERIVE Snell's Law from electrodynamics! "
        "We will only get halfway through the derivation today.",
        "image_location": "/pics/snelllaw1.png",
    },
    {
        "lecture": "Today we finish our derivation of Snell's Law! As an added bonus, we get the Law "
        "of Reflection also. Yay physics!!!!!!",
        "image_location": "pics/snellpart22.png",
    },
    {
        "lecture": "What is the electric potential of a dipole? Let's figure it out from the defition "
        "of electric potential, binomial expansions, and law of cosines! Yay!!!!!",
        "image_location": "pics/griffithsdipole.png",
    },
    {
        "lecture": "What is the energy stored in an electric field? We can figure it out through logic "
        "and math!!! Yay physics!!!!",
        "image_location": "pics/electroenergy.png",
    },
]

BORING_PHYSICS_LECTURES = [
    {
        "lecture": "Here is the law of reflection. Nobody knows where it comes from. Here is how you "
        "solve problems involving the law of reflection.",
        "image_location": "pics/reflectionlawboring.png",
    },
    {
        "lecture": "Here is Snell's Law. It is an experimental law. It cannot be derived. Here is how "
        "you solve problems involving Snell's Law.",
        "image_location": "pics/boringsnelllaw.png",
    },
    {
        "lecture": "What is the electric potential of a dipole? Here is the equation. You can "
        "memorize the equation and use it to put numbers in and get numbers out. ",
        "image_location": "pics/dipoleboring.png",
    },
    {
        "lecture": "What is the energy stored in an electric field? It is this equation. "
        "You can put in numbers for E and e0 and 2 and do math on the numbers and get "
        "another number and that number is a number and you can put that number into "
        "another number and then it will be a number with a number.....",
        "image_location": "pics/workenergyboring.png",
    },
]

FAKE_PHYSICS_LECTURES = [
    {
        "lecture": "Today we're going to learn about magenetism. Magnetism was discovered by the "
        "great scientist Rene Descartes. His theories led to the development of Maxwell's "
        "equations.",
        "image_location": "pics/bigdescartes2.png",
    },
    {
        "lecture": "Today we're going to learn about Quantum Physics.",
        "image_location": "pics/sciencereligion2.png",
    },
    {
        "lecture": "Today we're going to learn about how mass and electromagnetism are related.",
        "image_location": "pics/yourlegalaction.png",
    },
]

MATH_PHYSICS_LECTURES = [
    {"lecture": ":-/ ", "image_location": "pics/sadimaginary.png"},
    {"lecture": ":-(", "image_location": "pics/saddiffeqmodified.png"},
    {"lecture": ":,-(", "image_location": "pics/saderff.png"},
    {"lecture": ":,,,,,,,-(", "image_location": "pics/sadwahhmath.png"},
]

OCHEM_LECTURES = [
    {
        "lecture": "Here are some reactions. These reactions have mechanisms that are part logical "
        "and part arbitrary. You will probably need to memorize the reagents. But that's ok, "
        "it's not like there are whole other classes of reactions",
        "image_location": "pics/alkynestuffs2.png",
    },
    {
        "lecture": "Lol jk there actually are many other classes of reactions. Here are some with alkynes. "
        "(Don't forget alcohols and aldehydes and esters and ethers and...)",
        "image_location": "pics/alkenestuffs2.png",
    },
    {
        "lecture": "NMR can be used to identify chemicals. We're going to memorize the positions of NMR peaks. ",
        "image_location": "pics/nmrstuffs2.png",
    },
    {
        "lecture": "Here are some more arbitrary things to memorize.",
        "image_location": "pics/couplingconstants.png",
    },
    {"lecture": "Here are some PKAs to memorize.", "image_location": "pics/pkas.png"},
]

# Finals
COOL_FINAL = Final(
    physics_class="Cool Physics",
    questions=[
        Question(
            question_text="A photon checks into a hotel. The bellhop asks, 'Can I help you with your luggage?'"
            " What does the photon say?",
            answers=["A. Yes, please do.", "B. No thanks, I'm super good at carrying things.","C. That's offensive. ","D. I don't have any, I'm travelling light."],
            correct_answer=D,
        ),
        Question(
            question_text="A neutron walked into a bar and asked 'How much for a drink?' What did the bartender"
            " reply?",
            answers=["A. $5", "B. For you, no charge", "C. 5 Coulombs", "D. 5 e"],
            correct_answer=B,
        ),
        Question(
            question_text="Two atoms are walking down the street. One says to the other, 'Hey, I think I lost an "
            "electron!' The other says, 'Are you sure?' What does the first one reply?",
            answers=["A. Yes, I'm positive!", "B. No, you can never be 100 percent sure about anything in life", "C. No, I'm neutral!","D. Yes, I'm negatively sure!"],
            correct_answer=A,
        ),
    ],
)
BORING_FINAL = Final(
    physics_class="Boring Physics",
    questions=[
        Question(
            question_text="F = MA. If M = 5 kg and a = 20 m/s, what is F?",
            answers=["A. 4 Newtons","B. 100 Newtons","C. 200 Newtons","D. This is so boring."],
            correct_answer=D,
        ),
        Question(
            question_text="If I can travel 100 miles in 40 seconds, how many miles can I travel in 20 seconds?",
            answers=["A. 0 miles because I'm tired now.", "B. Unrealistic speeds. No one can travel that fast.", "C. 50 miles","D. 40 miles"],
            correct_answer=B,
        ),
        Question(
            question_text="N is a number. E(N) is an equation that gives some other number you want to know. "
            "What is the other number you want to know?",
            answers=["A. N", "B. N(E)", "C. E(N)", "D. I am asleep right now"],
            correct_answer=D,
        ),
    ],
)
FAKE_FINAL = Final(
    physics_class="Controversial Physics",
    questions=[
        Question(
            question_text="Light is electromagnetic radiation. It travels through the ether, even though "
            "we have not detected ether yet. Why have we not detected ether yet?",
            answers=["A. Ether doesn't exist", "B. We don't have sensitive enough intruments but we will find it someday", "C. Special relativity means that ether exists but is impossible to detect","D. Ether travels at the speed of light, so it is too fast to detect."],
            correct_answer=B,
        ),
        Question(
            question_text="Which field is objectively the best field?",
            answers=["A. Biology", "B. Chemistry", "C. Physics", "D. Math"],
            correct_answer=C,
        ),
        Question(
            question_text="The Bohr model is an early model of atomic structure that was later shown to be bad. "
            "What is the best reason for why it is bad?",
            answers=["A. Quantum physics means the Heisenberg Uncertainty principle which is wave particle "
            "duality \nand quantum mechanics to be of itself", "B. Actually the Bohr model is correct", "C. Because it's BOHRING HAHAHAHAHAHAHAHAHAHHAH sorry I'll never \ntry to make a joke ever again.", "D. If the Bohr model were accurate, that would mean that electrons "\
            "were \nplanets orbiting nuclei which were suns and little tiny people lived in those planets, "
            "\nbut we already know there are only 8 million people on Earth, and \nthere's several hundreds "
            "of atoms on Earth, so that means there can't be any more people."],
            correct_answer=B,
        ),
    ],
)
MATH_FINAL = Final(
    physics_class="Math Physics",
    questions=[
        Question(
            question_text=" :( ",
            answers=["A. :( ", "B. :, (", "C. :,,,,(", "D. :/"],
            correct_answer=A,
        ),
        Question(
            question_text="X = ?",
            answers=["A. 1", "B. 2", "C. 3", "4. -100000"],
            correct_answer=A,
        ),
        Question(
            question_text="math = ?",
            answers=["A. Mad - d + th", "B. Sad - d + th", "C. Bad - d + th", "D. Rad - d + th"],
            correct_answer=A,
        ),
    ],
)
OCHEM_FINAL = Final(
    physics_class="Organic Chemistry",
    questions=[
        Question(
            question_text="Which reagents will take you from an alkyne to an antimarkovnikov brominated alkene? "
            "Please also draw the mechanism.",
            answers=["A. Br_2", "B. HBr and H_2O_2", "C. Lindlar's catalyst", "D. NaBr, H_2O"],
            correct_answer=B,
        ),
        Question(
            question_text="Order these hydrogens in order of NMR delta shift, from lower shift to higher shift. "
            "(Hint: hydrogens that are more delta shifted tend to be attached to electronegative atoms "
            "since they are more deshielded from the magnetic field. However, there are exceptions. The "
            "exceptions are justified by rules that are arbitrarily made up to fit the exceptions.)",
            answers=["A. carboxylic acid hydrogen, hydrogen on a phenyl, hydrogen on a phenol, hydrogen on an "
            "alkane carbon", "B. hydrogen on an alkane carbon,  hydrogen on a phenyl, hydrogen on a phenol,"
            " carboxylic acid hydrogen", "C. hydrogen on an alkane carbon, hydrogen on a phenol, hydrogen"
            " on a phenyl, carboxylic acid hydrogen", "D. hydrogen on an alkane carbon, hydrogen on a phenyl,"
            " carboxylic acid hydrogen, hydrogen on a phenol"],
            correct_answer=B,
        ),
        Question(
            question_text="Order the hydrogens by PKAs, low to high. (Hint: PKA is defined as the - "
            "log of the concentration of H+ divided by the concentration of the conjugate base "
            "at equilibrium. Strong acids tend to have lower PKAs. Acidity depends on the "
            "electronegativity of the atom the hydrogen is attached to, resonance, orbital effects, "
            "and ultimately, memorization.)",
            answers=["A. diketone, phenol, carboxylic acid, hydrogen on a carbon connected to two nitriles", "B. carboxylic acid, phenol, hydrogen on a carbon connected to two nitriles, diketone", "C. carboxylic acid, diketone, phenol, hydrogen on a carbon connected to two nitriles ","D. carboxylic acid, phenol, diketone, hydrogen on a carbon connected to two nitriles "],
            correct_answer=C,
        ),
    ],
)

# Create classes and put them into a class list
ALL_CLASSES = [
    PhysicsClass(
        physics_class_name="Cool Physics",
        happiness=15,
        knowledge=15,
        day=0,
        lectures=COOL_PHYSICS_LECTURES,
        final=COOL_FINAL,
    ),
    PhysicsClass(
        physics_class_name="Boring Physics",
        happiness=-15,
        knowledge=5,
        day=0,
        lectures=BORING_PHYSICS_LECTURES,
        final=BORING_FINAL,
    ),
    PhysicsClass(
        physics_class_name="Fake Physics",
        happiness=-5,
        knowledge=5,
        day=0,
        lectures=FAKE_PHYSICS_LECTURES,
        final=FAKE_FINAL,
    ),
    PhysicsClass(
        physics_class_name="Math Physics",
        happiness=-20,
        knowledge=20,
        day=0,
        lectures=MATH_PHYSICS_LECTURES,
        final=MATH_FINAL,
    ),
    PhysicsClass(
        physics_class_name="Organic Chemistry",
        happiness=-15,
        knowledge=-5,
        day=0,
        lectures=OCHEM_LECTURES,
        final=OCHEM_FINAL,
    ),
]


### Labs
ALL_LABS = [
    Lab(lab_name="Big Stuff", lab_category=BIG_STUFF),
    Lab(lab_name="Medium-Sized Stuff", lab_category=NONE),
    Lab(lab_name="Small Stuff", lab_category=SMALL_STUFF),
]

# List of lab scenarios
lab_scenarios = [
    LabScenario(
        scenario="You didn't get enough sleep the night before. How to try to stay awake? Should you list all "
        "of the Real Housewives of Beverly Hills in your head that you can remember, or list all of "
        "the scientists in your head that you can think of?",
        choice1=Choice(
            choice_text="Real Housewives",
            happiness=20,
            knowledge=0,
            research=20,
            effect_text="Lisa Rinna...Lisa Vanderpump... Eileen Davidson... Kyle Richards... Kim Richards... "
            "You stay awake",
        ),
        choice2=Choice(
            choice_text="Scientists",
            happiness=-5,
            knowledge=0,
            research=5,
            effect_text="You fall asleep",
        ),
        lab_category=BOTH,
        has_been_displayed=False,
        sibling=1,
    ),
    LabScenario(
        scenario="You didn't get enough sleep the night before. How to try to stay awake? Should you list all of "
        "the Real Housewives of Beverly Hills in your head that you can remember, or list all of the "
        "scientists in your head that you can think of?",
        choice1=Choice(
            choice_text="Real Housewives",
            happiness=-5,
            knowledge=0,
            research=5,
            effect_text="You fall asleep",
        ),
        choice2=Choice(
            choice_text="Scientists",
            happiness=5,
            knowledge=0,
            research=20,
            effect_text="You stay awake",
        ),
        lab_category=BOTH,
        has_been_displayed=False,
        sibling=0,
    ),
    LabScenario(
        scenario="You are cold because you work in the basement of a basement. You have an extra sweater "
        "and a winter coat you can but on. But, thinking about it, maybe you should just tough it out?",
        choice1=Choice(
            choice_text="Wear extra sweater and coat",
            happiness=20,
            knowledge=10,
            research=10,
            effect_text="Good choice. You are much warmer now and are able to think more clearly.",
        ),
        choice2=Choice(
            choice_text="Tough it out",
            happiness=-60,
            knowledge=-10,
            research=-20,
            effect_text="You decide to not put on your coat or extra sweater and "
            "just tough it out. This was not a good idea. Two hours later, you reach the stage of "
            "hypothermia where cold feels warm, and you begin paradoxical undressing. This is not good "
            "to do in a place of research. You lose a lot of research points and happiness.",
        ),
        lab_category=BOTH,
        has_been_displayed=False,
        sibling=-1,
    ),
    LabScenario(
        scenario="How hard to work today?",
        choice1=Choice(
            choice_text="Really hard!",
            happiness=10,
            knowledge=10,
            research=10,
            effect_text="Good!",
        ),
        choice2=Choice(
            choice_text="Really really hard!",
            happiness=-20,
            knowledge=-20,
            research=0,
            effect_text="You pass out from exhaustion, and accidentally hit a lever releasing low level radiation "
            "into the lab.",
        ),
        lab_category=BOTH,
        has_been_displayed=False,
        sibling=4,
    ),
    LabScenario(
        scenario="How hard to work today?",
        choice1=Choice(
            choice_text="Really hard!",
            happiness=10,
            knowledge=5,
            research=15,
            effect_text="Good but could be better...",
        ),
        choice2=Choice(
            choice_text="Really really hard!",
            happiness=20,
            knowledge=40,
            research=60,
            effect_text="Amazing!!",
        ),
        lab_category=BOTH,
        has_been_displayed=False,
        sibling=3,
    ),
    LabScenario(
        scenario="Something is flashing red. Do you press the button next to it? But wait... this is an important "
        "experiment, and it isn't your experiment. You could mess it up. Maybe you should leave it alone?",
        choice1=Choice(
            choice_text="Press button",
            happiness=10,
            knowledge=10,
            research=20,
            effect_text="The experiment is ruined but you save the lab from burning down! Good call!",
        ),
        choice2=Choice(
            choice_text="Do nothing",
            happiness=-40,
            knowledge=-10,
            research=-20,
            effect_text="The lab burns down! :(",
        ),
        lab_category=BOTH,
        has_been_displayed=False,
        sibling=6,
    ),
    LabScenario(
        scenario="Something is flashing red. Do you press the button next to it? But wait... this is an important "
        "experiment, and it isn't your experiment. You could mess it up. Maybe you should leave it alone?",
        choice1=Choice(
            choice_text="Press button",
            happiness=-20,
            knowledge=-10,
            research=10,
            effect_text="Experiment is ruined! Your PI is super mad at you. :(",
        ),
        choice2=Choice(
            choice_text="Do nothing",
            happiness=20,
            knowledge=30,
            research=60,
            effect_text="Experiment is fine, good call!",
        ),
        lab_category=BOTH,
        has_been_displayed=False,
        sibling=5,
    ),
    LabScenario(
        scenario="Your entire lab has been trying to discover the Bigs Hoson particle for years. You think you "
        "see the signs of one in today's collider data. Do you immediately call the press to tell them?",
        choice1=Choice(
            choice_text="Yes!",
            happiness=50,
            knowledge=10,
            research=40,
            effect_text="You call the press and tell them. It turns out the signs were real, and you did discover "
            "the Bigs Hoson! You become a physics celebrity and go on many talk shows.",
        ),
        choice2=Choice(
            choice_text="No!",
            happiness=-10,
            knowledge=0,
            research=0,
            effect_text="You decide to wait and talk to your PI first. But in the two minutes "
            "you wait, some other lab calls the press and announces they have discovered the Bigs Hoson. :( ",
        ),
        lab_category=SMALL_STUFF,
        has_been_displayed=False,
        sibling=8,
    ),
    LabScenario(
        scenario="Your entire lab has been trying to discover the Bigs Hoson particle for years. "
        "You think you see the signs of one in today's collider data. Do you immediately "
        "call the press to tell them?",
        choice1=Choice(
            choice_text="Yes!",
            happiness=-50,
            knowledge=-10,
            research=-10,
            effect_text="You call the press and tell them. It turns out the signs were false. You are "
            "laughed at by all of physics.",
        ),
        choice2=Choice(
            choice_text="No!",
            happiness=20,
            knowledge=0,
            research=20,
            effect_text="You decide to wait and talk to your PI first. This is the normal "
            "and reasonable thing to do. Turns out the signs were false. Good thing you didn't "
            "go to the press. ",
        ),
        lab_category=SMALL_STUFF,
        has_been_displayed=False,
        sibling=7,
    ),
    LabScenario(
        scenario="You were setting up some optics but you got a mirror dirty. "
        "Should you clean it with methanol or acetone?",
        choice1=Choice(
            choice_text="Methanol",
            happiness=0,
            knowledge=0,
            research=5,
            effect_text="This mirror had extra dirt on it and the methanol isn't strong enough... "
            "you should have used acetone.",
        ),
        choice2=Choice(
            choice_text="Acetone",
            happiness=20,
            knowledge=0,
            research=15,
            effect_text="Good call! You are able to clean the mirror which had a lot of dirt on it.",
        ),
        lab_category=SMALL_STUFF,
        has_been_displayed=False,
        sibling=10,
    ),
    LabScenario(
        scenario="You were setting up some optics but you got a mirror dirty. "
        "Should you clean it with methanol or acetone?",
        choice1=Choice(
            choice_text="Methanol",
            happiness=20,
            knowledge=0,
            research=15,
            effect_text="Good call! This mirror didn't have that much dirt on it, so acetone would have been overkill. "
            "You successfully clean the mirror.",
        ),
        choice2=Choice(
            choice_text="Acetone",
            happiness=0,
            knowledge=0,
            research=5,
            effect_text="Oh no! After 20 minutes of cleaning, you end up making the mirror dirtier than it initially was.",
        ),
        lab_category=SMALL_STUFF,
        has_been_displayed=False,
        sibling=9,
    ),
    LabScenario(
        scenario="You are looking through your telescope and you see an asteroid coming to hit Earth. "
        "The asteroid is the size of the moon. Earth is doomed. What should you do?",
        choice1=Choice(
            choice_text="Tell your PI",
            happiness=-100,
            knowledge=-100,
            research=-100,
            effect_text="It doesn't really matter, does it? The entire planet is doomed.",
        ),
        choice2=Choice(
            choice_text="Go into the woods and live as a hermit for your remaining days",
            happiness=-100,
            knowledge=-100,
            research=-100,
            effect_text="It doesn't really matter, does it? The entire planet is doomed.",
        ),
        lab_category=BIG_STUFF,
        has_been_displayed=False,
        sibling=-1,
    ),
    LabScenario(
        scenario="The distance between the sun and the Earth is 93,000,000 miles. The sun has a diameter of about "
        "860,000 miles. The Earth has a radius of about 8,000 miles. You are 5 feet tall. There are 5280 "
        "feet in a mile. You are 0.001 miles tall. You are so tiny. A grain of sand is 0.003 feet which is "
        "0.0000006 miles in diameter.",
        choice1=Choice(
            choice_text="Wow that's disturbing",
            happiness=-15,
            knowledge=0,
            research=10,
            effect_text="Maybe you shouldn't have decided to study Big Stuff",
        ),
        choice2=Choice(
            choice_text="That makes me uncomfortable",
            happiness=-15,
            knowledge=0,
            research=10,
            effect_text="Maybe you shouldn't have decided to study Big Stuff",
        ),
        lab_category=BIG_STUFF,
        has_been_displayed=False,
        sibling=-1,
    ),
    LabScenario(
        scenario="You hear a knock on the lab door. Standing at the door is a person in a stormtrooper "\
        "costume. It's a Star Wars LARPer. He needs to borrow a laser.",
        choice1=Choice(
            choice_text="You give him a laser pointer, warning him not to point it in anyone's eyes",
            happiness=-20,
            knowledge=0,
            research=-20,
            effect_text="Two days later you get a call from OSHA. Because of your lapse in judgement, your "\
            "lab has to be shut down for two weeks and everyone has to retake safety training.",
        ),
        choice2=Choice(
            choice_text="You tell him to leave before you tell Darth Vader what he's been up to",
            happiness=10,
            knowledge=0,
            research=5,
            effect_text="The man takes off his helmet. 'Congratulations, you've passed', he says."\
            " It was an OSHA inspector. Your lab gets a small cash prize thanks to your diligence.",
        ),
        lab_category=SMALL_STUFF,
        has_been_displayed=False,
        sibling=14,
    ),
    LabScenario(
        scenario="You hear a knock on the lab door. Standing at the door is a person in a stormtrooper "\
        "costume. It's a Star Wars LARPer. He needs to borrow a laser.",
        choice1=Choice(
            choice_text="You give him a laser pointer, warning him not to point it in anyone's eyes",
            happiness=10,
            knowledge=0,
            research=-5,
            effect_text="The stormtrooper hugs you excitedly and then leaves. Two days later he"\
            " sends you pictures of an epic lightsaber he's built. You text him back a thumbs up emoji",
        ),
        choice2=Choice(
            choice_text="You tell him to leave before you tell Darth Vader what he's been up to",
            happiness=-5,
            knowledge=0,
            research=0,
            effect_text="The stormtrooper sighs loudly and walks away. You feel a little bit bad."
        ),
        lab_category=SMALL_STUFF,
        has_been_displayed=False,
        sibling=13,
    ),
    LabScenario(
        scenario="Should you read the manual?",
        choice1=Choice(
            choice_text="Yes!",
            happiness=-40,
            knowledge=-10,
            research=-20,
            effect_text="You wasted so much time reading the manual that you had to take an extra year "\
            "before you could graduate. Oops.",
        ),
        choice2=Choice(
            choice_text="No!",
            happiness=10,
            knowledge=5,
            research=20,
            effect_text="You speedily figure out the apparatus without any manual. Not only do gain knowledge, "\
            " you save lots of time.",
        ),
        lab_category=BOTH,
        has_been_displayed=False,
        sibling=16,
    ),
    LabScenario(
        scenario="Should you read the manual?",
        choice1=Choice(
            choice_text="Yes!",
            happiness=50,
            knowledge=0,
            research=0,
            effect_text="The manual contains a message on the second to last page, written by an "\
            "employee trapped in the manual factory. It asks to please send help. You call the police "\
            "and tell them. Thanks to you, the employee was saved in the nick of time.",
        ),
        choice2=Choice(
            choice_text="No!",
            happiness=-20,
            knowledge=0,
            research=-20,
            effect_text="While you are trying to figure out how to use the apparatus, you push the "\
            "orange button. The entire apparatus crumbles into dust. Maybe you should have read the "\
            "manual after all...",
        ),
        lab_category=BOTH,
        has_been_displayed=False,
        sibling=15,
    ),
    LabScenario(
        scenario="Your lab just got a superconducting magnet, and your labmate asks if you want to go "\
        "check it out. You want to but you can't remember if you have a pacemaker.",
        choice1=Choice(
            choice_text="Call Mom and ask if your operation at the age of 5 was for a bad heart",
            happiness=-10,
            knowledge=0,
            research=-5,
            effect_text="Your Mom tells you don't have a pacemaker. Now you feel embarrassed for forgetting "
            "such an obvious thing.",
        ),
        choice2=Choice(
            choice_text="Step into the magnetic field",
            happiness=5,
            knowledge=0,
            research=15,
            effect_text="Wheeee!",
        ),
        lab_category=SMALL_STUFF,
        has_been_displayed=False,
        sibling=-1,
    ),
    LabScenario(
        scenario="What kind of music should you play during your daily rote task?",
        choice1=Choice(
            choice_text="Classical",
            happiness=10,
            knowledge=0,
            research=0,
            effect_text="You feel boosted in happiness.",
        ),
        choice2=Choice(
            choice_text="Quantum",
            happiness=-10,
            knowledge=10,
            research=10,
            effect_text="You feel less happy but your knowledge and research increases.",
        ),
        lab_category=BOTH,
        has_been_displayed=False,
        sibling=-1,
    ),

]


### Endings
# Ending where happiness drops to 0
SAD_ENDING = Ending(
    ending_title="Ending 1 of 6: Sad Hermit",
    image="pics/hermit.png",
    ending_text="You are too unhappy, and you decide physics isn't for you. "
    "Disillusioned, you drop out of school and become a hermit. "
    "You become the coolest hermit in the world. Unfortunately, "
    "you did not become physics. YOU LOSE.",
)

# Ending if you don't enroll in any classes
NO_CLASSES_ENDING = Ending(
    ending_title="Ending 2 of 6: You didn't enroll in any classes?",
    image="pics/noclasses.png",
    ending_text="You didn't enroll in any classes? How can you become physics if you don't enroll "
    "in any physics classes? More importantly, How can you measure your self worth "
    "without grades and a gpa? YOU LOSE.",
)

# Ending where you become chemistry by mistake... TODO

# Ending if you finish the quarter but without high research or knowledge
BAD_STUDENT_ENDING = Ending(
    ending_title="Ending 3 of 6: Bad Student",
    image="pics/badstudent.png",
    ending_text="You did not have high enough knowledge or research. You did not become physics. "
    "You became a bad student. YOU LOSE.",
)

# Ending with med/low knowledge (between 0 and 79), high research (between 80 and 100)
SCOPE_ENDING = Ending(
    ending_title="Ending 4 of 6: Too much research",
    image="pics/scope1.jpg",
    ending_text="Oh no! You became an oscilloscope! You spent too much time in the lab! "
    "Your research went up but you didn't have high enough knowledge to go to "
    "grad school. YOU LOSE.",
)

# Ending with high knowledge (between 80 and 100), research > 50, happiness > 50
GRAD_SCHOOL_ENDING = Ending(
    ending_title="Ending 5 of 6: Physicist",
    image="pics/physicist.png",
    ending_text="You have a lot of physics knowledge, so you go to grad school. "
    "You become a physicist, not a physics! YOU LOSE.",
)

# Ending with happiness = between 90 and 100. research between 90 and 100. Knowledge between 90 and 100.
EQUATION_ENDING = Ending(
    ending_title="Ending 6 of 6: Success!",
    image="pics/becomingphys.png",
    ending_text="You did it!! You became a physics of yourself! This is you. You became physics! "
    "See how happy you are! YOU WIN!",
)
