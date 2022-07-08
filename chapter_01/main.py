import sys

from duck import ModelDuck, WildDuck
from fly_behavior import FlyBehavior, FlyRocketPowered


def main():
    exit_code = 0
    try:
        wild_duck: WildDuck = WildDuck()
        wild_duck.display()
        wild_duck.swim()
        wild_duck.perform_quack()
        wild_duck.perform_fly()

        print('\n')
        model_duck: ModelDuck = ModelDuck()
        model_duck.display()
        model_duck.swim()
        model_duck.perform_quack()
        model_duck.perform_fly()
        model_duck.set_fly_behavior(FlyRocketPowered())
        print('Upgrading flight behavior')
        model_duck.perform_fly()

    except Exception as exception:
        print(f"ERROR: executing chapter 1 exercise")
        print(f"EXCEPTION: {exception}")
        exit_code = 1
    finally:
        sys.exit(exit_code)


if __name__ == '__main__':
    main()
