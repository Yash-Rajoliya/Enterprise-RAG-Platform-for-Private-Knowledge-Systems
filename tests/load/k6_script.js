import http from "k6/http";

export default function () {
  http.post(
    "http://localhost:8000/v1/query",
    JSON.stringify({
      query: "What is enterprise RAG?"
    }),
    {
      headers: {
        "Content-Type": "application/json"
      }
    }
  );
}