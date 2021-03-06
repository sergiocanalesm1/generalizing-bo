from django.db import models

class Domain(models.TextChoices):
    COMPUTER_SCIENCE = 'Computer Science'
    PHYSICS = 'Physics'
    PHILOSOPHY = 'Philosophy'
    DESIGN = 'Design'
    ART = 'Art'
    ELECTRICAL_ENGINEERING = 'Electrical Engineering'
    SOFTWARE_ENGINEERING = 'Software Engineering'
    AEROSPACE_ENGINEERING = 'Aerospace Engineering'
    MEHCANICAL_ENGINEERING = 'Mechanical Engineering'
    BIOLOGY = 'Biology'
    CHEMESTRY = 'Chemestry'
    MATHEMATICS = 'Mathematics'
    LITERATURE = 'Literature'
    MUSIC = 'Music'
    LAW = 'Law'
    BUSINESS = 'Business'
    ECONOMICS = 'Economics'
    POLITICAL_SCIENCE = 'Political Science'
    ARCHITECTURE = 'Architecture'
    ANTHROPOLOGY = 'Anthropology'
    MEDICINE  = 'Medicine'
    EDUCATION = 'Education'
    PSYCOLOGY = 'Psychology'
    SPORTS = 'Sports'
    NEUROSCIENCE = 'Neuroscience'
    AGRICULTURE = 'Agriculture'
    HISTORY = 'History'
    OTHER = 'Other'