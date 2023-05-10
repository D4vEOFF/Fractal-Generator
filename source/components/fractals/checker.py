
lsystem_keys = ["name", "axiom", "rules", "rotateByAngle"]

def is_LSystem(fractal: dict) -> bool:
    """Checks whether given dictionary contains proper keys specific for LSystem."""

    key_presence = [key in fractal.keys() for key in lsystem_keys]

    # Key is missing
    if False in key_presence:
        return False
    
    return True