# Model Deployment Notes

Run API:

uvicorn deployment.api:app --reload

Open docs:

http://127.0.0.1:8000/docs

Test API using POST /predict

Monitoring:

python monitoring/drift_checker.py
