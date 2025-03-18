class LLMTailor:
    def __init__(self, model):
        self.model = model

    def tailor_cv(self, cv_text, job_spec):
        tailored_cv = self.model.generate(cv_text, job_spec)
        return tailored_cv