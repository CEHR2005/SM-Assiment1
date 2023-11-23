"""Module docstring:
This module demonstrates implementation of a HelloWorld program in Python."""
import io


class HelloWorld:
    """Represents the main HelloWorld application."""
    instance = None

    @classmethod
    def main(cls):
        """Main method to start the HelloWorld application."""
        cls.instantiate_hello_world_main_class_and_run()

    @classmethod
    def instantiate_hello_world_main_class_and_run(cls):
        """Instantiates the HelloWorld main class and performs setup."""
        cls.instance = HelloWorld()

    def __init__(self):
        """Initializes the HelloWorld class and runs the hello world logic."""
        factory = HelloWorldFactory.get_instance()
        hello_world = factory.create_hello_world()
        hello_world_string = hello_world.get_hello_world()
        print_strategy = hello_world.get_print_strategy()
        code = hello_world.print_hello_world(print_strategy,
                                             hello_world_string)
        if code.get_status_code() != 0:
            raise RuntimeError(f"Failed to print: {code.get_status_code()}")


class StringFactory:
    """Factory class for creating HelloWorldString instances."""
    _instance = None

    @classmethod
    def get_instance(cls):
        """Returns the singleton instance of StringFactory."""
        if cls._instance is None:
            cls._instance = StringFactory()
        return cls._instance

    def create_hello_world_string(self, string):
        """Creates a new HelloWorldString object with the provided string."""
        hello_world_string = HelloWorldString()
        hello_world_string.s = string
        return hello_world_string


class PrintStrategyFactory:
    """Factory class for creating IPrintStrategy instances."""
    _instance = None

    @classmethod
    def get_instance(cls):
        """Returns the singleton instance of PrintStrategyFactory."""
        if cls._instance is None:
            cls._instance = PrintStrategyFactory()
        return cls._instance

    def create_iprint_strategy(self):
        """Creates and returns an IPrintStrategy object."""
        print_strategy = PrintStrategyImplementation()
        code = print_strategy.setup_printing()
        if code.get_status_code() != 0:
            raise RuntimeError(
                f"Failed to create IPrintStrategy: {code.get_status_code()}"
            )
        return print_strategy


class PrintStrategyImplementation:
    """Implements the printing strategy for HelloWorldString."""

    def __init__(self):
        self.print_stream = None

    def setup_printing(self):
        """Sets up printing resources."""
        try:
            self.print_stream = io.BytesIO()
            return StatusCodeImplementation(0)
        except IOError:
            return StatusCodeImplementation(-1)

    def print_hello_world(self, string):
        """Prints the HelloWorldString."""
        try:
            self.print_stream.write(
                string.get_hello_world_string().encode('UTF-8')
            )
            return StatusCodeImplementation(0)
        except IOError:
            return StatusCodeImplementation(-1)


class StatusCodeImplementation:
    """Represents the status code returned by various operations."""

    def __init__(self, code):
        """Initializes the status code."""
        self.code = code

    def get_status_code(self):
        """Returns the status code."""
        return self.code


class HelloWorldString:
    """Represents a simple string specifically for the HelloWorld message."""

    def __init__(self):
        """Initializes the HelloWorldString with an empty string."""
        self.s = ""

    def get_hello_world_string(self):
        """Returns the HelloWorld string."""
        return self.s


class HelloWorldStringImplementation:
    """Implements the IHelloWorldString interface for HelloWorld."""

    def get_hello_world_string(self):
        """Returns a HelloWorldString instance with a predefined message."""
        factory = StringFactory.get_instance()
        s = factory.create_hello_world_string("Hello, World!")
        return s


class HelloWorldImplementation:
    """Implementation of the IHelloWorld interface."""

    def get_hello_world(self):
        """Returns an instance of IHelloWorldString."""
        string = HelloWorldStringImplementation()
        return string

    def get_print_strategy(self):
        """Returns an instance of IPrintStrategy."""
        factory = PrintStrategyFactory.get_instance()
        return factory.create_iprint_strategy()

    def print_hello_world(self, strategy, to_print):
        """Uses the provided print strategy to print the HelloWorldString."""
        code = strategy.print_hello_world(to_print)
        return code


class HelloWorldFactory:
    """Factory class for creating HelloWorld inst."""
    _instance = None

    @classmethod
    def get_instance(cls):
        """Returns the singleton instance of HelloWorldFactory."""
        if cls._instance is None:
            cls._instance = HelloWorldFactory()
        return cls._instance

    def create_hello_world(self):
        """Creates and returns a HelloWorld object."""
        hello_world = HelloWorldImplementation()

        return hello_world
