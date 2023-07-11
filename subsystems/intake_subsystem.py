import ctre
from commands2 import SubsystemBase


class IntakeSubsystem(SubsystemBase):
    # Create a new ArmSubsystem

    def __init__(self) -> None:
        super().__init__()

        self.intake_motor = ctre.WPI_TalonFX(1)

    def set_motor_speed(self, speed):
        self.intake_motor.set(speed)
