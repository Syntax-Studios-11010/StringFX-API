package main

import (
	"bytes"
	"fmt"
	"io"
	"log"
	"net/http"
)

// The URL where our Python service will be running inside Docker
const pythonServiceURL = "http://processor-python:8001/v1/process"

func main() {
	// Route all requests sent to /process over to our handler
	http.HandleFunc("/process", handleProcess)

	fmt.Println("🚀 StringFX Go Gateway running on port 8080...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func handleProcess(w http.ResponseWriter, r *http.Request) {
	// 1. Only allow POST requests
	if r.Method != http.MethodPost {
		http.Error(w, "Method not allowed. Use POST.", http.StatusMethodNotAllowed)
		return
	}

	// 2. Read the body payload sent by the user/client
	body, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "Failed to read request body", http.StatusInternalServerError)
		return
	}

	// 3. Forward the exact payload to the Python processing engine
	resp, err := http.Post(pythonServiceURL, "application/json", bytes.NewBuffer(body))
	if err != nil {
		http.Error(w, "Python Processor service is currently unreachable", http.StatusBadGateway)
		return
	}
	defer resp.Body.Close()

	// 4. Read the transformed result back from Python
	respBody, err := io.ReadAll(resp.Body)
	if err != nil {
		http.Error(w, "Failed to read response from Python processor", http.StatusInternalServerError)
		return
	}

	// 5. Send the finished result back to your friend/client!
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(resp.StatusCode)
	w.Write(respBody)
}