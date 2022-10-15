"""
Replace method with method object

This issue is typical when you have a long method that uses local variables in such a way that you cannot apply extract method.

Sometimes its useful to encapsulate a function into its own object (called a ``command object``). This object is usually based around a single
method, whose request and execution is the sole purpose of this object.

NOTE: Command in this context is an object that encapsulates a request, following the command pattern in Design Patterns. The example provides
    a ``command object`` to set the context and the ``command`` afterwards. Normally seen as a ``Behavioral Design Pattern``.

Some Benefits:

* Greater flexibility for the control an expression of a function than a standard function
* Commands can have complimentary expressions (i.e. rolling back changes from the command)
* Additional methods of the object can help facilitate the breakdown of the logic
"""
from abc import ABC, abstractmethod

# Bad
def score(candidate, medical_exam, scoring_guide):
    result = 0
    health_level = 0
    high_medical_risk_flag = False 

    if medical_exam.is_smoker:
        health_level += 10
        high_medical_risk_flag = True 
    
    certification_grade = "regular"

    if scoring_guide.state_with_low_certification(candidate.origin_state):
        certification_grade = "low"
        result -= 5

    # Lots more code like this
    result -= max(health_level - 5, 0)
    return result

# Good
class ICommand(ABC):

    @abstractmethod
    def execute(self):
        pass 


class Scorer(ICommand):

    def __init__(self, candidate, medical_exam, scoring_guide) -> None:
        # Factored out as instance variables
        self._candidate = candidate
        self._medical_exam = medical_exam
        self._scoring_guide = scoring_guide

    def execute(self):
        self._result = 0
        self._health_level = 0
        self._high_medical_risk_flag = False 

        # Extract method
        self.score_smoking()
        
        certification_grade = "regular"

        # Extract method
        self.score_based_on_origin(certification_grade)

        # Lots more code like this
        self._result -= max(self._health_level - 5, 0)
        return self._result

    def score_smoking(self):
        if self._medical_exam.is_smoker:
            self._health_level += 10
            self._high_medical_risk_flag = True  
    
    def score_based_on_origin(self, certification_grade):
        if self._scoring_guide.state_with_low_certification(self._candidate.origin_state):
            certification_grade = "low"
            self._result -= 5