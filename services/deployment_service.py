import logging
import traceback

class DeploymentService:
    def deploy_code(self, code):
        if not code.strip():
            logging.error("Deployment Service: No code to deploy.")
            return {"status": "Failed", "error": "No valid code to deploy."}

        try:
            exec_globals = {}
            exec(code, exec_globals)
            logging.info("Deployment Service: Code executed successfully.")
            return {"status": "Deployed"}
        except Exception as e:
            logging.error(f"Deployment Service: Deployment failed with error: {traceback.format_exc()}")
            return {"status": "Failed", "error": str(e)}
