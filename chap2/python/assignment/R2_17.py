"""
R-2.17
Draw a class inheritance diagram for the following set of classes:
- Class Goat extends object and adds an instance variable _tail and
  methods milk() and jump().
- Class Pig extends object and adds an instance variable _nose and
  methods eat(food) and wallow().
- Class Horse extends object and adds instance variable _height and
  _color, and methods run() and race().
- Class Racer extends Horse and adds a method race().
- Calss Equestarian extends Horse, adding an instance variable _weight
  and methods trot() and is_trained().
"""

"""
                        object
        ----------------------------------
            Goat        Pig         Horse
            _tail       _nose       _height
                                    _color
            milk()      eat(food)   run()
            jump()      wallow()    jump()
                                    --------------------------
                                    Racer           Equestrian
                                                    _weight
                                    race()          trot()
                                                    is_trained()
"""
