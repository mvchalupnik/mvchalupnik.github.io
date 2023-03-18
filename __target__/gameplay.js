// Transcrypt'ed from Python, 2023-03-17 23:46:55
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {BIG_STUFF, BOTH, Choice, Ending, Final, Lab, LabScenario, NONE, PhysicsClass, Question, SMALL_STUFF} from './physics_elements.js';
import {ALL_CLASSES, ALL_LABS, BAD_STUDENT_ENDING, CHOOSE_CLASS_TEXT, EQUATION_ENDING, GRAD_SCHOOL_ENDING, INTRO_TEXT, JOIN_TEXT, NO_CLASSES_ENDING, REGISTER_TEXT, SAD_ENDING, SCOPE_ENDING, lab_scenarios} from './game_text.js';
import {DAYS_IN_QUARTER, IMG_HEIGHT, IMG_WIDTH, SMALL_IMG_HEIGHT, SMALL_IMG_WIDTH} from './constants.js';
var __name__ = 'gameplay';
export var debug_endgame_off = true;
export var CONTINUE = 0;
export var NEGATIVE_HAPPINESS = 1;
export var START_FINALS = 2;
export var Game =  __class__ ('Game', [object], {
	__module__: __name__,
	happiness: 100,
	knowledge: 0,
	research: 0,
	day: 0,
	enrolled_physics_classes: [],
	joined_research_lab: Lab (__kwargtrans__ ({lab_name: 'none', lab_category: NONE})),
	get __init__ () {return __get__ (this, function (self) {
		document.getElementById ('happiness_label').textContent = 'Happiness: ' + str (self.happiness);
		document.getElementById ('knowledge_label').textContent = 'Knowledge: ' + str (self.knowledge);
		document.getElementById ('research_label').textContent = 'Research: ' + str (self.research);
		document.getElementById ('day_label').textContent = 'Day: ' + str (self.day);
		document.getElementById ('lab_label').textContent = 'Lab: none';
		document.getElementById ('class_label').textContent = 'Classes: none';
		self.show_main_choices ();
	});},
	get show_stat_changes () {return __get__ (this, function (self, delta_h, delta_k, delta_r) {
		var happiness_label = document.getElementById ('happiness_label');
		happiness_label.textContent = (('Happiness: ' + str (self.happiness)) + ' + ') + str (delta_h);
		if (delta_h >= 0) {
			happiness_label.style ['background-color'] = 'green';
			happiness_label.style ['color'] = 'white';
		}
		else {
			happiness_label.style ['background-color'] = 'red';
			happiness_label.style ['color'] = 'white';
		}
		var knowledge_label = document.getElementById ('knowledge_label');
		knowledge_label.textContent = (('Knowledge: ' + str (self.knowledge)) + ' + ') + str (delta_k);
		if (delta_k >= 0) {
			knowledge_label.style ['background-color'] = 'green';
			knowledge_label.style ['color'] = 'white';
		}
		else {
			knowledge_label.style ['background-color'] = 'red';
			knowledge_label.style ['color'] = 'white';
		}
		var research_label = document.getElementById ('research_label');
		research_label.textContent = (('Research: ' + str (self.research)) + ' + ') + str (delta_r);
		if (delta_k >= 0) {
			research_label.style ['background-color'] = 'green';
			research_label.style ['color'] = 'white';
		}
		else {
			research_label.style ['background-color'] = 'red';
			research_label.style ['color'] = 'white';
		}
		var day_label = document.getElementById ('day_label');
		day_label.textContent = ('Day: ' + str (self.day)) + ' + 1';
	});},
	get update_portrait () {return __get__ (this, function (self) {
		var happiness_label = document.getElementById ('happiness_label');
		happiness_label.textContent = 'Happiness: ' + str (self.happiness);
		happiness_label.style ['background-color'] = 'white';
		happiness_label.style ['color'] = 'black';
		var knowledge_label = document.getElementById ('knowledge_label');
		knowledge_label.textContent = 'Knowledge: ' + str (self.knowledge);
		knowledge_label.style ['background-color'] = 'white';
		knowledge_label.style ['color'] = 'black';
		var research_label = document.getElementById ('research_label');
		research_label.textContent = 'Research: ' + str (self.research);
		research_label.style ['background-color'] = 'white';
		research_label.style ['color'] = 'black';
		document.getElementById ('day_label').textContent = 'Day: ' + str (self.day);
		document.getElementById ('class_label').innerHTML = '';
		document.getElementById ('class_label').textContent = 'Classes: ';
		for (var [i, enrolled_physics_class] of enumerate (self.enrolled_physics_classes)) {
			var li1 = document.createElement ('li');
			li1.textContent = enrolled_physics_class ['physics_class_name'].physics_class_name;
			document.getElementById ('class_label').appendChild (li1);
		}
		document.getElementById ('lab_label').textContent = 'Lab: ' + self.joined_research_lab ['lab_name'].lab_name;
	});},
	get show_main_choices () {return __get__ (this, function (self) {
		document.getElementById ('player_inner_box').remove ();
		var new_inner_box = document.createElement ('div');
		new_inner_box.id = 'player_inner_box';
		var new_element_ids = [];
		var intro_label = document.createElement ('p');
		intro_label.id = 'intro_label';
		intro_label.textContent = 'Welcome to University School!\n Here you can take the first steps to becoming a physics. \nWhat would you like to do today?';
		new_inner_box.appendChild (intro_label);
		if (len (self.enrolled_physics_classes) == 0) {
			var button = document.createElement ('button');
			button.innerHTML = 'Register for Classes';
			button.id = 'class_button';
			new_element_ids.append (dict ({'element_id': button.id, 'action': self.register_classes}));
			new_inner_box.appendChild (button);
		}
		else {
			var button = document.createElement ('button');
			button.innerHTML = 'Go to Class';
			button.id = 'go_to_class_button';
			new_element_ids.append (dict ({'element_id': button.id, 'action': self.go_to_class}));
			new_inner_box.appendChild (button);
		}
		if (self.joined_research_lab ['lab_name'].lab_name == 'none') {
			var join_lab_button = document.createElement ('button');
			join_lab_button.innerHTML = 'Join a Lab';
			join_lab_button.id = 'join_lab_button';
			new_element_ids.append (dict ({'element_id': join_lab_button.id, 'action': self.join_lab}));
			new_inner_box.appendChild (join_lab_button);
		}
		else {
			var go_to_lab_button = document.createElement ('button');
			go_to_lab_button.innerHTML = 'Go to Lab';
			go_to_lab_button.id = 'go_to_lab_button';
			new_element_ids.append (dict ({'element_id': go_to_lab_button.id, 'action': self.go_to_lab}));
			new_inner_box.appendChild (go_to_lab_button);
		}
		document.getElementById ('player_text_box').appendChild (new_inner_box);
		for (var element_index = 0; element_index < len (new_element_ids); element_index++) {
			var element_id = new_element_ids [element_index].element_id;
			var action = new_element_ids [element_index].action;
			document.getElementById (element_id).addEventListener ('click', action);
		}
	});},
	get check_boundaries () {return __get__ (this, function (self) {
		if (self.happiness > 100) {
			self.happiness = 100;
		}
		if (self.knowledge > 100) {
			self.knowledge = 100;
		}
		if (self.research > 100) {
			self.research = 100;
		}
		if (self.happiness < 0) {
			self.happiness = 0;
		}
		if (self.knowledge < 0) {
			self.knowledge = 0;
		}
		if (self.research < 0) {
			self.research = 0;
		}
	});},
	get check_for_endgame () {return __get__ (this, function (self) {
		if (self.happiness <= 0 && debug_endgame_off) {
			return NEGATIVE_HAPPINESS;
		}
		if (self.day >= DAYS_IN_QUARTER && debug_endgame_off) {
			return START_FINALS;
		}
		return CONTINUE;
	});},
	get add_class () {return __get__ (this, function (self) {
		var checkbox_inputs = document.querySelectorAll ('input[type=checkbox]:checked');
		document.getElementById ('player_inner_box').remove ();
		var new_inner_box = document.createElement ('div');
		new_inner_box.id = 'player_inner_box';
		for (var checkbox_input of checkbox_inputs) {
			var selected_class = ALL_CLASSES [checkbox_input.value];
			if (selected_class ['physics_class_name'].physics_class_name == 'Fake Physics') {
				ALL_CLASSES [checkbox_input.value] ['physics_class_name'].physics_class_name = 'Controversial Physics';
				var controversial_message = 'Fake Physics has been renamed Controversial Physics in order to be more culturally sensitive. (Please select your classes again)';
				var cmessage = document.createElement ('p');
				cmessage.textContent = controversial_message;
				var cmessage_button = document.createElement ('button');
				cmessage_button.innerHTML = 'Ok then';
				cmessage_button.id = 'cmessage_button';
				new_inner_box.appendChild (cmessage);
				new_inner_box.appendChild (cmessage_button);
				document.getElementById ('player_text_box').appendChild (new_inner_box);
				document.getElementById ('cmessage_button').addEventListener ('click', self.register_classes);
				return ;
			}
		}
		for (var [index, checkbox_input] of enumerate (checkbox_inputs)) {
			var selected_class = ALL_CLASSES [checkbox_input.value];
			self.enrolled_physics_classes.append (selected_class);
		}
		document.getElementById ('player_text_box').appendChild (new_inner_box);
		self.update_portrait ();
		self.show_main_choices ();
	});},
	get register_classes () {return __get__ (this, function (self) {
		document.getElementById ('player_inner_box').remove ();
		var new_inner_box = document.createElement ('div');
		new_inner_box.id = 'player_inner_box';
		var new_element_ids = [];
		var register_div = document.createElement ('div');
		for (var [index, physics_class] of enumerate (ALL_CLASSES)) {
			var checkbox_div = document.createElement ('div');
			var checkbox = document.createElement ('input');
			checkbox ['type'] = 'checkbox';
			checkbox.id = 'register_classes_checkbox' + str (index);
			checkbox.value = index;
			var checkbox_label = document.createElement ('label');
			checkbox_label.textContent = physics_class ['physics_class_name'].physics_class_name;
			checkbox_label ['for'] = 'checkbox';
			checkbox_label.htmlFor = 'register_classes_checkbox' + str (index);
			checkbox_div.appendChild (checkbox);
			checkbox_div.appendChild (checkbox_label);
			register_div.appendChild (checkbox_div);
		}
		var register_button = document.createElement ('button');
		register_button.innerHTML = 'Done';
		register_button.id = 'register_button';
		new_element_ids.append (dict ({'element_id': register_button.id, 'action': self.add_class}));
		var register_label = document.createElement ('p');
		register_label.id = 'register_label';
		register_label.textContent = REGISTER_TEXT;
		var player_inner_box = document.createElement ('div');
		player_inner_box.id = 'player_inner_box';
		player_inner_box.appendChild (register_label);
		player_inner_box.appendChild (register_div);
		player_inner_box.appendChild (register_button);
		document.getElementById ('player_text_box').appendChild (player_inner_box);
		for (var element_index = 0; element_index < len (new_element_ids); element_index++) {
			var element_id = new_element_ids [element_index].element_id;
			var action = new_element_ids [element_index].action;
			document.getElementById (element_id).addEventListener ('click', action);
		}
	});},
	get add_lab () {return __get__ (this, function (self) {
		var radio_inputs = document.querySelectorAll ('input[type=radio]:checked');
		document.getElementById ('player_inner_box').remove ();
		var new_inner_box = document.createElement ('div');
		new_inner_box.id = 'player_inner_box';
		if (len (radio_inputs) != 1) {
			print ('Error: radio_input length should be 1');
		}
		var selected_lab = ALL_LABS [radio_inputs [0].value];
		if (selected_lab ['lab_name'].lab_name == 'Medium-Sized Stuff') {
			var medium_sized_lab_text = 'Lol we already know everything there is to know about Medium-sized stuff. Try another lab!';
			var medium_lab_label = document.createElement ('p');
			medium_lab_label.textContent = medium_sized_lab_text;
			var medium_lab_button = document.createElement ('button');
			medium_lab_button.innerHTML = 'Try Again';
			medium_lab_button.id = 'medium_lab_button';
			new_inner_box.appendChild (medium_lab_label);
			new_inner_box.appendChild (medium_lab_button);
			document.getElementById ('player_text_box').appendChild (new_inner_box);
			document.getElementById ('medium_lab_button').addEventListener ('click', self.show_main_choices);
		}
		else {
			document.getElementById ('player_text_box').appendChild (new_inner_box);
			self.joined_research_lab = selected_lab;
			self.update_portrait ();
			self.show_main_choices ();
		}
	});},
	get join_lab () {return __get__ (this, function (self) {
		document.getElementById ('player_inner_box').remove ();
		var new_inner_box = document.createElement ('div');
		new_inner_box.id = 'player_inner_box';
		var join_lab_div = document.createElement ('div');
		var join_lab_instructions = document.createElement ('p');
		join_lab_instructions.textContent = JOIN_TEXT;
		for (var [index, lab] of enumerate (ALL_LABS)) {
			var radio_div = document.createElement ('div');
			var radio = document.createElement ('input');
			radio ['type'] = 'radio';
			radio ['name'] = 'join_lab_radio';
			radio.id = 'join_lab_radio' + str (index);
			radio.value = index;
			radio.required = true;
			if (index == 0) {
				radio.checked = 'checked';
			}
			var radio_label = document.createElement ('label');
			radio_label.textContent = lab ['lab_name'].lab_name;
			radio_label ['for'] = 'radio';
			radio_label.htmlFor = 'join_lab_radio' + str (index);
			radio_div.appendChild (radio);
			radio_div.appendChild (radio_label);
			join_lab_div.appendChild (radio_div);
		}
		var join_lab_button = document.createElement ('button');
		join_lab_button.innerHTML = 'Done';
		join_lab_button.id = 'join_lab_button';
		new_inner_box.appendChild (join_lab_instructions);
		new_inner_box.appendChild (join_lab_div);
		new_inner_box.appendChild (join_lab_button);
		document.getElementById ('player_text_box').appendChild (new_inner_box);
		document.getElementById ('join_lab_button').addEventListener ('click', self.add_lab);
	});},
	get after_class () {return __get__ (this, function (self, class_index) {
		if (class_index >= 0) {
			self.happiness = self.happiness + self.enrolled_physics_classes [class_index] ['physics_class_name'].happiness;
			self.knowledge = self.knowledge + self.enrolled_physics_classes [class_index] ['physics_class_name'].knowledge;
			self.day = self.day + 1;
			self.enrolled_physics_classes [class_index].day = self.enrolled_physics_classes [class_index].day + 1;
		}
		self.check_boundaries ();
		self.update_portrait ();
		var status = self.check_for_endgame ();
		if (status == CONTINUE) {
			self.show_main_choices ();
		}
		else {
			self.end_game (status);
		}
	});},
	get in_class () {return __get__ (this, function (self) {
		var radio_inputs = document.querySelectorAll ('input[type=radio]:checked');
		document.getElementById ('player_inner_box').remove ();
		var new_inner_box = document.createElement ('div');
		new_inner_box.id = 'player_inner_box';
		if (len (radio_inputs) != 1) {
			print ('Error: radio_input length should be 1');
		}
		var class_index = radio_inputs [0].value;
		var selected_class = self.enrolled_physics_classes [class_index];
		if (selected_class.day < len (selected_class ['physics_class_name'].lectures)) {
			var class_image = document.createElement ('img');
			var class_day = selected_class.day;
			class_image.src = selected_class ['physics_class_name'].lectures [class_day] ['image_location'];
			new_inner_box.appendChild (class_image);
			self.show_stat_changes (selected_class ['physics_class_name'].happiness, selected_class ['physics_class_name'].knowledge, 0);
			var class_lecture = document.createElement ('p');
			var lecture_text = selected_class ['physics_class_name'].lectures [selected_class.day] ['lecture'];
			class_lecture.textContent = lecture_text;
		}
		else {
			var class_lecture = document.createElement ('p');
			class_lecture.textContent = 'Wheee you ran out of lectures';
			var class_index = -(1);
		}
		var lecture_button = document.createElement ('button');
		lecture_button.id = 'lecture_button';
		lecture_button.innerHTML = 'Done';
		new_inner_box.appendChild (class_lecture);
		new_inner_box.appendChild (lecture_button);
		document.getElementById ('player_text_box').appendChild (new_inner_box);
		document.getElementById ('lecture_button').addEventListener ('click', (function __lambda__ () {
			return self.after_class (class_index);
		}));
	});},
	get go_to_class () {return __get__ (this, function (self) {
		document.getElementById ('player_inner_box').remove ();
		var new_inner_box = document.createElement ('div');
		new_inner_box.id = 'player_inner_box';
		var go_to_class_div = document.createElement ('div');
		var go_to_class_p = document.createElement ('p');
		go_to_class_p.textContent = CHOOSE_CLASS_TEXT;
		for (var [index, enrolled_physics_class] of enumerate (self.enrolled_physics_classes)) {
			var radio_div = document.createElement ('div');
			var radio = document.createElement ('input');
			radio ['type'] = 'radio';
			radio ['name'] = 'go_to_class_radio';
			radio.id = 'go_to_class_radio' + str (index);
			radio.value = index;
			radio.required = true;
			if (index == 0) {
				radio ['checked'] = 'checked';
			}
			var radio_label = document.createElement ('label');
			radio_label.textContent = enrolled_physics_class ['physics_class_name'].physics_class_name;
			radio_label ['for'] = 'radio';
			radio_label.htmlFor = 'go_to_class_radio' + str (index);
			radio_div.appendChild (radio);
			radio_div.appendChild (radio_label);
			go_to_class_div.appendChild (radio_div);
		}
		var go_to_class_button = document.createElement ('button');
		go_to_class_button.innerHTML = 'Done';
		go_to_class_button.id = 'go_to_class_button';
		new_inner_box.appendChild (go_to_class_p);
		new_inner_box.appendChild (go_to_class_div);
		new_inner_box.appendChild (go_to_class_button);
		document.getElementById ('player_text_box').appendChild (new_inner_box);
		document.getElementById ('go_to_class_button').addEventListener ('click', self.in_class);
	});},
	get after_lab () {return __get__ (this, function (self, choice) {
		self.happiness = self.happiness + choice.choice_text.happiness;
		self.knowledge = self.knowledge + choice.choice_text.knowledge;
		self.research = self.research + choice.choice_text.research;
		self.day = self.day + 1;
		self.check_boundaries ();
		self.update_portrait ();
		var status = self.check_for_endgame ();
		if (status != CONTINUE) {
			self.end_game (status);
		}
		else {
			self.show_main_choices ();
		}
	});},
	get at_lab () {return __get__ (this, function (self, choice) {
		document.getElementById ('player_inner_box').remove ();
		var new_inner_box = document.createElement ('div');
		new_inner_box.id = 'player_inner_box';
		self.show_stat_changes (choice.choice_text.happiness, choice.choice_text.knowledge, choice.choice_text.research);
		var lab_choice_effect = document.createElement ('p');
		lab_choice_effect.textContent = choice.choice_text.effect_text;
		var lab_choice_effect_button = document.createElement ('button');
		lab_choice_effect_button.innerHTML = 'Done';
		lab_choice_effect_button.id = 'lab_choice_effect_button';
		new_inner_box.appendChild (lab_choice_effect);
		new_inner_box.appendChild (lab_choice_effect_button);
		document.getElementById ('player_text_box').appendChild (new_inner_box);
		document.getElementById ('lab_choice_effect_button').addEventListener ('click', (function __lambda__ () {
			return self.after_lab (choice);
		}));
	});},
	get go_to_lab () {return __get__ (this, function (self) {
		document.getElementById ('player_inner_box').remove ();
		var new_inner_box = document.createElement ('div');
		new_inner_box.id = 'player_inner_box';
		var lab_scenario = self.joined_research_lab.generate_lab_scenario (lab_scenarios);
		if (lab_scenario === null) {
			var ran_out_lab_label = document.createElement ('p');
			ran_out_lab_label.textContent = 'You go to lab, but there is no work for you there. Maybe you should go to class instead?';
			var ran_out_lab_button = document.createElement ('button');
			ran_out_lab_button.textContent = 'Ok';
			ran_out_lab_button.id = 'ran_out_lab_button';
			new_inner_box.appendChild (ran_out_lab_label);
			new_inner_box.appendChild (ran_out_lab_button);
			document.getElementById ('player_text_box').appendChild (new_inner_box);
			document.getElementById ('ran_out_lab_button').addEventListener ('click', self.show_main_choices);
		}
		else {
			var lab_title = document.createElement ('h3');
			lab_title.innerHTML = 'You went to Lab:';
			var lab_scenario_text = document.createElement ('p');
			lab_scenario_text.textContent = lab_scenario ['scenario'].scenario;
			var lab_choice_div = document.createElement ('div');
			var lab_choice1 = document.createElement ('button');
			lab_choice1.id = 'lab_choice1';
			lab_choice1.innerHTML = lab_scenario ['scenario'].choice1.choice_text.choice_text;
			var lab_choice2 = document.createElement ('button');
			lab_choice2.id = 'lab_choice2';
			lab_choice2.innerHTML = lab_scenario ['scenario'].choice2.choice_text.choice_text;
			lab_choice_div.appendChild (lab_choice1);
			lab_choice_div.appendChild (lab_choice2);
			new_inner_box.appendChild (lab_title);
			new_inner_box.appendChild (lab_scenario_text);
			new_inner_box.appendChild (lab_choice_div);
			document.getElementById ('player_text_box').appendChild (new_inner_box);
			document.getElementById ('lab_choice1').addEventListener ('click', (function __lambda__ () {
				return self.at_lab (lab_scenario ['scenario'].choice1);
			}));
			document.getElementById ('lab_choice2').addEventListener ('click', (function __lambda__ () {
				return self.at_lab (lab_scenario ['scenario'].choice2);
			}));
		}
	});},
	get grade_final () {return __get__ (this, function (self, class_index) {
		var completed_final = document.querySelectorAll ('input[type=radio]:checked');
		var physics_class = self.enrolled_physics_classes [class_index];
		var physics_class_label = document.getElementById ('physics_class_label');
		physics_class_label.textContent = physics_class ['physics_class_name'].physics_class_name + ' Final Answers';
		for (var question_index = 0; question_index < len (physics_class ['physics_class_name'].final.physics_class.questions); question_index++) {
			var question = physics_class ['physics_class_name'].final ['physics_class'].questions [question_index];
			for (var answer_index = 0; answer_index < len (question.question_text.answers); answer_index++) {
				var answer_id = (('finals_question_radio' + str (question_index)) + '_') + str (answer_index);
				var answer_label = document.getElementById (answer_id);
				if (question.question_text.correct_answer == answer_index) {
					answer_label.style ['background-color'] = 'green';
					answer_label.style ['color'] = 'white';
				}
				else {
					answer_label.style ['background-color'] = 'red';
					answer_label.style ['color'] = 'white';
				}
			}
		}
		document.getElementById ('finals_button').remove ();
		var continue_button = document.createElement ('button');
		continue_button.id = 'continue_button';
		continue_button.innerHTML = 'Continue';
		var new_inner_box = document.getElementById ('player_inner_box');
		new_inner_box.appendChild (continue_button);
		document.getElementById ('continue_button').addEventListener ('click', (function __lambda__ () {
			return self.do_final (class_index);
		}));
		var score = 0;
		for (var question_index = 0; question_index < len (physics_class ['physics_class_name'].final.physics_class.questions); question_index++) {
			var correct_answer = physics_class ['physics_class_name'].final.physics_class.questions [question_index].question_text.correct_answer;
			var player_answer = completed_final [question_index].value;
			if (correct_answer == player_answer) {
				var score = score + 1;
			}
		}
		physics_class.final_grade = score;
		var class_index = class_index + 1;
	});},
	get determine_ending () {return __get__ (this, function (self) {
		if (self.happiness >= 90 && self.knowledge >= 90 && self.research >= 90) {
			return EQUATION_ENDING;
		}
		else if (self.knowledge >= 80 && self.happiness >= 50 && self.research >= 50) {
			return GRAD_SCHOOL_ENDING;
		}
		else if (self.research >= 80) {
			return SCOPE_ENDING;
		}
		else {
			return BAD_STUDENT_ENDING;
		}
	});},
	get end_screen () {return __get__ (this, function (self, ending) {
		document.getElementById ('player_inner_box').remove ();
		var new_inner_box = document.createElement ('div');
		new_inner_box.id = 'player_inner_box';
		var end_frame_title = document.createElement ('h3');
		end_frame_title.textContent = ending ['ending_title'].ending_title;
		new_inner_box.appendChild (end_frame_title);
		var ending_image = document.createElement ('img');
		ending_image.src = ending ['ending_title'].image;
		new_inner_box.appendChild (ending_image);
		var ending_message = document.createElement ('p');
		ending_message.textContent = ending ['ending_title'].ending_text;
		new_inner_box.appendChild (ending_message);
		var quit_button = document.createElement ('a');
		quit_button.innerHTML = 'Quit';
		quit_button.id = 'quit_button';
		quit_button.href = 'main.html';
		new_inner_box.appendChild (quit_button);
		document.getElementById ('player_text_box').appendChild (new_inner_box);
	});},
	get get_letter_grade () {return __get__ (this, function (self, score) {
		var score = (float (score) * 4.0) / 3.0;
		if ((3.7 < score && score <= 4.0)) {
			return 'A';
		}
		if ((3.3 < score && score <= 3.7)) {
			return 'A-';
		}
		if ((3.0 < score && score <= 3.3)) {
			return 'B+';
		}
		if ((2.7 < score && score <= 3.0)) {
			return 'B';
		}
		if ((2.3 < score && score <= 2.7)) {
			return 'B-';
		}
		if ((2.0 < score && score <= 2.3)) {
			return 'C+';
		}
		if ((1.7 < score && score <= 2.0)) {
			return 'C';
		}
		if ((1.3 < score && score <= 1.7)) {
			return 'C-';
		}
		if ((1 < score && score <= 1.3)) {
			return 'D+';
		}
		if ((0.5 < score && score <= 1)) {
			return 'D';
		}
		else {
			return 'F';
		}
	});},
	get adjust_happiness_from_gpa () {return __get__ (this, function (self, gpa) {
		if ((3.5 < gpa && gpa <= 4.0)) {
			self.happiness = self.happiness + 100;
		}
		else if ((3.0 < gpa && gpa <= 3.5)) {
			self.happiness = self.happiness + 30;
		}
		else if ((2.5 < gpa && gpa <= 3.0)) {
			self.happiness = self.happiness + 10;
		}
		else if ((2.0 < gpa && gpa <= 2.5)) {
			self.happiness = self.happiness - 10;
		}
		else if ((1.0 < gpa && gpa <= 2.0)) {
			self.happiness = self.happiness - 30;
		}
		else {
			self.happiness = self.happiness - 60;
		}
		self.check_boundaries ();
	});},
	get do_final () {return __get__ (this, function (self, class_index) {
		document.getElementById ('player_inner_box').remove ();
		var new_inner_box = document.createElement ('div');
		new_inner_box.id = 'player_inner_box';
		if (class_index == len (self.enrolled_physics_classes)) {
			var finals_frame_title = document.createElement ('h3');
			finals_frame_title.textContent = 'Your Grades Are in...';
			new_inner_box.appendChild (finals_frame_title);
			var gpa = 0;
			for (var [index, physics_class] of enumerate (self.enrolled_physics_classes)) {
				var gpa = gpa + physics_class.final_grade;
				var letter_grade_text = (physics_class ['physics_class_name'].physics_class_name + ': ') + self.get_letter_grade (physics_class.final_grade);
				var finals_letter_grade = document.createElement ('p');
				finals_letter_grade.textContent = letter_grade_text;
				new_inner_box.appendChild (finals_letter_grade);
			}
			var gpa = float (gpa) / len (self.enrolled_physics_classes);
			var gpa = (gpa * 4.0) / 3.0;
			self.adjust_happiness_from_gpa (gpa);
			self.check_boundaries ();
			var end = self.determine_ending ();
			var grade_text = 'Your GPA is: ' + str (gpa);
			var grade_text2 = 'This has affected your happiness';
			var final_grade_label = document.createElement ('p');
			var final_grade_label2 = document.createElement ('p');
			final_grade_label.textContent = grade_text;
			final_grade_label2.textContent = grade_text2;
			new_inner_box.appendChild (final_grade_label);
			new_inner_box.appendChild (final_grade_label2);
			var final_grade_button = document.createElement ('button');
			final_grade_button.innerHTML = 'Continue';
			final_grade_button.id = 'final_grade_button';
			new_inner_box.appendChild (final_grade_button);
			document.getElementById ('player_text_box').appendChild (new_inner_box);
			document.getElementById ('final_grade_button').addEventListener ('click', (function __lambda__ () {
				return self.end_screen (end);
			}));
			return ;
		}
		var physics_class = self.enrolled_physics_classes [class_index];
		var physics_class_label = document.createElement ('h3');
		physics_class_label.textContent = physics_class ['physics_class_name'].physics_class_name + ' Final';
		physics_class_label.id = 'physics_class_label';
		new_inner_box.appendChild (physics_class_label);
		for (var question_index = 0; question_index < len (physics_class ['physics_class_name'].final.physics_class.questions); question_index++) {
			var finals_question_div = document.createElement ('div');
			var question = physics_class ['physics_class_name'].final ['physics_class'].questions [question_index];
			var finals_question_text = (str (question_index + 1) + '. ') + question.question_text.question_text;
			var finals_question_label = document.createElement ('p');
			finals_question_label.textContent = finals_question_text;
			finals_question_label.id = 'finals_question' + str (question_index);
			finals_question_div.appendChild (finals_question_label);
			for (var answer_index = 0; answer_index < len (question.question_text.answers); answer_index++) {
				var finals_question_answer = question.question_text.answers [answer_index];
				var radio_div = document.createElement ('div');
				var radio = document.createElement ('input');
				radio ['type'] = 'radio';
				radio ['name'] = 'finals_question_radio' + str (question_index);
				radio.value = answer_index;
				radio.required = true;
				if (answer_index == 0) {
					radio ['checked'] = 'checked';
				}
				var radio_label = document.createElement ('label');
				radio_label.textContent = finals_question_answer;
				radio_label ['for'] = 'radio';
				radio_label.id = (('finals_question_radio' + str (question_index)) + '_') + str (answer_index);
				radio_label.htmlFor = (('finals_question_radio' + str (question_index)) + '_') + str (answer_index);
				radio_div.appendChild (radio);
				radio_div.appendChild (radio_label);
				finals_question_div.appendChild (radio_div);
			}
			new_inner_box.appendChild (finals_question_div);
		}
		var hand_in_button = document.createElement ('button');
		hand_in_button.innerHTML = 'Hand in';
		hand_in_button.id = 'finals_button';
		new_inner_box.appendChild (hand_in_button);
		document.getElementById ('player_text_box').appendChild (new_inner_box);
		document.getElementById ('finals_button').addEventListener ('click', (function __lambda__ () {
			return self.grade_final (class_index);
		}));
	});},
	get end_game () {return __get__ (this, function (self, status) {
		self.check_boundaries ();
		self.update_portrait ();
		document.getElementById ('player_inner_box').remove ();
		var new_inner_box = document.createElement ('div');
		new_inner_box.id = 'player_inner_box';
		if (status == NEGATIVE_HAPPINESS) {
			var final_label = document.createElement ('p');
			final_label.textContent = 'You are too sad to continue!! :( :( ';
			var final_button = document.createElement ('button');
			final_button.innerHTML = 'What happens now?';
			final_button.id = 'final_button';
			new_inner_box.appendChild (final_label);
			new_inner_box.appendChild (final_button);
			document.getElementById ('player_text_box').appendChild (new_inner_box);
			document.getElementById ('final_button').addEventListener ('click', self.end_screen (SAD_ENDING));
		}
		else if (status == START_FINALS && len (self.enrolled_physics_classes) != 0) {
			var final_label = document.createElement ('p');
			final_label.textContent = "You have reached Finals week!! Remember, if you aren't miserable, you aren't studying hard enough!!";
			var final_button = document.createElement ('button');
			final_button.innerHTML = 'To Finals!';
			final_button.id = 'final_button';
			new_inner_box.appendChild (final_label);
			new_inner_box.appendChild (final_button);
			document.getElementById ('player_text_box').appendChild (new_inner_box);
			document.getElementById ('final_button').addEventListener ('click', (function __lambda__ () {
				return self.do_final (0);
			}));
		}
		else {
			self.end_screen (NO_CLASSES_ENDING);
		}
	});}
});
export var FirstScreen =  __class__ ('FirstScreen', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self) {
		document.getElementById ('yes-button').innerHTML = 'Yes';
		var no_button = document.getElementById ('no-button');
		no_button.innerHTML = 'No';
		no_button.href = 'main.html';
		document.getElementById ('image1').src = 'pics/100by100test.png';
		document.getElementById ('first-label').textContent = INTRO_TEXT;
	});},
	get start_game () {return __get__ (this, function (self) {
		window.location.href = 'portrait.html';
	});}
});

//# sourceMappingURL=gameplay.map