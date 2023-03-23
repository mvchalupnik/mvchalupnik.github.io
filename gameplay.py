from constants import IMG_HEIGHT, IMG_WIDTH, SMALL_IMG_HEIGHT, SMALL_IMG_WIDTH, DAYS_IN_QUARTER
from game_text import INTRO_TEXT, REGISTER_TEXT, JOIN_TEXT, CHOOSE_CLASS_TEXT, ALL_CLASSES, ALL_LABS,\
                      SAD_ENDING, NO_CLASSES_ENDING, BAD_STUDENT_ENDING, SCOPE_ENDING,\
                      GRAD_SCHOOL_ENDING, EQUATION_ENDING, lab_scenarios
from physics_elements import Final, Question, PhysicsClass, Choice, LabScenario, Lab, Ending,\
                             BIG_STUFF, SMALL_STUFF, BOTH, NONE

"""
gameplay.py
Contains classes containing the logic for the gameplay of Becoming Physics. These functions
are then converted to javascript using Transcrypt.
"""

# Set to False for "endless mode" (no endgame triggered) or debugging; True for normal play
debug_endgame_off = True

CONTINUE = 0
NEGATIVE_HAPPINESS = 1
START_FINALS = 2
NO_CLASSES = 3

class Game():
    """ Displays and runs the primary portion of the Becoming Physics Game.
    """
    # Initial game stats
    happiness = 100
    knowledge = 0
    research = 0
    day = 0

    enrolled_physics_classes = []
    joined_research_lab = Lab(lab_name="none", lab_category=NONE)

    def __init__ (self):
        # Initialize label texts
        document.getElementById('happiness_label').textContent = "Happiness: "+ str(self.happiness)
        document.getElementById('knowledge_label').textContent = "Knowledge: "+ str(self.knowledge)
        document.getElementById('research_label').textContent = "Research: "+ str(self.research)
        document.getElementById('day_label').textContent = "Day: "+ str(self.day)
        document.getElementById('lab_label').textContent = "Lab: none"
        document.getElementById('class_label').textContent = "Classes: none"

        self.show_main_choices(True)
    
    def show_stat_changes(self, delta_h, delta_k, delta_r):
        """ Show changes in players stats after lab or class event.
        Also shows advancement of day by + 1
        
        :param delta_h: The change in happiness
        :param delta_k: The change in knowledge
        :param delta_r: The change in research
        """
        happiness_label = document.getElementById('happiness_label')
        happiness_label.textContent = "Happiness: "+ str(self.happiness) + " + " + str(delta_h)
        if delta_h >= 0:
            happiness_label.style['background-color'] = "green";
            happiness_label.style['color'] = "white";
        else:
            happiness_label.style['background-color'] = "red";
            happiness_label.style['color'] = "white";

        knowledge_label = document.getElementById('knowledge_label')
        knowledge_label.textContent = "Knowledge: "+ str(self.knowledge) + " + " + str(delta_k)
        if delta_k >= 0:
            knowledge_label.style['background-color'] = "green";
            knowledge_label.style['color'] = "white";
        else:
            knowledge_label.style['background-color'] = "red";
            knowledge_label.style['color'] = "white";

        research_label = document.getElementById('research_label')
        research_label.textContent = "Research: "+ str(self.research) + " + " + str(delta_r)
        if delta_k >= 0:
            research_label.style['background-color'] = "green";
            research_label.style['color'] = "white";
        else:
            research_label.style['background-color'] = "red";
            research_label.style['color'] = "white";

        day_label = document.getElementById('day_label')
        day_label.textContent = "Day: "+ str(self.day) + " + 1"
    
    def update_portrait(self):    
        """ Update portrait and display stats. 
        """
        # Update and display player stats
        happiness_label = document.getElementById('happiness_label')
        happiness_label.textContent = "Happiness: "+ str(self.happiness)
        happiness_label.style['background-color'] = "white";
        happiness_label.style['color'] = "black";
        
        knowledge_label = document.getElementById('knowledge_label')
        knowledge_label.textContent = "Knowledge: "+ str(self.knowledge)
        knowledge_label.style['background-color'] = "white";
        knowledge_label.style['color'] = "black";

        research_label = document.getElementById('research_label')
        research_label.textContent = "Research: "+ str(self.research)
        research_label.style['background-color'] = "white";
        research_label.style['color'] = "black";

        document.getElementById('day_label').textContent = "Day: "+ str(self.day)

        # Display all enrolled classes
        document.getElementById('class_label').innerHTML = ''
        document.getElementById('class_label').textContent = "Classes: "
        for i, enrolled_physics_class in enumerate(self.enrolled_physics_classes):
            li1 = document.createElement('li')
            li1.textContent = enrolled_physics_class['physics_class_name'].physics_class_name
            document.getElementById('class_label').appendChild(li1)

        # Display research lab
        document.getElementById('lab_label').textContent = "Lab: " + self.joined_research_lab['lab_name'].lab_name
        
    def show_main_choices(self, is_first_screen):
        """ Show the main screen, showing the player's main choices of joining lab and classes, or attending
        lab or classes.

        :param is_first_screen: If true, display intro content
        """
        document.getElementById('player_inner_box').remove()
        new_inner_box = document.createElement('div')
        new_inner_box.id = 'player_inner_box'

        new_element_ids = []

        intro_label = document.createElement('p')
        intro_label.id = 'intro_label'

        if is_first_screen:
            intro_label.textContent = "Welcome to University School!\n Here you can take the "\
                                       "first steps to becoming a physics. \nWhat would you like to do today?"
        else:
            intro_label.textContent = "What would you like to do today?"
        new_inner_box.appendChild(intro_label)
        
        if len(self.enrolled_physics_classes) == 0:
            # If player has not joined any classes, display Register for classes option
            button = document.createElement("button")
            button.innerHTML = "Register for Classes"
            button.id = "class_button"
            new_element_ids.append({'element_id': button.id, 'action': self.register_classes})
            new_inner_box.appendChild(button)
        else:
            # If player has joined classes, display option to go to class
            button = document.createElement("button")
            button.innerHTML = "Go to Class"
            button.id = "go_to_class_button"
            new_element_ids.append({'element_id': button.id, 'action': self.go_to_class})
            new_inner_box.appendChild(button)

        # If player is not in a lab, display option to join a lab. Otherwise, display option to go to lab.
        if self.joined_research_lab['lab_name'].lab_name == "none":
            join_lab_button = document.createElement("button")
            join_lab_button.innerHTML = "Join a Lab"
            join_lab_button.id = "join_lab_button"
            new_element_ids.append({'element_id': join_lab_button.id, 'action': self.join_lab})
            new_inner_box.appendChild(join_lab_button)

        else:
            go_to_lab_button = document.createElement("button")
            go_to_lab_button.innerHTML = "Go to Lab"
            go_to_lab_button.id = "go_to_lab_button"
            new_element_ids.append({'element_id': go_to_lab_button.id, 'action': self.go_to_lab})
            new_inner_box.appendChild(go_to_lab_button)
            
        document.getElementById('player_text_box').appendChild(new_inner_box)
        
        # Add dynamic content
        for element_index in range(0, len(new_element_ids)):
            element_id = new_element_ids[element_index].element_id
            action = new_element_ids[element_index].action
            document.getElementById(element_id).addEventListener("click", action)


    def check_boundaries(self):
        """ After player stats are changed, validate the changes. In particular, no stats may exceed 100, so cap there, 
        and no stats may be less than 0, so place a floor there.
        """
        
        # Cap stats at 100
        if self.happiness > 100:
            self.happiness = 100
        if self.knowledge > 100:
            self.knowledge = 100
        if self.research > 100:
            self.research = 100
        
        # Set floor for stats at 0
        if self.happiness < 0:
            self.happiness = 0
        if self.knowledge < 0:
            self.knowledge = 0
        if self.research < 0:
            self.research = 0
        
    def check_for_endgame(self):
        """ Check for endgame conditions
        """
        # End game is triggered if player happiness reaches 0 or less
        if self.happiness <= 0 and debug_endgame_off:
            return NEGATIVE_HAPPINESS
        
        # End game is triggered if player reaches DAYS_IN_QUARTER and debug mode is off
        if self.day >= DAYS_IN_QUARTER and debug_endgame_off:
            if len(self.enrolled_physics_classes) == 0:
                return NO_CLASSES
            else:
                return START_FINALS

        # Otherwise, continue playing
        return CONTINUE
        
    def add_class(self):
        """ Add all classes that the player selected the checkbox for to the player's class enrolled classes list

        """
        checkbox_inputs = document.querySelectorAll('input[type=checkbox]:checked')

        document.getElementById('player_inner_box').remove()
        new_inner_box = document.createElement('div')
        new_inner_box.id = 'player_inner_box'

        for checkbox_input in checkbox_inputs:
            selected_class = ALL_CLASSES[checkbox_input.value]

            if selected_class['physics_class_name'].physics_class_name == "Fake Physics":
                # Rename Fake Physics to Controversial Physics
                ALL_CLASSES[checkbox_input.value]['physics_class_name'].physics_class_name = "Controversial Physics"

                controversial_message = "Fake Physics has been renamed Controversial Physics in "\
                                        "order to be more culturally sensitive. (Please select your classes again)" 

                cmessage = document.createElement('p')
                cmessage.textContent = controversial_message

                cmessage_button = document.createElement('button')
                cmessage_button.innerHTML = "Ok then"
                cmessage_button.id = 'cmessage_button'

                new_inner_box.appendChild(cmessage)
                new_inner_box.appendChild(cmessage_button)

                document.getElementById('player_text_box').appendChild(new_inner_box)
                document.getElementById('cmessage_button').addEventListener("click", self.register_classes)
                return

        for index, checkbox_input in enumerate(checkbox_inputs):
            # Enroll in all classes for which the checkbox was selected
            selected_class = ALL_CLASSES[checkbox_input.value]
            self.enrolled_physics_classes.append(selected_class)

        document.getElementById('player_text_box').appendChild(new_inner_box)
        self.update_portrait()
        self.show_main_choices(False)
    
    def register_classes(self):
        """ Register for a class by displaying to the player a list of classes with the options to 
        select a checkbox next to them, and prompting the player to select classes they would like
        to join.
        """
        # create a new inner box
        document.getElementById('player_inner_box').remove()
        new_inner_box = document.createElement('div')
        new_inner_box.id = 'player_inner_box'

        # Keep track of element ids to add event listeners to at the end
        new_element_ids = []

        register_div = document.createElement("div")

        for index, physics_class in enumerate(ALL_CLASSES):
            checkbox_div = document.createElement("div")

            checkbox = document.createElement("input")
            checkbox['type'] = "checkbox"
            checkbox.id = "register_classes_checkbox" + str(index)
            checkbox.value = index

            checkbox_label = document.createElement("label")
            checkbox_label.textContent = physics_class['physics_class_name'].physics_class_name
            checkbox_label['for'] = "checkbox"
            checkbox_label.htmlFor = "register_classes_checkbox" + str(index)

            checkbox_div.appendChild(checkbox)
            checkbox_div.appendChild(checkbox_label)
            register_div.appendChild(checkbox_div)
        
        register_button = document.createElement("button")
        register_button.innerHTML = "Done"
        register_button.id = "register_button"
#        new_element_ids.append({'element_id': register_button.id, 'action': lambda: self.add_class(self.event_frame.checkbox_list)})
        new_element_ids.append({'element_id': register_button.id, 'action': self.add_class})

        register_label = document.createElement("p")
        register_label.id = "register_label"
        register_label.textContent = REGISTER_TEXT

        # Add last!
        player_inner_box = document.createElement("div")
        player_inner_box.id = "player_inner_box"

        player_inner_box.appendChild(register_label)
        player_inner_box.appendChild(register_div)
        player_inner_box.appendChild(register_button)

        document.getElementById('player_text_box').appendChild(player_inner_box)

        # Add dynamic content
        for element_index in range(0, len(new_element_ids)):
            element_id = new_element_ids[element_index].element_id
            action = new_element_ids[element_index].action
            document.getElementById(element_id).addEventListener("click", action)
    
    def add_lab(self):
        """ Add the lab that the player chooses

        """
        radio_inputs = document.querySelectorAll('input[type=radio]:checked')

        # create a new inner box
        document.getElementById('player_inner_box').remove()
        new_inner_box = document.createElement('div')
        new_inner_box.id = 'player_inner_box'

        if len(radio_inputs) != 1:
            print('Error: radio_input length should be 1')

        selected_lab = ALL_LABS[radio_inputs[0].value]

        if selected_lab['lab_name'].lab_name == "Medium-Sized Stuff":

            medium_sized_lab_text = "Lol we already know everything there is to know about "\
                                    "Medium-sized stuff. Try another lab!"
            medium_lab_label = document.createElement('p')
            medium_lab_label.textContent = medium_sized_lab_text

            medium_lab_button = document.createElement('button')
            medium_lab_button.innerHTML = "Try Again"
            medium_lab_button.id = 'medium_lab_button'

            new_inner_box.appendChild(medium_lab_label)
            new_inner_box.appendChild(medium_lab_button)
            document.getElementById('player_text_box').appendChild(new_inner_box)
            document.getElementById('medium_lab_button').addEventListener("click", lambda: self.show_main_choices(False))
        else:
            document.getElementById('player_text_box').appendChild(new_inner_box)

            self.joined_research_lab = selected_lab
            self.update_portrait()
            self.show_main_choices(False)

        
    def join_lab(self): 
        """ Join a lab
        """
        # create a new inner box
        document.getElementById('player_inner_box').remove()
        new_inner_box = document.createElement('div')
        new_inner_box.id = 'player_inner_box'

        join_lab_div = document.createElement("div")

        join_lab_instructions = document.createElement("p")
        join_lab_instructions.textContent = JOIN_TEXT

        for index, lab in enumerate(ALL_LABS):
            radio_div = document.createElement("div")

            radio = document.createElement("input")
            radio['type'] = "radio"
            radio['name'] = "join_lab_radio"
            radio.id = "join_lab_radio" + str(index)
            radio.value = index
            radio.required = True

            # Set default value
            if index == 0:
                radio.checked = "checked"

            radio_label = document.createElement("label")
            radio_label.textContent = lab['lab_name'].lab_name
            radio_label['for'] = "radio"
            radio_label.htmlFor = "join_lab_radio" + str(index)

            radio_div.appendChild(radio)
            radio_div.appendChild(radio_label)
            join_lab_div.appendChild(radio_div)        

        join_lab_button = document.createElement("button")
        join_lab_button.innerHTML = "Done"
        join_lab_button.id = 'join_lab_button'

        new_inner_box.appendChild(join_lab_instructions)
        new_inner_box.appendChild(join_lab_div)
        new_inner_box.appendChild(join_lab_button)
        document.getElementById('player_text_box').appendChild(new_inner_box)
        document.getElementById('join_lab_button').addEventListener("click", self.add_lab)

    
    def after_class(self, class_index):
        """ This function is called after a Class finishes

        :param class_index: The index of enrolled_physics_classes pointing to the desired class
        """

        # If class_index = -1, this means the player ran out of lectures for that particular class
        if class_index >= 0 :
            # Add happiness and knowledge gained from classes to player stats
            self.happiness = self.happiness + self.enrolled_physics_classes[class_index]['physics_class_name'].happiness
            self.knowledge = self.knowledge + self.enrolled_physics_classes[class_index]['physics_class_name'].knowledge

            # Advance the day by 1
            self.day = self.day + 1

            # Advance the physics class index by 1
            self.enrolled_physics_classes[class_index].day = self.enrolled_physics_classes[class_index].day + 1
        
        # Validate changes to player stats
        self.check_boundaries()
        # Reset colors on stats and redisplay stats
        self.update_portrait()

        # Check for endgame
        status = self.check_for_endgame()
        if status == CONTINUE:
            self.show_main_choices(False)
        else:
            self.end_game(status)
    
    def in_class(self):
        """ Display class image and text if player attends class lecture.

        """
        radio_inputs = document.querySelectorAll('input[type=radio]:checked')

        # create a new inner box
        document.getElementById('player_inner_box').remove()
        new_inner_box = document.createElement('div')
        new_inner_box.id = 'player_inner_box'

        if len(radio_inputs) != 1:
            print('Error: radio_input length should be 1')
        class_index = radio_inputs[0].value
        selected_class = self.enrolled_physics_classes[class_index]

        # Make sure the player hasn't finished all possible lectures
        if selected_class.day < len(selected_class['physics_class_name'].lectures):
            class_image = document.createElement('img')
            class_day = selected_class.day

            class_image.src = selected_class['physics_class_name'].lectures[class_day]['image_location']
            new_inner_box.appendChild(class_image)

            self.show_stat_changes(selected_class['physics_class_name'].happiness, selected_class['physics_class_name'].knowledge, 0)
            class_lecture = document.createElement('p')
            lecture_text = selected_class['physics_class_name'].lectures[selected_class.day]['lecture']
            class_lecture.textContent = lecture_text

        else :
            # Player has attended all possible lectures for that particular class
            class_lecture = document.createElement('p')
            class_lecture.textContent = "Wheee you ran out of lectures"
            class_index = -1
        
        lecture_button = document.createElement('button')
        lecture_button.id = 'lecture_button'
        lecture_button.innerHTML='Done'

        new_inner_box.appendChild(class_lecture)
        new_inner_box.appendChild(lecture_button)
        document.getElementById('player_text_box').appendChild(new_inner_box)
        document.getElementById('lecture_button').addEventListener("click", lambda: self.after_class(class_index))

   
    def go_to_class(self):
        """ Display classes which player is enrolled in, and radio buttons for them to choose which class to attend
        """
        # create a new inner box
        document.getElementById('player_inner_box').remove()
        new_inner_box = document.createElement('div')
        new_inner_box.id = 'player_inner_box'

        go_to_class_div = document.createElement("div")

        # Display text prompting player to choose a class
        go_to_class_p = document.createElement("p")
        go_to_class_p.textContent = CHOOSE_CLASS_TEXT

        for index, enrolled_physics_class in enumerate(self.enrolled_physics_classes):
            radio_div = document.createElement("div")

            radio = document.createElement("input")
            radio['type'] = "radio"
            radio['name'] = "go_to_class_radio"
            radio.id = "go_to_class_radio" + str(index)
            radio.value = index
            radio.required = True

            # Set default value
            if index == 0:
                radio['checked'] = "checked"
            radio_label = document.createElement("label")
            radio_label.textContent = enrolled_physics_class['physics_class_name'].physics_class_name
            radio_label['for'] = "radio"
            radio_label.htmlFor = "go_to_class_radio" + str(index)

            radio_div.appendChild(radio)
            radio_div.appendChild(radio_label)
            go_to_class_div.appendChild(radio_div)

        go_to_class_button = document.createElement("button")
        go_to_class_button.innerHTML = "Done"
        go_to_class_button.id = 'go_to_class_button'

        new_inner_box.appendChild(go_to_class_p)
        new_inner_box.appendChild(go_to_class_div)
        new_inner_box.appendChild(go_to_class_button)
        document.getElementById('player_text_box').appendChild(new_inner_box)
        document.getElementById('go_to_class_button').addEventListener("click", self.in_class)

    def after_lab(self, choice):
        """ Funtion called after lab scenario completes
        """
        # Update player stats        
        self.happiness = self.happiness + choice.choice_text.happiness
        self.knowledge = self.knowledge + choice.choice_text.knowledge
        self.research = self.research + choice.choice_text.research
        self.day = self.day + 1
        
        # check stat boundaries
        self.check_boundaries()

        # Update stats
        self.update_portrait()

        # Check for endgame conditions
        status = self.check_for_endgame()
        if status != CONTINUE: 
            self.end_game(status)
        else:
            self.show_main_choices(False)
    
    def at_lab(self, choice):
        """ Show stat changes and display lab choice text effects for lab scenario and choice

        :param choice: the Choice which the player selected for a given LabScenario
        """
        # create a new inner box
        document.getElementById('player_inner_box').remove()
        new_inner_box = document.createElement('div')
        new_inner_box.id = 'player_inner_box'

        # Show changes in stats
        self.show_stat_changes(choice.choice_text.happiness, choice.choice_text.knowledge, choice.choice_text.research)

        lab_choice_effect = document.createElement('p')
        lab_choice_effect.textContent = choice.choice_text.effect_text
        lab_choice_effect_button = document.createElement('button')
        lab_choice_effect_button.innerHTML = "Done"
        lab_choice_effect_button.id = 'lab_choice_effect_button'

        new_inner_box.appendChild(lab_choice_effect)
        new_inner_box.appendChild(lab_choice_effect_button)
        document.getElementById('player_text_box').appendChild(new_inner_box)
        document.getElementById('lab_choice_effect_button').addEventListener("click", lambda: self.after_lab(choice))

    def go_to_lab(self):
        """ Go to lab and generate a LabScenario
        """
        # create a new inner box
        document.getElementById('player_inner_box').remove()
        new_inner_box = document.createElement('div')
        new_inner_box.id = 'player_inner_box'
        
        # Generate a lab scenario 
        lab_scenario = self.joined_research_lab.generate_lab_scenario(lab_scenarios)
        if lab_scenario is None: # Ran out of scenarios!
            ran_out_lab_label = document.createElement('p')
            ran_out_lab_label.textContent = "You go to lab, but there is no work for you there. "\
                                            "Maybe you should go to class instead?"

            ran_out_lab_button = document.createElement("button")
            ran_out_lab_button.textContent = "Ok"
            ran_out_lab_button.id = 'ran_out_lab_button'

            new_inner_box.appendChild(ran_out_lab_label)
            new_inner_box.appendChild(ran_out_lab_button)
            document.getElementById('player_text_box').appendChild(new_inner_box)
            document.getElementById('ran_out_lab_button').addEventListener("click", lambda: self.show_main_choices(False))

        else:
            # Create Lab scenario 
            lab_title = document.createElement('h3')
            lab_title.innerHTML = "You went to Lab:"
            lab_scenario_text = document.createElement('p')
            lab_scenario_text.textContent = lab_scenario['scenario'].scenario

            # Create the two LabScenario Choices
            lab_choice_div = document.createElement('div')
            lab_choice1 = document.createElement('button')
            lab_choice1.id = 'lab_choice1'
            lab_choice1.innerHTML = lab_scenario['scenario'].choice1.choice_text.choice_text

            lab_choice2 = document.createElement('button')
            lab_choice2.id = 'lab_choice2'
            lab_choice2.innerHTML = lab_scenario['scenario'].choice2.choice_text.choice_text

            lab_choice_div.appendChild(lab_choice1)
            lab_choice_div.appendChild(lab_choice2)

            new_inner_box.appendChild(lab_title)
            new_inner_box.appendChild(lab_scenario_text)
            new_inner_box.appendChild(lab_choice_div)

            document.getElementById('player_text_box').appendChild(new_inner_box)
            document.getElementById('lab_choice1').addEventListener("click", lambda: self.at_lab(lab_scenario['scenario'].choice1))
            document.getElementById('lab_choice2').addEventListener("click", lambda: self.at_lab(lab_scenario['scenario'].choice2))        


    def grade_final(self, class_index):
        """ Grade a final for a given PhysicsClass. Update player stats.
        
        :param completed_final: A list of IntVars() passed containing player's completed answers to the final
        :param class_index: The class index of enrolled_physics_classes pointing to the desired class
        """
        completed_final = document.querySelectorAll('input[type=radio]:checked')

        # get class from list of player's enrolled classes
        physics_class = self.enrolled_physics_classes[class_index]

        # Create a new frame to display grades
        physics_class_label = document.getElementById('physics_class_label')
        physics_class_label.textContent = physics_class['physics_class_name'].physics_class_name + " Final Answers"

        for question_index in range(0, len(physics_class['physics_class_name'].final.physics_class.questions)):
            question = physics_class['physics_class_name'].final['physics_class'].questions[question_index]

            # Loop over each answer and display the correct answer
            for answer_index in range(0, len(question.question_text.answers)):

                answer_id = "finals_question_radio" + str(question_index) + '_' + str(answer_index)
                answer_label = document.getElementById(answer_id)
                if question.question_text.correct_answer == answer_index:
                    # Make the correct answer appear in green
                    answer_label.style['background-color'] = "green"
                    answer_label.style['color'] = "white";
                else:
                    # Make all wrong answers appear in red
                    answer_label.style['background-color'] = "red"
                    answer_label.style['color'] = "white";

        # Remove Hand in button
        document.getElementById('finals_button').remove()

        # Create Continue button
        continue_button = document.createElement('button')
        continue_button.id = 'continue_button'

        continue_button.innerHTML = 'Continue'
        new_inner_box = document.getElementById('player_inner_box')
        new_inner_box.appendChild(continue_button)
        document.getElementById('continue_button').addEventListener("click", lambda: self.do_final(class_index))
        
        # Calculate and store grade
        score = 0
        for question_index in range(0, len(physics_class['physics_class_name'].final.physics_class.questions)):
            correct_answer = physics_class['physics_class_name'].final.physics_class.questions[question_index].question_text.correct_answer
            player_answer = completed_final[question_index].value
            if correct_answer == player_answer:
                score = score + 1
        physics_class.final_grade = score

        # Increase class_index by 1 for when continue button is pushed above
        class_index = class_index + 1
    
    def determine_ending(self):
        """ Determine the earned ending based on player stats
        """

        if(self.happiness >= 90 and self.knowledge >= 90 and self.research >= 90):
            # Best possible ending
            return EQUATION_ENDING
        elif(self.knowledge >= 80 and self.happiness >= 50 and self.research >= 50):
            # Okay ending
            return GRAD_SCHOOL_ENDING
        elif(self.research >= 80):
            # Okay ending
            return SCOPE_ENDING
        else:
            # Bad ending
            return BAD_STUDENT_ENDING
    
    def end_screen(self, ending):
        """ Display ending screen based on ending passed

        :param ending: the Ending to display to the player
        """
        # create a new inner box
        document.getElementById('player_inner_box').remove()
        new_inner_box = document.createElement('div')
        new_inner_box.id = 'player_inner_box'

        # Create ending screen frame title
        end_frame_title = document.createElement('h3')
        end_frame_title.textContent = ending['ending_title'].ending_title
        new_inner_box.appendChild(end_frame_title)

        # Create ending image
        ending_image = document.createElement('img')
        ending_image.src=ending['ending_title'].image
        new_inner_box.appendChild(ending_image)

        # Create ending message
        ending_message = document.createElement('p')
        ending_message.textContent = ending['ending_title'].ending_text
        new_inner_box.appendChild(ending_message)

        quit_button = document.createElement('a') #button
        quit_button.innerHTML = 'Quit'
        quit_button.id = 'quit_button'
        quit_button.href = "main.html"
        new_inner_box.appendChild(quit_button)
        document.getElementById('player_text_box').appendChild(new_inner_box)

    def get_letter_grade(self, score):
        """ Calculate GPA and letter grade for a given class from the three question quiz

        :score: the player's score on the three question quiz
        """
        score = float(score) * 4./3.

        if 3.7 < score <= 4.0 :
            return "A"
        if 3.3 < score <= 3.7 :
            return "A-"
        if 3.0 < score <= 3.3 :
            return "B+"
        if 2.7 < score <= 3.0 :
            return "B"
        if 2.3 < score <= 2.7 :
            return "B-"
        if 2.0 < score <= 2.3 :
            return "C+"
        if 1.7 < score <= 2.0 :
            return "C"
        if 1.3 < score <= 1.7 :
            return "C-"
        if 1 < score <= 1.3 :
            return "D+"
        if 0.5 < score <= 1 :
            return "D"
        else:
            return "F"
            
    def adjust_happiness_from_gpa(self, gpa) :
        """ Adjust player happiness based on GPA

        :param gpa: The player's GPA
        """
        if 3.5 < gpa <= 4.0:
            return 100
        elif 3.0 < gpa <= 3.5:
            return 30
        elif 2.5 < gpa <= 3.0:
            return 10
        elif 2.0 < gpa <= 2.5:
            return -10
        elif 1.0 < gpa <= 2.0:
            return -30
        else:
            return -60
        
    def do_final(self, class_index):
        """ Set up a final for a given PhysicsClass for the player to complete

        :param class_index:  The class index of enrolled_physics_classes pointing to the desired class
        """
        # create a new inner box
        document.getElementById('player_inner_box').remove()
        new_inner_box = document.createElement('div')
        new_inner_box.id = 'player_inner_box'

        # If class_index is equal to the size of the list of enrolled classes, we have finished finals
        if class_index == len(self.enrolled_physics_classes):
            # Display final grades
            finals_frame_title = document.createElement('h3')
            finals_frame_title.textContent = "Your Grades Are in..."
            new_inner_box.appendChild(finals_frame_title)

            # Determine gpa and display lettergrade of each class
            gpa = 0
            for index, physics_class in enumerate(self.enrolled_physics_classes):
                gpa = gpa + physics_class.final_grade
                
                letter_grade_text = physics_class['physics_class_name'].physics_class_name + ": " + self.get_letter_grade(physics_class.final_grade)
                finals_letter_grade = document.createElement('p')
                finals_letter_grade.textContent = letter_grade_text
                new_inner_box.appendChild(finals_letter_grade)

            # Find total GPA
            gpa = float(gpa) / len(self.enrolled_physics_classes)
            gpa = gpa * 4./3.
            
            # Determine happiness change based on gpa
            delta_h = self.adjust_happiness_from_gpa(gpa)
            self.show_stat_changes(delta_h, 0, 0)
            self.happiness = self.happiness + delta_h
            self.check_boundaries()
            
            # Determine player ending based on final stats
            end = self.determine_ending()

            grade_text = "Your GPA is: " + str(gpa)
            grade_text2 = "This has affected your happiness"
            final_grade_label = document.createElement('p')
            final_grade_label2 = document.createElement('p')
            final_grade_label.textContent = grade_text
            final_grade_label2.textContent = grade_text2
            new_inner_box.appendChild(final_grade_label)
            new_inner_box.appendChild(final_grade_label2)

            final_grade_button = document.createElement('button')
            final_grade_button.innerHTML = 'Continue'
            final_grade_button.id = 'final_grade_button'
            new_inner_box.appendChild(final_grade_button)

            document.getElementById('player_text_box').appendChild(new_inner_box)
            document.getElementById('final_grade_button').addEventListener("click", lambda: self.end_screen(end))
            return
        
        # Otherwise, do a final for class number class_index
        physics_class = self.enrolled_physics_classes[class_index]

        # Display text prompting player to choose a class
        physics_class_label = document.createElement("h3")
        physics_class_label.textContent = physics_class['physics_class_name'].physics_class_name + " Final"
        physics_class_label.id = 'physics_class_label'
        new_inner_box.appendChild(physics_class_label)

        for question_index in range(0, len(physics_class['physics_class_name'].final.physics_class.questions)):
            finals_question_div = document.createElement('div')

            question = physics_class['physics_class_name'].final['physics_class'].questions[question_index]
            finals_question_text = str(question_index+1) + ". " + question.question_text.question_text

            finals_question_label = document.createElement('p')
            finals_question_label.textContent = finals_question_text
            finals_question_label.id ='finals_question' + str(question_index)
            finals_question_div.appendChild(finals_question_label)

            # Loop through each of four possible answers
            for answer_index in range(0, len(question.question_text.answers)):
                finals_question_answer = question.question_text.answers[answer_index]

                radio_div = document.createElement("div")

                radio = document.createElement("input")
                radio['type'] = "radio"
                radio['name'] = "finals_question_radio" + str(question_index)
                radio.value = answer_index
                radio.required = True

                # Set default value
                if answer_index == 0:
                    radio['checked'] = "checked"
                radio_label = document.createElement("label")
                radio_label.textContent = finals_question_answer
                radio_label['for'] = "radio"
                radio_label.id = "finals_question_radio" + str(question_index) + '_' + str(answer_index)
                radio_label.htmlFor = "finals_question_radio" + str(question_index) + '_' + str(answer_index)

                radio_div.appendChild(radio)
                radio_div.appendChild(radio_label)
                finals_question_div.appendChild(radio_div)
            new_inner_box.appendChild(finals_question_div)

        hand_in_button = document.createElement("button")
        hand_in_button.innerHTML = "Hand in"
        hand_in_button.id = 'finals_button'

        new_inner_box.appendChild(hand_in_button)
        document.getElementById('player_text_box').appendChild(new_inner_box)
        document.getElementById('finals_button').addEventListener("click", lambda: self.grade_final(class_index))

    def end_game(self, status):
        """ Either end the game, or trigger finals, with particular route determined by status Enum provided.

        :param status: An EndGameStatus Enum to determine which route to take
        """
        self.check_boundaries()
        self.update_portrait()

        if status == NO_CLASSES:
            # If you enroll in no classes, call that no classes ending
            self.end_screen(NO_CLASSES_ENDING)
            return

        # create a new inner box
        document.getElementById('player_inner_box').remove()
        new_inner_box = document.createElement('div')
        new_inner_box.id = 'player_inner_box'

        if status == NEGATIVE_HAPPINESS:
            # If Happiness < 0, trigger SAD_ENDING
            final_label = document.createElement('p')
            final_label.textContent = "You are too sad to continue!! :( :( "
            final_button = document.createElement('button')
            final_button.innerHTML ="What happens now?"
            final_button.id = 'final_button'

            new_inner_box.appendChild(final_label)
            new_inner_box.appendChild(final_button)
            document.getElementById('player_text_box').appendChild(new_inner_box)
            document.getElementById('final_button').addEventListener("click", self.end_screen(SAD_ENDING))
        
        elif status == START_FINALS and len(self.enrolled_physics_classes) != 0:
            # Trigger the start of Finals
            final_label = document.createElement('p')
            final_label.textContent = "You have reached Finals week!! Remember, if you aren't miserable, "\
                                              "you aren't studying hard enough!!"
            final_button = document.createElement('button')
            final_button.innerHTML = "To Finals!"
            final_button.id = 'final_button'

            new_inner_box.appendChild(final_label)
            new_inner_box.appendChild(final_button)
            document.getElementById('player_text_box').appendChild(new_inner_box)
            document.getElementById('final_button').addEventListener("click", lambda: self.do_final(0))

        else:
            print('ERROR: invalid ending status')

class FirstScreen():
    """ FirstScreen is the first screen that is displayed in the Becoming Physics game.
    """
    def __init__ (self):
        # Load in content (for <a> set value)
        document.getElementById('yes-button').innerHTML = 'Yes'
        no_button = document.getElementById('no-button')
        no_button.innerHTML = 'No'
        no_button.href = "main.html"
        document.getElementById('image1').src='pics/100by100test.png'
        document.getElementById('first-label').textContent = INTRO_TEXT
        
    def start_game(self):
        """ Destroys the FirstScreen canvas and associated objects and instantiates the
        Game class
        """
        window.location.href = 'portrait.html';
