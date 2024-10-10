Building your first FastAPI application is straightforward. Here’s a step-by-step guide to creating, running, and testing a simple FastAPI app.

### Step 1: Install FastAPI and an ASGI Server

First, ensure you have Python installed. Then, install FastAPI and an ASGI server like `uvicorn` using pip:

```bash
pip install fastapi uvicorn
```

### Step 2: Create Your FastAPI Application

1. Create a new directory for your project:
   ```bash
   mkdir my_fastapi_app
   cd my_fastapi_app
   ```

2. Create a new Python file, e.g., `main.py`, and open it in your text editor.

3. Write the following code in `main.py`:

   ```python
   from fastapi import FastAPI

   app = FastAPI()

   @app.get("/")
   def read_root():
       return {"Hello": "World"}

   @app.get("/items/{item_id}")
   def read_item(item_id: int, q: str = None):
       return {"item_id": item_id, "query": q}
   ```

### Step 3: Run Your FastAPI Application

To run the application, use the following command in your terminal:

```bash
uvicorn main:app --reload
```

- `main` refers to the filename `main.py`.
- `app` refers to the FastAPI instance created in that file.
- `--reload` enables auto-reloading for development, so the server restarts on code changes.

### Step 4: Access Your Application

Once the server is running, you can access it in your web browser or API client:

- Open your browser and go to: `http://127.0.0.1:8000/`
  - You should see: `{"Hello": "World"}`

- To test the item endpoint, go to: `http://127.0.0.1:8000/items/5?q=test`
  - You should see: `{"item_id": 5, "query": "test"}`

### Step 5: Explore the Interactive API Documentation

FastAPI automatically generates interactive API documentation. You can access it at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### Conclusion

You've successfully built and run your first FastAPI application! You can now expand this app by adding more routes, handling different HTTP methods, integrating with databases, and more. If you have any further questions or need additional features, feel free to ask!











### Easy Questions

1. **What is FastAPI?**
   - **Use Case:** Understanding the framework's purpose and advantages for building APIs.
   - **Code Example:** N/A (Conceptual)

2. **How do you create a simple FastAPI application?**
   - **Use Case:** Setting up a basic API to serve data or handle requests.
   - **Code Example:**
     ```python
     from fastapi import FastAPI

     app = FastAPI()

     @app.get("/")
     def read_root():
         return {"Hello": "World"}
     ```

3. **What is the purpose of Pydantic in FastAPI?**
   - **Use Case:** Validating and serializing data models in API requests and responses.
   - **Code Example:**
     ```python
     from pydantic import BaseModel

     class Item(BaseModel):
         name: str
         price: float
     ```

4. **How do you define a GET endpoint in FastAPI?**
   - **Use Case:** Creating an endpoint to retrieve data from the server.
   - **Code Example:**
     ```python
     @app.get("/items/{item_id}")
     def read_item(item_id: int):
         return {"item_id": item_id}
     ```

5. **What are path parameters in FastAPI?**
   - **Use Case:** Handling dynamic URL segments to fetch specific resources.
   - **Code Example:**
     ```python
     @app.get("/users/{user_id}")
     def read_user(user_id: int):
         return {"user_id": user_id}
     ```

6. **How do you define query parameters in FastAPI?**
   - **Use Case:** Allowing users to filter or modify responses based on query strings.
   - **Code Example:**
     ```python
     @app.get("/items/")
     def read_items(skip: int = 0, limit: int = 10):
         return {"skip": skip, "limit": limit}
     ```

7. **What is the role of the `@app.post()` decorator?**
   - **Use Case:** Creating endpoints to accept data submissions (e.g., creating new resources).
   - **Code Example:**
     ```python
     @app.post("/items/")
     def create_item(item: Item):
         return {"item_name": item.name, "item_price": item.price}
     ```

8. **How do you return JSON responses in FastAPI?**
   - **Use Case:** Sending structured data back to clients in a standardized format.
   - **Code Example:**
     ```python
     from fastapi.responses import JSONResponse

     @app.get("/json")
     def get_json():
         return JSONResponse(content={"message": "This is a JSON response"})
     ```

9. **What is the difference between synchronous and asynchronous endpoints in FastAPI?**
   - **Use Case:** Understanding performance implications when handling I/O-bound operations.
   - **Code Example:**
     ```python
     @app.get("/sync")
     def sync_endpoint():
         return {"message": "This is a synchronous endpoint"}

     @app.get("/async")
     async def async_endpoint():
         return {"message": "This is an asynchronous endpoint"}
     ```

10. **How do you run a FastAPI application using Uvicorn?**
    - **Use Case:** Deploying the application locally for testing or development.
    - **Code Example:** Run in terminal:
      ```bash
      uvicorn main:app --reload
      ```

### Medium Questions

1. **How does FastAPI handle asynchronous programming?**
   - **Use Case:** Improving performance with non-blocking I/O operations in APIs.
   - **Code Example:**
     ```python
     @app.get("/async")
     async def read_async():
         await some_async_function()
         return {"message": "Async operation completed"}
     ```

2. **What are dependency injections in FastAPI?**
   - **Use Case:** Managing common logic (like authentication) across multiple endpoints.
   - **Code Example:**
     ```python
     from fastapi import Depends

     def get_query_param(q: str = None):
         return q

     @app.get("/items/")
     def read_items(q: str = Depends(get_query_param)):
         return {"query": q}
     ```

3. **How do you implement middleware in FastAPI?**
   - **Use Case:** Adding functionalities like logging or CORS to all requests.
   - **Code Example:**
     ```python
     from starlette.middleware.cors import CORSMiddleware

     app.add_middleware(
         CORSMiddleware,
         allow_origins=["*"],
         allow_credentials=True,
         allow_methods=["*"],
         allow_headers=["*"],
     )
     ```

4. **How can you implement authentication in FastAPI?**
   - **Use Case:** Securing endpoints to restrict access to authorized users only.
   - **Code Example:**
     ```python
     from fastapi.security import OAuth2PasswordBearer

     oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

     @app.get("/users/me")
     async def read_users_me(token: str = Depends(oauth2_scheme)):
         return {"token": token}
     ```

5. **What is the role of the `Depends` function in FastAPI?**
   - **Use Case:** Declaring dependencies for cleaner and more maintainable code.
   - **Code Example:**
     ```python
     from fastapi import Depends

     def common_parameters(q: str = None, skip: int = 0, limit: int = 10):
         return {"q": q, "skip": skip, "limit": limit}

     @app.get("/items/")
     def read_items(commons: dict = Depends(common_parameters)):
         return commons
     ```

6. **How do you handle CORS in FastAPI?**
   - **Use Case:** Allowing cross-origin requests from specific domains for client applications.
   - **Code Example:** (Already shown in middleware example using `CORSMiddleware`)

7. **How do you define a POST endpoint in FastAPI?**
   - **Use Case:** Creating endpoints to accept data submissions from clients.
   - **Code Example:**
     ```python
     @app.post("/items/")
     async def create_item(item: Item):
         return {"item_name": item.name, "item_price": item.price}
     ```

8. **What are response models in FastAPI?**
   - **Use Case:** Defining the structure of responses for better API documentation and validation.
   - **Code Example:**
     ```python
     class ItemResponse(BaseModel):
         name: str
         price: float

     @app.get("/items/{item_id}", response_model=ItemResponse)
     def read_item(item_id: int):
         return ItemResponse(name="Sample Item", price=10.0)
     ```

9. **How can you implement pagination in FastAPI?**
   - **Use Case:** Returning large datasets in smaller, manageable chunks.
   - **Code Example:**
     ```python
     @app.get("/items/")
     def read_items(skip: int = 0, limit: int = 10):
         items = [{"item_id": i} for i in range(100)]  # Simulated data
         return items[skip : skip + limit]
     ```

10. **How do you use FastAPI with SQLAlchemy?**
    - **Use Case:** Integrating with a relational database for data persistence.
    - **Code Example:**
      ```python
      from sqlalchemy import create_engine, Column, Integer, String
      from sqlalchemy.ext.declarative import declarative_base
      from sqlalchemy.orm import sessionmaker

      SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
      engine = create_engine(SQLALCHEMY_DATABASE_URL)
      SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
      Base = declarative_base()

      class User(Base):
          __tablename__ = "users"
          id = Column(Integer, primary_key=True, index=True)
          name = Column(String, index=True)

      Base.metadata.create_all(bind=engine)

      @app.post("/users/")
      def create_user(name: str):
          db = SessionLocal()
          db_user = User(name=name)
          db.add(db_user)
          db.commit()
          db.refresh(db_user)
          return db_user
      ```

### Hard Questions

1. **How can you optimize performance in a FastAPI application?**
   - **Use Case:** Enhancing the speed and efficiency of API responses under load.
   - **Code Example:** Using caching with `fastapi_cache`:
     ```python
     from fastapi_cache import FastAPICache
     from fastapi_cache.backends.redis import RedisBackend

     @app.on_event("startup")
     async def startup():
         redis = await aioredis.from_url("redis://localhost")
         FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

     @app.get("/cached/")
     @fastapi_cache.cached()
     async def get_cached_data():
         return {"data": "This data is cached!"}
     ```

2. **Explain the use of background tasks in FastAPI.**
   - **Use Case:** Performing non-blocking operations like sending emails after a response is returned.
   - **Code Example:**
     ```python
     from fastapi import BackgroundTasks

     def send_email(email: str):
         # Logic to send email
         print(f"Sending email to {email}")

     @app.post("/send/")
     async def send_email_background(email: str, background_tasks: BackgroundTasks):
         background_tasks.add_task(send_email, email)
         return {"message": "Email will be sent in the background."}
     ```

3. **How do you handle errors and exceptions in FastAPI?**
   - **Use Case:** Providing meaningful error messages and handling edge cases gracefully.
   - **Code Example:**
     ```python
     from fastapi import HTTPException

     @app.get("/items/{item_id}")
     def read_item(item_id: int):
         if item_id not in range(10):  # Simulated condition
             raise HTTPException(status_code=404, detail="Item not found")
         return {"item_id": item_id}
     ```

4. **Discuss the scalability of FastAPI applications.**
   - **Use Case:** Planning for traffic spikes and ensuring high availability.
   - **Code Example:** N/A (Conceptual)

5. **How can you implement WebSocket support in FastAPI?**
   - **Use Case:** Enabling real-time communication features in applications.
   - **Code Example:**
     ```python
     from fastapi import WebSocket

     @app.websocket("/ws")
     async def websocket_endpoint(websocket: WebSocket):
         await websocket.accept()
         while True:
             data = await websocket.receive_text()
             await websocket.send_text(f"Message text was: {data}")
     ```

6. **What strategies can you use for API versioning in FastAPI?**
   - **Use Case:** Maintaining backward compatibility while introducing new features.
   - **Code Example:**
     ```python
     @app.get("/v1/items/")
     def read_items_v1():
         return [{"item": "item_v1"}]

     @app.get("/v2/items/")
     def read_items_v2():
         return [{"item": "item_v2", "description": "New version item"}]
     ```

7. **How do you write custom middleware for logging requests and responses?**
   - **Use Case:** Monitoring API usage and performance for analytics.
   - **Code Example:**
     ```python
     from starlette.middleware.base import BaseHTTPMiddleware

     class LoggingMiddleware(BaseHTTPMiddleware):
         async def dispatch(self, request, call_next):
             print(f"Request: {request.method} {request.url}")
             response = await call_next(request)
             print(f"Response: {response.status_code}")
             return response

     app.add_middleware(LoggingMiddleware)
     ```

8. **How can you deploy FastAPI applications using Docker?**
   - **Use Case:** Containerizing applications for consistent deployment across environments.
   - **Code Example:** Dockerfile:
     ```Dockerfile
     FROM python:3.9

     WORKDIR /app
     COPY . /app

     RUN pip install fastapi uvicorn

     CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
     ```

9. **What are the best practices for securing FastAPI applications?**
   - **Use Case:** Protecting sensitive data and ensuring user privacy.
   - **Code Example:** Using HTTPS and validating JWT tokens for authentication.

10. **How can you integrate FastAPI with message brokers like RabbitMQ or Kafka?**
    - **Use Case:** Implementing asynchronous processing and decoupling services for better scalability.
    - **Code Example (with RabbitMQ):**
      ```python
      import aio_pika

      async def publish_message(message: str):
          connection = await aio_pika.connect_robust("amqp://user:password@localhost/")
          async with connection:
              channel = await connection.channel()
              await channel.default_exchange.publish(
                  aio_pika.Message(body=message.encode()),
                  routing_key="task_queue",
              )

      @app.post("/publish/")
      async def publish(message: str):
          await publish_message(message)
          return {"message": "Message published to RabbitMQ"}
      ```

Feel free to ask if you need more details or examples!