// Transcrypt'ed from Python, 2023-03-18 01:24:52
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as random from './random.js';
var __name__ = 'physics_elements';
export var Question =  __class__ ('Question', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, question_text, answers, correct_answer) {
		self.question_text = question_text;
		self.answers = answers;
		self.correct_answer = correct_answer;
	});}
});
export var Final =  __class__ ('Final', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, physics_class, questions) {
		self.physics_class = physics_class;
		self.questions = questions;
	});}
});
export var PhysicsClass =  __class__ ('PhysicsClass', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, physics_class_name, happiness, knowledge, day, lectures, final) {
		self.physics_class_name = physics_class_name;
		self.happiness = happiness;
		self.knowledge = knowledge;
		self.day = 0;
		self.lectures = lectures;
		self.final = final;
		self.final_grade = 0;
	});}
});
export var Choice =  __class__ ('Choice', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, choice_text, happiness, knowledge, research, effect_text) {
		self.choice_text = choice_text;
		self.happiness = happiness;
		self.knowledge = knowledge;
		self.research = research;
		self.effect_text = effect_text;
	});}
});
export var LabScenario =  __class__ ('LabScenario', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, scenario, choice1, choice2, lab_category, has_been_displayed, sibling) {
		if (typeof has_been_displayed == 'undefined' || (has_been_displayed != null && has_been_displayed.hasOwnProperty ("__kwargtrans__"))) {;
			var has_been_displayed = false;
		};
		if (typeof sibling == 'undefined' || (sibling != null && sibling.hasOwnProperty ("__kwargtrans__"))) {;
			var sibling = -(1);
		};
		self.has_been_displayed = has_been_displayed;
		self.sibling = sibling;
		self.scenario = scenario;
		self.choice1 = choice1;
		self.choice2 = choice2;
		self.lab_category = lab_category;
	});}
});
export var BIG_STUFF = 2;
export var SMALL_STUFF = 1;
export var BOTH = 0;
export var NONE = -(1);
export var Lab =  __class__ ('Lab', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, lab_name, lab_category) {
		self.lab_name = lab_name;
		self.lab_category = lab_category;
	});},
	get generate_lab_scenario () {return __get__ (this, function (self, lab_scenarios) {
		var undisplayed_lab_scenarios = [];
		for (var lab_scenario of lab_scenarios) {
			if (!(lab_scenario ['scenario'].has_been_displayed) && (lab_scenario ['scenario'].lab_category == BOTH || lab_scenario ['scenario'].lab_category == self.lab_name.lab_category)) {
				undisplayed_lab_scenarios.append (lab_scenario);
			}
		}
		if (len (undisplayed_lab_scenarios) == 0) {
			return null;
		}
		var random_index = int (random.random () * len (undisplayed_lab_scenarios));
		undisplayed_lab_scenarios [random_index] ['scenario'].has_been_displayed = true;
		var sibling_index = undisplayed_lab_scenarios [random_index] ['scenario'].sibling;
		if (sibling_index >= 0) {
			lab_scenarios [sibling_index] ['scenario'].has_been_displayed = true;
		}
		return undisplayed_lab_scenarios [random_index];
	});}
});
export var Ending =  __class__ ('Ending', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, ending_title, image, ending_text) {
		self.ending_title = ending_title;
		self.image = image;
		self.ending_text = ending_text;
	});}
});

//# sourceMappingURL=physics_elements.map