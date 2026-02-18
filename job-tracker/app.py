from flask import Flask

# load configuration (env vars etc)
import config

from services import health_bp, db_bp, submit_bp, jobs_bp, profiles_bp

app = Flask(__name__)

app.register_blueprint(health_bp)
app.register_blueprint(db_bp)
app.register_blueprint(submit_bp)
app.register_blueprint(jobs_bp)
app.register_blueprint(profiles_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
