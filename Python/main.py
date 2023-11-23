import io

class HelloWorld:
    instance = None

    @staticmethod
    def main():
        HelloWorld.instantiate_hello_world_main_class_and_run()

    @staticmethod
    def instantiate_hello_world_main_class_and_run():
        HelloWorld.instance = HelloWorld()

    def __init__(self):
        factory = HelloWorldFactory.get_instance()
        hello_world = factory.create_hello_world()
        hello_world_string = hello_world.get_hello_world()
        print_strategy = hello_world.get_print_strategy()
        code = hello_world.print(print_strategy, hello_world_string)
        if code.get_status_code() != 0:
            raise Exception("Failed to print: " + str(code.get_status_code()))

class StringFactory:
    instance = None

    @staticmethod
    def get_instance():
        if StringFactory.instance is None:
            StringFactory.instance = StringFactory()
        return StringFactory.instance

    def create_hello_world_string(self, str):
        s = HelloWorldString()
        s.s = str
        return s

class PrintStrategyFactory:
    instance = None

    @staticmethod
    def get_instance():
        if PrintStrategyFactory.instance is None:
            PrintStrategyFactory.instance = PrintStrategyFactory()
        return PrintStrategyFactory.instance

    def create_iprint_strategy(self):
        print_strategy = PrintStrategyImplementation()
        code = print_strategy.setup_printing()
        if code.get_status_code() != 0:
            raise Exception("Failed to create IPrintStrategy: " + str(code.get_status_code()))
        return print_strategy

class PrintStrategyImplementation:
    def setup_printing(self):
        try:
            self.print = io.BytesIO()  # Имитация потока вывода
            return StatusCodeImplementation(0)
        except Exception as e:
            return StatusCodeImplementation(-1)

    def print(self, string):
        try:
            self.print.write(string.get_hello_world_string().encode('UTF-8'))
            return StatusCodeImplementation(0)
        except Exception as e:
            return StatusCodeImplementation(-1)

class StatusCodeImplementation:
    def __init__(self, code):
        self.code = code

    def get_status_code(self):
        return self.code

class HelloWorldString:
    s = ""

    def get_hello_world_string(self):
        return self.s

class HelloWorldStringImplementation:
    def get_hello_world_string(self):
        factory = StringFactory.get_instance()
        s = factory.create_hello_world_string("Hello, World!")
        return s

class HelloWorldFactory:
    instance = None

    @staticmethod
    def get_instance():
        if HelloWorldFactory.instance is None:
            HelloWorldFactory.instance = HelloWorldFactory()
        return HelloWorldFactory.instance

    def create_hello_world(self):
        hello_world = HelloWorldImplementation()
        return hello_world

class HelloWorldImplementation:
    def get_hello_world(self):
        string = HelloWorldStringImplementation()
        return string

    def get_print_strategy(self):
        factory = PrintStrategyFactory.get_instance()
        return factory.create_iprint_strategy()

    def print(self, strategy, to_print):
        code = strategy.print(to_print)
        return code

# Точка входа
if __name__ == "__main__":
    HelloWorld.main()
