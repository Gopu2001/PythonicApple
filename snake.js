// Transcrypt'ed from Python, 2020-05-29 01:56:17
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {fabric} from './com.fabricjs.js';
var __name__ = '__main__';
var __left0__ = tuple ([500, 500]);
export var w = __left0__ [0];
export var h = __left0__ [1];
export var inc = 20;
var __left0__ = tuple ([37, 39, 32]);
export var left = __left0__ [0];
export var right = __left0__ [1];
export var space = __left0__ [2];
window.onkeydown = (function __lambda__ (event) {
	return event.keycode != space;
});
var __left0__ = null;
export var player = __left0__;
export var apple = __left0__;
export var obstacle = __left0__;
export var mongoose = __left0__;
export var canvas = __left0__;
export var facing = [1, 2, 3, 4];
export var LEFT = 1;
export var UP = 2;
export var RIGHT = 3;
export var DOWN = 4;
export var Snake =  __class__ ('Snake', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self) {
		self.alive = true;
		self.past = [];
		self.tail = [];
		self.coords = [];
		self.snake_length = 1;
		self.loc = tuple ([5 * inc, 5 * inc]);
		self.snake = new fabric.Rect (dict ({'left': self.loc [0], 'top': self.loc [1], 'width': inc, 'height': inc, 'originX': 'left', 'originY': 'top', 'fill': 'green'}));
		self.facing = 3;
	});},
	get py_update () {return __get__ (this, function (self) {
		canvas.remove (self.snake);
		for (var t_box of self.tail) {
			canvas.remove (t_box);
		}
		self.coords = [];
		self.tail = [];
		self.past.append (self.loc);
		if (self.facing == 1) {
			self.loc = tuple ([self.loc [0] - inc, self.loc [1]]);
		}
		else if (self.facing == 2) {
			self.loc = tuple ([self.loc [0], self.loc [1] - inc]);
		}
		else if (self.facing == 3) {
			self.loc = tuple ([self.loc [0] + inc, self.loc [1]]);
		}
		else {
			self.loc = tuple ([self.loc [0], self.loc [1] + inc]);
		}
		self.snake = new fabric.Rect (dict ({'left': self.loc [0], 'top': self.loc [1], 'width': inc, 'height': inc, 'originX': 'left', 'originY': 'top', 'fill': 'green'}));
		self.coords.append (self.loc);
		self.snake.hasControls = false;
		var tail = [];
		for (var i = 0; i < self.snake_length - 1; i++) {
			self.tail.append (new fabric.Rect (dict ({'left': self.past [len (self.past) - (i + 1)] [0], 'top': self.past [len (self.past) - (i + 1)] [1], 'width': inc, 'height': inc, 'originX': 'left', 'originY': 'top', 'fill': 'green'})));
			self.coords.append (self.past [len (self.past) - (i + 1)]);
		}
		for (var t_box of self.tail) {
			canvas.add (t_box);
			if (t_box.left == self.snake.left && t_box.top == self.snake.top) {
				alert ('You ate yourself! Click OK to continue.');
				self.die ();
			}
		}
		canvas.add (self.snake);
	});},
	get turn () {return __get__ (this, function (self, e) {
		if (e.keyCode == 37) {
			if (self.facing == 1) {
				self.facing = 4;
			}
			else {
				self.facing = facing [facing.index (self.facing) - 1];
			}
		}
		else if (e.keyCode == 39) {
			if (self.facing == 4) {
				self.facing = 1;
			}
			else {
				self.facing = facing [facing.index (self.facing) + 1];
			}
		}
		else if (e.keyCode == 80) {
			alert ('Game Paused. Click OK to continue.');
		}
	});},
	get turn_mobile () {return __get__ (this, function (self, event) {
		if (event.clientX < screen.width / 2) {
			if (self.facing == 1) {
				self.facing = 4;
			}
			else {
				self.facing = facing [facing.index (self.facing) - 1];
			}
		}
		else if (event.clientX > screen.width / 2) {
			if (self.facing == 4) {
				self.facing = 1;
			}
			else {
				self.facing = facing [facing.index (self.facing) + 1];
			}
		}
	});},
	get die () {return __get__ (this, function (self) {
		player.alive = false;
		canvas.remove (self.snake);
		for (var t_box of self.tail) {
			canvas.remove (t_box);
		}
		var __left0__ = false;
		var start = __left0__;
		var started = __left0__;
		gameOver ();
	});}
});
export var Apple =  __class__ ('Apple', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self) {
		self.spawn ();
	});},
	get spawn () {return __get__ (this, function (self) {
		self.loc = tuple ([int ((Math.random () * w) / inc) * inc, int ((Math.random () * h) / inc) * inc]);
		self.apple = new fabric.Rect (dict ({'left': self.loc [0], 'top': self.loc [1], 'width': inc, 'height': inc, 'originX': 'left', 'originY': 'top', 'fill': 'red'}));
		self.apple.hasControls = false;
		self.apple.evented = false;
		self.apple.selectable = false;
		canvas.add (self.apple);
	});},
	get eat () {return __get__ (this, function (self) {
		canvas.remove (self.apple);
	});}
});
export var Obstacle =  __class__ ('Obstacle', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self) {
		self.in_place = false;
		self.block = null;
	});},
	get generate_obstacle () {return __get__ (this, function (self, apple_loc) {
		if (self.block != null) {
			canvas.remove (self.block);
		}
		self.apple_loc = apple_loc;
		self.spot = int (Math.random () * 3) + 1;
		if (self.spot == LEFT && apple_loc [0] == 0) {
			self.spot = RIGHT;
		}
		if (self.spot == RIGHT && apple_loc [0] == w - inc) {
			self.spot = LEFT;
		}
		if (self.spot == UP && apple_loc [1] == 0) {
			self.spot = DOWN;
		}
		if (self.spot == DOWN && apple_loc [1] == h - inc) {
			self.spot = UP;
		}
		if (self.spot == LEFT) {
			self.locs = tuple ([self.apple_loc [0] - inc, self.apple_loc [1]]);
		}
		else if (self.spot == UP) {
			self.locs = tuple ([self.apple_loc [0], self.apple_loc [1] - inc]);
		}
		else if (self.spot == RIGHT) {
			self.locs = tuple ([self.apple_loc [0] + inc, self.apple_loc [1]]);
		}
		else if (self.spot == DOWN) {
			self.locs = tuple ([self.apple_loc [0], self.apple_loc [1] + inc]);
		}
	});},
	get draw_obstacle () {return __get__ (this, function (self) {
		if (self.block != null) {
			canvas.remove (self.block);
		}
		self.block = new fabric.Rect (dict ({'left': self.locs [0], 'top': self.locs [1], 'width': inc, 'height': inc, 'originX': 'left', 'originY': 'top', 'fill': 'black'}));
		self.block.hasControls = false;
		self.block.evented = false;
		self.block.selectable = false;
		canvas.add (self.block);
		self.in_place = true;
	});},
	get remove_obstacle () {return __get__ (this, function (self) {
		canvas.remove (self.block);
		self.in_place = false;
	});}
});
export var Mongoose =  __class__ ('Mongoose', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self) {
		self.locs = [0, 0];
		self.mongoose = null;
	});},
	get generate_mongoose () {return __get__ (this, function (self) {
		self.direction = int (Math.random () * 3) + 1;
		if (self.direction == LEFT) {
			self.locs [0] = w;
			self.locs [1] = int ((Math.random () * h) / inc) * inc;
		}
		if (self.direction == UP) {
			self.locs [0] = int ((Math.random () * w) / inc) * inc;
			self.locs [1] = h;
		}
		if (self.direction == RIGHT) {
			self.locs [0] = -(1) * inc;
			self.locs [1] = int ((Math.random () * h) / inc) * inc;
		}
		if (self.direction == DOWN) {
			self.locs [0] = int ((Math.random () * w) / inc) * inc;
			self.locs [1] = -(1) * inc;
		}
		self.hunting = true;
	});},
	get draw () {return __get__ (this, function (self) {
		if (self.mongoose != null) {
			canvas.remove (self.mongoose);
		}
		if (self.hunting) {
			if (self.direction == LEFT) {
				self.locs = [self.locs [0] - inc, self.locs [1]];
				if (self.locs [0] < 0) {
					self.die ();
				}
			}
			if (self.direction == UP) {
				self.locs = [self.locs [0], self.locs [1] - inc];
				if (self.locs [1] < 0) {
					self.die ();
				}
			}
			if (self.direction == RIGHT) {
				self.locs = [self.locs [0] + inc, self.locs [1]];
				if (self.locs [0] >= w) {
					self.die ();
				}
			}
			if (self.direction == DOWN) {
				self.locs = [self.locs [0], self.locs [1] + inc];
				if (self.locs [1] >= h) {
					self.die ();
				}
			}
			self.mongoose = new fabric.Rect (dict ({'left': self.locs [0], 'top': self.locs [1], 'width': inc, 'height': inc, 'originX': 'left', 'originY': 'top', 'fill': 'yellow'}));
			self.mongoose.hasControls = false;
			self.mongoose.evented = false;
			self.mongoose.selectable = false;
			canvas.add (self.mongoose);
		}
	});},
	get die () {return __get__ (this, function (self) {
		self.hunting = false;
		canvas.remove (self.mongoose);
	});}
});
export var py_update = function () {
	if (player != null) {
		moveCanvas ();
		changeColor ();
	}
	if (!(started) && start) {
		startTheGame ();
	}
	if (start && started && player != null) {
		player.py_update ();
		if (player.loc [0] == apple.loc [0] && player.loc [1] == apple.loc [1]) {
			apple.eat ();
			apple.spawn ();
			player.snake_length++;
			changeScore (player.snake_length - 1);
			if (player.snake_length - 1 > 5) {
				obstacle.generate_obstacle (apple.loc);
				if (!__in__ (obstacle.locs, player.coords)) {
					obstacle.draw_obstacle ();
				}
			}
			else if (obstacle.in_place) {
				obstacle.remove_obstacle ();
			}
		}
		if (obstacle.in_place && player.loc [0] == obstacle.locs [0] && player.loc [1] == obstacle.locs [1]) {
			alert ('You ran into an obstacle! Click OK to continue.');
			player.die ();
		}
		if (player.loc [0] < 0 || player.loc [0] >= w || player.loc [1] < 0 || player.loc [1] >= h) {
			alert ('You went out of bounds! Click OK to continue.');
			player.die ();
		}
		if (player.alive) {
			var update_time = 350 - 10 * (player.snake_length - 1);
			if (update_time <= 0) {
				var update_time = 1;
			}
			window.setTimeout (py_update, update_time);
		}
	}
	else {
		window.setTimeout (py_update, 500);
	}
};
export var focus = function () {
	var focus = !(focus);
};
export var pauseGame = function () {
	alert ('Game Paused. Click OK to continue.');
};
export var startTheGame = function () {
	canvas = new fabric.Canvas ('canvas', dict ({'width': w, 'height': h}));
	document.getElementById ('canvas').style.border = '5px solid black';
	player = Snake ();
	apple = Apple ();
	obstacle = Obstacle ();
	mongoose = Mongoose ();
	window.setTimeout (genMongoose, 2000);
	window.addEventListener ('keydown', player.turn, true);
	document.addEventListener ('click', player.turn_mobile);
	started = true;
};
py_update ();
export var draw_mongoose = function () {
	mongoose.draw ();
	checkMongooseOrDead ();
	if (mongoose.hunting) {
		window.setTimeout (draw_mongoose, 250);
	}
};
export var checkMongooseOrDead = function () {
	if (mongoose.hunting) {
		var index = 0;
		for (var coordinate of player.coords) {
			if (coordinate [0] == player.loc [0] && coordinate [1] == player.loc [1]) {
				continue;
			}
			if (mongoose.locs [0] == coordinate [0] && mongoose.locs [1] == coordinate [1]) {
				player.snake_length = index + 1;
				changeScore (player.snake_length - 1);
				break;
			}
			index++;
		}
		if (player.loc [0] == mongoose.locs [0] && player.loc [1] == mongoose.locs [1]) {
			mongoose.die ();
			player.snake_length += 2;
			changeScore (player.snake_length - 1);
		}
		var update_time = 50;
		if (update_time <= 0) {
			var update_time = 1;
		}
		window.setTimeout (checkMongooseOrDead, update_time);
	}
};
export var genMongoose = function () {
	if (start && started) {
		mongoose.generate_mongoose ();
		draw_mongoose ();
		window.setTimeout (genMongoose, ((250 * h) / inc) * 2);
	}
};
export var cv_mv = 1;
var left = 0;
export var top = 0;
export var m = null;
export var moveCanvas = function () {
	if (m != null) {
		window.clearTimeout (m);
	}
	if (start && started) {
		if (player.alive) {
			var cv = document.getElementById ('canvas');
			if (player.alive && player.snake_length - 1 >= 15) {
				if ((left + w) + 20 < window.innerWidth && mv_right) {
					left += cv_mv;
					if ((left + w) + 20 >= window.innerWidth) {
						mv_right = false;
					}
				}
				else if (!(mv_right)) {
					left -= cv_mv;
					if (left <= 0) {
						mv_right = true;
					}
				}
				if ((top + h) + 160 < window.innerHeight && mv_bottom) {
					top += cv_mv;
					if ((top + h) + 160 >= window.innerHeight) {
						mv_bottom = false;
					}
				}
				else if (!(mv_bottom)) {
					top -= cv_mv;
					if (top <= 0) {
						mv_bottom = true;
					}
				}
				cv.style.left = ('' + left) + 'px';
				cv.style.top = ('' + top) + 'px';
				cv.style.border = '5px solid black';
			}
		}
	}
	m = window.setTimeout (moveCanvas, 125);
};
export var mv_right = true;
export var mv_bottom = true;
export var t = null;
export var changeColor = function () {
	if (t != null) {
		window.clearTimeout (t);
	}
	if (start && started && player.alive && player.snake_length - 1 >= 10) {
		if (r > 0 && rd) {
			r--;
			if (r == 0) {
				rd = false;
			}
		}
		else if (!(rd)) {
			r++;
			if (r == 255) {
				rd = true;
			}
		}
		if (g > 0 && gd) {
			g--;
			if (g == 0) {
				gd = false;
			}
		}
		else if (!(gd)) {
			g++;
			if (g == 255) {
				gd = true;
			}
		}
		if (b > 0 && bd) {
			b--;
			if (b == 0) {
				bd = false;
			}
		}
		else if (!(bd)) {
			b++;
			if (b == 255) {
				bd = true;
			}
		}
		canvas.backgroundColor = ((((('rgb(' + r) + ',') + g) + ',') + b) + ')';
	}
	t = window.setTimeout (changeColor, 100);
};
var __left0__ = tuple ([int (255 * Math.random ()), int (255 * Math.random ()), int (255 * Math.random ())]);
export var r = __left0__ [0];
export var g = __left0__ [1];
export var b = __left0__ [2];
var __left0__ = tuple ([true, true, true]);
export var rd = __left0__ [0];
export var gd = __left0__ [1];
export var bd = __left0__ [2];

//# sourceMappingURL=snake.map