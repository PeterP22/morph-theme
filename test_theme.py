#!/usr/bin/env python3
"""
Test file to showcase theme colors with Python syntax highlighting.
This module demonstrates various Python constructs for theme testing.
"""

import os
import sys
import json
import asyncio
from typing import List, Dict, Optional, Union, Tuple
from dataclasses import dataclass, field
from enum import Enum
from abc import ABC, abstractmethod
from functools import wraps
from datetime import datetime, timedelta

# Constants
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30.5
API_ENDPOINT = "https://api.example.com/v1"
REGEX_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Enum example
class Status(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

# Dataclass example
@dataclass
class Configuration:
    """Configuration settings for the application."""
    host: str = "localhost"
    port: int = 8080
    debug: bool = False
    timeout: float = DEFAULT_TIMEOUT
    retries: int = MAX_RETRIES
    features: List[str] = field(default_factory=list)
    metadata: Dict[str, any] = field(default_factory=dict)

# Decorator example
def retry(max_attempts: int = 3):
    """Decorator to retry a function on failure."""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    await asyncio.sleep(2 ** attempt)
            return None
        return wrapper
    return decorator

# Abstract base class
class DataProcessor(ABC):
    """Abstract base class for data processors."""
    
    def __init__(self, name: str, config: Configuration):
        self.name = name
        self.config = config
        self._cache: Dict[str, any] = {}
        self._is_running = False
        
    @abstractmethod
    async def process(self, data: Dict[str, any]) -> Dict[str, any]:
        """Process the input data."""
        pass
    
    @abstractmethod
    def validate(self, data: Dict[str, any]) -> bool:
        """Validate the input data."""
        pass
    
    def clear_cache(self) -> None:
        """Clear the internal cache."""
        self._cache.clear()

# Concrete implementation
class JSONProcessor(DataProcessor):
    """Processes JSON data with validation and transformation."""
    
    def __init__(self, name: str, config: Configuration, strict_mode: bool = True):
        super().__init__(name, config)
        self.strict_mode = strict_mode
        self.processed_count = 0
        self.error_count = 0
        
    async def process(self, data: Dict[str, any]) -> Dict[str, any]:
        """
        Process JSON data with error handling.
        
        Args:
            data: Input dictionary to process
            
        Returns:
            Processed dictionary with additional metadata
            
        Raises:
            ValueError: If data validation fails
            TypeError: If data is not a dictionary
        """
        if not isinstance(data, dict):
            raise TypeError(f"Expected dict, got {type(data).__name__}")
            
        if not self.validate(data):
            raise ValueError("Data validation failed")
        
        # Process the data
        result = {
            "timestamp": datetime.now().isoformat(),
            "processor": self.name,
            "status": Status.PROCESSING.value,
            "data": data,
            "metadata": {
                "strict_mode": self.strict_mode,
                "attempt": 1,
                "cache_size": len(self._cache)
            }
        }
        
        # Simulate async processing
        await asyncio.sleep(0.1)
        
        # Update counters
        self.processed_count += 1
        result["status"] = Status.COMPLETED.value
        
        return result
    
    def validate(self, data: Dict[str, any]) -> bool:
        """Validate the input data structure."""
        if not data:
            return False
            
        required_fields = ["id", "type", "payload"]
        return all(field in data for field in required_fields)
    
    @retry(max_attempts=MAX_RETRIES)
    async def fetch_remote_data(self, url: str) -> Optional[Dict]:
        """Fetch data from a remote API."""
        # Simulated API call
        await asyncio.sleep(0.5)
        
        if url.startswith(API_ENDPOINT):
            return {
                "success": True,
                "data": {"example": "data"},
                "timestamp": datetime.now().timestamp()
            }
        return None
    
    @staticmethod
    def parse_config(config_str: str) -> Dict[str, Union[str, int, bool]]:
        """Parse configuration string into dictionary."""
        try:
            return json.loads(config_str)
        except json.JSONDecodeError as e:
            print(f"Error parsing config: {e}")
            return {}
    
    @classmethod
    def from_file(cls, filepath: str, config: Configuration) -> "JSONProcessor":
        """Create a processor instance from a configuration file."""
        with open(filepath, 'r') as f:
            settings = json.load(f)
        
        return cls(
            name=settings.get("name", "default"),
            config=config,
            strict_mode=settings.get("strict_mode", True)
        )

# Generic class with type parameters
class Cache[T]:
    """Generic cache implementation with TTL support."""
    
    def __init__(self, ttl: timedelta = timedelta(minutes=5)):
        self._store: Dict[str, Tuple[T, datetime]] = {}
        self.ttl = ttl
        
    def get(self, key: str) -> Optional[T]:
        """Get value from cache if not expired."""
        if key in self._store:
            value, timestamp = self._store[key]
            if datetime.now() - timestamp < self.ttl:
                return value
            del self._store[key]
        return None
    
    def set(self, key: str, value: T) -> None:
        """Store value in cache with current timestamp."""
        self._store[key] = (value, datetime.now())
    
    def __contains__(self, key: str) -> bool:
        """Check if key exists and is not expired."""
        return self.get(key) is not None
    
    def __len__(self) -> int:
        """Return number of items in cache."""
        return len(self._store)

# Example function with various syntax elements
async def main():
    """Main entry point for testing the theme."""
    # Initialize configuration
    config = Configuration(
        host="0.0.0.0",
        port=9000,
        debug=True,
        features=["auth", "logging", "metrics"],
        metadata={"version": "1.0.0", "environment": "development"}
    )
    
    # Create processor
    processor = JSONProcessor("main_processor", config)
    
    # Test data
    test_data = {
        "id": "12345",
        "type": "user_event",
        "payload": {
            "user_id": 42,
            "action": "login",
            "timestamp": datetime.now().isoformat()
        }
    }
    
    # Process data
    try:
        result = await processor.process(test_data)
        print(f"✅ Processing successful: {result['status']}")
        
        # Test cache
        cache: Cache[Dict] = Cache()
        cache.set("result", result)
        
        if "result" in cache:
            cached = cache.get("result")
            print(f"📦 Cached data retrieved: {cached['processor']}")
            
    except (ValueError, TypeError) as e:
        print(f"❌ Error: {e}")
        processor.error_count += 1
    finally:
        print(f"📊 Stats - Processed: {processor.processed_count}, Errors: {processor.error_count}")
    
    # Lambda function example
    square = lambda x: x ** 2
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(square, numbers))
    
    # List comprehension
    even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
    
    # Dictionary comprehension
    word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
    
    # Generator expression
    sum_of_squares = sum(x ** 2 for x in range(100))
    
    # F-string formatting
    name = "Theme Tester"
    version = 1.0
    message = f"Running {name} v{version:.1f} with {len(numbers)} items"
    
    # Multi-line string
    description = """
    This is a multi-line string that demonstrates
    how the theme handles longer text blocks
    with multiple lines and indentation.
    """
    
    # Binary, octal, and hex numbers
    binary_num = 0b101010  # 42 in binary
    octal_num = 0o52      # 42 in octal  
    hex_num = 0x2A        # 42 in hexadecimal
    
    # Complex numbers
    complex_num = 3 + 4j
    
    # Boolean operations
    is_valid = True and not False
    should_continue = (processor.processed_count > 0) or config.debug
    
    # Walrus operator (Python 3.8+)
    if (n := len(numbers)) > 3:
        print(f"List has {n} items")
    
    # Match statement (Python 3.10+)
    status = Status.COMPLETED
    match status:
        case Status.PENDING:
            print("Waiting to start...")
        case Status.PROCESSING:
            print("In progress...")
        case Status.COMPLETED:
            print("✓ Done!")
        case Status.FAILED | Status.CANCELLED:
            print("✗ Did not complete")
        case _:
            print("Unknown status")
    
    return result

# Run the async main function
if __name__ == "__main__":
    print("🎨 Theme Test Suite")
    print("=" * 50)
    
    # Create event loop and run
    loop = asyncio.get_event_loop()
    try:
        result = loop.run_until_complete(main())
        print("\n✨ Test completed successfully!")
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
    finally:
        loop.close()
        print("👋 Goodbye!")