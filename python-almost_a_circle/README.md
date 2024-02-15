
<h1><p align="center"> Python - Almost a Circle </h1></p></font>

Welcome to the "Almost a Circle" project! Here, I've applied my Python object-oriented programming skills by implementing three interconnected classes to represent rectangles and squares. To ensure the functionality of each class, I've developed a comprehensive test suite using the `unittest` module.

Throughout this project, I've harnessed various Python tools and concepts, including:

- Import
- Exceptions
- Private attributes
- Getter/setter methods
- Class/static methods
- Inheritance
- File I/O
- `args`/`kwargs`
- JSON and CSV serialization/deserialization
- Unittesting

## Tests :

Explore the tests in the [tests/test_models](./tests/test_models) directory, which contains independently-developed test files:

- [test_base.py](./tests/test_models/test_base.py)
- [test_rectangle.py](./tests/test_models/test_rectangle.py)
- [test_square.py](./tests/test_models/test_square.py)

## Classes
### Base
The "Base" class serves as the foundation for all other classes in the project and includes the following features:

- Private class attribute `__nb_objects = 0`.
- Public instance attribute `id`.
- Class constructor `def __init__(self, id=None):`
- If `id` is `None`, increments `__nb_objects` and assigns its value to the public instance attribute `id`.
- Otherwise, sets the public instance attribute `id` to the provided `id`.
- Static method `def to_json_string(list_dictionaries):` returns the JSON string serialization of a list of dictionaries.
  - Returns `"[]"` if `list_dictionaries` is `None` or empty.
- Class method `def save_to_file(cls, list_objs):` writes the JSON serialization of a list of objects to a file.
  - Saves an empty list if `list_objs` is `None`.
  - The file is saved with the name `<cls name>.json` (e.g., `Rectangle.json`).
  - Overwrites the file if it already exists.
- Static method `def from_json_string(json_string):` returns a list of objects deserialized from a JSON string.
  - Returns an empty list if `json_string` is `None` or empty.
- Class method `def create(cls, **dictionary):` instantiates an object with provided attributes.
- Class method `def load_from_file(cls):` returns a list of objects instantiated from a JSON file.
  - Returns an empty list if the file does not exist..
- Static method `def draw(list_rectangles, list_squares):` draws `Rectangle` and `Square` instances in a GUI window using the `turtle` module.

### Rectangle
Represents a rectangle and inherits from `Base`. Features include:

- Private instance attributes `__width`, `__height`, `__x`, and `__y`.
  - Each attribute has its own getter/setter.
- Class constructor `def __init__(self, width, height, x=0, y=0, id=None):`
  - Raises `TypeError` and `ValueError` exceptions for invalid attribute values.
- Public method `def area(self):` returns the area of the `Rectangle` instance.
- Public method `def display(self):` prints the `Rectangle` instance to `stdout` using the `#` character.
- Overwrites `__str__` method to print a `Rectangle` instance in the format `[Rectangle] (<id>) <x>/<y>`.
- Public method `def update(self, *args, **kwargs):` updates an instance of a `Rectangle` with given attributes.
- Public method `def to_dictionary(self):` returns the dictionary representation of a `Rectangle` instance.

### Square
Represents a square and inherits from `Rectangle`. Features include:

- Class constructor `def __init__(self, size, x=0, y=0, id=None):`
  - Assigns the `width` and `height` of the `Rectangle` superclass using the value of `size`.
- Overwrites `__str__` method to print a `Square` instance in the format `[Square] (<id>) <x>/<y>`.
- Public method `def update(self, *args, **kwargs):` updates an instance of a `Square` with given attributes.
- Public method `def to_dictionary(self):` returns the dictionary representation of a `Square`.

## Tasks 
| Task  |  Name of the task               | demanded work |
| :-------- |  :------------------------- | :------------------------- |
| `Task 0`| 0. If it's not tested it doesn't work| All the files, classes and methods must be unit tested and be PEP 8 validated.       |
| `Task 1`| 1. Base class| create a class constructor: __init__(self, id=None) .  |
| `Task 2`| 2. First Rectangle| Write the class Rectangle that inherits from Base.    |
| `Task 3`| 3. Validate attributes| Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded).          |
|`Task 4` | 4. Area first| Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.     |
| `Task 5`|5. Display #0 | Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - without handling x and y .          |
| `Task 6`|6. __str__ |Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height> .          |
| `Task 7`|7. Display #1 | Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y.  |
| `Task 8`| 8. Update #0| Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute.          |
|`Task 9` |9. Update #1 |Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes.           |
| `Task 10`|10. And now, the Square! | Write the class Square that inherits from Rectangle.          |
| `Task 11`|11. Square size |Update the class Square by adding the public getter and setter size.           |
| `Task 12`|12. Square update | Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes.          |
| `Task 13`| 13. Rectangle instance to dictionary representation| Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle.          |
|`Task 14` | 14. Square instance to dictionary representation| Update the class Square by adding the public method  to_dictionary(self): that returns the dictionary representation of a Squar.          |
| `Task 15`|15. Dictionary to JSON string | Update the class Base by adding the static method  to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries.          |
| `Task 16`|16. JSON string to file |Update the class Base by adding the class method  save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file.           |
| `Task 17`|17. JSON string to dictionary |Update the class Base by adding the static method  from_json_string(json_string): that returns the list of the JSON string representation json_string.          |
| `Task 18`|18. Dictionary to Instance |Update the class Base by adding the class method create(cls, **dictionary): that returns an instance with all attributes already set.           |
|`Task 19` |19. File to instances |  Update the class Base by adding the class method load_from_file(cls): that returns a list of instances.     |
### Advanced Task 
| Task  |  Name of the task               | demanded work |
| :-------- |  :------------------------- | :------------------------- |
| `Task 20`| 20. Let's draw it| Update the class Base by adding the static method draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares |



## Authors

- [@ChaimaBSlima](https://github.com/ChaimaBSlima)


## 🚀 About Me
I'm a Machine Learning developer...

