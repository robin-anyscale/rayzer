# serve_app.py
import time
import random
import numpy as np
from typing import Dict

import ray
from ray import serve
from fastapi import FastAPI
import xgboost as xgb

app = FastAPI()

@serve.deployment(
    num_replicas="auto",
    ray_actor_options={"num_cpus": 0.5,
                    #    "num_gpus": 0.5 ## Uncomment to use GPUs
                       },
    autoscaling_config={
        "min_replicas": 1,
        "max_replicas": 20,  # Increase based on your cluster capacity
        "target_num_ongoing_requests_per_replica": 2,  # Lower value = more aggressive scaling
        "upscale_delay_s": 5,  # Reduce delay before scaling up (default is 60s)
        "downscale_delay_s": 60,  # Keep resources longer
        "smoothing_factor": 0.2,  # Lower value = more responsive to traffic spikes
    }
)
@serve.ingress(app)
class XGBoostModel:
    def __init__(self):
        # Create a dummy XGBoost model
        print("Initializing XGBoost model...")
        
        # Create some synthetic data for training
        n_samples = 1000
        n_features = 20
        X = np.random.rand(n_samples, n_features)
        y = np.random.randint(0, 2, n_samples)  # Binary classification
        
        # Create DMatrix
        dtrain = xgb.DMatrix(X, label=y)
        
        # Set XGBoost parameters
        params = {
            'max_depth': 3,
            'eta': 0.1,
            'objective': 'binary:logistic',
            'eval_metric': 'logloss',
            'seed': 42
        }
        
        # Train the model
        print("Training XGBoost model...")
        self.model = xgb.train(params, dtrain, num_boost_round=10)
        print("XGBoost model trained successfully")
        
        # Save feature dimension for inference
        self.n_features = n_features
        
    @app.get("/")
    async def root(self):
        return {"status": "healthy"}
    
    @app.post("/predict")
    async def predict(self, data: Dict):
        # Extract complexity to simulate different workloads
        complexity = data.get("complexity", 1.0)
        complexity = min(max(complexity, 0.1), 5.0)  # Bound between 0.1 and 5.0
        
        # Get features from request or generate random ones
        features = data.get("features", None)
        if features is None or len(features) != self.n_features:
            # Generate random features if not provided correctly
            features = np.random.rand(self.n_features).tolist()
        
        # Start timing
        start_time = time.time()
        
        # Create DMatrix for prediction
        dtest = xgb.DMatrix(np.array([features]))
        
        # Make prediction
        prediction = self.model.predict(dtest)
        
        # Add some artificial delay based on complexity to simulate more processing
        if random.random() < 0.1:  # 10% of requests take longer
            time.sleep(0.5 * complexity)
            
        processing_time = time.time() - start_time
        
        return {
            "prediction": float(prediction[0]),
            "probability": float(prediction[0]),
            "processing_time": processing_time,
            "complexity": complexity,
            "instance_id": ray.get_runtime_context().get_node_id()
        }

app = XGBoostModel.bind()