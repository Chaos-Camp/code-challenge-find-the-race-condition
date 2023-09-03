## Code Challenge: Expose Race Conditions

**Objective:** Your mission, should you choose to accept it, is to write a series of tests targeting our given environment to expose potential race conditions. After testing, provide a detailed report on the discovered vulnerabilities and how you found them.

## Running the Test Server using Docker

Before diving into the challenge, you must set up and run the provided test server. Ensure you have both Docker and Docker-compose installed on your machine.

### Building the Docker Image:

1. Navigate to the directory containing the `Dockerfile` and other server files.
2. Build the Docker image with the following command:
```bash
docker build -t test-server-image .
```

### Running the Test Server:

1. After building the image, start the test server using:
```bash
docker run -p 8000:8000 test-server-image
```
2. The FastAPI application should be accessible at `http://localhost:8000` from your host machine.
### Challenge Details:

1. **Set Up the Environment** using the provided Docker file and instructions above.
2. **Develop the Tests:** Use any testing tools/frameworks you prefer. Race conditions often require many requests in quick succession or a particular sequence. Your tests should reproduce race conditions reliably.
3. **Report:** For each discovered race condition, provide:
   - A description of the vulnerability.
   - Steps to reproduce it.
   - Potential risks associated with the vulnerability.
   - Relevant code snippets or scripts used during testing.
   - Additional notes or observations.


Your submission will be evaluated based on your testing thoroughness, the clarity of your report, and your ability to discover and reproduce race conditions.

