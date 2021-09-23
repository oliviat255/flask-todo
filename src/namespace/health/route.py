from flask_restx import Resource, Namespace

health_ns = Namespace("health", description="health check")

@health_ns.route("/api", strict_slashes=False)
class Healthcheck(Resource): 
    """API Healthcheck class""" 
    @health_ns.response(200, "Success")
    def get(self): 
        return{"message": "application healthy"}