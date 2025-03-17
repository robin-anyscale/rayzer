# load_test.py
import time
import json
import random
import argparse
import requests
import threading
import concurrent.futures
from typing import Dict
import numpy as np
# import matplotlib.pyplot as plt
from datetime import datetime

class LoadTester:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.predict_url = f"{self.base_url}/predict"
        self.results = []
        self.instance_counts = {}
        self.lock = threading.Lock()
        
    def make_request(self, complexity: float) -> Dict:
        """Make a single request to the prediction endpoint"""
        try:
            payload = {"complexity": complexity}
            start_time = time.time()
            response = requests.post(self.predict_url, json=payload, timeout=30)
            end_time = time.time()
            
            if response.status_code == 200:
                result = response.json()
                result['latency'] = end_time - start_time
                result['timestamp'] = datetime.now().strftime('%H:%M:%S')
                
                with self.lock:
                    self.results.append(result)
                    instance_id = result.get('instance_id', 'unknown')
                    if instance_id in self.instance_counts:
                        self.instance_counts[instance_id] += 1
                    else:
                        self.instance_counts[instance_id] = 1
                
                return result
            else:
                print(f"Error: {response.status_code} - {response.text}")
                return {"error": response.status_code}
        except Exception as e:
            print(f"Request failed: {str(e)}")
            return {"error": str(e)}
    
    def run_load_test(self, 
                      requests_per_second: int, 
                      test_duration: int,
                      complexity_range: tuple = (0.5, 2.0),
                      ramp_up: bool = True):
        """
        Run a load test with specified RPS
        
        Args:
            requests_per_second: Target RPS
            test_duration: Test duration in seconds
            complexity_range: Range of complexity values
            ramp_up: Whether to gradually ramp up load
        """
        print(f"Starting load test: {requests_per_second} RPS for {test_duration} seconds")
        
        # For tracking actual RPS achieved
        actual_rps_values = []
        timestamp_values = []
        active_instances = []
        instance_counts_over_time = []
        
        # Calculate delay between requests to achieve desired RPS
        delay = 1.0 / requests_per_second if requests_per_second > 0 else 0
        
        # Setup thread pool for concurrent requests
        max_workers = min(50, requests_per_second * 2)  # Limit number of threads
        
        start_time = time.time()
        end_time = start_time + test_duration
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            
            # Track stats per second
            last_second = start_time
            requests_this_second = 0
            
            current_time = time.time()
            while current_time < end_time:
                # Calculate current target RPS if ramping up
                if ramp_up:
                    elapsed = current_time - start_time
                    progress = min(1.0, elapsed / (test_duration * 0.5))  # Ramp up in first half
                    current_rps = requests_per_second * progress
                else:
                    current_rps = requests_per_second
                
                current_delay = 1.0 / current_rps if current_rps > 0 else 0
                
                # Generate random complexity value
                complexity = random.uniform(complexity_range[0], complexity_range[1])
                
                # Submit request
                future = executor.submit(self.make_request, complexity)
                futures.append(future)
                requests_this_second += 1
                
                # Calculate stats each second
                if current_time - last_second >= 1.0:
                    # Record actual RPS
                    actual_rps_values.append(requests_this_second)
                    timestamp_values.append(int(current_time - start_time))
                    
                    # Count active instances
                    with self.lock:
                        instance_counts_over_time.append(len(self.instance_counts))
                    
                    print(f"Time: {int(current_time - start_time)}s, "
                          f"Actual RPS: {requests_this_second}, "
                          f"Active instances: {instance_counts_over_time[-1]}")
                    
                    last_second = current_time
                    requests_this_second = 0
                
                # Sleep to maintain RPS
                time.sleep(current_delay)
                current_time = time.time()
        
        # Wait for all pending requests to complete
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Request failed: {str(e)}")
        
        # Print final stats
        total_time = time.time() - start_time
        total_requests = len(self.results)
        actual_rps = total_requests / total_time
        
        print("\n===== Load Test Results =====")
        print(f"Test duration: {total_time:.2f} seconds")
        print(f"Total requests: {total_requests}")
        print(f"Average RPS: {actual_rps:.2f}")
        print(f"Unique instances seen: {len(self.instance_counts)}")
        print("Instance distribution:")
        for instance, count in sorted(self.instance_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"  {instance}: {count} requests ({count/total_requests*100:.1f}%)")
        
        # Calculate latency statistics
        latencies = [r['latency'] for r in self.results if 'latency' in r]
        if latencies:
            avg_latency = sum(latencies) / len(latencies)
            p50 = sorted(latencies)[int(len(latencies) * 0.5)]
            p95 = sorted(latencies)[int(len(latencies) * 0.95)]
            p99 = sorted(latencies)[int(len(latencies) * 0.99)]
            
            print("\nLatency Statistics:")
            print(f"  Average: {avg_latency*1000:.2f} ms")
            print(f"  p50: {p50*1000:.2f} ms")
            print(f"  p95: {p95*1000:.2f} ms")
            print(f"  p99: {p99*1000:.2f} ms")
        
        # Generate plots
        # self.plot_results(actual_rps_values, timestamp_values, instance_counts_over_time)
        
        return {
            "total_requests": total_requests,
            "actual_rps": actual_rps,
            "unique_instances": len(self.instance_counts),
            "avg_latency_ms": avg_latency * 1000 if latencies else None
        }
    
    def plot_results(self, actual_rps_values, timestamp_values, instance_counts):
        """Generate plots showing test results"""
        plt.figure(figsize=(12, 10))
        
        # Plot 1: RPS over time
        plt.subplot(2, 1, 1)
        plt.plot(timestamp_values, actual_rps_values, 'b-')
        plt.title('Requests Per Second Over Time')
        plt.xlabel('Time (seconds)')
        plt.ylabel('RPS')
        plt.grid(True)
        
        # Plot 2: Instances over time
        plt.subplot(2, 1, 2)
        plt.plot(timestamp_values, instance_counts, 'r-')
        plt.title('Active Instances Over Time')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Number of Instances')
        plt.grid(True)
        
        plt.tight_layout()
        plt.savefig('load_test_results.png')
        print("Results plotted to load_test_results.png")
        
        # Plot latency distribution
        latencies = [r['latency'] * 1000 for r in self.results if 'latency' in r]  # Convert to ms
        if latencies:
            plt.figure(figsize=(10, 6))
            plt.hist(latencies, bins=50, alpha=0.75)
            plt.title('Latency Distribution')
            plt.xlabel('Latency (ms)')
            plt.ylabel('Count')
            plt.grid(True)
            plt.savefig('latency_distribution.png')
            print("Latency distribution plotted to latency_distribution.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Load test Ray Serve deployment')
    parser.add_argument('--url', type=str, default="http://localhost:8000",
                        help='URL of the Ray Serve deployment')
    parser.add_argument('--rps', type=int, default=1,
                        help='Target requests per second')
    parser.add_argument('--duration', type=int, default=60,
                        help='Test duration in seconds')
    parser.add_argument('--min-complexity', type=float, default=0.5,
                        help='Minimum request complexity')
    parser.add_argument('--max-complexity', type=float, default=2.0,
                        help='Maximum request complexity')
    parser.add_argument('--ramp-up', action='store_true',
                        help='Gradually ramp up load')
    
    args = parser.parse_args()
    
    tester = LoadTester(args.url)
    tester.run_load_test(
        requests_per_second=args.rps,
        test_duration=args.duration,
        complexity_range=(args.min_complexity, args.max_complexity),
        ramp_up=args.ramp_up
    )